from __future__ import annotations

import argparse
import base64
import json
import platform as host_platform
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_DIR = ROOT / "activities" / "python" / "py2-activity-b-input-somma-001"
ACTIVITY_PATH = ACTIVITY_DIR / "activity.json"
STARTER_PATH = ACTIVITY_DIR / "starter" / "main.py"
WORKSPACE_NAME = "python-docente-m04-vm-gui-rehearsal"
RELEASE_LOCK = Path("packer/classroom-releases.lock.json")
EXPECTED_ACTIVE_RELEASE = "1.0.0"
EXPECTED_HOSTS = {
    ("windows", "amd64"): ("windows-amd64-virtualbox", "virtualbox", "x86_64"),
    ("windows", "x86_64"): ("windows-amd64-virtualbox", "virtualbox", "x86_64"),
    ("darwin", "arm64"): ("macos-arm64-vmware", "vmware_desktop", "aarch64"),
    ("darwin", "aarch64"): ("macos-arm64-vmware", "vmware_desktop", "aarch64"),
}

GUEST_RUNNER = r'''from __future__ import annotations

import base64
import json
from pathlib import Path
import subprocess
import sys

payload = base64.b64decode(sys.argv[1].encode("ascii"))
completed = subprocess.run(
    [sys.executable, "main.py"],
    input=payload,
    capture_output=True,
    cwd=Path(__file__).resolve().parent,
    timeout=10,
    check=False,
)
print(json.dumps({
    "returncode": completed.returncode,
    "stdout_b64": base64.b64encode(completed.stdout).decode("ascii"),
    "stderr_b64": base64.b64encode(completed.stderr).decode("ascii"),
}, sort_keys=True))
'''


def fail(message: str) -> None:
    raise RuntimeError(message)


def clean_arch(value: str) -> str:
    return str(value or "").strip().lower()


def current_target() -> tuple[str, str, str]:
    system = host_platform.system().strip().lower()
    machine = clean_arch(host_platform.machine())
    target = EXPECTED_HOSTS.get((system, machine))
    if target is None:
        fail(
            "Host non supportato per il rehearsal vm-gui: "
            f"system={system!r}, machine={machine!r}. "
            "Sono ammessi Windows amd64/VirtualBox e macOS Apple Silicon/VMware."
        )
    return target


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(f"JSON non leggibile {path}: {error}")
    if not isinstance(value, dict):
        fail(f"JSON non-oggetto: {path}")
    return value


def run(command: list[str], *, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and completed.returncode != 0:
        fail(
            f"Comando fallito ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )
    return completed


def verify_active_release(platform: Path, target_id: str, provider: str) -> dict[str, Any]:
    lock = load_json(platform / RELEASE_LOCK)
    if lock.get("schema_version") != "2cornot2c.classroom-release-lock.v1":
        fail("Schema classroom release lock inatteso")
    targets = lock.get("targets")
    if not isinstance(targets, dict):
        fail("classroom release lock senza targets")
    target = targets.get(target_id)
    if not isinstance(target, dict):
        fail(f"Target {target_id} assente dal classroom release lock")
    if target.get("provider") != provider:
        fail(f"Provider release lock inatteso per {target_id}: {target.get('provider')!r}")
    active = target.get("active_release")
    if not isinstance(active, dict):
        fail(f"Nessuna active_release per {target_id}")
    if active.get("version") != EXPECTED_ACTIVE_RELEASE:
        fail(
            f"Release classroom attiva inattesa per {target_id}: "
            f"{active.get('version')!r}; attesa {EXPECTED_ACTIVE_RELEASE}"
        )
    manifest_sha = str(active.get("manifest_sha256") or "")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest_sha):
        fail(f"manifest_sha256 non valido per {target_id}")
    return active


def selected_box(platform: Path, provider: str) -> str:
    provider_file = platform / ".classroom-provider"
    box_file = platform / ".classroom-box"
    if not provider_file.is_file() or not box_file.is_file():
        fail(
            "Classroom box non configurata. Sul vero host usa prima il percorso "
            "'Ambiente 2cornot2c' -> 'Installa, completa o ripara'."
        )
    selected_provider = provider_file.read_text(encoding="utf-8").strip()
    box = box_file.read_text(encoding="utf-8").strip()
    if selected_provider != provider:
        fail(f"Provider configurato {selected_provider!r}, atteso {provider!r}")
    if not re.fullmatch(r"[A-Za-z0-9._-]+/[A-Za-z0-9._-]+", box):
        fail(f"Nome box non valido: {box!r}")
    return box


def parse_box_list_machine_readable(output: str) -> set[tuple[str, str]]:
    records: dict[str, dict[str, str]] = {}
    for raw_line in output.splitlines():
        parts = raw_line.split(",", 3)
        if len(parts) != 4:
            continue
        _, target, kind, data = parts
        if kind not in {"box-name", "box-provider"}:
            continue
        records.setdefault(target, {})[kind] = data.strip()
    return {
        (record["box-name"], record["box-provider"])
        for record in records.values()
        if "box-name" in record and "box-provider" in record
    }


def verify_installed_box(vagrant: str, platform: Path, box: str, provider: str) -> None:
    completed = run([vagrant, "box", "list", "--machine-readable"], cwd=platform)
    installed = parse_box_list_machine_readable(completed.stdout)
    if (box, provider) not in installed:
        fail(
            f"Box selezionata non installata con il provider atteso: {box} ({provider}). "
            "Esegui il repair/install dell'Ambiente 2cornot2c prima del rehearsal."
        )


def load_cases() -> list[dict[str, str]]:
    activity = load_json(ACTIVITY_PATH)
    raw_cases = activity.get("test_cases")
    if not isinstance(raw_cases, list) or len(raw_cases) != 3:
        fail("M04 deve avere esattamente tre test_cases")
    cases: list[dict[str, str]] = []
    for item in raw_cases:
        if not isinstance(item, dict):
            fail("test_case M04 non-oggetto")
        name = str(item.get("name") or "")
        stdin = item.get("stdin")
        expected = item.get("expected_stdout")
        if not name or not isinstance(stdin, str) or not isinstance(expected, str):
            fail(f"test_case M04 incompleto: {item!r}")
        cases.append({"name": name, "stdin": stdin, "expected_stdout": expected})
    return cases


def corrected_student_edit(starter: str) -> str:
    needle = "risultato = 0"
    if starter.count(needle) != 1:
        fail("Starter M04 non contiene la singola modifica controllata attesa")
    return starter.replace(needle, "risultato = primo + secondo", 1)


def prepare_workspace(platform: Path, main_source: str) -> Path:
    lab = platform / "lab"
    lab.mkdir(exist_ok=True)
    workspace = lab / WORKSPACE_NAME
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir()
    (workspace / "main.py").write_text(main_source, encoding="utf-8")
    (workspace / "guest_runner.py").write_text(GUEST_RUNNER, encoding="utf-8")
    files = sorted(path.name for path in workspace.iterdir() if path.is_file())
    if files != ["guest_runner.py", "main.py"]:
        fail(f"Workspace rehearsal contiene file inattesi: {files}")
    return workspace


def guest_command(vagrant: str, platform: Path, shell_command: str) -> subprocess.CompletedProcess[str]:
    return run([vagrant, "ssh", "-c", shell_command], cwd=platform)


def guest_profile(vagrant: str, platform: Path, expected_machine: str) -> dict[str, str]:
    script = (
        "python3 -c 'import platform,sys,json; "
        "print(json.dumps({\"python\": platform.python_version(), "
        "\"machine\": platform.machine(), \"executable\": sys.executable}))'"
    )
    completed = guest_command(vagrant, platform, script)
    lines = [line.strip() for line in completed.stdout.splitlines() if line.strip().startswith("{")]
    if not lines:
        fail(f"Profilo guest non leggibile: {completed.stdout!r}")
    profile = json.loads(lines[-1])
    if not isinstance(profile, dict):
        fail("Profilo guest non-oggetto")
    python_version = str(profile.get("python") or "")
    machine = clean_arch(str(profile.get("machine") or ""))
    if not python_version.startswith("3.12."):
        fail(f"Python guest inatteso: {python_version!r}; richiesto 3.12.x")
    if machine != expected_machine:
        fail(f"Architettura guest inattesa: {machine!r}; attesa {expected_machine!r}")

    gui = guest_command(
        vagrant,
        platform,
        "systemctl is-active graphical.target && systemctl is-active lightdm",
    )
    gui_lines = [line.strip() for line in gui.stdout.splitlines() if line.strip()]
    if gui_lines[-2:] != ["active", "active"]:
        fail(f"Sessione grafica guest non attiva: {gui.stdout!r}")
    return {"python": python_version, "machine": machine, "gui": "active"}


def run_cases_in_guest(
    vagrant: str,
    platform: Path,
    cases: list[dict[str, str]],
) -> tuple[int, list[dict[str, Any]]]:
    passed = 0
    evidence: list[dict[str, Any]] = []
    guest_dir = f"/lab/{WORKSPACE_NAME}"
    for case in cases:
        encoded = base64.b64encode(case["stdin"].encode("utf-8")).decode("ascii")
        completed = guest_command(
            vagrant,
            platform,
            f"cd {guest_dir} && python3 guest_runner.py {encoded}",
        )
        payload_lines = [
            line.strip() for line in completed.stdout.splitlines() if line.strip().startswith("{")
        ]
        if not payload_lines:
            fail(f"Runner guest senza JSON per {case['name']!r}: {completed.stdout!r}")
        payload = json.loads(payload_lines[-1])
        stdout = base64.b64decode(str(payload["stdout_b64"])).decode("utf-8", errors="replace")
        stderr = base64.b64decode(str(payload["stderr_b64"])).decode("utf-8", errors="replace")
        ok = int(payload["returncode"]) == 0 and stdout == case["expected_stdout"]
        passed += int(ok)
        evidence.append(
            {
                "name": case["name"],
                "passed": ok,
                "returncode": int(payload["returncode"]),
                "stdout": stdout,
                "stderr": stderr,
            }
        )
    return passed, evidence


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Rehearsal M04 dentro la reale classroom vm-gui release attiva di 2cornot2c. "
            "Va eseguito sul vero host Windows amd64/VirtualBox o macOS Apple Silicon/VMware."
        )
    )
    parser.add_argument("--platform", type=Path, required=True, help="Checkout locale di TheBitPoets/2cornot2c")
    parser.add_argument(
        "--keep-workspace",
        action="store_true",
        help="Non rimuovere il piccolo workspace /lab usato dal rehearsal.",
    )
    args = parser.parse_args()

    platform = args.platform.expanduser().resolve(strict=True)
    if not (platform / "Vagrantfile").is_file():
        fail(f"Vagrantfile TheBitLab non trovato in {platform}")

    target_id, provider, expected_machine = current_target()
    active_release = verify_active_release(platform, target_id, provider)
    box = selected_box(platform, provider)
    vagrant = shutil.which("vagrant") or shutil.which("vagrant.exe")
    if not vagrant:
        fail("Vagrant non trovato sul vero host classroom")
    verify_installed_box(vagrant, platform, box, provider)

    starter = STARTER_PATH.read_text(encoding="utf-8")
    corrected = corrected_student_edit(starter)
    cases = load_cases()
    workspace = prepare_workspace(platform, starter)

    try:
        run([vagrant, "up", f"--provider={provider}"], cwd=platform)
        profile = guest_profile(vagrant, platform, expected_machine)

        starter_passed, starter_evidence = run_cases_in_guest(vagrant, platform, cases)
        if starter_passed != 1:
            fail(f"Discriminazione starter inattesa nella VM: {starter_passed}/3")

        (workspace / "main.py").write_text(corrected, encoding="utf-8")
        corrected_passed, corrected_evidence = run_cases_in_guest(vagrant, platform, cases)
        if corrected_passed != 3:
            fail(f"Student edit corretto inatteso nella VM: {corrected_passed}/3")

        report = {
            "schema_version": "python.m04-vm-gui-rehearsal.v1",
            "status": "passed",
            "target_id": target_id,
            "provider": provider,
            "box": box,
            "active_release": active_release["version"],
            "manifest_sha256": active_release["manifest_sha256"],
            "guest": profile,
            "activity_id": "py2-activity-b-input-somma-001",
            "starter_cases": f"{starter_passed}/3",
            "corrected_student_edit_cases": f"{corrected_passed}/3",
            "controlled_change": "risultato = 0 -> risultato = primo + secondo",
            "teacher_oracle_copied_to_guest": False,
            "solution_asset_copied_to_guest": False,
            "starter_evidence": starter_evidence,
            "corrected_evidence": corrected_evidence,
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
    finally:
        if not args.keep_workspace and workspace.exists():
            shutil.rmtree(workspace)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)

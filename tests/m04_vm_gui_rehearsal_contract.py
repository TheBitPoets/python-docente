from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests import m04_vm_gui_rehearsal as rehearsal


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    starter = rehearsal.STARTER_PATH.read_text(encoding="utf-8")
    corrected = rehearsal.corrected_student_edit(starter)
    if corrected == starter:
        fail("La modifica controllata M04 non cambia lo starter")
    if "risultato = primo + secondo" not in corrected:
        fail("La modifica controllata M04 non produce la somma richiesta")
    if corrected.count("risultato = primo + secondo") != 1:
        fail("La modifica controllata M04 deve essere unica")

    guest_runner = rehearsal.GUEST_RUNNER.casefold()
    forbidden_guest_tokens = (
        "expected_stdout",
        "solution/",
        "teacher/",
        "teacher_only",
        "test_cases",
    )
    leaked = [token for token in forbidden_guest_tokens if token in guest_runner]
    if leaked:
        fail(f"Il guest runner espone dettagli docente/oracolo: {leaked}")

    sample = "\n".join(
        [
            "1,,box-name,2cornot2c/classroom-1.0.0",
            "1,,box-provider,virtualbox",
            "1,,box-version,0",
        ]
    )
    parsed = rehearsal.parse_box_list_machine_readable(sample)
    if parsed != {("2cornot2c/classroom-1.0.0", "virtualbox")}:
        fail(f"Parsing box/provider inatteso: {parsed}")

    cases = rehearsal.load_cases()
    if len(cases) != 3:
        fail("Il rehearsal M04 deve mantenere esattamente tre casi")
    if [case["name"] for case in cases] != ["positivi", "zeri", "negativo e positivo"]:
        fail("I casi M04 del rehearsal non coincidono con l'Activity canonica")

    with tempfile.TemporaryDirectory(prefix="m04-vm-gui-human-workspace-") as raw_temp:
        workspace = rehearsal.prepare_workspace(Path(raw_temp), corrected)
        rehearsal.prepare_human_workspace(workspace, starter)
        human_files = sorted(path.name for path in workspace.iterdir() if path.is_file())
        if human_files != ["main.py"]:
            fail(f"Workspace umano non ridotto al solo starter: {human_files}")
        if (workspace / "main.py").read_text(encoding="utf-8") != starter:
            fail("Workspace umano non ripristina lo starter canonico")

    if rehearsal.EXPECTED_ACTIVE_RELEASE != "1.0.0":
        fail("La release vm-gui attesa deve restare esplicita finché non viene ripromossa")
    if set(rehearsal.EXPECTED_HOSTS.values()) != {
        ("windows-amd64-virtualbox", "virtualbox", "x86_64"),
        ("macos-arm64-vmware", "vmware_desktop", "aarch64"),
    }:
        fail("Il rehearsal deve coprire esattamente i due profili vm-gui classroom attivi")

    vmware_environment, vmware_state = rehearsal.vagrant_environment("vmware_desktop")
    if vmware_state != ".vagrant-vmware":
        fail("Il rehearsal VMware deve usare la directory di stato classroom dedicata")
    if vmware_environment.get("VAGRANT_DOTFILE_PATH") != ".vagrant-vmware":
        fail("Il rehearsal VMware non propaga VAGRANT_DOTFILE_PATH")

    previous_vagrant_state = os.environ.get("VAGRANT_DOTFILE_PATH")
    os.environ["VAGRANT_DOTFILE_PATH"] = "unexpected-global-state"
    try:
        virtualbox_environment, virtualbox_state = rehearsal.vagrant_environment("virtualbox")
    finally:
        if previous_vagrant_state is None:
            os.environ.pop("VAGRANT_DOTFILE_PATH", None)
        else:
            os.environ["VAGRANT_DOTFILE_PATH"] = previous_vagrant_state
    if virtualbox_state != ".vagrant" or "VAGRANT_DOTFILE_PATH" in virtualbox_environment:
        fail("Il rehearsal VirtualBox deve isolarsi da una directory Vagrant globale")

    report = rehearsal.build_report(
        course_identity={"commit": "a" * 40, "tracked_files_clean": True},
        platform_identity={"commit": "b" * 40, "tracked_files_clean": True},
        target_id="windows-amd64-virtualbox",
        provider="virtualbox",
        state_directory=".vagrant",
        box="2cornot2c/classroom-1.0.0",
        active_release={"version": "1.0.0", "manifest_sha256": "c" * 64},
        guest={"python": "3.12.13", "machine": "x86_64", "gui": "active"},
        starter_evidence=[],
        corrected_evidence=[],
    )
    scope = report.get("evidence_scope") or {}
    if scope != {
        "technical_vm_gui_execution": "passed",
        "normal_student_launcher_observed": False,
        "human_usability_observed": False,
        "real_school_host_attested": False,
        "teacher_signoff": "pending",
        "classroom_ready": False,
    }:
        fail(f"Boundary delle evidenze vm-gui inatteso: {scope}")
    if report.get("status") != "passed" or len(report.get("limitations") or []) != 3:
        fail("Il report tecnico non conserva stato e limitazioni esplicite")

    with tempfile.TemporaryDirectory(prefix="m04-vm-gui-report-contract-") as raw_temp:
        destination = Path(raw_temp) / "report.json"
        rehearsal.write_report(destination, report)
        if json.loads(destination.read_text(encoding="utf-8")) != report:
            fail("Il report vm-gui persistito non coincide con il payload verificato")
        try:
            rehearsal.write_report(destination, report)
        except RuntimeError:
            pass
        else:
            fail("Il report vm-gui esistente non deve essere sovrascritto")

    print(
        "PASS: M04 vm-gui rehearsal contract — controlled student edit, host-side oracle, "
        "exact profiles, VMware state isolation and non-overstating immutable report"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

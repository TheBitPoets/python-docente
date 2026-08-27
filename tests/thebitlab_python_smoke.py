from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_ROOT = ROOT / "activities" / "python" / "py2-activity-b-input-somma-001"
ACTIVITY = ACTIVITY_ROOT / "activity.json"
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
STUDENT_GUIDE = ACTIVITY_ROOT / "student" / "GUIDA.md"
CONTENT_PACK = ROOT / "content" / "python" / "content-pack.json"
THEBITLAB_REF = "cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0"
RUNNER_TOOLCHAIN_VERSION = "2026.07.1"
RUNNER_IMAGE = (
    "ghcr.io/thebitpoets/2cornot2c-assignment-runner@"
    "sha256:62f0f7b7bc1d48d01b7f8e5fa765e0b43be3622e70a614033b1bb4a4e522e159"
)


def fail(message: str) -> None:
    raise AssertionError(message)


def run_module(
    platform: Path,
    module: str,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, "-m", module, *args]
    return subprocess.run(
        command,
        cwd=platform,
        check=check,
        capture_output=True,
        text=True,
    )


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"{path} non contiene un oggetto JSON")
    return value


def validate_platform_pin(platform: Path) -> None:
    if sys.version_info[:2] != (3, 12):
        fail(
            "TheBitLab M04/P1 certification smoke requires host Python 3.12; "
            f"running {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        )

    revision = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip().lower()
    if revision != THEBITLAB_REF:
        fail(f"TheBitLab checkout mismatch: expected {THEBITLAB_REF}, found {revision}")

    lock_path = platform / "docker" / "assignment-runner" / "toolchain.lock.json"
    lock = load_json(lock_path)
    if lock.get("version") != RUNNER_TOOLCHAIN_VERSION:
        fail(
            "Assignment-runner toolchain version mismatch: "
            f"expected {RUNNER_TOOLCHAIN_VERSION}, found {lock.get('version')!r}"
        )
    if lock.get("immutable_reference") != RUNNER_IMAGE:
        fail(
            "Assignment-runner immutable reference mismatch: "
            f"expected {RUNNER_IMAGE}, found {lock.get('immutable_reference')!r}"
        )


def validate_contracts(platform: Path) -> None:
    sys.path.insert(0, str(platform))
    try:
        from scripts import content_pack_contract, validate_activity

        activity = load_json(ACTIVITY)
        errors = validate_activity.validate_activity(activity, str(ACTIVITY))
        if errors:
            fail("Activity non valida:\n- " + "\n- ".join(errors))

        pack = load_json(CONTENT_PACK)
        errors = content_pack_contract.validate_content_pack(
            pack,
            str(CONTENT_PACK),
            root=ROOT,
        )
        if errors:
            fail("Content Pack non valido:\n- " + "\n- ".join(errors))
    finally:
        try:
            sys.path.remove(str(platform))
        except ValueError:
            pass


def assert_student_scaffold(scaffold: Path) -> None:
    required = {
        "README.md",
        "activity.json",
        "main.py",
        "GUIDA.md",
    }
    actual_files = {
        path.relative_to(scaffold).as_posix()
        for path in scaffold.rglob("*")
        if path.is_file()
    }
    if actual_files != required:
        fail(
            "Student scaffold file surface mismatch: "
            f"missing={sorted(required - actual_files)}, "
            f"unexpected={sorted(actual_files - required)}"
        )

    if (scaffold / "main.py").read_bytes() != STARTER.read_bytes():
        fail("Student scaffold main.py non coincide con lo starter canonico")
    if (scaffold / "GUIDA.md").read_bytes() != STUDENT_GUIDE.read_bytes():
        fail("Student scaffold GUIDA.md non coincide con la guida studente canonica")

    public_activity = load_json(scaffold / "activity.json")
    forbidden_fields = {"test_cases", "rubrica"}
    leaked_fields = forbidden_fields & public_activity.keys()
    if leaked_fields:
        fail(f"Metadata riservati nello scaffold: {sorted(leaked_fields)}")

    public_assets = public_activity.get("assets") or []
    if not isinstance(public_assets, list):
        fail("Student scaffold activity.json assets non è una lista")
    for asset in public_assets:
        if not isinstance(asset, dict) or asset.get("visibility") != "student":
            fail(f"Asset non studente nello scaffold pubblico: {asset!r}")
        if asset.get("type") not in {"starter", "example", "fixture", "visible_test"}:
            fail(f"Tipo asset riservato nello scaffold pubblico: {asset!r}")

    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in (
        "expected_stdout",
        "teacher_only",
        "hidden_test",
        "solution/",
        "teacher/",
    ):
        if marker in serialized:
            fail(f"Marker riservato nello scaffold Activity: {marker}")

    readme = (scaffold / "README.md").read_text(encoding="utf-8")
    if THEBITLAB_REF not in readme:
        fail("Student scaffold README non registra il TheBitLab ref pinned")


def grade_source(
    platform: Path,
    source: Path,
    report: Path,
    *,
    authoritative_docker: bool,
) -> tuple[int, dict]:
    arguments = [
        "--activity",
        str(ACTIVITY),
        "--activity-root",
        str(ACTIVITY_ROOT),
        "--source",
        str(source),
        "--source-root",
        str(ACTIVITY_ROOT),
        "--language",
        "python",
        "--report",
        str(report),
    ]
    if authoritative_docker:
        arguments.extend(
            [
                "--docker",
                "--docker-image",
                RUNNER_IMAGE,
                "--toolchain-version",
                RUNNER_TOOLCHAIN_VERSION,
                "--toolchain-reference",
                RUNNER_IMAGE,
            ]
        )

    result = run_module(
        platform,
        "scripts.grade_activity",
        *arguments,
        check=False,
    )
    if not report.is_file():
        fail(
            "grade_activity non ha scritto il report; "
            f"mode={'docker' if authoritative_docker else 'host'}, "
            f"exit={result.returncode}, stdout={result.stdout!r}, stderr={result.stderr!r}"
        )
    loaded = load_json(report)
    if authoritative_docker:
        if loaded.get("toolchain_version") != RUNNER_TOOLCHAIN_VERSION:
            fail(f"Docker report senza toolchain version pinned: {loaded}")
        if loaded.get("toolchain_reference") != RUNNER_IMAGE:
            fail(f"Docker report senza immutable toolchain reference: {loaded}")
    return result.returncode, loaded


def assert_solution_and_starter(
    platform: Path,
    temp: Path,
    *,
    authoritative_docker: bool,
) -> None:
    solution_exit, solution_report = grade_source(
        platform,
        SOLUTION,
        temp / "solution-report.json",
        authoritative_docker=authoritative_docker,
    )
    if solution_exit != 0 or solution_report.get("passed") is not True:
        fail(
            "La soluzione non passa: "
            f"exit={solution_exit}, report={solution_report}"
        )
    summary = solution_report.get("summary") or {}
    if summary.get("passed") != 3 or summary.get("total") != 3:
        fail(f"Riepilogo soluzione inatteso: {summary}")

    starter_exit, starter_report = grade_source(
        platform,
        STARTER,
        temp / "starter-report.json",
        authoritative_docker=authoritative_docker,
    )
    if starter_exit == 0 or starter_report.get("passed") is True:
        fail(
            "Lo starter passa tutti i test: i test non discriminano "
            "la modifica richiesta"
        )
    starter_summary = starter_report.get("summary") or {}
    if starter_summary.get("total") != 3:
        fail(f"Lo starter non ha eseguito i tre test: {starter_summary}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    parser.add_argument(
        "--authoritative-docker",
        action="store_true",
        help="Exercise the immutable assignment-runner Docker toolchain instead of host grading.",
    )
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
    validate_platform_pin(platform)
    validate_contracts(platform)

    with tempfile.TemporaryDirectory(prefix="python-docente-smoke-") as raw_temp:
        temp = Path(raw_temp)
        target = temp / "student-repo"
        target.mkdir()
        run_module(
            platform,
            "scripts.create_submission_scaffold",
            "--activity",
            str(ACTIVITY),
            "--target",
            str(target),
            "--thebitlab-ref",
            THEBITLAB_REF,
        )
        scaffold = target / "assignments" / "py2-activity-b-input-somma-001"
        if not scaffold.is_dir():
            fail(f"Scaffold non creato: {scaffold}")
        assert_student_scaffold(scaffold)
        assert_solution_and_starter(
            platform,
            temp,
            authoritative_docker=args.authoritative_docker,
        )

    mode = "immutable Docker grading" if args.authoritative_docker else "host Python grading"
    print(
        "PASS: pinned Content Pack + Activity + exact student scaffold + "
        f"Python starter/solution deterministic grading ({mode})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

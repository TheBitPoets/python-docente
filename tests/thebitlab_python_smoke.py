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
CONTENT_PACK = ROOT / "content" / "python" / "content-pack.json"
THEBITLAB_REF = "cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0"


def fail(message: str) -> None:
    raise AssertionError(message)


def run_module(platform: Path, module: str, *args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, "-m", module, *args]
    return subprocess.run(
        command,
        cwd=platform,
        check=True,
        capture_output=True,
        text=True,
    )


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"{path} non contiene un oggetto JSON")
    return value


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
    missing = required - actual_files
    if missing:
        fail(f"Scaffold senza file richiesti: {sorted(missing)}")

    forbidden_parts = {"teacher", "solution", "tests", "hidden_tests"}
    for relative in actual_files:
        parts = {part.casefold() for part in Path(relative).parts}
        if parts & forbidden_parts:
            fail(f"Leakage teacher/solution nello scaffold: {relative}")

    public_activity = load_json(scaffold / "activity.json")
    forbidden_fields = {
        "test_cases",
        "rubrica",
    }
    leaked_fields = forbidden_fields & public_activity.keys()
    if leaked_fields:
        fail(f"Metadata riservati nello scaffold: {sorted(leaked_fields)}")

    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in ("expected_stdout", "teacher_only", "hidden_test", "solution/"):
        if marker in serialized:
            fail(f"Marker riservato nello scaffold Activity: {marker}")


def grade_source(platform: Path, source: Path, report: Path) -> dict:
    run_module(
        platform,
        "scripts.grade_activity",
        "--activity",
        str(ACTIVITY),
        "--source",
        str(source),
        "--language",
        "python",
        "--report",
        str(report),
    )
    return load_json(report)


def assert_solution_and_starter(platform: Path, temp: Path) -> None:
    solution_report = grade_source(platform, SOLUTION, temp / "solution-report.json")
    if solution_report.get("passed") is not True:
        fail(f"La soluzione non passa: {solution_report}")
    summary = solution_report.get("summary") or {}
    if summary.get("passed") != 3 or summary.get("total") != 3:
        fail(f"Riepilogo soluzione inatteso: {summary}")

    starter_report = grade_source(platform, STARTER, temp / "starter-report.json")
    if starter_report.get("passed") is True:
        fail("Lo starter passa tutti i test: i test non discriminano la modifica richiesta")
    starter_summary = starter_report.get("summary") or {}
    if starter_summary.get("total") != 3:
        fail(f"Lo starter non ha eseguito i tre test: {starter_summary}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
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
        assert_solution_and_starter(platform, temp)

    print(
        "PASS: Content Pack + Activity + scaffold visibility + "
        "Python starter/solution deterministic grading"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

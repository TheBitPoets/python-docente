from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "p2-canary-profile.json"
PROFILE = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
ACTIVITY = ROOT / str(PROFILE["activity_path"])
ACTIVITY_ROOT = ACTIVITY.parent
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
STUDENT_GUIDE = ACTIVITY_ROOT / "student" / "GUIDA.md"
EXPECTED_FILES = set(PROFILE["student_scaffold_files"])
EXPECTED_CASES = int(PROFILE["expected_cases"])
THEBITLAB_REF = str(PROFILE["thebitlab"]["ref"])
PROFILE_ID = str(PROFILE["thebitlab"]["profile"])


def fail(message: str) -> None:
    raise AssertionError(message)


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"{path}: JSON root non object")
    return value


def run_module(platform: Path, module: str, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", module, *args],
        cwd=platform,
        check=check,
        capture_output=True,
        text=True,
    )


def assert_platform(platform: Path) -> None:
    revision = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip().lower()
    if revision != THEBITLAB_REF:
        fail(f"P2 platform mismatch: expected {THEBITLAB_REF}, found {revision}")

    sys.path.insert(0, str(platform))
    try:
        from scripts import python_function_profile, validate_activity

        if python_function_profile.PROFILE_ID != PROFILE_ID:
            fail(
                f"P2 profile mismatch: expected {PROFILE_ID}, "
                f"found {python_function_profile.PROFILE_ID}"
            )
        activity = load_object(ACTIVITY)
        errors = validate_activity.validate_activity(activity, str(ACTIVITY))
        if errors:
            fail("P2 Activity non valida:\n- " + "\n- ".join(errors))
    finally:
        sys.path.remove(str(platform))


def assert_student_scaffold(platform: Path, temp: Path) -> None:
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
    scaffold = target / "assignments" / PROFILE["activity_id"]
    if not scaffold.is_dir():
        fail(f"Scaffold non creato: {scaffold}")
    files = {
        path.relative_to(scaffold).as_posix()
        for path in scaffold.rglob("*")
        if path.is_file()
    }
    if files != EXPECTED_FILES:
        fail(
            f"P2 scaffold surface mismatch: missing={sorted(EXPECTED_FILES-files)}, "
            f"unexpected={sorted(files-EXPECTED_FILES)}"
        )
    if (scaffold / "main.py").read_bytes() != STARTER.read_bytes():
        fail("P2 scaffold main.py non coincide con lo starter")
    if (scaffold / "GUIDA.md").read_bytes() != STUDENT_GUIDE.read_bytes():
        fail("P2 scaffold GUIDA.md non coincide con la guida")
    public_activity = load_object(scaffold / "activity.json")
    if "function_tests" in public_activity:
        fail("function_tests teacher-only leaked into student scaffold")
    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in ("expected_return", "expected_exception", "rettangolo 3x4", "base zero"):
        if marker in serialized:
            fail(f"P2 teacher oracle leaked into student scaffold: {marker}")


def grade_via_execution_service(platform: Path, source: Path, image: str) -> tuple[object, dict]:
    sys.path.insert(0, str(platform))
    try:
        from scripts.thebitlab_technical_services import (
            DockerGradeActivityExecutionService,
            ExecutionRequest,
        )

        execution = DockerGradeActivityExecutionService().run(
            ExecutionRequest(
                activity_id=PROFILE["activity_id"],
                student_id="p2-canary-student",
                files={"main.py": str(source)},
                language="python",
                timeout_seconds=5,
                metadata={
                    "activity_path": ACTIVITY,
                    "source_path": source,
                    "docker_image": image,
                },
            )
        )
    finally:
        sys.path.remove(str(platform))

    report = execution.metadata.get("runner_report")
    if not isinstance(report, dict):
        fail(
            "P2 normal Docker ExecutionService non ha prodotto runner_report: "
            f"status={execution.status!r}, detail={execution.detail!r}, metadata={execution.metadata!r}"
        )
    if execution.metadata.get("grading_profile") != PROFILE_ID:
        fail(f"P2 ExecutionService non ha dichiarato il profilo atteso: {execution.metadata}")
    return execution, report


def assert_grading(platform: Path, image: str) -> None:
    solution_execution, solution = grade_via_execution_service(platform, SOLUTION, image)
    if solution_execution.status != "passed" or solution.get("passed") is not True:
        fail(
            "P2 solution non passa nel normale ExecutionService: "
            f"status={solution_execution.status}, report={solution}"
        )
    if solution.get("profile") != PROFILE_ID:
        fail(f"P2 solution report profile inatteso: {solution}")
    if solution.get("summary") != {
        "passed": PROFILE["expected_solution_passed"],
        "total": EXPECTED_CASES,
    }:
        fail(f"P2 solution summary inatteso: {solution.get('summary')}")

    starter_execution, starter = grade_via_execution_service(platform, STARTER, image)
    if starter_execution.status != "failed" or starter.get("passed") is True:
        fail(
            "P2 starter non discrimina print vs return nel normale ExecutionService: "
            f"status={starter_execution.status}, report={starter}"
        )
    if starter.get("summary") != {
        "passed": PROFILE["expected_starter_passed"],
        "total": EXPECTED_CASES,
    }:
        fail(f"P2 starter summary inatteso: {starter.get('summary')}")
    if any(test.get("worker_status") != "returned" for test in starter.get("tests", [])):
        fail(f"P2 starter deve eseguire le funzioni e restituire None, non crashare: {starter}")
    if any(test.get("actual_return") is not None for test in starter.get("tests", [])):
        fail(f"P2 starter dovrebbe avere actual_return None: {starter}")
    if not all(str(test.get("stdout", "")).strip().isdigit() for test in starter.get("tests", [])):
        fail(f"P2 starter deve dimostrare che stdout corretto non equivale a return: {starter}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    parser.add_argument("--docker-image", required=True)
    args = parser.parse_args()

    if sys.version_info[:2] != tuple(int(part) for part in PROFILE["host_python"].split(".")):
        fail(
            f"P2 consumer richiede host Python {PROFILE['host_python']}; "
            f"found {sys.version_info.major}.{sys.version_info.minor}"
        )
    platform = args.platform.resolve(strict=True)
    assert_platform(platform)
    with tempfile.TemporaryDirectory(prefix="python-docente-p2-") as raw_temp:
        temp = Path(raw_temp)
        assert_student_scaffold(platform, temp)
    assert_grading(platform, args.docker_image)

    print(
        "PASS: M13 P2 canary validates candidate Activity/scaffold and proves "
        "print stdout != function return through the normal Docker ExecutionService"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

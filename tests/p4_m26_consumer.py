from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / "config" / "p4-canary-profile.json").read_text(encoding="utf-8"))
ACTIVITY = ROOT / PROFILE["activity_path"]
ACTIVITY_ROOT = ACTIVITY.parent
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
GRADING_FIXTURE = ACTIVITY_ROOT / "fixtures" / "misure.txt"
EXPECTED_FILES = set(PROFILE["student_scaffold_files"])
THEBITLAB_REF = PROFILE["thebitlab"]["ref"]
PROFILE_ID = PROFILE["thebitlab"]["profile"]


def fail(message: str) -> None:
    raise AssertionError(message)


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"{path}: JSON root non object")
    return value


def run_module(platform: Path, module: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", module, *args],
        cwd=platform,
        capture_output=True,
        text=True,
        check=True,
    )


def assert_platform(platform: Path) -> None:
    revision = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip().lower()
    if revision != THEBITLAB_REF:
        fail(f"P4 platform mismatch: expected {THEBITLAB_REF}, found {revision}")
    sys.path.insert(0, str(platform))
    try:
        from scripts import python_filesystem_profile, validate_activity

        if python_filesystem_profile.PROFILE_ID != PROFILE_ID:
            fail(f"P4 profile mismatch: {python_filesystem_profile.PROFILE_ID}")
        errors = validate_activity.validate_activity(load_object(ACTIVITY), str(ACTIVITY))
        if errors:
            fail("P4 Activity non valida:\n- " + "\n- ".join(errors))
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
    files = {
        path.relative_to(scaffold).as_posix()
        for path in scaffold.rglob("*")
        if path.is_file()
    }
    if files != EXPECTED_FILES:
        fail(f"P4 scaffold mismatch: expected={sorted(EXPECTED_FILES)} actual={sorted(files)}")
    if (scaffold / "main.py").read_bytes() != STARTER.read_bytes():
        fail("P4 starter scaffold mismatch")
    if (scaffold / "misure.txt").read_text(encoding="utf-8") != "2\n3\n":
        fail("P4 public sample fixture mismatch")
    public_activity = load_object(scaffold / "activity.json")
    if "filesystem_tests" in public_activity:
        fail("P4 filesystem_tests leaked into student scaffold")
    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in ("fixtures/misure.txt", "36\\n", "expected_artifacts"):
        if marker in serialized:
            fail(f"P4 teacher oracle leaked into scaffold: {marker}")


def run_student_lab(platform: Path, source: Path, image: str, root: Path) -> dict:
    activity_bundle = root / "activities" / PROFILE["activity_id"]
    fixture_dir = activity_bundle / "fixtures"
    fixture_dir.mkdir(parents=True)
    shutil.copy2(ACTIVITY, activity_bundle / "activity.json")
    shutil.copy2(GRADING_FIXTURE, fixture_dir / "misure.txt")

    workspace = (
        root
        / "students"
        / "p4-canary-student"
        / "assignments"
        / PROFILE["activity_id"]
    )
    workspace.mkdir(parents=True)
    shutil.copy2(source, workspace / "main.py")

    assignment = {
        "assignment_id": f"assignment-{PROFILE['activity_id']}",
        "activity_id": PROFILE["activity_id"],
        "student_id": "p4-canary-student",
        "activity": {"path": f"activities/{PROFILE['activity_id']}/activity.json"},
        "workspace": {
            "path": f"students/p4-canary-student/assignments/{PROFILE['activity_id']}"
        },
    }

    sys.path.insert(0, str(platform))
    try:
        from scripts import student_lab_runner

        return student_lab_runner.run_docker_assignment(
            assignment,
            root=root,
            timeout_seconds=5,
            docker_image=image,
        )
    finally:
        sys.path.remove(str(platform))


def assert_student_report_redacted(report: dict) -> None:
    tests = report.get("tests")
    if not isinstance(tests, list) or len(tests) != 1 or not isinstance(tests[0], dict):
        fail(f"P4 student report tests non validi: {tests}")
    test = tests[0]
    passed = report.get("passed") is True
    if test.get("name") != "Test 1":
        fail(f"P4 hidden test name non redatto: {test}")
    if test.get("passed") is not passed:
        fail(f"P4 redacted test outcome incoerente: {test}")
    expected_status = "passed" if passed else "failed"
    if test.get("status") != expected_status:
        fail(f"P4 redacted test status incoerente: {test}")
    message = test.get("message")
    if message is not None:
        allowed_message = "Test non superato: failed" if not passed else ""
        if message != allowed_message:
            fail(f"P4 redacted report contiene messaggio non generico: {test}")

    serialized = json.dumps(report, ensure_ascii=False).casefold()
    for marker in (
        "produce il totale nel file",
        "worker_status",
        "observed_artifacts",
        "checks",
        "fixtures/misure.txt",
        "expected_artifacts",
        '"36\\n"',
    ):
        if marker in serialized:
            fail(f"P4 teacher detail leaked into Student Lab report: {marker}")


def assert_grading(platform: Path, image: str, temp: Path) -> None:
    solution_root = temp / "solution-case"
    solution = run_student_lab(platform, SOLUTION, image, solution_root)
    if solution.get("passed") is not True or solution.get("summary") != {"passed": 1, "total": 1}:
        fail(f"P4 solution non passa nel normale Student Lab: {solution}")
    if solution.get("profile") != PROFILE_ID:
        fail(f"P4 solution non dichiara il profilo atteso: {solution}")
    assert_student_report_redacted(solution)

    starter_root = temp / "starter-case"
    starter = run_student_lab(platform, STARTER, image, starter_root)
    if starter.get("passed") is True or starter.get("summary") != {"passed": 0, "total": 1}:
        fail(f"P4 starter non discrimina stdout vs artifact nel normale Student Lab: {starter}")
    if starter.get("profile") != PROFILE_ID:
        fail(f"P4 starter non dichiara il profilo atteso: {starter}")
    assert_student_report_redacted(starter)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    parser.add_argument("--docker-image", required=True)
    args = parser.parse_args()

    expected_python = tuple(int(part) for part in PROFILE["host_python"].split("."))
    if sys.version_info[:2] != expected_python:
        fail(f"P4 consumer richiede Python {PROFILE['host_python']}")
    platform = args.platform.resolve(strict=True)
    assert_platform(platform)
    with tempfile.TemporaryDirectory(prefix="python-docente-p4-") as raw_temp:
        temp = Path(raw_temp)
        assert_student_scaffold(platform, temp)
        assert_grading(platform, args.docker_image, temp)
    print(
        "PASS: M26 P4 canary validates hidden grading fixture/scaffold and proves "
        "filesystem behavior through the normal redacted Student Lab Docker path"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

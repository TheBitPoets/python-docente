from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / "config" / "p4-canary-profile.json").read_text(encoding="utf-8"))
ACTIVITY = ROOT / PROFILE["activity_path"]
ACTIVITY_ROOT = ACTIVITY.parent
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
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


def grade(platform: Path, source: Path, image: str) -> dict:
    sys.path.insert(0, str(platform))
    try:
        from scripts import grade_python_filesystem_activity

        return grade_python_filesystem_activity.grade_in_docker(
            activity_path=ACTIVITY,
            source_path=source,
            image=image,
            timeout_seconds=5,
            activity_root=ACTIVITY_ROOT,
            source_root=ACTIVITY_ROOT,
        )
    finally:
        sys.path.remove(str(platform))


def assert_grading(platform: Path, image: str) -> None:
    solution = grade(platform, SOLUTION, image)
    if solution.get("passed") is not True or solution.get("summary") != {"passed": 1, "total": 1}:
        fail(f"P4 solution non passa: {solution}")
    test = solution["tests"][0]
    if test.get("worker_status") != "completed":
        fail(f"P4 solution worker status inatteso: {test}")

    starter = grade(platform, STARTER, image)
    if starter.get("passed") is True or starter.get("summary") != {"passed": 0, "total": 1}:
        fail(f"P4 starter non discrimina stdout vs artifact: {starter}")
    test = starter["tests"][0]
    if test.get("worker_status") != "completed":
        fail(f"P4 starter deve completare senza crash: {test}")
    checks = test.get("checks") or []
    if not any(check.get("status") == "missing" and check.get("path") == "risultato.txt" for check in checks):
        fail(f"P4 starter deve fallire per artifact mancante: {test}")
    if "36" not in str(test.get("stdout", "")):
        fail(f"P4 starter deve dimostrare che stdout corretto non equivale ad artifact: {test}")


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
        assert_student_scaffold(platform, Path(raw_temp))
    assert_grading(platform, args.docker_image)
    print(
        "PASS: M26 P4 canary validates hidden grading fixture, redacted scaffold and proves "
        "stdout != required filesystem artifact in authoritative Docker grading"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

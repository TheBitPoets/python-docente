from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform as host_platform
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "p1-canary-profile.json"
ACTIVITY_ROOT = ROOT / "activities" / "python" / "py2-activity-b-input-somma-001"
ACTIVITY = ACTIVITY_ROOT / "activity.json"
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
EXPECTED_FILES = {"README.md", "activity.json", "main.py", "GUIDA.md"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise AssertionError(message)


def load_object(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        fail(f"{path}: expected JSON object")
    return payload


def docker(
    image: str,
    workspace: Path,
    platform_name: str,
    *command: str,
    stdin: str | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--platform",
            platform_name,
            "--volume",
            f"{workspace.resolve()}:/workspace",
            image,
            *command,
        ],
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )


def assert_scaffold(workspace: Path) -> None:
    files = {
        path.relative_to(workspace).as_posix()
        for path in workspace.rglob("*")
        if path.is_file()
    }
    if files != EXPECTED_FILES:
        fail(
            "student workspace surface mismatch: "
            f"missing={sorted(EXPECTED_FILES - files)}, "
            f"unexpected={sorted(files - EXPECTED_FILES)}"
        )

    public_activity = load_object(workspace / "activity.json")
    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in (
        "expected_stdout",
        "test_cases",
        "teacher/",
        "solution/",
        "hidden_test",
        "teacher_only",
    ):
        if marker in serialized:
            fail(f"reserved marker leaked into public scaffold: {marker}")


def assert_image_identity(image: str, expected_source: str, expected_version: str) -> None:
    result = subprocess.run(
        [
            "docker",
            "inspect",
            "--format",
            "{{json .Config.Labels}}",
            image,
        ],
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )
    if result.returncode != 0:
        fail(f"docker inspect failed: {result.stderr}")
    labels = json.loads(result.stdout)
    if labels.get("org.opencontainers.image.revision") != expected_source:
        fail(f"student-dev source label mismatch: {labels}")
    if labels.get("org.opencontainers.image.version") != expected_version:
        fail(f"student-dev version label mismatch: {labels}")


def assert_environment(image: str, workspace: Path, platform_name: str, expected_machine: str) -> None:
    probe = docker(
        image,
        workspace,
        platform_name,
        "sh",
        "-eu",
        "-c",
        (
            'test "$(id -u)" = 1000; '
            'test "$(id -un)" = student; '
            f'test "$(uname -m)" = "{expected_machine}"; '
            'python3 -c "import sys; assert sys.version_info[:2] == (3, 12); print(sys.version.split()[0])"; '
            'git --version; '
            'printf classroom-write-ok > /workspace/.classroom-write-probe; '
            'test "$(cat /workspace/.classroom-write-probe)" = classroom-write-ok; '
            'rm /workspace/.classroom-write-probe'
        ),
    )
    if probe.returncode != 0:
        fail(
            "docker-light environment probe failed: "
            f"stdout={probe.stdout!r}, stderr={probe.stderr!r}"
        )


def exercise(
    image: str,
    workspace: Path,
    platform_name: str,
    cases: list[dict],
) -> tuple[int, int]:
    passed = 0
    executed = 0
    for case in cases:
        result = docker(
            image,
            workspace,
            platform_name,
            "python3",
            "/workspace/main.py",
            stdin=str(case["stdin"]),
        )
        executed += 1
        if result.returncode != 0:
            fail(
                f"{case['name']}: student program failed: "
                f"exit={result.returncode}, stderr={result.stderr!r}"
            )
        if result.stderr:
            fail(f"{case['name']}: unexpected stderr={result.stderr!r}")
        if result.stdout == str(case["expected_stdout"]):
            passed += 1
    return passed, executed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--platform", required=True, choices=["linux/amd64", "linux/arm64"])
    parser.add_argument("--starter-workspace", type=Path, required=True)
    parser.add_argument("--solution-workspace", type=Path, required=True)
    args = parser.parse_args()

    profile = load_object(PROFILE_PATH)
    classroom = profile.get("classroom_environment") or {}
    source = str(classroom.get("source_revision") or "")
    version = str(classroom.get("student_dev_version") or "")
    if not SHA_RE.fullmatch(source):
        fail(f"invalid classroom source revision: {source!r}")

    expected_platforms = classroom.get("platforms")
    if expected_platforms != ["linux/amd64", "linux/arm64"]:
        fail(f"unexpected classroom platforms: {expected_platforms!r}")
    machine_map = classroom.get("machine_names") or {}
    expected_machine = str(machine_map.get(args.platform) or "")
    if not expected_machine:
        fail(f"missing machine name for {args.platform}")

    starter_workspace = args.starter_workspace.resolve(strict=True)
    solution_workspace = args.solution_workspace.resolve(strict=True)
    assert_scaffold(starter_workspace)
    assert_scaffold(solution_workspace)
    if (starter_workspace / "main.py").read_bytes() != STARTER.read_bytes():
        fail("starter classroom workspace does not contain canonical starter main.py")
    if (solution_workspace / "main.py").read_bytes() != SOLUTION.read_bytes():
        fail("edited classroom workspace does not contain the expected corrected main.py")

    activity = load_object(ACTIVITY)
    cases = activity.get("test_cases")
    if not isinstance(cases, list) or len(cases) != 3:
        fail(f"M04 requires exactly 3 deterministic cases: {cases!r}")

    assert_image_identity(args.image, source, version)
    assert_environment(args.image, starter_workspace, args.platform, expected_machine)

    starter_passed, starter_executed = exercise(
        args.image,
        starter_workspace,
        args.platform,
        cases,
    )
    if starter_executed != 3 or starter_passed == 3:
        fail(
            "starter discrimination failed in docker-light: "
            f"passed={starter_passed}, executed={starter_executed}"
        )

    solution_passed, solution_executed = exercise(
        args.image,
        solution_workspace,
        args.platform,
        cases,
    )
    if solution_executed != 3 or solution_passed != 3:
        fail(
            "edited solution failed in docker-light: "
            f"passed={solution_passed}, executed={solution_executed}"
        )

    print(
        "PASS: M04 docker-light classroom profile — "
        f"platform={args.platform}, machine={expected_machine}, "
        f"starter={starter_passed}/3, edited=3/3, "
        f"student-dev={version}, source={source}, host={host_platform.system()}"
    )
    print(
        "NOTE: this is technical profile evidence; it does not replace the final "
        "human rehearsal on a real classroom host."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

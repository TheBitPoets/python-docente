from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "p1-canary-profile.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "thebitlab-python-smoke.yml"
SMOKE_PATH = ROOT / "tests" / "thebitlab_python_smoke.py"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
IMAGE_RE = re.compile(
    r"^ghcr\.io/thebitpoets/2cornot2c-assignment-runner@sha256:[0-9a-f]{64}$"
)
LOCAL_IMAGE_RE = re.compile(r"^thebitlab-assignment-runner:p1-canary-[0-9]{4}\.[0-9]{2}\.[1-9][0-9]*$")


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.relative_to(ROOT)}: JSON root must be object")
    return value


def main() -> int:
    profile = load_object(PROFILE_PATH)
    assert profile.get("schema_version") == "python.p1-canary-certification.v1"
    assert profile.get("activity_id") == "py2-activity-b-input-somma-001"
    assert profile.get("host_python") == "3.12"
    assert profile.get("host_os") == ["ubuntu-latest", "windows-latest"]
    assert profile.get("expected_cases") == 3
    assert profile.get("student_scaffold_files") == [
        "README.md",
        "activity.json",
        "main.py",
        "GUIDA.md",
    ]

    activity_path = ROOT / str(profile["activity_path"])
    activity = load_object(activity_path)
    assert activity.get("id") == profile["activity_id"]
    assert len(activity.get("test_cases") or []) == profile["expected_cases"]

    thebitlab = profile.get("thebitlab") or {}
    assert thebitlab.get("repository") == "TheBitPoets/2cornot2c"
    assert isinstance(thebitlab.get("ref"), str) and SHA_RE.fullmatch(thebitlab["ref"])

    grading = profile.get("authoritative_grading") or {}
    assert grading.get("required") is True
    assert grading.get("host_os") == "ubuntu-latest"
    assert grading.get("platform") == "linux/amd64"
    assert grading.get("toolchain_version") == "2026.07.1"
    assert grading.get("build_strategy") == "build-from-pinned-runner-source"
    assert isinstance(grading.get("runner_source_revision"), str)
    assert SHA_RE.fullmatch(grading["runner_source_revision"])
    assert isinstance(grading.get("local_image_tag"), str)
    assert LOCAL_IMAGE_RE.fullmatch(grading["local_image_tag"])
    assert isinstance(grading.get("release_lock_reference"), str)
    assert IMAGE_RE.fullmatch(grading["release_lock_reference"])

    policy = profile.get("certification_policy") or {}
    assert policy.get("direct_preflight_is_authoritative_grading") is False
    assert policy.get("host_smoke_required_on_all_host_os") is True
    assert policy.get("docker_grading_required_once") is True
    assert policy.get("published_ghcr_artifact_required_for_ci") is False
    assert policy.get("classroom_rehearsal_required") is True

    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert 'python-version: "3.12"' in workflow
    assert "os: [ubuntu-latest, windows-latest]" in workflow
    assert str(thebitlab["ref"]) in workflow
    assert str(grading["runner_source_revision"]) in workflow
    assert "scripts/build_assignment_runner.py" in workflow
    assert "--authoritative-docker" in workflow
    assert "--docker-image" in workflow
    assert "runner.os == 'Linux'" in workflow

    smoke = SMOKE_PATH.read_text(encoding="utf-8")
    assert "p1-canary-profile.json" in smoke
    assert "--authoritative-docker" in smoke
    assert "--docker-image" in smoke
    assert "--toolchain-version" in smoke
    assert "--toolchain-reference" in smoke

    print(
        "PASS: M04/P1 certification profile pins Python 3.12, Ubuntu+Windows, "
        "TheBitLab consumer SHA and source-built Docker grading toolchain"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

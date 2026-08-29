from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P2_PATH = ROOT / "config" / "p2-canary-profile.json"
P4_PATH = ROOT / "config" / "p4-canary-profile.json"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"{path}: root JSON must be object"
    return value


def main() -> int:
    p2 = load(P2_PATH)
    p4 = load(P4_PATH)

    assert p2["thebitlab"]["repository"] == p4["thebitlab"]["repository"] == "TheBitPoets/2cornot2c"
    assert p2["thebitlab"]["ref"] == p4["thebitlab"]["ref"]
    assert p2["thebitlab"]["pr"] == p4["thebitlab"]["pr"] == 766
    assert p2["thebitlab"]["profile"] == "python-function-v1"
    assert p4["thebitlab"]["profile"] == "python-filesystem-v1"
    assert p2["thebitlab"]["feature_pr"] == 763
    assert p4["thebitlab"]["feature_pr"] == 764

    p2_grading = p2["authoritative_grading"]
    p4_grading = p4["authoritative_grading"]
    assert p2_grading["strategy"] == p4_grading["strategy"] == "source-build-from-exact-combined-release-candidate"
    assert p2_grading["platform"] == p4_grading["platform"] == "linux/amd64"
    assert p2_grading["toolchain_version"] == p4_grading["toolchain_version"] == "2026.08.2"
    assert p2_grading["local_image_tag"] == p4_grading["local_image_tag"] == "thebitlab-python-grading-canaries"

    for profile in (p2, p4):
        policy = profile["certification_policy"]
        assert policy["candidate_profile_only"] is True
        assert policy["mass_activity_materialization_allowed"] is False
        assert policy["normal_student_lab_dispatch_certified"] is True
        assert policy["immutable_release_lock_required_before_stable"] is True
        assert policy["combined_p2_p4_toolchain_required"] is True

    print(
        "PASS: P2 and P4 course canaries share one exact 2026.08.2 combined "
        f"TheBitLab candidate {p2['thebitlab']['ref']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P2_PATH = ROOT / "config" / "p2-canary-profile.json"
P3_PATH = ROOT / "config" / "p3-canary-profile.json"
P4_PATH = ROOT / "config" / "p4-canary-profile.json"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"{path}: root JSON must be object"
    return value


def main() -> int:
    p2 = load(P2_PATH)
    p3 = load(P3_PATH)
    p4 = load(P4_PATH)
    profiles = (p2, p3, p4)

    assert {profile["thebitlab"]["repository"] for profile in profiles} == {
        "TheBitPoets/2cornot2c"
    }
    assert len({profile["thebitlab"]["ref"] for profile in profiles}) == 1
    assert {profile["thebitlab"]["pr"] for profile in profiles} == {768}
    assert p2["thebitlab"]["profile"] == "python-function-v1"
    assert p3["thebitlab"]["profile"] == "python-object-v1"
    assert p4["thebitlab"]["profile"] == "python-filesystem-v1"
    assert p2["thebitlab"]["feature_pr"] == 763
    assert p3["thebitlab"]["issue"] == 758
    assert p4["thebitlab"]["feature_pr"] == 764

    gradings = [profile["authoritative_grading"] for profile in profiles]
    assert {grading["strategy"] for grading in gradings} == {
        "source-build-from-exact-combined-release-candidate"
    }
    assert {grading["platform"] for grading in gradings} == {"linux/amd64"}
    assert {grading["toolchain_version"] for grading in gradings} == {"2026.08.3"}
    assert {grading["release_identity_status"] for grading in gradings} == {
        "combined-release-candidate-not-stable"
    }
    assert {grading["local_image_tag"] for grading in gradings} == {
        "thebitlab-python-grading-canaries"
    }

    for profile in profiles:
        policy = profile["certification_policy"]
        assert policy["candidate_profile_only"] is True
        assert policy["mass_activity_materialization_allowed"] is False
        assert policy["immutable_release_lock_required_before_stable"] is True
        assert policy["combined_p2_p3_p4_toolchain_required"] is True

    ref = p2["thebitlab"]["ref"]
    print(
        "PASS: P2, P3 and P4 course canaries share one exact 2026.08.3 "
        f"TheBitLab release candidate {ref}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

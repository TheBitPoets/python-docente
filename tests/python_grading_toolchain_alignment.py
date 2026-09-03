from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P2_PATH = ROOT / "config" / "p2-canary-profile.json"
P3_PATH = ROOT / "config" / "p3-canary-profile.json"
P4_PATH = ROOT / "config" / "p4-canary-profile.json"

RELEASE_SOURCE = "23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e"
RELEASE_VERSION = "2026.08.3"
RELEASE_DIGEST = "sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51"
IMAGE_REPOSITORY = "ghcr.io/thebitpoets/2cornot2c-assignment-runner"
IMMUTABLE_IMAGE = f"{IMAGE_REPOSITORY}@{RELEASE_DIGEST}"
FALLBACK_STRATEGY = "source-build-from-published-release-source"
ACCESS_STATUS = "ghcr-cross-repository-actions-access-pending"
LOCAL_IMAGE_TAG = "thebitlab-python-grading-stable-source"


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
    assert {profile["thebitlab"]["ref"] for profile in profiles} == {RELEASE_SOURCE}
    assert {profile["thebitlab"]["pr"] for profile in profiles} == {770}
    assert {profile["thebitlab"]["stable_lock_pr"] for profile in profiles} == {771}
    assert p2["thebitlab"]["profile"] == "python-function-v1"
    assert p3["thebitlab"]["profile"] == "python-object-v1"
    assert p4["thebitlab"]["profile"] == "python-filesystem-v1"
    assert p2["thebitlab"]["feature_pr"] == 763
    assert p3["thebitlab"]["issue"] == 758
    assert p4["thebitlab"]["feature_pr"] == 764

    gradings = [profile["authoritative_grading"] for profile in profiles]
    assert {grading["strategy"] for grading in gradings} == {FALLBACK_STRATEGY}
    assert {grading["platform"] for grading in gradings} == {"linux/amd64"}
    assert {grading["toolchain_version"] for grading in gradings} == {RELEASE_VERSION}
    assert {grading["release_identity_status"] for grading in gradings} == {
        "published-immutable-stable"
    }
    assert {grading["image_repository"] for grading in gradings} == {IMAGE_REPOSITORY}
    assert {grading["digest"] for grading in gradings} == {RELEASE_DIGEST}
    assert {grading["immutable_image_reference"] for grading in gradings} == {
        IMMUTABLE_IMAGE
    }
    assert {grading["consumer_image_access_status"] for grading in gradings} == {
        ACCESS_STATUS
    }
    assert {grading["local_image_tag"] for grading in gradings} == {LOCAL_IMAGE_TAG}

    for profile in profiles:
        policy = profile["certification_policy"]
        assert policy["candidate_profile_only"] is False
        assert policy["mass_activity_materialization_allowed"] is False
        assert policy["immutable_release_lock_required_before_stable"] is True
        assert policy["immutable_release_lock_verified"] is True
        assert policy["direct_immutable_image_pull_verified"] is False
        assert policy["combined_p2_p3_p4_toolchain_required"] is True

    print(
        "PASS: P2, P3 and P4 use published TheBitLab 2026.08.3 source "
        f"{RELEASE_SOURCE} with stable digest {RELEASE_DIGEST}; direct GHCR consumer "
        "access remains explicitly pending, so canaries rebuild only that released source"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

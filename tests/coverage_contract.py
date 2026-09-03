from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "curriculum-coverage.json"
PACK = ROOT / "content" / "python" / "content-pack.json"
COVERAGE = ROOT / "doc" / "COVERAGE.md"
FREEZE = ROOT / "doc" / "CURRICULUM_FREEZE_2026_2027.md"


def read(path: Path) -> str:
    assert path.is_file(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    value = json.loads(read(path))
    assert isinstance(value, dict), f"expected object: {path.relative_to(ROOT)}"
    return value


def main() -> None:
    cfg = load(CONFIG)
    pack = load(PACK)
    coverage_md = read(COVERAGE)
    freeze = read(FREEZE)

    assert cfg["schema_version"] == "python.curriculum-coverage.v1"
    assert cfg["course_id"] == "python-secondo-2026-2027"
    assert cfg["curriculum_source"] == "doc/CURRICULUM_FREEZE_2026_2027.md"
    assert cfg["coverage_document"] == "doc/COVERAGE.md"

    axes = cfg["axes"]
    assert axes == [
        "curriculum",
        "editorial",
        "semantic_review",
        "activity",
        "automated_grading",
        "platform_certification",
        "teacher_signoff",
        "classroom_rehearsal",
    ]

    policy = cfg["policy"]
    assert policy["single_completion_percentage_forbidden"] is True
    assert policy["editorial_coverage_implies_activity_coverage"] is False
    assert policy["activity_coverage_implies_automated_grading"] is False
    assert policy["automated_grading_implies_classroom_readiness"] is False

    outcomes = cfg["outcomes"]
    assert len(outcomes) == 25
    ids = [item["id"] for item in outcomes]
    assert ids == list(range(1, 26)), ids

    # Frozen source really exposes the same 25 numbered outcomes.
    for outcome_id in ids:
        assert f"{outcome_id}." in freeze, f"frozen outcome {outcome_id} missing"

    # Every coverage reference must exist. Every canonical Python lesson used by
    # the coverage map must also be a materialized Content Pack content item.
    materialized_paths = {
        str(item.get("path"))
        for item in pack.get("content_items", [])
        if isinstance(item, dict) and item.get("kind") == "module"
    }

    for outcome in outcomes:
        assert outcome["editorial_status"] in {
            "spec",
            "spec-plus-draft-reinforcement",
            "draft",
        }
        refs = outcome["refs"]
        assert refs, f"outcome {outcome['id']} has no coverage refs"
        for rel in refs:
            path = ROOT / rel
            assert path.is_file(), f"outcome {outcome['id']} missing ref {rel}"
            if rel.startswith("content/python/"):
                assert rel in materialized_paths, (
                    f"outcome {outcome['id']} references non-materialized lesson {rel}"
                )

    # PY2-01 is the only intentionally SPEC-only final editorial gap.
    assert outcomes[0]["editorial_status"] == "spec"
    assert outcomes[1]["editorial_status"] == "spec"
    assert outcomes[0]["delivery_status"] == "blocked-flowchart-lab"
    assert outcomes[1]["delivery_status"] == "blocked-flowchart-lab"
    for outcome in outcomes[3:]:
        assert outcome["editorial_status"] == "draft"

    # Do not inflate automated Activity coverage. At the current checkpoint the
    # Content Pack materializes only the M04 P1 canary.
    pack_activity_ids: set[str] = set()
    for item in pack.get("content_items", []):
        if not isinstance(item, dict):
            continue
        for activity_id in item.get("activity_ids") or []:
            pack_activity_ids.add(str(activity_id))

    declared_activity_ids = {
        str(activity_id)
        for outcome in outcomes
        for activity_id in outcome.get("automated_activity_ids") or []
    }

    assert pack_activity_ids == {"py2-activity-b-input-somma-001"}, pack_activity_ids
    assert declared_activity_ids == pack_activity_ids
    assert outcomes[4]["automated_activity_ids"] == ["py2-activity-b-input-somma-001"]

    # Cross-course/application axes never masquerade as numbered Python outcomes.
    git = cfg["cross_course"]["git_g1"]
    assert git["counts_as_python_numbered_outcome"] is False
    assert (ROOT / git["config"]).is_file()

    romeo = cfg["cross_course"]["romeo"]
    assert romeo["hardware_required_for_core"] is False
    assert romeo["runtime_certification_pending"] is True
    assert (ROOT / romeo["mapping"]).is_file()

    # The human-readable document must preserve the axis separation and current
    # truthful checkpoint.
    for phrase in (
        "coverage editoriale ≠ autograding coverage ≠ classroom readiness",
        "Frozen outcomes mapped          25/25",
        "Python Activities materialized  1 canary",
        "Teacher sign-off                pending",
        "Classroom rehearsal             pending",
    ):
        assert phrase in coverage_md, f"coverage document missing: {phrase}"

    print("PASS: 25/25 frozen outcomes mapped without inflating Activity/readiness coverage")


if __name__ == "__main__":
    main()

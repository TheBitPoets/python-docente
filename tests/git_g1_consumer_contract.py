from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "git-g1-consumer.json"
ENVIRONMENT = ROOT / "config" / "course-environment.json"
M14 = ROOT / "content" / "python" / "14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md"
M15 = ROOT / "content" / "python" / "15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md"
M16 = ROOT / "content" / "python" / "16_ASSERT_REGRESSION_TEST_REFACTOR.md"
CHECKPOINT_A = ROOT / "student" / "CHECKPOINT_A.md"
INTEGRATION = ROOT / "tracks" / "secondo" / "GIT_G1_INTEGRATION.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(text: str, *needles: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    assert not missing, f"missing {missing}"


def main() -> None:
    cfg = load_json(CONFIG)
    env = load_json(ENVIRONMENT)

    assert cfg["schema_version"] == "python.git-g1-consumer.v1"
    assert cfg["course_id"] == "python-secondo-2026-2027"

    provider = cfg["provider"]
    assert provider["repository"] == "TheBitPoets/git"
    assert provider["track"] == "G1"
    assert provider["status"] == "freeze-candidate-draft"
    assert len(provider["candidate_ref"]) == 40
    int(provider["candidate_ref"], 16)
    assert provider["contract_path"] == "doc/G1_CONSUMER_CONTRACT.md"
    assert provider["content_pack_path"] == "content/git/content-pack.json"

    required_capability = cfg["environment"]["required_capability"]
    assert required_capability == "git.basic.v1"
    assert required_capability in env["capabilities"]["required"]
    assert cfg["environment"]["network_required"] is False
    assert cfg["environment"]["github_account_required"] is False

    phases = {entry["phase"]: entry for entry in cfg["consumption"]}
    assert set(phases) == {"m14-m16", "checkpoint-a", "second-semester-projects"}

    assert phases["m14-m16"]["evidence_level"] == "guided"
    assert phases["m14-m16"]["outcomes"] == [
        "G1.OBSERVE.STATUS",
        "G1.OBSERVE.DIFF",
    ]

    checkpoint_outcomes = set(phases["checkpoint-a"]["outcomes"])
    assert {
        "G1.OBSERVE.STATUS",
        "G1.OBSERVE.DIFF",
        "G1.STAGE.INTENTIONAL",
        "G1.COMMIT.INTENTIONAL",
        "G1.HISTORY.INSPECT",
        "G1.MODEL.HEAD",
        "G1.WORKFLOW.CHECKPOINT",
    } <= checkpoint_outcomes
    assert phases["checkpoint-a"]["canonical_activity"] == "g1-stage-selettivo-001"

    boundary = cfg["python_course_boundary"]
    assert boundary["owns_git_curriculum"] is False
    assert boundary["copy_git_lessons"] is False
    assert boundary["git_is_primary_python_grade"] is False

    m14 = M14.read_text(encoding="utf-8")
    m15 = M15.read_text(encoding="utf-8")
    m16 = M16.read_text(encoding="utf-8")
    checkpoint = CHECKPOINT_A.read_text(encoding="utf-8")
    integration = INTEGRATION.read_text(encoding="utf-8")

    require(m14, "git status", "git diff")
    require(m15, "git diff")
    require(m16, "git diff", "Checkpoint A")
    require(
        checkpoint,
        "git status",
        "git diff",
        "git add",
        "git diff --staged",
        "git commit",
        "git log",
        "TheBitPoets/git",
        "g1-stage-selettivo-001",
    )
    require(
        integration,
        provider["candidate_ref"],
        "G1.OBSERVE.STATUS",
        "G1.OBSERVE.DIFF",
        "G1.WORKFLOW.CHECKPOINT",
        "24570f7a3af67634ec0cfbf54f486660359baaf2",
    )

    print("Git G1 consumer contract: OK")


if __name__ == "__main__":
    main()

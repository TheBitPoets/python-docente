from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REVIEWS = [
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_02_PY2_03_2026-08-25.md",
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_04_2026-08-25.md",
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_05_CHECKPOINT_A_2026-08-25.md",
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_06_PY2_07_CHECKPOINT_B_2026-08-25.md",
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_08_PY2_09_2026-08-25.md",
    ROOT / "doc" / "SEMANTIC_REVIEW_PY2_10_CHECKPOINT_C_2026-08-25.md",
]

RUNBOOKS = [ROOT / "teacher" / f"M{i:02d}_RUNBOOK.md" for i in range(4, 31)]


def text(path: Path) -> str:
    assert path.is_file(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def main() -> None:
    index = text(ROOT / "doc" / "SEMANTIC_REVIEW_INDEX_2026-08-25.md")

    for review in REVIEWS:
        assert review.name in index, f"review not indexed: {review.name}"
        body = text(review)
        assert "Nessun curriculum change richiesto" in body or "Nessun curriculum change" in body

    # All materialized module runbooks must expose an explicit mastery boundary
    # after the semantic-review pass.
    for runbook in RUNBOOKS:
        body = text(runbook)
        assert "MUST MASTER" in body, f"missing MUST MASTER: {runbook.name}"
        assert "Minimum mastery gate" in body or "Minimum mastery" in body or "Exit checkpoint" in body, (
            f"missing mastery/exit gate: {runbook.name}"
        )

    # Git is a cross-course embedded outcome subset, not a second full course.
    git_cfg = json.loads(text(ROOT / "config" / "git-g1-consumer.json"))
    delivery = git_cfg["delivery"]
    assert delivery["mode"] == "embedded-outcome-subset"
    assert delivery["full_g1_track_completion_required"] is False
    assert delivery["full_canonical_lesson_completion_required"] is False
    assert git_cfg["python_course_boundary"]["git_is_separate_high_stakes_checkpoint"] is False

    # Git begins in M14, not in M13.
    m13 = text(ROOT / "teacher" / "M13_RUNBOOK.md")
    assert "Niente Git in M13" in m13
    assert "git status" not in text(ROOT / "content" / "python" / "13_FUNZIONI_PARAMETRI_RETURN.md")

    # Platform grading profiles must remain teacher/delivery concerns in the
    # reviewed modules, not student mastery requirements.
    m16 = text(ROOT / "teacher" / "M16_RUNBOOK.md")
    m26 = text(ROOT / "teacher" / "M26_RUNBOOK.md")
    m30 = text(ROOT / "teacher" / "M30_RUNBOOK.md")
    assert "TEACHER / DELIVERY ONLY" in m16
    assert "TEACHER / DELIVERY ONLY" in m26
    assert "P3 — teacher/delivery boundary" in m30

    # Composition is frozen core and may not become optional at Checkpoint C.
    checkpoint_c = text(ROOT / "student" / "CHECKPOINT_C.md")
    assert "composizione/collaborazione reale tra oggetti" in checkpoint_c
    assert "La composizione non è opzionale nel capstone completo" in checkpoint_c
    assert "oppure motivazione del perché non serve" not in checkpoint_c

    # File/error handling must remain deliberately bounded to protect OOP.
    m26_review = text(ROOT / "doc" / "SEMANTIC_REVIEW_PY2_08_PY2_09_2026-08-25.md")
    assert "3 ore core" in m26_review
    for forbidden in ("CSV/JSON/binario", "P4"):
        assert forbidden in m26_review  # documented as excluded/teacher-only boundary

    # Capstone keeps the frozen progression and does not add another week.
    m30_runbook = text(ROOT / "teacher" / "M30_RUNBOOK.md")
    assert "M29 / settimana 31" in m30_runbook
    assert "M30 / settimana 32" in m30_runbook
    assert "Checkpoint C / settimana 33" in m30_runbook

    print("PASS: semantic review contract M04-M30 + checkpoints A/B/C")


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REVIEWS = [
    "SEMANTIC_REVIEW_PY2_02_PY2_03_2026-08-25.md",
    "SEMANTIC_REVIEW_PY2_04_2026-08-25.md",
    "SEMANTIC_REVIEW_PY2_05_CHECKPOINT_A_2026-08-25.md",
    "SEMANTIC_REVIEW_PY2_06_PY2_07_CHECKPOINT_B_2026-08-25.md",
    "SEMANTIC_REVIEW_PY2_08_PY2_09_2026-08-25.md",
    "SEMANTIC_REVIEW_PY2_10_CHECKPOINT_C_2026-08-25.md",
]


def read(path: Path) -> str:
    assert path.is_file(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def has_mastery_boundary(body: str) -> bool:
    markers = (
        "MUST MASTER",
        "Minimum mastery gate",
        "Minimum mastery checkpoint",
        "Exit checkpoint",
        "Contratto minimo",
        "Contratto minimo del capstone",
        "Gate di uscita",
    )
    return any(marker in body for marker in markers)


def main() -> None:
    index = read(ROOT / "doc" / "SEMANTIC_REVIEW_INDEX_2026-08-25.md")

    for filename in REVIEWS:
        assert filename in index, f"review not indexed: {filename}"
        body = read(ROOT / "doc" / filename)
        assert "Nessun curriculum change" in body or "ripristina" in body

    # Every materialized M04-M30 runbook must expose an explicit mastery/exit
    # boundary after the semantic review. The exact heading is intentionally
    # not standardized: the boundary matters more than one label.
    for number in range(4, 31):
        path = ROOT / "teacher" / f"M{number:02d}_RUNBOOK.md"
        body = read(path)
        assert has_mastery_boundary(body), f"missing mastery boundary: {path.name}"

    git_cfg = json.loads(read(ROOT / "config" / "git-g1-consumer.json"))
    delivery = git_cfg["delivery"]
    assert delivery["mode"] == "embedded-outcome-subset"
    assert delivery["full_g1_track_completion_required"] is False
    assert delivery["full_canonical_lesson_completion_required"] is False
    assert delivery["python_checkpoint_remains_primary_time_owner"] is True
    assert git_cfg["python_course_boundary"]["git_is_separate_high_stakes_checkpoint"] is False

    # M13 formalizes the M05 preview. Git starts in M14.
    m13_runbook = read(ROOT / "teacher" / "M13_RUNBOOK.md")
    m13_lesson = read(ROOT / "content" / "python" / "13_FUNZIONI_PARAMETRI_RETURN.md")
    assert "Niente Git in M13" in m13_runbook
    assert "git status" not in m13_lesson
    assert "git diff" not in m13_lesson

    # Frozen OOP composition outcome remains mandatory.
    checkpoint_c = read(ROOT / "student" / "CHECKPOINT_C.md")
    assert "composizione/collaborazione reale tra oggetti" in checkpoint_c
    assert "La composizione non è opzionale nel capstone completo" in checkpoint_c
    assert "oppure motivazione del perché non serve" not in checkpoint_c

    # M26 remains a deliberately bounded three-hour persistence/error unit.
    m26_review = read(ROOT / "doc" / "SEMANTIC_REVIEW_PY2_08_PY2_09_2026-08-25.md")
    assert "3 ore core" in m26_review
    assert "CSV, JSON, binario" in m26_review or "CSV/JSON/binario" in m26_review
    assert "TEACHER / DELIVERY ONLY" in m26_review

    # Grading profiles are delivery boundaries, not student mastery.
    assert "TEACHER / DELIVERY ONLY" in read(ROOT / "teacher" / "M16_RUNBOOK.md")
    assert "TEACHER / DELIVERY ONLY" in read(ROOT / "teacher" / "M26_RUNBOOK.md")
    assert "P3 — teacher/delivery boundary" in read(ROOT / "teacher" / "M30_RUNBOOK.md")

    # Capstone window must respect frozen weeks 29-32 + checkpoint week 33.
    m30 = read(ROOT / "teacher" / "M30_RUNBOOK.md")
    assert "M29 / settimana 31" in m30
    assert "M30 / settimana 32" in m30
    assert "Checkpoint C / settimana 33" in m30

    # Checkpoints B/C reuse complete G1 mechanics rather than the misleading
    # abbreviated status→diff→commit form.
    for checkpoint in (ROOT / "student" / "CHECKPOINT_B.md", ROOT / "student" / "CHECKPOINT_C.md"):
        body = read(checkpoint)
        for command in (
            "git status",
            "git diff",
            "git add <path>",
            "git diff --staged",
            "git commit",
            "git log / git show",
        ):
            assert command in body, f"missing {command!r} in {checkpoint.name}"

    print("PASS: semantic review coverage and frozen teaching boundaries")


if __name__ == "__main__":
    main()

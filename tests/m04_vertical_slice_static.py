from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "content" / "python" / "04_INTERPRETE_REPL_VALORI_IO.md"
SLIDES = ROOT / "slides" / "python" / "modules" / "04_INTERPRETE_REPL_VALORI_IO.md"
RUNBOOK = ROOT / "teacher" / "M04_RUNBOOK.md"
STUDENT_INDEX = ROOT / "student" / "README.md"
TEACHER_INDEX = ROOT / "teacher" / "README.md"
ACTIVITY = ROOT / "activities" / "python" / "py2-activity-b-input-somma-001" / "activity.json"
CONTENT_PACK = ROOT / "content" / "python" / "content-pack.json"
COURSE_DESIGN = ROOT / "doc" / "course_design.json"

ACTIVITY_ID = "py2-activity-b-input-somma-001"
LESSON_FILE = "04_INTERPRETE_REPL_VALORI_IO.md"
LESSON_PATH = f"content/python/{LESSON_FILE}"
LESSON_ANCHOR = "m04-interprete-repl-script-valori-e-inputoutput"


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    if not path.is_file():
        fail(f"File mancante: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def json_object(path: Path) -> dict:
    value = json.loads(text(path))
    if not isinstance(value, dict):
        fail(f"JSON non oggetto: {path.relative_to(ROOT)}")
    return value


def markdown_links(markdown: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", markdown)


def assert_no_teacher_links(path: Path) -> None:
    for target in markdown_links(text(path)):
        normalized = target.replace("\\", "/").lower()
        if "/teacher/" in f"/{normalized}" or "/solution/" in f"/{normalized}":
            fail(f"Materiale studente collega asset riservato in {path.relative_to(ROOT)}: {target}")


def assert_lesson_contract() -> None:
    lesson = text(LESSON)
    required = [
        "# M04 — Interprete, REPL, script, valori e input/output",
        "## Obiettivi",
        "# 1. Problema iniziale",
        "# 3. Il REPL",
        "# 11. Microscope",
        "# 14. Error Clinic",
        "# 17. Activity B — Completa la somma",
        "# 20. Sintesi",
        "# Fonti e riferimenti docente",
        ACTIVITY_ID,
        "input() → str",
        "nessun traceback ≠ correttezza",
    ]
    missing = [marker for marker in required if marker not in lesson]
    if missing:
        fail(f"Lesson M04 incompleta; marker mancanti: {missing}")
    assert_no_teacher_links(LESSON)


def assert_slide_contract() -> None:
    slides = text(SLIDES)
    if not slides.startswith("---\nmarp: true"):
        fail("Deck M04 non è una sorgente Marp canonica")
    slide_count = max(1, slides.count("\n---\n") - 1)
    if not 12 <= slide_count <= 25:
        fail(f"Deck M04 fuori densità attesa: {slide_count} slide")
    for marker in (ACTIVITY_ID, "prima prevedi, poi esegui", "input()", "Error Clinic"):
        if marker not in slides:
            fail(f"Deck M04 senza marker richiesto: {marker}")
    assert_no_teacher_links(SLIDES)


def assert_runbook_contract() -> None:
    runbook = text(RUNBOOK)
    for marker in (
        ACTIVITY_ID,
        "Misconception watchlist",
        "Differenziazione",
        "Evidence docente",
        "Cosa NON anticipare",
        "python-docente#7",
    ):
        if marker not in runbook:
            fail(f"Runbook M04 senza marker richiesto: {marker}")


def assert_navigation_contract() -> None:
    student = text(STUDENT_INDEX)
    teacher = text(TEACHER_INDEX)
    for marker in (
        "../content/python/04_INTERPRETE_REPL_VALORI_IO.md",
        "../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md",
        ACTIVITY_ID,
    ):
        if marker not in student:
            fail(f"Indice studente non collega M04 correttamente: {marker}")
    if "M04_RUNBOOK.md" not in teacher or ACTIVITY_ID not in teacher:
        fail("Indice docente non collega il vertical slice M04")
    assert_no_teacher_links(STUDENT_INDEX)


def assert_activity_contract() -> None:
    activity = json_object(ACTIVITY)
    if activity.get("id") != ACTIVITY_ID:
        fail("Activity id M04 inatteso")
    if activity.get("language") != "python" or activity.get("source_name") != "main.py":
        fail("Activity M04 non usa il profilo Python single-file previsto")
    grading = activity.get("grading_policy") or {}
    if grading.get("test") is not True or grading.get("sandbox") is not True:
        fail("Activity M04 deve richiedere test + sandbox")
    if grading.get("ai_feedback") is not False:
        fail("Activity fondazionale M04 non deve abilitare AI feedback")
    cases = activity.get("test_cases") or []
    expected = [
        ("2\n3\n", "5\n"),
        ("0\n0\n", "0\n"),
        ("-4\n10\n", "6\n"),
    ]
    actual = [(case.get("stdin"), case.get("expected_stdout")) for case in cases]
    if actual != expected:
        fail(f"Tre casi canarino M04 cambiati senza aggiornare il contratto: {actual}")
    refs = activity.get("source_refs") or []
    canonical_ref = next((ref for ref in refs if ref.get("source_id") == "python-course-content"), None)
    if not canonical_ref:
        fail("Activity M04 non riferisce la lesson canonica")
    expected_href = f"{LESSON_PATH}#{LESSON_ANCHOR}"
    if canonical_ref.get("href") != expected_href:
        fail(f"Href canonico Activity→lesson inatteso: {canonical_ref.get('href')}")


def assert_content_pack_contract() -> None:
    pack = json_object(CONTENT_PACK)
    sources = {source.get("id"): source for source in pack.get("sources", []) if isinstance(source, dict)}
    course_source = sources.get("python-course-content")
    if not course_source or LESSON_FILE not in (course_source.get("files") or []):
        fail("Content Pack non indicizza la lesson M04")
    items = {item.get("id"): item for item in pack.get("content_items", []) if isinstance(item, dict)}
    item = items.get("py2-m04-interprete-repl-io")
    if not item:
        fail("Content Pack senza content item M04")
    if item.get("path") != LESSON_PATH or ACTIVITY_ID not in (item.get("activity_ids") or []):
        fail("Content item M04 non collega lesson e Activity")


def assert_course_board_source_contract() -> None:
    design = json_object(COURSE_DESIGN)
    sources = {source.get("id"): source for source in design.get("sources", []) if isinstance(source, dict)}
    source = sources.get("python-course-content")
    if not source or LESSON_FILE not in (source.get("files") or []):
        fail("Course Design non espone M04 alla Course Board")
    years = design.get("years") or []
    year = next((year for year in years if year.get("id") == "python-secondo-2026-2027"), None)
    if not year:
        fail("Track secondo anno mancante nel Course Design")
    uda = next((uda for uda in year.get("udas", []) if uda.get("id") == "py2-02"), None)
    if not uda:
        fail("UDA PY2-02 mancante nel Course Design")
    if not isinstance(uda.get("items"), list):
        fail("PY2-02.items deve restare una lista modificabile dalla Course Board")
    # Non imponiamo qui che M04 sia già assegnata: il drag/save/reopen reale è un gate
    # di authoring dashboard, perché la board deve registrare sottoalbero e digest reali.


def main() -> int:
    assert_lesson_contract()
    assert_slide_contract()
    assert_runbook_contract()
    assert_navigation_contract()
    assert_activity_contract()
    assert_content_pack_contract()
    assert_course_board_source_contract()
    print("PASS: M04 lesson + slides + runbook + navigation + Activity + Content Pack + Course Board source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

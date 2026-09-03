from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "content" / "python" / "05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md"
SLIDES = ROOT / "slides" / "python" / "modules" / "05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md"
RUNBOOK = ROOT / "teacher" / "M05_RUNBOOK.md"
STUDENT_INDEX = ROOT / "student" / "README.md"
TEACHER_INDEX = ROOT / "teacher" / "README.md"
CONTENT_PACK = ROOT / "content" / "python" / "content-pack.json"
COURSE_DESIGN = ROOT / "doc" / "course_design.json"

LESSON_FILE = "05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md"
LESSON_PATH = f"content/python/{LESSON_FILE}"
ITEM_ID = "py2-m05-espressioni-operatori-prime-funzioni"
EXPECTED_PACK_ORDER = 6  # M05 is the sixth item because Content Pack order is 1-based (M00=1).


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


def assert_lesson() -> None:
    lesson = text(LESSON)
    required = (
        "# M05 — Espressioni, operatori e prime funzioni",
        "# 1. Problema iniziale: quanti minuti e quanti secondi?",
        "# 4. `/`, `//` e `%` non sono la stessa divisione",
        "floor division",
        "# 8. Precedenza: Python deve sapere cosa calcolare prima",
        "# 14. Prima funzione: dare un nome a una trasformazione",
        "# 15. `return` non è `print`",
        "# 17. Error Clinic",
        "# 20. Activity planning — non ancora materializzato",
        "# 22. Sintesi",
        "python-docente#7",
    )
    missing = [marker for marker in required if marker not in lesson]
    if missing:
        fail(f"Lesson M05 incompleta: {missing}")
    if "taglia la parte decimale" not in lesson or "non una generica regola" not in lesson:
        fail("M05 deve esplicitare che // è floor division, non troncamento generico")
    if "non materializziamo ora una seconda activity p1" not in lesson.casefold():
        fail("M05 non registra il boundary Activity/P1")
    assert_no_teacher_links(LESSON)


def assert_slides() -> None:
    slides = text(SLIDES)
    if not slides.startswith("---\nmarp: true"):
        fail("Deck M05 non è una sorgente Marp canonica")
    slide_count = max(1, slides.count("\n---\n"))
    if not 15 <= slide_count <= 28:
        fail(f"Deck M05 fuori densità attesa: {slide_count} slide")
    for marker in ("`/` non è `//`", "`%` = ciò che rimane", "Prima funzione", "`return` ≠ `print`", "Error Clinic"):
        if marker not in slides:
            fail(f"Deck M05 senza marker richiesto: {marker}")
    if "Non materializziamo una nuova Activity P1" not in slides:
        fail("Deck M05 perde il boundary P1")
    assert_no_teacher_links(SLIDES)


def assert_runbook() -> None:
    runbook = text(RUNBOOK)
    for marker in (
        "Misconception watchlist",
        "M1 — `//` significa sempre",
        "Differenziazione",
        "Evidence docente",
        "Cosa NON anticipare",
        "Handoff a PY2-03",
        "python-docente#7",
        "python-docente#8",
    ):
        if marker not in runbook:
            fail(f"Runbook M05 senza marker richiesto: {marker}")


def assert_navigation() -> None:
    student = text(STUDENT_INDEX)
    teacher = text(TEACHER_INDEX)
    for marker in (
        "../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md",
        "../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md",
        "[Espressioni, operatori e prime funzioni]",
    ):
        if marker not in student:
            fail(f"Indice studente non collega M05: {marker}")
    if "M05_RUNBOOK.md" not in teacher or "05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md" not in teacher:
        fail("Indice docente non collega il modulo M05")
    assert_no_teacher_links(STUDENT_INDEX)


def assert_content_pack() -> None:
    pack = json_object(CONTENT_PACK)
    sources = {s.get("id"): s for s in pack.get("sources", []) if isinstance(s, dict)}
    source = sources.get("python-course-content")
    if not source or LESSON_FILE not in (source.get("files") or []):
        fail("Content Pack non indicizza M05")
    items = {item.get("id"): item for item in pack.get("content_items", []) if isinstance(item, dict)}
    item = items.get(ITEM_ID)
    if not item:
        fail("Content Pack senza content item M05")
    if (
        item.get("path") != LESSON_PATH
        or item.get("order") != EXPECTED_PACK_ORDER
        or item.get("status") != "draft"
    ):
        fail(f"Content item M05 inatteso: {item}")
    if item.get("activity_ids"):
        fail("M05 non deve ancora dichiarare Activity materializzate")
    refs = item.get("source_refs") or []
    if not any(ref.get("id") == "python-course-content" and ref.get("locator") == LESSON_FILE for ref in refs):
        fail("Content item M05 senza provenance alla lesson canonica")


def assert_course_design() -> None:
    design = json_object(COURSE_DESIGN)
    sources = {s.get("id"): s for s in design.get("sources", []) if isinstance(s, dict)}
    source = sources.get("python-course-content")
    if not source or LESSON_FILE not in (source.get("files") or []):
        fail("Course Design non espone M05 alla Course Board")
    year = next((year for year in design.get("years", []) if year.get("id") == "python-secondo-2026-2027"), None)
    if not year:
        fail("Track secondo anno mancante")
    uda = next((uda for uda in year.get("udas", []) if uda.get("id") == "py2-02"), None)
    if not uda or uda.get("weeks") != 2:
        fail("PY2-02 non conserva la finestra congelata di 2 settimane")


def main() -> int:
    assert_lesson()
    assert_slides()
    assert_runbook()
    assert_navigation()
    assert_content_pack()
    assert_course_design()
    print("PASS: M05 lesson + slides + runbook + navigation + Content Pack + Course Board source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

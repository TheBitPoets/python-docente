from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK_PATH = ROOT / "content" / "python" / "content-pack.json"
DESIGN_PATH = ROOT / "doc" / "course_design.json"
STUDENT_INDEX = ROOT / "student" / "README.md"
TEACHER_INDEX = ROOT / "teacher" / "README.md"

MODULE_FILE_RE = re.compile(r"^(\d{2})_[A-Z0-9_]+\.md$")


def fail(message: str) -> None:
    raise AssertionError(message)


def read_text(path: Path) -> str:
    if not path.is_file():
        fail(f"File mancante: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def load_object(path: Path) -> dict:
    value = json.loads(read_text(path))
    if not isinstance(value, dict):
        fail(f"JSON non oggetto: {path.relative_to(ROOT)}")
    return value


def links(markdown: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", markdown)


def assert_no_reserved_links(path: Path) -> None:
    for target in links(read_text(path)):
        normalized = target.replace("\\", "/").lower()
        wrapped = f"/{normalized}"
        if "/teacher/" in wrapped or "/solution/" in wrapped or "/hidden_tests/" in wrapped:
            fail(f"Materiale studente collega asset riservato in {path.relative_to(ROOT)}: {target}")


def explicit_course_source_files(pack: dict) -> set[str]:
    source = next(
        (item for item in pack.get("sources", []) if isinstance(item, dict) and item.get("id") == "python-course-content"),
        None,
    )
    if not source:
        fail("Content Pack senza source python-course-content")
    return {str(item) for item in source.get("files", [])}


def design_course_source_files(design: dict) -> set[str]:
    source = next(
        (item for item in design.get("sources", []) if isinstance(item, dict) and item.get("id") == "python-course-content"),
        None,
    )
    if not source:
        fail("Course Design senza source python-course-content")
    return {str(item) for item in source.get("files", [])}


def assert_activity(activity_id: str, lesson_filename: str) -> None:
    root = ROOT / "activities" / "python" / activity_id
    metadata_path = root / "activity.json"
    activity = load_object(metadata_path)
    if activity.get("id") != activity_id:
        fail(f"Activity directory/id mismatch: {activity_id}")
    refs = activity.get("source_refs") or []
    canonical = next(
        (
            ref
            for ref in refs
            if isinstance(ref, dict)
            and ref.get("source_id") == "python-course-content"
            and lesson_filename in str(ref.get("href") or "")
        ),
        None,
    )
    if not canonical:
        fail(f"Activity {activity_id} non riferisce la lesson canonica {lesson_filename}")


def assert_module(
    item: dict,
    *,
    pack_files: set[str],
    design_files: set[str],
    student_index: str,
    teacher_index: str,
) -> int:
    item_id = str(item.get("id") or "")
    rel_lesson = str(item.get("path") or "")
    lesson_path = ROOT / rel_lesson
    lesson_filename = lesson_path.name
    match = MODULE_FILE_RE.fullmatch(lesson_filename)
    if not match:
        fail(f"Modulo {item_id}: filename non canonico: {lesson_filename}")
    module_number = int(match.group(1))
    module_code = f"M{module_number:02d}"

    if item.get("kind") != "module":
        fail(f"Content item {item_id} non è kind=module")
    if item.get("order") != module_number:
        fail(f"{item_id}: order {item.get('order')} != prefisso file {module_number}")
    if item.get("status") not in {"draft", "review", "approved"}:
        fail(f"{item_id}: status editoriale inatteso: {item.get('status')}")
    if lesson_filename not in pack_files:
        fail(f"{item_id}: lesson non elencata nella source del Content Pack")
    if lesson_filename not in design_files:
        fail(f"{item_id}: lesson non esposta alla Course Board")

    lesson = read_text(lesson_path)
    if not lesson.startswith(f"# {module_code} —"):
        fail(f"{item_id}: H1 lesson non inizia con '# {module_code} —'")
    assert_no_reserved_links(lesson_path)

    slide_path = ROOT / "slides" / "python" / "modules" / lesson_filename
    slides = read_text(slide_path)
    if not slides.startswith("---\nmarp: true"):
        fail(f"{item_id}: slide source Marp mancante/non canonica")
    if f"# {module_code} —" not in slides:
        fail(f"{item_id}: deck non identifica {module_code}")
    assert_no_reserved_links(slide_path)

    runbook_path = ROOT / "teacher" / f"{module_code}_RUNBOOK.md"
    runbook = read_text(runbook_path)
    if not runbook.startswith(f"# {module_code} — Runbook docente"):
        fail(f"{item_id}: runbook canonico mancante")
    if module_code not in teacher_index or lesson_filename not in teacher_index or runbook_path.name not in teacher_index:
        fail(f"{item_id}: indice docente non collega lesson/runbook")
    if lesson_filename not in student_index:
        fail(f"{item_id}: indice studente non collega la lesson")

    refs = item.get("source_refs") or []
    provenance = next(
        (
            ref
            for ref in refs
            if isinstance(ref, dict)
            and ref.get("id") == "python-course-content"
            and ref.get("locator") == lesson_filename
        ),
        None,
    )
    if not provenance:
        fail(f"{item_id}: provenance content-origin alla lesson mancante")

    activities = item.get("activity_ids") or []
    if len(activities) != len(set(activities)):
        fail(f"{item_id}: activity_ids duplicati")
    for activity_id in activities:
        assert_activity(str(activity_id), lesson_filename)

    return module_number


def main() -> int:
    pack = load_object(PACK_PATH)
    design = load_object(DESIGN_PATH)
    student_index = read_text(STUDENT_INDEX)
    teacher_index = read_text(TEACHER_INDEX)
    pack_files = explicit_course_source_files(pack)
    design_files = design_course_source_files(design)

    items = [item for item in pack.get("content_items", []) if isinstance(item, dict)]
    if not items:
        fail("Nessun content item materializzato")

    module_numbers: list[int] = []
    ids: set[str] = set()
    for item in items:
        item_id = str(item.get("id") or "")
        if not item_id or item_id in ids:
            fail(f"Content item id mancante/duplicato: {item_id!r}")
        ids.add(item_id)
        module_numbers.append(
            assert_module(
                item,
                pack_files=pack_files,
                design_files=design_files,
                student_index=student_index,
                teacher_index=teacher_index,
            )
        )

    if module_numbers != sorted(module_numbers):
        fail(f"Content items non ordinati per modulo: {module_numbers}")
    if len(module_numbers) != len(set(module_numbers)):
        fail(f"Numero modulo duplicato nel Content Pack: {module_numbers}")

    materialized_files = {Path(str(item.get("path"))).name for item in items}
    if materialized_files != pack_files:
        fail(
            "Source python-course-content e content_items divergono: "
            f"source-only={sorted(pack_files - materialized_files)}, "
            f"item-only={sorted(materialized_files - pack_files)}"
        )
    if pack_files != design_files:
        fail(
            "Content Pack e Course Design espongono lesson diverse: "
            f"pack-only={sorted(pack_files - design_files)}, "
            f"design-only={sorted(design_files - pack_files)}"
        )

    assert_no_reserved_links(STUDENT_INDEX)
    print(f"PASS: {len(items)} moduli materializzati coerenti nel catalogo authoring")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

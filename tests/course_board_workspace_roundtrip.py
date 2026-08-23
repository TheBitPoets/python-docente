from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
COURSE_DESIGN = ROOT / "doc" / "course_design.json"
LESSON = ROOT / "content" / "python" / "04_INTERPRETE_REPL_VALORI_IO.md"
SOURCE_ID = "python-course-content"
SOURCE_PATH = "content/python/04_INTERPRETE_REPL_VALORI_IO.md"
EXPECTED_ROOT_ID = (
    "python-course-content:content/python/04_INTERPRETE_REPL_VALORI_IO.md"
    "#m04-interprete-repl-script-valori-e-inputoutput"
)

HEADING_FIELDS = (
    "id",
    "title",
    "source",
    "source_id",
    "source_label",
    "source_provider",
    "source_repository",
    "source_ref",
    "source_commit",
    "content_sha256",
    "href",
    "level",
    "line",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"JSON non oggetto: {path}")
    return value


def item_from_heading(heading: dict) -> dict:
    item = {field: heading.get(field) for field in HEADING_FIELDS}
    item["frame"] = {"status": "draft"}
    return item


def subtree_from_headings(headings: list[dict], root_index: int) -> dict:
    """Mirror Course Board itemFromHeading/childItemsFromHeading for one heading."""

    root_heading = headings[root_index]
    root_level = int(root_heading["level"])
    root_source = (root_heading.get("source_id"), root_heading.get("source"))
    root = item_from_heading(root_heading)
    stack: list[tuple[int, dict]] = [(root_level, root)]

    for heading in headings[root_index + 1 :]:
        same_source = (heading.get("source_id"), heading.get("source")) == root_source
        if not same_source:
            break
        level = int(heading["level"])
        if level <= root_level:
            break

        item = item_from_heading(heading)
        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1] if stack else root
        parent.setdefault("children", []).append(item)
        stack.append((level, item))

    return root


def module_items_from_headings(headings: list[dict]) -> list[dict]:
    """Build all top-level heading trees that belong to the canonical M04 file.

    Course Design intentionally works at heading granularity, while Content Pack works at
    module/file granularity. M04 currently has several H1 sections in one Markdown file, so
    importing the whole module means adding every H1 subtree from that source to the UDA.
    """

    indices = [
        index
        for index, heading in enumerate(headings)
        if heading.get("source_id") == SOURCE_ID
        and heading.get("source") == SOURCE_PATH
        and int(heading.get("level", 0)) == 1
    ]
    if not indices:
        fail("Course Board non trova H1 per il modulo M04")

    items = [subtree_from_headings(headings, index) for index in indices]
    if items[0].get("id") != EXPECTED_ROOT_ID:
        fail(f"Primo H1 M04 inatteso: {items[0].get('id')}")
    if len(items) < 10:
        fail(f"M04 espone troppo pochi H1 per il file corrente: {len(items)}")
    return items


def find_second_year_uda(design: dict, uda_id: str) -> dict:
    year = next(
        (year for year in design.get("years", []) if year.get("id") == "python-secondo-2026-2027"),
        None,
    )
    if not isinstance(year, dict):
        fail("Track secondo anno non trovato")
    uda = next((uda for uda in year.get("udas", []) if uda.get("id") == uda_id), None)
    if not isinstance(uda, dict):
        fail(f"UDA non trovata: {uda_id}")
    return uda


def reduced_design_for_m04(original: dict) -> dict:
    design = deepcopy(original)
    source = next(
        (source for source in design.get("sources", []) if source.get("id") == SOURCE_ID),
        None,
    )
    if not isinstance(source, dict):
        fail(f"Fonte Course Board mancante: {SOURCE_ID}")
    design["sources"] = [deepcopy(source)]
    design.pop("source_files", None)
    for year in design.get("years", []):
        for uda in year.get("udas", []):
            uda["items"] = []
    return design


def flatten_items(items: list[dict]) -> list[dict]:
    result: list[dict] = []

    def visit(item: dict) -> None:
        result.append(item)
        for child in item.get("children") or []:
            visit(child)

    for item in items:
        visit(item)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
    sys.path.insert(0, str(platform))
    from scripts import course_board_server

    original = load_json(COURSE_DESIGN)
    design = reduced_design_for_m04(original)

    with tempfile.TemporaryDirectory(prefix="python-course-board-roundtrip-") as raw_temp:
        temp_root = Path(raw_temp)
        (temp_root / "doc").mkdir(parents=True)
        (temp_root / "content" / "python").mkdir(parents=True)
        shutil.copy2(LESSON, temp_root / "content" / "python" / LESSON.name)
        (temp_root / "doc" / "course_design.json").write_text(
            json.dumps(design, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        course_board_server.configure_data_root(temp_root)
        loaded = course_board_server.read_design()
        headings = course_board_server.extract_headings(loaded)
        module_items = module_items_from_headings(headings)

        first = module_items[0]
        if first.get("line") != 1 or first.get("level") != 1:
            fail(f"Metadati heading M04 inattesi: line={first.get('line')} level={first.get('level')}")
        if not first.get("content_sha256"):
            fail("Course Board non produce content_sha256 per M04")

        # The first title H1 has Obiettivi/Prerequisiti as its H2 children. Later numbered
        # sections are sibling H1 trees and are imported separately into the same UDA.
        first_children = first.get("children") or []
        child_titles = {child.get("title") for child in first_children}
        if not {"Obiettivi", "Prerequisiti"}.issubset(child_titles):
            fail(f"Sottoalbero iniziale M04 non conserva Obiettivi/Prerequisiti: {child_titles}")

        uda = find_second_year_uda(loaded, "py2-02")
        uda["items"] = module_items
        course_board_server.write_design(loaded)

        reopened = course_board_server.read_design()
        reopened_uda = find_second_year_uda(reopened, "py2-02")
        reopened_items = reopened_uda.get("items") or []
        if len(reopened_items) != len(module_items):
            fail(
                "Round-trip Course Design perde sezioni top-level M04: "
                f"{len(reopened_items)} != {len(module_items)}"
            )

        expected_flat = flatten_items(module_items)
        reopened_flat = flatten_items(reopened_items)
        if len(reopened_flat) != len(expected_flat):
            fail(f"Round-trip perde heading M04: {len(reopened_flat)} != {len(expected_flat)}")

        expected_by_id = {item.get("id"): item for item in expected_flat}
        reopened_by_id = {item.get("id"): item for item in reopened_flat}
        if set(reopened_by_id) != set(expected_by_id):
            fail("Round-trip altera l'insieme degli heading M04")

        for item_id, expected in expected_by_id.items():
            actual = reopened_by_id[item_id]
            for field in ("source_id", "source", "href", "content_sha256", "line", "level"):
                if actual.get(field) != expected.get(field):
                    fail(
                        f"Round-trip altera {field} per {item_id}: "
                        f"{actual.get(field)!r} != {expected.get(field)!r}"
                    )

        reopened_headings = course_board_server.extract_headings(reopened)
        current_by_id = {heading.get("id"): heading for heading in reopened_headings}
        for item_id, persisted in reopened_by_id.items():
            current = current_by_id.get(item_id)
            if not current:
                fail(f"Heading M04 non più indicizzabile dopo save/reopen: {item_id}")
            if current.get("content_sha256") != persisted.get("content_sha256"):
                fail(f"Digest M04 non coincide dopo save/reopen: {item_id}")

    print(
        "PASS: external Course Workspace M04 file → all H1 subtrees → "
        "PY2-02 save → reopen round-trip"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

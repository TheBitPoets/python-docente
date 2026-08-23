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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
    sys.path.insert(0, str(platform))
    try:
        from scripts import course_board_server
    finally:
        # Keep the platform importable for the imported module's lazy imports.
        pass

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
        root_index = next(
            (
                index
                for index, heading in enumerate(headings)
                if heading.get("source_id") == SOURCE_ID
                and heading.get("title") == "M04 — Interprete, REPL, script, valori e input/output"
            ),
            None,
        )
        if root_index is None:
            fail("Course Board non indicizza l'H1 canonico M04")

        root_heading = headings[root_index]
        if root_heading.get("id") != EXPECTED_ROOT_ID:
            fail(f"Heading id M04 inatteso: {root_heading.get('id')}")
        if root_heading.get("line") != 1 or root_heading.get("level") != 1:
            fail(f"Metadati heading M04 inattesi: line={root_heading.get('line')} level={root_heading.get('level')}")
        if not root_heading.get("content_sha256"):
            fail("Course Board non produce content_sha256 per M04")

        item_tree = subtree_from_headings(headings, root_index)
        children = item_tree.get("children") or []
        if len(children) < 5:
            fail(f"Sottoalbero M04 troppo piccolo: {len(children)} figli diretti")

        uda = find_second_year_uda(loaded, "py2-02")
        uda["items"] = [item_tree]
        course_board_server.write_design(loaded)

        reopened = course_board_server.read_design()
        reopened_uda = find_second_year_uda(reopened, "py2-02")
        items = reopened_uda.get("items") or []
        if len(items) != 1:
            fail(f"Round-trip Course Design non conserva M04: {len(items)} item")
        reopened_root = items[0]
        for field in ("id", "source_id", "source", "href", "content_sha256", "line", "level"):
            if reopened_root.get(field) != item_tree.get(field):
                fail(f"Round-trip altera {field}: {reopened_root.get(field)!r} != {item_tree.get(field)!r}")
        if len(reopened_root.get("children") or []) != len(children):
            fail("Round-trip perde il sottoalbero degli heading M04")

        reopened_headings = course_board_server.extract_headings(reopened)
        current_root = next((heading for heading in reopened_headings if heading.get("id") == EXPECTED_ROOT_ID), None)
        if not current_root:
            fail("M04 non è più indicizzabile dopo il salvataggio")
        if current_root.get("content_sha256") != reopened_root.get("content_sha256"):
            fail("Digest M04 non coincide dopo save/reopen")

    print("PASS: external Course Workspace M04 heading → UDA tree → save → reopen round-trip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

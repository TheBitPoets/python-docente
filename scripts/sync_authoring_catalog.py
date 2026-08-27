from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK_PATH = ROOT / "content" / "python" / "content-pack.json"
DESIGN_PATH = ROOT / "doc" / "course_design.json"
COURSE_SOURCE_ID = "python-course-content"
TRACK_ID = "python-secondo-2026-2027"
MODULE_FILE_RE = re.compile(r"^(\d{2})_[A-Z0-9_]+\.md$")

# M00 is orientation embedded in the first three-week PY2-01 window. Course
# Design deliberately has no separate py2-00 UDA, so M00–M03 share py2-01.
UDA_MODULE_RANGES: dict[str, tuple[int, int] | None] = {
    "py2-01": (0, 3),
    "py2-02": (4, 5),
    "py2-03": (6, 8),
    "py2-04": (9, 12),
    "py2-05": (13, 16),
    "checkpoint-a": None,
    "py2-06": (17, 19),
    "py2-07": (20, 22),
    "checkpoint-b": None,
    "py2-08": (23, 25),
    "py2-09": (26, 26),
    "py2-10": (27, 30),
    "checkpoint-c": None,
}


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} non contiene un oggetto JSON")
    return value


def module_number(filename: str) -> int:
    match = MODULE_FILE_RE.fullmatch(filename)
    if not match:
        raise ValueError(f"Filename lesson non canonico: {filename}")
    return int(match.group(1))


def canonical_modules(pack: dict) -> list[dict]:
    items = [item for item in pack.get("content_items", []) if isinstance(item, dict)]
    result: list[dict] = []
    seen_files: set[str] = set()
    seen_ids: set[str] = set()
    seen_numbers: set[int] = set()

    for item in items:
        if item.get("kind") != "module":
            continue
        item_id = str(item.get("id") or "")
        path = Path(str(item.get("path") or ""))
        if path.parent.as_posix() != "content/python":
            raise ValueError(f"Content item module fuori content/python: {item_id}")
        filename = path.name
        number = module_number(filename)
        if not item_id or item_id in seen_ids:
            raise ValueError(f"Content item id mancante/duplicato: {item_id!r}")
        if filename in seen_files:
            raise ValueError(f"Lesson duplicata nei content_items: {filename}")
        if number in seen_numbers:
            raise ValueError(f"Numero modulo duplicato nei content_items: M{number:02d}")
        if not (ROOT / path).is_file():
            raise ValueError(f"Lesson dichiarata ma mancante: {path.as_posix()}")

        seen_ids.add(item_id)
        seen_files.add(filename)
        seen_numbers.add(number)
        result.append(
            {
                "id": item_id,
                "filename": filename,
                "module_number": number,
                "catalog_order": int(item.get("order", 0)),
                "item": item,
            }
        )

    result.sort(key=lambda module: int(module["module_number"]))
    if not result:
        raise ValueError("Nessun modulo materializzato nel Content Pack")

    # thebitlab.content-pack.v1 requires a strictly positive integer order.
    # Module identity is instead carried by the canonical Mxx filename, so M00
    # maps to catalog order 1, M01 to 2, ..., M30 to 31.
    for index, module in enumerate(result, start=1):
        module["item"]["order"] = index
        module["catalog_order"] = index
    return result


def find_source(container: dict, source_id: str) -> dict:
    source = next(
        (
            item
            for item in container.get("sources", [])
            if isinstance(item, dict) and item.get("id") == source_id
        ),
        None,
    )
    if not isinstance(source, dict):
        raise ValueError(f"Source mancante: {source_id}")
    return source


def find_track(design: dict) -> dict:
    tracks = [
        year
        for year in design.get("years", [])
        if isinstance(year, dict) and year.get("id") == TRACK_ID
    ]
    if len(tracks) != 1:
        raise ValueError(f"Course Design: atteso un solo track {TRACK_ID}, trovati {len(tracks)}")
    return tracks[0]


def expected_uda_content_items(modules: list[dict]) -> dict[str, list[str]]:
    by_number = {int(module["module_number"]): str(module["id"]) for module in modules}
    expected: dict[str, list[str]] = {}
    for uda_id, bounds in UDA_MODULE_RANGES.items():
        if bounds is None:
            expected[uda_id] = []
            continue
        start, stop = bounds
        missing = [number for number in range(start, stop + 1) if number not in by_number]
        if missing:
            raise ValueError(f"{uda_id}: moduli mancanti dal Content Pack: {missing}")
        expected[uda_id] = [by_number[number] for number in range(start, stop + 1)]
    return expected


def stable_json(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def synchronized_documents() -> tuple[dict, dict, list[dict]]:
    pack = load_object(PACK_PATH)
    design = load_object(DESIGN_PATH)
    modules = canonical_modules(pack)
    module_files = [str(module["filename"]) for module in modules]

    pack_source = find_source(pack, COURSE_SOURCE_ID)
    design_source = find_source(design, COURSE_SOURCE_ID)
    pack_source["files"] = list(module_files)
    design_source["files"] = list(module_files)

    track = find_track(design)
    udas = {
        str(uda.get("id")): uda
        for uda in track.get("udas", [])
        if isinstance(uda, dict) and uda.get("id")
    }
    if set(udas) != set(UDA_MODULE_RANGES):
        raise ValueError(
            "Course Design UDA set inatteso: "
            f"missing={sorted(set(UDA_MODULE_RANGES) - set(udas))}, "
            f"extra={sorted(set(udas) - set(UDA_MODULE_RANGES))}"
        )

    expected_mapping = expected_uda_content_items(modules)
    for uda_id, content_item_ids in expected_mapping.items():
        udas[uda_id]["content_item_ids"] = list(content_item_ids)

    return pack, design, modules


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincronizza catalogo moduli e mapping UDA dal Content Pack."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Scrive Content Pack e Course Design; senza questa opzione esegue solo il check semantico.",
    )
    args = parser.parse_args()

    current_pack = load_object(PACK_PATH)
    current_design = load_object(DESIGN_PATH)
    expected_pack, expected_design, modules = synchronized_documents()

    dirty: list[str] = []
    if current_pack != expected_pack:
        dirty.append(PACK_PATH.relative_to(ROOT).as_posix())
    if current_design != expected_design:
        dirty.append(DESIGN_PATH.relative_to(ROOT).as_posix())

    if args.write:
        if current_pack != expected_pack:
            PACK_PATH.write_text(stable_json(expected_pack), encoding="utf-8")
        if current_design != expected_design:
            DESIGN_PATH.write_text(stable_json(expected_design), encoding="utf-8")
        print(
            f"SYNC: {len(modules)} moduli M{modules[0]['module_number']:02d}–M{modules[-1]['module_number']:02d}"
            + (f"; aggiornati: {', '.join(dirty)}" if dirty else "; nessuna modifica")
        )
        return 0

    if dirty:
        print(
            "Authoring catalog non sincronizzato: "
            + ", ".join(dirty)
            + ". Esegui: python scripts/sync_authoring_catalog.py --write"
        )
        return 1

    print(
        f"PASS: authoring catalog sincronizzato su {len(modules)} moduli "
        f"M{modules[0]['module_number']:02d}–M{modules[-1]['module_number']:02d}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

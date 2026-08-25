from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK_PATH = ROOT / "content" / "python" / "content-pack.json"
DESIGN_PATH = ROOT / "doc" / "course_design.json"
COURSE_SOURCE_ID = "python-course-content"


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} non contiene un oggetto JSON")
    return value


def canonical_module_files(pack: dict) -> list[str]:
    items = [item for item in pack.get("content_items", []) if isinstance(item, dict)]
    ordered = sorted(items, key=lambda item: int(item.get("order", 0)))
    result: list[str] = []
    seen: set[str] = set()
    for item in ordered:
        if item.get("kind") != "module":
            continue
        path = Path(str(item.get("path") or ""))
        if path.parent.as_posix() != "content/python":
            raise ValueError(f"Content item module fuori content/python: {item.get('id')}")
        filename = path.name
        if not filename.endswith(".md") or not filename:
            raise ValueError(f"Filename lesson non valido: {item.get('id')}")
        if filename in seen:
            raise ValueError(f"Lesson duplicata nei content_items: {filename}")
        seen.add(filename)
        if not (ROOT / path).is_file():
            raise ValueError(f"Lesson dichiarata ma mancante: {path.as_posix()}")
        result.append(filename)
    if not result:
        raise ValueError("Nessun modulo materializzato nel Content Pack")
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


def stable_json(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def synchronized_documents() -> tuple[dict, dict, list[str]]:
    pack = load_object(PACK_PATH)
    design = load_object(DESIGN_PATH)
    module_files = canonical_module_files(pack)

    pack_source = find_source(pack, COURSE_SOURCE_ID)
    design_source = find_source(design, COURSE_SOURCE_ID)
    pack_source["files"] = list(module_files)
    design_source["files"] = list(module_files)
    return pack, design, module_files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincronizza la source python-course-content dal catalogo content_items."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Scrive Content Pack e Course Design; senza questa opzione esegue solo il check.",
    )
    args = parser.parse_args()

    current_pack = PACK_PATH.read_text(encoding="utf-8")
    current_design = DESIGN_PATH.read_text(encoding="utf-8")
    pack, design, module_files = synchronized_documents()
    expected_pack = stable_json(pack)
    expected_design = stable_json(design)

    dirty: list[str] = []
    if current_pack != expected_pack:
        dirty.append(PACK_PATH.relative_to(ROOT).as_posix())
    if current_design != expected_design:
        dirty.append(DESIGN_PATH.relative_to(ROOT).as_posix())

    if args.write:
        PACK_PATH.write_text(expected_pack, encoding="utf-8")
        DESIGN_PATH.write_text(expected_design, encoding="utf-8")
        print(
            "SYNC: "
            + ", ".join(module_files)
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

    print(f"PASS: authoring catalog sincronizzato su {len(module_files)} moduli")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

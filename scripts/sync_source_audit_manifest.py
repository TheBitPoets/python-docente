from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "content" / "python" / "content-pack.json",
    ROOT / "doc" / "course_design.json",
]
SOURCE_ID = "python-source-audits"
EXPECTED_FILES = [
    "SOURCE_CATALOG.md",
    "FRIEDPYTHON_MAPPING.md",
    "FRIEDPYTHON_LISTS_TUPLES_AUDIT.md",
    "FRIEDPYTHON_DICTS_AUDIT.md",
    "FRIEDPYTHON_FILES_AUDIT.md",
]
SOURCE_DIR = ROOT / "sources"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"JSON root is not an object: {path.relative_to(ROOT)}")
    return value


def source_object(document: dict, *, path: Path) -> dict:
    matches = [
        item
        for item in document.get("sources", [])
        if isinstance(item, dict) and item.get("id") == SOURCE_ID
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"{path.relative_to(ROOT)}: expected exactly one {SOURCE_ID!r} source, found {len(matches)}"
        )
    return matches[0]


def current_files(path: Path) -> list[str]:
    source = source_object(load(path), path=path)
    files = source.get("files")
    if not isinstance(files, list) or not all(isinstance(item, str) for item in files):
        raise AssertionError(f"{path.relative_to(ROOT)}: invalid files list for {SOURCE_ID}")
    return list(files)


def find_source_object_span(text: str, *, path: Path) -> tuple[int, int]:
    id_match = re.search(r'"id"\s*:\s*"python-source-audits"', text)
    if not id_match:
        raise AssertionError(f"{path.relative_to(ROOT)}: source id {SOURCE_ID!r} not found in text")

    start = text.rfind("{", 0, id_match.start())
    if start < 0:
        raise AssertionError(f"{path.relative_to(ROOT)}: object start not found")

    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return start, index + 1

    raise AssertionError(f"{path.relative_to(ROOT)}: object end not found")


def patched_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start, end = find_source_object_span(text, path=path)
    object_text = text[start:end]

    # Keep the surrounding JSON formatting stable: replace only the explicit
    # files array inside the one source object instead of re-dumping the whole
    # Content Pack / Course Design document.
    files_match = re.search(r'("files"\s*:\s*)\[[^\]]*\]', object_text)
    if not files_match:
        raise AssertionError(f"{path.relative_to(ROOT)}: files array not found in {SOURCE_ID}")

    compact = json.dumps(EXPECTED_FILES, ensure_ascii=False, separators=(",", ":"))
    replacement = files_match.group(1) + compact
    new_object = object_text[: files_match.start()] + replacement + object_text[files_match.end() :]
    new_text = text[:start] + new_object + text[end:]

    # Fail closed: the text patch must still parse and expose exactly the
    # expected semantic list.
    parsed = json.loads(new_text)
    source = source_object(parsed, path=path)
    if source.get("files") != EXPECTED_FILES:
        raise AssertionError(f"{path.relative_to(ROOT)}: patched semantic files list mismatch")

    return new_text


def validate_source_files_exist() -> None:
    missing = [name for name in EXPECTED_FILES if not (SOURCE_DIR / name).is_file()]
    if missing:
        raise AssertionError(f"source audit files missing on disk: {missing}")


def check() -> bool:
    validate_source_files_exist()
    mismatches: list[str] = []
    for path in TARGETS:
        files = current_files(path)
        if files != EXPECTED_FILES:
            mismatches.append(
                f"{path.relative_to(ROOT)}: current={files!r}, expected={EXPECTED_FILES!r}"
            )

    if mismatches:
        print("SOURCE AUDIT MANIFEST DRIFT")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return False

    print("PASS: Content Pack and Course Design source-audit manifests are aligned")
    return True


def write() -> None:
    validate_source_files_exist()
    for path in TARGETS:
        new_text = patched_text(path)
        if new_text != path.read_text(encoding="utf-8"):
            path.write_text(new_text, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")
        else:
            print(f"unchanged {path.relative_to(ROOT)}")

    if not check():
        raise AssertionError("manifest sync write did not converge")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="replace only the python-source-audits files array in both manifests",
    )
    args = parser.parse_args()

    if args.write:
        write()
        return 0

    return 0 if check() else 1


if __name__ == "__main__":
    raise SystemExit(main())

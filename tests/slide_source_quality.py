from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "content" / "python" / "content-pack.json"
SLIDES_ROOT = ROOT / "slides" / "python" / "modules"

FORBIDDEN_STUDENT_DECK_MARKERS = (
    "TEACHER / DELIVERY ONLY",
    "P2 TheBitLab",
    "P3 TheBitLab",
    "P4 TheBitLab",
    "2cornot2c#756",
    "2cornot2c#757",
    "2cornot2c#758",
)


def read(path: Path) -> str:
    assert path.is_file(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    value = json.loads(read(path))
    assert isinstance(value, dict)
    return value


def frontmatter(body: str) -> str:
    assert body.startswith("---\n"), "deck must start with YAML frontmatter"
    end = body.find("\n---\n", 4)
    assert end != -1, "deck frontmatter not closed"
    return body[4:end]


def main() -> None:
    pack = load(PACK)
    items = [
        item
        for item in pack.get("content_items", [])
        if isinstance(item, dict) and item.get("kind") == "module"
    ]

    expected_paths: list[Path] = []
    expected_numbers = list(range(0, 31))
    actual_numbers: list[int] = []
    for item in items:
        lesson = Path(str(item["path"]))
        match = re.match(r"^(\d{2})_", lesson.name)
        assert match, f"non-canonical lesson filename: {lesson.name}"
        number = int(match.group(1))
        expected_paths.append(SLIDES_ROOT / lesson.name)
        actual_numbers.append(number)

    assert actual_numbers == expected_numbers, (
        f"expected M00-M30 catalog order, found {actual_numbers}"
    )
    assert len(expected_paths) == 31, f"expected M00-M30 decks, found {len(expected_paths)}"

    actual_paths = sorted(SLIDES_ROOT.glob("[0-9][0-9]_*.md"))
    assert set(actual_paths) == set(expected_paths), (
        f"slide source/catalog drift: expected-only={sorted(str(p.relative_to(ROOT)) for p in set(expected_paths)-set(actual_paths))}, "
        f"actual-only={sorted(str(p.relative_to(ROOT)) for p in set(actual_paths)-set(expected_paths))}"
    )

    for path in sorted(expected_paths):
        body = read(path)
        fm = frontmatter(body)
        number = int(path.name[:2])
        module = f"M{number:02d}"

        assert "marp: true" in fm, f"{path.name}: marp:true missing"
        assert "paginate: true" in fm, f"{path.name}: paginate:true missing"
        assert "size: 16:9" in fm, f"{path.name}: 16:9 missing"
        assert re.search(r"(?m)^title:\s*.+$", fm), f"{path.name}: title missing"
        assert f"# {module} —" in body, f"{path.name}: canonical module H1 missing"

        for marker in FORBIDDEN_STUDENT_DECK_MARKERS:
            assert marker not in body, f"{path.name}: internal delivery marker leaked: {marker}"

        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            normalized = target.replace("\\", "/").lower()
            wrapped = f"/{normalized}"
            assert "/teacher/" not in wrapped, f"{path.name}: teacher link leaked: {target}"
            assert "/solution/" not in wrapped, f"{path.name}: solution link leaked: {target}"
            assert "/hidden_tests/" not in wrapped, f"{path.name}: hidden-test link leaked: {target}"

        separators = body.count("\n---\n")
        assert separators >= 5, f"{path.name}: suspiciously small deck ({separators} separators)"

    print("PASS: 31/31 M00-M30 Marp source decks satisfy student-facing source quality gates")


if __name__ == "__main__":
    main()

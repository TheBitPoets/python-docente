from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import zipfile
from pathlib import Path

try:
    import pypdf
    from pypdf import PdfReader
except ModuleNotFoundError as error:
    raise SystemExit(
        "pypdf is required for slide artifact QA; install requirements-slide-release.txt"
    ) from error


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "slide-build-profile.json"
TARGET_ASPECT_RATIO = 16 / 9


def load_json(path: Path) -> dict:
    assert path.is_file(), f"missing file: {path.relative_to(ROOT)}"
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"JSON root must be object: {path.relative_to(ROOT)}"
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_slide_count(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines and lines[0].strip() == "---", f"{path.name}: missing frontmatter"
    frontmatter_end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    return 1 + sum(1 for line in lines[frontmatter_end + 1 :] if line.strip() == "---")


def html_slide_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    count = len(re.findall(r"<section(?:\s|>)", text, flags=re.IGNORECASE))
    assert count > 0, f"{path.relative_to(ROOT)}: no rendered <section> slides found"
    return count


def pdf_structure(path: Path) -> tuple[int, list[float]]:
    data = path.read_bytes()
    assert data.startswith(b"%PDF-"), f"{path.relative_to(ROOT)}: invalid PDF header"
    assert b"%%EOF" in data[-4096:], f"{path.relative_to(ROOT)}: missing PDF EOF marker"

    try:
        reader = PdfReader(path, strict=True)
    except Exception as error:  # pypdf exposes several parser-specific exception types
        raise AssertionError(f"{path.relative_to(ROOT)}: PDF page tree is not readable: {error}") from error

    assert not reader.is_encrypted, f"{path.relative_to(ROOT)}: release PDF must not be encrypted"
    count = len(reader.pages)
    assert count > 0, f"{path.relative_to(ROOT)}: PDF contains no pages"

    ratios: list[float] = []
    for index, page in enumerate(reader.pages, start=1):
        box = page.mediabox
        width = float(box.width)
        height = float(box.height)
        assert width > 0 and height > 0, (
            f"{path.relative_to(ROOT)}: page {index} has invalid MediaBox {box}"
        )
        ratio = width / height
        ratios.append(ratio)
        assert math.isclose(ratio, TARGET_ASPECT_RATIO, rel_tol=0.015), (
            f"{path.relative_to(ROOT)}: page {index} MediaBox ratio {ratio:.4f} is not ~16:9"
        )
        rotation = int(page.get("/Rotate", 0) or 0) % 360
        assert rotation in {0, 180}, (
            f"{path.relative_to(ROOT)}: page {index} uses unexpected rotation {rotation}; "
            "landscape geometry must come from MediaBox"
        )

    return count, ratios


def pptx_slide_count(path: Path) -> int:
    assert zipfile.is_zipfile(path), f"{path.relative_to(ROOT)}: PPTX is not a valid ZIP package"
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        assert "[Content_Types].xml" in names, f"{path.relative_to(ROOT)}: missing [Content_Types].xml"
        assert "ppt/presentation.xml" in names, f"{path.relative_to(ROOT)}: missing presentation.xml"
        slides = [
            name
            for name in names
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
        ]
    assert slides, f"{path.relative_to(ROOT)}: no slide XML parts"
    return len(slides)


def verify_artifact_entry(entry: dict, expected_slide_count: int, kind: str) -> int:
    artifact = entry["artifacts"][kind]
    path = ROOT / str(artifact["path"])
    assert path.is_file(), f"{entry['module']} {kind}: missing artifact"
    assert path.stat().st_size == int(artifact["bytes"]), f"{entry['module']} {kind}: byte-size drift"
    assert path.stat().st_size > 1000, f"{entry['module']} {kind}: suspiciously small artifact"
    assert sha256(path) == artifact["sha256"], f"{entry['module']} {kind}: SHA-256 drift"

    if kind == "html":
        count = html_slide_count(path)
    elif kind == "pdf":
        count, _ = pdf_structure(path)
    elif kind == "pptx":
        count = pptx_slide_count(path)
    else:
        raise AssertionError(f"unknown artifact kind: {kind}")

    assert count == expected_slide_count, (
        f"{entry['module']} {kind}: rendered count {count} != source slide count {expected_slide_count}"
    )
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated HTML/PDF/PPTX slide artifacts.")
    parser.add_argument(
        "--manifest",
        default="dist/slides/python/build-manifest.json",
        help="Build manifest path relative to repository root",
    )
    args = parser.parse_args()

    profile = load_json(PROFILE_PATH)
    manifest_path = ROOT / args.manifest
    manifest = load_json(manifest_path)

    assert manifest.get("schema_version") == "python.slide-artifact-manifest.v1"
    assert manifest.get("course_id") == profile["course_id"]
    assert manifest.get("source_commit_sha"), "manifest source_commit_sha missing"
    assert manifest.get("build_id"), "manifest build_id missing"

    pdf_parser = profile["quality"]["pdf_parser"]
    assert pdf_parser["package"] == "pypdf"
    expected_pypdf = str(pdf_parser["version"])
    assert pypdf.__version__ == expected_pypdf, (
        f"pypdf version drift: installed={pypdf.__version__}, expected={expected_pypdf}"
    )

    toolchain = manifest.get("toolchain") or {}
    assert toolchain.get("container_image") == profile["runtime"]["image_ref"]
    assert toolchain.get("container_digest") == profile["runtime"]["image_digest"]
    assert toolchain.get("platform") == profile["runtime"]["platform"]
    assert str(profile["renderer"]["version"]) in str(toolchain.get("marp_cli"))
    assert str(profile["runtime"]["node_version"]) in str(toolchain.get("node"))
    assert toolchain.get("browser"), "browser reported version missing"
    assert toolchain.get("pdf_parser") == f"pypdf {expected_pypdf}", (
        f"manifest PDF parser provenance mismatch: {toolchain.get('pdf_parser')!r}"
    )

    first = int(profile["module_range"]["first"])
    last = int(profile["module_range"]["last"])
    expected_modules = [f"M{number:02d}" for number in range(first, last + 1)]
    entries = manifest.get("modules") or []
    assert isinstance(entries, list)
    assert manifest.get("module_count") == len(expected_modules)
    assert [entry.get("module") for entry in entries] == expected_modules

    for entry in entries:
        module = str(entry["module"])
        source = ROOT / str(entry["source"])
        assert source.is_file(), f"{module}: missing source"
        assert sha256(source) == entry["source_sha256"], f"{module}: source SHA drift"
        expected_count = source_slide_count(source)
        assert expected_count == int(entry["expected_slide_count"]), f"{module}: source slide-count drift"

        counts = {
            kind: verify_artifact_entry(entry, expected_count, kind)
            for kind in ("html", "pdf", "pptx")
        }
        assert len(set(counts.values())) == 1, f"{module}: artifact formats disagree: {counts}"

    print(
        f"PASS: {len(entries)}/27 slide modules have complete HTML/PDF/PPTX artifacts "
        "with matching source/rendered counts, real PDF page-tree validation and provenance hashes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

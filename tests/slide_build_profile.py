from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "config" / "slide-build-profile.json"
EXPECTED_RENDERER = "4.5.0"
EXPECTED_PLATFORM = "linux/amd64"
EXPECTED_IMAGE_DIGEST = "sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87"
EXPECTED_MANIFEST_DIGEST = "sha256:4982f2f4e9b9ba6dc97f5cbb0eb0e286ae7654642ccf0778169d57c1c552a65a"
EXPECTED_NODE = "26.5.0"
EXPECTED_PDF_PARSER = "pypdf"
EXPECTED_PDF_PARSER_VERSION = "6.16.2"
EXPECTED_RELEASE_REQUIREMENTS = "requirements-slide-release.txt"
EXPECTED_VISUAL_SAMPLE = [0, 1, 2, 3, 4, 11, 18, 22, 26, 30]


def main() -> int:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert isinstance(profile, dict)

    renderer = profile["renderer"]
    assert renderer["package"] == "@marp-team/marp-cli"
    assert renderer["version"] == EXPECTED_RENDERER
    assert renderer["release_tag"] == f"v{EXPECTED_RENDERER}"
    assert renderer["status"] == "pinned"
    assert renderer["latest_alias_forbidden"] is True
    assert "latest" not in str(renderer["version"]).lower()

    runtime = profile["runtime"]
    assert runtime["strategy"] == "official-container-by-immutable-digest"
    assert runtime["platform"] == EXPECTED_PLATFORM
    assert runtime["image_digest"] == EXPECTED_IMAGE_DIGEST
    assert runtime["multiarch_manifest_digest"] == EXPECTED_MANIFEST_DIGEST
    assert runtime["node_version"] == EXPECTED_NODE
    assert runtime["browser_kind"] == "chromium"
    assert runtime["browser_pin"] == "exact-binary-contained-in-image-digest"
    assert runtime["browser_version_recorded_at_build"] is True
    assert runtime["status"] == "pinned-by-container-digest"

    image_ref = str(runtime["image_ref"])
    assert image_ref == f"ghcr.io/marp-team/marp-cli@{EXPECTED_IMAGE_DIGEST}"
    assert re.fullmatch(r"ghcr\.io/marp-team/marp-cli@sha256:[0-9a-f]{64}", image_ref)
    assert ":latest" not in image_ref

    modules = profile["module_range"]
    assert modules == {"first": 0, "last": 30, "expected_count": 31}

    outputs = profile["outputs"]
    assert outputs["root"] == "dist/slides/python"
    for kind, filename in (("html", "deck.html"), ("pdf", "deck.pdf"), ("pptx", "deck.pptx")):
        assert outputs[kind]["required"] is True
        assert outputs[kind]["filename"] == filename
    assert outputs["pptx"]["editability_claim"] == "not-assumed-until-verified"
    assert outputs["manifest"] == "dist/slides/python/build-manifest.json"

    quality = profile["quality"]
    assert quality["source_gate"] == "tests/slide_source_quality.py"
    assert quality["artifact_structural_gate"] == "tests/slide_artifact_quality.py"
    assert quality["release_requirements"] == EXPECTED_RELEASE_REQUIREMENTS
    assert quality["pdf_parser"] == {
        "package": EXPECTED_PDF_PARSER,
        "version": EXPECTED_PDF_PARSER_VERSION,
        "policy": "real-page-tree-and-mediabox-validation",
    }
    assert quality["visual_review_required"] is True
    assert quality["visual_review_sample_modules"] == EXPECTED_VISUAL_SAMPLE

    requirements_path = ROOT / EXPECTED_RELEASE_REQUIREMENTS
    assert requirements_path.is_file(), "slide release requirements file missing"
    requirements = [
        line.strip()
        for line in requirements_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    assert requirements == [f"{EXPECTED_PDF_PARSER}=={EXPECTED_PDF_PARSER_VERSION}"], (
        f"slide release PDF parser must be exactly pinned: {requirements}"
    )

    build = profile["build"]
    assert build["entrypoint"] == "scripts/build_slide_artifacts.py"
    assert build["browser"] == "chrome"
    assert build["clean_output_before_build"] is True
    assert build["generated_artifacts_committed"] is False

    provenance = profile["provenance"]
    assert provenance["pdf_parser_version_required"] is True

    for rel in (
        "scripts/build_slide_artifacts.py",
        "tests/slide_artifact_quality.py",
        "tests/slide_source_quality.py",
        EXPECTED_RELEASE_REQUIREMENTS,
        "doc/SLIDE_ARTIFACT_PIPELINE.md",
    ):
        assert (ROOT / rel).is_file(), f"missing slide pipeline file: {rel}"

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert "dist/" in gitignore, "generated dist/ artifacts must stay untracked"

    print(
        "PASS: slide build profile pins M00-M30 + Marp 4.5.0 + linux/amd64 immutable container "
        "+ pypdf 6.16.2 structural PDF QA"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

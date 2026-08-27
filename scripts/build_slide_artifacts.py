from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "slide-build-profile.json"
PACK_PATH = ROOT / "content" / "python" / "content-pack.json"


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"JSON root is not an object: {path.relative_to(ROOT)}")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_slide_count(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise AssertionError(f"{path.relative_to(ROOT)}: missing Marp frontmatter")
    try:
        frontmatter_end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise AssertionError(f"{path.relative_to(ROOT)}: unclosed frontmatter") from exc
    return 1 + sum(1 for line in lines[frontmatter_end + 1 :] if line.strip() == "---")


def module_sources(pack: dict, profile: dict) -> list[tuple[str, Path]]:
    first = int(profile["module_range"]["first"])
    last = int(profile["module_range"]["last"])
    expected_count = int(profile["module_range"]["expected_count"])

    result: list[tuple[str, Path]] = []
    for item in sorted(
        [x for x in pack.get("content_items", []) if isinstance(x, dict) and x.get("kind") == "module"],
        key=lambda x: int(x.get("order", 0)),
    ):
        number = int(item.get("order", 0))
        if not first <= number <= last:
            continue
        lesson = Path(str(item["path"]))
        slide = ROOT / profile["source_root"] / lesson.name
        if not slide.is_file():
            raise AssertionError(f"missing slide source: {slide.relative_to(ROOT)}")
        result.append((f"M{number:02d}", slide))

    expected_modules = [f"M{number:02d}" for number in range(first, last + 1)]
    actual_modules = [module for module, _ in result]
    if actual_modules != expected_modules or len(result) != expected_count:
        raise AssertionError(
            f"slide source range mismatch: expected={expected_modules}, actual={actual_modules}"
        )
    return result


def run(command: list[str], *, capture: bool = False) -> str:
    print("+", " ".join(command))
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    if completed.returncode != 0:
        output = completed.stdout or ""
        raise SystemExit(f"command failed ({completed.returncode}): {' '.join(command)}\n{output}")
    return (completed.stdout or "").strip()


def docker_common(profile: dict, *, mount_repo: bool) -> list[str]:
    runtime = profile["runtime"]
    command = [
        "docker",
        "run",
        "--rm",
        "--init",
        "--platform",
        str(runtime["platform"]),
    ]
    if mount_repo:
        command.extend(["-v", f"{ROOT}:/home/marp/app", "-e", "LANG=C.UTF-8"])
        if hasattr(os, "getuid") and hasattr(os, "getgid"):
            command.extend(["-e", f"MARP_USER={os.getuid()}:{os.getgid()}"])
    command.append(str(runtime["image_ref"]))
    return command


def toolchain_versions(profile: dict) -> dict:
    runtime = profile["runtime"]
    image = str(runtime["image_ref"])
    base = ["docker", "run", "--rm", "--platform", str(runtime["platform"])]

    marp = run(base + [image, "--version"], capture=True)
    node = run(base + ["--entrypoint", "node", image, "--version"], capture=True)
    browser = run(
        base + ["--entrypoint", str(runtime["browser_binary"]), image, "--version"],
        capture=True,
    )

    expected_renderer = str(profile["renderer"]["version"])
    if expected_renderer not in marp:
        raise AssertionError(f"renderer mismatch: expected {expected_renderer!r}, reported {marp!r}")
    expected_node = str(runtime["node_version"])
    if expected_node not in node:
        raise AssertionError(f"Node mismatch: expected {expected_node!r}, reported {node!r}")

    return {
        "marp_cli": marp,
        "node": node,
        "browser": browser,
        "container_image": image,
        "container_digest": runtime["image_digest"],
        "platform": runtime["platform"],
    }


def source_commit_sha() -> str:
    env_sha = os.environ.get("GITHUB_SHA") or os.environ.get("SOURCE_COMMIT_SHA")
    if env_sha:
        return env_sha
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if completed.returncode != 0 or not completed.stdout.strip():
        raise SystemExit("source commit SHA unavailable; set SOURCE_COMMIT_SHA")
    return completed.stdout.strip()


def build_one(profile: dict, module: str, source: Path, output_root: Path) -> dict:
    module_dir = output_root / module
    module_dir.mkdir(parents=True, exist_ok=True)

    html = module_dir / profile["outputs"]["html"]["filename"]
    pdf = module_dir / profile["outputs"]["pdf"]["filename"]
    pptx = module_dir / profile["outputs"]["pptx"]["filename"]

    source_rel = source.relative_to(ROOT).as_posix()
    html_rel = html.relative_to(ROOT).as_posix()
    pdf_rel = pdf.relative_to(ROOT).as_posix()
    pptx_rel = pptx.relative_to(ROOT).as_posix()

    common = docker_common(profile, mount_repo=True)
    run(common + [source_rel, "-o", html_rel, "--allow-local-files"])
    run(common + [source_rel, "--pdf", "--browser", str(profile["build"]["browser"]), "-o", pdf_rel, "--allow-local-files"])
    run(common + [source_rel, "--pptx", "--browser", str(profile["build"]["browser"]), "-o", pptx_rel, "--allow-local-files"])

    artifacts = {}
    for kind, path in (("html", html), ("pdf", pdf), ("pptx", pptx)):
        if not path.is_file() or path.stat().st_size <= 0:
            raise AssertionError(f"{module}: missing/empty {kind} artifact")
        artifacts[kind] = {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

    return {
        "module": module,
        "source": source_rel,
        "source_sha256": sha256(source),
        "expected_slide_count": source_slide_count(source),
        "artifacts": artifacts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build reproducible M04–M30 Marp release artifacts.")
    parser.add_argument("--build-id", help="Release/build identifier recorded in the manifest")
    parser.add_argument("--keep", action="store_true", help="Do not clean dist/slides/python first")
    args = parser.parse_args()

    if shutil.which("docker") is None:
        raise SystemExit("Docker is required for the pinned slide release build")

    profile = load_json(PROFILE_PATH)
    pack = load_json(PACK_PATH)
    if profile["renderer"]["status"] != "pinned":
        raise SystemExit("slide renderer profile is not pinned")

    output_root = ROOT / profile["outputs"]["root"]
    if output_root.exists() and not args.keep:
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    versions = toolchain_versions(profile)
    commit_sha = source_commit_sha()
    build_id = args.build_id or os.environ.get("GITHUB_RUN_ID") or f"local-{commit_sha[:12]}"

    modules = []
    for module, source in module_sources(pack, profile):
        print(f"\n== {module}: {source.name} ==")
        modules.append(build_one(profile, module, source, output_root))

    manifest = {
        "schema_version": "python.slide-artifact-manifest.v1",
        "course_id": profile["course_id"],
        "source_commit_sha": commit_sha,
        "build_id": str(build_id),
        "built_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "toolchain": versions,
        "module_count": len(modules),
        "modules": modules,
    }
    manifest_path = ROOT / profile["outputs"]["manifest"]
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    run([sys.executable, "tests/slide_artifact_quality.py", "--manifest", manifest_path.relative_to(ROOT).as_posix()])
    print(f"\nPASS: built {len(modules)} complete HTML/PDF/PPTX slide sets")
    print(f"manifest: {manifest_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

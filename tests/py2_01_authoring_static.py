from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    0: "00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md",
    1: "01_DAL_PROBLEMA_AI_PASSI.md",
    2: "02_FLOWCHART_SEQUENZA_SELEZIONE.md",
    3: "03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md",
}
PROFILE_PATH = ROOT / "config" / "flowchart-lab-candidate.json"
ENVIRONMENT_PATH = ROOT / "config" / "course-environment.json"
STUDENT_INDEX = ROOT / "student" / "README.md"
TEACHER_INDEX = ROOT / "teacher" / "README.md"
CONSUMER_WORKFLOW = ROOT / ".github" / "workflows" / "thebitlab-python-smoke.yml"


def read(path: Path) -> str:
    assert path.is_file(), f"missing: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    value = json.loads(read(path))
    assert isinstance(value, dict), f"JSON root is not object: {path.relative_to(ROOT)}"
    return value


def assert_no_reserved_links(path: Path) -> None:
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", read(path)):
        normalized = "/" + target.replace("\\", "/").lower()
        assert "/teacher/" not in normalized, f"student surface links teacher asset: {path.name} -> {target}"
        assert "/solution/" not in normalized, f"student surface links solution: {path.name} -> {target}"
        assert "/hidden_tests/" not in normalized, f"student surface links hidden tests: {path.name} -> {target}"


def assert_pre_python_surface(number: int, body: str, *, label: str) -> None:
    """Reject Python-as-prerequisite while allowing one explicitly negative M01 example."""
    lowered = body.casefold()
    fence_count = lowered.count("```python")
    if number == 1:
        assert fence_count <= 1, f"M01 {label}: more than one Python code fence in pre-Python module"
        if fence_count:
            assert (
                "python travestito" in lowered
                or "non serve python" in lowered
                or "non scrivere" in lowered
            ), f"M01 {label}: Python fence is not explicitly framed as an anti-example"
    else:
        assert fence_count == 0, f"M{number:02d} {label}: executable Python leaked into pre-Python module"


def main() -> int:
    student_index = read(STUDENT_INDEX)
    teacher_index = read(TEACHER_INDEX)

    for number, filename in MODULES.items():
        module = f"M{number:02d}"
        lesson_path = ROOT / "content" / "python" / filename
        slide_path = ROOT / "slides" / "python" / "modules" / filename
        runbook_path = ROOT / "teacher" / f"{module}_RUNBOOK.md"

        lesson = read(lesson_path)
        slides = read(slide_path)
        runbook = read(runbook_path)

        assert lesson.startswith(f"# {module} —"), f"{module}: lesson H1 drift"
        assert slides.startswith("---\nmarp: true"), f"{module}: Marp frontmatter missing"
        assert f"# {module} —" in slides, f"{module}: deck H1 missing"
        assert runbook.startswith(f"# {module} — Runbook docente"), f"{module}: runbook H1 drift"

        assert filename in student_index, f"{module}: student index missing lesson"
        assert filename in teacher_index, f"{module}: teacher index missing lesson"
        assert f"{module}_RUNBOOK.md" in teacher_index, f"{module}: teacher index missing runbook"

        assert_no_reserved_links(lesson_path)
        assert_no_reserved_links(slide_path)
        assert_pre_python_surface(number, lesson, label="lesson")
        assert_pre_python_surface(number, slides, label="deck")

    m00 = read(ROOT / "content" / "python" / MODULES[0]).casefold()
    assert "non devi ancora scrivere codice" in m00
    assert "python e flowchart lab non sono prerequisiti" in m00

    for number in (2, 3):
        body = read(ROOT / "content" / "python" / MODULES[number]).casefold()
        assert "flowchart lab candidate" in body, f"M{number:02d}: candidate boundary missing"
        assert "fallback" in body and ("carta" in body or "lavagna" in body), f"M{number:02d}: manual fallback missing"
        assert "autograding" not in body or "non" in body, f"M{number:02d}: suspicious autograding claim"

    profile = load(PROFILE_PATH)
    assert profile["status"] == "candidate-not-certified"
    platform_ref = str((profile.get("platform") or {}).get("ref") or "")
    assert re.fullmatch(r"[0-9a-f]{40}", platform_ref), "Flowchart candidate ref must be immutable"
    consumer_workflow = read(CONSUMER_WORKFLOW)
    assert f"ref: {platform_ref}" in consumer_workflow
    assert "ref: agent/course-environment-contract" not in consumer_workflow
    policy = profile["certification_policy"]
    assert policy["candidate_ci_is_classroom_certification"] is False
    assert policy["fallback_remains_required"] is True
    assert policy["required_fallback_id"] == "flowchart.manual-evidence.v1"
    assert policy["supported_profile_rehearsal_required"] is True
    assert policy["human_usability_review_required"] is True

    environment = load(ENVIRONMENT_PATH)
    fallbacks = (environment.get("capabilities") or {}).get("fallback") or []
    flowchart = [
        item for item in fallbacks
        if isinstance(item, dict) and item.get("capability") == "flowchart.lab.v1"
    ]
    assert len(flowchart) == 1
    assert flowchart[0].get("fallback_id") == "flowchart.manual-evidence.v1"

    activity_root = ROOT / "activities" / "python"
    for activity_json in activity_root.glob("*/activity.json"):
        activity = load(activity_json)
        runtime = activity.get("runtime") or {}
        assert runtime.get("runtime_id") != "flowchart-lab", (
            f"Flowchart Activity materialized before certification: {activity_json.relative_to(ROOT)}"
        )

    print(
        "PASS: PY2-01 M00-M03 draft authoring surfaces preserve pre-Python pedagogy, "
        "candidate Flowchart boundary and mandatory manual fallback"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

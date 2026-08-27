from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_REL = Path("activities/python/py2-activity-b-input-somma-001/activity.json")
ACTIVITY_ROOT = ROOT / ACTIVITY_REL.parent
ACTIVITY_ID = "py2-activity-b-input-somma-001"
THEBITLAB_REF = "cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0"
EXPECTED_STUDENT_FILES = {"README.md", "activity.json", "main.py", "GUIDA.md"}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"JSON non oggetto: {path}")
    return value


def assert_public_scaffold(scaffold: Path) -> None:
    actual = {
        path.relative_to(scaffold).as_posix()
        for path in scaffold.rglob("*")
        if path.is_file()
    }
    if actual != EXPECTED_STUDENT_FILES:
        fail(f"Scaffold gestito inatteso: {sorted(actual)}")

    public_activity = load_json(scaffold / "activity.json")
    for forbidden in ("test_cases", "rubrica"):
        if forbidden in public_activity:
            fail(f"Metadata docente esposti nello scaffold: {forbidden}")

    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    for marker in ("expected_stdout", "teacher_only", "hidden_test", "solution/"):
        if marker in serialized:
            fail(f"Marker riservato nello scaffold: {marker}")

    readme = (scaffold / "README.md").read_text(encoding="utf-8")
    if THEBITLAB_REF not in readme:
        fail("README studente non conserva il baseline TheBitLab pinned")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
    sys.path.insert(0, str(platform))
    from scripts import course_board_server

    with tempfile.TemporaryDirectory(prefix="python-docente-managed-assignment-") as raw_temp:
        course_root = Path(raw_temp) / "course"
        activity_target = course_root / ACTIVITY_REL.parent
        activity_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ACTIVITY_ROOT, activity_target)

        student_repo = course_root / "students" / "student-one"
        student_repo.mkdir(parents=True)

        course_board_server.configure_data_root(course_root)
        payload = {
            "activity_path": ACTIVITY_REL.as_posix(),
            "targets_text": str(student_repo),
            "language": "python",
            "thebitlab_ref": THEBITLAB_REF,
            "overwrite": False,
            "overwrite_source": False,
        }

        preview = course_board_server.preview_activity_assignment(payload)
        if preview.get("ok") is not True:
            fail(f"Preview managed non riuscita: {preview}")
        plan = preview.get("plan") or {}
        if plan.get("activity_id") != ACTIVITY_ID or plan.get("can_assign") is not True:
            fail(f"Piano managed inatteso: {plan}")
        if plan.get("blocked_targets"):
            fail(f"Target nuovo già bloccato: {plan.get('blocked_targets')}")

        student_assets = {
            (asset.get("type"), asset.get("target_path"))
            for asset in plan.get("student_assets", [])
            if isinstance(asset, dict)
        }
        if student_assets != {("starter", "main.py"), ("fixture", "GUIDA.md")}:
            fail(f"Asset studente preview inattesi: {student_assets}")
        teacher_assets = {
            asset.get("type")
            for asset in plan.get("teacher_assets", [])
            if isinstance(asset, dict)
        }
        if "teacher_only" not in teacher_assets:
            fail("Preview managed non separa l'asset teacher_only")

        distributed = course_board_server.distribute_activity_assignment(payload)
        if distributed.get("ok") is not True:
            fail(f"Distribuzione managed non riuscita: {distributed}")
        results = distributed.get("results") or []
        if len(results) != 1:
            fail(f"Numero risultati distribuzione inatteso: {results}")

        scaffold = student_repo / "assignments" / ACTIVITY_ID
        if not scaffold.is_dir():
            fail(f"Scaffold managed non creato: {scaffold}")
        assert_public_scaffold(scaffold)

        second_preview = course_board_server.preview_activity_assignment(payload)
        second_plan = second_preview.get("plan") or {}
        if second_plan.get("can_assign") is not False:
            fail("Seconda preview non rileva la consegna già esistente")
        blocked = {Path(value).resolve() for value in second_plan.get("blocked_targets", [])}
        if student_repo.resolve() not in blocked:
            fail(f"Target distribuito non compare tra i blocked target: {blocked}")

    print(
        "PASS: Course Workspace Activity preview -> managed distribution -> "
        "redacted student scaffold -> existing-assignment detection"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

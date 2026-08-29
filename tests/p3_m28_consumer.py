from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "p3-canary-profile.json"
PROFILE = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
ACTIVITY = ROOT / str(PROFILE["activity_path"])
ACTIVITY_ROOT = ACTIVITY.parent
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"
STUDENT_GUIDE = ACTIVITY_ROOT / "student" / "GUIDA.md"
EXPECTED_FILES = set(PROFILE["student_scaffold_files"])
EXPECTED_CASES = int(PROFILE["expected_cases"])
THEBITLAB_REF = str(PROFILE["thebitlab"]["ref"])
PROFILE_ID = str(PROFILE["thebitlab"]["profile"])
INHERITED_MANIFEST_VERSION = str(
    PROFILE["authoritative_grading"]["inherited_manifest_version"]
)
SCENARIO_MARKERS = {
    "stato iniziale",
    "aggiunta valida",
    "overflow rifiutato senza cambiare stato",
    "quantita negativa rifiutata",
    "istanze indipendenti",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        fail(f"{path}: JSON root non object")
    return value


def run_module(
    platform: Path,
    module: str,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", module, *args],
        cwd=platform,
        check=check,
        capture_output=True,
        text=True,
    )


def assert_platform(platform: Path) -> None:
    revision = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip().lower()
    if revision != THEBITLAB_REF:
        fail(f"P3 platform mismatch: expected {THEBITLAB_REF}, found {revision}")

    manifest = load_object(platform / "docker" / "assignment-runner" / "toolchain.json")
    lock = load_object(platform / "docker" / "assignment-runner" / "toolchain.lock.json")
    if manifest.get("version") != INHERITED_MANIFEST_VERSION:
        fail(
            "P3 inherited manifest mismatch: "
            f"expected {INHERITED_MANIFEST_VERSION}, found {manifest.get('version')}"
        )
    if PROFILE["certification_policy"]["distinct_release_identity_required_before_publish"] is not True:
        fail("P3 consumer deve impedire la pubblicazione sotto l'identita ereditata")
    if lock.get("version") == manifest.get("version"):
        fail("P3 source candidate non deve fingere che il manifest sia gia il lock stabile")

    sys.path.insert(0, str(platform))
    try:
        from scripts import python_object_profile, validate_activity

        if python_object_profile.PROFILE_ID != PROFILE_ID:
            fail(
                f"P3 profile mismatch: expected {PROFILE_ID}, "
                f"found {python_object_profile.PROFILE_ID}"
            )
        activity = load_object(ACTIVITY)
        errors = validate_activity.validate_activity(activity, str(ACTIVITY))
        if errors:
            fail("P3 Activity non valida:\n- " + "\n- ".join(errors))
    finally:
        sys.path.remove(str(platform))


def assert_student_scaffold(platform: Path, temp: Path) -> None:
    target = temp / "student-repo"
    target.mkdir()
    run_module(
        platform,
        "scripts.create_submission_scaffold",
        "--activity",
        str(ACTIVITY),
        "--target",
        str(target),
        "--thebitlab-ref",
        THEBITLAB_REF,
    )
    scaffold = target / "assignments" / PROFILE["activity_id"]
    if not scaffold.is_dir():
        fail(f"P3 scaffold non creato: {scaffold}")
    files = {
        path.relative_to(scaffold).as_posix()
        for path in scaffold.rglob("*")
        if path.is_file()
    }
    if files != EXPECTED_FILES:
        fail(
            f"P3 scaffold surface mismatch: missing={sorted(EXPECTED_FILES-files)}, "
            f"unexpected={sorted(files-EXPECTED_FILES)}"
        )
    if (scaffold / "main.py").read_bytes() != STARTER.read_bytes():
        fail("P3 scaffold main.py non coincide con lo starter")
    if (scaffold / "GUIDA.md").read_bytes() != STUDENT_GUIDE.read_bytes():
        fail("P3 scaffold GUIDA.md non coincide con la guida")

    public_activity = load_object(scaffold / "activity.json")
    if "object_tests" in public_activity:
        fail("object_tests teacher-only leaked into student scaffold")
    serialized = json.dumps(public_activity, ensure_ascii=False).casefold()
    forbidden = {
        "expected_return",
        "expected_exception",
        "expected_constructor_exception",
        "additional_instances",
        *SCENARIO_MARKERS,
    }
    for marker in forbidden:
        if marker.casefold() in serialized:
            fail(f"P3 teacher oracle leaked into student scaffold: {marker}")


def grade_via_execution_service(
    platform: Path,
    source: Path,
    image: str,
) -> tuple[object, dict]:
    sys.path.insert(0, str(platform))
    try:
        from scripts.thebitlab_technical_services import (
            DockerGradeActivityExecutionService,
            ExecutionRequest,
        )

        execution = DockerGradeActivityExecutionService().run(
            ExecutionRequest(
                activity_id=PROFILE["activity_id"],
                student_id="p3-canary-student",
                files={"main.py": str(source)},
                language="python",
                timeout_seconds=5,
                metadata={
                    "activity_path": ACTIVITY,
                    "source_path": source,
                    "docker_image": image,
                },
            )
        )
    finally:
        sys.path.remove(str(platform))

    report = execution.metadata.get("runner_report")
    if not isinstance(report, dict):
        fail(
            "P3 normal Docker ExecutionService non ha prodotto runner_report: "
            f"status={execution.status!r}, detail={execution.detail!r}, "
            f"metadata={execution.metadata!r}"
        )
    if execution.metadata.get("grading_profile") != PROFILE_ID:
        fail(f"P3 ExecutionService non ha dichiarato il profilo atteso: {execution.metadata}")
    return execution, report


def assert_grading(platform: Path, image: str) -> None:
    solution_execution, solution = grade_via_execution_service(platform, SOLUTION, image)
    if solution_execution.status != "passed" or solution.get("passed") is not True:
        fail(
            "P3 solution non passa nel normale ExecutionService: "
            f"status={solution_execution.status}, report={solution}"
        )
    if solution.get("profile") != PROFILE_ID:
        fail(f"P3 solution report profile inatteso: {solution}")
    if solution.get("summary") != {
        "passed": PROFILE["expected_solution_passed"],
        "total": EXPECTED_CASES,
    }:
        fail(f"P3 solution summary inatteso: {solution.get('summary')}")

    starter_execution, starter = grade_via_execution_service(platform, STARTER, image)
    if starter_execution.status != "failed" or starter.get("passed") is True:
        fail(
            "P3 starter non discrimina l'invariante nel normale ExecutionService: "
            f"status={starter_execution.status}, report={starter}"
        )
    if starter.get("summary") != {
        "passed": PROFILE["expected_starter_passed"],
        "total": EXPECTED_CASES,
    }:
        fail(f"P3 starter summary inatteso: {starter.get('summary')}")
    if any(test.get("worker_status") != "completed" for test in starter.get("tests", [])):
        fail(f"P3 starter deve eseguire tutti gli scenari senza crashare: {starter}")

    failed = {test.get("name") for test in starter.get("tests", []) if not test.get("passed")}
    expected_failed = {
        "overflow rifiutato senza cambiare stato",
        "quantita negativa rifiutata",
    }
    if failed != expected_failed:
        fail(f"P3 starter fallisce scenari inattesi: {failed}")

    overflow = next(
        test
        for test in starter["tests"]
        if test.get("name") == "overflow rifiutato senza cambiare stato"
    )
    negative = next(
        test
        for test in starter["tests"]
        if test.get("name") == "quantita negativa rifiutata"
    )
    if overflow["observations"][1].get("actual_return") is not True:
        fail(f"P3 starter overflow dovrebbe accettare erroneamente la seconda aggiunta: {overflow}")
    if overflow["observations"][2].get("actual_value") != 12:
        fail(f"P3 starter overflow dovrebbe violare il livello atteso: {overflow}")
    if negative["observations"][0].get("actual_return") is not True:
        fail(f"P3 starter quantita negativa dovrebbe essere accettata erroneamente: {negative}")
    if negative["observations"][1].get("actual_value") != -1:
        fail(f"P3 starter quantita negativa dovrebbe violare l'invariante: {negative}")


def student_lab_report(
    platform: Path,
    temp: Path,
    image: str,
    source: Path,
    label: str,
) -> dict:
    lab_root = temp / f"lab-{label}"
    activity_path = lab_root / "activities" / "activity.json"
    workspace_rel = Path("students") / "rossi-mario" / "assignments" / PROFILE["activity_id"]
    workspace = lab_root / workspace_rel
    activity_path.parent.mkdir(parents=True)
    workspace.mkdir(parents=True)
    activity_path.write_bytes(ACTIVITY.read_bytes())
    (workspace / "main.py").write_bytes(source.read_bytes())
    assignment = {
        "assignment_id": f"assignment-{PROFILE['activity_id']}-{label}",
        "activity_id": PROFILE["activity_id"],
        "student_id": "rossi-mario",
        "activity": {"path": "activities/activity.json"},
        "workspace": {"path": workspace_rel.as_posix()},
    }

    sys.path.insert(0, str(platform))
    try:
        from scripts import student_lab_runner

        return student_lab_runner.run_docker_assignment(
            assignment,
            root=lab_root,
            timeout_seconds=5,
            docker_image=image,
        )
    finally:
        sys.path.remove(str(platform))


def assert_public_report(report: dict, *, passed: int, total: int) -> None:
    if report.get("backend") != "docker" or report.get("profile") != PROFILE_ID:
        fail(f"P3 Student Lab metadata inattesi: {report}")
    if report.get("summary") != {"passed": passed, "total": total}:
        fail(f"P3 Student Lab summary inatteso: {report.get('summary')}")
    tests = report.get("tests")
    if not isinstance(tests, list) or len(tests) != total:
        fail(f"P3 Student Lab tests inattesi: {tests}")
    expected_names = [f"Test {index}" for index in range(1, total + 1)]
    if [test.get("name") for test in tests] != expected_names:
        fail(f"P3 Student Lab non ha redatto i nomi teacher-side: {tests}")

    serialized = json.dumps(report, ensure_ascii=False).casefold()
    forbidden = {
        "object_tests",
        "expected_return",
        "expected_exception",
        "expected_constructor_exception",
        "actual_return",
        "actual_value",
        "actual_exception",
        "observations",
        "worker_status",
        *SCENARIO_MARKERS,
    }
    for marker in forbidden:
        if marker.casefold() in serialized:
            fail(f"P3 teacher evidence leaked nel report Student Lab: {marker}")


def assert_student_lab_redaction(platform: Path, temp: Path, image: str) -> None:
    solution = student_lab_report(platform, temp, image, SOLUTION, "solution")
    if solution.get("passed") is not True or solution.get("status") != "passed":
        fail(f"P3 solution non passa nello Student Lab reale: {solution}")
    assert_public_report(solution, passed=PROFILE["expected_solution_passed"], total=EXPECTED_CASES)

    starter = student_lab_report(platform, temp, image, STARTER, "starter")
    if starter.get("passed") is True or starter.get("status") != "failed":
        fail(f"P3 starter non fallisce nello Student Lab reale: {starter}")
    assert_public_report(starter, passed=PROFILE["expected_starter_passed"], total=EXPECTED_CASES)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    parser.add_argument("--docker-image", required=True)
    args = parser.parse_args()

    if sys.version_info[:2] != tuple(int(part) for part in PROFILE["host_python"].split(".")):
        fail(
            f"P3 consumer richiede host Python {PROFILE['host_python']}; "
            f"found {sys.version_info.major}.{sys.version_info.minor}"
        )
    platform = args.platform.resolve(strict=True)
    assert_platform(platform)
    with tempfile.TemporaryDirectory(prefix="python-docente-p3-") as raw_temp:
        temp = Path(raw_temp)
        assert_student_scaffold(platform, temp)
        assert_grading(platform, args.docker_image)
        assert_student_lab_redaction(platform, temp, args.docker_image)

    print(
        "PASS: M28 P3 canary validates Activity/scaffold, proves the Serbatoio "
        "invariant through normal Docker object grading, and preserves Student Lab redaction"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

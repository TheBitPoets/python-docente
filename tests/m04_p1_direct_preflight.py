from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_ROOT = ROOT / "activities" / "python" / "py2-activity-b-input-somma-001"
ACTIVITY = ACTIVITY_ROOT / "activity.json"
STARTER = ACTIVITY_ROOT / "starter" / "main.py"
SOLUTION = ACTIVITY_ROOT / "solution" / "main.py"


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.relative_to(ROOT)}: JSON root must be an object")
    return value


def run_case(source: Path, stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(source)],
        cwd=ROOT,
        input=stdin,
        text=True,
        capture_output=True,
        timeout=2,
        check=False,
    )


def exercise(source: Path, cases: list[dict]) -> tuple[int, int]:
    passed = 0
    executed = 0
    for case in cases:
        name = str(case["name"])
        stdin = str(case["stdin"])
        expected = str(case["expected_stdout"])
        result = run_case(source, stdin)
        executed += 1
        if result.returncode != 0:
            raise AssertionError(
                f"{source.relative_to(ROOT)} / {name}: process failed "
                f"with exit={result.returncode}, stderr={result.stderr!r}"
            )
        if result.stderr:
            raise AssertionError(
                f"{source.relative_to(ROOT)} / {name}: unexpected stderr={result.stderr!r}"
            )
        if result.stdout == expected:
            passed += 1
    return passed, executed


def main() -> int:
    activity = load_object(ACTIVITY)
    cases = activity.get("test_cases")
    if not isinstance(cases, list) or len(cases) != 3:
        raise AssertionError(f"M04 P1 requires exactly 3 deterministic cases, found {cases!r}")

    names: list[str] = []
    for case in cases:
        if not isinstance(case, dict):
            raise AssertionError(f"invalid test case: {case!r}")
        if set(case) != {"name", "stdin", "expected_stdout"}:
            raise AssertionError(f"unexpected P1 test-case shape: {case!r}")
        if not all(isinstance(case[key], str) for key in ("name", "stdin", "expected_stdout")):
            raise AssertionError(f"P1 test-case values must be strings: {case!r}")
        names.append(case["name"])
    if len(names) != len(set(names)):
        raise AssertionError(f"duplicate P1 test-case names: {names}")

    solution_passed, solution_executed = exercise(SOLUTION, cases)
    if solution_executed != 3 or solution_passed != 3:
        raise AssertionError(
            f"reference solution must pass 3/3 cases; "
            f"executed={solution_executed}, passed={solution_passed}"
        )

    starter_passed, starter_executed = exercise(STARTER, cases)
    if starter_executed != 3:
        raise AssertionError(f"starter must execute all 3 cases; executed={starter_executed}")
    if starter_passed == 3:
        raise AssertionError("starter unexpectedly passes 3/3 cases: P1 test set is not discriminating")

    print(
        "PASS: M04 P1 direct preflight — "
        f"solution=3/3, starter={starter_passed}/3, executed=3/3, "
        f"python={sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    print("NOTE: this is platform-independent evidence, not authoritative Docker grading.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

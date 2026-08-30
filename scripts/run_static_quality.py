from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("authoring source synchronization", [sys.executable, "scripts/sync_authoring_catalog.py"]),
    ("source-audit manifest synchronization", [sys.executable, "scripts/sync_source_audit_manifest.py"]),
    ("authoring catalog", [sys.executable, "tests/course_authoring_catalog.py"]),
    ("PY2-01 M00-M03 authoring boundary", [sys.executable, "tests/py2_01_authoring_static.py"]),
    ("semantic review boundaries", [sys.executable, "tests/semantic_review_gate.py"]),
    ("Git G1 consumer", [sys.executable, "tests/git_g1_consumer_contract.py"]),
    ("frozen outcome coverage", [sys.executable, "tests/coverage_contract.py"]),
    ("slide source quality", [sys.executable, "tests/slide_source_quality.py"]),
    ("slide build profile pin", [sys.executable, "tests/slide_build_profile.py"]),
    ("M04 vertical-slice static QA", [sys.executable, "tests/m04_vertical_slice_static.py"]),
    ("M04 P1 certification profile", [sys.executable, "tests/p1_canary_profile.py"]),
    ("M04 P1 direct preflight", [sys.executable, "tests/m04_p1_direct_preflight.py"]),
    ("M04 vm-gui rehearsal contract", [sys.executable, "tests/m04_vm_gui_rehearsal_contract.py"]),
    ("P2/P4 combined grading alignment", [sys.executable, "tests/python_grading_toolchain_alignment.py"]),
    ("M05 pedagogical static QA", [sys.executable, "tests/m05_authoring_static.py"]),
]


def run_check(name: str, command: list[str]) -> None:
    print(f"\n== {name} ==")
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode != 0:
        raise SystemExit(
            f"FAIL: {name} exited with {completed.returncode}: {' '.join(command)}"
        )


def main() -> int:
    for name, command in CHECKS:
        run_check(name, command)

    print("\nPASS: static Python course quality suite")
    print("NOTE: this does not execute Docker slide builds or TheBitLab-dependent consumer/rehearsal gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

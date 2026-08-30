from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests import m04_vm_gui_rehearsal as rehearsal


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    starter = rehearsal.STARTER_PATH.read_text(encoding="utf-8")
    corrected = rehearsal.corrected_student_edit(starter)
    if corrected == starter:
        fail("La modifica controllata M04 non cambia lo starter")
    if "risultato = primo + secondo" not in corrected:
        fail("La modifica controllata M04 non produce la somma richiesta")
    if corrected.count("risultato = primo + secondo") != 1:
        fail("La modifica controllata M04 deve essere unica")

    guest_runner = rehearsal.GUEST_RUNNER.casefold()
    forbidden_guest_tokens = (
        "expected_stdout",
        "solution/",
        "teacher/",
        "teacher_only",
        "test_cases",
    )
    leaked = [token for token in forbidden_guest_tokens if token in guest_runner]
    if leaked:
        fail(f"Il guest runner espone dettagli docente/oracolo: {leaked}")

    sample = "\n".join(
        [
            "1,,box-name,2cornot2c/classroom-1.0.0",
            "1,,box-provider,virtualbox",
            "1,,box-version,0",
        ]
    )
    parsed = rehearsal.parse_box_list_machine_readable(sample)
    if parsed != {("2cornot2c/classroom-1.0.0", "virtualbox")}:
        fail(f"Parsing box/provider inatteso: {parsed}")

    cases = rehearsal.load_cases()
    if len(cases) != 3:
        fail("Il rehearsal M04 deve mantenere esattamente tre casi")
    if [case["name"] for case in cases] != ["positivi", "zeri", "negativo e positivo"]:
        fail("I casi M04 del rehearsal non coincidono con l'Activity canonica")

    if rehearsal.EXPECTED_ACTIVE_RELEASE != "1.0.0":
        fail("La release vm-gui attesa deve restare esplicita finché non viene ripromossa")
    if set(rehearsal.EXPECTED_HOSTS.values()) != {
        ("windows-amd64-virtualbox", "virtualbox", "x86_64"),
        ("macos-arm64-vmware", "vmware_desktop", "aarch64"),
    }:
        fail("Il rehearsal deve coprire esattamente i due profili vm-gui classroom attivi")

    print(
        "PASS: M04 vm-gui rehearsal contract — controlled student edit, host-side oracle, "
        "no solution/teacher leakage, exact active profiles"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

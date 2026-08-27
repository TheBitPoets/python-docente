from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "config" / "flowchart-lab-candidate.json"
ENVIRONMENT_PATH = ROOT / "config" / "course-environment.json"
PROFILE = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
PLATFORM_REF = str(PROFILE["platform"]["ref"])
RUNTIME_ID = str(PROFILE["runtime"]["runtime_id"])
ARTIFACT_NAME = str(PROFILE["runtime"]["artifact_name"])


def fail(message: str) -> None:
    raise AssertionError(message)


def request_json(endpoint: str, path: str, payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8")
    request = Request(
        endpoint.rstrip("/") + path,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(request, timeout=5) as response:
            raw = response.read()
    except HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        fail(f"{path} HTTP {error.code}: {body}")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        fail(f"{path}: risposta JSON non-oggetto")
    return value


def get_bytes(endpoint: str, path: str) -> tuple[str, bytes]:
    request = Request(endpoint.rstrip("/") + path, method="GET")
    with urlopen(request, timeout=5) as response:
        return response.headers.get_content_type(), response.read()


def threshold_artifact() -> dict[str, Any]:
    return {
        "schema_version": "thebitlab.flowchart.v1",
        "entry": "start",
        "nodes": [
            {"id": "start", "type": "start"},
            {
                "id": "read",
                "type": "input",
                "target": "temperatura",
                "data_type": "int",
            },
            {
                "id": "threshold",
                "type": "decision",
                "expression": "temperatura > 30",
            },
            {"id": "high", "type": "output", "expression": "'sopra soglia'"},
            {"id": "normal", "type": "output", "expression": "'entro soglia'"},
            {"id": "end", "type": "end"},
        ],
        "edges": [
            {"from": "start", "to": "read", "label": "next"},
            {"from": "read", "to": "threshold", "label": "next"},
            {"from": "threshold", "to": "high", "label": "true"},
            {"from": "threshold", "to": "normal", "label": "false"},
            {"from": "high", "to": "end", "label": "next"},
            {"from": "normal", "to": "end", "label": "next"},
        ],
        "layout": {
            "start": {"x": 450, "y": 60},
            "read": {"x": 450, "y": 170},
            "threshold": {"x": 450, "y": 290},
            "high": {"x": 260, "y": 430},
            "normal": {"x": 640, "y": 430},
            "end": {"x": 450, "y": 570},
        },
    }


def validate_course_fallback() -> None:
    environment = json.loads(ENVIRONMENT_PATH.read_text(encoding="utf-8"))
    fallbacks = (environment.get("capabilities") or {}).get("fallback") or []
    matching = [
        item
        for item in fallbacks
        if isinstance(item, dict) and item.get("capability") == "flowchart.lab.v1"
    ]
    if len(matching) != 1:
        fail("course environment deve mantenere esattamente un fallback per flowchart.lab.v1")
    expected = PROFILE["certification_policy"]["required_fallback_id"]
    if matching[0].get("fallback_id") != expected:
        fail(f"fallback Flowchart inatteso: {matching[0].get('fallback_id')!r}")
    if PROFILE["status"] != "candidate-not-certified":
        fail("il consumer Flowchart deve restare candidate-not-certified fino al rehearsal")
    if PROFILE["certification_policy"].get("candidate_ci_is_classroom_certification") is not False:
        fail("la CI candidate non deve equivalere a classroom certification")


def validate_platform_revision(platform: Path) -> None:
    revision = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip().lower()
    if revision != PLATFORM_REF:
        fail(f"Flowchart candidate mismatch: expected {PLATFORM_REF}, found {revision}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", type=Path, required=True)
    args = parser.parse_args()

    platform = args.platform.resolve(strict=True)
    validate_course_fallback()
    validate_platform_revision(platform)

    sys.path.insert(0, str(platform))
    plugin = None
    try:
        from scripts import flowchart_lab_runtime_plugin
        from scripts import thebitlab_builtin_runtimes

        builtin_names = [entry.name for entry in thebitlab_builtin_runtimes.BUILTIN_ENTRY_POINTS]
        if RUNTIME_ID not in builtin_names:
            fail(f"runtime built-in non registrato: {RUNTIME_ID}")

        plugin = flowchart_lab_runtime_plugin.create_plugin()
        descriptor = plugin.describe()
        if descriptor.get("runtime_id") != RUNTIME_ID:
            fail(f"runtime descriptor id inatteso: {descriptor}")
        if descriptor.get("plugin_version") != PROFILE["runtime"]["plugin_version"]:
            fail(f"runtime plugin version inattesa: {descriptor}")

        probe = plugin.probe()
        if probe.get("available") is not True:
            fail(f"Flowchart Lab probe non disponibile: {probe}")
        metadata = probe.get("metadata") or {}
        if metadata.get("offline") is not True or metadata.get("loopback_only") is not True:
            fail(f"probe non preserva offline/loopback boundary: {probe}")
        if metadata.get("artifact_name") != ARTIFACT_NAME:
            fail(f"artifact name inatteso nel probe: {probe}")

        with tempfile.TemporaryDirectory(prefix="python-docente-flowchart-") as raw_workspace:
            workspace = Path(raw_workspace)
            runtime_request = {
                "schema_version": PROFILE["runtime"]["request_schema"],
                "runtime_id": RUNTIME_ID,
                "paths": {"workspace": str(workspace)},
            }
            launch = plugin.launch(runtime_request)
            if launch.get("status") != "started":
                fail(f"Flowchart Lab launch non riuscito: {launch}")
            endpoint = str(launch.get("endpoint") or "")
            if not endpoint.startswith("http://127.0.0.1:"):
                fail(f"endpoint non loopback: {endpoint!r}")

            content_type, ui = get_bytes(endpoint, "/flowchart-lab/")
            if content_type != "text/html" or b"TheBitLab Flowchart Lab" not in ui:
                fail("browser UI Flowchart Lab non servita dal runtime")

            health = request_json(endpoint, "/api/workspace/status", {})
            if health.get("artifact_name") != ARTIFACT_NAME:
                fail(f"workspace status inatteso: {health}")

            artifact = threshold_artifact()
            saved = request_json(endpoint, "/api/workspace/save", {"artifact": artifact})
            if saved.get("saved") is not True:
                fail(f"artifact non salvato: {saved}")
            artifact_path = workspace / ARTIFACT_NAME
            if not artifact_path.is_file():
                fail(f"artifact gestito non creato: {artifact_path}")
            files = sorted(
                path.relative_to(workspace).as_posix()
                for path in workspace.rglob("*")
                if path.is_file()
            )
            if files != [ARTIFACT_NAME]:
                fail(f"workspace Flowchart ha scritto file inattesi: {files}")

            loaded = request_json(endpoint, "/api/workspace/load", {})
            if loaded.get("artifact") != artifact:
                fail("workspace load non preserva esattamente l'artifact salvato")

            hot = request_json(endpoint, "/api/run", {"artifact": artifact, "inputs": [31]})
            if hot.get("status") != "completed" or hot.get("outputs") != ["sopra soglia"]:
                fail(f"run true-branch inatteso: {hot}")
            if hot.get("final_variables") != {"temperatura": 31}:
                fail(f"variable watch finale inatteso: {hot}")

            session = request_json(endpoint, "/api/session", {"artifact": artifact, "inputs": [20]})
            session_id = str(session.get("session_id") or "")
            events: list[dict[str, Any]] = []
            state = session
            while not state.get("done"):
                state = request_json(endpoint, "/api/step", {"session_id": session_id})
                event = state.get("event")
                if isinstance(event, dict):
                    events.append(event)
            if state.get("outputs") != ["entro soglia"]:
                fail(f"step false-branch output inatteso: {state}")
            if state.get("variables") != {"temperatura": 20}:
                fail(f"step variable watch inatteso: {state}")
            if [event.get("node_id") for event in events] != [
                "start",
                "read",
                "threshold",
                "normal",
                "end",
            ]:
                fail(f"step path inatteso: {events}")

            svg = request_json(endpoint, "/api/svg", {"artifact": artifact})
            raw_svg = str(svg.get("svg") or "")
            if svg.get("media_type") != "image/svg+xml" or "<svg" not in raw_svg:
                fail("SVG evidence non prodotta")
            lowered_svg = raw_svg.casefold()
            if "<script" in lowered_svg or "javascript:" in lowered_svg:
                fail("SVG evidence contiene contenuto eseguibile inatteso")

            execution = plugin.run(runtime_request)
            if execution.get("status") != "runner_unavailable":
                fail(f"Flowchart runtime non deve dichiarare autograding: {execution}")
            execution_metadata = execution.get("metadata") or {}
            if execution_metadata.get("authoritative_grading") is not False:
                fail(f"Flowchart runtime ha dichiarato grading autorevole: {execution}")

            plugin.close(str(launch["session_id"]))
            plugin = None
    finally:
        if plugin is not None:
            plugin.close_all()
        try:
            sys.path.remove(str(platform))
        except ValueError:
            pass

    print(
        "PASS: PY2-01 Flowchart Lab candidate — built-in runtime probe/launch + UI + "
        "managed workspace + deterministic Run/Step/watch + SVG; authoritative grading remains disabled"
    )
    print("NOTE: candidate CI evidence is not Classroom Environment profile certification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

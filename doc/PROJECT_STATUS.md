# python-docente — project status

## Current phase

**Second-year curriculum freeze candidate + first authoring vertical slice.**

The complete second-year architecture has been designed and reviewed. Do not mass-generate the remaining lessons/slides/Activities yet: first keep the M04 vertical slice and platform gates honest.

## Current branch

`agent/course-architecture`

Draft PR:

`#1 — Draft Python curriculum architecture and second-year track`

---

# Curriculum status

## Complete second-year design

The track has:

- 33 weeks × 3 hours = 99 nominal hours;
- 30 core weeks = 90 nominal hours;
- 3 explicit checkpoint/buffer weeks = 9 hours;
- real timetable model: 2 active-theory hours + 1 lab hour;
- spiral method: test/trace/debug/naming/performance reasoning throughout;
- M00–M30 module map;
- all UDA specs `PY2_01_SPEC.md` … `PY2_10_SPEC.md`;
- mandatory OOP in weeks 29–32;
- no mandatory new prerequisite in week 33.

`tracks/secondo/ARCHITECTURE_REVIEW.md` confirms the load/dependency review and records the main density risk (PY2-07 lists/tuples), with explicit enrichment cuts before core alias/copy/data-model outcomes.

## Freeze candidate

`doc/CURRICULUM_FREEZE_CANDIDATE.md` now records the proposed stable curriculum decisions.

It is a **candidate**, not the final decision-owner freeze and not a Content Pack approval.

The candidate freezes the proposed *what/sequence/outcomes* while leaving delivery tooling independently evolvable.

---

# UDA design status

- PY2-01: algorithms / pseudocode / flow chart / trace — specified;
- PY2-02: REPL / first scripts / types / I/O / expressions — specified;
- PY2-03: Boolean logic / selection / nested decision/refactor — specified;
- PY2-04: while / for / patterns / nested loops / work intuition — specified;
- PY2-05: functions / return / scope / top-down / assert / regression — specified;
- PY2-06: strings / immutability / methods / text algorithms — specified;
- PY2-07: lists / alias-copy / tuples / matrices — specified;
- PY2-08: set / dict / frequency / nested models / data-structure choice — specified;
- PY2-09: pathlib / text files / with / predictable error boundary — specified;
- PY2-10: class / instance / init / state / composition / OOP capstone — specified.

---

# Git / Container

## Git

Git is a separate future progressive curriculum. The Python second-year G1 integration is defined in:

`tracks/secondo/GIT_G1_INTEGRATION.md`

Key decision:

```text
weeks 13–16: status/diff
Checkpoint A: first guided add/commit
second semester: commit/checkpoint routine
week 33: consolidation only, not first exposure
```

Teacher Git handouts are not needed yet. Request them when producing the definitive G1 lessons or when starting the standalone Git curriculum.

## Container

Container/Docker remains a separate future curriculum based on `kinderp/docker101` and its backlog issue #1. Python professional stages consume container literacy without duplicating that course.

---

# Romeo status

`tracks/secondo/ROMEO_MAPPING.md` is complete and pins the audited Romeo reference.

Strong selective mapping:

- PY2-03 conditions;
- PY2-04 loops;
- PY2-05 functions/top-down/debug;
- PY2-10 OOP/capstone.

No forced Romeo mapping for strings/set-dict/files.

`python-docente#4` is closed as mapping-complete.

Runtime cross-profile certification remains a platform/delivery concern.

---

# Assessment status

Assessment model/calendar are defined and `python-docente#5` is closed.

Approved minimum:

- one theory/written + one practical/practical-written assessment per quadrimester;
- formative evidence continuously through trace/debug/Activity/projects;
- autograding only for deterministic evidence; manual/rubric evidence remains first-class.

---

# TheBitLab authoring compatibility

`python-docente` is a real Course Workspace candidate:

- `doc/course_design.json` contains all 33 weeks/UDA/checkpoints;
- all ten UDA specs + architecture review + Git/Romeo mappings are indexed;
- `content/python/content-pack.json` is a draft `thebitlab.content-pack.v1`;
- Course Board can target a checkout using `course_board_server.py --root <workspace>`;
- repository remains mutable source of truth;
- Git is history/review;
- Course Bundle is immutable publication state.

Product-level `Open course` / bundle-inspection UX remains `TheBitPoets/2cornot2c#755`.

---

# Python grading profiles

Canonical design: `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

- P0 — manual/trace/design evidence;
- P1 — single-file stdin/stdout; generic runner exists, consumer certification open;
- P2 — function behavior, platform issue `2cornot2c#756`;
- P3 — object behavior, platform issue `2cornot2c#758`;
- P4 — filesystem behavior, platform issue `2cornot2c#757`;
- Romeo — external `romeo-sim` runtime plugin for domain-specific evidence.

Do not distort a P2/P3/P4 learning outcome into P1 merely because P1 exists.

---

# First technical Activity vertical slice

Activity:

`activities/python/py2-activity-b-input-somma-001/`

Includes:

- Activity 1.0 metadata;
- starter `main.py`;
- student `GUIDA.md`;
- solution;
- teacher notes;
- three deterministic stdin/stdout cases.

Certification issue:

`python-docente#7`.

Observed GitHub Actions runs currently fail before executing any workflow step on both Ubuntu/Windows, so they are classified as pre-execution infrastructure/policy failure, **not evidence that the smoke body failed**.

No mass Activity production until #7 has real evidence.

---

# First authoring/content vertical slice

M04 now has:

- canonical lesson: `content/python/04_INTERPRETE_REPL_VALORI_IO.md`;
- Marp slide source: `slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`;
- teacher runbook: `teacher/M04_RUNBOOK.md`;
- linked Activity `py2-activity-b-input-somma-001`;
- Content Pack `content_item` with provenance/reference mapping;
- Course Board local Markdown source entry.

This validates the **authoring shape**, not yet the live dashboard/runner execution.

The Course Design UDA item is intentionally not hand-forged: the first real Course Board round-trip should populate/align it, so the dashboard workflow is actually tested.

---

# Open blockers

## Curriculum decision

- explicit decision-owner approval of `CURRICULUM_FREEZE_CANDIDATE.md` before marking architecture frozen.

## Platform / delivery

- `python-docente#2` — managed Classroom Environment certification;
- `TheBitPoets/2cornot2c#753/#754` — environment contract + Flowchart Lab;
- `TheBitPoets/2cornot2c#755` — Course Workspace/Open course UX;
- `python-docente#6` — managed beginner REPL/editor workflow certification;
- `python-docente#7` — P1 first Python vertical slice certification;
- `TheBitPoets/2cornot2c#756` — P2 function behavior;
- `TheBitPoets/2cornot2c#757` — P4 filesystem behavior;
- `TheBitPoets/2cornot2c#758` — P3 object behavior;
- Romeo simulator cross-profile certification.

## Content production

- individual audit of legacy `friedpython` exercises before import;
- first real Course Board `--root` round-trip against M04;
- M04 lesson/deck/runbook teacher review;
- slide build/quality pipeline for this repo;
- then M05 vertical slice continuation and controlled expansion.

---

# Explicit non-goals now

- no claim that the course is classroom-ready;
- no final Content Pack approval;
- no mass lesson/slide/Activity generation before the first vertical slice gates;
- no fake grading for unsupported P2/P3/P4 outcomes;
- no hardware-dependent Romeo core;
- no duplication of standalone Git/Container curricula;
- no importing `friedpython` wholesale;
- no reopening TPSI5 curriculum while solving Python platform needs.

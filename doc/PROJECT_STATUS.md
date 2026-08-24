# python-docente — project status

## Current phase

**Curriculum FROZEN + first authoring/delivery vertical slice under certification.**

Canonical curriculum freeze:

`doc/CURRICULUM_FREEZE_2026_2027.md`

Decision owner approval: **2026-08-24**.

The second-year *what/sequence/outcomes* are now stable. Do not reopen them for ordinary lesson/tooling changes. Content Pack approval and classroom readiness remain separate later gates.

## Current branch / review surface

- branch: `agent/course-architecture`
- draft PR: `#1 — Draft Python curriculum architecture and second-year track`

The PR remains draft because the curriculum freeze is complete but delivery certification is not.

---

# 1. Curriculum — DONE / FROZEN

## Second-year shape

- 33 weeks × 3 hours = 99 nominal hours;
- 30 core weeks = 90 hours;
- 3 checkpoint/buffer weeks = 9 hours;
- real timetable: 2 active-theory hours + 1 lab hour;
- spiral method: test/trace/debug/naming/comparison/performance reasoning throughout;
- M00–M30 map;
- all UDA specs `PY2_01_SPEC.md` … `PY2_10_SPEC.md`;
- mandatory OOP in weeks 29–32;
- no mandatory new prerequisite in week 33.

Frozen UDA sequence:

```text
PY2-01 problem solving / algorithms / flow charts
PY2-02 REPL / first Python / types / I-O
PY2-03 selection / Boolean logic
PY2-04 loops / algorithmic patterns
PY2-05 functions / decomposition / assert / regression
Checkpoint A
PY2-06 strings
PY2-07 lists / tuples / alias-copy / matrices
Checkpoint B
PY2-08 set / dict / data-model choice
PY2-09 text files / pathlib / predictable errors
PY2-10 classes / objects / composition / OOP capstone
Checkpoint C
```

Architecture load/dependency review: `tracks/secondo/ARCHITECTURE_REVIEW.md`.

## Frozen design principles

- problem → algorithm → cases → code → test → debug → refactor;
- explicit loops before comprehensions;
- `if/elif/else` before optional `match/case`;
- data-structure choice is a required competence;
- OOP is core, composition before inheritance;
- file/error block intentionally small to protect OOP time;
- testing is progressive, not a final chapter.

---

# 2. Git / Container — architecture DONE

## Git

Git is a separate progressive curriculum. Python second year consumes G1 only:

```text
weeks 13–16: status / diff
Checkpoint A: first guided add / commit
second semester: normal checkpoint/history routine
```

The user's existing Git handouts should be requested when producing the definitive G1 material or starting the standalone Git course.

## Container

Container/Docker remains a separate future curriculum based on `kinderp/docker101` and backlog issue #1. Python professional stages consume container literacy without duplicating the Container course.

---

# 3. Romeo — mapping DONE, delivery certification OPEN

`tracks/secondo/ROMEO_MAPPING.md` is complete.

Strong mapping:

- PY2-03 conditions;
- PY2-04 loops;
- PY2-05 functions/top-down/debug;
- PY2-10 OOP/capstone.

No forced Romeo mapping for strings/set-dict/files. Hardware is never required for core completion.

`python-docente#4` is closed as mapping-complete.

`romeo-sim` install/probe/launch/run across supported Classroom Environment profiles still needs certification.

---

# 4. Assessment — DONE

Assessment model/calendar are defined; `python-docente#5` is closed.

Minimum frozen delivery expectation:

- one theory/written + one practical/practical-written assessment per quadrimester;
- formative evidence continuously through trace/debug/Activity/projects;
- autograding only for deterministic evidence;
- manual/rubric evidence remains first-class;
- foundational/core assessments do not allow AI-generated solutions; controlled AI review/debug comes later.

---

# 5. TheBitLab authoring model — designed, partial certification OPEN

`python-docente` is structured as a Course Workspace:

- `doc/course_design.json` — full 33-week UDA/checkpoint design;
- `content/python/content-pack.json` — draft `thebitlab.content-pack.v1`;
- all ten UDA specs + architecture review + Git/Romeo mappings indexed;
- repository = mutable authoring source of truth;
- Git = history/review;
- Course Bundle = immutable publication state.

Granularity decision:

```text
Content Pack: module/file identity
Course Board: heading-tree editorial granularity
```

The dashboard may therefore move/reorder individual lesson sections without losing module identity in the Content Pack.

Product UX for first-class `Open course` / bundle inspection remains `2cornot2c#755`; a bulk “add whole module/file to UDA” UX has been requested there.

---

# 6. Python grading profiles — designed

Canonical design: `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

- P0 — manual/trace/design evidence;
- P1 — single-file stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — external `romeo-sim` runtime plugin.

Do not distort P2/P3/P4 outcomes into stdin/stdout solely to obtain an automatic score.

---

# 7. First technical Activity vertical slice — CREATED, NOT CERTIFIED

Activity:

`activities/python/py2-activity-b-input-somma-001/`

Contains:

- Activity 1.0 metadata;
- starter `main.py`;
- student `GUIDA.md`;
- solution;
- teacher notes;
- 3 deterministic stdin/stdout canary cases;
- provenance link to canonical M04 lesson + PY2-02 design spec.

Certification: `python-docente#7`.

Required principle:

```text
starter must fail
solution must pass
student scaffold must not leak teacher/solution/test answers
```

---

# 8. First authoring/content vertical slice M04 — CREATED, UNDER GATES

M04 currently has:

- canonical lesson `content/python/04_INTERPRETE_REPL_VALORI_IO.md`;
- Marp slide source `slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`;
- teacher runbook `teacher/M04_RUNBOOK.md`;
- linked Activity `py2-activity-b-input-somma-001`;
- `student/README.md` navigation;
- `teacher/README.md` navigation;
- Content Pack `content_item` + provenance/reference mapping;
- Course Board source entry.

QA written:

- `tests/m04_vertical_slice_static.py` — lesson/slides/runbook/navigation/Activity/Content Pack coherence + no student leakage;
- `tests/course_board_workspace_roundtrip.py` — external Course Workspace heading-tree → UDA → save → reopen/provenance/digest;
- `tests/thebitlab_python_smoke.py` — Activity/Content Pack validation, scaffold redaction, starter/solution grading.

These tests are **written but not yet evidenced green** because GitHub Actions is failing before executing any job step.

---

# 9. CI blocker — OPEN

`python-docente#8` tracks GitHub Actions pre-execution failure.

Observed behavior on Ubuntu and Windows hosted runners:

```text
workflow dispatched
job conclusion = failure
steps = null
```

Therefore current failures are not evidence that M04 QA, Course Board round-trip or P1 grading failed; the test body has not started.

Do not weaken smoke semantics to hide this infrastructure/policy failure.

---

# 10. Classroom Environment / platform blockers — OPEN

- `python-docente#2` — managed Classroom Environment certification;
- `2cornot2c#753/#754` — environment contract + Flowchart Lab;
- `2cornot2c#755` — Course Workspace/Open course UX;
- `python-docente#6` — managed beginner REPL/editor workflow;
- `python-docente#7` — P1 consumer certification;
- `python-docente#8` — Actions pre-execution blocker;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior;
- Romeo simulator cross-profile certification.

P2/P3/P4 do not block teaching those concepts; they block only the promise of deterministic autograding for those profiles.

---

# 11. Sources / friedpython — architecture audit DONE, item audit OPEN

Done:

- source roles defined for Think/Pensare in Python, Learning/Imparare Python, Fluent Python, Python in a Nutshell, Pluralsight, official Python docs;
- `friedpython` snapshot pinned;
- thematic inventory performed for strings/lists/tuples/dictionaries/files;
- legacy caveats identified (e.g. Python 2 remnants; no blind copy).

Still required before reuse:

- audit each candidate exercise/example individually;
- modernize/adapt only selected items;
- rebuild as original lesson/Activity material with provenance.

---

# 12. What may proceed now

Because curriculum architecture is frozen, content work can proceed without reopening UDA/outcome design.

Recommended order:

1. resolve `#8` enough to execute the existing M04 gates;
2. run/fix static QA + Course Board round-trip + P1 consumer smoke;
3. certify M04 as the golden vertical slice;
4. establish slide build/quality pipeline;
5. promote M04 editorially after teacher review;
6. produce M05 using the same contract;
7. expand UDA-by-UDA, not all modules blindly at once;
8. implement/certify Flowchart Lab before finalizing PY2-01 delivery;
9. implement P2 before relying on function-behavior autograding in PY2-05;
10. implement P4 before file-behavior autograding in PY2-09;
11. implement P3 before generic OOP autograding in PY2-10;
12. certify `romeo-sim` before making Romeo Activities mandatory delivery.

---

# 13. Gates that remain distinct

## Curriculum architecture — FROZEN ✅

Completed 2026-08-24.

## Content Pack `1.0.0 / approved` — NOT YET

Needs complete reviewed content/provenance/coverage and a green end-to-end vertical slice.

## Ready for classroom / GO pilot — NOT YET

Needs real Classroom Environment/TheBitLab rehearsal. Neither freeze nor CI alone is sufficient.

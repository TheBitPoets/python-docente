# python-docente — project status

> Ultimo aggiornamento: **2026-08-28**  
> Branch: `agent/course-architecture`  
> Draft PR: `#1`  
> Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`

## Current phase

Il curriculum del secondo anno è **FROZEN** e il layer editoriale M04–M30 è completo in stato `draft`.

Il progetto è nella fase di **delivery / runtime / release certification**.

Restano separati, e non vanno confusi:

```text
curriculum frozen
!= contenuti editoriali completi
!= profile runtime certificati
!= teacher sign-off
!= Content Pack approved
!= classroom GO
```

`Content Pack 1.0.0 / approved` e `ready for classroom` sono ancora **NO**.

---

# 1. Curriculum / editorial / semantic state

```text
Curriculum architecture                 FROZEN
Frozen outcomes                         25/25 mapped
Lesson M04–M30                          COMPLETE / draft
Marp source deck M04–M30                COMPLETE / draft
Teacher runbook M04–M30                 COMPLETE / draft
Semantic review M04–M30                 COMPLETE / draft
Checkpoint A/B/C                        COMPLETE / draft
Content Pack catalog M04–M30            COMPLETE / draft
Course Design UDA mapping               COMPLETE / draft
Source-audit manifests                  ALIGNED
```

Authoritative semantic review index:

```text
doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md
```

Didactic pacing boundary:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

Content Pack remains:

```text
content/python/content-pack.json
version = 0.1.0
status = draft
```

No mass Activity generation is authorized by editorial completion alone.

---

# 2. Real GitHub Actions execution — RESTORED

`python-docente#8` is **CLOSED / completed**.

After the repository became public, GitHub-hosted runners began executing normally instead of failing pre-runner with `steps=null`.

The normal vertical-slice workflow now executes real steps on Ubuntu and Windows:

```text
static course QA
Course Workspace round-trip
managed Activity assignment
P1 host consumer
PY2-01 Flowchart candidate consumer
Ubuntu source-built authoritative Docker P1 grading
```

Known all-green vertical-slice evidence includes run:

```text
33120724282 / #389
Ubuntu  SUCCESS
Windows SUCCESS
```

The current workflow no longer depends on cross-repository GHCR package access for P1: Ubuntu reconstructs the authoritative runner from its exact locked source revision and verifies the build metadata before grading.

---

# 3. P1 — M04 stdin/stdout canary

Activity:

```text
py2-activity-b-input-somma-001
M04 / PY2-02
profile P1 — stdin/stdout
```

Machine-readable certification profile:

```text
config/p1-canary-profile.json
host Python = 3.12
host OS = Ubuntu + Windows
TheBitLab consumer baseline = cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
toolchain = 2026.07.1
```

Real evidence covers:

- Content Pack + Activity validation;
- exact four-file student scaffold;
- teacher/solution/expected-output non-leakage;
- Course Workspace save/reopen round-trip;
- managed assignment path;
- host grading Ubuntu + Windows;
- authoritative Docker grading;
- solution `3/3`;
- starter `1/3`, with all three cases executed.

`python-docente#7` remains open **only for final classroom-profile rehearsal / human delivery evidence**.

Software certification is not classroom certification.

---

# 4. P2 — M13 function-behavior canary

A second Python Activity is now materialized deliberately as a single P2 canary:

```text
py2-activity-b-return-area-001
M13 / PY2-05
profile = python-function-v1
```

The exercise is a controlled change:

```text
print(area)
→
return area
```

This is intentional: the starter already computes and prints the correct numeric result, so a valid P2 grader must still fail it because the function returns `None`.

Current candidate platform:

```text
TheBitPoets/2cornot2c PR #763 — DRAFT
candidate SHA = c718c40045c69f0863a4a68c7a3f802241685230
profile = python-function-v1
worker schema = thebitlab.python-function-worker.v1
```

Platform evidence:

```text
Python function profile P2 candidate
run 33182445790 / #12
SUCCESS
```

That run proves:

- strict `function_tests` contract;
- teacher expectations stay host-side;
- bounded deterministic value codec;
- real top-level function invocation;
- return / bool / exception behavior;
- missing/non-callable/import-error handling;
- bounded stdout/stderr;
- unsupported-return fail closed;
- infinite loop → bounded timeout;
- hardened Docker sandbox reuse;
- normal `DockerGradeActivityExecutionService` dispatch;
- real `student_lab_runner.run_docker_assignment()` P2 path;
- student-facing report redaction.

Existing C/P1/Node/SQLite Docker regression on the same candidate family is green:

```text
Build assignment runner Docker image
run 33182445721 / #1008
SUCCESS
```

Real course consumer evidence:

```text
Python M13 P2 canary
run 33182614844 / #3
SUCCESS
```

The course consumer now uses the **normal** `DockerGradeActivityExecutionService`, not a side harness.

Behavioral oracle:

```text
solution = 3/3 PASS
starter  = 0/3 FAIL
starter worker status = returned
starter actual_return = None
starter stdout = numerically correct
```

Therefore P2 is functionally proven through the real course path.

### P2 promotion boundary

P2 remains **candidate**, not stable.

Before broader P2 Activity materialization:

1. choose a new stable assignment-runner/toolchain identity for the P2-capable source;
2. publish/update the immutable release lock;
3. complete PR/release review and merge decision;
4. repin `python-docente` from candidate SHA to the promoted stable platform/toolchain.

Do **not** silently describe the modified candidate as the existing stable `2026.07.1` release.

---

# 5. Activity inventory

Exactly two new Python Activities are deliberately materialized today:

```text
M04  py2-activity-b-input-somma-001   P1 stdin/stdout
M13  py2-activity-b-return-area-001   P2 function behavior candidate
```

Policy remains:

```text
outcome
→ correct evidence profile
→ profile implementation
→ real profile certification
→ one canary consumer
→ stable promotion
→ broader Activity materialization
```

P3/P4 outcomes must not be distorted into P1/P2 merely to obtain automated scores.

---

# 6. PY2-01 / Flowchart Lab

Upstream candidate remains `2cornot2c#753/#754`.

Implemented surfaces include:

```text
thebitlab.flowchart.v1
headless validator/executor
bounded deterministic trace
loopback Run / Session / Step / Reset API
same-origin browser editor
variable watch
managed algorithm.flow.json persistence
JSON import/export
deterministic SVG evidence
built-in runtime plugin / registry
```

The `python-docente` vertical-slice workflow already validates the exact pinned Flowchart candidate on Ubuntu and Windows.

Boundary remains:

```text
implemented + CI consumer PASS
!= final classroom-profile rehearsal
```

Frozen fallback remains valid:

```text
paper / whiteboard
→ pseudocodice
→ manual flow chart
→ trace
→ test cases
```

PY2-01 is therefore much farther than SPEC-only, but is not yet declared classroom-certified.

---

# 7. Git G1 consumer

Source of truth:

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
```

Consumer mode:

```text
config/git-g1-consumer.json
mode = embedded-outcome-subset
full_g1_track_completion_required = false
full_canonical_lesson_completion_required = false
```

Progression:

```text
M14–M16          status/diff guided
Checkpoint A     status → diff → test → add → diff --staged → commit → status → log/show
second semester  progressive reuse/recovery
```

Static/structural consumer is complete and exercised by course CI. Classroom rehearsal remains separate.

---

# 8. Slide release artifacts — REAL BUILD PASS

The slide layer is no longer merely “pipeline implemented”. A real full release artifact bundle has been generated and structurally validated.

Evidence:

```text
workflow: Python slide release artifacts
run: 33116692428 / #1
job: 98673027862
result: SUCCESS
artifact id: 9664877644
artifact ZIP sha256:
4693a11cf7c77c987e7396e2375911566409746c0378498a925b38b4e105d268
```

Manifest evidence:

```text
source commit: c6b57d98184e5937a5d449c50b5d726dc2130aa7
modules: 27
27 HTML + 27 PDF + 27 PPTX
515 rendered/source slides
```

Toolchain observed:

```text
Marp CLI 4.5.0 / Marp Core 4.4.0
Node 26.5.0
Google Chrome for Testing 149.0.7827.55
pypdf 6.16.2
linux/amd64
pinned Marp image digest = sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
```

Engineering review:

```text
M04 / M11 / M18 / M22 / M26 / M30 PDF sample   PASS
six mandatory PPTX opened/converted in LibreOffice   PASS
slide counts preserved   PASS
```

OOXML inspection confirms Marp PPTX uses rendered slide background images; therefore **native PowerPoint object editability is not claimed**.

Detailed evidence:

```text
doc/SLIDE_ARTIFACT_REVIEW_2026-08-27.md
```

`python-docente#10` remains open only for human/target-consumer gates:

- open/present mandatory sample in target Microsoft PowerPoint, or explicitly decide it is not a supported target;
- human decision in `teacher/SLIDE_VISUAL_REVIEW.md`;
- expand review only if that pass reveals a systematic issue.

---

# 9. Profiles still pending

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  integrated candidate + real consumer PASS / stable promotion pending
P4 filesystem behavior                OPEN — 2cornot2c#757
P3 object behavior                    OPEN — 2cornot2c#758
romeo-sim                              certification pending
```

Next runtime priority after P2 stable-boundary work is **P4**, because M26 precedes OOP P3 in the course dependency/delivery sequence.

---

# 10. Teacher / release gates

Teacher sign-off:

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
status = PENDING
```

AI/CI cannot approve this gate.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. final P1 Classroom Environment rehearsal;
2. final Flowchart Lab managed classroom-profile rehearsal;
3. P2 stable toolchain/release promotion and repin;
4. P4 certification + first real consumer;
5. P3 certification + first real consumer;
6. `romeo-sim` certification before mandatory Romeo missions;
7. human PowerPoint/slide review completion;
8. human teacher sign-off;
9. final provenance/license review of the release candidate;
10. explicit Content Pack promotion;
11. final real Classroom Environment rehearsal;
12. explicit GO classroom decision.

---

# Gate status

```text
Curriculum architecture             FROZEN ✅
Frozen outcome mapping              25/25 ✅
Editorial M04–M30                   COMPLETE 🟡 draft
Semantic review M04–M30             COMPLETE 🟡 draft
Content Pack catalog M04–M30        COMPLETE 🟡 draft
Course Design M04–M30 mapping       COMPLETE 🟡 draft
Source-audit manifests              ALIGNED ✅ real CI
GitHub Actions blocker #8           RESOLVED ✅
Static QA Ubuntu/Windows            PASS ✅
Course Board round-trip             PASS ✅ Ubuntu + Windows
Managed P1 assignment               PASS ✅
P1 host smoke                       PASS ✅ Ubuntu + Windows / Python 3.12
P1 Docker grading                   PASS ✅ source-built locked runner
P1 classroom rehearsal              PENDING ⏳ #7
Flowchart Lab implementation        IMPLEMENTED ✅
Flowchart course CI consumer        PASS ✅ Ubuntu + Windows
Flowchart classroom rehearsal       PENDING ⏳
P2 contract/worker                  PASS ✅
P2 Docker sandbox                   PASS ✅
P2 normal Student Lab dispatch      PASS ✅
P2 real M13 consumer                PASS ✅
P2 stable toolchain promotion       PENDING ⏳
Slide 27×HTML/PDF/PPTX build        PASS ✅ real artifacts
Slide structural QA                 PASS ✅
Slide engineering sample review     PASS ✅
PowerPoint/human slide sign-off     PENDING ⏳ #10
P4 filesystem grading               OPEN ⏳
P3 object grading                   OPEN ⏳
romeo-sim certification             OPEN ⏳
Teacher sign-off                    PENDING ⏳
Content Pack 1.0 approved           NOT YET ⏳
Ready for classroom / GO            NOT YET ⏳
```

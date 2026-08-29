# python-docente — project status

> Ultimo aggiornamento: **2026-08-29**  
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
!= stable toolchain release
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

The repository is public and GitHub-hosted runners execute normally. The vertical-slice workflow exercises real steps on Ubuntu and Windows:

```text
static course QA
Course Workspace round-trip
managed Activity assignment
P1 host consumer
PY2-01 Flowchart candidate consumer
Ubuntu source-built authoritative Docker P1 grading
```

Recent all-green course evidence includes vertical-slice run `33258468869 / #417`; later documentation-only updates may produce newer runs.

---

# 3. P1 — M04 stdin/stdout canary

```text
Activity: py2-activity-b-input-somma-001
M04 / PY2-02
profile: P1 stdin/stdout
host: Python 3.12 / Ubuntu + Windows
TheBitLab baseline: cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
toolchain lock: 2026.07.1
```

Real evidence covers Activity validation, exact student scaffold/non-leakage, Course Workspace round-trip, managed assignment, host grading on Ubuntu/Windows and authoritative Docker grading. Behavioral oracle:

```text
solution = 3/3
starter  = 1/3, all cases executed
```

`python-docente#7` remains open only for final classroom-profile rehearsal / human delivery evidence.

---

# 4. P2 — M13 function-behavior canary

```text
Activity: py2-activity-b-return-area-001
M13 / PY2-05
profile: python-function-v1
platform PR: TheBitPoets/2cornot2c#763 — DRAFT
release-candidate SHA: d9ea02e1904ae363944e3c0a199f67bf0c4ac77c
release-candidate toolchain identity: 2026.08.1
```

Controlled change:

```text
print(area)
→
return area
```

P2 is functionally proven through the normal `DockerGradeActivityExecutionService` and Student Lab path. It keeps expected return/exception data on the trusted host, runs each case in the hardened Docker boundary and redacts hidden tests before the student report.

Real evidence includes green P2 dedicated CI, general C/P1/Node/SQLite Docker regression, full Quality including minimum Python/Windows and the real M13 consumer.

Behavioral oracle:

```text
solution = 3/3 PASS
starter  = 0/3 FAIL
starter stdout is numerically correct
starter actual_return = None
```

P2 has no known functional blocker, but **2026.08.1 is still a release candidate rather than the immutable stable course lock**. The reviewed merge/publish/digest/lock step is still required.

---

# 5. P4 — M26 filesystem-behavior canary

A third deliberate Python canary is now materialized:

```text
Activity: py2-activity-b-file-risultato-001
M26 / PY2-09
profile: python-filesystem-v1
platform PR: TheBitPoets/2cornot2c#764 — DRAFT
integrated candidate SHA: fb3cf4b923f776dd2c57cca73126d906541531bd
```

Controlled change:

```text
print(totale)
→
write risultato.txt
```

The P4 candidate implements and proves:

- versioned `filesystem_tests` contract;
- teacher fixture sources and expected contents outside the student scaffold;
- clean bounded tmpfs per test;
- read-only fixture mounts and fixture mutation protection;
- UTF-8 artifact manifest + host-side comparison;
- path traversal / external absolute read / symlink / directory-tree rejection for v1;
- fixture/output count and byte limits;
- student `FileNotFoundError` retained as program behavior;
- bounded timeout cleanup;
- canonical `DockerGradeActivityExecutionService` routing;
- normal `student_lab_runner.run_docker_assignment()` integration;
- hidden-test redaction before the persisted student report.

Platform evidence:

```text
P4 candidate                    33258370195 / #8    SUCCESS
P4 Student Lab integration      33258370237 / #1    SUCCESS
Docker regression               33258370210 / #1031 SUCCESS
Quality                         33258370217 / #1868 SUCCESS
```

Real course evidence:

```text
Python M26 P4 canary
run 33258589185 / #4
SUCCESS
platform pin: fb3cf4b923f776dd2c57cca73126d906541531bd
```

Behavioral oracle:

```text
solution -> creates risultato.txt -> 1/1 PASS
starter  -> computes and prints the correct total,
            but does not create risultato.txt -> 0/1 FAIL
```

The public scaffold fixture is deliberately different from the grading fixture, so copying/hardcoding the public sample cannot satisfy the authoritative test.

### P4 promotion boundary

P4 is functionally proven but **not stable**. Its branch still inherits the old `2026.07.1` runner identity while P2 has a separate `2026.08.1` release candidate. Before either profile is promoted broadly, P2 and P4 must be unified into one reviewed assignment-runner source/toolchain and one new immutable release lock.

---

# 6. Activity inventory

Exactly three new Python Activities are deliberately materialized:

```text
M04  py2-activity-b-input-somma-001       P1 stdin/stdout
M13  py2-activity-b-return-area-001       P2 function behavior candidate
M26  py2-activity-b-file-risultato-001    P4 filesystem behavior candidate
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

P3 outcomes must not be distorted into P1/P2/P4 merely to obtain automated scores.

---

# 7. PY2-01 / Flowchart Lab

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

The course vertical-slice workflow validates the pinned Flowchart candidate on Ubuntu and Windows.

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

---

# 8. Git G1 consumer

Source of truth:

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
config/git-g1-consumer.json
mode = embedded-outcome-subset
```

M14–M16 introduces status/diff progressively; Checkpoint A performs the first compact status → diff → test → add → staged diff → commit → status → log/show flow.

Static/structural consumer is complete and exercised by course CI. Classroom rehearsal remains separate.

---

# 9. Slide release artifacts — REAL BUILD PASS

```text
workflow: Python slide release artifacts
run: 33116692428 / #1
job: 98673027862
SUCCESS
artifact id: 9664877644
ZIP sha256: 4693a11cf7c77c987e7396e2375911566409746c0378498a925b38b4e105d268

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
```

Engineering PDF sample M04/M11/M18/M22/M26/M30 passed. All six mandatory PPTX files opened/converted in LibreOffice with exact slide counts. Marp PPTX native object editability is not claimed.

`python-docente#10` remains open only for target Microsoft PowerPoint / human visual sign-off.

---

# 10. Profiles / runtime still pending

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  integrated + real consumer PASS / stable release pending
P4 filesystem behavior                integrated + real consumer PASS / stable release pending
P3 object behavior                    OPEN — 2cornot2c#758
romeo-sim                              certification pending
```

The next new profile is **P3 object behavior**, but P2/P4 must not be given competing stable runner identities. A combined release boundary should be settled before broad Activity materialization.

---

# 11. Teacher / release gates

Teacher sign-off:

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
status = PENDING
```

AI/CI cannot approve this gate.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. final P1 Classroom Environment rehearsal;
2. final Flowchart Lab managed classroom-profile rehearsal;
3. unify P2 + P4 into one reviewed assignment-runner/toolchain;
4. publish and lock that immutable stable runner, then repin P2/P4 canaries;
5. implement/certify P3 object behavior + one real OOP consumer;
6. certify `romeo-sim` before mandatory Romeo missions;
7. complete target PowerPoint/human slide review;
8. human teacher sign-off;
9. final provenance/license review of the release candidate;
10. explicit Content Pack promotion;
11. final real Classroom Environment rehearsal;
12. explicit classroom GO decision.

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
P1 host/Docker grading              PASS ✅
P1 classroom rehearsal              PENDING ⏳ #7
Flowchart Lab implementation        IMPLEMENTED ✅
Flowchart course CI consumer        PASS ✅ Ubuntu + Windows
Flowchart classroom rehearsal       PENDING ⏳
P2 contract/worker/Docker            PASS ✅
P2 normal Student Lab dispatch      PASS ✅
P2 real M13 consumer                PASS ✅
P4 contract/worker/Docker            PASS ✅
P4 normal Student Lab dispatch      PASS ✅
P4 real M26 consumer                PASS ✅
P2+P4 unified stable toolchain      PENDING ⏳
P3 object grading                   OPEN ⏳
Slide 27×HTML/PDF/PPTX build        PASS ✅ real artifacts
Slide structural/engineering QA     PASS ✅
PowerPoint/human slide sign-off     PENDING ⏳ #10
romeo-sim certification             OPEN ⏳
Teacher sign-off                    PENDING ⏳
Content Pack 1.0 approved           NOT YET ⏳
Ready for classroom / GO            NOT YET ⏳
```

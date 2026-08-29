# python-docente — project status

> Ultimo aggiornamento: **2026-08-29**  
> Branch: `agent/course-architecture`  
> Draft PR: `#1`  
> Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`

## Current phase

Il curriculum del secondo anno è **FROZEN** e il layer editoriale M04–M30 è completo in stato `draft`.

Il progetto è nella fase di **delivery / runtime / release certification**.

Restano separati:

```text
curriculum frozen
!= contenuti editoriali completi
!= profili runtime tecnicamente certificati
!= stable immutable toolchain release
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

Content Pack remains:

```text
content/python/content-pack.json
version = 0.1.0
status = draft
```

Editorial completion does not authorize mass Activity generation.

---

# 2. Real GitHub Actions execution

`python-docente#8` is **CLOSED / completed**. The repository is public and GitHub-hosted runners execute normally.

Current post-repin vertical-slice evidence:

```text
TheBitLab Python vertical slice
run 33259784323 / #428
Ubuntu  SUCCESS
Windows SUCCESS
```

It includes the unified static QA, Course Workspace round-trip, managed P1 assignment, P1 host/Docker path and the pinned PY2-01 Flowchart consumer.

---

# 3. P1 — M04 stdin/stdout canary

```text
Activity: py2-activity-b-input-somma-001
M04 / PY2-02
profile: P1 stdin/stdout
host: Python 3.12 / Ubuntu + Windows
TheBitLab baseline: cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
stable toolchain lock: 2026.07.1
```

Behavioral oracle:

```text
solution = 3/3 PASS
starter  = 1/3, all cases executed
```

Software/Docker evidence is green. `python-docente#7` remains open only for final Classroom Environment / human rehearsal evidence.

---

# 4. Unified P2 + P4 grading candidate

P2 and P4 no longer use competing release candidates in the course.

Both are pinned to one exact platform source and one candidate toolchain:

```text
TheBitPoets/2cornot2c PR #766 — DRAFT
combined head = 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
toolchain candidate = 2026.08.2
stable checked-in lock = 2026.07.1
P2 = python-function-v1
P4 = python-filesystem-v1
```

The combined runner dispatch is explicit:

```text
filesystem_tests -> P4
function_tests   -> P2
neither          -> legacy P1/C/Node/SQLite
both             -> invalid_payload
```

Mixed P2+P4 contracts in one Activity and non-Python P2/P4 Activities fail closed.

## Platform coexistence evidence

```text
Combined Python grading profiles
run 33259536736 / #3
SUCCESS
```

One image, built once from the exact combined head, passed in the same job:

```text
combined contracts / identity           PASS
P2 + P4 modules packaged                PASS
legacy P1/C/Node/SQLite Student Lab     PASS
P2 normal Student Lab                   PASS
P4 normal Student Lab                   PASS
```

Release-validation evidence:

```text
Publish assignment runner toolchain
run 33259536908 / #13
validate SUCCESS
publish SKIPPED — correct for PR
```

The validate job stages the same candidate and passes legacy + P2 + P4 before any future `main` publication can occur.

Full platform regression:

```text
Quality
run 33259536787 / #1871
SUCCESS
```

Python, minimum-Python, Windows filesystem and Mermaid jobs are all green.

### Stable release boundary

`2026.08.2` is **technically green but not stable**. Stable promotion still requires:

```text
review / explicit merge decision for #766
→ publish from main
→ obtain real GHCR immutable digest
→ reviewed toolchain.lock update
→ stable course repin
```

No digest is invented and the old stable lock remains unchanged until that real publication exists.

---

# 5. P2 — M13 function-behavior canary

```text
Activity: py2-activity-b-return-area-001
M13 / PY2-05
profile: python-function-v1
combined platform ref: 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
candidate toolchain: 2026.08.2
feature provenance: 2cornot2c#763
release path: 2cornot2c#766
```

Controlled change:

```text
print(area) -> return area
```

Individual combined-candidate consumer evidence:

```text
Python M13 P2 canary
run 33259784340 / #32
SUCCESS
```

Behavioral oracle:

```text
solution = 3/3 PASS
starter  = 0/3 FAIL
starter stdout numerically correct
starter actual_return = None
```

Therefore the grader measures function return behavior rather than stdout.

---

# 6. P4 — M26 filesystem-behavior canary

```text
Activity: py2-activity-b-file-risultato-001
M26 / PY2-09
profile: python-filesystem-v1
combined platform ref: 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
candidate toolchain: 2026.08.2
feature provenance: 2cornot2c#764
release path: 2cornot2c#766
```

Controlled change:

```text
print(totale) -> write risultato.txt
```

P4 proves read-only teacher fixtures, clean bounded tmpfs, host-side artifact comparison, traversal/external-path/symlink/subdirectory policies, UTF-8/output limits, timeout cleanup, normal Docker dispatch, Student Lab integration and hidden-test redaction.

Individual combined-candidate consumer evidence:

```text
Python M26 P4 canary
run 33259784324 / #14
SUCCESS
```

Behavioral oracle:

```text
solution -> creates risultato.txt -> 1/1 PASS
starter  -> computes and prints correct total,
            but artifact is absent -> 0/1 FAIL
```

The public sample fixture differs from the teacher grading fixture, preventing sample-output hardcoding from satisfying the authoritative test.

---

# 7. Strong shared-image course evidence

The strongest current course gate is:

```text
Python combined grading canaries
run 33259784359 / #1
SUCCESS
```

This workflow:

1. verifies P2/P4 course pins are identical;
2. checks out combined TheBitLab head `670bc7a...` once;
3. verifies candidate `2026.08.2` while stable lock remains `2026.07.1`;
4. builds one Docker image once;
5. runs M13/P2 against it;
6. runs M26/P4 against the **same image**.

Static QA also contains `tests/python_grading_toolchain_alignment.py`, so future P2/P4 pin divergence fails the normal course quality suite.

---

# 8. Activity inventory

Exactly three deliberate Python canaries are materialized:

```text
M04  py2-activity-b-input-somma-001       P1 stdin/stdout
M13  py2-activity-b-return-area-001       P2 function behavior candidate
M26  py2-activity-b-file-risultato-001    P4 filesystem behavior candidate
```

Policy remains:

```text
outcome
→ correct evidence profile
→ implementation
→ real certification
→ one canary consumer
→ stable promotion
→ broader Activity materialization
```

P3 outcomes must not be distorted into P1/P2/P4 just to obtain automated scoring.

---

# 9. PY2-01 / Flowchart Lab

The managed Flowchart candidate (`2cornot2c#753/#754`) includes:

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

Course CI validates the pinned candidate on Ubuntu and Windows. Final classroom-profile rehearsal remains separate; the paper/whiteboard fallback remains valid.

---

# 10. Git G1 consumer

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
config/git-g1-consumer.json
mode = embedded-outcome-subset
```

Structural/process consumer is complete and exercised by course CI. Classroom rehearsal remains separate.

---

# 11. Slide release artifacts — REAL BUILD PASS

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

Engineering PDF sample M04/M11/M18/M22/M26/M30 and six mandatory PPTX LibreOffice openings passed. Native PowerPoint object editability is not claimed.

`python-docente#10` remains open for target Microsoft PowerPoint / human visual sign-off.

---

# 12. Profiles / runtime still pending

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  unified candidate + real consumer PASS / stable publish pending
P4 filesystem behavior                unified candidate + real consumer PASS / stable publish pending
P3 object behavior                    OPEN — 2cornot2c#758
romeo-sim                              certification pending
```

The next new automated profile is **P3 object behavior** for the OOP block M27–M30.

---

# 13. Remaining promotion gates

Teacher sign-off remains `PENDING`; AI/CI cannot approve it.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. final P1 Classroom Environment rehearsal;
2. final Flowchart managed classroom-profile rehearsal;
3. review/merge/publish/immutable-lock promotion of combined P2+P4 `2026.08.2`;
4. P3 object behavior certification + one real OOP consumer;
5. `romeo-sim` certification before mandatory Romeo missions;
6. target PowerPoint/human slide review;
7. human teacher sign-off;
8. final provenance/license review;
9. explicit Content Pack promotion;
10. final real Classroom Environment rehearsal;
11. explicit classroom GO decision.

---

# Gate status

```text
Curriculum architecture             FROZEN ✅
Frozen outcome mapping              25/25 ✅
Editorial M04–M30                   COMPLETE 🟡 draft
Semantic review M04–M30             COMPLETE 🟡 draft
Content Pack catalog M04–M30        COMPLETE 🟡 draft
Course Design mapping               COMPLETE 🟡 draft
Source-audit manifests              ALIGNED ✅
GitHub Actions blocker #8           RESOLVED ✅
Static QA Ubuntu/Windows            PASS ✅
Course Board round-trip             PASS ✅
P1 host/Docker grading              PASS ✅
P1 classroom rehearsal              PENDING ⏳ #7
Flowchart implementation/CI         PASS ✅
Flowchart classroom rehearsal       PENDING ⏳
P2 normal Student Lab               PASS ✅
P4 normal Student Lab               PASS ✅
P2+P4 same-image platform gate      PASS ✅ 2026.08.2 candidate
P2+P4 same-image course gate        PASS ✅
P2+P4 immutable stable release      PENDING ⏳
P3 object grading                   OPEN ⏳
Slide real build/engineering QA     PASS ✅
PowerPoint/human slide sign-off     PENDING ⏳ #10
romeo-sim certification             OPEN ⏳
Teacher sign-off                    PENDING ⏳
Content Pack 1.0 approved           NOT YET ⏳
Ready for classroom / GO            NOT YET ⏳
```

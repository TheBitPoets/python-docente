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
!= release candidate verde
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

# 2. Python grading release candidate — P2 + P3 + P4

The three behavior profiles now share one truthful combined release candidate:

```text
TheBitPoets/2cornot2c PR #768 — DRAFT
candidate version = 2026.08.3
exact source = 3b482fe6a031bd6e7285342e489def786d77d197
stable checked-in lock = 2026.07.1
P2 = python-function-v1
P3 = python-object-v1
P4 = python-filesystem-v1
```

Lineage:

```text
#766 -> combined P2 + P4 source candidate
#767 -> P3 object behavior stacked on #766
#768 -> distinct P2 + P3 + P4 release identity 2026.08.3
```

## Strong same-image platform proof

```text
Combined Python grading profiles
run 33276143332 / #17
SUCCESS
```

One image built once from the exact `2026.08.3` source passed:

```text
combined P2/P3/P4 contracts + identity  PASS
legacy P1/C/Node/SQLite Student Lab     PASS
P2 normal Student Lab                   PASS
P3 normal Student Lab                   PASS
P4 normal Student Lab                   PASS
```

## Guarded release validation

```text
Publish assignment runner toolchain
run 33276143365 / #27
SUCCESS

validate  SUCCESS
publish   SKIPPED — correct for PR
```

Other evidence on the same head:

```text
Build assignment runner Docker #1051      SUCCESS
Python function profile P2 #37            SUCCESS
Python object profile P3 #5               SUCCESS
Python filesystem profile P4 #25          SUCCESS
P4 Student Lab integration #14            SUCCESS
Smoke student repository template #145    SUCCESS
Quality #1888                              SUCCESS
```

Quality #1888 had one first-attempt Windows-only JavaScript failure after 554 other Windows tests passed. The failed Windows job was rerun unchanged; the Node/SQL step passed and the overall workflow concluded SUCCESS. No release/P2/P3/P4 code was changed for that rerun.

## Stable release boundary

`2026.08.3` is a **fully green release candidate, not a stable published release**.

Current truth:

```text
2026.08.3 source candidate          PASS
same-image P2/P3/P4                PASS
publish validation                 PASS
GHCR publication                   NOT DONE
real 2026.08.3 immutable digest    NOT AVAILABLE YET
stable toolchain.lock update       NOT DONE
```

No digest is invented. Merge/publication requires an explicit release decision.

---

# 3. Course-side shared 2026.08.3 proof

P2, P3 and P4 course profiles are all pinned to:

```text
TheBitPoets/2cornot2c@3b482fe6a031bd6e7285342e489def786d77d197
version = 2026.08.3
PR = #768
```

Static alignment:

```text
tests/python_grading_toolchain_alignment.py
```

fails if P2/P3/P4 diverge in source, version or candidate identity.

## Strong same-image course proof

```text
Python combined grading canaries
run 33276449691 / #7
SUCCESS
```

The workflow:

1. proves P2/P3/P4 pins are identical;
2. checks out the exact `3b482fe6...` source once;
3. builds one `2026.08.3` image once;
4. runs M13/P2 against it;
5. runs M28/P3 against the same image;
6. runs M26/P4 against the same image.

All three pass.

Current individual/regrression course evidence:

```text
Python M13 P2 canary              run 33276449646 / #38  SUCCESS
Python M28 P3 canary              run 33276449656 / #5   SUCCESS
Python M26 P4 canary              run 33276449659 / #20  SUCCESS
Python combined grading canaries  run 33276449691 / #7   SUCCESS
TheBitLab Python vertical slice    run 33276449733 / #434 SUCCESS
```

---

# 4. P1 — M04 stdin/stdout canary

```text
Activity: py2-activity-b-input-somma-001
M04 / PY2-02
profile: P1 stdin/stdout
TheBitLab stable baseline: cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
stable toolchain lock: 2026.07.1
```

Behavioral oracle:

```text
solution = 3/3 PASS
starter  = 1/3, all cases executed
```

Software/Docker evidence is green. `python-docente#7` remains open only for final Classroom Environment / human rehearsal evidence.

---

# 5. P2 — M13 function behavior

```text
Activity: py2-activity-b-return-area-001
M13 / PY2-05
profile: python-function-v1
candidate: 2026.08.3 @ 3b482fe6...
```

Controlled change:

```text
print(area) -> return area
```

Oracle:

```text
solution = 3/3 PASS
starter  = 0/3 FAIL
starter stdout numerically correct
starter actual_return = None
```

Therefore the grader measures function return behavior rather than stdout.

---

# 6. P4 — M26 filesystem behavior

```text
Activity: py2-activity-b-file-risultato-001
M26 / PY2-09
profile: python-filesystem-v1
candidate: 2026.08.3 @ 3b482fe6...
```

Controlled change:

```text
print(totale) -> write risultato.txt
```

Oracle:

```text
solution -> creates risultato.txt -> 1/1 PASS
starter  -> correct computed/printed total, no artifact -> 0/1 FAIL
```

Teacher fixture/oracle details remain redacted from the Student Lab report.

---

# 7. P3 — M28 object behavior

P3 is implemented, platform-certified and consumed by one real non-Romeo course Activity.

```text
Activity: py2-activity-b-serbatoio-invariante-001
M28 / PY2-10
profile: python-object-v1
candidate: 2026.08.3 @ 3b482fe6...
```

P3 platform capabilities include:

```text
constructor behavior
public method calls
method return observation
public attribute/property observation
expected exception behavior
two-instance independence
bounded deterministic value codec
fresh hardened container per scenario
teacher expected values host-side
student-report redaction
fail-closed profile ambiguity
```

Normal Docker dispatch:

```text
function_tests   -> python-function-v1
object_tests     -> python-object-v1
filesystem_tests -> python-filesystem-v1
none             -> legacy P1/C/Node/SQLite
multiple         -> invalid_payload before student code runs
```

M28 invariant:

```text
0 <= livello <= capacita
```

Oracle:

```text
solution = 5/5 PASS
starter  = 3/5
```

The starter passes initial state, valid transition and independent instances, but fails exactly:

```text
overflow rifiutato senza cambiare stato
quantita negativa rifiutata
```

The course consumer also proves exact scaffold and Student Lab redaction of teacher-side `object_tests` and observations.

---

# 8. Activity inventory

Exactly four deliberate Python canaries are materialized:

```text
M04  py2-activity-b-input-somma-001             P1 stdin/stdout
M13  py2-activity-b-return-area-001             P2 function behavior
M26  py2-activity-b-file-risultato-001          P4 filesystem behavior
M28  py2-activity-b-serbatoio-invariante-001    P3 object behavior
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

No mass Activity generation is authorized yet.

---

# 9. PY2-01 / Flowchart Lab

The managed Flowchart candidate includes:

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

# 12. Profiles / runtime status

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  2026.08.3 candidate + real consumer PASS
P3 object behavior                    2026.08.3 candidate + real M28 consumer PASS
P4 filesystem behavior                2026.08.3 candidate + real consumer PASS
P2+P3+P4 same-image platform          PASS
P2+P3+P4 same-image course            PASS
P2/P3/P4 immutable stable release     PENDING
romeo-sim                              certification pending
```

The grading-profile implementation phase is complete at **release-candidate level**. The remaining grading blocker is release promotion, not behavior implementation.

---

# 13. Remaining promotion gates

Teacher sign-off remains `PENDING`; AI/CI cannot approve it.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. final P1 Classroom Environment rehearsal;
2. final Flowchart managed classroom-profile rehearsal;
3. explicit review/merge/release decision for the stacked `2cornot2c` candidate lineage;
4. publish the intended `2026.08.3` runner from the guarded `main` path;
5. obtain the real GHCR immutable digest;
6. update the reviewed stable toolchain lock and repin the course to that immutable release;
7. certify `romeo-sim` before mandatory Romeo missions;
8. target Microsoft PowerPoint / human slide review;
9. human teacher sign-off;
10. final provenance/license review;
11. explicit Content Pack promotion;
12. final real Classroom Environment rehearsal;
13. explicit classroom GO decision.

---

# Gate status

```text
Curriculum architecture                 FROZEN ✅
Frozen outcome mapping                  25/25 ✅
Editorial M04–M30                       COMPLETE 🟡 draft
Semantic review M04–M30                 COMPLETE 🟡 draft
Content Pack catalog M04–M30            COMPLETE 🟡 draft
Course Design mapping                   COMPLETE 🟡 draft
Source-audit manifests                  ALIGNED ✅
GitHub Actions blocker #8               RESOLVED ✅
Static QA / vertical slice              PASS ✅
Course Board round-trip                 PASS ✅
P1 host/Docker grading                  PASS ✅
P1 classroom rehearsal                  PENDING ⏳ #7
Flowchart implementation/CI             PASS ✅
Flowchart classroom rehearsal           PENDING ⏳
P2 normal Student Lab                   PASS ✅
P3 normal Student Lab                   PASS ✅
P4 normal Student Lab                   PASS ✅
P3 M28 real course canary               PASS ✅ 5/5 vs 3/5
P2+P3+P4 release candidate identity     PASS ✅ 2026.08.3
P2+P3+P4 same-image platform gate       PASS ✅
P2+P3+P4 same-image course gate         PASS ✅
2026.08.3 publish validation             PASS ✅
2026.08.3 actual publication            NOT DONE ⏳
P2/P3/P4 immutable stable release       PENDING ⏳
Slide real build/engineering QA         PASS ✅
PowerPoint/human slide sign-off         PENDING ⏳ #10
romeo-sim certification                 OPEN ⏳
Teacher sign-off                        PENDING ⏳
Content Pack 1.0 approved               NOT YET ⏳
Ready for classroom / GO                NOT YET ⏳
```

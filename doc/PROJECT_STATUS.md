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

Current post-P3 course evidence:

```text
TheBitLab Python vertical slice
run 33275840276 / #431
SUCCESS

Python combined grading canaries
run 33275840271 / #4
SUCCESS
```

The normal course regression remains green after adding the fourth deliberate Python canary.

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

P2 and P4 use one exact platform source and one candidate toolchain:

```text
TheBitPoets/2cornot2c PR #766 — DRAFT
combined head = 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
toolchain candidate = 2026.08.2
stable checked-in lock = 2026.07.1
P2 = python-function-v1
P4 = python-filesystem-v1
```

Canonical dispatch on that lineage is fail-closed.

Strong platform evidence remains green:

```text
Combined Python grading profiles
run 33259536736 / #3
SUCCESS

Publish assignment runner toolchain / validate
run 33259536908 / #13
SUCCESS
publish SKIPPED — correct for PR

Quality
run 33259536787 / #1871
SUCCESS
```

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
platform ref: 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
candidate toolchain: 2026.08.2
feature provenance: 2cornot2c#763
release path: 2cornot2c#766
```

Controlled change:

```text
print(area) -> return area
```

Current course evidence:

```text
Python M13 P2 canary
run 33275840264 / #35
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
platform ref: 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
candidate toolchain: 2026.08.2
feature provenance: 2cornot2c#764
release path: 2cornot2c#766
```

Controlled change:

```text
print(totale) -> write risultato.txt
```

Current course evidence:

```text
Python M26 P4 canary
run 33275840262 / #17
SUCCESS
```

Behavioral oracle:

```text
solution -> creates risultato.txt -> 1/1 PASS
starter  -> computes and prints correct total,
            but artifact is absent -> 0/1 FAIL
```

Teacher fixture/oracle details remain redacted from the Student Lab report.

---

# 7. P3 — object behavior platform candidate

P3 is no longer an unimplemented blocker.

Platform candidate:

```text
TheBitPoets/2cornot2c PR #767 — DRAFT
profile = python-object-v1
exact source = 1c2889530d0bdd485fa68b233311cd5f91cd67c2
stacked base = 670bc7a7e24d6eab7b4ac9aefda9a0baef8ec6d2
issue = 2cornot2c#758
```

The profile provides:

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

Real platform certification evidence:

```text
Python object profile P3 candidate
run 33275402278 / #3
SUCCESS
```

The same exact P3 head also preserved all previous platform regressions:

```text
Quality #1886                              SUCCESS
Build assignment runner Docker #1049       SUCCESS
Python function profile P2 #35             SUCCESS
Python filesystem profile P4 #23           SUCCESS
P4 Student Lab integration #12             SUCCESS
Combined Python grading profiles #15       SUCCESS
Publish assignment runner validate #25     SUCCESS
Smoke student repository template #143     SUCCESS
uTUI consumer evidence #948                 SUCCESS
```

Normal Docker dispatch now behaves as:

```text
function_tests   -> python-function-v1
object_tests     -> python-object-v1
filesystem_tests -> python-filesystem-v1
none             -> legacy P1/C/Node/SQLite
multiple         -> invalid_payload before student code runs
```

## P3 release identity boundary

The P3 branch is stacked on the P2+P4 candidate and still inherits the manifest string `2026.08.2`.

Therefore:

```text
P3 exact-source candidate = CERTIFIED
P3 immutable stable release = NOT YET
```

Do **not** publish P3 as though the inherited `2026.08.2` were the same immutable release already reviewed for P2+P4.

A distinct P2+P3+P4 release-candidate identity/version must be prepared and validated before publication. The stable lock remains unchanged until a real publish produces a real digest.

---

# 8. P3 — M28 real course canary

The first real non-Romeo OOP consumer is now materialized and green.

```text
Activity: py2-activity-b-serbatoio-invariante-001
M28 / PY2-10
profile: python-object-v1
platform exact source: 1c2889530d0bdd485fa68b233311cd5f91cd67c2
release status: exact-source candidate / not stable
```

Pedagogical invariant:

```text
0 <= livello <= capacita
```

Controlled change:

```text
starter:
  aggiungi() modifica sempre il livello e restituisce True

solution:
  quantità negativa -> False, stato invariato
  overflow          -> False, stato invariato
  transizione valida -> True, stato aggiornato
```

Behavioral oracle:

```text
solution = 5/5 PASS
starter  = 3/5
```

The starter intentionally passes:

```text
stato iniziale
transizione valida
istanze indipendenti
```

and fails exactly:

```text
overflow rifiutato senza cambiare stato
quantita negativa rifiutata
```

Real course evidence:

```text
Python M28 P3 canary
run 33275840266 / #2
SUCCESS
```

That workflow proves, against one image built from the exact P3 source:

1. exact source pin and release boundary;
2. Activity validation;
3. exact 4-file student scaffold;
4. no `object_tests`/expected oracle leak into the public Activity;
5. solution 5/5 through the normal Docker ExecutionService;
6. starter 3/5 with all five scenarios actually executed;
7. exact failed controlled-change scenarios;
8. normal Student Lab solution/starter execution;
9. teacher scenario names and object observations redacted to public `Test 1…N` results.

P3 now satisfies the required **one real `python-docente` OOP consumer** gate.

---

# 9. Activity inventory

Exactly four deliberate Python canaries are materialized:

```text
M04  py2-activity-b-input-somma-001             P1 stdin/stdout
M13  py2-activity-b-return-area-001             P2 function behavior candidate
M26  py2-activity-b-file-risultato-001          P4 filesystem behavior candidate
M28  py2-activity-b-serbatoio-invariante-001    P3 object behavior candidate
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

# 10. PY2-01 / Flowchart Lab

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

# 11. Git G1 consumer

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
config/git-g1-consumer.json
mode = embedded-outcome-subset
```

Structural/process consumer is complete and exercised by course CI. Classroom rehearsal remains separate.

---

# 12. Slide release artifacts — REAL BUILD PASS

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

# 13. Profiles / runtime status

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  unified candidate + real consumer PASS / stable publish pending
P3 object behavior                    exact-source candidate + real M28 consumer PASS / stable release identity pending
P4 filesystem behavior                unified candidate + real consumer PASS / stable publish pending
romeo-sim                              certification pending
```

P3 implementation/canary is no longer a functional blocker. Its remaining blocker is **release promotion**, not behavior certification.

---

# 14. Remaining promotion gates

Teacher sign-off remains `PENDING`; AI/CI cannot approve it.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. final P1 Classroom Environment rehearsal;
2. final Flowchart managed classroom-profile rehearsal;
3. prepare/review a distinct combined P2+P3+P4 release candidate;
4. merge/publish the intended runner release from the reviewed release path;
5. obtain the real GHCR immutable digest and update the reviewed toolchain lock;
6. repin course P2/P3/P4 consumers to the promoted stable release;
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
Curriculum architecture             FROZEN ✅
Frozen outcome mapping              25/25 ✅
Editorial M04–M30                   COMPLETE 🟡 draft
Semantic review M04–M30             COMPLETE 🟡 draft
Content Pack catalog M04–M30        COMPLETE 🟡 draft
Course Design mapping               COMPLETE 🟡 draft
Source-audit manifests              ALIGNED ✅
GitHub Actions blocker #8           RESOLVED ✅
Static QA / vertical slice          PASS ✅
Course Board round-trip             PASS ✅
P1 host/Docker grading              PASS ✅
P1 classroom rehearsal              PENDING ⏳ #7
Flowchart implementation/CI         PASS ✅
Flowchart classroom rehearsal       PENDING ⏳
P2 normal Student Lab               PASS ✅
P3 platform candidate               PASS ✅ exact-source
P3 normal Student Lab               PASS ✅
P3 M28 real course canary           PASS ✅ 5/5 vs 3/5
P4 normal Student Lab               PASS ✅
P2+P4 same-image platform gate      PASS ✅ 2026.08.2 candidate
P2+P4 same-image course gate        PASS ✅
P2+P3+P4 distinct release identity  PENDING ⏳
P2/P3/P4 immutable stable release   PENDING ⏳
Slide real build/engineering QA     PASS ✅
PowerPoint/human slide sign-off     PENDING ⏳ #10
romeo-sim certification             OPEN ⏳
Teacher sign-off                    PENDING ⏳
Content Pack 1.0 approved           NOT YET ⏳
Ready for classroom / GO            NOT YET ⏳
```

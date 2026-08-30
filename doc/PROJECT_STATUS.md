# python-docente — project status

> Ultimo aggiornamento: **2026-08-30**  
> Branch: `agent/course-architecture`  
> Draft PR: `#1`  
> Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`

## Current phase

Il curriculum del secondo anno è **FROZEN** e il layer editoriale M04–M30 è completo in stato `draft`.

Il progetto è nella fase di **delivery / classroom rehearsal / final promotion**.

Restano separati:

```text
curriculum frozen
!= contenuti editoriali completi
!= runtime/grading stabile
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

# 2. Python grading toolchain — `2026.08.3` PUBLISHED + STABLE LOCK

TheBitLab now has one real combined P2 + P3 + P4 stable release:

```text
version = 2026.08.3
release source = 23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
P2 = python-function-v1
P3 = python-object-v1
P4 = python-filesystem-v1
```

Release lineage:

```text
#766 -> P2 + P4 source work
#767 -> P3 object behavior
#768 -> combined release-candidate identity
#770 -> cumulative release transition to main
#771 -> real immutable lock promotion + anti-republish guard
```

## Real publication

```text
Publish assignment runner toolchain
run 33293976574 / #30
validate = SUCCESS
publish  = SUCCESS
```

Published source:

```text
23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
```

Real GHCR immutable digest:

```text
sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
```

Immutable reference:

```text
ghcr.io/thebitpoets/2cornot2c-assignment-runner@sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
```

This digest comes from the successful upstream publication evidence. It is not inferred or invented.

## Stable lock

`2cornot2c#771` promoted the exact published release into:

```text
docker/assignment-runner/toolchain.lock.json
version = 2026.08.3
source_revision = 23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
immutable_reference = ...@sha256:c0594df8...
```

The lock merge commit is:

```text
29c90735a842738c67b798e97b2e5b00696b5e25
```

A release-safety gap was fixed before lock promotion: automatic publication on `main` is now triggered only by a reviewed change to:

```text
docker/assignment-runner/toolchain.json
```

A lock/test/documentation-only merge cannot republish the same version from a different commit.

Post-merge verification confirmed that the lock promotion did **not** trigger a second `2026.08.3` publication.

---

# 3. Platform P2 + P3 + P4 certification

The exact unified release source passed the combined platform gate:

```text
Combined Python grading profiles #17/#18/#19  SUCCESS
P2 candidate workflow                         SUCCESS
P3 candidate workflow                         SUCCESS
P4 candidate workflow                         SUCCESS
legacy P1/C/Node/SQLite Student Lab           SUCCESS
P2 normal Student Lab                         SUCCESS
P3 normal Student Lab                         SUCCESS
P4 normal Student Lab                         SUCCESS
Quality                                       SUCCESS
```

Normal Docker dispatch:

```text
function_tests   -> python-function-v1
object_tests     -> python-object-v1
filesystem_tests -> python-filesystem-v1
none             -> legacy P1/C/Node/SQLite
multiple         -> invalid_payload before student code runs
```

The grading-profile behavior implementation/release phase is therefore **complete**.

---

# 4. Course-side stable release consumption

P2/P3/P4 course profiles now reference the real stable release identity:

```text
TheBitLab release source = 23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
version = 2026.08.3
release PR = #770
stable lock PR = #771
digest = sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
candidate_profile_only = false
```

## Direct GHCR consumer access — operational blocker

A direct pull from `python-docente` was tested with `packages: read` and successful GHCR login, but all P2/P3/P4 workflows received:

```text
Error response from daemon: manifest unknown
```

The same digest was successfully published and remotely verified by the upstream `2cornot2c` release workflow. The failure is therefore recorded as a **cross-repository GHCR Actions access/visibility blocker**, not as a grading or digest failure.

Current course profile records this truth explicitly:

```text
release_identity_status = published-immutable-stable
consumer_image_access_status = ghcr-cross-repository-actions-access-pending
direct_immutable_image_pull_verified = false
```

Until package Actions access is granted to `TheBitPoets/python-docente`, course CI uses the fail-safe fallback:

```text
source-build-from-published-release-source
```

It rebuilds only the exact source that produced the stable release (`23bc1d36...`), with the same pinned Debian snapshot/toolchain manifest. It does **not** fall back to the older release candidate.

This is a delivery workaround, not a downgrade of grading semantics.

---

# 5. Strong stable-source course proof

Latest green evidence after stable promotion/fallback:

```text
Python M13 P2 canary              run 33294985877 / #44  SUCCESS
Python M28 P3 canary              run 33294985878 / #11  SUCCESS
Python M26 P4 canary              run 33294985888 / #26  SUCCESS
Python combined grading canaries  run 33294985932 / #13  SUCCESS
TheBitLab Python vertical slice    run 33294985910 / #440 SUCCESS
```

The combined course workflow:

1. verifies P2/P3/P4 share the same stable release source/version/digest metadata;
2. checks out `23bc1d36...` once;
3. builds one `2026.08.3` runner once;
4. runs M13/P2;
5. runs M28/P3 against the same image;
6. runs M26/P4 against the same image.

All three pass.

`tests/python_grading_toolchain_alignment.py` prevents drift between the three course profiles and keeps the GHCR direct-pull blocker explicit.

---

# 6. Four deliberate Python canaries

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

# 7. P1 — M04 stdin/stdout

```text
Activity = py2-activity-b-input-somma-001
solution = 3/3 PASS
starter  = 1/3, all cases executed
```

Software/Docker path is green. `python-docente#7` remains open for final real Classroom Environment / human rehearsal evidence.

---

# 8. P2 — M13 function behavior

```text
Activity = py2-activity-b-return-area-001
profile = python-function-v1
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

The grader measures function return behavior rather than stdout.

---

# 9. P4 — M26 filesystem behavior

```text
Activity = py2-activity-b-file-risultato-001
profile = python-filesystem-v1
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

# 10. P3 — M28 object behavior

```text
Activity = py2-activity-b-serbatoio-invariante-001
profile = python-object-v1
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

P3 also proves constructor/method/state behavior, expected exceptions, independent instances, hardened container execution and Student Lab teacher-oracle redaction.

---

# 11. PY2-01 / Flowchart Lab

The managed Flowchart candidate includes:

```text
thebitlab.flowchart.v1
headless validator/executor
bounded deterministic trace
Run / Session / Step / Reset
same-origin browser editor
variable watch
managed algorithm.flow.json persistence
JSON import/export
deterministic SVG evidence
runtime plugin / registry
```

Course CI is green. Final classroom-profile rehearsal remains separate; paper/whiteboard/template remains the valid fallback.

---

# 12. Git G1 consumer

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
config/git-g1-consumer.json
mode = embedded-outcome-subset
```

Structural/process consumer is complete. Classroom rehearsal/final evidence remains separate.

---

# 13. Slide release artifacts

Existing real release build evidence:

```text
workflow: Python slide release artifacts
run: 33116692428 / #1
SUCCESS
artifact id: 9664877644
27 HTML + 27 PDF + 27 PPTX
515 rendered/source slides
```

`python-docente#10` remains open for target Microsoft PowerPoint / human visual sign-off. Native PowerPoint object editability is not claimed.

---

# 14. Runtime/profile status

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software certified / classroom rehearsal pending
P2 function behavior                  stable 2026.08.3 + real consumer PASS
P3 object behavior                    stable 2026.08.3 + real M28 consumer PASS
P4 filesystem behavior                stable 2026.08.3 + real consumer PASS
P2+P3+P4 shared platform semantics     PASS
P2+P3+P4 shared course stable-source   PASS
published immutable GHCR release       PASS
stable toolchain lock                  PASS
python-docente direct GHCR pull        BLOCKED by cross-repo package access
romeo-sim                              certification pending
```

The remaining GHCR issue is operational delivery/access only; the grading semantics, release and stable lock are complete.

---

# 15. Remaining promotion gates

Teacher sign-off remains `PENDING`; AI/CI cannot approve it.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. grant/verify cross-repository GHCR package Actions access for `python-docente`, then switch canaries from stable-source rebuild to direct immutable pull;
2. final P1 Classroom Environment rehearsal;
3. final Flowchart managed classroom-profile rehearsal;
4. certify `romeo-sim` before any mandatory Romeo missions;
5. target Microsoft PowerPoint / human slide review;
6. human teacher sign-off;
7. final provenance/license review;
8. explicit Content Pack promotion;
9. final real Classroom Environment rehearsal;
10. explicit classroom GO decision.

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
2026.08.3 publication                   PASS ✅
2026.08.3 real immutable digest         PASS ✅ c0594df8...
2026.08.3 stable toolchain lock         PASS ✅ #771
anti-republish release guard            PASS ✅
P2/P3/P4 stable-source course gate      PASS ✅ #13
python-docente direct GHCR pull         BLOCKED ⏳ package Actions access
Slide real build/engineering QA         PASS ✅
PowerPoint/human slide sign-off         PENDING ⏳ #10
romeo-sim certification                 OPEN ⏳
Teacher sign-off                        PENDING ⏳
Content Pack 1.0 approved               NOT YET ⏳
Ready for classroom / GO                NOT YET ⏳
```

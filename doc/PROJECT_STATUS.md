# python-docente — project status

> Ultimo aggiornamento: **2026-09-03**
> Branch: `agent/course-architecture`  
> Draft PR: `#1`  
> Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`

## Current phase

Il curriculum del secondo anno è **FROZEN** e il layer editoriale M04–M30 è completo in stato `draft`.

Il progetto è nella fase di **delivery / classroom rehearsal / final promotion**.

Restano deliberatamente separati:

```text
curriculum frozen
!= contenuti editoriali completi
!= runtime/grading stabile
!= managed launcher technically certified
!= docker-light technical profile certified
!= vm-gui / real classroom host rehearsed
!= human teacher sign-off
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

# 2. Python grading toolchain — `2026.08.3` PUBLISHED + STABLE

TheBitLab has one real combined P2 + P3 + P4 stable release:

```text
version = 2026.08.3
release source = 23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
P2 = python-function-v1
P3 = python-object-v1
P4 = python-filesystem-v1
```

Release lineage:

```text
#766 -> P2 + P4
#767 -> P3 object behavior
#768 -> combined candidate identity
#770 -> cumulative release transition to main
#771 -> immutable stable lock + anti-republish guard
```

Real publication:

```text
Publish assignment runner toolchain
run 33293976574 / #30
validate = SUCCESS
publish  = SUCCESS
```

Real immutable digest:

```text
sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
```

Immutable reference:

```text
ghcr.io/thebitpoets/2cornot2c-assignment-runner@sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
```

Stable lock merge commit:

```text
29c90735a842738c67b798e97b2e5b00696b5e25
```

Automatic publication on `main` is restricted to a reviewed `toolchain.json` manifest/version change; lock/test/documentation-only changes cannot silently republish an existing version.

---

# 3. Python grading platform certification

The stable implementation supports the normal Student Lab dispatcher:

```text
function_tests   -> python-function-v1
object_tests     -> python-object-v1
filesystem_tests -> python-filesystem-v1
none             -> legacy P1/C/Node/SQLite
multiple         -> invalid_payload before student code runs
```

Platform evidence for the unified grading line is green, including P2/P3/P4 candidates, normal Student Lab dispatch, legacy paths and shared combined gates.

The grading-profile implementation/release phase is **complete**.

---

# 4. Course-side stable release consumption

P2/P3/P4 course profiles reference the real stable release identity:

```text
TheBitLab release source = 23bc1d36c7eb8c1b10a11cbde5f226ce7554f85e
version = 2026.08.3
release PR = #770
stable lock PR = #771
digest = sha256:c0594df833925044831463a9ee631aba2688929951a7dbcb53612b86d221ed51
candidate_profile_only = false
```

## Direct GHCR consumer access — operational blocker

A direct pull from `python-docente` was tested with `packages: read` and successful GHCR login, but GHCR returned:

```text
Error response from daemon: manifest unknown
```

Upstream publication and remote verification of the same digest succeeded. This remains a **cross-repository GHCR Actions access/visibility blocker**, not a grading or digest failure.

Until package Actions access is granted to `TheBitPoets/python-docente`, course CI uses the fail-safe delivery fallback:

```text
source-build-from-published-release-source
```

It rebuilds only the exact source that produced stable `2026.08.3`; it does not fall back to an older candidate.

---

# 5. Latest course grading proof

Latest green evidence on the head that introduced the P1 classroom-profile rehearsal:

```text
Python M13 P2 canary              run 33322459858 / #57  SUCCESS
Python M26 P4 canary              run 33322459901 / #39  SUCCESS
Python M28 P3 canary              run 33322459891 / #24  SUCCESS
Python combined grading canaries  run 33322459915 / #26  SUCCESS
TheBitLab Python vertical slice    run 33322459876 / #453 SUCCESS
```

The combined grading gate still proves one shared stable-source runner for P2/P3/P4.

Exactly four deliberate Python canaries are materialized:

```text
M04  py2-activity-b-input-somma-001             P1 stdin/stdout
M13  py2-activity-b-return-area-001             P2 function behavior
M26  py2-activity-b-file-risultato-001          P4 filesystem behavior
M28  py2-activity-b-serbatoio-invariante-001    P3 object behavior
```

Behavioral discrimination remains:

```text
M04 solution/edit 3/3; starter 1/3
M13 solution 3/3; starter 0/3 despite correct numeric stdout
M26 solution 1/1; starter 0/1 despite correct computed value
M28 solution 5/5; starter 3/5, failing exactly negative quantity + overflow invariants
```

No mass Activity generation is authorized yet.

---

# 6. PY2-01 / Flowchart Lab — managed launcher technical PASS

The Flowchart stack includes:

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
Student Runtime CLI launcher
```

Course pin:

```text
TheBitPoets/2cornot2c
ref = 736bbfddfb79e431b9dedbfd1d877f06aa8b02b5
```

Real managed-launcher technical evidence:

```text
Flowchart managed classroom certification
run 33321478705 / #12 — SUCCESS
Ubuntu / Windows / macOS = PASS
```

The rehearsal starts the **real `student_runtime_cli launch` as a subprocess** and verifies from outside that process:

```text
assignment selection
→ runtime registry/probe
→ managed loopback launch
→ browser UI reachable
→ save/load algorithm.flow.json
→ deterministic Run
→ Session/Step + variable watch
→ deterministic SVG
→ launcher owns endpoint lifecycle
→ endpoint dies with launcher
→ no authoritative autograding claim
```

The rehearsal exposed and fixed two real defects that in-process tests had hidden:

1. the CLI returned after starting a daemon-thread server, destroying the endpoint;
2. Python `HTTPServer.server_bind()` performed an unnecessary reverse/FQDN lookup on loopback, stalling the macOS profile.

Final fix uses a dedicated loopback HTTP server bind that does **not** call `socket.getfqdn()`. A regression test forces `getfqdn()` to fail and proves server creation remains valid.

Same final upstream head is green on:

```text
Quality                              #1911 SUCCESS
Build assignment runner Docker       #1074 SUCCESS
uTUI consumer evidence               #969 SUCCESS
Romeo sim cross-profile              #18 SUCCESS
Publish toolchain validation          #49 SUCCESS
Flowchart managed launcher           #12 SUCCESS
```

## Truth boundary

This is a **cross-platform managed-launcher technical PASS**, not final classroom certification.

`config/flowchart-lab-candidate.json` therefore correctly remains:

```text
status = candidate-not-certified
candidate_ci_is_classroom_certification = false
fallback_remains_required = true
supported_profile_rehearsal_required = true
human_usability_review_required = true
```

`flowchart.manual-evidence.v1` remains a valid fallback until the real docker-light/vm-gui rehearsal and human browser usability review are complete.

---

# 7. Romeo simulator — managed runtime certified

`romeo-sim` is technically certified as a managed simulator runtime. Physical Romeo hardware is neither required nor claimed as certified.

Cross-profile evidence:

```text
Romeo sim cross-profile certification
run 33315344675 / #3 — SUCCESS
Ubuntu / Windows / macOS = PASS
```

Authoritative runtime evidence:

```text
Romeo 0.2.0 release source = 584ba489000a559f9e4cd3326a83f925d6c73a45
release workflow = 32518993805
image = ghcr.io/thebitpoets/romeo-runtime@sha256:db7373cc6d24337427d0071dd633f902e266ffae1c440cd2bd605564bb3c7581
```

The certification:

1. pulls the exact immutable digest;
2. installs the matching Romeo 0.2.0 plugin;
3. verifies digest-pinned sandbox eligibility;
4. executes official `y1-u08-avanti-indietro` and `y2-u07-json` Activities through the current TheBitLab broker;
5. verifies authoritative Docker execution;
6. proves mutable/missing image identities fail closed.

This closes the technical Romeo simulator blocker for simulated course missions.

---

# 8. P1 M04 — docker-light technical classroom profile certified

P1 M04 already had green host/Docker grading. It now also has a real technical rehearsal inside the actual Course Environment `docker-light` student image.

Pinned environment:

```text
TheBitPoets/2cornot2c
Course Environment source = 736bbfddfb79e431b9dedbfd1d877f06aa8b02b5
student-dev version = 2026.07.1
Ubuntu snapshot = 20260713T000000Z
Python = 3.12.3
student UID/GID = 1000
```

Authoritative technical evidence:

```text
M04 docker-light classroom profile
run 33322459863 / #5 — SUCCESS
linux/amd64 PASS
linux/arm64 PASS
```

The workflow does not copy a hand-made fake workspace. It:

1. checks out the exact historical TheBitLab scaffold-generation baseline pinned for M04;
2. generates two real managed student scaffolds with `scripts.create_submission_scaffold`;
3. preserves the public student surface only:
   `README.md`, `activity.json`, `main.py`, `GUIDA.md`;
4. verifies teacher tests/oracles/solution paths are not exposed;
5. builds the exact `student-dev 2026.07.1` image from the pinned Course Environment source for both amd64 and arm64;
6. runs as the real non-root `student` user UID 1000;
7. proves the bind-mounted managed workspace is writable by that student;
8. feeds the real M04 stdin cases through Docker interactive stdin;
9. gets the exact discrimination:

```text
starter = 1/3
corrected student edit = 3/3
```

This closes the **docker-light technical profile** portion of `python-docente#7`.

## P1 truth boundary

Issue #7 must remain open. This CI evidence does **not** replace:

```text
vm-gui rehearsal on the released classroom boxes
real school/classroom host rehearsal
human teacher evidence/sign-off
```

The two upstream classroom box releases are already physically published/collated upstream, but M04 has not yet been rehearsed inside those boxes as a course consumer.

## Rehearsal kit vm-gui — READY TO RUN

Il gate fisico non è stato marcato PASS. È ora disponibile un pacchetto
eseguibile e registrabile:

```text
tests/m04_vm_gui_rehearsal.py
teacher/M04_CLASSROOM_REHEARSAL.md
teacher/M04_CLASSROOM_REHEARSAL_RECORD.md
evidence/m04-vm-gui/
```

L'harness:

1. rifiuta checkout con modifiche tracciate e un `2cornot2c` diverso dal pin;
2. verifica box, provider, release attiva, Python guest e GUI;
3. usa `.vagrant` su Windows/VirtualBox e la directory reale
   `.vagrant-vmware` su macOS/VMware;
4. prova starter `1/3` e modifica controllata `3/3` dentro la guest;
5. può salvare un report JSON nuovo e non sovrascrivibile con commit, host,
   release, manifest ed evidenza per caso;
6. registra esplicitamente `classroom_ready = false`, human usability non
   osservata e teacher sign-off pending.

Il record umano resta separato e deve documentare launcher normale, desktop,
editor, terminale, workspace condiviso e persistenza sul vero host. Stato
attuale: **harness READY; physical/human evidence PENDING**.

---

# 9. Git G1 consumer

Git G1 consumer remains structurally complete:

```text
TheBitPoets/git
G1 candidate ref = 65d8aff8c9a590560c500762d4dc7378a3239bf2
mode = embedded-outcome-subset
```

Classroom evidence for Git remains part of the final environment rehearsal rather than a new curriculum blocker.

---

# 10. Slide release artifacts

Existing real build evidence:

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

# 11. Runtime/profile status

```text
P0 manual/trace/design                 available by pedagogy
P1 stdin/stdout                        software PASS + docker-light amd64/arm64 PASS
P1 vm-gui / real classroom host       PENDING
P2 function behavior                  stable 2026.08.3 + real consumer PASS
P3 object behavior                    stable 2026.08.3 + real M28 consumer PASS
P4 filesystem behavior                stable 2026.08.3 + real consumer PASS
P2+P3+P4 shared platform semantics     PASS
P2+P3+P4 shared course stable-source   PASS
published immutable GHCR release       PASS
stable toolchain lock                  PASS
python-docente direct GHCR pull        BLOCKED by cross-repo package access
flowchart managed launcher             PASS Ubuntu/Windows/macOS
flowchart final classroom approval     PENDING profile + human review
romeo-sim                              CERTIFIED managed simulator PASS
```

---

# 12. Remaining promotion gates

Teacher sign-off remains `PENDING`; AI/CI cannot approve it.

Before `Content Pack 1.0.0 / approved` and classroom GO remain at least:

1. grant/verify cross-repository GHCR package Actions access for `python-docente`, then switch canaries from stable-source rebuild to direct immutable pull;
2. P1 M04 `vm-gui` rehearsal on the released classroom boxes + final real host/human evidence;
3. Flowchart real docker-light/vm-gui classroom-profile rehearsal;
4. Flowchart human browser usability/teacher evidence review;
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
Static QA / vertical slice              PASS ✅ #453
Course Board round-trip                 PASS ✅
P1 host/Docker grading                  PASS ✅
P1 docker-light amd64                   PASS ✅ #5
P1 docker-light arm64                   PASS ✅ #5
P1 vm-gui / real classroom host         PENDING ⏳ #7
Flowchart implementation/core CI        PASS ✅
Flowchart managed CLI lifecycle         PASS ✅ Ubuntu/Windows/macOS #12
Flowchart reverse-DNS regression        PASS ✅
Flowchart exact course consumer         PASS ✅
Flowchart classroom profile rehearsal   PENDING ⏳
Flowchart human usability review        PENDING ⏳
P2 normal Student Lab                   PASS ✅
P3 normal Student Lab                   PASS ✅
P4 normal Student Lab                   PASS ✅
P3 M28 real course canary               PASS ✅ 5/5 vs 3/5
2026.08.3 publication                   PASS ✅
2026.08.3 real immutable digest         PASS ✅ c0594df8...
2026.08.3 stable toolchain lock         PASS ✅ #771
anti-republish release guard            PASS ✅
P2/P3/P4 stable-source course gate      PASS ✅ #26
python-docente direct GHCR pull         BLOCKED ⏳ package Actions access
romeo-sim plugin cross-profile          PASS ✅ Ubuntu/Windows/macOS
romeo-sim immutable Docker broker       PASS ✅ db7373cc...
romeo-sim official simulated Activities PASS ✅
Slide real build/engineering QA         PASS ✅
PowerPoint/human slide sign-off         PENDING ⏳ #10
Teacher sign-off                        PENDING ⏳
Content Pack 1.0 approved               NOT YET ⏳
Ready for classroom / GO                NOT YET ⏳
```

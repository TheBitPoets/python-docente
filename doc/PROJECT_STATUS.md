# python-docente — project status

## Current phase

**Curriculum FROZEN + M04–M30 editorialmente completi, catalogati e semanticamente revisionati; delivery/release QA phase with real CI execution restored.**

Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`  
Decision-owner approval: **2026-08-24**.  
Branch: `agent/course-architecture`  
Draft PR: `#1`.

`Content Pack 1.0 / approved` e `ready for classroom` restano gate futuri separati.

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
PY2-01 final digital delivery           implementation upstream / certification pending
```

Review index canonico:

```text
doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md
```

Regola didattica trasversale:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# 2. Authoritative Content Pack / Course Design catalog — M04–M30 COMPLETE

`python-docente#11` è chiusa come completed.

Content Pack:

```text
content/python/content-pack.json
version = 0.1.0
status = draft
content_items = exactly M04…M30
python-course-content.files = exactly M04…M30
```

Course Design:

```text
doc/course_design.json
python-course-content.files = exactly M04…M30
```

Mapping machine-readable UDA → moduli:

```text
PY2-02  M04–M05
PY2-03  M06–M08
PY2-04  M09–M12
PY2-05  M13–M16
PY2-06  M17–M19
PY2-07  M20–M22
PY2-08  M23–M25
PY2-09  M26
PY2-10  M27–M30
```

Il mapping usa `content_item_ids` separato da `items`, perché `items` appartiene al modello Course Board degli heading/subtree.

Protection:

```text
scripts/sync_authoring_catalog.py
tests/course_authoring_catalog.py
```

Il gate richiede esattamente 27 moduli M04–M30, source parity Content Pack/Course Design e assegnazione esatta di ogni content item a una sola UDA.

La precedente validazione sintetica è stata superata da **esecuzione CI reale** dopo il ripristino di GitHub Actions.

---

# 3. Provenance source manifests — ALIGNED

`python-docente#9` è chiusa come completed.

`python-source-audits.files` in Content Pack e Course Design contiene esattamente:

```text
SOURCE_CATALOG.md
FRIEDPYTHON_MAPPING.md
FRIEDPYTHON_LISTS_TUPLES_AUDIT.md
FRIEDPYTHON_DICTS_AUDIT.md
FRIEDPYTHON_FILES_AUDIT.md
```

Helper/gate:

```text
scripts/sync_source_audit_manifest.py
```

Il controllo è incluso nell'entrypoint statico unificato ed è ora eseguito realmente in Actions.

Nessun `friedpython` wholesale import: ogni riuso resta audit individuale + riscrittura/modernizzazione.

---

# 4. Static QA / real Actions evidence — RESTORED

Entrypoint unico:

```text
python scripts/run_static_quality.py
```

Include:

- authoring catalog synchronization;
- source-audit manifest synchronization;
- exact M04–M30 authoring/UDA catalog gate;
- semantic review boundaries;
- Git G1 consumer contract;
- frozen outcome coverage;
- slide source quality;
- slide toolchain/build-profile pin gate;
- M04 vertical-slice static QA;
- P1 canary profile contract;
- M04 P1 direct preflight;
- M05 pedagogical static QA.

Il 27 agosto 2026 `python-docente` è stato reso pubblico. Lo stesso workflow che da repository privato moriva pre-runner con `steps=null` ha iniziato a eseguire realmente checkout, Python e test. `python-docente#8` è quindi **CLOSED / completed**.

Evidence reale ottenuta su GitHub-hosted runners:

```text
Ubuntu / Python 3.12   static QA                         PASS
Windows / Python 3.12  static QA                         PASS
Ubuntu                  pinned TheBitLab checkout         PASS
Windows                 pinned TheBitLab checkout         PASS
Ubuntu                  Course Workspace round-trip       PASS
Windows                 Course Workspace round-trip       PASS
Ubuntu                  host P1 consumer smoke            PASS
Windows                 host P1 consumer smoke            PASS
```

Il direct P1 preflight su Python 3.12 dimostra:

```text
solution = 3/3 PASS
starter  = 1/3 PASS, ma esegue tutti e 3 i casi
```

Quindi il set di test discrimina realmente la modifica richiesta.

Due difetti ordinari emersi solo dopo l'avvio reale dei runner sono stati corretti senza cambiare la semantica del corso:

1. gate M05 troppo accoppiati a maiuscole/formattazione Markdown;
2. output finale Course Board con freccia Unicode non stampabile sulla console Windows cp1252.

---

# 5. Git G1 consumer — STRUCTURAL COMPLETE

Source of truth:

```text
TheBitPoets/git
G1 candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
```

Consumer:

```text
config/git-g1-consumer.json
mode = embedded-outcome-subset
full_g1_track_completion_required = false
full_canonical_lesson_completion_required = false
```

Progressione:

```text
M14–M16          status/diff guided
Checkpoint A     status → diff → test → add → diff --staged → commit → status → log/show
second semester  reuse G1 + progressive recovery
```

Git resta evidence di processo nel Python, non un secondo corso high-stakes. Il contratto statico è ora eseguito realmente in CI; il rehearsal didattico resta separato.

---

# 6. M04 / P1 Activity — SOFTWARE + IMMUTABLE DOCKER EVIDENCE PASS

Unica nuova Activity Python materializzata:

```text
py2-activity-b-input-somma-001 — M04 — P1 canary
```

Certification issue: `python-docente#7`.

Profilo machine-readable:

```text
config/p1-canary-profile.json
TheBitLab = cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
Python host = 3.12
runner = ghcr.io/thebitpoets/2cornot2c-assignment-runner@sha256:62f0f7b7bc1d48d01b7f8e5fa765e0b43be3622e70a614033b1bb4a4e522e159
toolchain = 2026.07.1
```

Real PASS evidence ora copre:

- Content Pack validation contro il baseline pinned;
- Activity validation;
- generazione exact student scaffold;
- assenza teacher/solution/hidden expected-output leakage;
- solution 3/3;
- starter 1/3 ma tutti e tre i casi eseguiti;
- host smoke Python 3.12 su Ubuntu e Windows;
- Course Workspace save/reopen round-trip su Ubuntu e Windows;
- **authoritative immutable Docker grading**.

Authoritative Docker run:

```text
TheBitPoets/2cornot2c Actions run 33083704963
job 98557492246
conclusion = SUCCESS

python-docente = 18b0d26fa9b449f6bd613430d0c917e80567d4bc
TheBitLab      = cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
Python         = 3.12.14
runner digest  = sha256:62f0f7b7bc1d48d01b7f8e5fa765e0b43be3622e70a614033b1bb4a4e522e159
```

Final worker evidence:

```text
PASS: pinned Content Pack + Activity + exact student scaffold +
Python starter/solution deterministic grading (immutable Docker grading)
```

`#7` resta **OPEN** perché software/Docker certification non equivale ancora a classroom certification. Mancano:

- apertura/assegnazione completa attraverso il vero managed student-facing path;
- rehearsal finale dei profili Classroom Environment supportati.

### GHCR cross-repository access

Il normale workflow `python-docente` è volutamente fail-closed sull'ultimo step Docker perché il package GHCR del runner è repository-scoped: il token Actions di `python-docente` non riesce ancora a scaricarlo.

Il package e il digest sono validi: dal repository produttore `2cornot2c` il digest è scaricabile e il P1 Docker passa. Serve ancora una configurazione GitHub Package amministrativa per concedere Actions access a `TheBitPoets/python-docente` oppure una decisione esplicita di visibilità del package.

Questo è un problema di delivery/permission del workflow consumer, non un fallimento del contratto P1.

---

# 7. Activity / grading policy

Policy:

```text
outcome
→ evidence profile corretto
→ profile certification
→ Activity materialization
```

Profili:

- P0 — manual/trace/design;
- P1 — stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — `romeo-sim` external runtime.

Non deformare P2/P3/P4 in P1 per ottenere un voto automatico.

---

# 8. Flowchart Lab / PY2-01 — IMPLEMENTED UPSTREAM, CERTIFICATION PENDING

`2cornot2c#753` / draft PR `#754` hanno ormai un managed Flowchart Lab MVP composto da:

```text
thebitlab.flowchart.v1 artifact
→ headless validator/executor
→ thebitlab.flowtrace.v1
→ loopback service/API
→ browser editor
→ managed algorithm.flow.json workspace persistence
→ deterministic SVG evidence
→ built-in runtime plugin / registry
```

Sono presenti core, API Run/Session/Step/Reset, browser editor offline same-origin, variable watch, workspace load/save, JSON import/export, SVG evidence e runtime plugin.

Il boundary resta:

```text
implemented + tested != classroom certified
```

Per questo PY2-01 non viene ancora dichiarata digitalmente pronta e il fallback frozen resta valido:

```text
paper / whiteboard
→ pseudocodice
→ manual flow chart
→ trace
→ test cases
```

Prima della promozione servono ancora real managed-profile rehearsal/certification e il primo consumer PY2-01 nel percorso studente effettivo.

---

# 9. Slide artifact layer — TOOLCHAIN/PIPELINE IMPLEMENTED, REAL BUILD PENDING

27 source deck M04–M30 presenti.

Pin release:

```text
@marp-team/marp-cli 4.5.0
platform: linux/amd64
image:
  ghcr.io/marp-team/marp-cli@sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
Node in upstream v4.5.0 image recipe: 26.5.0
browser: Chromium pinned by exact image digest; reported version recorded at build
```

Surfaces:

```text
config/slide-build-profile.json
tests/slide_source_quality.py
tests/slide_build_profile.py
scripts/build_slide_artifacts.py
tests/slide_artifact_quality.py
.github/workflows/slide-artifacts.yml
teacher/SLIDE_VISUAL_REVIEW.md
doc/SLIDE_ARTIFACT_PIPELINE.md
```

Build target:

```text
27 HTML
27 PDF
27 PPTX
+ build-manifest.json with source/artifact hashes + toolchain provenance
```

Issue `#10` resta aperta perché ancora mancano:

- build reale 27×3;
- structural artifact QA su file reali;
- visual review M04/M11/M18/M22/M26/M30;
- verifica apertura/comportamento PPTX nel consumer target.

Ora che Actions eseguono realmente, questo diventa uno dei prossimi gate praticabili.

---

# 10. Teacher / release gates

Teacher sign-off:

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
status = PENDING
```

Non può essere auto-approvato da AI/CI.

Prima di `Content Pack 1.0.0 / approved` restano almeno:

1. completare `#7` con managed assignment + classroom-profile rehearsal;
2. eseguire/chiudere slide artifact build + visual QA `#10`;
3. certificare Flowchart Lab/Classroom Environment e materializzare il consumer PY2-01 corretto;
4. certificare P2/P4/P3 prima delle relative promesse di autograding;
5. certificare `romeo-sim` prima di missioni obbligatorie;
6. materializzare Activity per profilo/UDA con evidence corretta;
7. risolvere il GHCR Actions access del consumer `python-docente` per rendere verde anche il percorso Docker nel suo workflow ordinario;
8. teacher sign-off umano;
9. final provenance/license review del release candidate;
10. promuovere esplicitamente Content Pack solo dopo i gate;
11. real TheBitLab classroom-profile rehearsal;
12. GO classroom.

---

# Gate status

```text
Curriculum architecture        FROZEN ✅
Frozen outcome mapping         25/25 ✅
Editorial M04–M30              COMPLETE 🟡 draft
Semantic review M04–M30        COMPLETE 🟡 draft
Content Pack catalog M04–M30   COMPLETE 🟡 draft
Course Design M04–M30 mapping  COMPLETE 🟡 draft
Source-audit manifests         ALIGNED ✅ real CI
Static QA Ubuntu/Windows       PASS ✅
Course Board round-trip        PASS ✅ Ubuntu + Windows
P1 host smoke                  PASS ✅ Ubuntu + Windows / Python 3.12
P1 immutable Docker grading    PASS ✅ exact locked runner
P1 classroom rehearsal         PENDING ⏳ #7
Private Actions blocker #8     RESOLVED ✅ repo public
Git G1 structural consumer     COMPLETE ✅ static CI / rehearsal pending
Flowchart Lab implementation   IMPLEMENTED 🟡 certification pending
Slide generated artifacts      NOT YET ⏳ #10
P2/P3/P4 grading               OPEN ⏳
romeo-sim certification        OPEN ⏳
Teacher sign-off               PENDING ⏳
Content Pack 1.0 approved      NOT YET ⏳
Ready for classroom / GO       NOT YET ⏳
```

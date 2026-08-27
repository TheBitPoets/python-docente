# python-docente — project status

## Current phase

**Curriculum FROZEN + M04–M30 editorialmente completi, catalogati e semanticamente revisionati; delivery/release QA phase.**

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
PY2-01 final digital delivery           SPEC-only / Flowchart Lab pending
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

Il gate richiede **esattamente 27 moduli M04–M30**, source parity Content Pack/Course Design e assegnazione esatta di ogni content item a una sola UDA.

Validazione sintetica del nuovo contratto:

```text
PASS: authoring catalog sincronizzato su 27 moduli M04–M30
PASS: 27 moduli M04–M30 coerenti in Content Pack, Course Design e UDA mapping
```

Questa è evidence logica del contratto, non sostituisce l'esecuzione sul checkout reale/CI.

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

Il controllo è incluso nell'entrypoint statico unificato.

Nessun `friedpython` wholesale import: ogni riuso resta audit individuale + riscrittura/modernizzazione.

---

# 4. Static QA entrypoint

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
- M05 pedagogical static QA.

La workflow privata usa questo entrypoint prima dei consumer check TheBitLab.

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

Git resta evidence di processo nel Python, non un secondo corso high-stakes.

---

# 6. Activity / grading state

Unica nuova Activity Python materializzata:

```text
py2-activity-b-input-somma-001 — M04 — P1 canary
```

Certification: `python-docente#7`.

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

# 7. CI blocker #8 — CURRENT HEAD STILL PRE-RUNNER

Sul current head osservato `ceb2791013b79c4e22f53294224b56caa5726fe1`:

```text
workflow run 33059326027 / #309
ubuntu-latest  failure / steps=null
windows-latest failure / steps=null
```

Nessuno step ha iniziato l'esecuzione.

Quindi questa run **non è evidence di PASS né di FAIL** per:

- static quality suite;
- catalog M04–M30;
- provenance manifest;
- semantic/coverage/Git gates;
- slide build-profile gate;
- Course Board round-trip;
- Python TheBitLab smoke.

Issue: `python-docente#8`.

Leading hypotheses già ristrette: quota/budget/spending dei private Actions oppure hosted-runner policy organizzativa.

---

# 8. Slide artifact layer — TOOLCHAIN/PIPELINE IMPLEMENTED, REAL BUILD PENDING

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

La workflow slide è `workflow_dispatch` Ubuntu-only per evitare build costose a ogni PR.

Issue `#10` resta aperta perché ancora mancano:

- build reale 27×3;
- structural artifact QA su file reali;
- visual review M04/M11/M18/M22/M26/M30;
- verifica apertura/comportamento PPTX nel consumer target.

Non dichiarare artifact PASS o PPTX completamente editabile prima di questi gate.

---

# 9. PY2-01 boundary

PY2-01 resta deliberatamente SPEC-only finché Flowchart Lab / Classroom Environment non è truthful/certified.

Fallback frozen valido:

```text
paper / whiteboard
→ pseudocodice
→ manual flow chart
→ trace
→ test cases
```

Blocker: `python-docente#2`, `2cornot2c#753/#754`.

---

# 10. Teacher / release gates

Teacher sign-off:

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
status = PENDING
```

Non può essere auto-approvato da AI/CI.

Prima di `Content Pack 1.0.0 / approved` restano almeno:

1. risolvere `#8` e far eseguire sul checkout reale i gate già scritti;
2. certificare M04/P1 `#7`;
3. eseguire/chiudere slide artifact build + visual QA `#10`;
4. chiudere PY2-01 Flowchart Lab/environment boundary;
5. certificare P2/P4/P3 prima delle relative promesse di autograding;
6. certificare `romeo-sim` prima di missioni obbligatorie;
7. materializzare Activity per profilo/UDA con evidence corretta;
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
Source-audit manifests         ALIGNED 🟡 runtime CI pending
Git G1 structural consumer     COMPLETE 🟡 runtime evidence pending
Slide toolchain/build/QA code  IMPLEMENTED 🟡 real build pending
PY2-01 final digital delivery  BLOCKED/WAITING 🟡
P1 golden vertical slice       CREATED / NOT CERTIFIED 🟡
Private Actions runners        BLOCKED 🔴 #8
Slide generated artifacts      NOT YET ⏳ #10
P2/P3/P4 grading               OPEN ⏳
romeo-sim certification        OPEN ⏳
Teacher sign-off               PENDING ⏳
Content Pack 1.0 approved      NOT YET ⏳
Ready for classroom / GO       NOT YET ⏳
```

# Python docente

Repository di progettazione e delivery del curriculum Python TheBitPoets.

## Stato corrente

```text
Secondo anno 2026/27
Curriculum architecture        FROZEN
Core editorial M04–M30         COMPLETE / draft
Semantic review M04–M30        COMPLETE / draft
Checkpoint A/B/C review        COMPLETE / draft
Coverage 25 frozen outcomes    MAPPED
Git G1 structural consumer     COMPLETE / delivery evidence pending
PY2-01 flow chart              SPEC-only / Flowchart Lab pending
P1/P2/P3/P4 certification      NOT COMPLETE
Teacher sign-off               PENDING
Content Pack 1.0 approved      NOT YET
Ready for classroom            NOT YET
```

Il curriculum annuale è congelato, ma **freeze curricolare, coverage editoriale, Activity coverage, grading certification, teacher sign-off e classroom-ready sono gate distinti**.

## Entrypoint

- studente: [`student/README.md`](student/README.md)
- docente: [`teacher/README.md`](teacher/README.md)
- curriculum freeze: [`doc/CURRICULUM_FREEZE_2026_2027.md`](doc/CURRICULUM_FREEZE_2026_2027.md)
- stato progetto: [`doc/PROJECT_STATUS.md`](doc/PROJECT_STATUS.md)
- mappa moduli: [`tracks/secondo/MODULE_MAP.md`](tracks/secondo/MODULE_MAP.md)
- semantic review: [`doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md`](doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md)
- coverage/provenance: [`doc/COVERAGE.md`](doc/COVERAGE.md)
- machine coverage: [`config/curriculum-coverage.json`](config/curriculum-coverage.json)
- slide pipeline: [`doc/SLIDE_ARTIFACT_PIPELINE.md`](doc/SLIDE_ARTIFACT_PIPELINE.md)
- teacher sign-off: [`teacher/TEACHER_SIGNOFF_CHECKLIST.md`](teacher/TEACHER_SIGNOFF_CHECKLIST.md)
- integrazione Git G1: [`tracks/secondo/GIT_G1_INTEGRATION.md`](tracks/secondo/GIT_G1_INTEGRATION.md)
- consumer contract Git: [`config/git-g1-consumer.json`](config/git-g1-consumer.json)

## Architettura delivery

```text
repo checkout
= Course Workspace mutabile

Content Pack
= identità e catalogo dei moduli

Course Board
= granularità editoriale heading-tree

Git
= storia e review del workspace

Course Bundle
= release immutabile
```

## Secondo anno

Il track 2026/27 è di 33 settimane × 3 ore, da problem solving e algoritmi fino a strutture dati, file ed OOP/capstone.

M04–M30 hanno lesson canonica, deck Marp e runbook docente. Il core materializzato è stato revisionato semanticamente UDA per UDA usando il boundary:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

PY2-01 resta volutamente SPEC-only finché il Flowchart Lab non è certificato; carta/lavagna/pseudocodice/trace restano fallback valido.

## Coverage

I 25 outcome frozen sono mappati in `doc/COVERAGE.md` e `config/curriculum-coverage.json`.

Importante:

```text
coverage editoriale
≠ Activity coverage
≠ automated grading coverage
≠ teacher sign-off
≠ classroom readiness
```

Oggi il corso Python materializza una sola nuova Activity automatica canonica: il canarino M04 `py2-activity-b-input-somma-001`.

## Git G1

Git è un curriculum separato. Python seconda consuma soltanto il sottoinsieme G1 necessario al workflow:

```text
M14–M16
  status / diff — guided

Checkpoint A
  status → diff → test → add → diff --staged → commit → status → log/show

secondo semestre
  riuso G1 + recovery progressiva
```

Source of truth: `TheBitPoets/git`. La dipendenza corrente è registrata in `config/git-g1-consumer.json` in modalità `embedded-outcome-subset`.

## Activity e grading

M04 contiene il golden vertical slice P1 `py2-activity-b-input-somma-001`.

Profili TheBitLab:

- P0 — manual/trace/design;
- P1 — stdin/stdout;
- P2 — function behavior;
- P3 — object behavior;
- P4 — filesystem behavior;
- `romeo-sim` — runtime applicativo separato.

Non vengono creati falsi grader adattando outcome a un profilo non certificato.

## Slide delivery

I 27 deck Marp M04–M30 sono source canonici. La pipeline artifact target è:

```text
Markdown
→ source QA
→ renderer pinned
→ HTML / PDF / PPTX
→ artifact QA
→ visual review
→ teacher sign-off
```

La build reale non è ancora certificata; non confondere source deck presenti con artifact già validati.

## Gate aperti

- managed Classroom Environment / Flowchart Lab;
- beginner REPL/editor workflow;
- P1 canary certification;
- private GitHub Actions pre-runner blocker;
- P2/P3/P4;
- `romeo-sim` cross-profile;
- slide artifact build/QA;
- teacher sign-off;
- provenance/coverage final review;
- real TheBitLab rehearsal;
- Content Pack approval.

Vedi [`doc/PROJECT_STATUS.md`](doc/PROJECT_STATUS.md) per il checkpoint operativo aggiornato.
# Python docente

Repository di progettazione e delivery del curriculum Python TheBitPoets.

## Stato corrente

```text
Secondo anno 2026/27
Curriculum architecture        FROZEN
Core editorial M04–M30         COMPLETE / draft
Checkpoint A/B/C               COMPLETE / draft
Git G1 structural consumer     COMPLETE / delivery evidence pending
PY2-01 flow chart              SPEC-only / Flowchart Lab pending
Content Pack 1.0 approved      NOT YET
Ready for classroom            NOT YET
```

Il curriculum annuale è congelato, ma **freeze curricolare, Content Pack approvato e classroom-ready sono gate distinti**.

## Entrypoint

- studente: [`student/README.md`](student/README.md)
- docente: [`teacher/README.md`](teacher/README.md)
- curriculum freeze: [`doc/CURRICULUM_FREEZE_2026_2027.md`](doc/CURRICULUM_FREEZE_2026_2027.md)
- stato progetto: [`doc/PROJECT_STATUS.md`](doc/PROJECT_STATUS.md)
- mappa moduli: [`tracks/secondo/MODULE_MAP.md`](tracks/secondo/MODULE_MAP.md)
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

M04–M30 hanno lesson canonica, deck Marp e runbook docente. PY2-01 resta volutamente SPEC-only finché il Flowchart Lab non è certificato; carta/lavagna/pseudocodice/trace restano fallback valido.

## Git G1

Git è un curriculum separato. Python seconda consuma soltanto il sottoinsieme G1 necessario al workflow:

```text
M14–M16
  status / diff — guided

Checkpoint A
  status → diff → test → add → diff --staged → commit → status → log/show

secondo semestre
  checkpoint/recovery G1 — independent progressivo
```

Source of truth: `TheBitPoets/git`. La dipendenza corrente è registrata in `config/git-g1-consumer.json` e verificata da `tests/git_g1_consumer_contract.py`.

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

## Gate aperti

- managed Classroom Environment / Flowchart Lab;
- beginner REPL/editor workflow;
- P1 canary certification;
- private GitHub Actions pre-runner blocker;
- P2/P3/P4;
- `romeo-sim` cross-profile;
- build/QA degli artifact slide;
- teacher review, provenance/coverage finale;
- Content Pack approval;
- rehearsal reale TheBitLab.

Vedi [`doc/PROJECT_STATUS.md`](doc/PROJECT_STATUS.md) per il checkpoint operativo aggiornato.

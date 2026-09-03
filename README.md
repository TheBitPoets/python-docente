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
PY2-01 flow chart              DRAFT / managed launcher technical PASS
P1/P2/P3/P4 grading            SOFTWARE/CONSUMER PASS
M04 docker-light               PASS amd64/arm64
M04 vm-gui + human rehearsal   READY TO RUN / PHYSICAL PASS PENDING
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
- rehearsal M04 reale: [`teacher/M04_CLASSROOM_REHEARSAL.md`](teacher/M04_CLASSROOM_REHEARSAL.md)
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

PY2-01 M00–M03 è materializzato come draft. Il launcher gestito Flowchart Lab è
tecnicamente verde su Ubuntu, Windows e macOS, ma resta
`candidate-not-certified`; carta/lavagna/pseudocodice/trace restano fallback
valido fino al rehearsal dei profili classroom e alla review umana.

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

Oggi il corso Python materializza esattamente quattro canarini deliberati: M04/P1,
M13/P2, M26/P4 e M28/P3. Questo non autorizza la produzione massiva delle
Activity.

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

I 27 deck Marp M04–M30 sono source canonici. La build reale HTML/PDF/PPTX e la
QA ingegneristica sono verdi; la review umana PowerPoint resta aperta. La
pipeline artifact è:

```text
Markdown
→ source QA
→ renderer pinned
→ HTML / PDF / PPTX
→ artifact QA
→ visual review
→ teacher sign-off
```

Non confondere la build/QA ingegneristica con il sign-off visuale umano.

## Gate aperti

- M04 `vm-gui` sui due profili rilasciati e real-school/human evidence;
- Flowchart Lab sui profili classroom e review umana;
- beginner REPL/editor workflow umano;
- accesso diretto GHCR cross-repository per `python-docente`;
- review PowerPoint umana;
- teacher sign-off;
- provenance/coverage final review;
- real TheBitLab rehearsal;
- Content Pack approval.

Vedi [`doc/PROJECT_STATUS.md`](doc/PROJECT_STATUS.md) per il checkpoint operativo aggiornato.

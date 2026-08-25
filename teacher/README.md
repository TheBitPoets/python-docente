# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / produzione editoriale controllata**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

## Architettura del corso

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md) — baseline congelata e change-control.
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md) — audit delle 33 settimane.
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md) — struttura di seconda.
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md) — prove e checkpoint.
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md) — P0/P1/P2/P3/P4.
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md) — Course Workspace ↔ dashboard ↔ Git.

## Moduli editoriali materializzati

### PY2-02 — primi programmi

- M04: [lesson](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · [runbook](M04_RUNBOOK.md) · Activity canarino `py2-activity-b-input-somma-001`.
- M05: [lesson](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [runbook](M05_RUNBOOK.md).

### PY2-03 — selezione e logica

- M06: [lesson](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md) · [runbook](M06_RUNBOOK.md).
- M07: [lesson](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [runbook](M07_RUNBOOK.md).
- M08: [lesson](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [runbook](M08_RUNBOOK.md).

### PY2-04 — iterazione e pattern — **editorialmente completa**

- M09: [lesson](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [runbook](M09_RUNBOOK.md).
- M10: [lesson](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md) · [runbook](M10_RUNBOOK.md).
- M11: [lesson](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [runbook](M11_RUNBOOK.md).
- M12: [lesson](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [runbook](M12_RUNBOOK.md).

M11 introduce invarianti intuitivi (`totale`, `conteggio`, `minimo`, `trovato`). M12 introduce `R × C` come quantità di lavoro osservabile senza Big-O formale.

### PY2-05 — funzioni, decomposizione e testing — **editorialmente completa**

#### M13 — funzioni, parametri, argomenti e `return`
- [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md)
- [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md)
- [runbook](M13_RUNBOOK.md)

Focus: definizione/chiamata, parametro/argomento, `return` vs `print`, predicate, call trace e primo bisogno reale di P2.

#### M14 — scope locale, passaggio dati e composizione
- [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md)
- [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md)
- [runbook](M14_RUNBOOK.md)

Focus: dipendenze esplicite, evitare stato globale nascosto, composizione, call graph e primo uso didattico di `git status`/`git diff`.

#### M15 — progettazione top-down e responsabilità
- [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md)
- [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md)
- [runbook](M15_RUNBOOK.md)

Focus: specifica → responsabilità → firme → contratti intuitivi → casi → implementazione; separazione I/O/logica/output; pre/post-condizioni beginner.

#### M16 — `assert`, regression test, debug e refactoring
- [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md)
- [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md)
- [runbook](M16_RUNBOOK.md)

Focus:

```text
contratto → casi → assert → diagnosi → fix → regression → refactor
```

M16 prepara il Checkpoint A e il primo checkpoint Git guidato.

## Policy Activity

Solo M04 materializza una nuova Activity P1. M05–M16 contengono Activity candidate/esercizi, ma non aggiungono Activity autogradate finché il profilo richiesto non è certificato.

Per PY2-05 il profilo corretto è P2 (`2cornot2c#756`): testare direttamente funzione + argomenti + return/exception, senza deformare l'esercizio in stdin/stdout.

Romeo non viene duplicato dentro questo repo: le missioni restano nel repository Romeo e vengono referenziate/adattate solo dopo certificazione `romeo-sim`.

## Git G1 — punto di ingresso attuale

Da M14 il workflow Python usa progressivamente:

```text
git status
git diff
```

Al Checkpoint A aggiungeremo:

```text
git add
git commit
git log essenziale
```

Il curriculum Git resta separato. **Ora è il momento corretto per auditare le dispense Git esistenti del docente** prima di produrre il micro-modulo G1 definitivo e, in seguito, il corso Git autonomo.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è il Course Workspace mutabile; Git conserva storia/review; il futuro Course Bundle è release immutabile. L'UX bulk “Aggiungi intero modulo/file” è tracciata in `2cornot2c#755`.

`scripts/sync_authoring_catalog.py` deriva le lesson materializzate dai `content_items` del Content Pack e controlla/sincronizza la source `python-course-content` nel Content Pack e nel Course Design.

## Ambiente TheBitLab

- Classroom Environment unico scuola/casa;
- Python baseline iniziale 3.12-compatible;
- REPL prima di VS Code;
- VS Code solo managed;
- Flowchart Lab target cross-platform;
- Romeo tramite `romeo-sim`;
- grading autorevole separato dall'ambiente interattivo.

Blocker principali:

- `2cornot2c#753/#754` — Classroom Environment + Flowchart Lab;
- `2cornot2c#755` — Open course/workspace UX;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior;
- `python-docente#7` — P1 consumer;
- `python-docente#8` — Actions private-repo pre-execution.

## QA authoring

`tests/course_authoring_catalog.py` controlla tutti i moduli materializzati: lesson, Marp deck, runbook, navigazione, provenance, Course Board source e Activity dichiarate. Il workflow esegue anche `scripts/sync_authoring_catalog.py` in modalità check.

## Diagnosi CI #8

Un job con soltanto `runs-on` + `echo`, senza action esterne, fallisce pre-step su Ubuntu/Windows. Il private repo TPSI4 aveva CI verde il 19 agosto e lo stesso problema dal 21: quota/budget Actions dei repository privati è l'ipotesi principale, da verificare nelle impostazioni organizzazione. Non indebolire lo YAML per nascondere il problema.

## Criterio di produzione

Continuiamo un modulo alla volta:

```text
lesson
+ slide
+ runbook
+ Content Pack/Course Board
+ navigation
+ QA
```

Nuove Activity autogradate soltanto quando il relativo profilo è certificato.

Prossimi passi editoriali: Checkpoint A/Git G1, poi PY2-06 stringhe (M17–M19).

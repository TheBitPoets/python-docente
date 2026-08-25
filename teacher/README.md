# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / produzione editoriale controllata**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

Questo indice è il punto di ingresso del docente per progettazione, conduzione e delivery.

## Architettura del corso

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md) — baseline congelata e change-control.
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md) — audit delle 33 settimane.
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md) — struttura di seconda.
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md) — prove e checkpoint.
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md) — P0/P1/P2/P3/P4.
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md) — Course Workspace ↔ dashboard ↔ Git.

## Moduli editoriali materializzati

### M04 — Interprete, REPL, valori e I/O
- lesson: [`04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md)
- slide: [`04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md)
- runbook: [`M04_RUNBOOK.md`](M04_RUNBOOK.md)
- Activity canarino: `py2-activity-b-input-somma-001`

### M05 — Espressioni, operatori e prime funzioni
- lesson: [`05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- slide: [`05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- runbook: [`M05_RUNBOOK.md`](M05_RUNBOOK.md)

### M06 — Booleani, confronti e `if`
- lesson: [`06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md)
- slide: [`06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md)
- runbook: [`M06_RUNBOOK.md`](M06_RUNBOOK.md)

### M07 — `elif`, casi esclusivi e logica composta
- lesson: [`07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- slide: [`07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- runbook: [`M07_RUNBOOK.md`](M07_RUNBOOK.md)

### M08 — Annidamento, validazione e refactoring
- lesson: [`08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- slide: [`08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- runbook: [`M08_RUNBOOK.md`](M08_RUNBOOK.md)

M06–M08 materializzano tutta PY2-03: soglie/confronti → scelta della struttura (`elif` vs `if` indipendenti) → logica composta → annidamento/validazione/refactoring.

### M09 — `while`, stato, sentinelle e validazione ripetuta
- lesson: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- slide: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- runbook: [`M09_RUNBOOK.md`](M09_RUNBOOK.md)

Nucleo M09:

```text
stato iniziale
→ condizione di continuazione
→ corpo
→ aggiornamento
→ terminazione spiegabile
```

La validazione M08 diventa ora ripetibile con `while`. Sentinelle, zero/una/più iterazioni, aggiornamento su tutti i path e debug dei cicli infiniti sono core. `while True` + `break` è solo variante dopo il modello esplicito.

Romeo può usare il riferimento pinned `romeo-y1-u16-ciclo-while` come applicazione opzionale, soltanto con `romeo-sim` certificato.

## Policy Activity durante questa fase

Solo M04 materializza una nuova Activity P1. M05–M09 contengono Activity candidate/esercizi, ma non aggiungono Activity autogradate fino a quando `python-docente#7` non certifica il canarino.

Romeo non viene duplicato dentro questo repo: missioni/scenari restano nel repository Romeo e vengono usati solo attraverso riferimenti/adattamenti approvati.

## Change-control

Dopo il freeze, lesson, slide, Activity, rubric, tooling, runner e UX sono delivery changes finché non cambiano outcome obbligatori, prerequisiti core, ordine necessario, ore core sostanziali, OOP obbligatoria o ruolo curricolare di Git/Container/Romeo.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è il Course Workspace mutabile; Git conserva storia/review; il futuro Course Bundle è release immutabile. L'UX bulk “Aggiungi intero modulo/file” è tracciata in `2cornot2c#755`.

## Ambiente TheBitLab

- Classroom Environment unico per scuola/casa;
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

`tests/course_authoring_catalog.py` controlla tutti i moduli materializzati: lesson, Marp deck, runbook, navigazione, provenance, Course Board source e Activity dichiarate.

M04 conserva i gate tecnici specifici; M05 conserva un controllo pedagogico dedicato. L'assenza di runner Actions non equivale a PASS/FAIL del contenuto.

## Diagnosi CI #8

Un job con soltanto `runs-on` + `echo`, senza action esterne, fallisce pre-step su Ubuntu/Windows. Il private repo TPSI4 aveva CI verde il 19 agosto e lo stesso problema dal 21: quota/budget Actions dei repository privati è l'ipotesi principale, da verificare nelle impostazioni organizzazione. Non indebolire lo YAML per nascondere il problema.

## Git e Container

Git e Container restano curricula separati. Git G1 entra progressivamente in Python; le dispense Git verranno richieste quando si produrrà G1 definitivo o il corso Git autonomo. Container/Docker resta nel backlog separato `docker101#1`.

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

Nuove Activity autogradate soltanto quando il relativo profilo è certificato. Il prossimo modulo è M10 (`for`, `range`, scelta `for` vs `while`).

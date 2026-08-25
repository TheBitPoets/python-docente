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

`CURRICULUM_FREEZE_2026_2027.md` è il documento curricolare autorevole.

## Moduli editoriali materializzati

### M04 — Interprete, REPL, script, valori e input/output

- lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md)
- slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md)
- runbook: [`M04_RUNBOOK.md`](M04_RUNBOOK.md)
- Activity canarino: `py2-activity-b-input-somma-001`
- certificazione: `python-docente#7`
- blocker CI privati: `python-docente#8`

M04 resta il **golden vertical slice tecnico**.

### M05 — Espressioni, operatori e prime funzioni

- lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- runbook: [`M05_RUNBOOK.md`](M05_RUNBOOK.md)

Focus: espressioni, `/ // %`, precedenza, f-string/built-in essenziali, prima funzione pura e preview `return` vs `print`.

### M06 — Booleani, confronti e prima selezione con `if`

- lesson: [`content/python/06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md)
- slide: [`slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md)
- runbook: [`M06_RUNBOOK.md`](M06_RUNBOOK.md)

Focus: soglie → confronto → `bool` → `if/else` → indentazione → trace → test sotto/sulla/sopra confine. Romeo soltanto applicazione opzionale tramite missione pinned `romeo-y1-u14-condizioni` quando il runtime è certificato.

### M07 — `elif`, casi esclusivi e condizioni composte

- lesson: [`content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- slide: [`slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- runbook: [`M07_RUNBOOK.md`](M07_RUNBOOK.md)

Nucleo:

```text
un solo risultato → if/elif/else
più effetti possibili → if indipendenti
and/or/not → compongono condizioni
```

Short-circuit è solo intuizione controllata; chained comparisons arrivano dopo la forma logica con `and`.

### M08 — Annidamento, validazione e refactoring

- lesson: [`content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- slide: [`slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- runbook: [`M08_RUNBOOK.md`](M08_RUNBOOK.md)

Nucleo:

```text
dipendenza reale tra decisioni
→ annidamento/path trace
→ validazione prima della classificazione
→ refactoring protetto dagli stessi test
```

M08 **non** introduce ancora `while` per ripetere input e non introduce `try/except`: distingue deliberatamente valore fuori dominio da conversione fallita.

## Policy Activity durante questa fase

Solo M04 materializza una nuova Activity P1. M05–M08 contengono Activity candidate ed esercizi pratici, ma non aggiungono nuove Activity autogradate fino a quando `python-docente#7` non dà evidenza sul canarino P1.

Romeo non viene duplicato dentro questo repo: le missioni restano nel repo Romeo e vengono referenziate/adattate soltanto dopo certificazione `romeo-sim`.

## Change-control

Dopo il freeze, modifiche a lesson, slide, Activity, rubric, tooling, runner e UX sono **delivery changes** finché non cambiano outcome obbligatori, prerequisiti core, ordine necessario, ore core sostanziali, OOP obbligatoria o ruolo di Git/Container/Romeo.

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

`tests/course_authoring_catalog.py` controlla in modo scalabile i moduli materializzati: lesson, Marp deck, runbook, navigazione, provenance, Course Board source e Activity dichiarate.

M04 conserva i gate tecnici specifici; M05 conserva un controllo pedagogico dedicato. La CI non ha ancora evidenza perché i runner privati falliscono prima degli step; `steps: null` non è un PASS/FAIL dei test.

## Diagnosi CI #8

Un job diagnostico composto solo da `runs-on` + `echo`, senza action esterne, fallisce pre-step su Ubuntu e Windows. Inoltre il private repo TPSI4 aveva CI verde il 19 agosto e lo stesso failure dal 21. La causa più probabile è quota/budget Actions dei repository privati, da verificare nelle impostazioni Billing/Actions dell'organizzazione; non va “corretta” indebolendo lo YAML.

## Git e Container

Git e Container restano curricula separati. Git G1 entra progressivamente in Python; le dispense Git verranno richieste quando si produrrà G1 definitivo o il corso Git autonomo. Container/Docker resta nel backlog separato `docker101#1`.

## Criterio di produzione

Possiamo continuare **modulo per modulo**:

```text
lesson
+ slide
+ runbook
+ Content Pack/Course Board
+ navigation
+ QA
```

Nuove Activity autogradate soltanto quando il relativo profilo di grading è certificato.

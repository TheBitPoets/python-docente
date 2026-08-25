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

### PY2-02 — primi programmi

- M04: [`04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · [runbook](M04_RUNBOOK.md) · Activity canarino `py2-activity-b-input-somma-001`.
- M05: [`05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [runbook](M05_RUNBOOK.md).

### PY2-03 — selezione e logica

- M06: [`06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md) · [runbook](M06_RUNBOOK.md).
- M07: [`07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [runbook](M07_RUNBOOK.md).
- M08: [`08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [runbook](M08_RUNBOOK.md).

M06–M08 coprono soglie/confronti → `elif` vs `if` indipendenti → `and/or/not` → annidamento/validazione/refactoring.

### PY2-04 — iterazione e pattern

#### M09 — `while`, stato, sentinelle e validazione ripetuta

- lesson: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- slide: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- runbook: [`M09_RUNBOOK.md`](M09_RUNBOOK.md)

Nucleo: stato iniziale → condizione → corpo → aggiornamento → terminazione spiegabile. Validazione ripetuta e sentinella sono core; `while True` + `break` è variante successiva.

#### M10 — `for`, `range` e scelta `for` vs `while`

- lesson: [`10_FOR_RANGE_SCELTA_CICLO.md`](../content/python/10_FOR_RANGE_SCELTA_CICLO.md)
- slide: [`10_FOR_RANGE_SCELTA_CICLO.md`](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md)
- runbook: [`M10_RUNBOOK.md`](M10_RUNBOOK.md)

Nucleo:

```text
range → start incluso / stop escluso / step
for   → percorso o numero di iterazioni noto
while → durata dipendente dallo stato
```

Off-by-one, range vuoto, step negativo, refactoring `while`→`for`, stato ridondante e uso disciplinato di `break`/`continue` sono competenze esplicite. Romeo `y1-u15-ciclo-for` resta applicazione opzionale con simulatore certificato.

## Policy Activity

Solo M04 materializza una nuova Activity P1. M05–M10 contengono Activity candidate/esercizi, ma non aggiungono Activity autogradate finché `python-docente#7` non certifica il canarino.

Romeo non viene duplicato dentro questo repo: le missioni restano nel repository Romeo e vengono referenziate/adattate solo dopo certificazione `romeo-sim`.

## Change-control

Dopo il freeze, lesson, slide, Activity, rubric, tooling, runner e UX sono delivery changes finché non cambiano outcome obbligatori, prerequisiti core, ordine necessario, ore core sostanziali, OOP obbligatoria o ruolo curricolare di Git/Container/Romeo.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è il Course Workspace mutabile; Git conserva storia/review; il futuro Course Bundle è release immutabile. L'UX bulk “Aggiungi intero modulo/file” è tracciata in `2cornot2c#755`.

`scripts/sync_authoring_catalog.py` deriva la lista delle lesson materializzate dai `content_items` del Content Pack e può sincronizzare la source `python-course-content` nel Content Pack e nel Course Design (`--write`); senza `--write` è un check fail-closed.

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

`tests/course_authoring_catalog.py` controlla tutti i moduli materializzati: lesson, Marp deck, runbook, navigazione, provenance, Course Board source e Activity dichiarate. Il workflow esegue anche `scripts/sync_authoring_catalog.py` in modalità check.

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

Nuove Activity autogradate soltanto quando il relativo profilo è certificato. Il prossimo modulo è M11: contatori, accumulatori, minimo/massimo progressivo, ricerca e flag.

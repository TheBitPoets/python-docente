# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / produzione editoriale controllata**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

## Architettura del corso

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md)
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md)
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md)
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md)
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md)
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md)

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

### PY2-05 — funzioni, decomposizione e testing — **editorialmente completa**
- M13: [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md) · [runbook](M13_RUNBOOK.md).
- M14: [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [runbook](M14_RUNBOOK.md).
- M15: [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [runbook](M15_RUNBOOK.md).
- M16: [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [runbook](M16_RUNBOOK.md).

#### Checkpoint A
- [Guida studente](../student/CHECKPOINT_A.md)
- [Runbook docente](CHECKPOINT_A_RUNBOOK.md)

Consolida la prova pratica V2 e introduce il primo workflow Git G1 guidato `status → diff → test → add → commit → log`. La parte Git resta draft fino all'audit delle dispense docente.

### PY2-06 — stringhe — **editorialmente completa**
- M17: [lesson](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [runbook](M17_RUNBOOK.md).
- M18: [lesson](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [runbook](M18_RUNBOOK.md).
- M19: [lesson](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [runbook](M19_RUNBOOK.md).

M17–M19 trattano `str` come sequenza immutabile, indici/slicing, membership/metodi, normalizzazione, algoritmi su testo e `split()` come ponte esplicito verso le liste. Nessun residuo Python 2 di `friedpython` viene importato automaticamente.

## Policy Activity

Solo M04 materializza una nuova Activity P1. M05–M19 contengono Activity candidate/esercizi, ma non aggiungono Activity autogradate finché il profilo richiesto non è certificato.

Per funzioni/stringhe pure il profilo corretto è P2 (`2cornot2c#756`): funzione + argomenti eseguiti nel sandbox, actual return/exception restituito al trusted host, expected mantenuto host-side.

## Git G1 — audit dispense ora necessario

Da M14 il workflow Python usa progressivamente `git status` e `git diff`; al Checkpoint A entrano `add`, `commit` e `log`.

`tracks/secondo/GIT_G1_INTEGRATION.md` registra che il trigger per l'audit delle dispense docente è raggiunto. Le dispense vanno ora classificate G1/G2/G3/G4; Python seconda consumerà solo G1 e il futuro corso Git resterà canonico.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è Course Workspace mutabile; Git conserva storia/review; Course Bundle è release immutabile. `2cornot2c#755` traccia Open Course e bulk whole-module insertion.

`scripts/sync_authoring_catalog.py` deriva le lesson materializzate dai `content_items` e controlla/sincronizza la source `python-course-content` in Content Pack/Course Design.

## Ambiente TheBitLab

- Classroom Environment unico scuola/casa;
- Python baseline 3.12-compatible;
- REPL prima di VS Code;
- VS Code solo managed;
- Flowchart Lab target cross-platform;
- Romeo tramite `romeo-sim`;
- grading autorevole separato dall'ambiente interattivo.

Blocker: `#753/#754` ambiente/Flowchart, `#755` Course Workspace UX, `#756` P2, `#757` P4, `#758` P3, `python-docente#7` P1 canary, `python-docente#8` Actions private-repo.

## QA authoring

`tests/course_authoring_catalog.py` controlla tutti i moduli materializzati; il workflow esegue anche `scripts/sync_authoring_catalog.py` in check mode. M04 mantiene i gate tecnici specifici.

## Diagnosi CI #8

Un job con solo `runs-on` + `echo` fallisce pre-step su Ubuntu/Windows. TPSI4 privato aveva CI verde il 19 agosto e lo stesso problema dal 21: quota/budget Actions privati è l'ipotesi principale, con policy hosted-runner come alternativa. Non indebolire lo YAML.

## Criterio di produzione

Continuiamo un modulo alla volta:

```text
lesson + slide + runbook + Content Pack/Course Board + navigation + QA
```

Nuove Activity autogradate soltanto quando il relativo profilo è certificato.

Prossimo blocco: **PY2-07 — liste, tuple e dati tabellari (M20–M22)**.

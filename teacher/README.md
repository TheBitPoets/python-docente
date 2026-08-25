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

### PY2-02
M04–M05: primi programmi, REPL, I/O, operatori e prima preview di funzione.

### PY2-03
M06–M08: selezione, logica, annidamento, validazione e refactoring.

### PY2-04 — **completa**
- M09 [lesson](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [runbook](M09_RUNBOOK.md)
- M10 [lesson](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [runbook](M10_RUNBOOK.md)
- M11 [lesson](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [runbook](M11_RUNBOOK.md)
- M12 [lesson](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [runbook](M12_RUNBOOK.md)

### PY2-05 — **completa**
- M13 [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [runbook](M13_RUNBOOK.md)
- M14 [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [runbook](M14_RUNBOOK.md)
- M15 [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [runbook](M15_RUNBOOK.md)
- M16 [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [runbook](M16_RUNBOOK.md)

#### Checkpoint A
- [Guida studente](../student/CHECKPOINT_A.md)
- [Runbook](CHECKPOINT_A_RUNBOOK.md)

Consolida V2 pratica e introduce Git G1 `status → diff → test → add → commit → log`. Il trigger per auditare le dispense Git è raggiunto.

### PY2-06 — stringhe — **completa**
- M17 [lesson](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [runbook](M17_RUNBOOK.md)
- M18 [lesson](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [runbook](M18_RUNBOOK.md)
- M19 [lesson](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [runbook](M19_RUNBOOK.md)

### PY2-07 — liste, tuple e dati tabellari — **completa**

#### M20 — liste, mutabilità e metodi
- [lesson](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md)
- [slide](../slides/python/modules/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md)
- [runbook](M20_RUNBOOK.md)

Focus: `str` immutabile vs `list` mutabile, metodi essenziali, `append/extend`, `remove/pop`, metodi mutanti che restituiscono `None`, iterazione diretta/indice/`enumerate`.

#### M21 — alias, copie, filtri e ordinamento
- [lesson](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md)
- [slide](../slides/python/modules/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md)
- [runbook](M21_RUNBOOK.md)

Focus: due nomi→un oggetto, shallow copy, contratto di mutazione, evitare remove durante iterazione, `sort()` vs `sorted()`, filtraggio/trasformazione con loop esplicito.

#### M22 — tuple, unpacking e matrici
- [lesson](../content/python/22_TUPLE_UNPACKING_MATRICI.md)
- [slide](../slides/python/modules/22_TUPLE_UNPACKING_MATRICI.md)
- [runbook](M22_RUNBOOK.md)

Focus: list vs tuple per modello dati, packing/unpacking, liste annidate, attraversamento matrici e row aliasing. Debug obbligatorio di `[[0] * C] * R`.

#### Checkpoint B
- [Guida studente](../student/CHECKPOINT_B.md)
- [Runbook](CHECKPOINT_B_RUNBOOK.md)

Consolida stringhe/liste/tuple e prepara V3 prima di set/dict.

## Audit `friedpython`

- mapping generale: [`sources/FRIEDPYTHON_MAPPING.md`](../sources/FRIEDPYTHON_MAPPING.md)
- audit liste/tuple: [`sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`](../sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md)

Risultati importanti:

- esercizi liste 1–2: buoni spunti M20;
- 3–5: candidati M21 dopo riscrittura;
- esercizio 6 ASCII frequenze: non core liste, rinviato a M24 come confronto data-model;
- tuple legacy contiene anche sintassi Python 2, quindi nessuna copia diretta;
- comprehension solo enrichment dopo loop equivalente.

Il source audit è esposto alla Course Board separatamente dal contenuto canonico.

## Policy Activity

Solo M04 materializza una nuova Activity P1. M05–M22 contengono esercizi/Activity candidate, ma non nuove Activity autogradate finché il profilo richiesto non è certificato.

Per funzioni pure il profilo corretto è P2 (`2cornot2c#756`).

## Git G1

Da M14 usiamo `status/diff`; Checkpoint A aggiunge `add/commit/log`. Le dispense Git del docente **servono ora** per produrre il materiale G1 canonico e poi alimentare il corso Git autonomo, senza duplicazione dentro Python.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è Course Workspace mutabile; Git conserva storia/review; Course Bundle è release immutabile. `2cornot2c#755` traccia Open Course e bulk whole-module insertion.

`scripts/sync_authoring_catalog.py` controlla/sincronizza la source `python-course-content`; `tests/course_authoring_catalog.py` verifica lesson, deck, runbook, navigazione, provenance e Activity dichiarate.

## Ambiente TheBitLab / blocker

- `2cornot2c#753/#754` — Classroom Environment + Flowchart Lab
- `2cornot2c#755` — Course Workspace UX
- `2cornot2c#756` — P2
- `2cornot2c#757` — P4
- `2cornot2c#758` — P3
- `python-docente#7` — P1 canary
- `python-docente#8` — Actions private-repo pre-execution

Non deformare gli outcome per adattarli a un grader non certificato.

## Criterio di produzione

Continuiamo un modulo alla volta:

```text
lesson + slide + runbook + Content Pack/Course Board + navigation + QA
```

Prossimo blocco: **PY2-08 — set, dizionari e modellazione dei dati (M23–M25)**.

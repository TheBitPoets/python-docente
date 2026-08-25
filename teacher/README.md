# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / core M04–M30 materializzato editorialmente**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

## Documenti autorevoli

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md)
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md)
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md)
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md)
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md)
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md)

## Stato editoriale annuale

### PY2-01 — problem solving / flow chart

**SPEC-only**. Non materializziamo la delivery digitale definitiva finché Flowchart Lab non è certificato. Carta/lavagna/pseudocodice/trace restano fallback valido.

### PY2-02 — completa editorialmente
- M04 [lesson](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · [runbook](M04_RUNBOOK.md)
- M05 [lesson](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [runbook](M05_RUNBOOK.md)

M04 resta il golden vertical slice tecnico con Activity P1 `py2-activity-b-input-somma-001`.

### PY2-03 — completa editorialmente
- M06 [lesson](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [runbook](M06_RUNBOOK.md)
- M07 [lesson](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [runbook](M07_RUNBOOK.md)
- M08 [lesson](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [runbook](M08_RUNBOOK.md)

### PY2-04 — completa editorialmente
- M09 [lesson](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [runbook](M09_RUNBOOK.md)
- M10 [lesson](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [runbook](M10_RUNBOOK.md)
- M11 [lesson](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [runbook](M11_RUNBOOK.md)
- M12 [lesson](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [runbook](M12_RUNBOOK.md)

### PY2-05 — completa editorialmente
- M13 [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [runbook](M13_RUNBOOK.md)
- M14 [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [runbook](M14_RUNBOOK.md)
- M15 [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [runbook](M15_RUNBOOK.md)
- M16 [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [runbook](M16_RUNBOOK.md)

#### Checkpoint A
- [Guida studente](../student/CHECKPOINT_A.md)
- [Runbook](CHECKPOINT_A_RUNBOOK.md)

Git G1 entra qui: `status → diff → test → add → commit → log`.

### PY2-06 — completa editorialmente
- M17 [lesson](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [runbook](M17_RUNBOOK.md)
- M18 [lesson](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [runbook](M18_RUNBOOK.md)
- M19 [lesson](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [runbook](M19_RUNBOOK.md)

### PY2-07 — completa editorialmente
- M20 [lesson](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [runbook](M20_RUNBOOK.md)
- M21 [lesson](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [runbook](M21_RUNBOOK.md)
- M22 [lesson](../content/python/22_TUPLE_UNPACKING_MATRICI.md) · [runbook](M22_RUNBOOK.md)

#### Checkpoint B
- [Guida studente](../student/CHECKPOINT_B.md)
- [Runbook](CHECKPOINT_B_RUNBOOK.md)

### PY2-08 — completa editorialmente
- M23 [lesson](../content/python/23_SET_UNICITA_MEMBERSHIP.md) · [slide](../slides/python/modules/23_SET_UNICITA_MEMBERSHIP.md) · [runbook](M23_RUNBOOK.md)
- M24 [lesson](../content/python/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [slide](../slides/python/modules/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [runbook](M24_RUNBOOK.md)
- M25 [lesson](../content/python/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [slide](../slides/python/modules/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [runbook](M25_RUNBOOK.md)

Focus: scegliere il modello dai requisiti e dalle operazioni dominanti, non dal “livello” percepito della struttura.

### PY2-09 — completa editorialmente
- M26 [lesson](../content/python/26_FILE_TESTO_PATHLIB_ERRORI.md) · [slide](../slides/python/modules/26_FILE_TESTO_PATHLIB_ERRORI.md) · [runbook](M26_RUNBOOK.md)

Il core resta volutamente piccolo per proteggere l'OOP: file testo UTF-8, `with`, `pathlib`, errori prevedibili; CSV/JSON/binario come extension.

### PY2-10 — completa editorialmente
- M27 [lesson](../content/python/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [slide](../slides/python/modules/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [runbook](M27_RUNBOOK.md)
- M28 [lesson](../content/python/28_METODI_STATO_INVARIANTI.md) · [slide](../slides/python/modules/28_METODI_STATO_INVARIANTI.md) · [runbook](M28_RUNBOOK.md)
- M29 [lesson](../content/python/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [slide](../slides/python/modules/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [runbook](M29_RUNBOOK.md)
- M30 [lesson](../content/python/30_CAPSTONE_OOP.md) · [slide](../slides/python/modules/30_CAPSTONE_OOP.md) · [runbook](M30_RUNBOOK.md)

#### Checkpoint C — settimana 33
- [Guida studente](../student/CHECKPOINT_C.md)
- [Runbook](CHECKPOINT_C_RUNBOOK.md)

Nessun nuovo prerequisito: finalizzazione, recupero, evidence ed enrichment.

## Audit `friedpython`

- mapping generale: [`sources/FRIEDPYTHON_MAPPING.md`](../sources/FRIEDPYTHON_MAPPING.md)
- audit liste/tuple: [`sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`](../sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md)

Ogni riuso richiede audit individuale e riscrittura/modernizzazione; niente import wholesale.

## Policy Activity / grading

Solo M04 materializza per ora una nuova Activity P1. Gli altri moduli contengono esercizi e Activity candidate, ma una Activity autogradata viene materializzata solo quando il profilo necessario è certificato.

- P0 — manuale/trace/design;
- P1 — stdin/stdout;
- P2 — funzioni (`2cornot2c#756`);
- P3 — oggetti (`2cornot2c#758`);
- P4 — filesystem (`2cornot2c#757`);
- `romeo-sim` — dominio robotico simulato.

Non deformare gli outcome per adattarli a un grader non certificato.

## Git G1

Da M14 usiamo `status/diff`; Checkpoint A aggiunge `add/commit/log`. Le dispense Git del docente **servono ora** per produrre il materiale G1 canonico e alimentare il corso Git autonomo, senza duplicazione dentro Python.

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
- `romeo-sim` — cross-profile certification ancora aperta

## Criterio di produzione da qui in avanti

Il core M04–M30 esiste. Da questo punto il lavoro passa da **authoring primario** a:

```text
audit editoriale
→ QA e build slide
→ Activity planning/materialization per profilo
→ Course Board round-trip
→ TheBitLab certification
→ teacher review
→ Content Pack approval
```

PY2-01 resta l'unico blocco core senza lesson finali, in attesa della decisione/implementazione Flowchart Lab.

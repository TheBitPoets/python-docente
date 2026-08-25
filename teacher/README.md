# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / core M04–M30 materializzato + semanticamente revisionato**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

## Documenti autorevoli

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md)
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md)
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md)
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md)
5. [`doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md`](../doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md)
6. [`doc/COVERAGE.md`](../doc/COVERAGE.md) e [`config/curriculum-coverage.json`](../config/curriculum-coverage.json)
7. [`tracks/secondo/GIT_G1_INTEGRATION.md`](../tracks/secondo/GIT_G1_INTEGRATION.md) e [`config/git-g1-consumer.json`](../config/git-g1-consumer.json)
8. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md)
9. [`doc/SLIDE_ARTIFACT_PIPELINE.md`](../doc/SLIDE_ARTIFACT_PIPELINE.md)
10. [`TEACHER_SIGNOFF_CHECKLIST.md`](TEACHER_SIGNOFF_CHECKLIST.md)
11. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md)

## Regola di delivery dopo la semantic review

Il materiale può essere più ricco del mastery settimanale. Nei runbook il boundary didattico è:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

Una verifica high-stakes non deve assumere automaticamente dettagli guided/enrichment non realmente consolidati nella classe.

## Stato editoriale annuale

### PY2-01 — problem solving / flow chart

**SPEC-only**. Non materializziamo la delivery digitale definitiva finché Flowchart Lab non è certificato. Carta/lavagna/pseudocodice/trace restano fallback valido.

### PY2-02 — completa editorialmente e revisionata
- M04 [lesson](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · [runbook](M04_RUNBOOK.md)
- M05 [lesson](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [runbook](M05_RUNBOOK.md)

M04 resta il golden vertical slice tecnico con Activity P1 `py2-activity-b-input-somma-001`.

### PY2-03 — completa editorialmente e revisionata
- M06 [lesson](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md) · [runbook](M06_RUNBOOK.md)
- M07 [lesson](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [runbook](M07_RUNBOOK.md)
- M08 [lesson](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [runbook](M08_RUNBOOK.md)

### PY2-04 — completa editorialmente e revisionata
- M09 [lesson](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [runbook](M09_RUNBOOK.md)
- M10 [lesson](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md) · [runbook](M10_RUNBOOK.md)
- M11 [lesson](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [runbook](M11_RUNBOOK.md)
- M12 [lesson](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [runbook](M12_RUNBOOK.md)

### PY2-05 — completa editorialmente e revisionata
- M13 [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md) · [runbook](M13_RUNBOOK.md)
- M14 [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [runbook](M14_RUNBOOK.md)
- M15 [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [runbook](M15_RUNBOOK.md)
- M16 [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [runbook](M16_RUNBOOK.md)

#### Checkpoint A
- [Guida studente](../student/CHECKPOINT_A.md)
- [Runbook](CHECKPOINT_A_RUNBOOK.md)

Git G1 entra progressivamente in PY2-05. M14–M16 consumano `G1.OBSERVE.STATUS` e `G1.OBSERVE.DIFF`; il Checkpoint A aggiunge staging, commit, history e modello HEAD tramite il corso Git canonico `TheBitPoets/git`, senza duplicare lesson e senza richiedere il completamento standalone G1.

### PY2-06 — completa editorialmente e revisionata
- M17 [lesson](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [runbook](M17_RUNBOOK.md)
- M18 [lesson](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [runbook](M18_RUNBOOK.md)
- M19 [lesson](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [runbook](M19_RUNBOOK.md)

### PY2-07 — completa editorialmente e revisionata
- M20 [lesson](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [slide](../slides/python/modules/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [runbook](M20_RUNBOOK.md)
- M21 [lesson](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [slide](../slides/python/modules/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [runbook](M21_RUNBOOK.md)
- M22 [lesson](../content/python/22_TUPLE_UNPACKING_MATRICI.md) · [slide](../slides/python/modules/22_TUPLE_UNPACKING_MATRICI.md) · [runbook](M22_RUNBOOK.md)

#### Checkpoint B
- [Guida studente](../student/CHECKPOINT_B.md)
- [Runbook](CHECKPOINT_B_RUNBOOK.md)

Checkpoint B misura scelta/modello/mutabilità, non cataloghi di API. Git riusa il workflow G1 completo senza nuovi outcome G2.

### PY2-08 — completa editorialmente e revisionata
- M23 [lesson](../content/python/23_SET_UNICITA_MEMBERSHIP.md) · [slide](../slides/python/modules/23_SET_UNICITA_MEMBERSHIP.md) · [runbook](M23_RUNBOOK.md)
- M24 [lesson](../content/python/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [slide](../slides/python/modules/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [runbook](M24_RUNBOOK.md)
- M25 [lesson](../content/python/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [slide](../slides/python/modules/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [runbook](M25_RUNBOOK.md)

Focus: scegliere il modello dai requisiti e dalle operazioni dominanti, non dal “livello” percepito o dalla quantità di nesting.

### PY2-09 — completa editorialmente e revisionata
- M26 [lesson](../content/python/26_FILE_TESTO_PATHLIB_ERRORI.md) · [slide](../slides/python/modules/26_FILE_TESTO_PATHLIB_ERRORI.md) · [runbook](M26_RUNBOOK.md)

Il core resta deliberatamente piccolo: 3 ore per `Path` relativo, UTF-8, read/write, `with`, righe, I/O separato e un errore esterno mirato. P4 è delivery teacher-side.

### PY2-10 — completa editorialmente e revisionata
- M27 [lesson](../content/python/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [slide](../slides/python/modules/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [runbook](M27_RUNBOOK.md)
- M28 [lesson](../content/python/28_METODI_STATO_INVARIANTI.md) · [slide](../slides/python/modules/28_METODI_STATO_INVARIANTI.md) · [runbook](M28_RUNBOOK.md)
- M29 [lesson](../content/python/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [slide](../slides/python/modules/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [runbook](M29_RUNBOOK.md)
- M30 [lesson](../content/python/30_CAPSTONE_OOP.md) · [slide](../slides/python/modules/30_CAPSTONE_OOP.md) · [runbook](M30_RUNBOOK.md)

Composizione è outcome core. Il capstone misura responsabilità, stato/invarianti, collaborazione, struttura dati, test/regression e spiegazione, non quantità di classi/framework.

#### Checkpoint C — settimana 33
- [Guida studente](../student/CHECKPOINT_C.md)
- [Runbook](CHECKPOINT_C_RUNBOOK.md)

Nessun nuovo prerequisito. Nel capstone completo la composizione è obbligatoria; nel recovery si riduce il dominio, non si cancella l'outcome.

## Coverage / provenance

- human-readable: [`doc/COVERAGE.md`](../doc/COVERAGE.md)
- machine-readable: [`config/curriculum-coverage.json`](../config/curriculum-coverage.json)
- static gate: `tests/coverage_contract.py`

I 25 outcome frozen sono mappati. Questo non significa 25 Activity o 25 grader: oggi l'unica nuova Activity Python materializzata resta il canarino P1 M04.

## Audit `friedpython`

- mapping generale: [`sources/FRIEDPYTHON_MAPPING.md`](../sources/FRIEDPYTHON_MAPPING.md)
- audit liste/tuple: [`sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`](../sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md)
- audit dict/file presenti in `sources/`

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

## Slide source / artifact

- source QA: `tests/slide_source_quality.py`
- pipeline: [`doc/SLIDE_ARTIFACT_PIPELINE.md`](../doc/SLIDE_ARTIFACT_PIPELINE.md)

I 27 source deck sono presenti, ma HTML/PDF/PPTX non vanno dichiarati PASS finché non vengono realmente costruiti e verificati.

## Teacher sign-off

Checklist:

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
```

Resta **PENDING**. Static QA, semantic review e build non possono auto-approvare il corso.

## Course Board / Content Pack

```text
Content Pack → modulo = file/lesson canonica
Course Board → item = heading + sottoalbero
```

Il repo è Course Workspace mutabile; Git conserva storia/review; Course Bundle è release immutabile. `2cornot2c#755` traccia Open Course e bulk whole-module insertion.

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

Il core M04–M30 esiste ed è semanticamente revisionato. Da questo punto il lavoro è:

```text
coverage/provenance
→ slide source/artifact QA
→ teacher sign-off
→ Activity materialization per profilo
→ Course Board/TheBitLab certification
→ Content Pack approval
→ rehearsal reale
```

PY2-01 resta l'unico blocco core senza lesson finali, in attesa del boundary Flowchart Lab.
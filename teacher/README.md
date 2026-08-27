# Python — guida docente

> Stato: **curriculum FROZEN 2026/27; M00–M30 materializzati editorialmente come draft**. M04–M30 hanno semantic review completa; M00–M03 sono il nuovo blocco PY2-01 in review. Non dichiarare il corso pronto per studenti finché delivery, teacher sign-off e rehearsal non sono chiusi.

## Documenti autorevoli

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md)
2. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md)
3. [`doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md`](../doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md)
4. [`doc/COVERAGE.md`](../doc/COVERAGE.md) e [`config/curriculum-coverage.json`](../config/curriculum-coverage.json)
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md)
6. [`config/course-environment.json`](../config/course-environment.json)
7. [`config/flowchart-lab-candidate.json`](../config/flowchart-lab-candidate.json)
8. [`config/p1-canary-profile.json`](../config/p1-canary-profile.json)
9. [`doc/SLIDE_ARTIFACT_PIPELINE.md`](../doc/SLIDE_ARTIFACT_PIPELINE.md)
10. [`doc/SLIDE_ARTIFACT_REVIEW_2026-08-27.md`](../doc/SLIDE_ARTIFACT_REVIEW_2026-08-27.md)
11. [`TEACHER_SIGNOFF_CHECKLIST.md`](TEACHER_SIGNOFF_CHECKLIST.md)

## Regola didattica trasversale

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

Una verifica high-stakes non deve assumere automaticamente contenuti guided/enrichment non realmente consolidati.

---

# PY2-01 — Problem solving, algoritmi e flow chart

**Materializzato come draft.** Il Flowchart Lab ha un consumer reale CI-green su Ubuntu/Windows ma resta `candidate-not-certified`; `flowchart.manual-evidence.v1` rimane fallback obbligatorio finché non completiamo il rehearsal dei profili classroom e la review umana.

- M00 [lesson](../content/python/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md) · [slide](../slides/python/modules/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md) · [runbook](M00_RUNBOOK.md)
- M01 [lesson](../content/python/01_DAL_PROBLEMA_AI_PASSI.md) · [slide](../slides/python/modules/01_DAL_PROBLEMA_AI_PASSI.md) · [runbook](M01_RUNBOOK.md)
- M02 [lesson](../content/python/02_FLOWCHART_SEQUENZA_SELEZIONE.md) · [slide](../slides/python/modules/02_FLOWCHART_SEQUENZA_SELEZIONE.md) · [runbook](M02_RUNBOOK.md)
- M03 [lesson](../content/python/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md) · [slide](../slides/python/modules/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md) · [runbook](M03_RUNBOOK.md)

Timing: M00 orientamento + M01 condividono la settimana 1; M02 = settimana 2; M03 = settimana 3. Nessun Python come prerequisito e nessuna Activity Flowchart con autograding autorevole.

# PY2-02 — Primi programmi Python

- M04 [lesson](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · [runbook](M04_RUNBOOK.md)
- M05 [lesson](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [runbook](M05_RUNBOOK.md)

M04 resta il golden vertical slice tecnico con Activity P1 `py2-activity-b-input-somma-001`. Host CI Ubuntu/Windows e grading Docker source-built pinned sono PASS; #7 resta aperta per il rehearsal classroom.

# PY2-03 — Selezione e logica

- M06 [lesson](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md) · [runbook](M06_RUNBOOK.md)
- M07 [lesson](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [runbook](M07_RUNBOOK.md)
- M08 [lesson](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [runbook](M08_RUNBOOK.md)

# PY2-04 — Iterazione e pattern algoritmici

- M09 [lesson](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [runbook](M09_RUNBOOK.md)
- M10 [lesson](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md) · [runbook](M10_RUNBOOK.md)
- M11 [lesson](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [runbook](M11_RUNBOOK.md)
- M12 [lesson](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [runbook](M12_RUNBOOK.md)

# PY2-05 — Funzioni, decomposizione e testing

- M13 [lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md) · [runbook](M13_RUNBOOK.md)
- M14 [lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [runbook](M14_RUNBOOK.md)
- M15 [lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [runbook](M15_RUNBOOK.md)
- M16 [lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [runbook](M16_RUNBOOK.md)

### Checkpoint A
- [Guida studente](../student/CHECKPOINT_A.md) · [runbook](CHECKPOINT_A_RUNBOOK.md)

Git G1 entra progressivamente da M14 e resta un consumer embedded del corso Git canonico, non un secondo curriculum duplicato.

# PY2-06 — Stringhe come sequenze

- M17 [lesson](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [runbook](M17_RUNBOOK.md)
- M18 [lesson](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [runbook](M18_RUNBOOK.md)
- M19 [lesson](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [runbook](M19_RUNBOOK.md)

# PY2-07 — Liste, tuple e dati tabellari

- M20 [lesson](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [slide](../slides/python/modules/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [runbook](M20_RUNBOOK.md)
- M21 [lesson](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [slide](../slides/python/modules/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [runbook](M21_RUNBOOK.md)
- M22 [lesson](../content/python/22_TUPLE_UNPACKING_MATRICI.md) · [slide](../slides/python/modules/22_TUPLE_UNPACKING_MATRICI.md) · [runbook](M22_RUNBOOK.md)

### Checkpoint B
- [Guida studente](../student/CHECKPOINT_B.md) · [runbook](CHECKPOINT_B_RUNBOOK.md)

# PY2-08 — Set, dizionari e modellazione

- M23 [lesson](../content/python/23_SET_UNICITA_MEMBERSHIP.md) · [slide](../slides/python/modules/23_SET_UNICITA_MEMBERSHIP.md) · [runbook](M23_RUNBOOK.md)
- M24 [lesson](../content/python/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [slide](../slides/python/modules/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [runbook](M24_RUNBOOK.md)
- M25 [lesson](../content/python/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [slide](../slides/python/modules/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [runbook](M25_RUNBOOK.md)

# PY2-09 — Persistenza ed errori prevedibili

- M26 [lesson](../content/python/26_FILE_TESTO_PATHLIB_ERRORI.md) · [slide](../slides/python/modules/26_FILE_TESTO_PATHLIB_ERRORI.md) · [runbook](M26_RUNBOOK.md)

# PY2-10 — Classi, oggetti e capstone

- M27 [lesson](../content/python/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [slide](../slides/python/modules/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [runbook](M27_RUNBOOK.md)
- M28 [lesson](../content/python/28_METODI_STATO_INVARIANTI.md) · [slide](../slides/python/modules/28_METODI_STATO_INVARIANTI.md) · [runbook](M28_RUNBOOK.md)
- M29 [lesson](../content/python/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [slide](../slides/python/modules/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [runbook](M29_RUNBOOK.md)
- M30 [lesson](../content/python/30_CAPSTONE_OOP.md) · [slide](../slides/python/modules/30_CAPSTONE_OOP.md) · [runbook](M30_RUNBOOK.md)

### Checkpoint C
- [Guida studente](../student/CHECKPOINT_C.md) · [runbook](CHECKPOINT_C_RUNBOOK.md)

---

# Activity / grading policy

```text
outcome
→ evidence profile corretto
→ profile certification
→ Activity materialization
```

- P0 — manuale / trace / design;
- P1 — stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- `romeo-sim` — runtime esterno selettivo.

Non deformare gli outcome per adattarli a un grader non certificato. Flowchart Lab oggi è interactive/manual evidence e dichiara `authoritative_grading=false`.

# Coverage / provenance

- [`doc/COVERAGE.md`](../doc/COVERAGE.md)
- [`config/curriculum-coverage.json`](../config/curriculum-coverage.json)
- `tests/coverage_contract.py`
- `tests/course_authoring_catalog.py`
- `tests/py2_01_authoring_static.py`

I 25 outcome frozen restano mappati; questo non significa una Activity per outcome.

# Slide layer

La pipeline release è pinned a Marp 4.5.0 + immutable container digest. Il real build M04–M30 ha già PASS strutturale e sample engineering review; con la materializzazione M00–M03 il target release diventa **31 deck M00–M30**, quindi serve un nuovo real build prima dell'approvazione finale. Il PPTX Marp è presentabile ma non va descritto come nativamente editabile: il contenuto è renderizzato come background image.

# Teacher sign-off

`teacher/TEACHER_SIGNOFF_CHECKLIST.md` resta **PENDING**. CI, review semantica e build non possono auto-approvare il corso.

# Gate ancora aperti

- #7 — rehearsal Classroom Environment del P1;
- #10 — nuovo real build M00–M30 + target PowerPoint/human visual decision;
- #2 / `2cornot2c#753/#754` — Flowchart/Classroom Environment profile certification;
- P2/P3/P4;
- `romeo-sim` cross-profile certification;
- provenance/license final review;
- Content Pack 1.0 approval;
- GO classroom.

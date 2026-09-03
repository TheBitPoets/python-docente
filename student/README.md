# Python — percorso studente

> Stato: **curriculum 2026/27 congelato; M00–M30 materializzati editorialmente come draft**. M04–M30 hanno già semantic review completa; M00–M03 sono il nuovo blocco PY2-01 in review. Il corso non è ancora dichiarato pronto per la classe finché i gate TheBitLab e il sign-off docente non sono chiusi.

## Ambiente

Tutte le attività digitali devono usare il **Classroom Environment TheBitLab** previsto dal corso. Baseline iniziale: Python 3.12-compatible, REPL standard, workspace gestito, VS Code soltanto quando il profilo managed è certificato.

Per PY2-01 il Flowchart Lab ha un consumer candidate reale e testato su Ubuntu/Windows, ma non è ancora una capability classroom-certified. Se non è disponibile nel profilo reale, si usa il fallback carta/lavagna/template + pseudocodice + trace + casi di test: gli outcome non cambiano.

## PY2-01 — Problem solving, algoritmi e flow chart

- **M00** — [Problema, algoritmo, programma, input e output](../content/python/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md) · [slide](../slides/python/modules/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md). Orientamento iniziale integrato nella prima settimana.
- **M01** — [Dal problema ai passi: specifica, pseudocodice e trace](../content/python/01_DAL_PROBLEMA_AI_PASSI.md) · [slide](../slides/python/modules/01_DAL_PROBLEMA_AI_PASSI.md).
- **M02** — [Flow chart: sequenza, input/output e selezione](../content/python/02_FLOWCHART_SEQUENZA_SELEZIONE.md) · [slide](../slides/python/modules/02_FLOWCHART_SEQUENZA_SELEZIONE.md).
- **M03** — [Flow chart: iterazione, terminazione e annidamento](../content/python/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md) · [slide](../slides/python/modules/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md).

In queste tre settimane non serve conoscere Python. Il percorso è:

```text
problema → pseudocodice → flow chart → trace → test → debug
```

Quando Flowchart Lab è disponibile nel percorso managed puoi usare Run/Step/Reset, variable watch, `algorithm.flow.json` e SVG evidence. La qualità del diagramma e della spiegazione resta evidence/rubric docente: non esiste un voto automatico affidabile sulla “bellezza” dell'algoritmo.

## PY2-02 — Primi programmi Python

- **M04** — [Interprete, REPL, valori e I/O](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · Activity canarino `py2-activity-b-input-somma-001`.
- **M05** — [Espressioni, operatori e prime funzioni](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md).

## PY2-03 — Selezione e logica

- **M06** — [Booleani, confronti e `if`](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md).
- **M07** — [`elif`, casi esclusivi e condizioni composte](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md).
- **M08** — [Annidamento, validazione e refactoring](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md).

## PY2-04 — Iterazione e pattern algoritmici

- **M09** — [`while`, stato e sentinelle](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md).
- **M10** — [`for`, `range`, scelta del ciclo](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md).
- **M11** — [Contatori, accumulatori, min/max, ricerca e flag](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md).
- **M12** — [Cicli annidati, griglie e costo del lavoro](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md).

## PY2-05 — Funzioni, decomposizione e testing

- **M13** — [Funzioni, parametri e `return`](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md).
- **M14** — [Scope locale, passaggio dati e composizione](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md).
- **M15** — [Progettazione top-down e responsabilità](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md).
- **M16** — [`assert`, regression test, debug e refactoring](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md).

Da M14 Git G1 viene usato soltanto per osservare stato e cambiamento (`status`/`diff`) in modo guidato.

### Checkpoint A

- [Guida Checkpoint A](CHECKPOINT_A.md)

Consolida il primo nucleo e introduce il primo checkpoint Git G1 guidato:

```text
status → diff → test → add → diff --staged → commit → status → log/show
```

Le spiegazioni e le attività Git appartengono al corso Git G1 canonico; il corso Python le usa senza ricopiarle.

## PY2-06 — Stringhe come sequenze e testo

- **M17** — [Indici, slicing e immutabilità](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md).
- **M18** — [Ricerca, metodi e normalizzazione](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md).
- **M19** — [Algoritmi su testo e parsing semplice](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md).

## PY2-07 — Liste, tuple e dati tabellari

- **M20** — [Liste: mutabilità, metodi e iterazione](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md) · [slide](../slides/python/modules/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md).
- **M21** — [Alias, copie, filtri e ordinamento](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md) · [slide](../slides/python/modules/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md).
- **M22** — [Tuple, unpacking e matrici](../content/python/22_TUPLE_UNPACKING_MATRICI.md) · [slide](../slides/python/modules/22_TUPLE_UNPACKING_MATRICI.md).

### Checkpoint B

- [Guida Checkpoint B](CHECKPOINT_B.md)

Consolida stringhe, liste, tuple, alias/copia e dati tabellari.

## PY2-08 — Set, dizionari e modellazione dei dati

- **M23** — [Set: unicità, membership e operazioni insiemistiche](../content/python/23_SET_UNICITA_MEMBERSHIP.md) · [slide](../slides/python/modules/23_SET_UNICITA_MEMBERSHIP.md).
- **M24** — [Dizionari: chiave→valore, lookup e frequenze](../content/python/24_DIZIONARI_LOOKUP_FREQUENZE.md) · [slide](../slides/python/modules/24_DIZIONARI_LOOKUP_FREQUENZE.md).
- **M25** — [Strutture combinate e scelta del modello](../content/python/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md) · [slide](../slides/python/modules/25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md).

Domanda guida dell'UDA:

```text
quali operazioni devo fare più spesso?
→ quale struttura rappresenta meglio il problema?
```

Non esiste una struttura “più avanzata” in assoluto: list/tuple/set/dict sono strumenti diversi.

## PY2-09 — Persistenza ed errori prevedibili

- **M26** — [File di testo, `pathlib` ed errori prevedibili](../content/python/26_FILE_TESTO_PATHLIB_ERRORI.md) · [slide](../slides/python/modules/26_FILE_TESTO_PATHLIB_ERRORI.md).

Il core usa file di testo UTF-8, `with`, `pathlib` e gestione essenziale degli errori prevedibili. CSV/JSON/binario restano enrichment o percorso successivo.

## PY2-10 — Classi, oggetti e capstone

- **M27** — [Classi, istanze, attributi e `self`](../content/python/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md) · [slide](../slides/python/modules/27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md).
- **M28** — [Metodi, stato e invarianti](../content/python/28_METODI_STATO_INVARIANTI.md) · [slide](../slides/python/modules/28_METODI_STATO_INVARIANTI.md).
- **M29** — [Composizione, collaborazione e responsabilità](../content/python/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md) · [slide](../slides/python/modules/29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md).
- **M30** — [Capstone OOP](../content/python/30_CAPSTONE_OOP.md) · [slide](../slides/python/modules/30_CAPSTONE_OOP.md).

Il capstone deve dimostrare comprensione, non quantità di codice: analisi, classi sensate, stato, metodi, composizione quando appropriata, struttura dati, test/edge case e spiegazione delle scelte.

### Checkpoint C — settimana 33

- [Guida Checkpoint C](CHECKPOINT_C.md)

Nessun nuovo prerequisito: finalizzazione del capstone, recupero mirato, evidence annuale ed eventuale enrichment.

## Policy Activity

M04 resta il canarino tecnico P1. PY2-01 usa per ora evidence manuale/Flowchart managed senza autograding autorevole. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il relativo profilo non è certificato.

Profili target:

- P0 — manuale/trace/design;
- P1 — programmi stdin/stdout;
- P2 — funzioni pure;
- P3 — comportamento oggetti;
- P4 — filesystem;
- `romeo-sim` — missioni robotiche simulate.

Romeo è applicazione selettiva; hardware fisico non è requisito core.

## Metodo del corso

```text
problema → previsione/algoritmo → codice → esecuzione → test → diagnosi → correzione → spiegazione
```

## AI

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

Il curriculum è congelato e M00–M30 sono materializzati editorialmente come draft. M04/P1 ha CI host + Docker autorevole verde; PY2-01 ha un consumer Flowchart candidate verde su Ubuntu/Windows ma richiede ancora il rehearsal dei profili classroom e review umana prima della certificazione. Le slide M04–M30 hanno già un real build strutturale PASS; dopo l'aggiunta di M00–M03 il prossimo release build dovrà coprire tutti i 31 moduli. Restano inoltre P2/P3/P4, `romeo-sim`, teacher sign-off e GO classroom.

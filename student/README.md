# Python — percorso studente

> Stato: **curriculum 2026/27 congelato; contenuti in produzione controllata**. Il corso completo non è ancora dichiarato pronto per la classe.

## Ambiente

Tutte le attività devono essere svolte nel **Classroom Environment TheBitLab** previsto dal corso.

Baseline iniziale:

- Python 3.12-compatible;
- REPL Python standard;
- workspace del corso gestito;
- editor/VS Code soltanto quando l'integrazione TheBitLab del profilo è certificata.

## PY2-01 — Problem solving, algoritmi e flow chart

Stato: **SPEC**. La delivery definitiva dipende dal Flowchart Lab TheBitLab.

## PY2-02 — Primi programmi Python

- **M04** — [Interprete, REPL, valori e I/O](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · Activity canarino `py2-activity-b-input-somma-001`.
- **M05** — [Espressioni, operatori e prime funzioni](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md).

## PY2-03 — Selezione e logica

- **M06** — [Booleani, confronti e `if`](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md).
- **M07** — [`elif`, casi esclusivi e condizioni composte](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md).
- **M08** — [Annidamento, validazione e refactoring](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md).

## PY2-04 — Iterazione e pattern algoritmici — completa editorialmente

- **M09** — [`while`, stato e sentinelle](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md).
- **M10** — [`for`, `range`, scelta del ciclo](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md).
- **M11** — [Contatori, accumulatori, min/max, ricerca e flag](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md).
- **M12** — [Cicli annidati, griglie e costo del lavoro](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md).

## PY2-05 — Funzioni, decomposizione e testing — completa editorialmente

- **M13** — [Funzioni, parametri e `return`](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md) · [slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md).
- **M14** — [Scope locale, passaggio dati e composizione](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md) · [slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md).
- **M15** — [Progettazione top-down e responsabilità](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md) · [slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md).
- **M16** — [`assert`, regression test, debug e refactoring](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md) · [slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md).

### Checkpoint A

- [Guida studente Checkpoint A](CHECKPOINT_A.md)

Consolida il primo nucleo e introduce il primo workflow Git G1 guidato:

```text
status → diff → test → add → commit → log
```

Il materiale Git definitivo verrà collegato dopo l'audit delle dispense docente.

## PY2-06 — Stringhe come sequenze e testo — completa editorialmente

- **M17** — [Stringhe: indici, slicing e immutabilità](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md).
- **M18** — [Ricerca, metodi e normalizzazione](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md).
- **M19** — [Algoritmi su testo e parsing semplice](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md).

Modelli da portare con te:

```text
str = sequenza ordinata immutabile
indice → una posizione
slice → nuova sottostringa
esistenza → in
posizione → find
normalizzazione → solo quando il requisito la giustifica
split() → ponte verso list
```

Il prossimo blocco è **PY2-07 — liste, tuple e dati tabellari**.

## Policy Activity

M04 resta il canarino tecnico P1. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il profilo richiesto non è certificato. Per funzioni/stringhe pure il profilo target è P2 (`2cornot2c#756`).

Romeo è applicazione selettiva tramite simulatore certificato; hardware fisico non è requisito core.

## Metodo del corso

```text
problema
→ previsione / algoritmo
→ codice
→ esecuzione
→ test
→ diagnosi
→ correzione
→ spiegazione
```

## AI

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

M04 è sotto certificazione in `python-docente#7`; il blocco GitHub Actions dei repository privati è `python-docente#8`; P2 è `2cornot2c#756`. Se una capability non è disponibile, si usa il fallback dichiarato senza fingere che il grading automatico sia operativo.

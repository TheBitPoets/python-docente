# Python — percorso studente

> Stato: **curriculum 2026/27 congelato; contenuti in produzione controllata**. Il corso completo non è ancora dichiarato pronto per la classe.

## Ambiente

Tutte le attività devono essere svolte nel **Classroom Environment TheBitLab** previsto dal corso. Baseline iniziale: Python 3.12-compatible, REPL standard, workspace gestito, VS Code soltanto quando il profilo managed è certificato.

## PY2-01 — Problem solving, algoritmi e flow chart

Stato: **SPEC**. La delivery definitiva dipende dal Flowchart Lab TheBitLab.

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

### Checkpoint A

- [Guida Checkpoint A](CHECKPOINT_A.md)

Consolida il primo nucleo e introduce Git G1: `status → diff → test → add → commit → log`. Il materiale Git definitivo sarà collegato dopo l'audit delle dispense docente.

## PY2-06 — Stringhe come sequenze e testo

- **M17** — [Indici, slicing e immutabilità](../content/python/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md) · [slide](../slides/python/modules/17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md).
- **M18** — [Ricerca, metodi e normalizzazione](../content/python/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md) · [slide](../slides/python/modules/18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md).
- **M19** — [Algoritmi su testo e parsing semplice](../content/python/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md) · [slide](../slides/python/modules/19_ALGORITMI_TESTO_PARSING_SEMPLICE.md).

## PY2-07 — Liste, tuple e dati tabellari — completa editorialmente

### M20 — Liste: mutabilità, metodi e iterazione

- [Lesson](../content/python/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md)
- [Slide](../slides/python/modules/20_LISTE_MUTABILITA_METODI_ITERAZIONE.md)

Modello:

```text
str  → sequenza immutabile
list → sequenza mutabile
```

Ricorda: `append()`/`sort()` mutano l'oggetto e non restituiscono la lista.

### M21 — Alias, copie, filtri e ordinamento

- [Lesson](../content/python/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md)
- [Slide](../slides/python/modules/21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md)

Modello:

```text
b = a        → alias, stesso oggetto
b = a.copy() → nuovo contenitore esterno
```

Verifica sempre anche il contratto di mutazione/non-mutazione dell'input.

### M22 — Tuple, unpacking, liste annidate e matrici

- [Lesson](../content/python/22_TUPLE_UNPACKING_MATRICI.md)
- [Slide](../slides/python/modules/22_TUPLE_UNPACKING_MATRICI.md)

Scegli la struttura dal significato:

```text
collezione che cambia → list
raggruppamento stabile posizionale → tuple candidata
matrice/griglia → lista di righe quando il dominio lo richiede
```

Evita la trappola delle righe condivise `[[0] * C] * R`.

### Checkpoint B

- [Guida Checkpoint B](CHECKPOINT_B.md)

Consolida stringhe, liste, tuple, alias/copia e dati tabellari prima di set e dizionari.

## Policy Activity

M04 resta il canarino tecnico P1. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il relativo profilo non è certificato. Per funzioni pure il profilo target è P2 (`2cornot2c#756`).

Romeo è applicazione selettiva tramite simulatore certificato; hardware fisico non è requisito core.

## Metodo del corso

```text
problema → previsione/algoritmo → codice → esecuzione → test → diagnosi → correzione → spiegazione
```

## AI

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

M04 è sotto certificazione in `python-docente#7`; Actions private-repo è `python-docente#8`; P2 è `2cornot2c#756`. Se una capability non è disponibile, si usa il fallback dichiarato senza fingere che il grading automatico sia operativo.

# Python — percorso studente

> Stato: **curriculum 2026/27 congelato; contenuti in produzione controllata**. Il corso completo non è ancora dichiarato pronto per la classe.

## Ambiente

Tutte le attività devono essere svolte nel **Classroom Environment TheBitLab** previsto dal corso.

Baseline iniziale:

- Python 3.12-compatible;
- REPL Python standard;
- workspace del corso gestito;
- editor/VS Code soltanto quando l'integrazione TheBitLab prevista per il profilo usato è certificata.

## PY2-01 — Problem solving, algoritmi e flow chart

Stato: **SPEC**, non ancora lesson finale. La delivery definitiva dipende dal Flowchart Lab TheBitLab.

## PY2-02 — Primi programmi Python

- **M04** — [lesson](../content/python/04_INTERPRETE_REPL_VALORI_IO.md) · [slide](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md) · Activity canarino `py2-activity-b-input-somma-001`.
- **M05** — [lesson](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md) · [slide](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md).

## PY2-03 — Selezione e logica

- **M06** — [Booleani, confronti e `if`](../content/python/06_BOOLEANI_CONFRONTI_IF.md) · [slide](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md).
- **M07** — [`elif`, casi esclusivi e condizioni composte](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md) · [slide](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md).
- **M08** — [Annidamento, validazione e refactoring](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md) · [slide](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md).

## PY2-04 — Iterazione e pattern algoritmici — completa editorialmente

- **M09** — [`while`, stato e sentinelle](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md) · [slide](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md).
- **M10** — [`for`, `range`, scelta del ciclo](../content/python/10_FOR_RANGE_SCELTA_CICLO.md) · [slide](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md).
- **M11** — [Contatori, accumulatori, min/max, ricerca e flag](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md) · [slide](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md).
- **M12** — [Cicli annidati, griglie e costo del lavoro](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md) · [slide](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md).

Modelli da portare con te:

```text
while → durata dipendente dallo stato
for   → percorso/numero di iterazioni noto
contatore → quanti?
accumulatore → totale
min/max → estremo visto finora
R × C → lavoro del corpo interno in una griglia
```

## PY2-05 — Funzioni, decomposizione e testing — completa editorialmente

### M13 — Funzioni, parametri e `return`

- [Lesson](../content/python/13_FUNZIONI_PARAMETRI_RETURN.md)
- [Slide](../slides/python/modules/13_FUNZIONI_PARAMETRI_RETURN.md)

Modello:

```text
argomenti → parametri locali → corpo → return → valore al chiamante
```

Distingui sempre `return` da `print`.

### M14 — Scope locale, passaggio dei dati e composizione

- [Lesson](../content/python/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md)
- [Slide](../slides/python/modules/14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md)

Una funzione dovrebbe ricevere esplicitamente ciò che le serve e restituire ciò che produce. Usa variabili intermedie quando rendono visibile il flusso dei dati.

### M15 — Progettazione top-down e responsabilità

- [Lesson](../content/python/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md)
- [Slide](../slides/python/modules/15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md)

Prima dei corpi delle funzioni progetta responsabilità, firme, contratti, casi di test e un piccolo call graph.

### M16 — `assert`, regression test, debug e refactoring

- [Lesson](../content/python/16_ASSERT_REGRESSION_TEST_REFACTOR.md)
- [Slide](../slides/python/modules/16_ASSERT_REGRESSION_TEST_REFACTOR.md)

Workflow:

```text
contratto → casi → assert → diagnosi → fix → regression → refactor
```

Un test verde non dimostra automaticamente ogni comportamento possibile; anche un test può essere sbagliato rispetto alla specifica.

Dopo M16 arriva il **Checkpoint A**, con consolidamento e primo commit Git guidato.

## Policy Activity

M04 resta il canarino tecnico P1. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il profilo richiesto non è certificato. Per M13–M16 il profilo futuro è P2 function-behavior (`2cornot2c#756`).

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

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando più avanti verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

M04 è sotto certificazione in `python-docente#7`; il blocco GitHub Actions dei repository privati è `python-docente#8`. P2 è tracciato in `2cornot2c#756`. Se una capability non è disponibile, si usa il fallback dichiarato senza fingere che il grading automatico sia operativo.

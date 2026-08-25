# Python — percorso studente

> Stato: **curriculum 2026/27 congelato; contenuti in produzione controllata**. Il corso completo non è ancora dichiarato pronto per la classe.

Questo indice è il punto di ingresso dello studente. Non è necessario conoscere la struttura interna del repository.

## Ambiente

Tutte le attività devono essere svolte nel **Classroom Environment TheBitLab** previsto dal corso.

Baseline iniziale:

- Python 3.12-compatible;
- REPL Python standard;
- workspace del corso gestito;
- editor/VS Code soltanto quando l'integrazione TheBitLab prevista per il profilo usato è certificata.

Non installare tool o dipendenze per conto proprio solo perché una lesson li cita: le capability tecniche appartengono al profilo TheBitLab.

## Secondo anno 2026/27

Il curriculum è congelato, ma i materiali vengono pubblicati modulo per modulo dopo review e gate tecnici.

### PY2-01 — Problem solving, algoritmi e flow chart

Stato: **SPEC**, non ancora lesson finale. Prima di Python impariamo a descrivere e verificare un algoritmo: input/output, passi, selezione, iterazione, trace e casi di test.

### PY2-02 — Primi programmi Python

#### M04 — Interprete, REPL, script, valori e input/output
- Lesson: [`04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md)
- Slide: [`04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md)
- Activity canarino: `py2-activity-b-input-somma-001`

#### M05 — Espressioni, operatori e prime funzioni
- Lesson: [`05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- Slide: [`05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)

### PY2-03 — Selezione e logica

#### M06 — Booleani, confronti e `if`
- Lesson: [`06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md)
- Slide: [`06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md)

#### M07 — `elif`, casi esclusivi e condizioni composte
- Lesson: [`07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- Slide: [`07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)

#### M08 — Annidamento, validazione e refactoring
- Lesson: [`08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- Slide: [`08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)

PY2-03 ti porta da una domanda vero/falso alla scelta consapevole tra `elif`, più `if` indipendenti, condizioni composte e annidamento. Un refactoring è corretto soltanto se conserva i casi di test e il comportamento richiesto.

### PY2-04 — Iterazione e pattern algoritmici

#### M09 — `while`, stato, sentinelle e validazione ripetuta
- Lesson: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- Slide: [`09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)

Per ogni `while` identifica stato iniziale, condizione, corpo e aggiornamento e spiega perché il ciclo può terminare.

#### M10 — `for`, `range` e scelta `for` vs `while`
- Lesson: [`10_FOR_RANGE_SCELTA_CICLO.md`](../content/python/10_FOR_RANGE_SCELTA_CICLO.md)
- Slide: [`10_FOR_RANGE_SCELTA_CICLO.md`](../slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md)

Prima di eseguire un `range`, indica primo valore, ultimo valore effettivo e numero di valori. Ricorda: start incluso, stop escluso.

#### M11 — Contatori, accumulatori, minimo/massimo, ricerca e flag
- Lesson: [`11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md`](../content/python/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md)
- Slide: [`11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md`](../slides/python/modules/11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md)

Domanda guida:

> che cosa devo ricordare tra un'iterazione e la successiva?

Impara a leggere variabili di stato tramite invarianti semplici:

```text
conteggio = quanti casi validi ho già visto
totale    = somma dei valori già elaborati
minimo    = più piccolo valore visto finora
trovato   = almeno un match è comparso finora
```

#### M12 — Cicli annidati, griglie e costo del lavoro
- Lesson: [`12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md`](../content/python/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md)
- Slide: [`12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md`](../slides/python/modules/12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md)

Modello centrale:

```text
R righe × C colonne
→ R × C esecuzioni del corpo interno
```

Prima correttezza e comprensibilità; poi struttura adatta e rimozione del lavoro chiaramente inutile. Niente Big-O formale in questa fase.

PY2-04 è ora materializzata integralmente. Il prossimo blocco è **PY2-05 — funzioni, decomposizione e testing**.

## Policy Activity

M04 resta il canarino tecnico P1. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il profilo richiesto non è certificato.

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

Il risultato corretto da solo non basta: devi spiegare perché la soluzione rispetta la specifica.

## AI

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando più avanti verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

M04 è sotto certificazione in `python-docente#7`; il blocco GitHub Actions dei repository privati è `python-docente#8`. Se una capability TheBitLab non è disponibile, si usa il fallback dichiarato senza fingere che il grading automatico sia operativo.

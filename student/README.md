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

- Lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md)
- Slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md)
- Activity canarino: `py2-activity-b-input-somma-001`

Prevedi prima di eseguire; spiega perché `input()` restituisce testo e quando serve una conversione.

#### M05 — Espressioni, operatori e prime funzioni

- Lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- Slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)

Scegli `/`, `//`, `%` in base al problema, usa parentesi per chiarire l'intenzione e introduci una prima funzione pura con il modello `return` ≠ `print`.

### PY2-03 — Selezione e logica

#### M06 — Booleani, confronti e `if`

- Lesson: [`content/python/06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md)
- Slide: [`slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md)

Traduci le soglie in confronti e testa sotto/sulla/sopra il confine. Comprendi `=` vs `==`, indentazione e ramo vero/falso.

#### M07 — `elif`, casi esclusivi e condizioni composte

- Lesson: [`content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- Slide: [`slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)

Scegli fra una catena `if/elif/else` e più `if` indipendenti a partire dalla specifica. Impara `and`, `or`, `not` e intervalli.

#### M08 — Annidamento, validazione e refactoring

- Lesson: [`content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- Slide: [`slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)

Riconosci dipendenze reali tra decisioni, valida prima di classificare e usa gli stessi test per verificare un refactoring. Qui rileviamo input fuori dominio, ma non lo ripetiamo ancora.

### PY2-04 — Iterazione e pattern algoritmici

#### M09 — `while`, stato, sentinelle e validazione ripetuta

- Lesson: [`content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)
- Slide: [`slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`](../slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md)

Per ogni `while` devi saper identificare:

```text
stato iniziale
condizione
corpo
aggiornamento
```

E soprattutto spiegare **perché può terminare**. Impari validazione ripetuta, sentinelle, casi zero/una/più iterazioni e debug dei cicli infiniti.

`while True` + `break` è una variante successiva: non sostituisce la progettazione della terminazione.

#### M10 — `for`, `range` e scelta `for` vs `while`

Stato: **prossimo modulo da materializzare**.

## Policy Activity

M04 resta il canarino tecnico P1. I moduli successivi hanno esercizi e Activity candidate, ma non materializziamo nuove Activity autogradate finché il profilo richiesto non è certificato.

Romeo è sempre applicazione selettiva tramite simulatore certificato; hardware fisico non è requisito core.

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

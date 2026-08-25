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

Stato: **SPEC**, non ancora lesson finale.

Prima di Python impariamo a descrivere e verificare un algoritmo: input/output, passi, selezione, iterazione, trace e casi di test.

### PY2-02 — Primi programmi Python

#### M04 — Interprete, REPL, script, valori e input/output

- Lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md)
- Slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md)
- Activity canarino: `py2-activity-b-input-somma-001`

Prima di eseguire il codice, scrivi sempre una previsione quando richiesto. Devi saper spiegare perché `input()` restituisce testo e perché una conversione è necessaria quando vuoi fare calcoli numerici.

Lo studente deve ricevere lo **scaffold redatto** generato da TheBitLab, non navigare nelle cartelle `teacher/` o `solution/` del repository docente.

#### M05 — Espressioni, operatori e prime funzioni

- Lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)
- Slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md)

Prevedi valore e tipo prima del REPL. Impara a scegliere fra `/`, `//` e `%` in base al problema, usa parentesi quando chiariscono l'intenzione e introduci una prima funzione pura piccola. Devi saper spiegare il modello iniziale `return` → valore al chiamante e `print` → output.

Nessuna nuova Activity autogradata obbligatoria viene aggiunta qui finché il canarino M04/P1 non è certificato.

### PY2-03 — Selezione e logica

#### M06 — Booleani, confronti e prima selezione con `if`

- Lesson: [`content/python/06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md)
- Slide: [`slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md)

Traduci parole come `almeno`, `al massimo`, `più di`, `meno di` nell'operatore corretto. Per ogni soglia prova un caso sotto, uno sul confine e uno sopra. Devi saper spiegare `=` vs `==`, il ruolo dell'indentazione e perché un ramo può essere saltato senza errore.

Romeo può comparire solo come applicazione opzionale, tramite `romeo-sim` certificato e senza hardware fisico obbligatorio.

#### M07 — `elif`, casi esclusivi e condizioni composte

- Lesson: [`content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)
- Slide: [`slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`](../slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md)

Domanda fondamentale:

```text
un solo risultato tra alternative?
oppure
più effetti che possono coesistere?
```

Da questa risposta scegli fra `if/elif/else` e più `if` indipendenti. Impara poi `and`, `or`, `not`, intervalli e confronti concatenati senza trasformarli in formule da memorizzare.

#### M08 — Annidamento, validazione e refactoring

- Lesson: [`content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)
- Slide: [`slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`](../slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md)

Impara a riconoscere quando una decisione dipende davvero da un'altra, a seguire i path di una selezione annidata e a validare un valore prima di classificarlo. In questa fase sappiamo **rilevare** un input fuori dominio, ma non ancora richiederlo di nuovo: la ripetizione arriverà con `while`.

Un refactoring è corretto soltanto se i casi di test confermano che il comportamento richiesto è rimasto invariato.

### PY2-04 — Iterazione e pattern algoritmici

Il prossimo blocco materializzato partirà da M09: `while`, stato che cambia, terminazione e validazione ripetuta.

## Metodo del corso

Il ciclo che useremo continuamente è:

```text
problema
→ previsione / algoritmo
→ codice
→ esecuzione
→ test
→ lettura dell'errore o del report
→ correzione
→ spiegazione
```

Il risultato corretto da solo non basta: devi riuscire a spiegare che cosa fanno le istruzioni e perché la soluzione rispetta la specifica.

## AI

Nelle attività fondazionali e nelle verifiche core non usare AI per generare la soluzione. Quando più avanti verrà consentita per review/debug, dovrai comunque verificare, testare e spiegare il codice risultante.

## Stato tecnico

Il vertical slice M04 è ancora sotto certificazione in `python-docente#7`. Il blocco GitHub Actions dei repository privati è separato in `python-docente#8`. Se una capability TheBitLab non è ancora disponibile, il docente userà il fallback didattico dichiarato senza fingere che il grading automatico sia operativo.

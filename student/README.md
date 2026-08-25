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

1. Studia la lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md).
2. Durante la lezione usa le slide/recap: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md).
3. Prima di eseguire il codice, scrivi sempre una previsione quando richiesto.
4. Completa l'Activity B **“Completa la somma”** tramite l'assegnazione TheBitLab del docente.
5. Leggi il report tecnico e correggi il programma senza aggiungere output non richiesto.
6. Devi saper spiegare perché `input()` restituisce testo e perché la conversione è necessaria nel problema della somma.

Activity canonica del vertical slice:

```text
py2-activity-b-input-somma-001
```

Lo studente deve ricevere lo **scaffold redatto** generato da TheBitLab, non navigare nelle cartelle `teacher/` o `solution/` del repository docente.

#### M05 — Espressioni, operatori e prime funzioni

Stato: **draft editoriale**; nessuna nuova Activity autogradata obbligatoria finché il canarino M04/P1 non è certificato.

1. Studia la lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md).
2. Usa le slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md).
3. Prevedi valore e tipo prima di usare il REPL.
4. Impara a scegliere fra `/`, `//` e `%` in base al problema, non per imitazione.
5. Usa parentesi quando rendono il calcolo più esplicito.
6. Scrivi una prima funzione pura piccola e verifica più casi.
7. Devi saper spiegare il modello iniziale `return` → valore al chiamante e `print` → output.

M05 propone esercizi pratici su quoziente/resto, tempo, precedenza, debug e prime funzioni, ma non richiede ancora pytest, scope avanzato o package.

### PY2-03 — Selezione e logica

#### M06 — Booleani, confronti e prima selezione con `if`

Stato: **draft editoriale**.

1. Studia la lesson: [`content/python/06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md).
2. Usa le slide: [`slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md).
3. Prima del codice traduci parole come `almeno`, `al massimo`, `più di`, `meno di` nell'operatore di confronto corretto.
4. Per ogni soglia prova almeno un caso sotto, uno esattamente sul confine e uno sopra.
5. Devi saper spiegare `=` vs `==`, il ruolo dell'indentazione e perché un ramo `if` può essere saltato senza che ci sia un errore.
6. Il flow chart resta il modello della decisione: Python cambia la notazione, non la logica.

Romeo può comparire solo come applicazione opzionale dopo gli esercizi generali, tramite `romeo-sim` certificato; non serve hardware fisico per comprendere M06.

#### M07 — `elif`, casi esclusivi e logica composta

Stato: **prossimo modulo da materializzare**.

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

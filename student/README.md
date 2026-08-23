# Python — percorso studente

> Stato: **vertical slice draft**. Il corso completo non è ancora pubblicato né dichiarato pronto per classe.

Questo indice è il punto di ingresso dello studente. Non è necessario conoscere la struttura interna del repository.

## Ambiente

Tutte le attività devono essere svolte nel **Classroom Environment TheBitLab** previsto dal corso.

Baseline del primo vertical slice:

- Python 3.12;
- REPL Python standard;
- workspace del corso gestito;
- editor/VS Code soltanto quando l'integrazione TheBitLab prevista per il profilo usato è certificata.

Non installare tool o dipendenze per conto proprio solo perché una lesson li cita: le capability tecniche appartengono al profilo TheBitLab.

## Secondo anno 2026/27

Il percorso completo è ancora in progettazione. La prima parte materializzata è PY2-02 / M04.

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

Stato: specificato in PY2-02, contenuto finale ancora da produrre dopo la revisione del vertical slice M04.

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

Il vertical slice M04 è ancora sotto certificazione in `python-docente#7`. Se una capability TheBitLab non è ancora disponibile, il docente userà il fallback didattico dichiarato senza fingere che il grading automatico sia operativo.

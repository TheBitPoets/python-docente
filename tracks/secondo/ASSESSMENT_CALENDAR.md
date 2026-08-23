# Python secondo anno — calendario valutazioni (DRAFT)

Vincolo approvato: almeno **una prova teorica/scritta e una prova pratica o pratica/scritta per quadrimestre**.

Il calendario usa i checkpoint del corso per evitare di aggiungere settimane artificiali solo per le verifiche.

## Principi

- valutare comprensione e progettazione, non solo output finale;
- separare almeno in parte teoria/trace da implementazione;
- includere debugging e scelta dei costrutti;
- non rendere Romeo obbligatorio in tutte le prove;
- nessuna AI generativa per produrre soluzioni nelle prove core;
- TheBitLab autograda solo evidenze deterministiche; flow chart, motivazioni e design restano rubric/manual evidence quando necessario.

---

# Primo quadrimestre

## V1 — prova teorica/scritta

**Finestra candidata:** settimane 8–9, dopo M08 e prima che l'iterazione diventi il focus dominante.

### Copertura

- problema/input/output/vincoli;
- algoritmo e pseudocodice;
- flow chart;
- trace;
- tipi/espressioni/operatori;
- `if/elif/else`;
- logica booleana;
- condizioni annidate;
- casi limite;
- lettura di semplici errori.

### Formato possibile

- costruire o completare un flow chart;
- prevedere output/valori intermedi;
- correggere una condizione;
- scegliere tra più strutture decisionali;
- trasformare un requisito in pseudocodice;
- breve frammento Python da leggere/spiegare.

### Evidence

Manuale/rubric per progettazione e spiegazione; eventuali trace strutturati possono essere verificati automaticamente dove deterministico.

---

## V2 — prova pratica/pratica-scritta

**Finestra candidata:** Checkpoint A, settimana 17.

### Copertura

- selezione;
- `for` / `while`;
- cicli e condizioni annidate;
- accumulatori/contatori/sentinelle;
- min/max/ricerca;
- funzioni;
- `return`;
- decomposizione;
- casi di test;
- debugging.

### Struttura candidata

```text
specifica
→ analisi breve
→ algoritmo/pseudocodice essenziale
→ implementazione
→ test richiesti
→ bug-fix o spiegazione finale
```

Una variante può usare una missione Romeo simulata; deve esistere anche una variante generale equivalente.

### Rubrica indicativa

- 30% correttezza;
- 15% comprensione/algoritmo;
- 15% scelta costrutti;
- 15% decomposizione/funzioni;
- 10% test/casi limite;
- 10% leggibilità/naming;
- 5% spiegazione/debug.

Le percentuali sono da calibrare dopo i primi prototipi di prova.

---

# Secondo quadrimestre

## V3 — prova teorica/scritta

**Finestra candidata:** Checkpoint B / settimane 24–25.

### Copertura

- stringhe;
- liste e tuple;
- mutabilità/immutabilità;
- alias vs copia;
- slicing;
- ricerca/filtro/aggregazione;
- matrici;
- scelta preliminare della struttura dati;
- funzioni applicate a collezioni;
- efficienza intuitiva di scansioni e cicli annidati.

Se set/dict sono già completati, la prova può includere una sezione di scelta `list/tuple/set/dict`; altrimenti tale competenza entra nella prova pratica finale.

### Formato possibile

- trace su alias/mutazioni;
- prevedere contenuto di una struttura;
- scegliere una rappresentazione dati;
- correggere un algoritmo su stringhe/liste;
- motivare loop vs metodo built-in;
- breve problema di modellazione.

---

## V4 — prova pratica/pratica-scritta finale

**Finestra candidata:** settimane 31–32, dentro M29/M30; settimana 33 resta buffer/recupero/finalizzazione.

### Copertura

- funzioni;
- stringhe/strutture dati;
- dict/set dove appropriati;
- file/error handling essenziale se richiesto dal problema;
- classi/oggetti;
- `__init__`;
- metodi;
- stato/comportamento;
- composizione semplice;
- testing/debugging;
- scelta e spiegazione del modello dati.

### Formato candidato

Mini-capstone controllato, sviluppato in una finestra definita e con specifica sufficientemente piccola da essere valutabile individualmente.

Romeo simulato è candidato forte per una variante, soprattutto per rendere visibile stato/comportamento; deve restare disponibile una variante generale equivalente.

### Evidence

- sorgenti;
- test/checklist;
- eventuale output/runtime trace;
- breve design note;
- spiegazione di almeno una scelta;
- history Git minima se già introdotta e disponibile nel profilo TheBitLab.

---

# Evidenze formative non necessariamente valutate

Tra le quattro prove principali usare micro-evidence:

- exit ticket di trace;
- diagramma flow chart;
- bug da diagnosticare;
- mini-implementazione;
- confronto `for` vs `while`;
- confronto lista vs set/dict;
- `assert` su funzione;
- missione Romeo;
- commit Git significativo;
- refactoring breve.

Queste evidenze servono a:

- individuare misconceptions;
- decidere recupero/enrichment;
- evitare che una singola verifica misuri tutto;
- costruire la teacher guide con segnali diagnostici concreti.

# Recupero

I checkpoint A/B/C sono progettati anche per recupero.

Una prova di recupero deve misurare gli stessi outcome della prova originale, non replicarne necessariamente il testo o il progetto.

# AI e verifiche

Nelle V1–V4:

- nessuna AI generativa per creare soluzione, algoritmo o codice;
- strumenti di completamento AI disabilitati se presenti;
- l'ambiente TheBitLab deve rendere la policy tecnicamente e proceduralmente chiara quanto possibile.

Le Activity AI-assisted appartengono a un modulo/competenza separato e non sostituiscono queste evidenze fondamentali.

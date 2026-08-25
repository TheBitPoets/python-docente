# M12 — Runbook docente

## Modulo

**Cicli annidati, griglie e costo del lavoro**  
UDA PY2-04 — Iterazione e pattern algoritmici

Stato: draft editoriale controllato.

## Obiettivo docente

Chiudere la prima UDA sui cicli portando gli studenti da:

```text
so scrivere un ciclo
```

verso:

```text
so comporre cicli quando il problema ha più dimensioni
→ so fare trace delle coppie
→ so prevedere quante volte lavoro
→ so riconoscere lavoro chiaramente inutile
```

Non trasformare M12 in una lezione di complessità algoritmica formale. Il livello richiesto è **quantità di lavoro osservabile e motivata**.

---

# Ritmo consigliato — settimana 12

## Ora teoria attiva 1 — coppie e griglie

### 0–10 min — richiamo

Riprendere `for range` e chiedere:

> Se ho 3 righe e per ogni riga devo visitare 4 colonne, che struttura naturale emerge?

### 10–25 min — doppio ciclo

Usare subito:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

Gli studenti devono elencare le coppie prima dell'esecuzione.

### 25–40 min — R × C

Passare dal trace al conteggio:

```text
2 × 3 = 6
3 × 4 = 12
```

Far distinguere “numero di iterazioni esterne” e “numero di esecuzioni del corpo interno”.

### 40–55 min — griglia

Costruire un rettangolo di simboli e mostrare il significato dei due livelli.

### Exit micro-check

Per tre coppie di `range` brevi, prevedere coppie e numero di esecuzioni.

---

# Ora teoria attiva 2 — reset, condizioni e lavoro

## 0–15 min — reset al livello giusto

Usare un “totale per riga”. Chiedere dove deve vivere l'inizializzazione.

Mostrare tre versioni:

- troppo esterna;
- corretta;
- troppo interna.

## 15–30 min — `if` dentro due cicli

Pattern diagonale o scacchiera semplice.

Il focus è leggere la coppia `(riga, colonna)` e capire da quali variabili dipende la decisione.

## 30–45 min — lavoro ripetuto

Mostrare un calcolo che non dipende da `i` ma viene rifatto dentro il loop.

Domanda:

> cambia davvero a ogni iterazione?

Se no, spostarlo fuori può migliorare sia intenzione sia lavoro svolto.

## 45–55 min — confronto singolo vs doppio

Tabella N / N×N con valori piccoli. Nessuna notazione Big-O obbligatoria.

Far verbalizzare:

> se raddoppio N, che cosa succede al numero di esecuzioni?

---

# Ora laboratorio

## Fase A — nested trace, 10 min

Coppie `(i, j)` su range piccoli.

## Fase B — controlled change, 10 min

Da 2×3 a 4×5:

1. prevedere il numero di iterazioni;
2. prevedere la forma dell'output;
3. poi modificare il codice.

## Fase C — implementazione, 15 min

Griglia rettangolare o tabella con un pattern condizionale.

## Fase D — Debug Clinic, 10 min

Distribuire bug diversi:

- indice sbagliato;
- reset al livello errato;
- `print()` con indentazione sbagliata;
- range interno non corretto;
- calcolo invariabile ripetuto.

## Fase E — mini-project / exit, 10–15 min

Problema con selezione + ciclo + almeno uno tra:

- accumulatore;
- ricerca;
- doppio ciclo.

Richiedere anche una stima semplice del numero di iterazioni principali.

---

# Misconception watchlist

## M1 — il ciclo interno continua da dove era rimasto

Correzione: trace completo. Per ogni nuova iterazione esterna il `for` interno esegue nuovamente il proprio percorso.

## M2 — due cicli annidati significano sempre N²

Solo se entrambi eseguono circa N iterazioni. In generale ragioniamo sui range reali: `R × C`.

## M3 — più annidamento = più avanzato

No. L'annidamento deve essere richiesto dal problema. Annidare inutilmente peggiora comprensibilità e lavoro.

## M4 — basta contare le righe di codice per stimare il costo

No. Conta quante volte le istruzioni vengono eseguite.

## M5 — ottimizzare prima di avere una soluzione corretta

Ordine didattico obbligatorio:

```text
correttezza → comprensibilità → struttura → lavoro inutile → efficienza
```

## M6 — tutto ciò che è fuori dal ciclo è più veloce quindi va spostato

Solo ciò che non dipende dall'iterazione corrente e mantiene la stessa semantica può essere spostato.

---

# Differenziazione

## Recupero

- range massimo 2×3;
- trace cartaceo obbligatorio;
- nomi `riga`/`colonna` invece di `i`/`j`;
- output semplice di coordinate prima dei pattern;
- una sola variabile di stato per riga.

## Enrichment

- griglia non quadrata;
- pattern diagonale/inversa semplice;
- contare quante celle soddisfano una condizione;
- confrontare una versione che ricalcola un valore invariabile e una che lo pre-calcola;
- discutere caso N×M vs N×N.

---

# Evidence docente

Raccogliere almeno:

- un nested trace corretto;
- previsione `R × C`;
- un debug sul livello di reset;
- una spiegazione del perché un doppio ciclo è naturale in un problema;
- un esempio di lavoro ripetuto evitabile.

---

# Romeo

Uso opzionale, solo se `romeo-sim` è certificato:

- percorsi a griglia;
- ripetizione di una sequenza per righe/colonne;
- scenario che rende visibile la quantità di comandi prodotti.

Non usare Romeo per introdurre networking, eventi o hardware in questa UDA.

---

# Cosa NON anticipare

- Big-O formale;
- matrici Python vere come liste di liste: arriveranno in PY2-07;
- comprehensions annidate;
- generatori;
- NumPy;
- ottimizzazioni premature;
- profiling professionale.

M12 prepara questi concetti senza sovraccaricare il secondo anno.

---

# Exit checkpoint UDA PY2-04

Prima di entrare nelle funzioni, verificare che gli studenti sappiano:

1. scegliere `for` o `while`;
2. spiegare la terminazione di un `while`;
3. usare sentinella/validazione ripetuta;
4. usare contatore/accumulatore;
5. mantenere min/max progressivi;
6. distinguere primo match/tutti i match;
7. leggere un flag;
8. combinare selezione e ciclo;
9. leggere un doppio ciclo;
10. stimare `R × C` in casi semplici;
11. riconoscere lavoro chiaramente inutile.

Se questi punti non sono stabili, usare il checkpoint successivo per consolidare prima di formalizzare la decomposizione in funzioni.

---

# Handoff a PY2-05

La domanda cambia da:

> come controllo il flusso?

verso:

> come divido il programma in responsabilità piccole, nominabili e testabili?

Questo apre M13–M16 su funzioni, `return`, scope locale, top-down, assert e regression/refactor.

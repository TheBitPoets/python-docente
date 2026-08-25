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

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. distinguere ciclo esterno e ciclo interno;
2. fare trace di coppie `(riga, colonna)` su range piccoli;
3. prevedere `R × C` esecuzioni del corpo interno;
4. spiegare che il ciclo interno riparte per ogni iterazione esterna;
5. inizializzare/reset tare lo stato al livello corretto;
6. usare un `if` che dipende dalla coppia corrente quando il problema lo richiede;
7. riconoscere quando il doppio ciclo è naturale al dominio;
8. riconoscere un calcolo chiaramente ripetuto pur non dipendendo dall'iterazione;
9. confrontare intuitivamente una scansione singola con una doppia scansione.

## GUIDED EXPOSURE

- `print(..., end="")` come puro strumento di output per costruire righe;
- tabella `N` vs `N×N` per intuire la crescita del lavoro;
- spostare fuori dal ciclo un calcolo invariabile quando la semantica resta identica.

## ENRICHMENT / BACKUP

- griglie/pattern più elaborati;
- conteggi su celle;
- confronti `N×M` vs `N×N` più ricchi;
- Romeo su percorsi a griglia.

Big-O, profiling e ottimizzazione professionale non fanno parte del gate.

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

Far distinguere:

- quante iterazioni esterne?;
- quante interne per ogni esterna?;
- quante esecuzioni totali del corpo interno?.

### 40–55 min — griglia

Costruire un rettangolo di simboli. `end=""` è soltanto uno strumento per non andare a capo: non diventa un nuovo argomento da valutare.

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

Collegare a M11:

> che cosa deve significare questa variabile durante **una singola riga**?

## 15–30 min — `if` dentro due cicli

Pattern diagonale o scacchiera semplice.

Il focus è leggere la coppia `(riga, colonna)` e capire da quali variabili dipende la decisione.

## 30–45 min — lavoro ripetuto

Mostrare un calcolo che non dipende da `i` ma viene rifatto dentro il loop.

Domanda:

> cambia davvero a ogni iterazione?

Se no, spostarlo fuori può migliorare intenzione e lavoro svolto, purché il comportamento resti identico.

## 45–60 min — confronto singolo vs doppio

Tabella N / N×N con valori piccoli. Nessuna notazione Big-O obbligatoria.

Far verbalizzare:

> se aumento entrambe le dimensioni, perché il numero di esecuzioni cresce molto più rapidamente di un singolo passaggio?

Non richiedere formule asintotiche.

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

Il mini-project può essere completato fuori dall'ora se necessario: non deve rubare tempo al consolidamento dell'exit gate.

---

# Misconception watchlist

## M1 — il ciclo interno continua da dove era rimasto

Correzione: trace completo. Per ogni nuova iterazione esterna il `for` interno esegue nuovamente il proprio percorso.

## M2 — due cicli annidati significano sempre N²

Solo se entrambi eseguono circa N iterazioni. In generale ragioniamo sui range reali: `R × C`.

## M3 — più annidamento = più avanzato

No. L'annidamento deve essere richiesto dal problema.

## M4 — basta contare le righe di codice per stimare il costo

No. Conta quante volte le istruzioni vengono eseguite.

## M5 — ottimizzare prima di avere una soluzione corretta

Ordine:

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
- output di coordinate prima dei pattern;
- una sola variabile di stato per riga.

## Enrichment

- griglia non quadrata;
- pattern diagonale/inversa semplice;
- contare celle che soddisfano una condizione;
- confronto calcolo invariabile dentro/fuori;
- caso N×M vs N×N.

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

---

# Exit checkpoint UDA PY2-04 — cinque competenze integrate

## A — Controllare la ripetizione

- scegliere `for`/`while`;
- spiegare terminazione e confini.

## B — Tracciare

- trace di loop singoli e doppi piccoli;
- zero/una/più iterazioni.

## C — Mantenere stato

- contatore/accumulatore;
- min/max;
- flag/ricerca;
- inizializzazione/update corretti.

## D — Comporre

- `if` dentro loop;
- doppio ciclo semplice quando il dominio lo richiede.

## E — Ragionare sul lavoro

- `R × C`;
- riconoscere lavoro chiaramente inutile;
- privilegiare correttezza e leggibilità prima dell'ottimizzazione.

Non richiedere nel gate:

- `while True`;
- uso autonomo di `break/continue`;
- Big-O;
- `for/else`;
- comprehensions.

---

# Handoff a PY2-05

La domanda cambia da:

> come controllo il flusso?

verso:

> come divido il programma in responsabilità piccole, nominabili e testabili?

Questo apre M13–M16 su funzioni, `return`, scope locale, top-down, assert e regression/refactor.

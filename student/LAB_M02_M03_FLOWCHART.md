# Laboratorio — Selezioni e cicli nei flow chart

**Durata:** 60–90 minuti.  
**Prerequisiti:** [pseudocodice e trace (M01)](../content/python/01_DAL_PROBLEMA_AI_PASSI.md), [selezione (M02)](../content/python/02_FLOWCHART_SEQUENZA_SELEZIONE.md), [cicli e annidamento (M03)](../content/python/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md).

## Organizzazione del lavoro

Lavora individualmente o in coppia. In coppia, alternate chi costruisce l’algoritmo e chi lo esegue a mano, scambiandovi i ruoli a ogni esercizio.

- **In 60 minuti:** svolgi gli esercizi **1, 3, 5, 7, 9 e 11**, uno per ogni gruppo.
- **In 90 minuti:** aggiungi gli esercizi **2, 4, 6, 8, 10 e 12**. Parti dal lavoro del primo esercizio del gruppo e modifica ciò che serve.
- Usa il Flowchart Lab se disponibile; altrimenti disegna su carta o sul template fornito dal docente.

| Fase | Percorso da 60 minuti | Aggiunte per arrivare a 90 minuti |
| --- | --- | --- |
| Leggere le consegne e preparare il foglio | 5 min | — |
| Selezione a due vie | Esercizio 1: 6 min | Esercizio 2: 4 min |
| Selezione a più vie | Esercizio 3: 8 min | Esercizio 4: 5 min |
| Selezione con un solo ramo | Esercizio 5: 6 min | Esercizio 6: 4 min |
| Ciclo controllato dai dati | Esercizio 7: 8 min | Esercizio 8: 5 min |
| Ripetizioni lette in input | Esercizio 9: 8 min | Esercizio 10: 5 min |
| Ciclo e selezione annidati | Esercizio 11: 14 min | Esercizio 12: 7 min |
| Controllo e consegna | 5 min | — |
| **Totale** | **60 min** | **+30 min** |

I tempi sono indicativi. Se un esercizio essenziale richiede più tempo, completa e verifica quello prima di passare alle varianti.

## Che cosa produrre

Per ogni esercizio svolto prepara:

1. **Input e output:** indica quali dati ricevi e quale risultato devi mostrare.
2. **Flow chart:** usa i simboli del corso e scrivi `true` e `false` sulle uscite dei rombi.
3. **Pseudocodice sotto il diagramma:** usa `LEGGI`, `MOSTRA`, `ASSEGNA variabile ← espressione`, `SE / ALTRIMENTI SE / ALTRIMENTI / FINE SE` e `MENTRE / FINE MENTRE`.
4. **Verifica:** esegui tutti i casi indicati e annota l’output ottenuto. Per almeno un caso scrivi una trace dei valori e dei rami percorsi.
5. **Per i cicli:** spiega in una frase che cosa cambia e quando si esce.

Per le varianti puoi copiare il tuo primo diagramma e modificarlo, conservando entrambe le versioni. I risultati attesi servono per il confronto: prevedili prima di seguire le frecce. Il lavoro richiesto è su flow chart e pseudocodice; Python verrà introdotto nel modulo successivo.

---

## A. Selezione a due vie

Usa `SE ... ALTRIMENTI`: per ogni input si esegue uno solo dei due rami.

### 1. Spedizione gratuita — essenziale, 6 minuti

Un negozio applica **5 euro** di spedizione quando l’importo degli acquisti è inferiore a **50 euro**. Da 50 euro in poi la spedizione è gratuita.

Leggi `importo`, un numero intero non negativo, e mostra **soltanto il costo della spedizione**.

| Input: importo | Output atteso |
| --- | --- |
| 49 | 5 |
| 50 | 0 |
| 51 | 0 |

**Controlla:** a quale ramo appartiene esattamente 50?

### 2. Pari oppure dispari — variante, 4 minuti

Leggi un intero `numero` maggiore o uguale a zero. Mostra `pari` se il resto della divisione per 2 è zero, altrimenti mostra `dispari`. Usa l’operatore `%` studiato in M01.

| Input: numero | Output atteso |
| --- | --- |
| 0 | pari |
| 7 | dispari |
| 8 | pari |

**Controlla:** ciascun percorso deve produrre un solo messaggio.

## B. Selezione a più vie

Usa una catena con **almeno due `ALTRIMENTI SE`**. Dopo il primo caso vero, gli altri rami vengono saltati.

### 3. Quattro fasce di punteggio — essenziale, 8 minuti

Leggi un `punteggio` intero da 0 a 100 e mostra una sola valutazione:

- da 90 a 100: `ottimo`;
- da 75 a 89: `buono`;
- da 60 a 74: `sufficiente`;
- da 0 a 59: `insufficiente`.

L’input è già nell’intervallo ammesso. Disegna un rombo per ogni confronto necessario.

| Input: punteggio | Output atteso |
| --- | --- |
| 59 | insufficiente |
| 60 | sufficiente |
| 75 | buono |
| 90 | ottimo |

**Aggiungi due test:** 74 e 89, scrivendo tu l’output atteso. Spiega perché 95 deve produrre un solo messaggio, anche se supera tutte e tre le soglie.

### 4. Biglietto del museo — variante, 5 minuti

Per questo esercizio il museo usa queste tariffe:

- meno di 6 anni: **0 euro**;
- da 6 a 13 anni: **5 euro**;
- da 14 a 64 anni: **10 euro**;
- da 65 anni in poi: **7 euro**.

Leggi `eta`, un intero non negativo, e mostra il prezzo del biglietto. Adatta la catena dell’esercizio 3 alle nuove soglie.

| Input: eta | Output atteso |
| --- | --- |
| 5 | 0 |
| 6 | 5 |
| 14 | 10 |
| 65 | 7 |

**Aggiungi due test:** 13 e 64. Verifica che tra due fasce consecutive non rimanga scoperta nessuna età.

## C. Selezione con un solo ramo

Usa `SE ... FINE SE`, **senza `ALTRIMENTI`**. Il ramo falso salta l’azione facoltativa e raggiunge il passo comune.

### 5. Consegna urgente — essenziale, 6 minuti

Leggi `prezzo`, un intero non negativo, e `urgente`, che può valere soltanto `si` oppure `no`.

Il prezzo finale parte dal prezzo letto. **Solo se la consegna è urgente**, aggiungi 3 euro. Mostra il prezzo finale in entrambi i casi, dopo il ricongiungimento dei rami.

| Input: prezzo, urgente | Output atteso |
| --- | --- |
| 12, no | 12 |
| 12, si | 15 |
| 0, si | 3 |

**Controlla:** il valore da mostrare deve essere disponibile anche quando la condizione è falsa.

### 6. Bonus missione — variante, 4 minuti

Leggi `punti`, un intero non negativo, e `completata`, che vale `si` oppure `no`. Se la missione è completata, aggiungi **10 punti**; altrimenti i punti rimangono quelli iniziali. Mostra sempre il punteggio finale.

| Input: punti, completata | Output atteso |
| --- | --- |
| 20, no | 20 |
| 20, si | 30 |
| 0, si | 10 |

**Controlla:** l’output deve stare dopo `FINE SE`.

## D. Ciclo controllato dai dati

Il numero di ripetizioni dipende dai valori letti. Usa `MENTRE` e rendi visibile quale lettura permette di aggiornare la condizione.

### 7. Un voto valido — essenziale, 8 minuti

Leggi un voto intero. Se è fuori dall’intervallo **0–10**, estremi inclusi, chiedilo di nuovo. Continua finché ricevi un voto valido, poi mostra **una sola volta quel voto**.

| Input successivi | Output atteso | Nuove letture dopo la prima |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10 | 10 | 0 |
| -1, 11, 7 | 7 | 2 |

**Trace richiesta:** usa la sequenza `-1, 11, 7` e registra voto, esito della condizione e azione a ogni controllo.

**Spiega:** se continuano ad arrivare voti non validi, il ciclo termina? Da quale evento dipende l’uscita?

### 8. Somma fino allo zero — variante, 5 minuti

Leggi una sequenza di interi non negativi. Lo **zero termina l’inserimento**. Somma i valori precedenti allo zero e mostra il totale soltanto alla fine. Non leggere altri dati dopo lo zero.

| Input successivi | Output atteso |
| --- | --- |
| 0 | 0 |
| 2, 3, 0 | 5 |
| 4, 1, 2, 0 | 7 |

**Controlla:** dove inizializzi il totale? Dove leggi il primo valore e quelli successivi? Per completare queste prove, tutte le sequenze fornite terminano con zero.

## E. Ciclo con numero di ripetizioni letto in input

Leggiamo prima quante ripetizioni svolgere: da quel momento il numero di giri è stabilito. **Nel flow chart rimane un test sul contatore**: usa l’inizializzazione, `MENTRE` e l’incremento visti in M03. I valori elaborati nel corpo non decidono quando uscire.

### 9. I primi N numeri — essenziale, 8 minuti

Leggi `N`, un intero non negativo. Mostra **esattamente N numeri interi consecutivi, partendo da 0**, uno per iterazione. Se `N` vale zero, non mostrare nessun numero.

| Input: N | Output atteso, in ordine |
| --- | --- |
| 5 | 0, 1, 2, 3, 4 |
| 1 | 0 |
| 0 | nessun output |

Per `N = 5`, prepara una trace con queste colonne: numero dell’iterazione, valore prima dell’output, output, valore dopo l’aggiornamento. Registra anche l’ultimo controllo, quello che fa uscire dal ciclo.

**Controlla:** con `N = 5` devono esserci esattamente cinque iterazioni. L’ultimo numero mostrato è 4; il numero 5 non deve essere mostrato.

### 10. N letture, una somma — variante, 5 minuti

Leggi `N`, un intero non negativo, poi leggi **esattamente N numeri interi**, anche negativi o nulli. Mostra la loro somma dopo l’ultima lettura. Se `N` vale zero, non leggere altri dati e mostra 0.

Tra i valori da sommare, **zero è un dato** e non interrompe il ciclo. `N` indica soltanto quante letture fare e non entra nella somma.

| Primo input: N | Valori successivi | Output atteso |
| --- | --- | --- |
| 4 | 1, 2, 3, 4 | 10 |
| 0 | nessuno | 0 |
| 3 | 5, 0, -2 | 3 |

**Controlla:** una variabile conta le letture e una conserva la somma. Devono mantenere significati diversi.

## F. Ciclo e selezione annidati

### 11. Contare i numeri pari — essenziale, 14 minuti

Leggi **esattamente cinque interi non negativi** e conta quanti sono pari. Mostra soltanto il conteggio finale.

Usa una **selezione dentro il ciclo**: ogni numero viene letto, ma il conteggio dei pari aumenta soltanto quando il resto della divisione per 2 è zero. Anche zero è pari.

| Cinque input | Output atteso |
| --- | --- |
| 2, 3, 4, 5, 0 | 3 |
| 1, 3, 5, 7, 9 | 0 |
| 0, 2, 4, 6, 8 | 5 |

**Trace richiesta:** per il primo caso registra numero di letture, valore letto, esito del confronto e conteggio dei pari.

**Controlla:** il numero di letture deve aumentare anche quando il valore è dispari. Che cosa succederebbe se aggiornassi quel contatore soltanto nel ramo vero?

### 12. Avvio facoltativo — variante, 7 minuti

Leggi `scelta`, che può valere soltanto `avvia` oppure `stop`. Se la scelta è `avvia`, mostra il messaggio `pronto` **esattamente tre volte**; se è `stop`, termina senza mostrare messaggi.

Usa un **ciclo dentro una selezione**. Il ramo che salta il ciclo deve arrivare alla fine.

| Input: scelta | Output atteso |
| --- | --- |
| avvia | pronto, pronto, pronto |
| stop | nessun output |

**Spiega:** nell’esercizio 11 la selezione decide se aggiornare un conteggio; qui che cosa decide? Mostra nel diagramma quale percorso evita l’intero ciclo.

---

## Controllo finale e consegna

- [ ] Ogni rombo ha due uscite etichettate e tutti i collegamenti sono leggibili.
- [ ] Flow chart e pseudocodice descrivono gli stessi passi nello stesso ordine.
- [ ] Ogni variabile viene inizializzata o letta prima di essere usata.
- [ ] Ho verificato le uguaglianze sulle soglie e il numero esatto di iterazioni.
- [ ] Nei cicli il ritorno raggiunge il controllo corretto e l’aggiornamento avviene nel punto giusto.
- [ ] Per ogni esercizio svolto ho annotato i test e almeno una trace.

Consegna gli elaborati identificati con **nome o nomi della coppia e numero dell’esercizio**. Se lavori su carta, consegna i fogli; se lavori in digitale, raccogli diagrammi, pseudocodice e verifiche nella cartella indicata dal docente.

Chiudi scegliendo uno dei tuoi cicli e spiegando in due frasi **perché termina** e **quale modifica potrebbe impedirgli di terminare**.

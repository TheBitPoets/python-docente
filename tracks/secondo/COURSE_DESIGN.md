# Python — track secondo anno (DRAFT)

## Profilo

- durata nominale: **33 settimane**;
- carico: **3 ore/settimana = 99 ore**;
- ingresso: nessun prerequisito di programmazione;
- uscita: programmazione strutturata solida, decomposizione in funzioni, stringhe e strutture dati fondamentali, file/error handling di base, classi e oggetti fondamentali.

Il corso deve produrre studenti capaci non solo di ricordare sintassi, ma di:

1. comprendere un problema;
2. formalizzare una soluzione;
3. scegliere costrutti e strutture dati appropriati;
4. implementare una soluzione leggibile;
5. testarla e fare debugging;
6. spiegare perché la soluzione funziona e quali alternative esistono.

## Piano 33 settimane

| Settimane | UDA | Ore | Focus |
|---|---|---:|---|
| 1–3 | PY2-01 Problem solving e algoritmi | 9 | problemi, decomposizione, pseudocodice, flow chart, trace, test cases |
| 4–5 | PY2-02 Primi programmi Python | 6 | ambiente, print/input, tipi, variabili, operatori, conversioni, debugging base |
| 6–8 | PY2-03 Selezione | 9 | bool, confronti, if/elif/else, condizioni composte e annidate, validazione |
| 9–12 | PY2-04 Iterazione | 12 | while, for/range, sentinelle, contatori, accumulatori, break/continue, annidamento |
| 13–14 | PY2-05 Pattern algoritmici | 6 | min/max, ricerca, frequenze, pattern combinati, scelta del costrutto |
| 15–18 | PY2-06 Funzioni e decomposizione | 12 | parametri, return, scope, composizione, top-down, test di funzioni |
| 19–21 | PY2-07 Stringhe | 9 | indicizzazione, slicing, iterazione, metodi, parsing, problemi testuali |
| 22–25 | PY2-08 Liste e tuple | 12 | mutabilità, metodi, alias/copia, iterazione, tuple, matrici, scelta struttura |
| 26–28 | PY2-09 Set e dizionari | 9 | membership, lookup, frequenze, record, strutture annidate, scelta struttura |
| 29–30 | PY2-10 File ed errori | 6 | with/open, text I/O, pathlib introduttivo, try/except, dati persistenti |
| 31–33 | PY2-11 Classi, oggetti e capstone | 9 | classi, istanze, attributi, metodi, __init__, composizione, mini-progetto |

Totale: **99 ore**.

## Ritmo indicativo delle 3 ore

Non è una gabbia, ma il default progettuale è:

```text
30–45 min   nuovo concetto / modello mentale
20–30 min   trace / esempi / domande
45–60 min   guided coding / Activity A-B
45–60 min   problem solving / Activity C-D
15–30 min   recap, confronto soluzioni, evidence
```

Alcune settimane saranno invece interamente laboratorio, verifica, recupero o mini-progetto.

## Progressione algoritmica obbligatoria

### Prima del Python

Lo studente deve saper rappresentare in flow chart:

- sequenza;
- input/output;
- selezione semplice;
- selezione doppia;
- selezione multipla;
- ciclo pre-condizionale;
- ciclo controllato da contatore;
- selezione dentro un ciclo;
- ciclo dentro una selezione;
- cicli annidati.

### Dopo l'introduzione di Python

Per problemi significativi chiedere periodicamente:

```text
1. dati in ingresso
2. output
3. esempi/casi limite
4. algoritmo/pseudocodice
5. eventuale flow chart
6. trace manuale
7. codice Python
8. test
9. spiegazione delle scelte
```

Non è necessario produrre sempre tutti e nove gli artefatti; vengono scelti in base all'obiettivo della Activity.

## Selezione: competenze minime

Lo studente deve saper distinguere:

```python
if a:
    ...
if b:
    ...
```

da:

```python
if a:
    ...
elif b:
    ...
else:
    ...
```

Deve capire quando le condizioni sono indipendenti e quando sono mutuamente esclusive.

Deve saper costruire e semplificare condizioni con `and`, `or`, `not` e confronti, evitando annidamenti inutili.

## Iterazione: competenze minime

Lo studente deve padroneggiare:

- `while` quando la durata dipende da una condizione;
- `for` quando si itera su una sequenza/intervallo;
- contatore;
- accumulatore;
- valore sentinella;
- flag con consapevolezza;
- min/max progressivo;
- cicli annidati;
- `if` dentro `for/while`;
- `for/while` dentro rami condizionali;
- controllo degli errori off-by-one.

Non basta riconoscere il costrutto: deve saper scegliere tra `for` e `while` e motivarlo.

## Funzioni: soglia di padronanza

Prima di passare alle strutture dati complesse, lo studente deve saper:

- estrarre una funzione da codice duplicato;
- distinguere parametro e argomento;
- restituire un risultato invece di stampare tutto;
- separare acquisizione dati, logica e presentazione;
- chiamare funzioni da altre funzioni;
- progettare almeno un piccolo programma top-down;
- scrivere semplici casi di test deterministici.

## Strutture dati: criterio di scelta

La domanda ricorrente sarà: **quali operazioni dobbiamo fare sui dati?**

| Esigenza dominante | Struttura candidata |
|---|---|
| sequenza ordinata modificabile | `list` |
| sequenza/record immutabile semplice | `tuple` |
| elementi unici / membership | `set` |
| associazione chiave → valore / lookup | `dict` |
| testo | `str` |

Gli studenti devono anche combinare strutture:

- lista di tuple;
- lista di dizionari;
- dizionario di liste;
- dizionario di dizionari;
- matrice come lista di liste.

L'obiettivo non è memorizzare tutte le combinazioni, ma modellare i dati in funzione del problema.

## Efficienza nel secondo anno

Niente corso formale di analisi asintotica, ma introdurre precocemente intuizioni come:

- una scansione completa cresce con la quantità di dati;
- due cicli annidati sulla stessa collezione possono crescere molto più velocemente;
- cercare per chiave in un dizionario è normalmente più adatto che scandire una lista quando il problema è un lookup;
- evitare lavoro ripetuto dentro un ciclo quando può essere calcolato una volta;
- leggibilità e semplicità restano criteri fondamentali: una micro-ottimizzazione non giustifica codice incomprensibile.

## OOP: confine di seconda

### Core obbligatorio

- perché introdurre un oggetto;
- classe vs istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato + comportamento;
- più istanze indipendenti;
- composizione semplice;
- responsabilità di una classe;
- mini-progetto finale.

### Estensione se il gruppo è pronto

- `__str__` / `__repr__`;
- properties introduttive;
- ereditarietà semplice;
- dataclass come confronto dopo aver compreso una classe esplicita.

### Fuori dal core di seconda

- multiple inheritance/MRO;
- descriptors;
- metaclasses;
- ABC/protocols avanzati;
- decorators avanzati;
- iterator protocol custom;
- async/concurrency;
- packaging professionale.

## Verifiche e valutazione

Distribuire le evidenze durante tutto l'anno:

- flow chart/pseudocodice;
- trace di codice;
- esercizi di implementazione;
- debug di codice difettoso;
- scelta del costrutto/struttura dati motivata;
- verifiche pratiche a tempo;
- mini-progetti;
- capstone OOP.

### Rubrica trasversale proposta

- correttezza;
- comprensione del problema;
- qualità dell'algoritmo;
- scelta dei costrutti;
- decomposizione;
- scelta/modellazione dei dati;
- leggibilità/naming;
- gestione casi limite;
- test/debugging;
- capacità di spiegazione.

## Activity mix suggerito

Per ogni UDA, non necessariamente in uguale quantità:

```text
A Observe/Trace
B Controlled Change
C Implement
D Debug/Diagnose
E Mini-project
F Integrated Product
```

Nel primo quadrimestre prevalgono A/B/C/D. Nel secondo aumentano E e integrazione tra concetti.

## `friedpython`

Il materiale esistente entra soprattutto nelle UDA PY2-07, PY2-08, PY2-09 e PY2-10 dopo audit. Non va copiato in blocco e non determina l'ordine del corso.

## Progetto longitudinale

Ancora da decidere. Romeo è un candidato, ma il secondo anno deve poter completare l'intero percorso anche senza hardware fisico. Qualunque uso di Romeo deve quindi avere un simulatore o boundary che renda il progetto eseguibile in laboratorio/CI/TheBitLab.

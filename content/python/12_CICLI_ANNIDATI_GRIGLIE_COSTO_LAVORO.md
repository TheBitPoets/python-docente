# M12 — Cicli annidati, griglie e costo del lavoro

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-04 — Iterazione e pattern algoritmici  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- leggere un ciclo dentro un altro ciclo;
- distinguere ciclo esterno e ciclo interno;
- eseguire il trace di coppie `(i, j)` su intervalli piccoli;
- determinare quante volte viene eseguito il corpo interno in casi semplici;
- generare tabelle, griglie e pattern rettangolari;
- usare `if` dentro cicli annidati quando il problema lo richiede;
- riconoscere variabili resettate al livello sbagliato;
- distinguere annidamento naturale da lavoro ripetuto inutile;
- spostare fuori dal ciclo calcoli che non dipendono dall'iterazione corrente;
- confrontare intuitivamente una scansione singola con una scansione doppia;
- motivare una soluzione rispetto a correttezza, leggibilità e quantità di lavoro.

---

# 1. Per ogni riga, tutte le colonne

Pensa a una griglia:

```text
R righe
C colonne
```

Per visitare ogni cella possiamo descrivere:

```text
per ogni riga
    per ogni colonna
        visita la cella
```

In Python:

```python
for riga in range(righe):
    for colonna in range(colonne):
        print(riga, colonna)
```

Il ciclo interno completa il proprio percorso **per ogni** valore del ciclo esterno.

---

# 2. Trace delle coppie

Esempio:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

Prima prevedi:

```text
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
```

Tabella:

| iterazione esterna | `i` | `j` visitati |
|---:|---:|---|
| 1 | 0 | 0, 1, 2 |
| 2 | 1 | 0, 1, 2 |

---

# 3. Quante volte viene eseguito il corpo interno?

Se abbiamo:

```text
R valori nel ciclo esterno
C valori nel ciclo interno
```

il corpo interno viene eseguito:

```text
R × C
```

volte.

Esempio:

```text
2 × 3 = 6
```

Non serve ancora il formalismo Big-O per capire che raddoppiare entrambe le dimensioni aumenta molto il lavoro.

---

# 4. Una tabella rettangolare

Problema:

> Stampa una griglia di `righe × colonne` asterischi.

```python
for _ in range(righe):
    for _ in range(colonne):
        print("*", end="")
    print()
```

Per ora `end=""` viene usato come strumento di output, non come nuovo argomento da approfondire.

Modello:

```text
ciclo esterno → cambia riga
ciclo interno → produce le colonne della riga
```

---

# 5. Reset al livello giusto

Supponiamo di voler calcolare un totale per ogni riga.

La variabile che rappresenta **il totale della riga corrente** deve essere azzerata:

```text
una volta per riga
```

non una volta per cella e non una sola volta per tutta la griglia.

Questo è un errore di scope temporale del pattern, anche prima di studiare lo scope formale delle funzioni.

---

# 6. Pattern con condizione dentro due cicli

Problema:

> Stampa `#` sulla diagonale di una piccola griglia quadrata e `.` altrove.

```python
for riga in range(n):
    for colonna in range(n):
        if riga == colonna:
            print("#", end="")
        else:
            print(".", end="")
    print()
```

Qui la selezione dipende dalla coppia corrente `(riga, colonna)`.

---

# 7. Tutte le coppie

Un doppio ciclo è naturale quando il problema chiede di considerare tutte le coppie di due piccoli insiemi di valori.

Esempio:

```python
for i in range(3):
    for j in range(2):
        ...
```

Domanda importante:

> il problema richiede davvero tutte le coppie?

Se no, il doppio ciclo può essere lavoro inutile.

---

# 8. Annidamento naturale vs accidentale

## Naturale

```text
griglia
→ per ogni riga
   → ogni colonna
```

## Accidentale

```text
per ogni valore
    ricalcolo qualcosa che non dipende dal valore corrente
```

Esempio concettuale:

```python
for i in range(n):
    valore_costante = calcolo_che_non_dipende_da_i()
    ...
```

Se il calcolo non cambia:

```python
valore_costante = calcolo_che_non_dipende_da_i()
for i in range(n):
    ...
```

comunica meglio anche l'intenzione.

---

# 9. Quantità di lavoro: primo modello

Con una scansione singola:

```text
N valori
→ circa N elaborazioni
```

Con due cicli entrambi su `N`:

```text
N × N
```

Esempi:

| N | singolo ciclo | doppio ciclo N×N |
|---:|---:|---:|
| 3 | 3 | 9 |
| 10 | 10 | 100 |
| 100 | 100 | 10000 |

Non stiamo ancora studiando formalmente la complessità asintotica.

Stiamo imparando a chiederci:

> quanto lavoro sto facendo e perché?

---

# 10. Ordine dei criteri

Per una soluzione di seconda usiamo questo ordine:

```text
1. correttezza
2. comprensibilità
3. struttura adatta al problema
4. evitare lavoro chiaramente inutile
5. efficienza quando il volume dei dati la rende rilevante
```

Non useremo:

```text
più corto = più veloce
più Pythonico = sempre migliore
```

come regole automatiche.

---

# 11. Worked example: tabellina rettangolare

Specifica:

> Per righe da 1 a 3 e colonne da 1 a 4 stampa il prodotto della coppia corrente.

```python
for riga in range(1, 4):
    for colonna in range(1, 5):
        print(riga * colonna, end=" ")
    print()
```

Prima del codice puoi prevedere:

```text
3 righe
4 colonne
12 prodotti
```

Questa previsione è già ragionamento sulla quantità di lavoro.

---

# 12. Error Clinic

## A — variabile sbagliata

```python
for riga in range(3):
    for colonna in range(4):
        print(riga, riga)
```

Il ciclo interno varia, ma il programma non usa `colonna`.

## B — reset troppo interno

```python
for riga in range(righe):
    for colonna in range(colonne):
        totale_riga = 0
        totale_riga += valore
```

Il totale viene cancellato a ogni cella.

## C — reset troppo esterno

Una variabile che dovrebbe ripartire per ogni riga viene inizializzata una sola volta prima di tutto il doppio ciclo.

## D — indentazione errata

Un `print()` che dovrebbe chiudere la riga finisce dentro il ciclo delle colonne.

## E — lavoro ripetuto

Un valore invariabile viene ricalcolato nel ciclo interno.

---

# 13. Trace di un doppio ciclo

Per:

```python
for i in range(2):
    for j in range(2):
        print(i + j)
```

compila:

| `i` | `j` | `i + j` |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 2 |

Il trace deve mostrare che il ciclo interno riparte da capo a ogni nuova iterazione esterna.

---

# 14. Activity candidate

## A — Nested trace

Elenca tutte le coppie prodotte da due `range` piccoli.

## B — Controlled Change

Cambia da griglia `2×3` a `4×5` e prevedi **prima** quante iterazioni/output saranno prodotti.

## C — Implement

Genera una griglia rettangolare con un pattern condizionale.

## D — Debug

Correggi variabili interne/esterne confuse, reset al livello errato, indentazione e range sbagliati.

## E — Mini-project

Problema con:

- almeno un ciclo;
- almeno una selezione;
- contatore/accumulatore oppure annidamento;
- casi di test progettati prima del codice;
- breve motivazione del costrutto scelto;
- stima semplice del numero di iterazioni principali.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 15. Romeo opzionale

Romeo può usare griglie o sequenze ripetute per visualizzare:

- percorsi rettangolari;
- combinazioni riga/colonna;
- ripetizione di pattern;
- confronto fra comando duplicato e ciclo.

Il simulatore è applicazione, non prerequisito. Hardware fisico resta fuori dal core.

---

# 16. Exit checkpoint PY2-04

Alla fine dell'UDA dovresti saper:

- scegliere `while` o `for` e motivarlo;
- garantire la terminazione di un `while`;
- usare sentinelle e validazione ripetuta;
- usare contatori e accumulatori;
- mantenere min/max progressivi;
- costruire una semplice ricerca/flag;
- combinare selezione e iterazione;
- leggere/scrivere un doppio ciclo semplice;
- stimare il numero di esecuzioni principali in casi piccoli;
- riconoscere lavoro chiaramente ripetuto senza necessità.

---

# 17. Sintesi

```text
ciclo singolo
→ attraversa una dimensione
```

```text
ciclo annidato
→ per ogni valore esterno, percorri quelli interni
```

```text
R × C
→ numero di coppie/celle visitate
```

```text
correttezza
→ comprensibilità
→ struttura adatta
→ niente lavoro chiaramente inutile
→ efficienza quando serve
```

Il prossimo blocco del corso sposta l'attenzione dal controllo del flusso alla **decomposizione in funzioni testabili**.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — `for`, `range`, `if` e controllo del flusso;
- *Think Python / Pensare in Python* — iterazione e debugging;
- *Learning Python / Imparare Python* — reference sistematico;
- Romeo pinned — applicazioni simulate opzionali.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

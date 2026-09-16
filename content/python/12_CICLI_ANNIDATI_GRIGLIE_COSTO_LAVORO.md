# M12 — Cicli annidati, griglie e costo del lavoro

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
I cicli annidati percorrono coppie e griglie e rendono osservabile la quantità di lavoro.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Scrivere cicli con range e usare contatori e accumulatori da M10–M11.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
leggere un ciclo dentro un altro ciclo;<br>distinguere ciclo esterno e ciclo interno;<br>eseguire il trace di coppie <code>(i, j)</code> su intervalli piccoli; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
L&#x27;inizializzazione va collocata al livello corrispondente al significato dello stato. Riprendi <a href="11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md">M11 — Contatori, accumulatori, minimo/massimo, ricerca e flag</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="13_FUNZIONI_PARAMETRI_RETURN.md">M13 — Funzioni produttive: parametri, argomenti e <code>return</code></a>. Le funzioni formalizzano la trasformazione nominata introdotta in M05: parametri in ingresso e risultato restituito.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Elenca le coppie di una griglia 2×3 e verifica che il corpo interno venga eseguito sei volte.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128279;</span> Rimando:</strong>
<a href="../../student/README.md">Indice del percorso studente</a>; <a href="#obiettivi">obiettivi della lezione</a>.
</p>

</details>
</td></tr>
</table>
<!-- COURSE-FRAME:END -->

<blockquote>
<p align="justify"><strong>Stato:</strong> draft editoriale controllato<br>
<strong>UDA:</strong> PY2-04 — Iterazione e pattern algoritmici<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>leggere un ciclo dentro un altro ciclo;</li>
  <li>distinguere ciclo esterno e ciclo interno;</li>
  <li>eseguire il trace di coppie <code>(i, j)</code> su intervalli piccoli;</li>
  <li>determinare quante volte viene eseguito il corpo interno in casi semplici;</li>
  <li>generare tabelle, griglie e pattern rettangolari;</li>
  <li>usare <code>if</code> dentro cicli annidati quando il problema lo richiede;</li>
  <li>riconoscere variabili resettate al livello sbagliato;</li>
  <li>distinguere annidamento naturale da lavoro ripetuto inutile;</li>
  <li>spostare fuori dal ciclo calcoli che non dipendono dall'iterazione corrente;</li>
  <li>confrontare intuitivamente una scansione singola con una scansione doppia;</li>
  <li>motivare una soluzione rispetto a correttezza, leggibilità e quantità di lavoro.</li>
</ul>

---

## 1. Per ogni riga, tutte le colonne

<p align="justify">Pensa a una griglia:</p>

```text
R righe
C colonne
```

<p align="justify">Per visitare ogni cella possiamo descrivere:</p>

```text
per ogni riga
    per ogni colonna
        visita la cella
```

<p align="justify">In Python:</p>

```python
for riga in range(righe):
    for colonna in range(colonne):
        print(riga, colonna)
```

<p align="justify">Il ciclo interno completa il proprio percorso <strong>per ogni</strong> valore del ciclo esterno.</p>

---

## 2. Trace delle coppie

<p align="justify">Esempio:</p>

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

<p align="justify">Prima prevedi:</p>

```text
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
```

<p align="justify">Tabella:</p>

<table align="center">
<thead>
<tr>
<th>iterazione esterna</th>
<th><code>i</code></th>
<th><code>j</code> visitati</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
</tbody>
</table>

---

## 3. Quante volte viene eseguito il corpo interno?

<p align="justify">Se abbiamo:</p>

```text
R valori nel ciclo esterno
C valori nel ciclo interno
```

<p align="justify">il corpo interno viene eseguito:</p>

```text
R × C
```

<p align="justify">volte.</p>

<p align="justify">Esempio:</p>

```text
2 × 3 = 6
```

<p align="justify">Non serve ancora il formalismo Big-O per capire che raddoppiare entrambe le dimensioni aumenta molto il lavoro.</p>

---

## 4. Una tabella rettangolare

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Stampa una griglia di <code>righe × colonne</code> asterischi.</p>
</blockquote>

```python
for _ in range(righe):
    for _ in range(colonne):
        print("*", end="")
    print()
```

<p align="justify">Per ora <code>end=""</code> viene usato come strumento di output, non come nuovo argomento da approfondire.</p>

<p align="justify">Modello:</p>

```text
ciclo esterno → cambia riga
ciclo interno → produce le colonne della riga
```

---

## 5. Reset al livello giusto

<p align="justify">Supponiamo di voler calcolare un totale per ogni riga.</p>

<p align="justify">La variabile che rappresenta <strong>il totale della riga corrente</strong> deve essere azzerata:</p>

```text
una volta per riga
```

<p align="justify">non una volta per cella e non una sola volta per tutta la griglia.</p>

<p align="justify">Questo è un errore di scope temporale del pattern, anche prima di studiare lo scope formale delle funzioni.</p>

---

## 6. Pattern con condizione dentro due cicli

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Stampa <code>#</code> sulla diagonale di una piccola griglia quadrata e <code>.</code> altrove.</p>
</blockquote>

```python
for riga in range(n):
    for colonna in range(n):
        if riga == colonna:
            print("#", end="")
        else:
            print(".", end="")
    print()
```

<p align="justify">Qui la selezione dipende dalla coppia corrente <code>(riga, colonna)</code>.</p>

---

## 7. Tutte le coppie

<p align="justify">Un doppio ciclo è naturale quando il problema chiede di considerare tutte le coppie di due piccoli insiemi di valori.</p>

<p align="justify">Esempio:</p>

```python
for i in range(3):
    for j in range(2):
        ...
```

<p align="justify">Domanda importante:</p>

<blockquote>
<p align="justify">il problema richiede davvero tutte le coppie?</p>
</blockquote>

<p align="justify">Se no, il doppio ciclo può essere lavoro inutile.</p>

---

## 8. Annidamento naturale vs accidentale

### Naturale

```text
griglia
→ per ogni riga
   → ogni colonna
```

### Accidentale

```text
per ogni valore
    ricalcolo qualcosa che non dipende dal valore corrente
```

<p align="justify">Esempio concettuale:</p>

```python
for i in range(n):
    valore_costante = calcolo_che_non_dipende_da_i()
    ...
```

<p align="justify">Se il calcolo non cambia:</p>

```python
valore_costante = calcolo_che_non_dipende_da_i()
for i in range(n):
    ...
```

<p align="justify">comunica meglio anche l'intenzione.</p>

---

## 9. Quantità di lavoro: primo modello

<p align="justify">Con una scansione singola:</p>

```text
N valori
→ circa N elaborazioni
```

<p align="justify">Con due cicli entrambi su <code>N</code>:</p>

```text
N × N
```

<p align="justify">Esempi:</p>

<table align="center">
<thead>
<tr>
<th>N</th>
<th>singolo ciclo</th>
<th>doppio ciclo N×N</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>3</td>
<td>9</td>
</tr>
<tr>
<td>10</td>
<td>10</td>
<td>100</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>10000</td>
</tr>
</tbody>
</table>

<p align="justify">Non stiamo ancora studiando formalmente la complessità asintotica.</p>

<p align="justify">Stiamo imparando a chiederci:</p>

<blockquote>
<p align="justify">quanto lavoro sto facendo e perché?</p>
</blockquote>

---

## 10. Ordine dei criteri

<p align="justify">Per una soluzione di seconda usiamo questo ordine:</p>

```text
1. correttezza
2. comprensibilità
3. struttura adatta al problema
4. evitare lavoro chiaramente inutile
5. efficienza quando il volume dei dati la rende rilevante
```

<p align="justify">Non useremo:</p>

```text
più corto = più veloce
più Pythonico = sempre migliore
```

<p align="justify">come regole automatiche.</p>

---

## 11. Worked example: tabellina rettangolare

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Per righe da 1 a 3 e colonne da 1 a 4 stampa il prodotto della coppia corrente.</p>
</blockquote>

```python
for riga in range(1, 4):
    for colonna in range(1, 5):
        print(riga * colonna, end=" ")
    print()
```

<p align="justify">Prima del codice puoi prevedere:</p>

```text
3 righe
4 colonne
12 prodotti
```

<p align="justify">Questa previsione è già ragionamento sulla quantità di lavoro.</p>

---

## 12. Error Clinic

### A — variabile sbagliata

```python
for riga in range(3):
    for colonna in range(4):
        print(riga, riga)
```

<p align="justify">Il ciclo interno varia, ma il programma non usa <code>colonna</code>.</p>

### B — reset troppo interno

```python
for riga in range(righe):
    for colonna in range(colonne):
        totale_riga = 0
        totale_riga += valore
```

<p align="justify">Il totale viene cancellato a ogni cella.</p>

### C — reset troppo esterno

<p align="justify">Una variabile che dovrebbe ripartire per ogni riga viene inizializzata una sola volta prima di tutto il doppio ciclo.</p>

### D — indentazione errata

<p align="justify">Un <code>print()</code> che dovrebbe chiudere la riga finisce dentro il ciclo delle colonne.</p>

### E — lavoro ripetuto

<p align="justify">Un valore invariabile viene ricalcolato nel ciclo interno.</p>

---

## 13. Trace di un doppio ciclo

<p align="justify">Per:</p>

```python
for i in range(2):
    for j in range(2):
        print(i + j)
```

<p align="justify">compila:</p>

<table align="center">
<thead>
<tr>
<th><code>i</code></th>
<th><code>j</code></th>
<th><code>i + j</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
</tbody>
</table>

<p align="justify">Il trace deve mostrare che il ciclo interno riparte da capo a ogni nuova iterazione esterna.</p>

---

## 14. Activity candidate

### A — Nested trace

<p align="justify">Elenca tutte le coppie prodotte da due <code>range</code> piccoli.</p>

### B — Controlled Change

<p align="justify">Cambia da griglia <code>2×3</code> a <code>4×5</code> e prevedi <strong>prima</strong> quante iterazioni/output saranno prodotti.</p>

### C — Implement

<p align="justify">Genera una griglia rettangolare con un pattern condizionale.</p>

### D — Debug

<p align="justify">Correggi variabili interne/esterne confuse, reset al livello errato, indentazione e range sbagliati.</p>

### E — Mini-project

<p align="justify">Problema con:</p>

<ul>
  <li>almeno un ciclo;</li>
  <li>almeno una selezione;</li>
  <li>contatore/accumulatore oppure annidamento;</li>
  <li>casi di test progettati prima del codice;</li>
  <li>breve motivazione del costrutto scelto;</li>
  <li>stima semplice del numero di iterazioni principali.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 15. Romeo opzionale

<p align="justify">Romeo può usare griglie o sequenze ripetute per visualizzare:</p>

<ul>
  <li>percorsi rettangolari;</li>
  <li>combinazioni riga/colonna;</li>
  <li>ripetizione di pattern;</li>
  <li>confronto fra comando duplicato e ciclo.</li>
</ul>

<p align="justify">Il simulatore è applicazione, non prerequisito. Hardware fisico resta fuori dal core.</p>

---

## 16. Exit checkpoint PY2-04

<p align="justify">Alla fine dell'UDA dovresti saper:</p>

<ul>
  <li>scegliere <code>while</code> o <code>for</code> e motivarlo;</li>
  <li>garantire la terminazione di un <code>while</code>;</li>
  <li>usare sentinelle e validazione ripetuta;</li>
  <li>usare contatori e accumulatori;</li>
  <li>mantenere min/max progressivi;</li>
  <li>costruire una semplice ricerca/flag;</li>
  <li>combinare selezione e iterazione;</li>
  <li>leggere/scrivere un doppio ciclo semplice;</li>
  <li>stimare il numero di esecuzioni principali in casi piccoli;</li>
  <li>riconoscere lavoro chiaramente ripetuto senza necessità.</li>
</ul>

---

## 17. Sintesi

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

<p align="justify">Il prossimo blocco del corso sposta l'attenzione dal controllo del flusso alla <strong>decomposizione in funzioni testabili</strong>.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — <code>for</code>, <code>range</code>, <code>if</code> e controllo del flusso;</li>
  <li><em>Think Python / Pensare in Python</em> — iterazione e debugging;</li>
  <li><em>Learning Python / Imparare Python</em> — reference sistematico;</li>
  <li>Romeo pinned — applicazioni simulate opzionali.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

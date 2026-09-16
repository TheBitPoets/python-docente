# M11 — Contatori, accumulatori, minimo/massimo, ricerca e flag

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Contatori, accumulatori e flag descrivono che cosa ricordare durante un&#x27;elaborazione iterativa.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare for/while e selezioni e seguire l&#x27;aggiornamento delle variabili da M09–M10.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
riconoscere quando un problema richiede un contatore oppure un accumulatore;<br>usare <code>if</code> dentro <code>for</code> e <code>while</code> per elaborare solo i casi rilevanti;<br>mantenere una somma progressiva e ricavarne una media quando il conteggio è valido; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Una variabile di stato deve avere un significato che puoi spiegare dopo ogni iterazione. Riprendi <a href="10_FOR_RANGE_SCELTA_CICLO.md">M10 — <code>for</code>, <code>range</code> e scelta <code>for</code> vs <code>while</code></a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md">M12 — Cicli annidati, griglie e costo del lavoro</a>. I cicli annidati percorrono coppie e griglie e rendono osservabile la quantità di lavoro.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia conteggio e somma dei positivi; verifica il caso senza positivi prima di calcolare la media.
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
  <li>riconoscere quando un problema richiede un contatore oppure un accumulatore;</li>
  <li>usare <code>if</code> dentro <code>for</code> e <code>while</code> per elaborare solo i casi rilevanti;</li>
  <li>mantenere una somma progressiva e ricavarne una media quando il conteggio è valido;</li>
  <li>mantenere un minimo o un massimo progressivo senza usare valori-sentinella arbitrari;</li>
  <li>distinguere “trova il primo” da “conta/trova tutti”;</li>
  <li>usare un flag booleano quando rappresenta davvero uno stato utile;</li>
  <li>riconoscere quando un flag è ridondante;</li>
  <li>progettare casi di test per nessun match, un match, più match e confini significativi;</li>
  <li>descrivere con una frase che cosa rappresenta una variabile durante il ciclo.</li>
</ul>

---

## 1. Il problema non è il ciclo: è che cosa devo ricordare

<p align="justify">Considera una sequenza di valori:</p>

```text
4  -2  7  0  5
```

<p align="justify">Potremmo voler sapere:</p>

<ul>
  <li>quanti sono positivi;</li>
  <li>qual è la loro somma;</li>
  <li>qual è il valore più piccolo;</li>
  <li>se compare almeno uno zero;</li>
  <li>dove si trova il primo valore maggiore di 6.</li>
</ul>

<p align="justify">Il ciclo attraversa i dati. La parte importante è capire <strong>quale informazione deve sopravvivere da un'iterazione alla successiva</strong>.</p>

<p align="justify">Modello:</p>

```text
valore corrente
      ↓
condizione / elaborazione
      ↓
stato aggiornato
      ↓
iterazione successiva
```

<p align="justify">Quello stato può essere un contatore, un totale, un minimo, un massimo, un flag o un risultato di ricerca.</p>

---

## 2. Pattern contatore

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi <code>N</code> valori e conta quanti sono positivi.</p>
</blockquote>

<p align="justify">Una forma tipica è:</p>

```python
conteggio = 0

for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1

print(conteggio)
```

### Invariante intuitivo

<p align="justify">Dopo ogni iterazione:</p>

<blockquote>
<p align="justify"><code>conteggio</code> è il numero di valori positivi già elaborati.</p>
</blockquote>

<p align="justify">Questa frase ci permette di controllare il programma.</p>

<p align="justify">Se <code>conteggio += 1</code> fosse fuori dall'<code>if</code>, la frase non sarebbe più vera.</p>

### Trace

<p align="justify">Per i valori:</p>

```text
4, -2, 7
```

<table align="center">
<thead>
<tr>
<th>valore</th>
<th><code>valore &gt; 0</code></th>
<th><code>conteggio</code> dopo l'iterazione</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td>True</td>
<td>1</td>
</tr>
<tr>
<td>-2</td>
<td>False</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>True</td>
<td>2</td>
</tr>
</tbody>
</table>

---

## 3. Pattern accumulatore

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Calcola la somma di <code>N</code> valori.</p>
</blockquote>

```python
totale = 0

for _ in range(n):
    valore = int(input())
    totale += valore

print(totale)
```

### Invariante

<blockquote>
<p align="justify"><code>totale</code> è la somma dei valori già elaborati.</p>
</blockquote>

<p align="justify">Questa frase spiega perché <code>totale</code> deve essere inizializzato <strong>prima</strong> del ciclo.</p>

<p align="justify">Errore classico:</p>

```python
for _ in range(n):
    totale = 0
    valore = int(input())
    totale += valore
```

<p align="justify">Qui il totale viene azzerato a ogni iterazione.</p>

---

## 4. Contatore + accumulatore: la media

<p align="justify">Per una media servono almeno:</p>

```text
somma
conteggio
```

<p align="justify">Se il numero di valori è noto e tutti sono validi:</p>

```python
totale = 0

for _ in range(n):
    totale += int(input())

media = totale / n
```

<p align="justify">Ma se contiamo soltanto i valori che soddisfano una condizione:</p>

```python
totale = 0
conteggio = 0

for _ in range(n):
    valore = int(input())
    if valore >= 0:
        totale += valore
        conteggio += 1
```

<p align="justify">prima della divisione dobbiamo chiederci:</p>

<blockquote>
<p align="justify"><code>conteggio</code> può essere zero?</p>
</blockquote>

<p align="justify">Una soluzione deve gestire esplicitamente quel caso.</p>

---

## 5. Minimo e massimo progressivo

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Tra più valori trova il minimo.</p>
</blockquote>

<p align="justify">Una cattiva abitudine è inventare una sentinella numerica:</p>

```python
minimo = 999999
```

<p align="justify">Funziona soltanto se il dominio garantisce che nessun valore possa essere maggiore o uguale a quella scelta. Se il dominio cambia, il programma può diventare sbagliato.</p>

### Strategia robusta con primo dato

<p align="justify">Se sappiamo che esiste almeno un valore:</p>

```python
minimo = int(input())

for _ in range(n - 1):
    valore = int(input())
    if valore < minimo:
        minimo = valore

print(minimo)
```

### Invariante

<blockquote>
<p align="justify"><code>minimo</code> è il più piccolo valore visto finora.</p>
</blockquote>

<p align="justify">Per il massimo:</p>

<blockquote>
<p align="justify"><code>massimo</code> è il più grande valore visto finora.</p>
</blockquote>

<p align="justify">Queste frasi sono più importanti della forma esatta del codice.</p>

---

## 6. Ricerca: primo match oppure tutti i match?

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">Tra i valori compare almeno un numero uguale a 0?</p>
</blockquote>

<p align="justify">Se ci interessa soltanto sapere se esiste, possiamo fermarci al primo match.</p>

<p align="justify">Esempio concettuale:</p>

```python
trovato = False

for _ in range(n):
    valore = int(input())
    if valore == 0:
        trovato = True
```

<p align="justify">Al termine:</p>

```python
if trovato:
    print("presente")
else:
    print("assente")
```

### Ma devo davvero leggere tutti i valori?

<p align="justify">Dipende dal contratto del problema.</p>

<p align="justify">Se i dati arrivano da una struttura già disponibile, una ricerca del primo match può fermarsi con <code>break</code>.</p>

<p align="justify">Se i dati arrivano uno alla volta da input e il contratto richiede comunque di consumarli tutti, il comportamento può essere diverso.</p>

<p align="justify">Il pattern non si sceglie isolatamente: dipende dall'interfaccia e dall'obiettivo.</p>

---

## 7. Flag booleani

<p align="justify">Un flag è una variabile booleana che rappresenta uno stato significativo.</p>

<p align="justify">Esempio:</p>

```python
trovato = False
```

<p align="justify">Invariante:</p>

<blockquote>
<p align="justify"><code>trovato</code> indica se finora abbiamo incontrato almeno un valore che soddisfa la ricerca.</p>
</blockquote>

### Flag utile

<p align="justify">Quando il valore booleano viene usato dopo il ciclo o rappresenta chiaramente uno stato.</p>

### Flag ridondante

<p align="justify">Se serve solo per imitare una condizione già disponibile o se un <code>break</code>/<code>return</code> futuro renderebbe il flusso più diretto.</p>

<p align="justify">Non esiste la regola “i flag sono sbagliati”. La domanda è:</p>

<blockquote>
<p align="justify">questa variabile aggiunge significato o aggiunge soltanto meccanica?</p>
</blockquote>

---

## 8. Selezione dentro iterazione

<p align="justify">Molti algoritmi combinano:</p>

```text
ripeti
→ osserva un valore
→ decidi se interessa
→ aggiorna lo stato
```

<p align="justify">Esempio: conta quanti valori sono compresi tra 10 e 20 inclusi.</p>

```python
conteggio = 0

for _ in range(n):
    valore = int(input())
    if 10 <= valore <= 20:
        conteggio += 1
```

<p align="justify">Questo è un uso naturale di <code>if</code> dentro <code>for</code>.</p>

---

## 9. Ciclo dentro una decisione

<p align="justify">Anche il contrario può essere naturale:</p>

```python
if n > 0:
    for _ in range(n):
        ...
else:
    print("nessun dato")
```

<p align="justify">Il punto non è collezionare combinazioni sintattiche.</p>

<p align="justify">La domanda resta:</p>

<blockquote>
<p align="justify">la struttura rappresenta davvero il problema?</p>
</blockquote>

---

## 10. Worked example: statistiche sui valori positivi

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Leggi <code>N</code> interi. Stampa quanti sono positivi e la loro somma.</p>
</blockquote>

<p align="justify">Casi da progettare prima:</p>

<table align="center">
<thead>
<tr>
<th>valori</th>
<th>positivi</th>
<th>somma positiva</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2, 5, -1</code></td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><code>-3, 0, -2</code></td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><code>4</code></td>
<td>1</td>
<td>4</td>
</tr>
</tbody>
</table>

<p align="justify">Codice:</p>

```python
n = int(input())
conteggio = 0
totale = 0

for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1
        totale += valore

print(conteggio)
print(totale)
```

<p align="justify">Invarianti:</p>

```text
conteggio = numero di positivi già visti
totale    = somma dei positivi già visti
```

---

## 11. Error Clinic

### A — accumulatore resettato

```python
for _ in range(n):
    totale = 0
    totale += int(input())
```

<p align="justify">Domanda: quale invariante viene distrutto?</p>

### B — contatore incrementato sempre

```python
if valore > 0:
    print(valore)
conteggio += 1
```

<p align="justify">Se volevamo contare soltanto i positivi, l'aggiornamento è nel livello sbagliato.</p>

### C — media con denominatore zero

```python
media = totale / conteggio
```

<p align="justify">Quale caso di test lo mette in crisi?</p>

### D — minimo sentinella fragile

```python
minimo = 999999
```

<p align="justify">Quale assunzione nascosta stiamo facendo?</p>

### E — flag mai aggiornato

```python
trovato = False
for ...:
    if condizione:
        print("trovato")
```

<p align="justify">Dopo il ciclo <code>trovato</code> è ancora <code>False</code>.</p>

---

## 12. Ricerca lineare: ragionare sul lavoro

<p align="justify">Se controlliamo i valori uno dopo l'altro, nel caso peggiore possiamo doverli esaminare tutti.</p>

<p align="justify">Per ora basta questa intuizione:</p>

```text
più dati
→ più confronti
```

<p align="justify">Non introduciamo ancora il formalismo Big-O.</p>

<p align="justify">Ma iniziamo a distinguere:</p>

<ul>
  <li>ricerca del primo match;</li>
  <li>conteggio di tutti i match;</li>
  <li>elaborazione completa obbligatoria.</li>
</ul>

<p align="justify">Queste tre richieste possono produrre algoritmi diversi.</p>

---

## 13. Activity candidate

### A — Trace pattern

<p align="justify">Completa tabelle con <code>conteggio</code>, <code>totale</code>, <code>minimo</code> e <code>trovato</code> dopo ogni iterazione.</p>

### B — Controlled Change

<p align="justify">Trasforma “conta positivi” in “conta valori nell'intervallo <code>[10, 20]</code>”, aggiornando prima i casi di test.</p>

### C — Implement

<p align="justify">Leggi <code>N</code> dati e calcola:</p>

<ul>
  <li>somma;</li>
  <li>conteggio di quelli validi;</li>
  <li>eventuale media solo se il conteggio è diverso da zero.</li>
</ul>

### D — Debug

<p align="justify">Correggi accumulatori resettati, update fuori dal ramo, minimo inizializzato male e flag incoerenti.</p>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo P1 canarino non è certificato.</p>

---

## 14. Romeo come applicazione selettiva

<p align="justify">Una missione simulata può richiedere di:</p>

<ul>
  <li>contare quante azioni soddisfano una condizione;</li>
  <li>accumulare una distanza/tempo concettuale;</li>
  <li>rilevare se un checkpoint è stato raggiunto;</li>
  <li>fermare una ricerca quando l'obiettivo è trovato.</li>
</ul>

<p align="justify">Romeo non sostituisce gli esercizi generali e non introduce hardware fisico nel core.</p>

---

## 15. Checkpoint

<p align="justify">Dovresti saper spiegare senza eseguire il codice:</p>

<ol>
  <li>differenza tra contatore e accumulatore;</li>
  <li>perché un accumulatore si inizializza prima del ciclo;</li>
  <li>perché <code>minimo = 999999</code> può essere fragile;</li>
  <li>quale invariante rappresenta un minimo progressivo;</li>
  <li>differenza tra “trova il primo” e “conta tutti”;</li>
  <li>quando un flag aggiunge significato;</li>
  <li>quale test protegge una media da divisione per zero.</li>
</ol>

---

## 16. Sintesi

```text
ciclo = attraversa/ripete
stato = ricorda ciò che serve
```

```text
contatore    → quanti?
accumulatore → quanto in totale?
min/max      → estremo visto finora
flag         → stato sì/no
ricerca      → primo / esiste / tutti?
```

<p align="justify">La domanda di debugging più potente del modulo è:</p>

<blockquote>
<p align="justify">quale frase dovrebbe essere vera su questa variabile dopo ogni iterazione?</p>
</blockquote>

<p align="justify">Nel prossimo modulo useremo più cicli insieme e inizieremo a ragionare su griglie, coppie di indici e quantità di lavoro svolto.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — <code>for</code>, <code>while</code>, <code>if</code>, <code>break</code> e semantica di base;</li>
  <li><em>Think Python / Pensare in Python</em> — iterazione, accumulator patterns e debugging;</li>
  <li><em>Learning Python / Imparare Python</em> — controllo del flusso come reference di copertura;</li>
  <li>Romeo pinned — dominio applicativo opzionale.</li>
</ul>

<p align="justify">Le fonti licensed sono riferimenti, non testo da riprodurre.</p>

# M10 — `for`, `range` e scelta `for` vs `while`

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il for attraversa valori; range rende espliciti inizio, limite escluso e passo.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Tracciare un ciclo e motivarne la terminazione come in M09.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
usare <code>for</code> con <code>range</code>;<br>prevedere i valori prodotti da <code>range(stop)</code>, <code>range(start, stop)</code> e <code>range(start, stop, step)</code>;<br>ricordare che il limite finale di <code>range</code> è escluso; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Scegli il ciclo in base all&#x27;intenzione: attraversare valori oppure attendere il cambiamento di una condizione. Riprendi <a href="09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md">M09 — <code>while</code>, stato, sentinelle e validazione ripetuta</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="11_CONTATORI_ACCUMULATORI_RICERCA_FLAG.md">M11 — Contatori, accumulatori, minimo/massimo, ricerca e flag</a>. Contatori, accumulatori e flag descrivono che cosa ricordare durante un&#x27;elaborazione iterativa.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Elenca prima a mano i valori di tre range, compreso un countdown, e verifica quante iterazioni producono.
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
<p align="justify"><strong>Stato:</strong> draft / controlled authoring continuation<br>
<strong>UDA:</strong> PY2-04 — Iterazione e pattern algoritmici<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>usare <code>for</code> con <code>range</code>;</li>
  <li>prevedere i valori prodotti da <code>range(stop)</code>, <code>range(start, stop)</code> e <code>range(start, stop, step)</code>;</li>
  <li>ricordare che il limite finale di <code>range</code> è escluso;</li>
  <li>contare avanti e indietro con step appropriato;</li>
  <li>riconoscere un <code>range</code> vuoto;</li>
  <li>spiegare quante iterazioni produce un semplice <code>range</code>;</li>
  <li>scegliere <code>for</code> quando l'insieme/numero di iterazioni è noto o naturalmente attraversabile;</li>
  <li>scegliere <code>while</code> quando la durata dipende da una condizione dinamica;</li>
  <li>riscrivere un semplice <code>while</code> contatore come <code>for</code> e confrontare le due versioni;</li>
  <li>usare <code>break</code> e <code>continue</code> con disciplina, soltanto quando chiariscono il flusso;</li>
  <li>diagnosticare off-by-one, stop errato, step errato e contatori manuali inutili.</li>
</ul>

## Prerequisiti

<p align="justify">Da M09 dovresti già saper:</p>

<ul>
  <li>leggere un <code>while</code> come stato + condizione + aggiornamento;</li>
  <li>fare trace di un ciclo;</li>
  <li>spiegare la terminazione;</li>
  <li>riconoscere zero/una/più iterazioni;</li>
  <li>usare validazione ripetuta e sentinella.</li>
</ul>

---

## 1. Problema iniziale: stampa esattamente cinque valori

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Stampa i numeri da 0 a 4.</p>
</blockquote>

<p align="justify">Con <code>while</code> possiamo scrivere:</p>

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

<p align="justify">È corretto.</p>

<p align="justify">Ma qui conosciamo già esattamente i valori da attraversare:</p>

```text
0, 1, 2, 3, 4
```

<p align="justify">Python offre una struttura che comunica direttamente questa intenzione:</p>

```python
for i in range(5):
    print(i)
```

---

## 2. Modello del `for`

<p align="justify">Nel nostro primo uso:</p>

```python
for i in range(5):
    print(i)
```

<p align="justify">puoi leggere:</p>

```text
per ogni valore i prodotto da range(5)
    esegui il corpo
```

<p align="justify">A differenza del <code>while</code>, non gestiamo manualmente:</p>

```text
inizializzazione del contatore
condizione sul contatore
incremento del contatore
```

<p align="justify">quando tutto ciò è già espresso da <code>range</code>.</p>

---

## 3. `range(stop)`

```python
range(5)
```

<p align="justify">produce concettualmente:</p>

```text
0, 1, 2, 3, 4
```

<p align="justify">Il valore <code>5</code> non è incluso.</p>

<p align="justify">Questa è una regola fondamentale:</p>

<blockquote>
<p align="justify">lo <code>stop</code> è escluso.</p>
</blockquote>

<p align="justify">Per vedere i valori nel REPL puoi usare temporaneamente:</p>

```python
list(range(5))
```

<p align="justify">La lista qui è soltanto una lente di osservazione: studieremo le liste formalmente più avanti.</p>

---

## 4. `range(start, stop)`

```python
range(2, 6)
```

<p align="justify">produce:</p>

```text
2, 3, 4, 5
```

<p align="justify">Modello:</p>

```text
start incluso
stop escluso
step predefinito = +1
```

<p align="justify">Prima di eseguire un <code>range</code>, chiediti sempre:</p>

```text
primo valore?
ultimo valore effettivo?
quanti valori?
```

---

## 5. `range(start, stop, step)`

```python
range(2, 10, 2)
```

<p align="justify">produce:</p>

```text
2, 4, 6, 8
```

<p align="justify">Lo step indica come cambia il valore a ogni passo.</p>

<p align="justify">Esempio decrescente:</p>

```python
range(5, 0, -1)
```

<p align="justify">produce:</p>

```text
5, 4, 3, 2, 1
```

<p align="justify">Per scendere serve uno step negativo.</p>

---

## 6. Range vuoto

```python
range(5, 0)
```

<p align="justify">con lo step predefinito <code>+1</code> non produce valori.</p>

<p align="justify">Perché?</p>

<p align="justify">Partendo da 5 e aumentando, non possiamo avvicinarci allo stop 0 nel verso richiesto.</p>

<p align="justify">Invece:</p>

```python
range(5, 0, -1)
```

<p align="justify">ha senso per un countdown.</p>

<p align="justify">Un ciclo <code>for</code> su un range vuoto esegue il corpo zero volte.</p>

---

## 7. Off-by-one: il confine conta

<p align="justify">Obiettivo:</p>

<blockquote>
<p align="justify">stampa 1, 2, 3, 4, 5.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
for i in range(1, 5):
    print(i)
```

<p align="justify">Output:</p>

```text
1, 2, 3, 4
```

<p align="justify">Per includere 5:</p>

```python
range(1, 6)
```

<p align="justify">Non memorizzare “aggiungi sempre 1”: ragiona sul fatto che lo stop è escluso.</p>

---

## 8. Trace di un `for`

```python
for i in range(2, 5):
    print(i * 10)
```

<table align="center">
<thead>
<tr>
<th>iterazione</th>
<th><code>i</code></th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>2</td>
<td>20</td>
</tr>
<tr>
<td>2</td>
<td>3</td>
<td>30</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>40</td>
</tr>
</tbody>
</table>

<p align="justify">Dopo l'ultimo valore del range, il ciclo termina.</p>

<p align="justify">Non serve aggiornare manualmente <code>i</code>.</p>

---

## 9. `for` vs `while`: stessa possibilità, intenzione diversa

<p align="justify">Versione <code>while</code>:</p>

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

<p align="justify">Versione <code>for</code>:</p>

```python
for i in range(5):
    print(i)
```

<p align="justify">Entrambe sono corrette.</p>

<p align="justify">Nel problema “attraversa i valori 0..4” la versione <code>for</code> comunica meglio:</p>

```text
so già quali valori devo visitare
```

<p align="justify">e riduce il rischio di dimenticare l'aggiornamento.</p>

---

## 10. Modello di scelta

### Preferisci `for` quando

```text
conosci i valori/iterazioni da attraversare
```

<p align="justify">Esempi:</p>

<ul>
  <li>ripeti N volte;</li>
  <li>attraversa un intervallo;</li>
  <li>più avanti: attraversa elementi di una sequenza.</li>
</ul>

### Preferisci `while` quando

```text
continui finché una condizione dipendente dallo stato resta vera
```

<p align="justify">Esempi:</p>

<ul>
  <li>input finché valido;</li>
  <li>continua fino a sentinella;</li>
  <li>ripeti finché una condizione dinamica cambia.</li>
</ul>

<p align="justify">Non è una regola assoluta di sintassi: è un criterio di comunicazione dell'algoritmo.</p>

---

## 11. Microscope: `for` o `while`?

<p align="justify">Per ogni problema scegli prima il costrutto e motiva in una frase.</p>

<ol>
  <li>stampa i numeri 1..10;</li>
  <li>chiedi un voto finché è valido;</li>
  <li>ripeti una trasformazione esattamente 8 volte;</li>
  <li>leggi dati fino alla sentinella <code>-1</code>;</li>
  <li>countdown da 10 a 1;</li>
  <li>continua finché il saldo è negativo e arrivano nuovi versamenti.</li>
</ol>

<p align="justify">Il voto non dipende soltanto dalla scelta corretta, ma dalla motivazione.</p>

---

## 12. Non duplicare il contatore dentro un `for`

<p align="justify">Codice sospetto:</p>

```python
contatore = 0
for i in range(5):
    print(contatore)
    contatore += 1
```

<p align="justify">Se <code>contatore</code> serve soltanto a replicare esattamente <code>i</code>, abbiamo introdotto stato ridondante.</p>

<p align="justify">Può bastare:</p>

```python
for i in range(5):
    print(i)
```

<p align="justify">Un contatore separato è corretto quando rappresenta <strong>un'altra quantità</strong>, per esempio quanti valori soddisfano una condizione; questo sarà M11.</p>

---

## 13. Countdown

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">stampa 5, 4, 3, 2, 1.</p>
</blockquote>

```python
for i in range(5, 0, -1):
    print(i)
```

<p align="justify">Domande:</p>

```text
start = ?
stop escluso = ?
step = ?
ultimo valore effettivo = ?
```

<p align="justify">Per includere <code>0</code> dovremmo modificare lo stop.</p>

---

## 14. `break`: interrompere quando l'obiettivo è già raggiunto

<p align="justify">Esempio controllato:</p>

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

<p align="justify"><code>break</code> interrompe il ciclo corrente.</p>

<p align="justify">Non è obbligatorio usare <code>break</code> ogni volta che esiste una condizione di stop. Lo usiamo quando rende il flusso più diretto e il motivo dell'interruzione è chiaro.</p>

<p align="justify">In M11 lo vedremo nel pattern “trova il primo elemento”.</p>

---

## 15. `continue`: passa all'iterazione successiva

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

<p align="justify">Quando <code>i == 2</code>, il resto del corpo viene saltato e il <code>for</code> passa al valore successivo.</p>

<p align="justify">Regola didattica:</p>

<blockquote>
<p align="justify">non usare <code>continue</code> per evitare di strutturare una condizione leggibile.</p>
</blockquote>

<p align="justify">Confronta sempre con una versione basata su <code>if</code> normale.</p>

---

## 16. Error Clinic: stop incluso per errore

<p align="justify">Obiettivo:</p>

```text
0, 1, 2, 3, 4
```

<p align="justify">Bug:</p>

```python
for i in range(6):
    print(i)
```

<p align="justify">Produce anche <code>5</code>.</p>

<p align="justify">Prima di cambiare codice, scrivi la sequenza prevista.</p>

---

## 17. Error Clinic: step nel verso sbagliato

<p align="justify">Bug:</p>

```python
for i in range(5, 0, 1):
    print(i)
```

<p align="justify">Il range è vuoto.</p>

<p align="justify">Se start &gt; stop e vogliamo scendere, lo step deve essere negativo.</p>

---

## 18. Error Clinic: `while` manuale quando `for` comunica meglio

```python
i = 0
while i < 100:
    elabora(i)
    i += 1
```

<p align="justify">Può essere corretto.</p>

<p align="justify">Ma se l'unico scopo dello stato <code>i</code> è attraversare 0..99, confronta con:</p>

```python
for i in range(100):
    elabora(i)
```

<p align="justify">Il refactoring elimina gestione manuale non necessaria.</p>

---

## 19. Romeo: ripetere una missione a numero noto

<p align="justify">Romeo è un'applicazione naturale del <code>for</code>.</p>

<p align="justify">Esempio concettuale:</p>

<blockquote>
<p align="justify">ripeti quattro volte il comando necessario per un lato/una rotazione e costruisci una missione quadrata.</p>
</blockquote>

<p align="justify">Il repo Romeo pinned contiene attività <code>for</code> coerenti con questo livello, tra cui:</p>

```text
romeo-y1-u15-ciclo-for
```

<p align="justify">Prima risolvi problemi generali con <code>range</code>; il simulatore viene dopo e solo quando <code>romeo-sim</code> è certificato.</p>

---

## 20. Activity planning — M10

<p align="justify">Candidati, senza nuova Activity P1 materializzata:</p>

#### A — Range microscope

<p align="justify">Prevedere i valori di diversi <code>range</code> senza eseguire.</p>

#### B — `for` o `while`?

<p align="justify">Classificare problemi e motivare la scelta.</p>

#### C — Implement

<p align="justify">Countdown, ripetizione N volte, serie di trasformazioni semplici.</p>

#### D — Debug

<p align="justify">Correggere:</p>

<ul>
  <li>stop errato;</li>
  <li>step errato;</li>
  <li>range vuoto;</li>
  <li>off-by-one;</li>
  <li>contatore manuale duplicato;</li>
  <li><code>break</code>/<code>continue</code> usati senza necessità.</li>
</ul>

<p align="justify">M04 resta il canarino P1 fino a certificazione.</p>

---

## 21. Esercizi brevi

### A — Prevedi il range

<p align="justify">Scrivi la sequenza prodotta da:</p>

```python
range(4)
range(2, 6)
range(1, 8, 2)
range(5, 0, -1)
range(5, 0)
```

### B — Ripeti N volte

<p align="justify">Leggi <code>n</code> e stampa <code>ciao</code> esattamente <code>n</code> volte per <code>n &gt;= 0</code>.</p>

### C — Countdown

<p align="justify">Stampa da <code>n</code> a <code>1</code> con <code>for</code> e <code>range</code>.</p>

### D — Refactoring

<p align="justify">Ricevi un <code>while</code> contatore corretto e riscrivilo con <code>for</code>. Spiega quale gestione manuale hai eliminato.</p>

---

## 22. Checkpoint M10

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Che valori produce <code>range(5)</code>?</li>
  <li>Perché lo stop non viene incluso?</li>
  <li>Che produce <code>range(2, 6, 2)</code>?</li>
  <li>Perché <code>range(5, 0)</code> è vuoto?</li>
  <li>Quando <code>for</code> comunica meglio l'algoritmo rispetto a <code>while</code>?</li>
  <li>Quando <code>while</code> resta la scelta naturale?</li>
  <li>Perché aggiungere un contatore che duplica <code>i</code> può essere inutile?</li>
  <li>Che cosa fa <code>break</code>?</li>
  <li>Che cosa fa <code>continue</code>?</li>
  <li>Perché non li usiamo come scorciatoie automatiche?</li>
</ol>

---

## 23. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
for → so quali valori/iterazioni attraversare
```

```text
range → start incluso, stop escluso, step controlla il verso
```

```text
while → durata dipendente dallo stato
```

```text
scelta del ciclo → comunica il modello del problema
```

<p align="justify">Nel prossimo modulo metteremo <code>if</code> dentro i cicli e impareremo pattern fondamentali: contatori, accumulatori, minimo/massimo progressivo, ricerca e flag.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione/verifica:</p>

<ul>
  <li>documentazione Python 3.12 — <code>for</code>, <code>range</code>, <code>break</code>, <code>continue</code> e control flow;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — iteration e debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — loop semantics;</li>
  <li>Romeo pinned <code>45e5f7e131802fccc89358a23a25dbed1884bbfa</code> — <code>y1-u15-ciclo-for</code> come riferimento applicativo.</li>
</ul>

### Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_04_SPEC.md</code>;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>.</li>
</ul>

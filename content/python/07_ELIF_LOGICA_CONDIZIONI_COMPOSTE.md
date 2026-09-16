# M07 — `elif`, casi esclusivi e condizioni composte

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Più casi richiedono di distinguere alternative esclusive e condizioni indipendenti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare confronti e if/else e verificare una soglia come in M06.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
costruire una catena <code>if/elif/else</code> con più casi;<br>spiegare che in una catena viene eseguito il <strong>primo ramo vero</strong>;<br>distinguere più <code>if</code> indipendenti da casi mutuamente esclusivi; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Un confronto produce un booleano; and, or e not combinano condizioni già comprensibili. Riprendi <a href="06_BOOLEANI_CONFRONTI_IF.md">M06 — Booleani, confronti e prima selezione con <code>if</code></a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md">M08 — Selezioni annidate, validazione e refactoring</a>. La validazione stabilisce quando una seconda decisione ha senso e guida un refactoring verificabile.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia la classificazione del voto e confrontala con più if indipendenti sugli stessi valori di frontiera.
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
<strong>UDA:</strong> PY2-03 — Selezione e logica<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>costruire una catena <code>if/elif/else</code> con più casi;</li>
  <li>spiegare che in una catena viene eseguito il <strong>primo ramo vero</strong>;</li>
  <li>distinguere più <code>if</code> indipendenti da casi mutuamente esclusivi;</li>
  <li>usare <code>and</code>, <code>or</code>, <code>not</code> in condizioni semplici;</li>
  <li>leggere una piccola tabella di verità;</li>
  <li>esprimere intervalli numerici in modo corretto;</li>
  <li>comprendere la forma concatenata <code>a &lt;= x &lt;= b</code> dopo aver compreso la forma con <code>and</code>;</li>
  <li>progettare un test per ogni ramo e per ogni confine importante;</li>
  <li>individuare soglie nell'ordine sbagliato, rami irraggiungibili e condizioni sovrapposte;</li>
  <li>spiegare perché una soluzione usa <code>elif</code> oppure più <code>if</code>.</li>
</ul>

## Prerequisiti

<p align="justify">Da M06 dovresti già saper:</p>

<ul>
  <li>valutare confronti semplici;</li>
  <li>usare <code>if</code> e <code>if/else</code>;</li>
  <li>distinguere <code>=</code> e <code>==</code>;</li>
  <li>fare il trace di un ramo;</li>
  <li>testare una soglia sotto/sulla/sopra;</li>
  <li>comprendere l'indentazione come struttura del blocco.</li>
</ul>

---

## 1. Problema iniziale: classificare un voto

<p align="justify">Specifica:</p>

```text
voto < 6      → insufficiente
6 <= voto < 8 → buono
voto >= 8     → ottimo
```

<p align="justify">I tre casi si escludono a vicenda: per un singolo voto vogliamo <strong>una sola classificazione</strong>.</p>

<p align="justify">Possiamo descrivere la decisione così:</p>

```text
voto < 6 ?
   sì → insufficiente
   no → voto < 8 ?
           sì → buono
           no → ottimo
```

<p align="justify">In Python questa struttura si esprime naturalmente con:</p>

```python
if voto < 6:
    print("insufficiente")
elif voto < 8:
    print("buono")
else:
    print("ottimo")
```

---

## 2. `elif` significa “altrimenti, se…”

<p align="justify">Una catena:</p>

```python
if condizione_1:
    ...
elif condizione_2:
    ...
else:
    ...
```

<p align="justify">si legge concettualmente:</p>

```text
se condizione_1 è vera
    esegui ramo 1
altrimenti, se condizione_2 è vera
    esegui ramo 2
altrimenti
    esegui ramo finale
```

<p align="justify">Punto fondamentale:</p>

<blockquote>
<p align="justify">dopo il primo ramo vero, gli altri rami della stessa catena non vengono più scelti.</p>
</blockquote>

---

## 3. Trace della catena: il primo ramo vero vince

<p align="justify">Programma:</p>

```python
voto = int(input())

if voto < 6:
    print("insufficiente")
elif voto < 8:
    print("buono")
else:
    print("ottimo")
```

## Caso `5`

```text
voto < 6 → True
ramo 1   → eseguito
resto catena → saltato
```

## Caso `7`

```text
voto < 6 → False
voto < 8 → True
ramo 2   → eseguito
else     → saltato
```

## Caso `9`

```text
voto < 6 → False
voto < 8 → False
else     → eseguito
```

---

## 4. Perché nel secondo `elif` basta `voto < 8`?

<p align="justify">La specifica del caso centrale è:</p>

```text
6 <= voto < 8
```

<p align="justify">Eppure il codice usa:</p>

```python
elif voto < 8:
```

<p align="justify">Perché?</p>

<p align="justify">Se siamo arrivati a quell'<code>elif</code>, sappiamo già che:</p>

```python
voto < 6
```

<p align="justify">è falso.</p>

<p align="justify">Quindi il voto è già almeno 6.</p>

<p align="justify">Il contesto creato dai rami precedenti può rendere inutile ripetere una parte della condizione.</p>

<p align="justify">Questo non significa che dobbiamo sempre scrivere condizioni più corte: la condizione deve restare comprensibile.</p>

---

## 5. Più `if` indipendenti: quando possono verificarsi più effetti

<p align="justify">Problema diverso:</p>

<blockquote>
<p align="justify">Se piove, porta l'ombrello. Se fa freddo, indossa la giacca.</p>
</blockquote>

<p align="justify">Le due condizioni sono indipendenti: possono essere vere entrambe.</p>

```python
if piove:
    print("ombrello")

if fa_freddo:
    print("giacca")
```

<p align="justify">Possibili risultati:</p>

```text
nessun messaggio
solo ombrello
solo giacca
ombrello + giacca
```

<p align="justify">Se trasformassimo il secondo <code>if</code> in <code>elif</code>, impediremmo l'esecuzione di entrambi i comportamenti nella stessa esecuzione.</p>

---

## 6. Domanda guida: “quanti rami possono essere eseguiti?”

<p align="justify">Prima di scegliere la sintassi chiediti:</p>

```text
I casi sono mutuamente esclusivi?
```

<p align="justify">Se vogliamo <strong>un solo risultato</strong> tra alternative:</p>

```text
if / elif / else
```

<p align="justify">Se più condizioni possono produrre <strong>più effetti contemporaneamente</strong>:</p>

```text
if indipendenti
```

<p align="justify">Non è una regola basata sul numero di condizioni, ma sulla relazione tra i casi del problema.</p>

---

## 7. `and`: devono essere vere entrambe

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Accesso consentito se l'età è almeno 18 <strong>e</strong> il biglietto è valido.</p>
</blockquote>

<p align="justify">Possiamo modellare:</p>

```python
eta >= 18 and biglietto_valido
```

<p align="justify"><code>and</code> produce <code>True</code> solo quando entrambe le parti sono vere.</p>

<table align="center">
<thead>
<tr>
<th>A</th>
<th>B</th>
<th><code>A and B</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>False</td>
<td>False</td>
<td>False</td>
</tr>
<tr>
<td>False</td>
<td>True</td>
<td>False</td>
</tr>
<tr>
<td>True</td>
<td>False</td>
<td>False</td>
</tr>
<tr>
<td>True</td>
<td>True</td>
<td>True</td>
</tr>
</tbody>
</table>

<p align="justify">Prima formula la frase in linguaggio naturale; poi traduci in Python.</p>

---

## 8. `or`: basta che almeno una sia vera

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Accesso gratuito se sei minore di 6 anni <strong>oppure</strong> hai almeno 65 anni.</p>
</blockquote>

```python
eta < 6 or eta >= 65
```

<table align="center">
<thead>
<tr>
<th>A</th>
<th>B</th>
<th><code>A or B</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>False</td>
<td>False</td>
<td>False</td>
</tr>
<tr>
<td>False</td>
<td>True</td>
<td>True</td>
</tr>
<tr>
<td>True</td>
<td>False</td>
<td>True</td>
</tr>
<tr>
<td>True</td>
<td>True</td>
<td>True</td>
</tr>
</tbody>
</table>

<p align="justify"><code>or</code> non significa “scegli una delle due condizioni a caso”.</p>

<p align="justify">Significa che il risultato complessivo è vero se almeno una parte è vera.</p>

---

## 9. `not`: nega una condizione già compresa

<p align="justify">Se:</p>

```python
account_attivo
```

<p align="justify">è un booleano, allora:</p>

```python
not account_attivo
```

<p align="justify">produce il valore opposto.</p>

<table align="center">
<thead>
<tr>
<th>A</th>
<th><code>not A</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>False</td>
<td>True</td>
</tr>
<tr>
<td>True</td>
<td>False</td>
</tr>
</tbody>
</table>

<p align="justify">Non usare <code>not</code> per rendere artificialmente più complicata una condizione che potresti esprimere direttamente.</p>

<p align="justify">Confronta:</p>

```python
not eta < 18
```

<p align="justify">con:</p>

```python
eta >= 18
```

<p align="justify">La seconda forma comunica direttamente la soglia che ci interessa.</p>

---

## 10. Intervalli: prima la logica, poi la forma compatta

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify"><code>x</code> deve essere compreso tra 0 e 10, estremi inclusi.</p>
</blockquote>

<p align="justify">Forma logica esplicita:</p>

```python
x >= 0 and x <= 10
```

<p align="justify">Dopo aver compreso questa forma, Python permette anche:</p>

```python
0 <= x <= 10
```

<p align="justify">Nel corso useremo la forma concatenata quando rende la condizione più naturale da leggere.</p>

<p align="justify">Non la impariamo come formula magica: rappresenta lo stesso intervallo che sappiamo già spiegare con <code>and</code>.</p>

---

## 11. Worked example: tariffa per fasce

<p align="justify">Specifica semplificata:</p>

```text
eta < 6        → 0 euro
6 <= eta < 18  → 5 euro
eta >= 18      → 10 euro
```

<p align="justify">Casi di test:</p>

<table align="center">
<thead>
<tr>
<th>età</th>
<th>tariffa</th>
</tr>
</thead>
<tbody>
<tr>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td>6</td>
<td>5</td>
</tr>
<tr>
<td>17</td>
<td>5</td>
</tr>
<tr>
<td>18</td>
<td>10</td>
</tr>
<tr>
<td>70</td>
<td>10</td>
</tr>
</tbody>
</table>

<p align="justify">Codice:</p>

```python
eta = int(input())

if eta < 6:
    tariffa = 0
elif eta < 18:
    tariffa = 5
else:
    tariffa = 10

print(tariffa)
```

<p align="justify">I test sui confini <code>6</code> e <code>18</code> sono essenziali.</p>

---

## 12. Error Clinic: soglie nell'ordine sbagliato

<p align="justify">Bug:</p>

```python
if voto >= 6:
    print("sufficiente")
elif voto >= 8:
    print("ottimo")
```

<p align="justify">Per <code>9</code>:</p>

```text
voto >= 6 → True
```

<p align="justify">Il primo ramo viene eseguito e il secondo non viene mai raggiunto.</p>

<p align="justify">Il problema non è la sintassi: è l'ordine dei casi.</p>

<p align="justify">Una possibile struttura coerente è:</p>

```python
if voto >= 8:
    print("ottimo")
elif voto >= 6:
    print("sufficiente")
else:
    print("insufficiente")
```

---

## 13. Error Clinic: più `if` quando volevamo un solo risultato

<p align="justify">Bug concettuale:</p>

```python
if voto >= 6:
    print("sufficiente")

if voto >= 8:
    print("ottimo")
```

<p align="justify">Con <code>9</code> otteniamo due classificazioni.</p>

<p align="justify">Se la specifica chiede <strong>una sola fascia</strong>, i due <code>if</code> indipendenti non rappresentano correttamente il problema.</p>

---

## 14. Error Clinic: `elif` quando due effetti possono coesistere

<p align="justify">Specifica:</p>

```text
se piove → ombrello
se fa freddo → giacca
```

<p align="justify">Bug:</p>

```python
if piove:
    print("ombrello")
elif fa_freddo:
    print("giacca")
```

<p align="justify">Se piove <strong>e</strong> fa freddo, viene stampato soltanto <code>ombrello</code>.</p>

<p align="justify">Il problema richiede due condizioni indipendenti.</p>

---

## 15. Error Clinic: `and` invece di `or`

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">gratis se età &lt; 6 oppure età &gt;= 65.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
if eta < 6 and eta >= 65:
    print("gratis")
```

<p align="justify">Nessuna età può soddisfare contemporaneamente entrambe le condizioni.</p>

<p align="justify">La traduzione della parola <strong>oppure</strong> è stata sbagliata.</p>

---

## 16. Short-circuit: un'intuizione utile

<p align="justify">Python valuta <code>and</code> e <code>or</code> da sinistra a destra e può non aver bisogno di valutare la seconda parte.</p>

<p align="justify">Esempio guidato:</p>

```python
if divisore != 0 and numero / divisore > 2:
    print("ok")
```

<p align="justify">Se <code>divisore != 0</code> è <code>False</code>, l'intera condizione <code>and</code> è già falsa: non serve valutare la divisione.</p>

<p align="justify">Per ora non memorizziamo trucchi.</p>

<p align="justify">Portiamo con noi soltanto due idee:</p>

<ul>
  <li>l'ordine delle condizioni può avere un significato;</li>
  <li>una condizione semplice/sicura può precedere un'operazione che ha senso solo in alcuni casi.</li>
</ul>

<p align="justify">Approfondiremo questi temi quando avremo più esperienza.</p>

---

## 17. Microscope: classifica la struttura prima del codice

<p align="justify">Per ogni specifica indica prima:</p>

```text
A) un solo ramo possibile
B) più effetti possibili
```

<ol>
  <li>“classifica il voto come insufficiente/buono/ottimo”;</li>
  <li>“se piove prendi ombrello; se fa freddo prendi giacca”;</li>
  <li>“scegli una tariffa tra tre fasce”;</li>
  <li>“se hai completato il quiz assegna badge; se hai completato il progetto assegna bonus”.</li>
</ol>

<p align="justify">Soltanto dopo scegli:</p>

```text
if / elif / else
oppure
if indipendenti
```

---

## 18. Activity planning — M07

<p align="justify">Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:</p>

### A — Classifica il caso

<p align="justify">Dato input + catena, prevedere il primo ramo eseguito.</p>

### B — Due `if` o `elif`?

<p align="justify">Diverse specifiche brevi: scegliere la struttura e motivarla.</p>

### C — Implement

<p align="justify">Classificatore a 3–4 fasce con test sui confini.</p>

### D — Debug

<p align="justify">Correggere:</p>

<ul>
  <li>soglie nell'ordine sbagliato;</li>
  <li>ramo irraggiungibile;</li>
  <li>due <code>if</code> quando serviva un solo risultato;</li>
  <li><code>elif</code> quando due effetti possono coesistere;</li>
  <li><code>and</code>/<code>or</code> sbagliato.</li>
</ul>

<p align="justify">M04 resta il canarino P1 fino alla certificazione <code>python-docente#7</code>.</p>

---

## 19. Romeo come applicazione selettiva

<p align="justify">Romeo non è necessario per imparare <code>elif</code>, <code>and</code> o <code>or</code>.</p>

<p align="justify">Dopo i problemi generali, il simulatore può offrire una variante di missione con regole multiple, ad esempio:</p>

```text
modalità sicura + limite di velocità
oppure
selezione di un comportamento da un parametro della missione
```

<p align="justify">La variante deve:</p>

<ul>
  <li>usare soltanto API già appropriate al livello;</li>
  <li>rimanere deterministica;</li>
  <li>non introdurre sensori/networking non ancora studiati;</li>
  <li>essere opzionale finché <code>romeo-sim</code> non è certificato nel Classroom Environment.</li>
</ul>

<p align="justify">Non duplichiamo ora una nuova Activity Romeo nel repo Python.</p>

---

## 20. Esercizi brevi

## A — Fasce

<p align="justify">Classifica una temperatura:</p>

```text
< 0      → gelo
0..24    → normale
>= 25    → caldo
```

<p align="justify">Scrivi prima i casi <code>-1</code>, <code>0</code>, <code>24</code>, <code>25</code>.</p>

## B — Indipendenti o esclusivi?

<p align="justify">Per ciascuna specifica scegli <code>if</code> indipendenti o catena <code>elif</code> e motiva in una riga.</p>

## C — Accesso composto

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">consentito se età &gt;= 18 e biglietto valido.</p>
</blockquote>

<p align="justify">Progetta i quattro casi della tabella di verità e poi il codice.</p>

## D — Intervallo

<p align="justify">Verifica se un numero appartiene all'intervallo chiuso <code>[10, 20]</code> prima con <code>and</code>, poi con confronto concatenato.</p>

<p align="justify">Spiega perché le due condizioni rappresentano lo stesso insieme di valori.</p>

---

## 21. Checkpoint M07

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Che cosa significa “primo ramo vero” in una catena <code>if/elif/else</code>?</li>
  <li>Perché <code>elif voto &lt; 8</code> può essere sufficiente dopo <code>if voto &lt; 6</code>?</li>
  <li>Quando sono corretti due <code>if</code> indipendenti?</li>
  <li>Quando è preferibile una catena mutuamente esclusiva?</li>
  <li>Quando <code>A and B</code> è vero?</li>
  <li>Quando <code>A or B</code> è vero?</li>
  <li>Che cosa produce <code>not True</code>?</li>
  <li>Che insieme di valori rappresenta <code>0 &lt;= x &lt;= 10</code>?</li>
  <li>Perché l'ordine <code>if voto &gt;= 6</code> poi <code>elif voto &gt;= 8</code> è problematico?</li>
</ol>

---

## 22. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
if / elif / else → scegli il primo ramo vero
```

```text
if indipendenti → più effetti possono coesistere
```

```text
and → tutte vere
or  → almeno una vera
not → negazione
```

```text
intervallo → confini + casi di test
```

<p align="justify">Nel prossimo modulo useremo selezioni annidate, validazione e refactoring per capire quando una decisione dipende realmente da un'altra e quando invece il codice può essere reso più semplice.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione/verifica:</p>

<ul>
  <li>documentazione Python 3.12 — <code>if</code> statement, Boolean operations, comparisons e chained comparisons;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — conditional execution, recursion-free beginner reasoning e debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — Boolean expressions, control flow e statement semantics;</li>
  <li>Romeo pinned <code>45e5f7e131802fccc89358a23a25dbed1884bbfa</code> — solo riferimento applicativo selettivo.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

## Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_03_SPEC.md</code>;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>.</li>
</ul>

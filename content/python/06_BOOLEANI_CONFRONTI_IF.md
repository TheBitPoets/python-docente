# M06 — Booleani, confronti e prima selezione con `if`

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Una condizione booleana permette al programma di scegliere il comportamento richiesto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Leggere input, valutare espressioni e progettare casi di test da M04–M05.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
riconoscere un'espressione che produce <code>True</code> o <code>False</code>;<br>usare <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code> nei casi semplici;<br>distinguere assegnamento <code>=</code> e confronto <code>==</code>; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Riprendi il rombo del flow chart e associa i rami vero/falso ai blocchi indentati. Riprendi <a href="05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md">M05 — Espressioni, operatori e prime funzioni</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md">M07 — <code>elif</code>, casi esclusivi e condizioni composte</a>. Più casi richiedono di distinguere alternative esclusive e condizioni indipendenti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Verifica la spedizione gratuita sotto, sulla e sopra la soglia, spiegando il ramo percorso.
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
  <li>riconoscere un'espressione che produce <code>True</code> o <code>False</code>;</li>
  <li>usare <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code> nei casi semplici;</li>
  <li>distinguere assegnamento <code>=</code> e confronto <code>==</code>;</li>
  <li>prevedere il risultato di un confronto prima di eseguirlo;</li>
  <li>tradurre una decisione sì/no in un <code>if</code>;</li>
  <li>usare <code>if/else</code> quando i due casi sono complementari;</li>
  <li>capire che l'indentazione definisce il blocco eseguito dal ramo;</li>
  <li>fare il trace di una selezione con dati concreti;</li>
  <li>progettare test <strong>sotto, sulla e sopra</strong> una soglia;</li>
  <li>diagnosticare condizioni invertite, confini sbagliati e rami con output errato;</li>
  <li>spiegare a parole perché un certo input percorre un certo ramo.</li>
</ul>

## Prerequisiti

<p align="justify">Da M04–M05 dovresti già saper:</p>

<ul>
  <li>leggere input e convertire tipi;</li>
  <li>usare variabili, espressioni e output;</li>
  <li>distinguere <code>/</code>, <code>//</code>, <code>%</code> nei problemi appropriati;</li>
  <li>prevedere valore e tipo di espressioni semplici;</li>
  <li>progettare più casi di test;</li>
  <li>leggere errori beginner e correggere una modifica alla volta.</li>
</ul>

---

## 1. Problema iniziale: lo sconto si applica oppure no?

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Se il totale dell'ordine è almeno 50 euro, la spedizione è gratuita. Altrimenti costa 5 euro.</p>
</blockquote>

<p align="justify">Prima di Python dobbiamo capire la <strong>decisione</strong>.</p>

```text
totale >= 50 ?
    sì  → spedizione = 0
    no  → spedizione = 5
```

<p align="justify">La parte più importante è la soglia:</p>

```text
almeno 50
```

<p align="justify">significa che <strong>50 è incluso</strong>.</p>

<p align="justify">Quindi la domanda corretta è:</p>

```python
totale >= 50
```

<p align="justify">non:</p>

```python
totale > 50
```

---

## 2. Una condizione è un'espressione che produce `bool`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — condizione booleana:</strong>
Negli esempi di questo modulo una condizione è un'espressione che produce un valore di tipo <code>bool</code>: <code>True</code> oppure <code>False</code>. Questa risposta determina il ramo da eseguire.
</p>
</td>
</tr>
</table>

<p align="justify">Nel REPL, prima prevedi:</p>

```python
7 > 3
```

<p align="justify">Il risultato è:</p>

```python
True
```

<p align="justify">Poi:</p>

```python
7 < 3
```

<p align="justify">produce:</p>

```python
False
```

<p align="justify">Il tipo è:</p>

```python
bool
```

<p align="justify">Modello mentale:</p>

```text
valori
  ↓
confronto
  ↓
True oppure False
```

<p align="justify">Questa risposta vero/falso può controllare quale ramo del programma viene eseguito.</p>

---

## 3. Operatori di confronto

<table align="center">
<thead>
<tr>
<th>Operatore</th>
<th>Domanda</th>
<th>Esempio</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>==</code></td>
<td>ha lo stesso valore?</td>
<td><code>voto == 6</code></td>
</tr>
<tr>
<td><code>!=</code></td>
<td>ha valore diverso?</td>
<td><code>voto != 6</code></td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>minore di?</td>
<td><code>eta &lt; 18</code></td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>minore o uguale?</td>
<td><code>temperatura &lt;= 0</code></td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>maggiore di?</td>
<td><code>punti &gt; 100</code></td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>maggiore o uguale?</td>
<td><code>totale &gt;= 50</code></td>
</tr>
</tbody>
</table>

<p align="justify">Non scegliere l'operatore guardando soltanto il simbolo.</p>

<p align="justify">Traduci prima la frase:</p>

```text
più di 10        → > 10
almeno 10        → >= 10
meno di 10       → < 10
al massimo 10    → <= 10
esattamente 10   → == 10
```

---

## 4. `=` e `==` fanno lavori diversi

<p align="justify">In M04 abbiamo usato:</p>

```python
eta = 15
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — assegnamento:</strong>
Un <strong>assegnamento</strong> associa un nome al valore prodotto dall'espressione a destra di <code>=</code>.
</p>
</td>
</tr>
</table>

<p align="justify">Per fare una domanda di uguaglianza usiamo:</p>

```python
eta == 15
```

<p align="justify">che produce:</p>

```text
True oppure False
```

<p align="justify">Modello:</p>

```text
=   → assegna
==  → confronta
```

<p align="justify">Python non considera questi due operatori intercambiabili.</p>

---

## 5. Primo `if`: esegui qualcosa soltanto quando la condizione è vera

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — selezione semplice — if:</strong>
<code>if</code> esegue il proprio blocco quando la condizione è vera. Quando è falsa, il blocco viene saltato e l'esecuzione prosegue.
</p>
</td>
</tr>
</table>

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Se la temperatura è sotto zero, stampa <code>gelo</code>.</p>
</blockquote>

```python
temperatura = int(input())

if temperatura < 0:
    print("gelo")
```

<p align="justify">Se l'input è <code>-3</code>, la condizione è vera e il ramo viene eseguito.</p>

<p align="justify">Se l'input è <code>5</code>, la condizione è falsa e quel <code>print</code> non viene eseguito.</p>

<p align="justify">Questo <strong>non è un errore</strong>: è proprio il comportamento richiesto da un <code>if</code> senza <code>else</code>.</p>

---

## 6. I due punti e l'indentazione fanno parte della struttura

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — blocco e indentazione:</strong>
Un blocco è un gruppo di istruzioni che appartengono alla stessa struttura. In Python l'indentazione, cioè il rientro all'inizio delle righe, delimita il blocco.
</p>
</td>
</tr>
</table>

<p align="justify">Osserva:</p>

```python
if temperatura < 0:
    print("gelo")
```

<p align="justify">Due elementi sono strutturali:</p>

<ol>
  <li><code>:</code> dopo la condizione;</li>
  <li>il blocco indentato sotto <code>if</code>.</li>
</ol>

<p align="justify">L'indentazione non è soltanto estetica.</p>

<p align="justify">Indica quali istruzioni appartengono al ramo.</p>

<p align="justify">Confronta:</p>

```python
if temperatura < 0:
    print("gelo")
print("fine")
```

<p align="justify"><code>print("fine")</code> viene eseguito comunque perché non appartiene al blocco dell'<code>if</code>.</p>

---

## 7. Trace di un `if`

<p align="justify">Programma:</p>

```python
numero = int(input())

if numero > 0:
    print("positivo")

print("fine")
```

## Caso A — input `4`

```text
numero           → 4
numero > 0       → True
ramo if          → eseguito
output            → positivo
print("fine")    → eseguito
output            → fine
```

## Caso B — input `-2`

```text
numero           → -2
numero > 0       → False
ramo if          → saltato
print("fine")    → eseguito
output            → fine
```

<p align="justify">Il trace deve seguire il valore concreto della condizione, non ciò che "sembra probabile".</p>

---

## 8. Quando serve `else`

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Stampa <code>maggiorenne</code> se l'età è almeno 18, altrimenti stampa <code>minorenne</code>.</p>
</blockquote>

<p align="justify">I casi sono complementari:</p>

```text
eta >= 18
oppure
eta < 18
```

<p align="justify">Possiamo scrivere:</p>

```python
eta = int(input())

if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

<p align="justify"><code>else</code> significa:</p>

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — else:</strong>
<code>else</code> introduce il ramo eseguito quando la condizione dell'<code>if</code> è falsa.
</p>
</td>
</tr>
</table>

<p align="justify">Non serve riscrivere la condizione opposta.</p>

---

## 9. Un solo ramo di `if/else` viene eseguito

<p align="justify">Con:</p>

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

<p align="justify">per ogni singola esecuzione:</p>

```text
condizione True  → ramo if
condizione False → ramo else
```

<p align="justify">Non vengono eseguiti entrambi.</p>

<p align="justify">Questa idea diventerà importante in M07 quando confronteremo:</p>

```text
più if indipendenti
```

<p align="justify">con:</p>

```text
if / elif / else
```

---

## 10. I casi di frontiera: sotto, sulla, sopra

<p align="justify">Per una soglia <code>18</code>, non basta provare un valore lontano.</p>

<p align="justify">Casi minimi:</p>

<table align="center">
<thead>
<tr>
<th>età</th>
<th>atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>17</td>
<td>minorenne</td>
</tr>
<tr>
<td>18</td>
<td>maggiorenne</td>
</tr>
<tr>
<td>19</td>
<td>maggiorenne</td>
</tr>
</tbody>
</table>

<p align="justify">Perché <code>18</code> è fondamentale?</p>

<p align="justify">Perché distingue:</p>

```python
eta > 18
```

<p align="justify">da:</p>

```python
eta >= 18
```

<p align="justify">Un test sul confine trova errori che un caso come <code>25</code> non vede.</p>

---

## 11. Worked example: spedizione gratuita

## Specifica

```text
INPUT: totale ordine, intero non negativo
OUTPUT: costo spedizione
REGOLA: se totale >= 50 → 0, altrimenti → 5
```

## Casi prima del codice

<table align="center">
<thead>
<tr>
<th>totale</th>
<th>spedizione attesa</th>
</tr>
</thead>
<tbody>
<tr>
<td>49</td>
<td>5</td>
</tr>
<tr>
<td>50</td>
<td>0</td>
</tr>
<tr>
<td>51</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>5</td>
</tr>
</tbody>
</table>

## Codice

```python
totale = int(input())

if totale >= 50:
    spedizione = 0
else:
    spedizione = 5

print(spedizione)
```

<p align="justify">Il <code>print</code> è fuori dalla selezione perché in entrambi i casi vogliamo mostrare il valore finale di <code>spedizione</code>.</p>

---

## 12. Confronto: duplicare output oppure calcolare prima?

<p align="justify">Versione A:</p>

```python
if totale >= 50:
    print(0)
else:
    print(5)
```

<p align="justify">Versione B:</p>

```python
if totale >= 50:
    spedizione = 0
else:
    spedizione = 5

print(spedizione)
```

<p align="justify">Entrambe possono essere corrette per questa specifica.</p>

<p align="justify">La B separa meglio:</p>

```text
decisione / calcolo
→ presentazione finale
```

<p align="justify">Ma non trasformiamo questa preferenza in una regola meccanica: confrontiamo sempre chiarezza e obiettivo del problema.</p>

---

## 13. Microscope: prevedi `True` o `False`

<p align="justify">Senza REPL, completa prima:</p>

<table align="center">
<thead>
<tr>
<th>Espressione</th>
<th>Risultato previsto</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5 &gt; 2</code></td>
<td>?</td>
</tr>
<tr>
<td><code>5 &lt; 2</code></td>
<td>?</td>
</tr>
<tr>
<td><code>5 == 5</code></td>
<td>?</td>
</tr>
<tr>
<td><code>5 != 5</code></td>
<td>?</td>
</tr>
<tr>
<td><code>10 &gt;= 10</code></td>
<td>?</td>
</tr>
<tr>
<td><code>9 &gt;= 10</code></td>
<td>?</td>
</tr>
<tr>
<td><code>0 &lt;= 0</code></td>
<td>?</td>
</tr>
</tbody>
</table>

<p align="justify">Poi verifica.</p>

<p align="justify">Il simbolo <code>=</code> singolo non compare nella tabella perché non è un confronto.</p>

---

## 14. Error Clinic

## Caso 1 — confine sbagliato

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">accesso consentito da 18 anni compresi.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
if eta > 18:
    print("consentito")
```

<p align="justify">Quale input distingue subito il bug?</p>

```text
18
```

## Caso 2 — condizione invertita

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">stampa <code>negativo</code> se il numero è minore di zero.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
if numero > 0:
    print("negativo")
```

<p align="justify">Il programma è sintatticamente valido ma rappresenta la domanda sbagliata.</p>

## Caso 3 — `=` al posto di `==`

```python
if voto = 6:
    print("sei")
```

<p align="justify">Qui stai tentando di usare un assegnamento dove Python richiede un'espressione valida come condizione.</p>

<p align="justify">Per confrontare il valore:</p>

```python
if voto == 6:
```

## Caso 4 — indentazione

```python
if temperatura < 0:
print("gelo")
```

<p align="justify">Il blocco non è strutturato correttamente.</p>

## Caso 5 — output nel ramo sbagliato

```python
if eta >= 18:
    print("minorenne")
else:
    print("maggiorenne")
```

<p align="justify">La sintassi è valida; il comportamento non rispetta la specifica.</p>

---

## 15. `is` non è il sostituto di `==`

<p align="justify">Per confrontare normalmente valori numerici o stringhe nel nostro corso usiamo:</p>

```python
==
```

<p align="justify">Non insegniamo:</p>

```python
is
```

<p align="justify">come scorciatoia per l'uguaglianza di valore.</p>

<p align="justify"><code>is</code> riguarda l'identità degli oggetti e verrà contestualizzato molto più avanti, quando avremo un modello degli oggetti sufficiente.</p>

<p align="justify">Regola beginner:</p>

```text
uguaglianza di valore → ==
```

---

## 16. Dal flow chart al Python

<p align="justify">Decisione algoritmica:</p>

```text
        eta >= 18 ?
       /           \
     sì             no
     |              |
maggiorenne      minorenne
```

<p align="justify">Python:</p>

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

<p align="justify">La sintassi cambia, ma il modello della decisione è lo stesso.</p>

<p align="justify">Per questo il flow chart non era un esercizio separato da Python: rappresentava la struttura che ora codifichiamo.</p>

---

## 17. Activity planning — M06

<p align="justify">Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:</p>

### A — Predict/Trace

<p align="justify">Dato valore + condizione, prevedere:</p>

<ul>
  <li><code>True</code>/<code>False</code>;</li>
  <li>ramo eseguito;</li>
  <li>output.</li>
</ul>

### B — Controlled Change

<p align="justify">Cambiare una soglia e aggiornare i casi <code>sotto / sulla / sopra</code>.</p>

### C — Implement

<p align="justify">Da un flow chart sì/no già noto a un programma <code>if/else</code>.</p>

### D — Debug

<p align="justify">Correggere:</p>

<ul>
  <li><code>&gt;</code> vs <code>&gt;=</code>;</li>
  <li>condizione invertita;</li>
  <li><code>=</code> vs <code>==</code>;</li>
  <li>indentazione;</li>
  <li>messaggi nei rami sbagliati.</li>
</ul>

<p align="justify">M04 resta il canarino P1 finché <code>python-docente#7</code> non è certificato.</p>

---

## 18. Romeo come applicazione opzionale

<p align="justify">Il concetto di selezione deve essere padroneggiato anche senza Romeo.</p>

<p align="justify">Dopo gli esercizi generali possiamo usare il simulatore come problema concreto.</p>

<p align="justify">La piattaforma Romeo pinned contiene già una missione didattica:</p>

```text
romeo-y1-u14-condizioni — Decidi con if
```

<p align="justify">Idea della missione:</p>

<blockquote>
<p align="justify">se la modalità sicura è attiva, usa una velocità ridotta; completa la missione e fermati.</p>
</blockquote>

<p align="justify">Il valore didattico è vedere che:</p>

```text
condizione
→ scelta di comportamento
→ effetto osservabile nel simulatore
```

<p align="justify">Regole:</p>

<ul>
  <li><code>romeo-sim</code> soltanto nel Classroom Environment certificato;</li>
  <li>hardware fisico non richiesto;</li>
  <li>niente networking/FastAPI/WebSocket;</li>
  <li>la missione è applicazione del concetto, non il suo prerequisito.</li>
</ul>

---

## 19. Esercizi brevi

## A — Soglia

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Se il punteggio è almeno 100, stampa <code>livello</code>; altrimenti stampa <code>continua</code>.</p>
</blockquote>

<p align="justify">Scrivi prima i casi <code>99</code>, <code>100</code>, <code>101</code>, poi il codice.</p>

## B — Positivo o non positivo

<p align="justify">Leggi un intero e stampa:</p>

```text
positivo
```

<p align="justify">se è maggiore di zero, altrimenti:</p>

```text
non positivo
```

<p align="justify">Quale ramo percorre <code>0</code>?</p>

## C — Debug del confine

<p align="justify">Correggi:</p>

```python
if temperatura > 0:
    print("sopra zero")
else:
    print("zero o sotto")
```

<p align="justify">solo se una nuova specifica dice:</p>

<blockquote>
<p align="justify"><code>sopra zero</code> deve essere stampato anche per <code>0</code>.</p>
</blockquote>

<p align="justify">Quale operatore cambia e perché?</p>

## D — Flow chart → codice

<p align="justify">Ricevi un flow chart con una sola decisione e produci:</p>

<ol>
  <li>tabella di tre casi;</li>
  <li>condizione Python;</li>
  <li><code>if/else</code>;</li>
  <li>trace di un caso.</li>
</ol>

---

## 20. Checkpoint M06

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Che tipo produce <code>7 &gt;= 7</code>?</li>
  <li>Differenza fra <code>=</code> e <code>==</code>?</li>
  <li>Perché <code>eta &gt;= 18</code> include il valore 18?</li>
  <li>Che cosa succede al blocco <code>if</code> se la condizione è <code>False</code> e non esiste <code>else</code>?</li>
  <li>Perché l'indentazione non è soltanto estetica?</li>
  <li>Quali tre valori sceglieresti per testare una soglia 50?</li>
  <li>Perché non usiamo <code>is</code> come sostituto di <code>==</code>?</li>
  <li>In che modo il flow chart della decisione corrisponde a <code>if/else</code>?</li>
</ol>

---

## 21. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
confronto → bool
```

```text
True  → esegui ramo if
False → salta ramo if / usa else se presente
```

```text
=  → assegnamento
== → confronto di valore
```

```text
soglia → test sotto / sulla / sopra
```

```text
indentazione → appartenenza al blocco
```

<p align="justify">Nel prossimo modulo passeremo da due casi a più casi e capiremo quando usare <code>elif</code>, quando usare più <code>if</code> indipendenti e come comporre condizioni con <code>and</code>, <code>or</code>, <code>not</code>.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione/verifica:</p>

<ul>
  <li>documentazione Python 3.12 — confronti, <code>if</code> e control flow;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — conditional execution e debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — espressioni booleane, statement e controllo;</li>
  <li>Romeo pinned <code>45e5f7e131802fccc89358a23a25dbed1884bbfa</code> — riferimento tecnico/applicativo per <code>romeo-y1-u14-condizioni</code>.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

## Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_03_SPEC.md</code>;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>.</li>
</ul>

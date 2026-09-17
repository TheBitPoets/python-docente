# M04 — Interprete, REPL, script, valori e input/output

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Gli algoritmi già tracciati vengono eseguiti dall&#x27;interprete, prima nel REPL e poi in uno script.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Individuare input/output, descrivere passi e proporre casi di test; nessuna conoscenza precedente di Python.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare in modo semplice che cosa fa l'interprete Python;<br>usare il REPL per provare un'espressione alla volta;<br>distinguere un valore, un nome/variabile e un'espressione; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Confronta il risultato atteso dal trace manuale con quello prodotto dal programma. Riprendi <a href="03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md">M03 — Flow chart: iterazione, terminazione e annidamento</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md">M05 — Espressioni, operatori e prime funzioni</a>. Le espressioni trasformano valori; una prima funzione dà un nome al calcolo e ne restituisce il risultato.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Prova la somma con input testuali, conversione in numeri e stampa; esegui poi lo stesso calcolo da un file .py.
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
<p align="justify"><strong>Stato:</strong> draft / vertical slice di authoring<br>
<strong>UDA:</strong> PY2-02 — Primi programmi Python<br>
<strong>Baseline:</strong> Python 3.12 nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>spiegare in modo semplice che cosa fa l'interprete Python;</li>
  <li>usare il REPL per provare un'espressione alla volta;</li>
  <li>distinguere un valore, un nome/variabile e un'espressione;</li>
  <li>riconoscere i tipi fondamentali <code>int</code>, <code>float</code>, <code>str</code> e <code>bool</code> nei casi più semplici;</li>
  <li>assegnare un valore a una variabile;</li>
  <li>usare <code>print()</code> per produrre output;</li>
  <li>usare <code>input()</code> e ricordare che restituisce una stringa;</li>
  <li>convertire dati con <code>int()</code>, <code>float()</code> e <code>str()</code> quando serve;</li>
  <li>salvare ed eseguire un piccolo programma <code>.py</code>;</li>
  <li>leggere la parte essenziale di un errore/traceback;</li>
  <li>provare lo stesso programma con più casi e confrontare risultato atteso e ottenuto.</li>
</ul>

## Prerequisiti

<p align="justify">Dovresti già saper, almeno su problemi semplici:</p>

<ul>
  <li>individuare input e output;</li>
  <li>descrivere un algoritmo come passi ordinati;</li>
  <li>eseguire un trace manuale;</li>
  <li>proporre qualche caso di test.</li>
</ul>

<p align="justify">Non serve conoscere già Python.</p>

---

# 1. Problema iniziale: dal procedimento al programma

<p align="justify">Considera questo problema:</p>

<blockquote>
<p align="justify">Leggi due numeri interi e mostra la loro somma.</p>
</blockquote>

<p align="justify">Prima del codice possiamo descriverlo così:</p>

```text
INPUT: primo numero, secondo numero
OUTPUT: somma

1. acquisisci il primo numero
2. acquisisci il secondo numero
3. calcola primo + secondo
4. mostra il risultato
```

<p align="justify">Il programma Python non inventa la soluzione: <strong>traduce questo algoritmo in istruzioni che l'interprete può eseguire</strong>.</p>

<p align="justify">Una possibile traduzione è:</p>

```python
primo = int(input())
secondo = int(input())
risultato = primo + secondo
print(risultato)
```

<p align="justify">Non preoccuparti ancora di ricordare tutto. In questo modulo smonteremo il programma riga per riga.</p>

---

# 2. Che cosa fa l'interprete Python

<p align="justify">Un file Python contiene testo con istruzioni Python.</p>

<p align="justify">Quando esegui:</p>

```text
python programma.py
```

<p align="justify">stai chiedendo all'interprete Python di leggere ed eseguire il programma.</p>

<p align="justify">Un modello mentale sufficiente per iniziare è:</p>

```text
sorgente .py
    ↓
interprete Python
    ↓
esecuzione delle istruzioni
    ↓
output oppure errore
```

<p align="justify">Python svolge internamente molti passaggi più complessi, ma non servono ancora per capire i primi programmi. Più avanti potremo approfondire bytecode, virtual machine e modello di esecuzione.</p>

## Una regola utile

<p align="justify">Il computer non esegue ciò che <strong>intendevi</strong> scrivere.</p>

<p align="justify">Esegue ciò che il programma <strong>dice realmente</strong>, secondo le regole del linguaggio.</p>

<p align="justify">Per questo impariamo a:</p>

```text
prevedere
→ eseguire
→ osservare
→ confrontare
→ correggere
```

---

# 3. Il REPL: un laboratorio per fare esperimenti

<p align="justify">Python può essere usato in modalità interattiva.</p>

<p align="justify">Nel Classroom Environment apri il REPL Python secondo il comando/launcher indicato dalla guida TheBitLab. Vedrai un prompt simile a:</p>

```text
>>>
```

<p align="justify">REPL significa:</p>

```text
Read   → leggi ciò che scrivi
Eval   → valutalo/eseguilo
Print  → mostra il risultato quando appropriato
Loop   → torna al prompt
```

## Primo esperimento

<p align="justify">Prima <strong>prevedi</strong> il risultato:</p>

```python
2 + 3
```

<p align="justify">Poi esegui.</p>

<p align="justify">Dovresti osservare:</p>

```text
5
```

<p align="justify">Prova allo stesso modo:</p>

```python
10 - 4
3 * 5
10 / 2
```

## Il REPL non è un indovino

<p align="justify">Se scrivi:</p>

```python
2 +
```

<p align="justify">l'espressione non rispetta la sintassi richiesta e Python segnala un errore.</p>

<p align="justify">Un errore non è una sconfitta: è <strong>informazione sul programma che hai realmente scritto</strong>.</p>

---

# 4. Valori e tipi

<p align="justify">Un programma lavora con dati.</p>

<p align="justify">Python distingue diversi tipi di valore.</p>

## Interi: `int`

```python
42
-7
0
```

<p align="justify">sono valori interi.</p>

<p align="justify">Nel REPL:</p>

```python
>>> type(42)
<class 'int'>
```

## Numeri con parte decimale: `float`

```python
3.5
-0.25
2.0
```

<p align="justify">Nel REPL:</p>

```python
>>> type(3.5)
<class 'float'>
```

## Testo: `str`

```python
"ciao"
"42"
"Python"
```

<p align="justify">sono stringhe.</p>

<p align="justify">Nota importante:</p>

```text
42      numero intero
"42"    testo formato dai caratteri 4 e 2
```

<p align="justify">Non sono lo stesso valore.</p>

## Booleani: `bool`

<p align="justify">I valori booleani sono:</p>

```python
True
False
```

<p align="justify">Diventeranno fondamentali quando studieremo le decisioni con <code>if</code>.</p>

---

# 5. Variabili: dare un nome a un valore

<p align="justify">Nel REPL prova:</p>

```python
eta = 15
```

<p align="justify">Poi:</p>

```python
eta
```

<p align="justify">Il risultato è:</p>

```text
15
```

<p align="justify">Possiamo usare il nome in un'espressione:</p>

```python
eta + 1
```

## Modello mentale iniziale

<p align="justify">Per ora pensa a:</p>

```text
eta ──> 15
```

<p align="justify">Il nome <code>eta</code> permette di riferirsi al valore.</p>

<p align="justify">Più avanti renderemo questo modello più preciso quando studieremo oggetti, mutabilità e alias.</p>

## `=` non significa "è uguale" nel senso matematico

<p align="justify">In:</p>

```python
eta = 15
```

<p align="justify"><code>=</code> rappresenta un <strong>assegnamento</strong>: associa il nome <code>eta</code> al valore prodotto a destra.</p>

<p align="justify">Se poi scrivi:</p>

```python
eta = 16
```

<p align="justify">il nome ora fa riferimento al nuovo valore.</p>

## Nomi leggibili

<p align="justify">Preferisci:</p>

```python
prezzo_totale = 25
```

<p align="justify">rispetto a:</p>

```python
x = 25
```

<p align="justify">quando il nome aiuta a capire il significato del dato.</p>

<p align="justify">Un nome breve non è automaticamente migliore.</p>

---

# 6. `print()`: produrre output

<p align="justify">Nel REPL:</p>

```python
print("ciao")
```

<p align="justify">mostra:</p>

```text
ciao
```

<p align="justify">Possiamo stampare una variabile:</p>

```python
nome = "Anna"
print(nome)
```

<p align="justify">oppure un'espressione:</p>

```python
print(2 + 3)
```

## REPL e `print()` non sono la stessa cosa

<p align="justify">Nel REPL:</p>

```python
>>> 2 + 3
5
```

<p align="justify">il REPL visualizza il valore dell'espressione.</p>

<p align="justify">In un file <code>.py</code>, invece:</p>

```python
2 + 3
```

<p align="justify">calcola il valore, ma non hai chiesto al programma di mostrarlo.</p>

<p align="justify">Per produrre l'output:</p>

```python
print(2 + 3)
```

<p align="justify">Questa differenza è importante nel passaggio REPL → script.</p>

---

# 7. `input()`: ricevere dati

<p align="justify">Prova:</p>

```python
nome = input()
```

<p align="justify">Il programma aspetta che tu scriva qualcosa e prema Invio.</p>

<p align="justify">Poi:</p>

```python
print(nome)
```

## Il punto fondamentale: `input()` restituisce testo

<p align="justify">Anche se digiti:</p>

```text
12
```

<p align="justify">il risultato di <code>input()</code> è una stringa.</p>

<p align="justify">Verificalo:</p>

```python
dato = input()
print(type(dato))
```

<p align="justify">Se digiti <code>12</code>, vedrai comunque:</p>

```text
<class 'str'>
```

---

# 8. Perché `"2" + "3"` non fa `5`

<p align="justify">Prima prevedi:</p>

```python
"2" + "3"
```

<p align="justify">Il risultato è:</p>

```text
'23'
```

<p align="justify">Per le stringhe, <code>+</code> concatena testo.</p>

<p align="justify">Con gli interi:</p>

```python
2 + 3
```

<p align="justify">il risultato è:</p>

```text
5
```

<p align="justify">Il simbolo è lo stesso, ma l'operazione dipende dai tipi coinvolti.</p>

<p align="justify">Questa è una delle ragioni per cui <strong>capire i tipi</strong> è importante.</p>

---

# 9. Conversioni: trasformare il dato quando il problema lo richiede

<p align="justify">Se vuoi usare come numero ciò che è stato letto con <code>input()</code>, devi convertirlo.</p>

```python
testo = input()
numero = int(testo)
```

<p align="justify">Spesso si scrive direttamente:</p>

```python
numero = int(input())
```

## `int()`

<p align="justify">Converte un testo compatibile in intero:</p>

```python
int("42")
```

<p align="justify">produce:</p>

```text
42
```

<p align="justify">Ma:</p>

```python
int("ciao")
```

<p align="justify">non può produrre un intero valido e genera un errore.</p>

## `float()`

```python
float("3.5")
```

<p align="justify">produce un <code>float</code>.</p>

## `str()`

```python
str(42)
```

<p align="justify">produce il testo:</p>

```text
"42"
```

## Non convertire per abitudine

<p align="justify">La domanda deve essere:</p>

<blockquote>
<p align="justify">Quale tipo mi serve per l'operazione che devo fare?</p>
</blockquote>

<p align="justify">Se stai leggendo un nome, non ha senso convertirlo in <code>int</code>.</p>

---

# 10. Dal REPL al primo script

<p align="justify">Un esperimento REPL scompare quando chiudi la sessione.</p>

<p align="justify">Un programma che vuoi conservare e rieseguire va scritto in un file.</p>

<p align="justify">Crea nel workspace gestito dal corso un file:</p>

```text
main.py
```

<p align="justify">con:</p>

```python
nome = input()
print(nome)
```

<p align="justify">Eseguilo con il workflow TheBitLab indicato dalla guida.</p>

## Perché passare presto agli script

<p align="justify">Il REPL è ottimo per:</p>

<ul>
  <li>esperimenti;</li>
  <li>espressioni;</li>
  <li>controllare un'ipotesi;</li>
  <li>capire un errore piccolo.</li>
</ul>

<p align="justify">Lo script è migliore quando vuoi:</p>

<ul>
  <li>conservare il programma;</li>
  <li>eseguirlo di nuovo;</li>
  <li>modificarlo;</li>
  <li>testarlo;</li>
  <li>versionarlo;</li>
  <li>costruire qualcosa di più grande.</li>
</ul>

<p align="justify">Non sono concorrenti: sono strumenti diversi.</p>

---

# 11. Microscope: esegui mentalmente questo programma

<p align="justify">Prima di provarlo, completa il trace:</p>

```python
primo = 4
secondo = 6
risultato = primo + secondo
print(risultato)
```

<table align="center">
<thead>
<tr>
<th>Passo</th>
<th><code>primo</code></th>
<th><code>secondo</code></th>
<th><code>risultato</code></th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr>
<td>dopo riga 1</td>
<td>4</td>
<td>—</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>dopo riga 2</td>
<td>4</td>
<td>6</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>dopo riga 3</td>
<td>4</td>
<td>6</td>
<td>?</td>
<td>—</td>
</tr>
<tr>
<td>dopo riga 4</td>
<td>4</td>
<td>6</td>
<td>?</td>
<td>?</td>
</tr>
</tbody>
</table>

<p align="justify">Soltanto dopo eseguilo.</p>

## Variante

<p align="justify">Cambia:</p>

```python
secondo = -2
```

<p align="justify">Prevedi di nuovo prima dell'esecuzione.</p>

<p align="justify">Questa abitudine — <strong>predict before run</strong> — continuerà per tutto il corso.</p>

---

# 12. Worked example: somma di due numeri letti dall'utente

<p align="justify">Riprendiamo il problema iniziale.</p>

## Specifica

```text
INPUT: due interi, uno per riga
OUTPUT: la loro somma
```

## Casi di test prima del codice

<table align="center">
<thead>
<tr>
<th>input 1</th>
<th>input 2</th>
<th>output atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>-4</td>
<td>10</td>
<td>6</td>
</tr>
</tbody>
</table>

## Codice

```python
primo = int(input())
secondo = int(input())
risultato = primo + secondo
print(risultato)
```

## Trace con `-4` e `10`

```text
input()             → "-4"
int("-4")           → -4
primo               → -4

input()             → "10"
int("10")           → 10
secondo             → 10

primo + secondo     → 6
risultato           → 6
print(risultato)    → mostra 6
```

<p align="justify">Notare la distinzione tra:</p>

```text
"10"   stringa letta
10      intero ottenuto dopo conversione
```

---

# 13. Confronto: due programmi che sembrano simili

## Versione A

```python
primo = input()
secondo = input()
print(primo + secondo)
```

<p align="justify">Con input:</p>

```text
2
3
```

<p align="justify">produce:</p>

```text
23
```

## Versione B

```python
primo = int(input())
secondo = int(input())
print(primo + secondo)
```

<p align="justify">produce:</p>

```text
5
```

## Domanda

<p align="justify">Entrambi i programmi "funzionano" nel senso che Python li esegue.</p>

<p align="justify">Ma soltanto uno rispetta la specifica <strong>somma di due interi</strong>.</p>

<p align="justify">Quindi:</p>

<blockquote>
<p align="justify">programma eseguibile ≠ programma corretto rispetto al problema.</p>
</blockquote>

---

# 14. Error Clinic

<p align="justify">Gli errori fanno parte del lavoro del programmatore.</p>

## Caso 1 — errore di sintassi

```python
print("ciao"
```

<p align="justify">Python non riesce a interpretare correttamente la struttura del programma.</p>

<p align="justify">Non guardare cento righe a caso. Inizia dall'informazione che l'errore fornisce e dalla riga indicata, controllando anche ciò che la precede.</p>

## Caso 2 — nome non definito

```python
prezzo = 10
print(prezzo_totale)
```

<p align="justify">Hai assegnato un valore a <code>prezzo</code>, ma chiedi di usare <code>prezzo_totale</code>.</p>

<p align="justify">Python non corregge automaticamente il nome in base a ciò che probabilmente intendevi.</p>

## Caso 3 — conversione impossibile

```python
numero = int("ciao")
```

<p align="justify">La sintassi è valida, ma il valore non può essere convertito nel modo richiesto.</p>

## Caso 4 — errore logico

```python
primo = int(input())
secondo = int(input())
risultato = primo - secondo
print(risultato)
```

<p align="justify">Il programma può terminare senza traceback, ma non calcola ciò che la specifica chiede.</p>

<p align="justify">Questo è un punto fondamentale:</p>

```text
nessun errore Python
≠
soluzione corretta
```

<p align="justify">I casi di test ci aiutano a scoprirlo.</p>

---

# 15. Come leggere un traceback beginner

<p align="justify">Non devi capire subito ogni riga.</p>

<p align="justify">Per ora usa questa strategia:</p>

<ol>
  <li>individua il <strong>tipo di errore</strong> nell'ultima parte;</li>
  <li>leggi il messaggio;</li>
  <li>individua la riga del tuo file indicata;</li>
  <li>collega l'errore a ciò che quella riga sta tentando di fare;</li>
  <li>modifica una cosa alla volta;</li>
  <li>riesegui il caso che falliva.</li>
</ol>

<p align="justify">Esempio concettuale:</p>

```text
ValueError: invalid literal for int() ...
```

<p align="justify">Domanda utile:</p>

<blockquote>
<p align="justify">quale testo sto tentando di convertire in intero?</p>
</blockquote>

<p align="justify">Non:</p>

<blockquote>
<p align="justify">come faccio a far sparire il messaggio?</p>
</blockquote>

---

# 16. Output deterministico e TheBitLab

<p align="justify">In alcune Activity automatiche il contratto dice esattamente quale output deve produrre il programma.</p>

<p align="justify">Se la specifica è:</p>

```text
leggi due interi e stampa soltanto la somma
```

<p align="justify">questa soluzione è coerente:</p>

```python
primo = int(input())
secondo = int(input())
print(primo + secondo)
```

<p align="justify">Questa invece aggiunge output non richiesto:</p>

```python
primo = int(input("Inserisci il primo numero: "))
secondo = int(input("Inserisci il secondo numero: "))
print("La somma è", primo + secondo)
```

<p align="justify">In un'applicazione reale i prompt possono essere utilissimi. Qui, però, <strong>l'interfaccia testuale non è l'obiettivo</strong> e il test automatico deve poter confrontare input e output in modo deterministico.</p>

<p align="justify">La regola non è "non usare mai prompt".</p>

<p align="justify">La regola è:</p>

<blockquote>
<p align="justify">rispetta il contratto dell'interfaccia che stai implementando.</p>
</blockquote>

---

# 17. Activity B — Completa la somma

<p align="justify">Il primo vertical slice TheBitLab del corso è:</p>

```text
py2-activity-b-input-somma-001
```

<p align="justify">Ricevi uno starter simile a:</p>

```python
primo = int(input())
secondo = int(input())
risultato = 0
print(risultato)
```

<p align="justify">Devi modificare <strong>soltanto ciò che serve</strong> affinché rispetti la specifica.</p>

<p align="justify">Prima di eseguire, prevedi l'output per:</p>

```text
2, 3
0, 0
-4, 10
```

<p align="justify">Poi usa il report per confrontare il comportamento reale con quello atteso.</p>

## Perché è un'Activity B

<p align="justify">Non stai progettando ancora tutto il programma da zero.</p>

<p align="justify">Stai facendo una <strong>modifica controllata</strong> a una struttura già comprensibile.</p>

<p align="justify">In Activity successive passeremo a implementazione autonoma, debug e mini-progetti.</p>

---

# 18. Esercizi brevi

## A — Prevedi il tipo e il valore

<p align="justify">Senza REPL, scrivi prima la previsione:</p>

```python
3 + 4
"3" + "4"
int("8") + 2
str(5)
```

<p align="justify">Poi verifica.</p>

## B — Trova la differenza

<p align="justify">Spiega perché:</p>

```python
eta = input()
print(eta + "1")
```

<p align="justify">non significa "aumenta l'età di uno".</p>

<p align="justify">Scrivi poi la versione corretta per un'età intera.</p>

## C — Dal problema al codice

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Leggi un numero intero e mostra il suo doppio.</p>
</blockquote>

<p align="justify">Produci:</p>

<ol>
  <li>input;</li>
  <li>output;</li>
  <li>algoritmo;</li>
  <li>due casi di test;</li>
  <li>codice.</li>
</ol>

## D — Debug

<p align="justify">Correggi il programma:</p>

```python
prezzo = int(input())
quantita = int(input())
totale = prezzo + quantita
print(totale)
```

<p align="justify">se la specifica chiede il costo totale di <code>quantita</code> pezzi allo stesso prezzo.</p>

<p align="justify">Non limitarti a cambiare il simbolo: spiega perché.</p>

---

# 19. Verifica rapida

<p align="justify">Rispondi senza eseguire Python.</p>

<ol>
  <li>Che tipo restituisce <code>input()</code>?</li>
  <li>Che differenza c'è tra <code>42</code> e <code>"42"</code>?</li>
  <li>A cosa serve <code>int()</code> in <code>int(input())</code>?</li>
  <li>Perché il REPL mostra il risultato di <code>2 + 3</code>, mentre una riga <code>2 + 3</code> in uno script non produce necessariamente output visibile?</li>
  <li>Un programma senza traceback è sicuramente corretto? Perché?</li>
  <li>Qual è il primo passo utile quando compare un traceback?</li>
</ol>

<p align="justify">Dopo aver risposto, verifica con piccoli esperimenti soltanto le risposte di cui non sei sicuro.</p>

---

# 20. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
Python esegue il programma scritto, non quello immaginato.
```

```text
input() → str
```

```text
conversione solo quando serve al tipo di operazione
```

```text
REPL = esperimento rapido
script = programma salvato/ripetibile
```

```text
prevedi → esegui → confronta → correggi
```

```text
nessun traceback ≠ correttezza
```

<p align="justify">Nel prossimo modulo useremo espressioni e operatori con maggiore precisione e inizieremo a dare un nome a piccole trasformazioni tramite funzioni.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione e verifica tecnica usa:</p>

<ul>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — modello beginner, valori/variabili/funzioni/debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — coverage di tipi, espressioni e statement;</li>
  <li>documentazione Python 3.12 — tutorial, built-in <code>input</code>, <code>print</code>, <code>int</code>, <code>float</code>, <code>str</code>, <code>type</code>;</li>
  <li>Pluralsight Python Essentials — gap-check di percorso/laboratorio.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

## Activity correlate

<ul>
  <li><code>py2-activity-b-input-somma-001</code> — <strong>Completa la somma</strong>.</li>
</ul>

## Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_02_SPEC.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>;</li>
  <li><code>tracks/secondo/ARCHITECTURE_REVIEW.md</code>.</li>
</ul>

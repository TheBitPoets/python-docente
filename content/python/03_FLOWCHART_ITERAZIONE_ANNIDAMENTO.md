# M03 — Flow chart: iterazione, terminazione e annidamento

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
La ripetizione aggiunge al diagramma uno stato che cambia e una condizione di terminazione.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Leggere sequenze e selezioni e compilare una trace table come in M02.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
riconoscere quando una parte dell'algoritmo deve essere ripetuta;<br>rappresentare un ciclo controllato da una condizione;<br>rappresentare un ciclo controllato da un contatore a livello algoritmico; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Ogni passaggio nel rombo valuta la condizione con i valori correnti, non con quelli iniziali. Riprendi <a href="02_FLOWCHART_SEQUENZA_SELEZIONE.md">M02 — Flow chart: sequenza, input/output e selezione</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="04_INTERPRETE_REPL_VALORI_IO.md">M04 — Interprete, REPL, script, valori e input/output</a>. Gli algoritmi già tracciati vengono eseguiti dall&#x27;interprete, prima nel REPL e poi in uno script.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia un ciclo con zero, una e più iterazioni; individua l&#x27;aggiornamento che consente di uscire.
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
<p align="justify"><strong>Stato:</strong> draft<br>
<strong>UDA:</strong> PY2-01 — Problem solving, algoritmi e flow chart<br>
<strong>Delivery:</strong> Flowchart Lab candidate quando disponibile; fallback manuale sempre valido finché la capability non è classroom-certified</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>riconoscere quando una parte dell'algoritmo deve essere ripetuta;</li>
  <li>rappresentare un ciclo controllato da una condizione;</li>
  <li>rappresentare un ciclo controllato da un contatore a livello algoritmico;</li>
  <li>individuare inizializzazione, condizione, corpo e aggiornamento;</li>
  <li>spiegare perché un ciclo termina;</li>
  <li>usare una selezione dentro un ciclo e un ciclo dentro una selezione;</li>
  <li>leggere un primo ciclo annidato senza trasformarlo in una ricetta da memorizzare;</li>
  <li>progettare casi che rivelano off-by-one, aggiornamento mancante e mancata terminazione.</li>
</ul>

---

## 1. Quando una freccia torna indietro

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Chiedi un valore finché non è compreso tra 1 e 10.</p>
</blockquote>

<p align="justify">Una sequenza non basta, perché non sappiamo in anticipo quante volte l'utente fornirà un dato non valido.</p>

<p align="justify">Serve una ripetizione:</p>

```text
leggi valore
↓
valido?
  sì → continua
  no → torna a leggere
```

<p align="justify">La freccia che ritorna non significa “ripeti per sempre”.</p>

<p align="justify">Deve esistere una condizione che permette di uscire.</p>

---

## 2. Le quattro domande del ciclo

<p align="justify">Per ogni ciclo chiedi:</p>

```text
1. che stato esiste prima del ciclo?
2. quando il corpo deve essere eseguito?
3. che cosa cambia nel corpo?
4. perché prima o poi la condizione cambia abbastanza da uscire?
```

<p align="justify">Queste domande sono più importanti del nome che il futuro linguaggio userà per il ciclo.</p>

---

## 3. Ciclo controllato da condizione

<p align="justify">Pseudocodice:</p>

```text
LEGGI valore
MENTRE valore < 1 O valore > 10
    LEGGI valore
FINE MENTRE
MOSTRA "valido"
```

<p align="justify">Trace con input:</p>

```text
0
12
7
```

<table align="center">
<thead>
<tr>
<th>controllo</th>
<th>valore</th>
<th>invalido?</th>
<th>azione</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>sì</td>
<td>leggi ancora</td>
</tr>
<tr>
<td>2</td>
<td>12</td>
<td>sì</td>
<td>leggi ancora</td>
</tr>
<tr>
<td>3</td>
<td>7</td>
<td>no</td>
<td>esci</td>
</tr>
</tbody>
</table>

<p align="justify">Il numero di ripetizioni dipende dai dati.</p>

---

## 4. Aggiornamento mancante

<p align="justify">Algoritmo:</p>

```text
ASSEGNA i ← 0
MENTRE i < 3
    MOSTRA i
FINE MENTRE
```

<p align="justify">Che cosa cambia <code>i</code>?</p>

<p align="justify">Nulla.</p>

<p align="justify">La condizione <code>i &lt; 3</code> resta vera e il ciclo non termina.</p>

<p align="justify">Correzione:</p>

```text
ASSEGNA i ← i + 1
```

<p align="justify">nel punto appropriato del corpo.</p>

---

## 5. Contatore: stato che racconta quante volte

```text
ASSEGNA i ← 0
MENTRE i < 3
    MOSTRA i
    ASSEGNA i ← i + 1
FINE MENTRE
```

<p align="justify">Trace:</p>

<table align="center">
<thead>
<tr>
<th>passo ciclo</th>
<th>i prima</th>
<th>output</th>
<th>i dopo</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
</tbody>
</table>

<p align="justify">Al controllo successivo <code>3 &lt; 3</code> è falso.</p>

<p align="justify">Quindi il ciclo termina.</p>

---

## 6. Off-by-one

<p align="justify">Vogliamo mostrare:</p>

```text
1 2 3
```

<p align="justify">Confronta:</p>

```text
i ← 1
MENTRE i < 3
```

<p align="justify">con:</p>

```text
i ← 1
MENTRE i <= 3
```

<p align="justify">Una sola differenza nel confine cambia il numero di iterazioni.</p>

<p align="justify">Per i cicli i casi vicino al limite sono test fondamentali.</p>

---

## 7. Accumulatore concettuale

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Somma tre valori.</p>
</blockquote>

<p align="justify">Possiamo mantenere uno stato <code>totale</code>:</p>

```text
totale ← 0
contatore ← 0

MENTRE contatore < 3
    LEGGI valore
    totale ← totale + valore
    contatore ← contatore + 1
FINE MENTRE

MOSTRA totale
```

<p align="justify">Domanda guida:</p>

<blockquote>
<p align="justify">Che cosa significa <code>totale</code> dopo ogni iterazione?</p>
</blockquote>

<p align="justify">Risposta utile:</p>

<blockquote>
<p align="justify">contiene la somma dei valori letti <strong>finora</strong>.</p>
</blockquote>

<p align="justify">Questa spiegazione vale più della memorizzazione di un pattern.</p>

---

## 8. Selezione dentro un ciclo

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi 5 numeri e conta quanti sono positivi.</p>
</blockquote>

<p align="justify">Struttura:</p>

```text
ripeti per 5 valori
    leggi valore
    se valore > 0
        incrementa conteggio
```

<p align="justify">Il ciclo decide <strong>quante volte osservare</strong>.</p>

<p align="justify">La selezione decide <strong>se aggiornare lo stato</strong> per quel dato.</p>

<p align="justify">Sono due responsabilità diverse.</p>

---

## 9. Ciclo dentro una selezione

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Se l'utente sceglie “esegui”, ripeti un'operazione 3 volte; altrimenti termina.</p>
</blockquote>

<p align="justify">Qui la decisione avviene prima:</p>

```text
scelta == "esegui"?
 true → ciclo
 false → end
```

<p align="justify">Non esiste una regola “il ciclo va sempre fuori” o “la decisione va sempre dentro”.</p>

<p align="justify">La struttura dipende dal problema.</p>

---

## 10. Primo ciclo annidato

<p align="justify">Una piccola griglia 2 × 3 può essere descritta così:</p>

```text
per ogni riga
    per ogni colonna
        visita cella
```

<p align="justify">A livello di flow chart possiamo rappresentare due stati:</p>

```text
riga
colonna
```

<p align="justify">Il ciclo interno completa le colonne di una riga; poi il ciclo esterno passa alla riga successiva.</p>

<p align="justify">Non serve ancora formalizzare complessità Big-O.</p>

<p align="justify">Domanda intuitiva:</p>

<blockquote>
<p align="justify">Se raddoppio righe e colonne, quante più celle devo visitare?</p>
</blockquote>

---

## 11. Trace di cicli annidati

<p align="justify">Per 2 righe × 2 colonne:</p>

<table align="center">
<thead>
<tr>
<th>riga</th>
<th>colonna</th>
<th>cella visitata</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0</td>
<td>(0,0)</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>(0,1)</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>(1,0)</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>(1,1)</td>
</tr>
</tbody>
</table>

<p align="justify">Se perdi il filo, non indovinare: costruisci una tabella.</p>

---

## 12. Flowchart Lab e step limit

<p align="justify">Il Flowchart Lab candidate può eseguire diagrammi e produrre un trace deterministico.</p>

<p align="justify">Per sicurezza esiste un limite massimo di step.</p>

<p align="justify">Un risultato <code>limit-exceeded</code> non dimostra automaticamente quale sia il bug, ma è evidence che il diagramma non ha raggiunto <code>end</code> entro il limite previsto.</p>

<p align="justify">Il lavoro dello studente resta:</p>

<ol>
  <li>trovare il ciclo coinvolto;</li>
  <li>osservare stato e condizione;</li>
  <li>individuare ciò che non cambia come previsto;</li>
  <li>correggere il modello.</li>
</ol>

## Fallback manuale obbligatorio

<p align="justify">Finché <code>flowchart.lab.v1</code> non è classroom-certified, lo stesso esercizio deve poter essere svolto senza il tool usando:</p>

```text
carta / lavagna / template
+ pseudocodice
+ trace table
+ casi di test
+ rubric docente
```

<p align="justify">Il fallback manuale non è un corso diverso: preserva gli stessi outcome di algoritmo, terminazione, trace e debug.</p>

---

## 13. Error Clinic — ciclo infinito

<p align="justify">Cerca uno di questi segnali:</p>

<ul>
  <li>aggiornamento assente;</li>
  <li>aggiornamento nella direzione sbagliata;</li>
  <li>condizione che non può diventare falsa;</li>
  <li>ritorno grafico collegato al nodo sbagliato.</li>
</ul>

<p align="justify">Non correggere “a tentativi”.</p>

<p align="justify">Usa il trace degli ultimi step disponibili.</p>

---

## 14. Error Clinic — inizializzazione nel posto sbagliato

<p align="justify">Vogliamo contare eventi:</p>

```text
conteggio ← 0
MENTRE ...
    ...
    conteggio ← conteggio + 1
FINE MENTRE
```

<p align="justify">Errore:</p>

```text
MENTRE ...
    conteggio ← 0
    conteggio ← conteggio + 1
FINE MENTRE
```

<p align="justify">Il contatore viene azzerato a ogni iterazione.</p>

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">Quale significato avrebbe dovuto mantenere da un giro al successivo?</p>
</blockquote>

---

## 15. Controlled Change

<p align="justify">Diagramma iniziale:</p>

<blockquote>
<p align="justify">mostra i valori da 0 a 2.</p>
</blockquote>

<p align="justify">Modifica richiesta:</p>

<blockquote>
<p align="justify">mostra i valori da 0 a 4.</p>
</blockquote>

<p align="justify">Cambia soltanto il confine necessario e aggiorna i test attesi.</p>

<p align="justify">Poi prova una seconda modifica:</p>

<blockquote>
<p align="justify">mostra da 1 a 5.</p>
</blockquote>

<p align="justify">Questa volta potrebbe servire cambiare sia inizializzazione sia condizione.</p>

---

## 16. Mini-project — missione su griglia

<p align="justify">Progetta una piccola missione algoritmica senza API Python e senza hardware obbligatorio.</p>

<p align="justify">Esempio:</p>

<blockquote>
<p align="justify">Un robot concettuale percorre una riga di 5 celle. Per ogni cella legge se è libera; conta gli ostacoli e termina dopo l'ultima cella.</p>
</blockquote>

<p align="justify">Consegna:</p>

```text
specifica sintetica
input/output
flow chart
trace su almeno 2 casi
1 caso limite
spiegazione della terminazione
```

<p align="justify">Romeo può essere solo scenario motivante: questa UDA non dipende da <code>romeo-sim</code>.</p>

---

## 17. Exit checkpoint PY2-01

<p align="justify">Prima di passare al primo programma Python dovresti riuscire a:</p>

<ol>
  <li>identificare input/output/vincoli;</li>
  <li>scrivere pseudocodice leggibile;</li>
  <li>costruire una sequenza;</li>
  <li>costruire una selezione;</li>
  <li>costruire un ciclo con inizializzazione/condizione/aggiornamento;</li>
  <li>seguire il diagramma con un trace;</li>
  <li>trovare almeno un caso limite;</li>
  <li>spiegare perché il diagramma termina;</li>
  <li>diagnosticare un errore evidente in un algoritmo altrui.</li>
</ol>

<p align="justify">Non è richiesta perfezione grafica.</p>

## Recap

```text
problema
→ algoritmo
→ flow chart
→ trace
→ test
→ debug
```

<p align="justify">Nel prossimo modulo useremo Python per tradurre procedure che sappiamo già leggere, simulare e verificare.</p>

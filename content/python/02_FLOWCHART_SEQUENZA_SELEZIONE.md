# M02 — Flow chart: sequenza, input/output e selezione

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
I passi e le decisioni diventano un diagramma di flusso leggibile anche senza computer.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Saper scomporre una consegna ed eseguire un dry-run come in M01.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
leggere i simboli fondamentali di un diagramma di flusso;<br>costruire una sequenza con input, elaborazione e output;<br>rappresentare una decisione booleana; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il diagramma rappresenta lo stesso algoritmo dello pseudocodice: cambia la notazione, non il risultato atteso. Riprendi <a href="01_DAL_PROBLEMA_AI_PASSI.md">M01 — Dal problema ai passi: specifica, pseudocodice e trace</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md">M03 — Flow chart: iterazione, terminazione e annidamento</a>. La ripetizione aggiunge al diagramma uno stato che cambia e una condizione di terminazione.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Disegna la selezione sulla soglia e segui entrambi i rami con due input concreti, su carta o nel Flowchart Lab disponibile.
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
  <li>leggere i simboli fondamentali di un diagramma di flusso;</li>
  <li>costruire una sequenza con input, elaborazione e output;</li>
  <li>rappresentare una decisione booleana;</li>
  <li>costruire selezione semplice e doppia;</li>
  <li>seguire un diagramma passo-passo con dati concreti;</li>
  <li>compilare una trace table elementare;</li>
  <li>diagnosticare rami mancanti, condizioni invertite e output collocati nel punto sbagliato;</li>
  <li>salvare, quando il Flowchart Lab è disponibile, l'artifact gestito <code>algorithm.flow.json</code> senza confondere la validità strutturale con la qualità dell'algoritmo.</li>
</ul>

---

## 1. Perché un diagramma?

<p align="justify">Lo pseudocodice descrive i passi con testo.</p>

<p align="justify">Un flow chart rende visibile il <strong>flusso di controllo</strong>:</p>

```text
inizio
  ↓
input
  ↓
calcolo
  ↓
decisione
 ↙      ↘
...     ...
```

<p align="justify">Non serve a “decorare” l'algoritmo. Serve a mostrare:</p>

<ul>
  <li>che cosa succede prima e dopo;</li>
  <li>dove il flusso si divide;</li>
  <li>dove i rami si ricongiungono;</li>
  <li>se ogni percorso può arrivare a una conclusione.</li>
</ul>

---

## 2. Simboli core del corso

<p align="justify">Usiamo un insieme piccolo e stabile.</p>

<table align="center">
<thead>
<tr>
<th>Idea</th>
<th>Forma convenzionale</th>
<th>Significato</th>
</tr>
</thead>
<tbody>
<tr>
<td>start/end</td>
<td>terminatore</td>
<td>inizio/fine</td>
</tr>
<tr>
<td>input/output</td>
<td>parallelogramma</td>
<td>dato acquisito o mostrato</td>
</tr>
<tr>
<td>processing</td>
<td>rettangolo</td>
<td>calcolo/assegnamento</td>
</tr>
<tr>
<td>decision</td>
<td>rombo</td>
<td>condizione con rami</td>
</tr>
<tr>
<td>freccia</td>
<td>collegamento</td>
<td>prossimo passo</td>
</tr>
</tbody>
</table>

<p align="justify">La forma grafica aiuta, ma la correttezza dipende soprattutto dal significato dei nodi e dei collegamenti.</p>

---

## 3. Prima sequenza

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi due numeri e mostra la loro somma.</p>
</blockquote>

<p align="justify">Modello:</p>

```text
START
  ↓
INPUT A
  ↓
INPUT B
  ↓
SOMMA ← A + B
  ↓
OUTPUT SOMMA
  ↓
END
```

<p align="justify">Ogni passo ha un solo successore.</p>

<p align="justify">Questa è una <strong>sequenza</strong>.</p>

---

## 4. Trace della sequenza

<p align="justify">Con input <code>2</code> e <code>3</code>:</p>

<table align="center">
<thead>
<tr>
<th>nodo</th>
<th>A</th>
<th>B</th>
<th>somma</th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr>
<td>start</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>input A</td>
<td>2</td>
<td>—</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>input B</td>
<td>2</td>
<td>3</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>calcolo</td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>—</td>
</tr>
<tr>
<td>output</td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>5</td>
</tr>
</tbody>
</table>

<p align="justify">Il diagramma non sostituisce il trace: ci dice <strong>dove andare</strong>, il trace mostra <strong>che cosa succede ai dati</strong>.</p>

---

## 5. La decisione

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi una temperatura e indica se supera 30.</p>
</blockquote>

<p align="justify">La condizione è:</p>

```text
temperatura > 30 ?
```

<p align="justify">Dal rombo partono due possibilità:</p>

```text
           temperatura > 30?
              /      \
           true      false
            /          \
     "sopra soglia"  "entro soglia"
```

<p align="justify">Una condizione deve poter essere valutata come vera o falsa nel punto in cui viene usata.</p>

---

## 6. Selezione doppia

<p align="justify">Nel nostro Flowchart Lab i rami di una decisione sono espliciti:</p>

```text
true
false
```

<p align="justify">Per la soglia:</p>

```text
START
 ↓
INPUT temperatura
 ↓
[temperatura > 30?]
  true ↙       ↘ false
OUTPUT alta   OUTPUT normale
       ↘       ↙
          END
```

<p align="justify">Domanda importante:</p>

<blockquote>
<p align="justify">Tutti i possibili input seguono uno dei due rami?</p>
</blockquote>

<p align="justify">Per una condizione booleana sì: o è vera o è falsa.</p>

---

## 7. Selezione semplice

<p align="justify">A volte un ramo non richiede un'azione specifica.</p>

<p align="justify">Esempio:</p>

<blockquote>
<p align="justify">Se il saldo è negativo, mostra un avviso; poi continua.</p>
</blockquote>

```text
[saldo < 0?]
 true ↙     ↘ false
AVVISO       |
     \       /
      prossimo passo
```

<p align="justify">Anche quando un ramo “non fa nulla”, il flusso deve restare chiaro.</p>

---

## 8. Condizione invertita

<p align="justify">Specificazione:</p>

<blockquote>
<p align="justify">Mostra “ammesso” se età &gt;= 14.</p>
</blockquote>

<p align="justify">Diagramma sbagliato:</p>

```text
età >= 14?
true  → "non ammesso"
false → "ammesso"
```

<p align="justify">Il diagramma può essere strutturalmente valido ma semanticamente sbagliato.</p>

<p align="justify">Questo è un punto fondamentale:</p>

```text
file/schema valido ≠ algoritmo corretto
```

<p align="justify">Per questo la qualità dell'algoritmo resta evidence/rubric docente.</p>

---

## 9. Output troppo presto

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Applica uno sconto se il prezzo supera 100, poi mostra il prezzo finale.</p>
</blockquote>

<p align="justify">Errore:</p>

```text
INPUT prezzo
↓
OUTPUT prezzo
↓
decisione sconto
```

<p align="justify">Il risultato viene mostrato <strong>prima</strong> della decisione che dovrebbe modificarlo.</p>

<p align="justify">Il trace individua immediatamente il primo punto di divergenza.</p>

---

## 10. Più casi

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Classifica un valore come negativo, zero o positivo.</p>
</blockquote>

<p align="justify">Possiamo usare due decisioni:</p>

```text
n < 0?
 true → negativo
 false → n == 0?
          true → zero
          false → positivo
```

<p align="justify">Non abbiamo bisogno di un nuovo simbolo per ogni possibile problema.</p>

<p align="justify">Componiamo poche primitive chiare.</p>

---

## 11. Flowchart Lab: che cosa deve fare per noi

<p align="justify">Quando il runtime managed è disponibile, il percorso è:</p>

```text
TheBitLab
→ Flowchart Lab locale
→ browser UI
→ diagramma
→ Run / Step / Reset
→ variable watch
→ algorithm.flow.json nel workspace
```

<p align="justify">Il browser non esegue Python dello studente.</p>

<p align="justify">Il motore usa un linguaggio di espressioni ristretto e deterministico.</p>

## Importante

<p align="justify">Finché <code>flowchart.lab.v1</code> non è certificata nei profili classroom, il corso mantiene il fallback:</p>

```text
carta / lavagna / template
+ trace table
+ casi di test
+ rubric docente
```

<p align="justify">Gli outcome didattici non dipendono dalla disponibilità del tool.</p>

---

## 12. Save non significa “consegna perfetta”

<p align="justify">Il Flowchart Lab può verificare cose deterministiche:</p>

<ul>
  <li>schema valido;</li>
  <li>nodi e archi coerenti;</li>
  <li>esecuzione terminata entro il limite;</li>
  <li>output/trace per input dichiarati.</li>
</ul>

<p align="justify">Non può assegnare automaticamente un voto affidabile a:</p>

<ul>
  <li>chiarezza della decomposizione;</li>
  <li>scelta più appropriata dei costrutti;</li>
  <li>semplicità del diagramma;</li>
  <li>qualità della spiegazione.</li>
</ul>

<p align="justify">Questi aspetti restano manuali.</p>

---

## 13. Laboratorio guidato — soglia

<p align="justify">Costruisci il diagramma:</p>

<blockquote>
<p align="justify">Leggi <code>temperatura</code>. Se è maggiore di 30 mostra “sopra soglia”, altrimenti mostra “entro soglia”.</p>
</blockquote>

<p align="justify">Prima di eseguirlo, prepara i test:</p>

```text
31 → sopra soglia
30 → entro soglia
29 → entro soglia
```

<p align="justify">Perché 30 è il caso più importante da non dimenticare?</p>

---

## 14. Controlled Change

<p align="justify">Parti dal diagramma funzionante e cambia soltanto:</p>

```text
soglia 30 → soglia 25
```

<p align="justify">Poi aggiorna i casi di test.</p>

<p align="justify">Obiettivo:</p>

<blockquote>
<p align="justify">modificare il requisito senza ridisegnare parti non coinvolte.</p>
</blockquote>

---

## 15. Error Clinic

<p align="justify">Diagnostica uno alla volta:</p>

<ol>
  <li>ramo <code>false</code> mancante;</li>
  <li>condizione invertita;</li>
  <li>output prima dell'assegnamento;</li>
  <li>nodo non raggiungibile;</li>
  <li>ramo che non arriva a <code>end</code>;</li>
  <li>trace atteso diverso dall'esecuzione.</li>
</ol>

<p align="justify">Per ogni errore scrivi:</p>

```text
sintomo
primo nodo problematico
modifica minima
caso che lo rivela
```

---

## Minimum mastery checkpoint

<p align="justify">Dovresti saper:</p>

<ol>
  <li>riconoscere start/end, input/output, processing e decision;</li>
  <li>costruire una sequenza;</li>
  <li>costruire una selezione doppia;</li>
  <li>seguire true/false con un input concreto;</li>
  <li>compilare una trace table;</li>
  <li>progettare almeno un test sul confine;</li>
  <li>distinguere validità strutturale e correttezza semantica;</li>
  <li>usare il fallback manuale senza perdere gli outcome se il tool non è disponibile.</li>
</ol>

## Recap

```text
sequenza → un percorso
selezione → il flusso sceglie un ramo
trace → rende visibile stato e percorso
test → prova casi diversi, soprattutto i confini
```

<p align="justify">Prossimo modulo: introduciamo ripetizione, terminazione e annidamento nei diagrammi.</p>

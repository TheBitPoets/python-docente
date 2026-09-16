# M09 — `while`, stato, sentinelle e validazione ripetuta

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il while ripete un lavoro finché lo stato soddisfa una condizione, anche quando il numero di ripetizioni non è noto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Costruire condizioni e validare un valore con selezioni come in M06–M08.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare che <code>while</code> ripete un blocco finché una condizione resta vera;<br>identificare stato iniziale, condizione, corpo e aggiornamento;<br>eseguire il trace di un ciclo <code>while</code>; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il ciclo algoritmico di M03 aveva già inizializzazione, test, corpo e aggiornamento. Riprendi <a href="08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md">M08 — Selezioni annidate, validazione e refactoring</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="10_FOR_RANGE_SCELTA_CICLO.md">M10 — <code>for</code>, <code>range</code> e scelta <code>for</code> vs <code>while</code></a>. Il for attraversa valori; range rende espliciti inizio, limite escluso e passo.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia la validazione ripetuta e una sequenza con sentinella, includendo l&#x27;uscita al primo controllo.
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
  <li>spiegare che <code>while</code> ripete un blocco finché una condizione resta vera;</li>
  <li>identificare stato iniziale, condizione, corpo e aggiornamento;</li>
  <li>eseguire il trace di un ciclo <code>while</code>;</li>
  <li>spiegare quale valore deve cambiare perché il ciclo possa terminare;</li>
  <li>riconoscere un ciclo infinito e un aggiornamento mancante;</li>
  <li>usare un contatore in un <code>while</code>;</li>
  <li>ripetere una richiesta finché un valore rientra nel dominio valido;</li>
  <li>usare una sentinella per indicare la fine di una sequenza di input;</li>
  <li>distinguere condizione di continuazione e condizione di uscita;</li>
  <li>progettare test con zero, una e più iterazioni quando il problema lo consente;</li>
  <li>usare <code>while True</code>/<code>break</code> soltanto dopo aver compreso e motivato la condizione di terminazione.</li>
</ul>

## Prerequisiti

<p align="justify">Da PY2-03 dovresti già saper:</p>

<ul>
  <li>costruire condizioni con confronti, <code>and</code>, <code>or</code>, <code>not</code>;</li>
  <li>validare un valore con <code>if/else</code>;</li>
  <li>fare path trace;</li>
  <li>distinguere dato fuori dominio da errore di conversione;</li>
  <li>progettare casi di test sui confini.</li>
</ul>

---

## 1. Problema iniziale: chiedi di nuovo finché il voto è valido

<p align="justify">In M08 sapevamo fare questo:</p>

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    print("dato valido")
```

<p align="justify">Ma la specifica ora cambia:</p>

<blockquote>
<p align="justify">Continua a chiedere un voto finché l'utente inserisce un intero tra 0 e 10.</p>
</blockquote>

<p align="justify">Non basta più una decisione eseguita una sola volta.</p>

<p align="justify">Serve una <strong>ripetizione controllata da una condizione</strong>.</p>

---

## 2. Il modello del `while`

<p align="justify">Schema:</p>

```text
stato iniziale
     ↓
condizione? ── False ──> fine
     |
    True
     ↓
   corpo
     ↓
aggiornamento dello stato
     └───────────────↺
```

<p align="justify">In Python:</p>

```python
while condizione:
    corpo
```

<p align="justify">Il corpo viene ripetuto finché la condizione continua a produrre <code>True</code>.</p>

---

## 3. Primo ciclo con contatore

```python
i = 0

while i < 3:
    print(i)
    i = i + 1
```

<p align="justify">Output:</p>

```text
0
1
2
```

<p align="justify">Quattro parti da riconoscere:</p>

```text
inizializzazione → i = 0
condizione       → i < 3
corpo            → print(i)
aggiornamento    → i = i + 1
```

---

## 4. Trace riga per riga

<p align="justify">Per:</p>

```python
i = 0
while i < 3:
    print(i)
    i = i + 1
```

<table align="center">
<thead>
<tr>
<th>controllo</th>
<th><code>i</code> prima</th>
<th><code>i &lt; 3</code></th>
<th>output</th>
<th><code>i</code> dopo aggiornamento</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>True</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>True</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>3</td>
<td>False</td>
<td>—</td>
<td>—</td>
</tr>
</tbody>
</table>

<p align="justify">L'ultimo controllo esiste anche se il corpo non viene più eseguito.</p>

---

## 5. Domanda obbligatoria: “perché questo ciclo può finire?”

<p align="justify">Nel ciclo precedente:</p>

```text
i parte da 0
→ ogni iterazione aumenta di 1
→ prima o poi i < 3 diventa False
```

<p align="justify">Ogni volta che scrivi un <code>while</code>, devi saper rispondere:</p>

<ol>
  <li>quale parte della condizione dipende dallo stato?</li>
  <li>quale istruzione cambia quello stato?</li>
  <li>esiste un percorso in cui l'aggiornamento non avviene?</li>
  <li>può la condizione diventare falsa?</li>
</ol>

<p align="justify">Questa è una regola di progettazione, non soltanto di debugging.</p>

---

## 6. Ciclo infinito: aggiornamento mancante

<p align="justify">Bug:</p>

```python
i = 0

while i < 3:
    print(i)
```

<p align="justify"><code>i</code> resta sempre <code>0</code>.</p>

<p align="justify">Quindi:</p>

```text
0 < 3 → True
```

<p align="justify">continua a essere vero.</p>

<p align="justify">Il problema non è “Python si è bloccato”: il programma non contiene alcun meccanismo che renda falsa la condizione.</p>

---

## 7. Zero iterazioni è un comportamento valido

```python
i = 5

while i < 3:
    print(i)
```

<p align="justify">La condizione iniziale è subito <code>False</code>.</p>

<p align="justify">Il corpo viene eseguito <strong>zero volte</strong>.</p>

<p align="justify">Per questo i test di un <code>while</code> devono considerare, quando la specifica lo permette:</p>

```text
zero iterazioni
una iterazione
più iterazioni
```

---

## 8. Validazione ripetuta

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Leggi un voto finché è compreso tra 0 e 10.</p>
</blockquote>

```python
voto = int(input())

while voto < 0 or voto > 10:
    voto = int(input())

print(voto)
```

<p align="justify">Modello:</p>

```text
leggi
→ non valido?
    sì → leggi di nuovo
    no → continua dopo il ciclo
```

<p align="justify">Il nuovo input è l'aggiornamento dello stato.</p>

---

## 9. Trace della validazione

<p align="justify">Input forniti, uno dopo l'altro:</p>

```text
12
-1
7
```

<p align="justify">Trace:</p>

```text
voto = 12
12 fuori 0..10 → True  → nuova lettura

voto = -1
-1 fuori 0..10 → True  → nuova lettura

voto = 7
7 fuori 0..10 → False → fine ciclo
```

<p align="justify">Output finale:</p>

```text
7
```

<p align="justify">Il numero di iterazioni non era noto in anticipo.</p>

---

## 10. Condizione di continuazione vs condizione di uscita

<p align="justify">Nel codice:</p>

```python
while voto < 0 or voto > 10:
    voto = int(input())
```

<p align="justify">la condizione dice:</p>

<blockquote>
<p align="justify"><strong>continua</strong> mentre il voto è invalido.</p>
</blockquote>

<p align="justify">La condizione di uscita equivalente, in linguaggio naturale, è:</p>

<blockquote>
<p align="justify">esci quando <code>0 &lt;= voto &lt;= 10</code>.</p>
</blockquote>

<p align="justify">Non confondere le due frasi.</p>

<p align="justify">Se la specifica dice “ripeti finché non è valido”, prima scrivi chiaramente quale condizione mantiene attivo il ciclo.</p>

---

## 11. Variante con booleano nominato

<p align="justify">Possiamo scrivere:</p>

```python
voto = int(input())
voto_non_valido = voto < 0 or voto > 10

while voto_non_valido:
    voto = int(input())
    voto_non_valido = voto < 0 or voto > 10
```

<p align="justify">È corretto, ma introduce un obbligo in più:</p>

<blockquote>
<p align="justify">aggiornare anche <code>voto_non_valido</code> ogni volta che cambia <code>voto</code>.</p>
</blockquote>

<p align="justify">Nel problema semplice la condizione diretta è più difficile da desincronizzare:</p>

```python
while voto < 0 or voto > 10:
```

<p align="justify">Un nome booleano è utile quando aggiunge significato senza creare stato duplicato inutile.</p>

---

## 12. Sentinella: un valore che segnala “fine”

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi numeri e stampali. Il valore <code>-1</code> indica che l'inserimento è terminato e non deve essere elaborato.</p>
</blockquote>

<p align="justify">Schema:</p>

```text
leggi valore
finché valore != -1:
    elabora valore
    leggi nuovo valore
```

<p align="justify">Python:</p>

```python
numero = int(input())

while numero != -1:
    print(numero)
    numero = int(input())
```

<p align="justify"><code>-1</code> è la <strong>sentinella</strong>.</p>

---

## 13. La sentinella deve essere fuori dai dati normali

<p align="justify">Se <code>-1</code> è un valore valido del dominio, usarlo come segnale di fine crea ambiguità.</p>

<p align="justify">Prima di scegliere una sentinella chiediti:</p>

```text
può comparire come dato normale?
```

<p align="justify">In esercizi scolastici la specifica dichiarerà chiaramente il valore sentinella.</p>

<p align="justify">In applicazioni reali esistono molte altre forme di terminazione; qui impariamo il pattern.</p>

---

## 14. Trace della sentinella

<p align="justify">Input:</p>

```text
4
8
-1
```

<table align="center">
<thead>
<tr>
<th>valore letto</th>
<th><code>numero != -1</code></th>
<th>elaborato?</th>
<th>nuova lettura?</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td>True</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>8</td>
<td>True</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>-1</td>
<td>False</td>
<td>no</td>
<td>no</td>
</tr>
</tbody>
</table>

<p align="justify">Il valore di fine controlla il ciclo ma non viene elaborato.</p>

---

## 15. Error Clinic: aggiornamento solo in un ramo

<p align="justify">Bug:</p>

```python
numero = int(input())

while numero != -1:
    if numero > 0:
        print(numero)
        numero = int(input())
```

<p align="justify">Che succede se <code>numero</code> vale <code>0</code>?</p>

```text
numero != -1 → True
numero > 0   → False
nuova lettura → non avviene
numero resta 0
```

<p align="justify">Il ciclo diventa infinito.</p>

<p align="justify">L'aggiornamento deve avvenire su tutti i percorsi che devono far progredire il ciclo.</p>

---

## 16. Error Clinic: condizione invertita

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">ripeti mentre il voto è fuori 0..10.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
while 0 <= voto <= 10:
    voto = int(input())
```

<p align="justify">Questa condizione ripete <strong>quando il voto è valido</strong>.</p>

<p align="justify">Prima del codice verbalizza sempre:</p>

```text
quando devo continuare?
```

---

## 17. Error Clinic: off-by-one con contatore

<p align="justify">Obiettivo:</p>

<blockquote>
<p align="justify">stampa <code>0</code>, <code>1</code>, <code>2</code>.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
i = 0
while i <= 3:
    print(i)
    i += 1
```

<p align="justify">Produce anche <code>3</code>.</p>

<p align="justify">I test del primo/ultimo valore sono fondamentali anche nei cicli.</p>

---

## 18. `while True` e `break`: non come scorciatoia iniziale

<p align="justify">Python permette:</p>

```python
while True:
    voto = int(input())
    if 0 <= voto <= 10:
        break
```

<p align="justify">Questa forma può essere utile quando la condizione di uscita emerge naturalmente <strong>dentro</strong> il corpo.</p>

<p align="justify">Ma non è il nostro modello introduttivo primario.</p>

<p align="justify">Prima devi saper progettare:</p>

```text
stato
condizione
aggiornamento
terminazione
```

<p align="justify">Regola:</p>

<blockquote>
<p align="justify"><code>while True</code> non serve a evitare di pensare alla condizione di fine.</p>
</blockquote>

<p align="justify">Se usi <code>break</code>, devi indicare con precisione quale percorso lo raggiunge e perché.</p>

---

## 19. Confronto di due validazioni

<p align="justify">Versione A:</p>

```python
voto = int(input())
while voto < 0 or voto > 10:
    voto = int(input())
```

<p align="justify">Versione B:</p>

```python
while True:
    voto = int(input())
    if 0 <= voto <= 10:
        break
```

<p align="justify">Entrambe possono essere corrette.</p>

<p align="justify">Per il primo apprendimento preferiamo A perché rende la condizione di continuazione visibile nella testata del ciclo.</p>

<p align="justify">B diventa utile quando il flusso interno rende più chiara l'uscita.</p>

<p align="justify">La scelta va motivata, non trasformata in una regola assoluta.</p>

---

## 20. Microscope: individua le quattro parti

<p align="justify">Per ciascun ciclo identifica:</p>

```text
stato iniziale
condizione
corpo
aggiornamento
```

#### A

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

#### B

```python
parola = input()
while parola != "fine":
    print(parola)
    parola = input()
```

<p align="justify">Poi rispondi:</p>

<blockquote>
<p align="justify">quale valore può rendere falsa la condizione?</p>
</blockquote>

---

## 21. Romeo: ripetizione controllata nel simulatore

<p align="justify">Romeo può rendere visibile un ciclo, ma soltanto dopo il modello generale.</p>

<p align="justify">Il repo Romeo pinned contiene attività su <code>while</code> e simulazione deterministica, ad esempio:</p>

```text
romeo-y1-u16-ciclo-while
```

<p align="justify">Uso didattico possibile:</p>

```text
contatore/stato
→ invia un numero controllato di comandi
→ terminazione
→ stop
```

<p align="justify">Il simulatore deve essere certificato nel Classroom Environment prima di diventare delivery obbligatoria. Hardware fisico non è richiesto.</p>

---

## 22. Activity planning — M09

<p align="justify">Candidati, senza materializzare ancora una nuova Activity P1:</p>

#### A — Trace

<p align="justify">Compilare tabella iterazione/stato/condizione/output.</p>

#### B — Controlled Change

<p align="justify">Cambiare limiti di una validazione e aggiornare i test.</p>

#### C — Implement

<p align="justify">Richiedere un valore finché appartiene a un intervallo valido.</p>

#### D — Debug

<p align="justify">Correggere:</p>

<ul>
  <li>aggiornamento mancante;</li>
  <li>aggiornamento in un solo ramo;</li>
  <li>condizione invertita;</li>
  <li>inizializzazione errata;</li>
  <li>off-by-one;</li>
  <li>sentinella elaborata per errore.</li>
</ul>

<p align="justify">M04 resta il canarino P1 fino alla certificazione <code>python-docente#7</code>.</p>

---

## 23. Esercizi brevi

### A — Trace contatore

<p align="justify">Prevedi l'output:</p>

```python
i = 2
while i < 6:
    print(i)
    i += 2
```

### B — Validazione

<p align="justify">Leggi un intero finché è compreso tra <code>1</code> e <code>5</code> inclusi. Progetta una sequenza di input che provochi:</p>

```text
zero ripetizioni
una ripetizione
tre ripetizioni
```

### C — Sentinella

<p align="justify">Leggi parole finché non compare <code>stop</code>; stampa ogni parola normale, ma non la sentinella.</p>

### D — Debug terminazione

<p align="justify">Trova un input che rende infinito il programma:</p>

```python
x = int(input())
while x != 0:
    if x > 0:
        x -= 1
```

<p align="justify">Spiega perché.</p>

---

## 24. Checkpoint M09

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Che cosa significa “<code>while</code> ripete finché la condizione è vera”?</li>
  <li>Quali sono le quattro parti del nostro modello di ciclo?</li>
  <li>Perché <code>i = 0; while i &lt; 3:</code> richiede un aggiornamento di <code>i</code>?</li>
  <li>Che cosa significa zero iterazioni?</li>
  <li>Qual è l'aggiornamento nella validazione ripetuta del voto?</li>
  <li>Che differenza c'è tra condizione di continuazione e condizione di uscita?</li>
  <li>Che cos'è una sentinella?</li>
  <li>Perché una sentinella deve essere distinguibile dai dati normali?</li>
  <li>Perché un aggiornamento presente solo in un ramo può creare un ciclo infinito?</li>
  <li>Perché <code>while True</code> non deve essere una scorciatoia per evitare di progettare la terminazione?</li>
</ol>

---

## 25. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
while → ripeti finché una condizione resta vera
```

```text
stato iniziale
→ condizione
→ corpo
→ aggiornamento
→ nuovo controllo
```

```text
ogni while → deve avere una storia di terminazione
```

```text
validazione ripetuta → controlla / rileggi / ricontrolla
```

```text
sentinella → valore che segnala la fine
```

<p align="justify">Nel prossimo modulo confronteremo <code>while</code> con <code>for</code>: quando sappiamo già quali valori/iterazioni attraversare, <code>for</code> spesso comunica meglio l'intenzione e riduce gli errori di gestione manuale del contatore.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione/verifica:</p>

<ul>
  <li>documentazione Python 3.12 — <code>while</code>, <code>break</code>, control flow;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — iteration, reassignment, debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — loops and control-flow semantics;</li>
  <li>Romeo pinned <code>45e5f7e131802fccc89358a23a25dbed1884bbfa</code> — <code>y1-u16-ciclo-while</code> come riferimento applicativo.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

### Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_04_SPEC.md</code>;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>.</li>
</ul>

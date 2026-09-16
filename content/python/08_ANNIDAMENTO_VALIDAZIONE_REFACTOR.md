# M08 — Selezioni annidate, validazione e refactoring

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
La validazione stabilisce quando una seconda decisione ha senso e guida un refactoring verificabile.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Leggere if/elif/else, condizioni composte e intervalli da M06–M07.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
leggere e scrivere una selezione annidata semplice;<br>seguire il percorso dei rami con un trace;<br>riconoscere quando una seconda decisione dipende davvero dalla prima; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Un ramo non percorso non esegue le istruzioni che contiene; conta la dipendenza fra decisioni. Riprendi <a href="07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md">M07 — <code>elif</code>, casi esclusivi e condizioni composte</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md">M09 — <code>while</code>, stato, sentinelle e validazione ripetuta</a>. Il while ripete un lavoro finché lo stato soddisfa una condizione, anche quando il numero di ripetizioni non è noto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Prova il classificatore con un voto non valido e con i confini validi, poi confronta i risultati prima e dopo la semplificazione.
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
  <li>leggere e scrivere una selezione annidata semplice;</li>
  <li>seguire il percorso dei rami con un trace;</li>
  <li>riconoscere quando una seconda decisione dipende davvero dalla prima;</li>
  <li>distinguere annidamento necessario da annidamento accidentale;</li>
  <li>rilevare un input non valido e separare caso valido/non valido;</li>
  <li>progettare casi di test che percorrono i principali path;</li>
  <li>confrontare annidamento e condizione composta quando entrambi sono corretti;</li>
  <li>usare una variabile booleana con un nome quando aggiunge significato;</li>
  <li>semplificare codice senza cambiare il comportamento osservabile;</li>
  <li>spiegare perché una versione è più leggibile o più aderente alla specifica.</li>
</ul>

## Prerequisiti

<p align="justify">Da M06–M07 dovresti già saper:</p>

<ul>
  <li>costruire <code>if</code>, <code>if/else</code>, <code>if/elif/else</code>;</li>
  <li>distinguere condizioni indipendenti e casi esclusivi;</li>
  <li>usare confronti, <code>and</code>, <code>or</code>, <code>not</code>;</li>
  <li>testare soglie e intervalli;</li>
  <li>individuare rami irraggiungibili o sovrapposti;</li>
  <li>fare il trace del primo ramo vero.</li>
</ul>

---

## 1. Problema iniziale: una domanda che ha senso solo dopo un'altra

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">Prima controlla se le credenziali sono valide. Soltanto se lo sono, controlla se l'account è attivo.</p>
</blockquote>

<p align="justify">La seconda domanda dipende dalla prima:</p>

```text
credenziali valide?
    no  → accesso negato
    sì  → account attivo?
              no  → account disabilitato
              sì  → accesso consentito
```

<p align="justify">Una traduzione diretta è:</p>

```python
if credenziali_valide:
    if account_attivo:
        print("accesso consentito")
    else:
        print("account disabilitato")
else:
    print("accesso negato")
```

<p align="justify">Qui l'annidamento rappresenta una <strong>dipendenza reale fra decisioni</strong>.</p>

---

## 2. Che cosa significa “annidare”

<p align="justify">Un <code>if</code> è annidato quando compare dentro il blocco di un'altra selezione.</p>

```python
if condizione_1:
    if condizione_2:
        ...
```

<p align="justify">Il secondo <code>if</code> viene raggiunto soltanto quando:</p>

```text
condizione_1 → True
```

<p align="justify">Quindi il percorso del programma dipende da più decisioni successive.</p>

---

## 3. Path trace: segui il percorso, non tutto il codice

<p align="justify">Programma:</p>

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
    else:
        print("disabilitato")
else:
    print("negato")
```

## Caso A

```text
credenziali_valide = False
account_attivo = True
```

<p align="justify">Trace:</p>

```text
credenziali_valide? → False
ramo esterno else   → negato
secondo if           → non raggiunto
```

## Caso B

```text
credenziali_valide = True
account_attivo = False
```

<p align="justify">Trace:</p>

```text
credenziali_valide? → True
account_attivo?     → False
ramo interno else   → disabilitato
```

<p align="justify">Il trace segue <strong>un path</strong> per volta.</p>

---

## 4. Costruire una tabella dei path

<p align="justify">Per due booleani:</p>

<table align="center">
<thead>
<tr>
<th>credenziali valide</th>
<th>account attivo</th>
<th>output atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>False</td>
<td>False</td>
<td>negato</td>
</tr>
<tr>
<td>False</td>
<td>True</td>
<td>negato</td>
</tr>
<tr>
<td>True</td>
<td>False</td>
<td>disabilitato</td>
</tr>
<tr>
<td>True</td>
<td>True</td>
<td>accesso</td>
</tr>
</tbody>
</table>

<p align="justify">Notare che quando le credenziali non sono valide, il valore di <code>account_attivo</code> non cambia il risultato.</p>

<p align="justify">Questa tabella ci aiuta a capire la struttura prima del codice.</p>

---

## 5. Annidamento oppure condizione composta?

<p align="justify">Specifica più semplice:</p>

<blockquote>
<p align="justify">Stampa <code>accesso</code> soltanto se credenziali valide <strong>e</strong> account attivo.</p>
</blockquote>

<p align="justify">Versione annidata:</p>

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

<p align="justify">Versione composta:</p>

```python
if credenziali_valide and account_attivo:
    print("accesso")
```

<p align="justify">In questa specifica ridotta possono essere equivalenti per l'output richiesto.</p>

<p align="justify">La seconda comunica direttamente:</p>

```text
entrambe le condizioni devono essere vere
```

<p align="justify">Ma se dobbiamo distinguere anche <code>credenziali non valide</code> da <code>account disabilitato</code>, l'annidamento o una struttura multi-ramo può rappresentare meglio il dominio.</p>

---

## 6. Meno annidamento non significa automaticamente codice migliore

<p align="justify">Evita regole meccaniche come:</p>

```text
meno righe = meglio
meno livelli = sempre meglio
```

<p align="justify">Confronta invece:</p>

<ol>
  <li>quali casi deve distinguere la specifica;</li>
  <li>quali condizioni hanno senso solo dopo altre;</li>
  <li>quali output/comportamenti devono restare differenti;</li>
  <li>quale struttura rende evidente il percorso.</li>
</ol>

<p align="justify">Il refactoring deve preservare il comportamento richiesto, non soltanto ridurre l'indentazione.</p>

---

## 7. Validazione: separare dati validi e non validi

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi un voto tra 0 e 10. Se è fuori intervallo stampa <code>dato non valido</code>; altrimenti classificalo.</p>
</blockquote>

<p align="justify">Per ora sappiamo <strong>rilevare</strong> l'errore:</p>

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
```

<p align="justify">Importante:</p>

<blockquote>
<p align="justify">non sappiamo ancora ripetere automaticamente la richiesta finché il dato diventa valido.</p>
</blockquote>

<p align="justify">Quello richiederà <code>while</code> in PY2-04.</p>

---

## 8. Validare non significa “mettere un try ovunque”

<p align="justify">Nel punto attuale del corso distinguiamo due problemi diversi.</p>

### Valore numerico fuori dal dominio

```text
voto = 12
```

<p align="justify">Il dato è un intero, ma non è valido per la nostra specifica <code>0..10</code>.</p>

<p align="justify">Possiamo rilevarlo con una condizione.</p>

### Testo non convertibile in intero

```text
"ciao"
```

<p align="justify"><code>int("ciao")</code> produce un errore di conversione.</p>

<p align="justify">Non introduciamo ancora <code>try/except</code> come nuovo argomento: la gestione programmata delle eccezioni verrà affrontata più avanti.</p>

<p align="justify">Per ora i test delle selezioni usano input del tipo già previsto dal contratto.</p>

---

## 9. Worked example: voto valido + classificazione

## Specifica

```text
INPUT: intero
se fuori 0..10 → dato non valido
altrimenti:
  < 6  → insufficiente
  >= 6 → sufficiente
```

## Casi di test

<table align="center">
<thead>
<tr>
<th>input</th>
<th>atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>-1</td>
<td>dato non valido</td>
</tr>
<tr>
<td>0</td>
<td>insufficiente</td>
</tr>
<tr>
<td>5</td>
<td>insufficiente</td>
</tr>
<tr>
<td>6</td>
<td>sufficiente</td>
</tr>
<tr>
<td>10</td>
<td>sufficiente</td>
</tr>
<tr>
<td>11</td>
<td>dato non valido</td>
</tr>
</tbody>
</table>

## Codice

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
```

<p align="justify">I casi <code>-1</code>, <code>0</code>, <code>10</code>, <code>11</code> controllano i confini della validità; <code>5</code> e <code>6</code> controllano la soglia della classificazione.</p>

---

## 10. Variante: condizione di validità nominata

<p align="justify">Quando un nome aggiunge significato:</p>

```python
voto_valido = 0 <= voto <= 10
```

<p align="justify">Poi:</p>

```python
if voto_valido:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
else:
    print("dato non valido")
```

<p align="justify">Il nome <code>voto_valido</code> rende esplicita una regola del dominio.</p>

<p align="justify">Non trasformiamo però ogni confronto in una variabile booleana: il nome deve spiegare qualcosa.</p>

---

## 11. Refactoring controllato: stessi test prima e dopo

<p align="justify">Supponiamo che questo comportamento sia sufficiente:</p>

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

<p align="justify">Possibile refactoring:</p>

```python
if credenziali_valide and account_attivo:
    print("accesso")
```

<p align="justify">Prima di dire che il refactoring è corretto:</p>

<ol>
  <li>conserva i casi di test;</li>
  <li>esegui mentalmente o realmente gli stessi input;</li>
  <li>verifica che output/comportamento restino uguali;</li>
  <li>spiega quale versione comunica meglio l'intenzione.</li>
</ol>

<p align="justify">Il test non serve solo a trovare bug nuovi: protegge anche durante le modifiche.</p>

---

## 12. Error Clinic: annidamento che cambia il significato

<p align="justify">Specifica:</p>

<blockquote>
<p align="justify">se piove stampa <code>ombrello</code>; se fa freddo stampa <code>giacca</code>. I due effetti possono coesistere.</p>
</blockquote>

<p align="justify">Bug:</p>

```python
if piove:
    if fa_freddo:
        print("giacca")
    print("ombrello")
```

<p align="justify">Se <code>fa_freddo</code> è True ma <code>piove</code> è False, <code>giacca</code> non viene mai stampato.</p>

<p align="justify">L'annidamento ha introdotto una dipendenza che la specifica non aveva.</p>

<p align="justify">Corretto per effetti indipendenti:</p>

```python
if piove:
    print("ombrello")

if fa_freddo:
    print("giacca")
```

---

## 13. Error Clinic: ramo valido nel posto sbagliato

<p align="justify">Bug:</p>

```python
if voto < 6:
    print("insufficiente")
else:
    if voto < 0 or voto > 10:
        print("dato non valido")
    else:
        print("sufficiente")
```

<p align="justify">Con <code>voto = -1</code>:</p>

```text
voto < 6 → True
```

<p align="justify">quindi viene stampato <code>insufficiente</code> prima ancora di controllare che il dato sia fuori dominio.</p>

<p align="justify">La validazione deve avvenire <strong>prima</strong> della classificazione se la classificazione ha senso solo per valori validi.</p>

---

## 14. Error Clinic: condizione composta che perde informazioni

<p align="justify">Versione:</p>

```python
if credenziali_valide and account_attivo:
    print("accesso")
else:
    print("negato")
```

<p align="justify">È corretta se la specifica distingue soltanto:</p>

```text
accesso / non accesso
```

<p align="justify">Non è sufficiente se dobbiamo distinguere:</p>

```text
credenziali errate
account disabilitato
```

<p align="justify">Una semplificazione sintattica può perdere informazioni richieste dal dominio.</p>

---

## 15. Path coverage: quali percorsi abbiamo davvero provato?

<p align="justify">Per una selezione annidata non basta dire “ho fatto tre test”.</p>

<p align="justify">Chiediti:</p>

```text
quali path del diagramma/codice percorrono?
```

<p align="justify">Esempio credenziali/account:</p>

```text
P1 → credenziali false
P2 → credenziali true, account false
P3 → credenziali true, account true
```

<p align="justify">Questi tre path coprono i tre risultati distinti.</p>

<p align="justify">La combinazione <code>credenziali false, account true</code> può essere utile per confermare che il secondo dato è irrilevante quando la prima decisione fallisce.</p>

---

## 16. De Morgan: solo una lente, non un capitolo

<p align="justify">A volte incontreremo negazioni come:</p>

```python
not (eta >= 18 and biglietto_valido)
```

<p align="justify">Esistono regole logiche per trasformare condizioni negate, ma in questa fase non facciamo algebra booleana formale.</p>

<p align="justify">Regola pratica:</p>

<blockquote>
<p align="justify">se una condizione è difficile da leggere, prima riscrivila in linguaggio naturale e verifica i casi; non cercare una forma “furba”.</p>
</blockquote>

<p align="justify">Eventuali equivalenze di De Morgan vengono usate soltanto come piccoli esempi guidati.</p>

---

## 17. Microscope: dipendenza reale o accidentale?

<p align="justify">Per ogni coppia di regole decidi se la seconda dipende dalla prima.</p>

### A

```text
se utente autenticato, allora controlla se ha permesso admin
```

### B

```text
se piove, ombrello; se freddo, giacca
```

### C

```text
se voto valido, allora classificalo
```

### D

```text
se ha completato quiz, badge; se ha completato progetto, bonus
```

<p align="justify">Prima descrivi la relazione; poi scegli annidamento, condizione composta o <code>if</code> indipendenti.</p>

---

## 18. Activity planning — M08

<p align="justify">Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:</p>

### A — Path trace

<p align="justify">Dato codice annidato, segnare il percorso seguito per più input.</p>

### B — Controlled refactor

<p align="justify">Trasformare un annidamento ridondante in una condizione composta, mantenendo gli stessi test.</p>

### C — Implement

<p align="justify">Problema con:</p>

<ul>
  <li>validazione iniziale;</li>
  <li>almeno tre casi validi;</li>
  <li>output deterministico;</li>
  <li>tabella dei casi prima del codice.</li>
</ul>

### D — Debug Clinic

<p align="justify">Correggere validazione tardiva, dipendenza accidentale o ramo mancante.</p>

### E — Mini-project

<p align="justify">Configuratore/regole semplici:</p>

<ol>
  <li>input/output/vincoli;</li>
  <li>flow chart o pseudocodice;</li>
  <li>tabella casi/path;</li>
  <li>implementazione;</li>
  <li>test;</li>
  <li>spiegazione della struttura scelta.</li>
</ol>

<p align="justify">M04 resta il canarino P1 fino alla certificazione <code>python-docente#7</code>.</p>

---

## 19. Romeo come problema di path/refactoring

<p align="justify">Romeo resta opzionale.</p>

<p align="justify">Un uso sensato in M08 è confrontare due modi di esprimere regole di una missione simulata:</p>

```text
prima valida un parametro
→ poi scegli un comportamento
```

<p align="justify">oppure fare il path trace di una missione già nota.</p>

<p align="justify">Vincoli:</p>

<ul>
  <li>niente hardware necessario;</li>
  <li>niente nuove API avanzate;</li>
  <li>niente networking;</li>
  <li>nessuna Activity Romeo duplicata nel repo Python;</li>
  <li><code>romeo-sim</code> solo quando certificato.</li>
</ul>

---

## 20. Mini-project: classificatore validato

<p align="justify">Specifica candidata:</p>

<blockquote>
<p align="justify">Leggi un punteggio intero tra 0 e 100. Se non è valido stampa <code>errore</code>. Se è valido, classificalo in tre fasce definite dalla consegna.</p>
</blockquote>

<p align="justify">Deliverable:</p>

```text
input/output/vincoli
flow chart o pseudocodice
tabella casi
codice
trace di un path
spiegazione di una scelta strutturale
```

<p align="justify">Non serve un progetto grande: il valore è integrare analisi, selezione, test e refactoring.</p>

---

## 21. Checkpoint M08 / uscita PY2-03

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Quando un <code>if</code> annidato rappresenta una dipendenza reale?</li>
  <li>Perché l'annidamento pioggia → freddo sarebbe sbagliato se i due effetti sono indipendenti?</li>
  <li>Perché validiamo un voto prima di classificarlo?</li>
  <li>In questa fase, che cosa facciamo con un voto fuori <code>0..10</code>?</li>
  <li>Perché non ripetiamo ancora automaticamente l'input?</li>
  <li>Quando <code>if A: if B:</code> può essere sostituito da <code>if A and B:</code> senza perdere comportamento richiesto?</li>
  <li>Che cosa significa preservare i test durante un refactoring?</li>
  <li>Perché una variabile come <code>voto_valido</code> può migliorare la leggibilità?</li>
  <li>Che cosa significa coprire i principali path?</li>
</ol>

---

## 22. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
annidamento → una decisione dipende da un'altra
```

```text
validazione → prima stabilisci se il dato appartiene al dominio
```

```text
refactoring → cambia struttura, preserva comportamento
```

```text
test/path → proteggono anche durante le modifiche
```

```text
leggibilità → il codice deve comunicare la regola del problema
```

<p align="justify">La prossima UDA introduce la ripetizione: useremo <code>while</code> per ripetere una richiesta finché una condizione cambia e <code>for</code> quando il numero/insieme delle iterazioni è noto.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione/verifica:</p>

<ul>
  <li>documentazione Python 3.12 — control flow, Boolean operations e comparisons;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — conditional execution, nested conditionals, debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — statement nesting, Boolean logic e control flow;</li>
  <li>Romeo pinned <code>45e5f7e131802fccc89358a23a25dbed1884bbfa</code> — riferimento applicativo selettivo.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

## Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_03_SPEC.md</code>;</li>
  <li><code>tracks/secondo/ASSESSMENT_CALENDAR.md</code>;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>.</li>
</ul>

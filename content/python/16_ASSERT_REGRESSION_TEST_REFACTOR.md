# M16 — `assert`, regression test, debug e refactoring

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
I casi scelti diventano assert e proteggono correzioni e refactoring dalle regressioni.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Scrivere funzioni con contratti semplici e scegliere casi normali e limite da M13–M15.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
trasformare casi di test in semplici <code>assert</code>;<br>distinguere caso normale, confine e caso non valido previsto dal contratto;<br>leggere un <code>AssertionError</code> elementare; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Un risultato atteso nasce dalla specifica; un test fallito può rivelare un errore nel programma o nel test. Riprendi <a href="15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md">M15 — Progettazione top-down e responsabilità</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md">M17 — Stringhe: indici, slicing e immutabilità</a>. Le stringhe sono sequenze immutabili da leggere per posizione o attraversare direttamente.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Riproduci un bug con un assert, correggilo e riesegui i casi precedenti prima di refactorare; prepara il Checkpoint A.
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
<strong>UDA:</strong> PY2-05 — Funzioni, decomposizione e testing<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>trasformare casi di test in semplici <code>assert</code>;</li>
  <li>distinguere caso normale, confine e caso non valido previsto dal contratto;</li>
  <li>leggere un <code>AssertionError</code> elementare;</li>
  <li>capire che un test fallito è informazione, non una soluzione automatica;</li>
  <li>aggiungere un test quando scopri un bug;</li>
  <li>verificare che la correzione non rompa casi già funzionanti;</li>
  <li>refactorare mantenendo invariato il comportamento richiesto;</li>
  <li>distinguere bug nel codice e test scritto male;</li>
  <li>confrontare due implementazioni con lo stesso contratto;</li>
  <li>spiegare il ciclo red → diagnose → fix → regression → refactor.</li>
</ul>

---

## 1. Dai casi su carta a test eseguibili

<p align="justify">Finora abbiamo scritto tabelle come:</p>

<table align="center">
<thead>
<tr>
<th>input</th>
<th>atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>-2</td>
<td>-4</td>
</tr>
</tbody>
</table>

<p align="justify">Per:</p>

```python
def doppio(x):
    return x * 2
```

<p align="justify">possiamo scrivere:</p>

```python
assert doppio(3) == 6
assert doppio(0) == 0
assert doppio(-2) == -4
```

<p align="justify"><code>assert</code> rende eseguibile una aspettativa.</p>

---

## 2. Che cosa significa un `assert`

```python
assert espressione_booleana
```

<p align="justify">Se l'espressione è <code>True</code>, l'esecuzione continua.</p>

<p align="justify">Se è <code>False</code>, Python segnala un <code>AssertionError</code>.</p>

<p align="justify">Non stiamo ancora studiando un framework di test.</p>

<p align="justify">Stiamo costruendo un ponte tra:</p>

```text
caso di test pensato
→ aspettativa eseguibile
```

---

## 3. Un test verde non dimostra tutto

<p align="justify">Tre assert che passano non dimostrano automaticamente che una funzione sia corretta per ogni possibile input.</p>

<p align="justify">I test danno <strong>evidenza</strong> e trovano bug.</p>

<p align="justify">La qualità dipende anche dai casi scelti.</p>

<p align="justify">Domande:</p>

<ul>
  <li>ho provato un caso normale?;</li>
  <li>un confine?;</li>
  <li>un valore negativo se il dominio lo permette?;</li>
  <li>un caso che in passato falliva?.</li>
</ul>

---

## 4. Caso normale, confine, caso non valido

<p align="justify">Per:</p>

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

<p align="justify">possiamo scegliere:</p>

```python
assert eta_valida(30) is True
assert eta_valida(0) is True
assert eta_valida(120) is True
assert eta_valida(-1) is False
assert eta_valida(121) is False
```

<p align="justify">I confini sono particolarmente importanti quando compaiono <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code> e <code>&gt;=</code>.</p>

---

## 5. Test fallito = domanda diagnostica

<p align="justify">Supponiamo:</p>

```python
def doppio(x):
    return x + 2

assert doppio(3) == 6
```

<p align="justify">Il test fallisce.</p>

<p align="justify">Workflow:</p>

```text
quale caso?
→ atteso?
→ ottenuto?
→ bug nel codice o nel test?
→ modifica minima
→ riesegui tutti i test
```

---

## 6. Il test può essere sbagliato

```python
assert doppio(3) == 7
```

<p align="justify">Se la specifica dice “moltiplica per due”, il bug è nel test.</p>

<p align="justify">Non bisogna modificare il codice soltanto per far diventare verde un test errato.</p>

<p align="justify">Fonte autorevole:</p>

```text
specifica / contratto
```

<p align="justify">Il test deve rappresentarla correttamente.</p>

---

## 7. Regression test

<p align="justify">Scenario:</p>

<ol>
  <li>scopri un bug;</li>
  <li>trovi un input che lo riproduce;</li>
  <li>aggiungi un test per quell'input;</li>
  <li>il test deve fallire prima della correzione;</li>
  <li>correggi il codice;</li>
  <li>riesegui il nuovo test e quelli precedenti.</li>
</ol>

<p align="justify">Questo test protegge dal ritorno dello stesso bug in futuro.</p>

---

## 8. Esempio di regression

<p align="justify">Bug:</p>

```python
def massimo(a, b):
    if a > b:
        return a
    return a
```

<p align="justify">Caso che espone il problema:</p>

```python
assert massimo(2, 5) == 5
```

<p align="justify">Prima della correzione il test fallisce.</p>

<p align="justify">Poi correggiamo:</p>

```python
def massimo(a, b):
    if a > b:
        return a
    return b
```

<p align="justify">E rieseguiamo tutti i test.</p>

---

## 9. Refactoring

<p align="justify">Definizione operativa:</p>

<blockquote>
<p align="justify">migliorare la struttura del codice senza cambiare il comportamento richiesto.</p>
</blockquote>

<p align="justify">Esempi:</p>

<ul>
  <li>rinominare;</li>
  <li>estrarre una funzione;</li>
  <li>eliminare duplicazione;</li>
  <li>semplificare una condizione;</li>
  <li>separare I/O da logica;</li>
  <li>rimuovere una dipendenza globale.</li>
</ul>

<p align="justify">I test aiutano a capire se il comportamento osservabile è rimasto lo stesso.</p>

---

## 10. Test prima e dopo il refactoring

<p align="justify">Prima:</p>

```python
assert calcola_sconto(100, 10) == 10
assert calcola_sconto(50, 0) == 0
```

<p align="justify">Refactoring della funzione.</p>

<p align="justify">Dopo:</p>

```text
riesegui gli stessi test
```

<p align="justify">Se diventano rossi, il refactoring potrebbe aver cambiato il comportamento.</p>

---

## 11. `assert` non sostituisce la gestione degli errori

<p align="justify">Non usiamo <code>assert</code> per gestire input utente invalido o errori esterni prevedibili.</p>

<p align="justify">Qui <code>assert</code> serve a verificare aspettative durante sviluppo/esercitazione.</p>

<p align="justify">La gestione delle eccezioni e dei confini esterni verrà affrontata nel blocco file/errori.</p>

---

## 12. Più test, responsabilità più piccole

<p align="justify">Una funzione piccola e con contratto chiaro è più semplice da testare.</p>

<p align="justify">Questo collega M15 e M16:</p>

```text
responsabilità chiara
→ input/output chiari
→ casi più chiari
→ test più semplici
```

---

## 13. Due implementazioni, stesso contratto

<p align="justify">Supponiamo due funzioni che devono entrambe calcolare il valore assoluto di un intero.</p>

<p align="justify">Se rispettano lo stesso contratto, possiamo applicare gli stessi casi a entrambe.</p>

<p align="justify">Questo permette di confrontare:</p>

<ul>
  <li>correttezza;</li>
  <li>leggibilità;</li>
  <li>struttura;</li>
  <li>lavoro svolto quando rilevante.</li>
</ul>

<p align="justify">Non scegliamo soltanto la versione con meno righe.</p>

---

## 14. Ciclo di debug protetto dai test

```text
test rosso
→ riproduci
→ localizza
→ modifica minima
→ test verde
→ tutti i test verdi
→ eventuale refactor
→ tutti i test ancora verdi
```

<p align="justify">È un modello professionale ridotto a scala beginner.</p>

---

## 15. Git G1: diff e primo checkpoint

<p align="justify">Durante un fix/refactor:</p>

```text
git diff
```

<p align="justify">mostra ciò che è cambiato.</p>

<p align="justify">Al Checkpoint A arriveranno:</p>

```text
git add
git commit
```

<p align="justify">per salvare uno stato significativo del progetto.</p>

<p align="justify">Il corso Git rimane separato e più ampio.</p>

---

## 16. TheBitLab P2

<p align="justify">Questa UDA richiede idealmente test diretti delle funzioni:</p>

```text
funzione + argomenti
→ sandbox
→ return/exception reale
→ confronto host-side con expected
```

<p align="justify">Questo è il profilo <code>P2 / python-function-v1</code> tracciato in <code>2cornot2c#756</code>.</p>

<p align="justify">Fino alla certificazione:</p>

<ul>
  <li><code>assert</code> nel workspace come evidence;</li>
  <li>verifiche manuali/formative;</li>
  <li>niente parser fragile del codice;</li>
  <li>niente trasformazione forzata in stdin/stdout quando l'obiettivo è il comportamento della funzione.</li>
</ul>

---

## 17. Activity candidate

### A — Test reader

<p align="justify">Prevedi quali assert passano/falliscono e perché.</p>

### B — Add a test

<p align="justify">Aggiungi un caso limite che espone un bug.</p>

### C — Implement from contract

<p align="justify">Implementa una funzione a partire da contratto + test.</p>

### D — Debug regression

<p align="justify">Riproduci bug → test rosso → fix → tutti verdi.</p>

### E — Mini-project funzionale

<p align="justify">Richiede:</p>

<ul>
  <li>almeno 3 funzioni/responsabilità;</li>
  <li>I/O separato;</li>
  <li>selezione/cicli già appresi;</li>
  <li>almeno 5 casi complessivi;</li>
  <li>call graph breve;</li>
  <li>spiegazione di un refactoring.</li>
</ul>

---

## 18. Exit checkpoint PY2-05

<p align="justify">Dovresti saper:</p>

<ul>
  <li>definire/chiamare funzioni;</li>
  <li>distinguere parametro/argomento;</li>
  <li>usare <code>return</code>;</li>
  <li>distinguere <code>return</code>/<code>print</code>;</li>
  <li>capire scope locale beginner;</li>
  <li>comporre funzioni;</li>
  <li>progettare top-down;</li>
  <li>separare I/O/logica/output;</li>
  <li>scrivere casi e <code>assert</code>;</li>
  <li>aggiungere un regression test;</li>
  <li>refactorare con protezione dei test.</li>
</ul>

---

## 19. Sintesi

```text
contratto
→ casi
→ assert
→ implementazione
→ debug
→ regression
→ refactor
```

```text
test verde ≠ prova assoluta
```

```text
specifica autorevole
→ test coerente
→ codice coerente
```

<p align="justify">Il Checkpoint A consoliderà il primo grande nucleo del corso e introdurrà il primo commit Git guidato.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — <code>assert</code>, funzioni e <code>AssertionError</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — debugging e testing beginner;</li>
  <li>pratiche professionali di regression testing/refactoring adattate al secondo anno;</li>
  <li>TheBitLab <code>2cornot2c#756</code> — profilo P2 function-behavior.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>

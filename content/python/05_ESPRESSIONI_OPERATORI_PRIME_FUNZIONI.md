# M05 — Espressioni, operatori e prime funzioni

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Le espressioni trasformano valori; una prima funzione dà un nome al calcolo e ne restituisce il risultato.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare REPL, script, variabili, input, output e conversioni semplici da M04.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
costruire espressioni aritmetiche leggibili;<br>usare <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>//</code>, <code>%</code> e <code>**</code> nei problemi appropriati;<br>prevedere il valore e il tipo di espressioni semplici; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Valore, tipo e risultato stampato sono osservazioni diverse della stessa prova. Riprendi <a href="04_INTERPRETE_REPL_VALORI_IO.md">M04 — Interprete, REPL, script, valori e input/output</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="06_BOOLEANI_CONFRONTI_IF.md">M06 — Booleani, confronti e prima selezione con <code>if</code></a>. Una condizione booleana permette al programma di scegliere il comportamento richiesto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Converti 137 secondi in minuti e resto, poi controlla 60, 59 e 0 con la funzione proposta.
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
<strong>UDA:</strong> PY2-02 — Primi programmi Python<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>costruire espressioni aritmetiche leggibili;</li>
  <li>usare <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>//</code>, <code>%</code> e <code>**</code> nei problemi appropriati;</li>
  <li>prevedere il valore e il tipo di espressioni semplici;</li>
  <li>usare parentesi per rendere esplicita l'intenzione del calcolo;</li>
  <li>distinguere divisione <code>/</code>, divisione intera verso il basso <code>//</code> e resto <code>%</code>;</li>
  <li>usare <code>%</code> per problemi di quoziente/resto e divisibilità elementare;</li>
  <li>produrre output leggibile con f-string;</li>
  <li>usare alcune funzioni built-in quando rendono il programma più chiaro;</li>
  <li>riconoscere la differenza fra <strong>calcolare</strong>, <strong>restituire</strong> e <strong>stampare</strong>;</li>
  <li>definire e chiamare una prima funzione pura molto semplice;</li>
  <li>progettare casi di test prima di considerare concluso un piccolo programma.</li>
</ul>

## Prerequisiti

<p align="justify">Da M04 dovresti già saper:</p>

<ul>
  <li>usare REPL e script <code>.py</code>;</li>
  <li>riconoscere <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code> nei casi base;</li>
  <li>usare variabili, <code>input()</code>, <code>print()</code> e conversioni semplici;</li>
  <li>leggere un traceback beginner;</li>
  <li>verificare uno script con più input.</li>
</ul>

---

## 1. Problema iniziale: quanti minuti e quanti secondi?

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Leggi un numero intero di secondi e mostra quanti minuti completi contiene e quanti secondi restano.</p>
</blockquote>

<p align="justify">Esempio:</p>

```text
INPUT: 137
OUTPUT: 2 17
```

<p align="justify">Prima del codice:</p>

```text
137 secondi
= 2 gruppi completi da 60
+ 17 secondi rimanenti
```

<p align="justify">Quindi servono <strong>due risultati diversi</strong>:</p>

```text
quoziente intero → 2
resto             → 17
```

<p align="justify">Python possiede operatori che esprimono direttamente queste due idee.</p>

---

## 2. Un'espressione produce un valore

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — espressione:</strong>
Un'espressione è una parte di codice che viene valutata per produrre un valore: può contenere valori, nomi, operatori o chiamate di funzione.
</p>
</td>
</tr>
</table>

<p align="justify">Nel REPL:</p>

```python
2 + 3
```

<p align="justify">è un'espressione.</p>

<p align="justify">Produce il valore:</p>

```text
5
```

<p align="justify">Anche:</p>

```python
prezzo * quantita
```

<p align="justify">è un'espressione se i nomi hanno già un valore associato.</p>

<p align="justify">Possiamo usare il risultato in un assegnamento:</p>

```python
totale = prezzo * quantita
```

<p align="justify">Modello mentale:</p>

```text
valori / nomi
     ↓
espressione
     ↓
valore risultante
     ↓
assegnamento / return / print / altra espressione
```

---

## 3. Operatori aritmetici fondamentali

<p align="justify">Con numeri, incontreremo spesso:</p>

<table align="center">
<thead>
<tr>
<th>Operatore</th>
<th>Idea</th>
<th>Esempio</th>
<th>Risultato</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>+</code></td>
<td>somma</td>
<td><code>7 + 3</code></td>
<td><code>10</code></td>
</tr>
<tr>
<td><code>-</code></td>
<td>differenza</td>
<td><code>7 - 3</code></td>
<td><code>4</code></td>
</tr>
<tr>
<td><code>*</code></td>
<td>prodotto</td>
<td><code>7 * 3</code></td>
<td><code>21</code></td>
</tr>
<tr>
<td><code>/</code></td>
<td>divisione</td>
<td><code>7 / 2</code></td>
<td><code>3.5</code></td>
</tr>
<tr>
<td><code>//</code></td>
<td>floor division</td>
<td><code>7 // 2</code></td>
<td><code>3</code></td>
</tr>
<tr>
<td><code>%</code></td>
<td>resto/modulo</td>
<td><code>7 % 2</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><code>**</code></td>
<td>potenza</td>
<td><code>2 ** 3</code></td>
<td><code>8</code></td>
</tr>
</tbody>
</table>

<p align="justify">Non scegliere un operatore perché "sembra giusto".</p>

<p align="justify">Chiediti:</p>

<blockquote>
<p align="justify">Quale trasformazione richiede il problema?</p>
</blockquote>

---

## 4. `/`, `//` e `%` non sono la stessa divisione

## `/` — divisione

```python
8 / 2
```

<p align="justify">produce:</p>

```text
4.0
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — divisione — /:</strong>
In Python 3, <code>/</code> produce un risultato di tipo <code>float</code>, anche quando matematicamente il risultato è intero.
</p>
</td>
</tr>
</table>

## `//` — floor division

```python
17 // 3
```

<p align="justify">produce:</p>

```text
5
```

<p align="justify">Per numeri positivi puoi leggerlo inizialmente come:</p>

<blockquote>
<p align="justify">quanti gruppi completi da 3 stanno in 17?</p>
</blockquote>

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — divisione intera — //:</strong>
<code>//</code> calcola il quoziente arrotondato verso il basso, cioè verso meno infinito: è <em>floor division</em>, non una generica regola "taglia la parte decimale". Per interi non negativi e divisore positivo conta i gruppi completi. Per il core beginner useremo soprattutto questi casi; con numeri negativi segue comunque l'arrotondamento verso meno infinito.
</p>
</td>
</tr>
</table>

## `%` — resto

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — resto — %:</strong>
<code>%</code> calcola il resto della divisione. Per interi non negativi e divisore positivo indica quanti elementi avanzano dopo aver formato i gruppi completi.
</p>
</td>
</tr>
</table>

```python
17 % 3
```

<p align="justify">produce:</p>

```text
2
```

<p align="justify">I tre valori sono collegati:</p>

```text
17 = (17 // 3) * 3 + (17 % 3)
17 = 5 * 3 + 2
```

<p align="justify">Questa relazione è un ottimo strumento di controllo.</p>

---

## 5. Worked example: secondi → minuti + resto

## Specifica

```text
INPUT: secondi_totali, intero non negativo
OUTPUT: minuti_completi e secondi_restanti
```

## Casi di test

<table align="center">
<thead>
<tr>
<th>input</th>
<th>minuti</th>
<th>resto</th>
</tr>
</thead>
<tbody>
<tr>
<td>137</td>
<td>2</td>
<td>17</td>
</tr>
<tr>
<td>60</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>59</td>
<td>0</td>
<td>59</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

## Codice

```python
secondi_totali = int(input())
minuti = secondi_totali // 60
secondi = secondi_totali % 60
print(minuti, secondi)
```

## Trace con 137

```text
secondi_totali        → 137
137 // 60             → 2
minuti                 → 2
137 % 60              → 17
secondi                → 17
print(minuti, secondi) → 2 17
```

<p align="justify">Il codice è corto perché il problema è stato modellato bene prima.</p>

---

## 6. `%` come domanda sul resto

<p align="justify">Un numero intero è divisibile per 2 quando il resto della divisione per 2 è zero:</p>

```python
numero % 2
```

<p align="justify">Esempi:</p>

```text
8 % 2 → 0
9 % 2 → 1
```

<p align="justify">Per ora osserviamo soltanto il valore del resto.</p>

<p align="justify">Nel prossimo blocco, con <code>if</code>, useremo una condizione come:</p>

```python
numero % 2 == 0
```

<p align="justify">per decidere fra comportamenti diversi.</p>

<p align="justify">Non anticipiamo ancora tutta la selezione: qui impariamo la trasformazione numerica.</p>

---

## 7. Potenze: `**`, non `^`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — potenza — **:</strong>
<code>base ** esponente</code> calcola la potenza della base. Con un esponente intero positivo, corrisponde a moltiplicare la base per se stessa tante volte quanto indica l'esponente.
</p>
</td>
</tr>
</table>

<p align="justify">In Python:</p>

```python
2 ** 5
```

<p align="justify">produce:</p>

```text
32
```

<p align="justify">Un errore comune è scrivere:</p>

```python
2 ^ 5
```

<p align="justify">pensando che <code>^</code> significhi potenza.</p>

<p align="justify">In Python <code>^</code> ha un altro significato (XOR bit-a-bit), che non ci serve ora.</p>

<p align="justify">Regola beginner:</p>

```text
potenza → **
```

---

## 8. Precedenza: Python deve sapere cosa calcolare prima

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — precedenza degli operatori:</strong>
La precedenza stabilisce quali operatori vengono applicati prima quando un'espressione ne contiene più di uno. Le parentesi permettono di rendere esplicito o cambiare il raggruppamento.
</p>
</td>
</tr>
</table>

<p align="justify">Considera:</p>

```python
2 + 3 * 4
```

<p align="justify">Python applica regole di precedenza e produce:</p>

```text
14
```

<p align="justify">perché il prodotto viene eseguito prima della somma.</p>

<p align="justify">Con:</p>

```python
(2 + 3) * 4
```

<p align="justify">il risultato diventa:</p>

```text
20
```

## Regola pratica del corso

<p align="justify">Non trasformiamo la precedenza in una gara di memoria.</p>

<p align="justify">Usa le parentesi quando:</p>

<ul>
  <li>cambiano realmente l'ordine del calcolo;</li>
  <li>rendono più evidente l'intenzione;</li>
  <li>evitano a chi legge di dover ricostruire mentalmente un'espressione complessa.</li>
</ul>

<p align="justify">Per il nostro livello basta ricordare la struttura generale:</p>

```text
parentesi
→ potenze
→ *, /, //, %
→ +, -
```

<p align="justify">Per casi più sottili, meglio rendere il codice esplicito invece di affidarsi alla memoria.</p>

---

## 9. Espressione corretta ma difficile da leggere

<p align="justify">Confronta:</p>

```python
risultato = a + b * c - d / e
```

<p align="justify">con:</p>

```python
costo_componenti = b * c
quota = d / e
risultato = a + costo_componenti - quota
```

<p align="justify">Le due forme non sono sempre equivalenti dal punto di vista del dominio, ma mostrano un criterio importante:</p>

<blockquote>
<p align="justify">un risultato intermedio con un buon nome può spiegare <strong>che cosa significa</strong> una parte del calcolo.</p>
</blockquote>

<p align="justify">Non estrarre variabili inutili per ogni singolo simbolo; usale quando comunicano un concetto.</p>

---

## 10. Microscope: tipo e valore

<p align="justify">Prima di eseguire, completa la tabella.</p>

<table align="center">
<thead>
<tr>
<th>Espressione</th>
<th>Valore previsto</th>
<th>Tipo previsto</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7 + 3</code></td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td><code>7 / 2</code></td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td><code>7 // 2</code></td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td><code>7 % 2</code></td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td><code>2 ** 3</code></td>
<td>?</td>
<td>?</td>
</tr>
<tr>
<td><code>4 * 3.5</code></td>
<td>?</td>
<td>?</td>
</tr>
</tbody>
</table>

<p align="justify">Poi verifica nel REPL con <code>type()</code> soltanto dopo aver scritto le previsioni.</p>

<p align="justify">Obiettivo:</p>

```text
prevedere
→ osservare
→ spiegare una differenza
```

<p align="justify">non copiare l'output del REPL.</p>

---

## 11. Built-in: usare uno strumento quando esprime bene l'intenzione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — funzione built-in:</strong>
Una funzione built-in è una funzione già disponibile in Python senza doverla definire o importare, come <code>len()</code>, <code>min()</code> e <code>max()</code>.
</p>
</td>
</tr>
</table>

<p align="justify">Python fornisce funzioni built-in utili.</p>

<p align="justify">Esempi semplici:</p>

```python
abs(-8)
round(3.14159, 2)
min(8, 3, 12)
max(8, 3, 12)
len("Python")
```

<p align="justify">Non dobbiamo imparare una lunga lista di built-in.</p>

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">questa funzione esprime meglio l'operazione che voglio fare rispetto a riscriverla manualmente?</p>
</blockquote>

<p align="justify"><code>len()</code> era già comparsa come lente sulle stringhe; <code>min()</code> e <code>max()</code> qui sono semplici strumenti. Più avanti impareremo anche a calcolare min/max progressivamente per capire l'algoritmo sottostante.</p>

---

## 12. Output leggibile con f-string

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — f-string:</strong>
Una f-string è una stringa preceduta da <code>f</code> che inserisce nel testo i valori delle espressioni racchiuse tra parentesi graffe.
</p>
</td>
</tr>
</table>

<p align="justify">Per un programma destinato a una persona possiamo voler scrivere:</p>

```python
nome = "Ada"
punti = 27
print(f"{nome} ha {punti} punti")
```

<p align="justify">Output:</p>

```text
Ada ha 27 punti
```

<p align="justify">Dentro <code>{...}</code> possiamo inserire espressioni semplici:</p>

```python
print(f"Il doppio è {numero * 2}")
```

## Contratto prima dell'estetica

<p align="justify">Nelle Activity con output esatto dobbiamo comunque rispettare la specifica.</p>

<p align="justify">Se il contratto dice:</p>

```text
OUTPUT: 54
```

<p align="justify">stampare:</p>

```text
Il doppio è 54
```

<p align="justify">è un output diverso.</p>

<p align="justify">Le f-string sono uno strumento di presentazione, non un motivo per ignorare l'interfaccia richiesta.</p>

---

## 13. Calcolare e stampare sono responsabilità diverse

<p align="justify">Considera:</p>

```python
base = 5
altezza = 3
area = base * altezza
print(area)
```

<p align="justify">Qui possiamo distinguere:</p>

```text
calcolo       → base * altezza
risultato     → area
presentazione → print(area)
```

<p align="justify">Questa separazione diventerà sempre più utile quando i programmi cresceranno.</p>

---

## 14. Prima funzione: dare un nome a una trasformazione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — funzione:</strong>
Una funzione è un blocco di istruzioni con un nome che svolge un compito. Una chiamata ne esegue il corpo e può fornire dati di ingresso e ottenere un valore di ritorno.
</p>
</td>
</tr>
</table>

<p align="justify">Possiamo dare un nome al calcolo dell'area:</p>

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

<p align="justify">Poi usarlo:</p>

```python
area = area_rettangolo(5, 3)
print(area)
```

<p align="justify">Per ora ci basta questo modello:</p>

```text
input della trasformazione
        ↓
parametri
        ↓
calcolo
        ↓
return
        ↓
valore prodotto
```

<p align="justify">Non stiamo ancora facendo il modulo completo sulle funzioni: scope, progettazione top-down, contratti e decomposizione sistematica arriveranno in PY2-05.</p>

---

## 15. `return` non è `print`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — return:</strong>
<code>return</code> termina la chiamata della funzione e restituisce un valore al chiamante. Il valore restituito può essere usato in altri calcoli; non viene stampato automaticamente.
</p>
</td>
</tr>
</table>

<p align="justify">Queste due funzioni non hanno lo stesso comportamento:</p>

```python
def doppio(numero):
    return numero * 2
```

```python
def mostra_doppio(numero):
    print(numero * 2)
```

<p align="justify">La prima <strong>produce un valore</strong> che può essere usato altrove:</p>

```python
risultato = doppio(4)
print(risultato + 1)
```

<p align="justify">La seconda produce output sul terminale, ma non sta restituendo quel numero al chiamante.</p>

<p align="justify">Per ora ricordiamo soltanto:</p>

```text
return → valore verso chi ha chiamato la funzione
print  → output verso l'esterno
```

<p align="justify">Approfondiremo questa distinzione con molti esempi in PY2-05.</p>

---

## 16. Testare una piccola funzione

<p align="justify">Per:</p>

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

<p align="justify">possiamo pensare ai casi prima del codice:</p>

<table align="center">
<thead>
<tr>
<th>base</th>
<th>altezza</th>
<th>atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>5</td>
<td>3</td>
<td>15</td>
</tr>
<tr>
<td>1</td>
<td>7</td>
<td>7</td>
</tr>
<tr>
<td>0</td>
<td>4</td>
<td>0</td>
</tr>
</tbody>
</table>

<p align="justify">E poi verificare nel REPL:</p>

```python
area_rettangolo(5, 3)
area_rettangolo(1, 7)
area_rettangolo(0, 4)
```

<p align="justify">Non serve ancora un framework di testing per imparare l'idea fondamentale:</p>

<blockquote>
<p align="justify">una trasformazione dovrebbe poter essere verificata con esempi scelti consapevolmente.</p>
</blockquote>

---

## 17. Error Clinic

## Caso 1 — operatore sbagliato

```python
quadrato = numero ^ 2
```

<p align="justify">Se volevi una potenza, l'operatore non esprime l'operazione richiesta.</p>

## Caso 2 — divisione sbagliata per il dominio

```python
scatole = pezzi / capacita
```

<p align="justify">Se il problema chiede <strong>scatole complete</strong>, probabilmente <code>/</code> non è il modello giusto.</p>

## Caso 3 — resto dimenticato

```python
minuti = secondi_totali // 60
```

<p align="justify">Se la specifica chiede anche i secondi rimanenti manca una parte dell'output.</p>

## Caso 4 — precedenza non esplicita

```python
media = a + b + c / 3
```

<p align="justify">La formula non calcola la media aritmetica dei tre valori.</p>

<p align="justify">Una forma corretta e chiara è:</p>

```python
media = (a + b + c) / 3
```

## Caso 5 — funzione definita ma non chiamata

```python
def doppio(numero):
    return numero * 2

risultato = doppio
```

<p align="justify"><code>doppio</code> e <code>doppio(5)</code> non sono la stessa cosa.</p>

<p align="justify">Per invocare la trasformazione servono le parentesi e gli argomenti richiesti.</p>

## Caso 6 — stampare invece di restituire

<p align="justify">Se una funzione deve produrre un valore riutilizzabile, sostituire <code>return</code> con <code>print</code> cambia il suo contratto.</p>

---

## 18. Confrontare soluzioni

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Converti una quantità di secondi in minuti completi e secondi restanti.</p>
</blockquote>

### Soluzione A

```python
minuti = secondi_totali // 60
resto = secondi_totali % 60
```

### Soluzione B

```python
minuti = int(secondi_totali / 60)
resto = secondi_totali - minuti * 60
```

<p align="justify">Per input non negativi entrambe possono produrre lo stesso risultato nei casi semplici.</p>

<p align="justify">Ma la A comunica direttamente le due operazioni del problema:</p>

```text
gruppi completi
resto
```

<p align="justify">Il confronto non riguarda soltanto il numero di caratteri.</p>

<p align="justify">Criteri:</p>

```text
correttezza
→ significato espresso
→ leggibilità
→ assenza di lavoro inutile
```

---

## 19. Esercizi brevi

## A — Predict

<p align="justify">Prevedi valore e tipo:</p>

```python
15 / 4
15 // 4
15 % 4
3 + 2 * 5
(3 + 2) * 5
2 ** 4
```

## B — Quoziente/resto

<p align="justify">Dato un numero di caramelle e una dimensione fissa della confezione, calcola:</p>

<ul>
  <li>confezioni complete;</li>
  <li>caramelle rimaste.</li>
</ul>

<p align="justify">Prima scrivi input/output e almeno tre casi.</p>

## C — Ore, minuti, secondi

<p align="justify">Dato un numero non negativo di secondi, produci:</p>

```text
ore_complete minuti_restanti secondi_restanti
```

<p align="justify">Scomponi il problema prima di scrivere il codice.</p>

## D — Debug

<p align="justify">Correggi:</p>

```python
a = int(input())
b = int(input())
media = a + b / 2
print(media)
```

<p align="justify">Spiega il bug, non limitarti a modificare una riga.</p>

## E — Prima funzione

<p align="justify">Scrivi:</p>

```python
def perimetro_rettangolo(base, altezza):
    ...
```

<p align="justify">La funzione deve <strong>restituire</strong> il valore. Proponi tre casi di test prima dell'implementazione.</p>

---

## 20. Activity planning — non ancora materializzato

<p align="justify">Per M05 sono candidati:</p>

<ul>
  <li><strong>A Observe/Trace:</strong> precedenza, valore e tipo;</li>
  <li><strong>B Controlled Change:</strong> correggere una formula mantenendo invariato il contratto I/O;</li>
  <li><strong>C Implement:</strong> conversione secondi → unità + resti;</li>
  <li><strong>D Debug:</strong> precedenza, <code>/</code> vs <code>//</code>, <code>%</code>, <code>^</code> vs <code>**</code>;</li>
  <li><strong>E Mini-program:</strong> piccolo calcolatore a una sola trasformazione, senza selezione.</li>
</ul>

<p align="justify">Non materializziamo ora una seconda Activity P1 nel repository: <code>py2-activity-b-input-somma-001</code> resta il canarino tecnico finché <code>python-docente#7</code> non è certificato.</p>

---

## 21. Checkpoint M05

<p align="justify">Senza eseguire Python, spiega:</p>

<ol>
  <li>Qual è la differenza tra <code>/</code>, <code>//</code> e <code>%</code>?</li>
  <li>Perché <code>17 // 3</code> e <code>17 % 3</code> descrivono due parti dello stesso problema?</li>
  <li>Perché <code>(a + b + c) / 3</code> è diverso da <code>a + b + c / 3</code>?</li>
  <li>Qual è l'operatore di potenza in Python?</li>
  <li>Perché una f-string può rendere sbagliato un output autogradato anche se il calcolo è corretto?</li>
  <li>Che differenza c'è tra <code>return</code> e <code>print</code> nel nostro modello iniziale?</li>
  <li>Perché mostriamo una funzione già ora senza approfondire ancora scope e decomposizione?</li>
</ol>

---

## 22. Sintesi

<p align="justify">Porta con te questi modelli:</p>

```text
espressione → valore
```

```text
/  → divisione
// → gruppi completi / floor division
%  → resto
```

```text
parentesi = intenzione esplicita
```

```text
buon nome → significato del risultato intermedio
```

```text
funzione piccola = trasformazione con un nome
```

```text
return ≠ print
```

<p align="justify">Nel prossimo blocco useremo espressioni che producono <code>True</code>/<code>False</code> per prendere decisioni con <code>if</code>, <code>elif</code> ed <code>else</code>.</p>

---

## Fonti e riferimenti docente

<p align="justify">Questa lesson è materiale originale del corso. Per progettazione e verifica tecnica:</p>

<ul>
  <li>documentazione Python 3.12 — tutorial sui numeri/espressioni e reference delle espressioni;</li>
  <li>Allen Downey, <em>Think Python / Pensare in Python</em> — progressione beginner, funzioni e debugging;</li>
  <li>Mark Lutz, <em>Learning Python / Imparare Python</em> — copertura sistematica di espressioni/operatori/funzioni;</li>
  <li>Pluralsight Python Essentials — gap-check del percorso e dei laboratori.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference e non testo da riprodurre.</p>

## Collegamenti di progettazione

<ul>
  <li><code>tracks/secondo/PY2_02_SPEC.md</code>;</li>
  <li><code>doc/CURRICULUM_FREEZE_2026_2027.md</code>;</li>
  <li><code>doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md</code>.</li>
</ul>

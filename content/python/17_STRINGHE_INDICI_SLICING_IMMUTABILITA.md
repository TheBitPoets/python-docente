# M17 — Stringhe: indici, slicing e immutabilità

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Le stringhe sono sequenze immutabili da leggere per posizione o attraversare direttamente.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare stringhe semplici, cicli, funzioni e test; riprendere le competenze consolidate nel Checkpoint A.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
descrivere una <code>str</code> come sequenza ordinata immutabile di testo Unicode a livello beginner;<br>usare <code>len()</code>;<br>usare indici da <code>0</code> e indici negativi; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Come in range, lo stop dello slicing è escluso; un nuovo risultato non implica una mutazione dell&#x27;originale. Riprendi <a href="16_ASSERT_REGRESSION_TEST_REFACTOR.md">M16 — <code>assert</code>, regression test, debug e refactoring</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md">M18 — Ricerca, membership, metodi e normalizzazione delle stringhe</a>. Ricerca e normalizzazione scelgono metodi coerenti con la domanda posta sul testo.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Disegna gli indici di una stringa breve e prevedi una slice, un indice negativo e un accesso fuori intervallo.
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
<strong>UDA:</strong> PY2-06 — Stringhe come sequenze e testo<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>descrivere una <code>str</code> come sequenza ordinata immutabile di testo Unicode a livello beginner;</li>
  <li>usare <code>len()</code>;</li>
  <li>usare indici da <code>0</code> e indici negativi;</li>
  <li>leggere/scrivere slicing <code>start:stop</code> con stop escluso;</li>
  <li>usare uno step semplice quando serve;</li>
  <li>distinguere <code>IndexError</code> da slicing fuori range;</li>
  <li>spiegare perché <code>testo[0] = ...</code> non è ammesso;</li>
  <li>creare una nuova stringa invece di modificare quella esistente;</li>
  <li>scegliere iterazione diretta o per indice in base al problema.</li>
</ul>

---

## 1. Una stringa è una sequenza

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — stringa:</strong>
Una stringa <code>str</code> è una sequenza ordinata e immutabile di testo Unicode. Possiamo leggere gli elementi tramite indici, ma non modificarli direttamente nella stringa esistente.
</p>
</td>
</tr>
</table>

```python
parola = "python"
```

<p align="justify">Modello:</p>

```text
indice       0  1  2  3  4  5
             p  y  t  h  o  n
indice neg. -6 -5 -4 -3 -2 -1
```

<p align="justify">La posizione fa parte della struttura.</p>

---

## 2. Lunghezza

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — lunghezza — len():</strong>
<code>len(testo)</code> restituisce il numero di elementi della stringa. La stringa vuota ha lunghezza 0.
</p>
</td>
</tr>
</table>

```python
len("python")
```

<p align="justify">restituisce:</p>

```text
6
```

<p align="justify">Gli indici validi positivi vanno da <code>0</code> a <code>len(testo) - 1</code>.</p>

---

## 3. Accesso con indice

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — indice:</strong>
Un indice identifica una posizione nella sequenza. Gli indici non negativi iniziano da 0; gli indici negativi contano dalla fine, con <code>-1</code> per l'ultimo elemento.
</p>
</td>
</tr>
</table>

```python
parola[0]   # 'p'
parola[5]   # 'n'
parola[-1]  # 'n'
```

<p align="justify">Prima di eseguire, prevedi sempre carattere e posizione.</p>

---

## 4. `IndexError`

```python
parola[6]
```

<p align="justify">con <code>parola = "python"</code> tenta di accedere a una posizione inesistente e genera <code>IndexError</code>.</p>

<p align="justify">Domanda di debug:</p>

<blockquote>
<p align="justify">qual è l'ultimo indice valido?</p>
</blockquote>

---

## 5. Slicing

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — slicing:</strong>
Lo slicing seleziona una parte di una sequenza. Nella forma <code>testo[start:stop:step]</code>, <code>start</code> è incluso, <code>stop</code> è escluso e <code>step</code> indica il passo.
</p>
</td>
</tr>
</table>

```python
parola[1:4]
```

<p align="justify">produce:</p>

```text
'yth'
```

<p align="justify">Regola:</p>

```text
start incluso
stop escluso
```

<p align="justify">È lo stesso modello già incontrato con <code>range</code>.</p>

---

## 6. Slice fuori range

<p align="justify">A differenza dell'accesso singolo, uno slice può oltrepassare il limite senza <code>IndexError</code>:</p>

```python
parola[3:100]
```

<p align="justify">produce la parte disponibile da indice 3 in poi.</p>

<p align="justify">Non confondere:</p>

```text
indice singolo fuori range → errore
slice oltre il limite      → taglio della parte disponibile
```

---

## 7. Indici negativi

```python
parola[-1]
parola[-2]
```

<p align="justify">sono utili quando il problema parla naturalmente di ultimo/penultimo carattere.</p>

<p align="justify">Non usarli per rendere il codice “più furbo” quando un indice positivo comunica meglio l'intenzione.</p>

---

## 8. Step nello slicing

```python
parola[::2]
```

<p align="justify">prende un carattere ogni due.</p>

```python
parola[::-1]
```

<p align="justify">produce una stringa in ordine inverso.</p>

<p align="justify">Queste forme devono essere spiegate tramite <code>start:stop:step</code>, non memorizzate come trucchi.</p>

---

## 9. Immutabilità

<p align="justify">Questo non è ammesso:</p>

```python
parola[0] = "P"
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — immutabilità:</strong>
Una stringa è immutabile: il suo contenuto non può essere modificato in posto. Per ottenere un testo diverso creiamo una nuova stringa.
</p>
</td>
</tr>
</table>

<p align="justify">Per ottenere un nuovo valore:</p>

```python
nuova = "P" + parola[1:]
```

<p align="justify">Il valore originale resta invariato.</p>

---

## 10. Iterazione diretta

<p align="justify">Se serve soltanto il carattere:</p>

```python
for carattere in parola:
    print(carattere)
```

<p align="justify">È spesso più chiaro di:</p>

```python
for i in range(len(parola)):
    print(parola[i])
```

---

## 11. Quando serve l'indice

<p align="justify">L'indice è utile se la posizione è parte del problema:</p>

<ul>
  <li>confrontare caratteri in posizioni diverse;</li>
  <li>estrarre campi fissi;</li>
  <li>costruire un trace posizione/carattere;</li>
  <li>verificare un pattern posizionale.</li>
</ul>

<p align="justify">La scelta deve essere motivata.</p>

---

## 12. Unicode: modello leggero ma corretto

<p align="justify">Core:</p>

<blockquote>
<p align="justify"><code>str</code> rappresenta testo Unicode.</p>
</blockquote>

<p align="justify">Per il secondo anno non serve approfondire encoding/code point/grapheme cluster.</p>

<p align="justify">Teacher note: evitare affermazioni assolute del tipo “ogni simbolo visibile è sempre un singolo indice”. I dettagli Unicode completi appartengono al percorso avanzato.</p>

---

## 13. Letterali ed escape

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — letterale stringa ed escape:</strong>
Un letterale stringa scrive direttamente un valore testuale nel codice, delimitandolo con virgolette. Una sequenza di escape usa la barra inversa per rappresentare caratteri speciali, come <code>\n</code> per un ritorno a capo.
</p>
</td>
</tr>
</table>

<p align="justify">Consolidare:</p>

```python
"ciao"
'ciao'
"riga 1\nriga 2"
"tab\tvalore"
"C:\\cartella"
```

<p align="justify">Triple quote e raw string possono comparire come preview mirata, non come prerequisito.</p>

---

## 14. Worked example: prefisso e suffisso

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Da un codice <code>ABC-123</code> estrai le tre lettere iniziali e le tre cifre finali.</p>
</blockquote>

```python
codice = "ABC-123"
prefisso = codice[:3]
suffisso = codice[-3:]
```

<p align="justify">Casi di test devono chiarire la forma attesa del codice prima di affidarsi alle posizioni.</p>

---

## 15. Error Clinic

<ul>
  <li>indice <code>len(testo)</code> usato come se fosse valido;</li>
  <li>stop incluso invece di escluso;</li>
  <li>tentativo di mutazione;</li>
  <li>indice usato quando bastava il carattere;</li>
  <li>variabile indice riutilizzata male;</li>
  <li>confusione tra slice fuori range e accesso singolo fuori range.</li>
</ul>

---

## 16. Activity candidate

<ul>
  <li><strong>A — Index/slice microscope:</strong> prevedi valore o errore;</li>
  <li><strong>B — Controlled Change:</strong> cambia uno slice e spiega inclusione/esclusione;</li>
  <li><strong>C — Implement:</strong> estrai/ricomponi parti di un codice testuale;</li>
  <li><strong>D — Debug:</strong> correggi indice, slice, mutazione o scelta di iterazione.</li>
</ul>

<p align="justify">Nessuna nuova Activity P2/P1 viene materializzata in questa fase.</p>

---

## 17. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>perché il primo indice è 0;</li>
  <li>qual è l'ultimo indice positivo valido;</li>
  <li><code>start</code> incluso / <code>stop</code> escluso;</li>
  <li>indice singolo fuori range vs slice fuori range;</li>
  <li>che cosa significa immutabile;</li>
  <li>iterazione diretta vs per indice;</li>
  <li>perché uno slicing crea una nuova stringa.</li>
</ol>

---

## 18. Sintesi

```text
str = sequenza ordinata immutabile
```

```text
indice → una posizione
slice  → nuova sottostringa
```

```text
serve solo il carattere? → for diretto
serve la posizione?      → indice
```

<p align="justify">Nel prossimo modulo useremo membership, ricerca e metodi per normalizzare e trasformare il testo in modo consapevole.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>str</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — strings/traversal;</li>
  <li><em>Learning Python / Imparare Python</em> — string object coverage;</li>
  <li><em>Fluent Python</em> — controllo correttezza Unicode/sequence;</li>
  <li><code>friedpython@cb3f3dc...</code> come source pack legacy, non copiato direttamente.</li>
</ul>

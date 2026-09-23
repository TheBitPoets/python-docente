# M21 — Alias, copie, filtri e ordinamento delle liste

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Alias e copie spiegano gli effetti delle mutazioni; filtri e ordinamenti vanno scelti considerando anche l&#x27;input.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Creare e modificare liste e distinguere mutazione e risultato da M20.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare che due nomi possono riferirsi alla stessa lista;<br>prevedere gli effetti di una mutazione attraverso un alias;<br>creare una copia superficiale con <code>.copy()</code> o slicing; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il nome riferisce un oggetto: assegnare un altro nome non costruisce automaticamente una nuova lista. Riprendi <a href="20_LISTE_MUTABILITA_METODI_ITERAZIONE.md">M20 — Liste: mutabilità, metodi essenziali e iterazione</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="22_TUPLE_UNPACKING_MATRICI.md">M22 — Tuple, unpacking, liste annidate e matrici</a>. Tuple e liste annidate rappresentano record, coordinate e dati tabellari con regole diverse di mutabilità.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Confronta b = a e b = a.copy(), modifica un elemento e controlla entrambi i nomi.
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
<strong>UDA:</strong> PY2-07 — Liste, tuple e dati tabellari<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>spiegare che due nomi possono riferirsi alla stessa lista;</li>
  <li>prevedere gli effetti di una mutazione attraverso un alias;</li>
  <li>creare una copia superficiale con <code>.copy()</code> o slicing;</li>
  <li>distinguere alias e copia;</li>
  <li>capire che una copia superficiale non duplica ricorsivamente gli oggetti annidati;</li>
  <li>evitare mutazioni strutturali ingenue durante l'iterazione;</li>
  <li>filtrare/trasformare una lista costruendone una nuova con loop esplicito;</li>
  <li>cercare, contare e aggregare elementi riusando i pattern già noti;</li>
  <li>distinguere <code>sort()</code> e <code>sorted()</code>;</li>
  <li>verificare sia il risultato sia l'eventuale mutazione dell'input.</li>
</ul>

---

## 1. Due nomi, un solo oggetto

```python
a = [10, 20]
b = a
b.append(30)
```

<p align="justify">Che cosa contiene <code>a</code>?</p>

```text
[10, 20, 30]
```

<p align="justify">Modello:</p>

```text
a ─┐
   ├──> [10, 20, 30]
b ─┘
```

<p align="justify"><code>b = a</code> non crea una nuova lista.</p>

---

## 2. Alias

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — alias:</strong>
Un alias è un altro nome per lo stesso oggetto.
</p>
</td>
</tr>
</table>

<p align="justify">Se l'oggetto è mutabile, una mutazione osservata tramite un nome è visibile anche tramite gli altri alias.</p>

<p align="justify">Questo modello sarà importante anche per parametri mutabili e OOP.</p>

---

## 3. Copia superficiale

```python
a = [10, 20]
b = a.copy()
```

<p align="justify">oppure:</p>

```python
b = a[:]
```

<p align="justify">Ora <code>a</code> e <code>b</code> sono liste esterne diverse.</p>

<p align="justify">Per liste piatte di valori immutabili:</p>

```python
b.append(30)
```

<p align="justify">non modifica <code>a</code>.</p>

---

## 4. Copia non significa clonazione infinita

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
```

<p align="justify">Le liste esterne sono diverse, ma gli oggetti interni sono ancora condivisi.</p>

<p align="justify">Modello:</p>

```text
a ─> [ ─────> [1, 9], ─────> [2] ]
b ─> [ ─────> [1, 9], ─────> [2] ]
```

<p align="justify">Per il core basta capire:</p>

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — copia superficiale:</strong>
Una copia superficiale copia il contenitore esterno, non ricrea ricorsivamente tutto ciò che contiene.
</p>
</td>
</tr>
</table>

<p align="justify"><code>deepcopy</code> non è prerequisito.</p>

---

## 5. Testare alias e copia

<p align="justify">Non testare soltanto il risultato finale.</p>

<p align="justify">Se una funzione promette di non mutare l'input:</p>

```python
originale = [3, -1, 5]
risultato = solo_positivi(originale)

assert risultato == [3, 5]
assert originale == [3, -1, 5]
```

<p align="justify">Il secondo assert verifica il contratto di non-mutazione.</p>

---

## 6. Mutare la lista mentre la percorri

<p align="justify">Questo pattern è rischioso:</p>

```python
for valore in numeri:
    if valore < 0:
        numeri.remove(valore)
```

<p align="justify">Mentre il <code>for</code> avanza, la struttura cambia e alcuni elementi possono essere saltati.</p>

---

## 7. Strategia sicura: nuova lista

```python
positivi = []

for valore in numeri:
    if valore >= 0:
        positivi.append(valore)
```

<p align="justify">Vantaggi beginner:</p>

<ul>
  <li>input resta leggibile;</li>
  <li>output è separato;</li>
  <li>il contratto è chiaro;</li>
  <li>il test può verificare che l'input non cambi.</li>
</ul>

---

## 8. Iterare su una copia

<p align="justify">Quando la specifica richiede davvero di modificare la lista originale:</p>

```python
for valore in numeri.copy():
    if valore < 0:
        numeri.remove(valore)
```

<p align="justify">È una strategia possibile, ma va usata consapevolmente.</p>

<p align="justify">Spesso costruire una nuova lista resta più chiaro.</p>

---

## 9. Filtrare

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — filtro:</strong>
Filtrare una sequenza significa selezionare gli elementi che soddisfano una condizione. Qui costruiamo una nuova lista con gli elementi scelti.
</p>
</td>
</tr>
</table>

```python
def solo_positivi(numeri):
    risultato = []
    for numero in numeri:
        if numero > 0:
            risultato.append(numero)
    return risultato
```

<p align="justify">Questo riusa:</p>

```text
loop + if + append + return + test
```

---

## 10. Trasformare

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — trasformazione di una sequenza:</strong>
Trasformare una sequenza significa applicare un'operazione ai suoi elementi per ottenere nuovi valori. Qui li raccogliamo in una nuova lista.
</p>
</td>
</tr>
</table>

```python
def doppi(numeri):
    risultato = []
    for numero in numeri:
        risultato.append(numero * 2)
    return risultato
```

<p align="justify">La lista originale non viene modificata se il contratto non lo richiede.</p>

---

## 11. Comprehension: solo confronto opzionale

<p align="justify">Dopo aver compreso il loop:</p>

```python
positivi = [x for x in numeri if x > 0]
```

<p align="justify">può essere mostrata come forma equivalente e concisa.</p>

<p align="justify">Non è prerequisito del core di seconda.</p>

---

## 12. `sort()` vs `sorted()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — sort() e sorted():</strong>
<code>lista.sort()</code> ordina la lista in posto e restituisce <code>None</code>. <code>sorted(iterabile)</code> restituisce una nuova lista ordinata.
</p>
</td>
</tr>
</table>

```python
numeri.sort()
```

<ul>
  <li>modifica <code>numeri</code>;</li>
  <li>restituisce <code>None</code>.</li>
</ul>

```python
ordinati = sorted(numeri)
```

<ul>
  <li>produce una nuova lista ordinata;</li>
  <li>lascia <code>numeri</code> invariata.</li>
</ul>

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">devo preservare l'ordine originale?</p>
</blockquote>

---

## 13. Bug `sort()` assegnato

```python
numeri = numeri.sort()
```

<p align="justify">Dopo:</p>

```text
numeri → None
```

<p align="justify">È lo stesso modello già visto con <code>append()</code>.</p>

---

## 14. Ricerca e aggregazione sulle liste

<p align="justify">I pattern M11 ora lavorano su dati conservati:</p>

```python
def massimo_lista(numeri):
    massimo = numeri[0]
    for numero in numeri[1:]:
        if numero > massimo:
            massimo = numero
    return massimo
```

<p align="justify">Nota: non usare <code>max</code> come nome variabile perché oscura la built-in <code>max()</code>.</p>

---

## 15. Friedpython: massimo da modernizzare

<p align="justify">L'esercizio legacy sul massimo è concettualmente buono, ma usa:</p>

```python
max = numeri[0]
```

<p align="justify">Nel corso lo riscriviamo con:</p>

```python
massimo = numeri[0]
```

<p align="justify">per non oscurare il nome built-in.</p>

---

## 16. Friedpython: lista inversa come confronto

<p align="justify">Lo spunto legacy usa <code>reversed()</code> + <code>append</code>.</p>

<p align="justify">Possiamo confrontare:</p>

```text
nuova lista costruita manualmente
list(reversed(numeri))
numeri[::-1]
numeri.reverse()
```

<p align="justify">La domanda centrale è:</p>

<blockquote>
<p align="justify">creo un nuovo oggetto o modifico l'originale?</p>
</blockquote>

---

## 17. Performance intuitiva

<p align="justify">Senza Big-O formale:</p>

<ul>
  <li>ricerca in lista → in generale scansione finché trovi/fine;</li>
  <li>inserimento/rimozione in mezzo → può spostare elementi;</li>
  <li><code>append</code> → crescita naturale in coda;</li>
  <li>se domina unicità o lookup per chiave, una lista potrebbe non essere la struttura migliore.</li>
</ul>

<p align="justify">Set/dict arriveranno presto proprio per questo.</p>

---

## 18. Error Clinic

<ul>
  <li>alias involontario;</li>
  <li><code>.copy()</code> interpretato come copia ricorsiva;</li>
  <li>rimozione durante <code>for</code> sulla stessa lista;</li>
  <li><code>sort()</code> assegnato;</li>
  <li>funzione che muta input quando prometteva nuova lista;</li>
  <li>nome <code>max</code>/<code>list</code>/<code>str</code> usato come variabile oscurando built-in importanti.</li>
</ul>

---

## 19. Activity candidate

<ul>
  <li><strong>A — Alias microscope:</strong> disegna nomi e oggetti;</li>
  <li><strong>B — Safe filtering:</strong> ripara mutazione durante iterazione;</li>
  <li><strong>C — Implement:</strong> funzione che filtra/trasforma senza mutare input;</li>
  <li><strong>D — Debug:</strong> alias, shallow copy, sort/None, mutation contract.</li>
</ul>

---

## 20. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li><code>b = a</code> vs <code>b = a.copy()</code>;</li>
  <li>shallow copy;</li>
  <li>perché rimuovere durante iterazione può saltare elementi;</li>
  <li><code>sort</code> vs <code>sorted</code>;</li>
  <li>come testare che l'input non venga mutato;</li>
  <li>perché evitare di oscurare built-in con nomi variabile.</li>
</ol>

---

## 21. Sintesi

```text
alias → stesso oggetto
copy  → nuovo contenitore esterno
```

```text
mutazione prevista? → testala
non-mutazione promessa? → testala
```

```text
sort()   → in-place / None
sorted() → nuova lista
```

<p align="justify">Nel prossimo modulo confronteremo liste e tuple e useremo liste annidate per dati tabellari e matrici.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 su liste/copie/ordinamento;</li>
  <li><em>Think Python / Pensare in Python</em> — aliasing/mutability;</li>
  <li><em>Learning Python / Imparare Python</em> — list operations;</li>
  <li>audit <code>sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md</code>.</li>
</ul>

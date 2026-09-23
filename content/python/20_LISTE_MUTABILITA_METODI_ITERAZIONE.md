# M20 — Liste: mutabilità, metodi essenziali e iterazione

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Le liste mantengono una sequenza modificabile; alcuni metodi cambiano l&#x27;oggetto senza restituire la lista.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare sequenze, indici, slicing e iterazione da M17–M19.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
creare una <code>list</code>;<br>usare <code>len()</code>, indici positivi/negativi e slicing;<br>modificare un elemento per indice; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Una stringa richiede un nuovo oggetto per cambiare testo; una lista può cambiare mantenendo la propria identità. Riprendi <a href="19_ALGORITMI_TESTO_PARSING_SEMPLICE.md">M19 — Algoritmi su testo e parsing semplice</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md">M21 — Alias, copie, filtri e ordinamento delle liste</a>. Alias e copie spiegano gli effetti delle mutazioni; filtri e ordinamenti vanno scelti considerando anche l&#x27;input.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia append e pop distinguendo lo stato della lista dal valore restituito dal metodo.
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
  <li>creare una <code>list</code>;</li>
  <li>usare <code>len()</code>, indici positivi/negativi e slicing;</li>
  <li>modificare un elemento per indice;</li>
  <li>usare <code>append</code>, <code>extend</code>, <code>insert</code>, <code>remove</code>, <code>pop</code> con semantica corretta;</li>
  <li>distinguere metodi che modificano la lista da operazioni che producono un nuovo valore;</li>
  <li>evitare il bug <code>lista = lista.append(...)</code>;</li>
  <li>iterare direttamente sugli elementi;</li>
  <li>usare indice quando la posizione serve davvero;</li>
  <li>usare <code>enumerate()</code> quando servono indice e valore;</li>
  <li>verificare membership con <code>in</code>;</li>
  <li>spiegare la differenza fondamentale tra <code>str</code> immutabile e <code>list</code> mutabile.</li>
</ul>

---

## 1. Da `str` a `list`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — lista e mutabilità:</strong>
Una lista <code>list</code> è una sequenza ordinata e mutabile di elementi. È mutabile perché possiamo cambiare gli elementi, aggiungerli o rimuoverli nello stesso oggetto.
</p>
</td>
</tr>
</table>

<p align="justify">Con una stringa:</p>

```python
testo = "ciao"
```

<p align="justify">non puoi fare:</p>

```python
testo[0] = "C"
```

<p align="justify">Con una lista:</p>

```python
numeri = [10, 20, 30]
numeri[0] = 99
```

<p align="justify">la struttura cambia:</p>

```text
[99, 20, 30]
```

<p align="justify">La mutabilità è il nuovo modello mentale dell'UDA.</p>

---

## 2. Creazione e accesso

```python
numeri = [12, 45, 7]
```

```python
len(numeri)
numeri[0]
numeri[-1]
numeri[1:3]
```

<p align="justify">Indici e slicing riusano il modello imparato sulle stringhe.</p>

<p align="justify">Differenza importante: la lista può essere modificata.</p>

---

## 3. Modifica per indice

```python
numeri = [10, 20, 30]
numeri[1] = 25
```

<p align="justify">Ora:</p>

```text
[10, 25, 30]
```

<p align="justify">Non è stata creata automaticamente una nuova lista: abbiamo mutato l'oggetto esistente.</p>

---

## 4. `append()`

```python
numeri = [10, 20]
numeri.append(30)
```

<p align="justify">Risultato:</p>

```text
[10, 20, 30]
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — append():</strong>
<code>append()</code> aggiunge <strong>un elemento</strong> in fondo.
</p>
</td>
</tr>
</table>

---

## 5. Bug fondamentale: metodo mutante + assegnamento

<p align="justify">Questo è sbagliato:</p>

```python
numeri = [10, 20]
numeri = numeri.append(30)
```

<p align="justify"><code>append()</code> modifica la lista e restituisce <code>None</code>.</p>

<p align="justify">Dopo l'assegnamento:</p>

```text
numeri → None
```

<p align="justify">Questo stesso modello tornerà con <code>sort()</code>.</p>

---

## 6. `append()` vs `extend()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — extend():</strong>
<code>extend()</code> aggiunge alla lista gli elementi di un iterabile, uno alla volta. <code>append()</code> aggiunge invece l'argomento come singolo elemento.
</p>
</td>
</tr>
</table>

```python
x = [1, 2]
x.append([3, 4])
```

<p align="justify">produce:</p>

```text
[1, 2, [3, 4]]
```

<p align="justify">Invece:</p>

```python
x = [1, 2]
x.extend([3, 4])
```

<p align="justify">produce:</p>

```text
[1, 2, 3, 4]
```

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">voglio aggiungere <strong>un elemento</strong> che è una lista oppure incorporare <strong>più elementi</strong>?</p>
</blockquote>

---

## 7. `insert()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — insert():</strong>
<code>lista.insert(indice, valore)</code> inserisce un elemento nella posizione indicata, spostando gli elementi successivi.
</p>
</td>
</tr>
</table>

```python
nomi = ["Anna", "Carlo"]
nomi.insert(1, "Bruno")
```

<p align="justify">Usalo quando la posizione è davvero parte del requisito.</p>

<p align="justify">Non scegliere <code>insert()</code> solo perché esiste.</p>

---

## 8. `remove()` vs `pop()`

```python
valori.remove(7)
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — remove():</strong>
<code>remove(valore)</code> rimuove la prima occorrenza del valore indicato; se non è presente, segnala <code>ValueError</code>. Nell'esempio il valore da rimuovere è 7.
</p>
</td>
</tr>
</table>

```python
ultimo = valori.pop()
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — pop():</strong>
<code>pop()</code> rimuove e restituisce l'ultimo elemento; <code>pop(indice)</code> rimuove e restituisce quello nella posizione indicata.
</p>
</td>
</tr>
</table>

```python
x = valori.pop(2)
```

<p align="justify">rimuove e restituisce l'elemento in <strong>posizione</strong> 2.</p>

<p align="justify">Valore e posizione non sono la stessa cosa.</p>

---

## 9. Iterazione diretta

<p align="justify">Se serve soltanto il valore:</p>

```python
for numero in numeri:
    print(numero)
```

<p align="justify">È la forma naturale per molte scansioni.</p>

---

## 10. Iterazione per indice

<p align="justify">Se la posizione serve al problema:</p>

```python
for i in range(len(numeri)):
    print(i, numeri[i])
```

<p align="justify">Non usare l'indice come rituale.</p>

---

## 11. `enumerate()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — enumerate():</strong>
<code>enumerate()</code> permette di attraversare una sequenza ottenendo insieme l'indice e il valore di ciascun elemento. Il conteggio parte da 0 se non viene indicato un altro inizio.
</p>
</td>
</tr>
</table>

<p align="justify">Quando servono insieme indice e valore:</p>

```python
for i, numero in enumerate(numeri):
    print(i, numero)
```

<p align="justify">Ora possiamo rileggere <code>i, numero</code> come unpacking di una coppia prodotta dall'iterazione.</p>

---

## 12. Membership

```python
7 in numeri
```

<p align="justify">restituisce un booleano.</p>

<p align="justify">Il modello è identico alla membership nelle stringhe, ma ora gli elementi possono essere valori di tipi diversi secondo il contratto della lista.</p>

---

## 13. Slicing di una lista

```python
prima_parte = numeri[:3]
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — slicing di lista:</strong>
Lo slicing di una lista produce una nuova lista superficiale con gli elementi selezionati: il contenitore è nuovo, mentre gli elementi sono gli stessi oggetti selezionati dall'originale.
</p>
</td>
</tr>
</table>

<p align="justify">Nel prossimo modulo distingueremo in dettaglio:</p>

```text
alias
vs
copia
```

---

## 14. Worked example: raccolta di N valori

```python
n = int(input())
valori = []

for _ in range(n):
    valori.append(int(input()))
```

<p align="justify">Ora i dati rimangono disponibili per più elaborazioni successive.</p>

<p align="justify">Questo è diverso da elaborare ogni valore e dimenticarlo subito.</p>

---

## 15. Error Clinic

<ul>
  <li><code>lista = lista.append(x)</code>;</li>
  <li><code>append([a, b])</code> quando serviva <code>extend([a, b])</code>;</li>
  <li><code>remove(indice)</code> pensando che rimuova per posizione;</li>
  <li>indice fuori range;</li>
  <li>iterazione per indice quando la posizione non serve;</li>
  <li>modifica dell'elemento sbagliato.</li>
</ul>

---

## 16. Confronto da `friedpython`

<p align="justify">Gli esercizi legacy 1 e 2 mostrano bene lo stesso attraversamento con:</p>

```text
while + indice
vs
for diretto sugli elementi
```

<p align="justify">Nel corso 2026/27 li trattiamo come <strong>confronto di intenzione</strong>, non come due sintassi equivalenti da memorizzare.</p>

<p align="justify">Se la posizione non serve, il <code>for</code> diretto comunica meglio il problema.</p>

---

## 17. Activity candidate

<ul>
  <li><strong>A — Predict mutation:</strong> prevedi lista e return dopo operazioni;</li>
  <li><strong>B — Controlled Change:</strong> scegli <code>append/extend/insert/remove/pop</code> da una specifica;</li>
  <li><strong>C — Implement:</strong> costruisci una lista da N input e calcola proprietà già note;</li>
  <li><strong>D — Debug:</strong> metodo mutante assegnato, indice, remove/pop, append/extend.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 18. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li><code>str</code> immutabile vs <code>list</code> mutabile;</li>
  <li><code>append</code> vs <code>extend</code>;</li>
  <li><code>remove</code> vs <code>pop</code>;</li>
  <li>perché <code>lista = lista.append(x)</code> è un bug;</li>
  <li>valore vs indice;</li>
  <li><code>for</code> diretto vs indice vs <code>enumerate</code>.</li>
</ol>

---

## 19. Sintesi

```text
list = sequenza ordinata mutabile
```

```text
metodo mutante
→ cambia l'oggetto
→ spesso restituisce None
```

```text
solo valore → for diretto
indice+valore → enumerate
```

<p align="justify">Nel prossimo modulo vedremo che due nomi possono riferirsi <strong>alla stessa lista</strong>: alias, copie e mutazioni diventano quindi fondamentali.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 sulle liste;</li>
  <li><em>Think Python / Pensare in Python</em> — lists/mutability;</li>
  <li><em>Learning Python / Imparare Python</em> — list object coverage;</li>
  <li><code>friedpython@cb3f3dc...</code> auditato in <code>sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md</code>.</li>
</ul>

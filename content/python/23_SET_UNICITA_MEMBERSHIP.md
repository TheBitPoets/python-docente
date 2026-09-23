# M23 — Set: unicità, membership e operazioni insiemistiche

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il set modella unicità e appartenenza e permette operazioni fra insiemi.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare membership, cicli e collezioni da M20–M22; consolidare il Checkpoint B.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
creare un <code>set</code> non vuoto;<br>creare un set vuoto con <code>set()</code> e distinguere <code>{}</code>;<br>spiegare che gli elementi sono unici; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Una struttura si sceglie per le operazioni richieste: la posizione nella lista non è il modello del set. Riprendi <a href="22_TUPLE_UNPACKING_MATRICI.md">M22 — Tuple, unpacking, liste annidate e matrici</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="24_DIZIONARI_LOOKUP_FREQUENZE.md">M24 — Dizionari: chiave→valore, lookup e frequenze</a>. Il dizionario associa chiavi uniche a valori e sostiene lookup e conteggi di frequenza.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Calcola unione, intersezione e differenza dei corsi frequentati, senza dipendere dall&#x27;ordine di stampa.
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
<strong>UDA:</strong> PY2-08 — Set, dizionari e modellazione dei dati<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>creare un <code>set</code> non vuoto;</li>
  <li>creare un set vuoto con <code>set()</code> e distinguere <code>{}</code>;</li>
  <li>spiegare che gli elementi sono unici;</li>
  <li>usare <code>add</code>, <code>remove</code>, <code>discard</code> consapevolmente;</li>
  <li>usare membership <code>in</code>/<code>not in</code>;</li>
  <li>usare unione, intersezione e differenza;</li>
  <li>deduplicare quando l'ordine non è requisito dominante;</li>
  <li>scegliere <code>set</code> vs <code>list</code> in base a unicità/membership/ordine;</li>
  <li>non dipendere dall'ordine di iterazione/stampa di un set;</li>
  <li>capire a livello beginner che gli elementi devono essere hashable.</li>
</ul>

---

## 1. Il set non è una lista senza duplicati

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — insieme — set:</strong>
Un <code>set</code> è una collezione mutabile di valori distinti. Rappresenta appartenenza e unicità; non offre posizioni indicizzate né un ordine su cui basare la soluzione.
</p>
</td>
</tr>
</table>

```python
tag = {"python", "git", "linux"}
```

<p align="justify">Modello:</p>

```text
set = collezione di valori distinti
```

<p align="justify">Le domande naturali sono:</p>

```text
questo valore appartiene all'insieme?
quali valori sono comuni?
quali valori sono presenti solo da una parte?
```

<p align="justify">Non:</p>

```text
qual è l'elemento in posizione 2?
```

<p align="justify">Il set non è una sequenza indicizzata.</p>

---

## 2. Set vuoto

<p align="justify">Questo crea un <strong>dict vuoto</strong>:</p>

```python
x = {}
```

<p align="justify">Per un set vuoto:</p>

```python
x = set()
```

<p align="justify">È un Error Clinic obbligatorio.</p>

---

## 3. Unicità

```python
nomi = ["anna", "luca", "anna", "marta"]
unici = set(nomi)
```

<p align="justify">Semanticamente otteniamo i valori distinti.</p>

<p align="justify">Se l'ordine originale è requisito, convertire semplicemente in set può perdere informazione importante sul modello.</p>

---

## 4. Membership

```python
"python" in tag
```

<p align="justify">Quando la domanda dominante è membership ripetuta, il set è una struttura naturale.</p>

<p align="justify">Intuizione prestazionale:</p>

```text
list → ricerca lungo la sequenza
set  → progettato per membership tramite hashing
```

<p align="justify">Non introduciamo ancora Big-O formale né promesse assolute sul tempo.</p>

---

## 5. `add()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — add():</strong>
<code>insieme.add(valore)</code> aggiunge un valore al set. Se è già presente, l'insieme conserva una sola occorrenza.
</p>
</td>
</tr>
</table>

```python
tag.add("docker")
```

<p align="justify">Se l'elemento è già presente, il set continua ad averne una sola copia.</p>

<p align="justify">Questa proprietà deriva dalla semantica del set, non da un controllo manuale sui duplicati.</p>

---

## 6. `remove()` vs `discard()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — remove() e discard() sui set:</strong>
Entrambi rimuovono il valore indicato dal set. Se il valore manca, <code>remove()</code> segnala <code>KeyError</code>, mentre <code>discard()</code> lascia l'insieme invariato senza segnalare errore.
</p>
</td>
</tr>
</table>

```python
insieme.remove(x)
```

<p align="justify">se <code>x</code> manca, segnala un errore.</p>

```python
insieme.discard(x)
```

<p align="justify">se <code>x</code> manca, non genera errore.</p>

<p align="justify">La scelta dipende dal contratto:</p>

<ul>
  <li>assenza inattesa → <code>remove</code> può evidenziare un problema;</li>
  <li>“assicura che x non ci sia” → <code>discard</code> può essere naturale.</li>
</ul>

---

## 7. Unione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — unione di insiemi:</strong>
L'unione contiene gli elementi presenti in almeno uno dei due insiemi, senza duplicati.
</p>
</td>
</tr>
</table>

```python
A | B
```

<p align="justify">oppure:</p>

```python
A.union(B)
```

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">quali elementi appartengono ad almeno uno dei due insiemi?</p>
</blockquote>

---

## 8. Intersezione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — intersezione di insiemi:</strong>
L'intersezione contiene soltanto gli elementi presenti in entrambi gli insiemi.
</p>
</td>
</tr>
</table>

```python
A & B
```

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">quali elementi appartengono a entrambi?</p>
</blockquote>

<p align="justify">Esempio naturale: studenti iscritti a due attività.</p>

---

## 9. Differenza

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — differenza di insiemi:</strong>
La differenza <code>A - B</code> contiene gli elementi presenti in A e assenti da B. Scambiando l'ordine degli insiemi può cambiare il risultato.
</p>
</td>
</tr>
</table>

```python
A - B
```

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">quali elementi sono in A ma non in B?</p>
</blockquote>

<p align="justify">L'ordine degli operandi conta.</p>

---

## 10. Worked example: corsi frequentati

```python
python = {"Anna", "Luca", "Marta"}
git = {"Luca", "Paolo", "Marta"}
```

<p align="justify">Possiamo chiedere:</p>

```python
entrambi = python & git
almeno_uno = python | git
solo_python = python - git
```

<p align="justify">Prima di eseguire, prevedi semanticamente i gruppi.</p>

---

## 11. Set vs list

<table align="center">
<thead>
<tr>
<th>Esigenza</th>
<th><code>list</code></th>
<th><code>set</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>ordine/posizione</td>
<td>naturale</td>
<td>non è il criterio del set</td>
</tr>
<tr>
<td>duplicati significativi</td>
<td>sì</td>
<td>no</td>
</tr>
<tr>
<td>mutazione sequenziale</td>
<td>sì</td>
<td>sì, con semantica insiemistica</td>
</tr>
<tr>
<td>membership dominante</td>
<td>possibile</td>
<td>naturale</td>
</tr>
<tr>
<td>indice/slicing</td>
<td>sì</td>
<td>no</td>
</tr>
<tr>
<td>unione/intersezione</td>
<td>manuale</td>
<td>naturale</td>
</tr>
</tbody>
</table>

---

## 12. Hashability beginner

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — hashable:</strong>
Un valore è <em>hashable</em> se ha un valore hash che resta stabile durante la sua vita e coerente con l'uguaglianza: valori uguali devono avere lo stesso hash. Gli elementi di un set e le chiavi di un dizionario devono essere hashable.
</p>
</td>
</tr>
</table>

<p align="justify">Candidati comuni:</p>

```text
str
int
float
bool
tuple di elementi hashable
```

<p align="justify">Non puoi inserire direttamente una <code>list</code> mutabile come elemento di un set.</p>

<p align="justify">Gli internals dell'hash table arrivano più avanti.</p>

---

## 13. Non dipendere dall'ordine

<p align="justify">Non scrivere un algoritmo che assume:</p>

```text
"il primo elemento stampato dal set sarà..."
```

<p align="justify">Se l'ordine è requisito del problema, scegli una struttura/strategia che lo rappresenti esplicitamente.</p>

---

## 14. Error Clinic

<ul>
  <li><code>{}</code> usato come set vuoto;</li>
  <li>aspettarsi duplicati;</li>
  <li>usare indice/slice su set;</li>
  <li>affidarsi all'ordine di iterazione;</li>
  <li><code>remove</code> su elemento assente quando il contratto voleva idempotenza;</li>
  <li>lista mutabile usata come elemento;</li>
  <li>set scelto quando l'ordine di prima occorrenza era parte del requisito.</li>
</ul>

---

## 15. Activity candidate

<ul>
  <li><strong>A — Set microscope:</strong> prevedi contenuto semantico dopo add/duplicati;</li>
  <li><strong>B — List or set?</strong> scegli e motiva;</li>
  <li><strong>C — Implement:</strong> unione/intersezione/differenza tra gruppi/tag;</li>
  <li><strong>D — Debug:</strong> <code>{}</code>, ordine, duplicati, remove/discard, elemento non hashable.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 16. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>perché <code>{}</code> non è set vuoto;</li>
  <li>unicità;</li>
  <li>membership come operazione dominante;</li>
  <li><code>remove</code> vs <code>discard</code>;</li>
  <li>unione/intersezione/differenza;</li>
  <li>list vs set;</li>
  <li>perché non usare indici/ordine come proprietà del set.</li>
</ol>

---

## 17. Sintesi

```text
set → valori unici + membership + operazioni insiemistiche
```

```text
ordine importante? → chiediti se set è davvero il modello giusto
```

<p align="justify">Nel prossimo modulo passeremo da “appartiene?” a una domanda diversa:</p>

```text
chiave → quale valore associato?
```

<p align="justify">cioè il modello del dizionario.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>set</code>/<code>frozenset</code> (solo <code>set</code> core);</li>
  <li><em>Fluent Python</em> come controllo teacher-side su hashing/collections;</li>
  <li><em>Learning Python / Imparare Python</em> — set coverage;</li>
  <li>Pluralsight come gap-check.</li>
</ul>

<p align="justify"><code>friedpython</code> non dispone di un blocco set centrale equivalente; M23 è quindi originale.</p>

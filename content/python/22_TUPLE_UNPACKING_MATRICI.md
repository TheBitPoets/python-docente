# M22 — Tuple, unpacking, liste annidate e matrici

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Tuple e liste annidate rappresentano record, coordinate e dati tabellari con regole diverse di mutabilità.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare liste, copie, alias e cicli annidati da M12 e M20–M21.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
creare e leggere una <code>tuple</code>;<br>spiegare che una tupla è una sequenza immutabile;<br>creare correttamente una tupla a un elemento <code>(x,)</code>; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
La copia superficiale non duplica gli oggetti interni; la stessa attenzione serve quando costruisci righe di una matrice. Riprendi <a href="21_ALIAS_COPIE_FILTRI_ORDINAMENTO.md">M21 — Alias, copie, filtri e ordinamento delle liste</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="23_SET_UNICITA_MEMBERSHIP.md">M23 — Set: unicità, membership e operazioni insiemistiche</a>. Il set modella unicità e appartenenza e permette operazioni fra insiemi.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Costruisci una matrice con righe indipendenti e confrontala con la versione che riusa la stessa riga.
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
  <li>creare e leggere una <code>tuple</code>;</li>
  <li>spiegare che una tupla è una sequenza immutabile;</li>
  <li>creare correttamente una tupla a un elemento <code>(x,)</code>;</li>
  <li>usare packing e unpacking semplici;</li>
  <li>scegliere intuitivamente <code>list</code> vs <code>tuple</code>;</li>
  <li>usare tuple come piccoli record posizionali/coordinate quando appropriato;</li>
  <li>usare liste di tuple e strutture combinate semplici;</li>
  <li>creare e attraversare una lista di liste;</li>
  <li>usare accesso <code>[riga][colonna]</code>;</li>
  <li>riusare cicli annidati sui dati tabellari;</li>
  <li>diagnosticare la trappola delle righe condivise nella costruzione di matrici.</li>
</ul>

---

## 1. Una tupla è una sequenza immutabile

```python
punto = (3, 5)
```

<p align="justify">Come una lista, ha ordine e indici.</p>

```python
punto[0]
punto[1]
```

<p align="justify">Ma non puoi fare:</p>

```python
punto[0] = 10
```

<p align="justify">Il contenitore tupla è immutabile.</p>

---

## 2. Perché scegliere una tupla?

<p align="justify">Domanda beginner:</p>

```text
questa sequenza deve crescere/cambiare
oppure rappresenta un raggruppamento stabile di valori posizionali?
```

<p align="justify">Esempi candidati:</p>

<ul>
  <li>voti da aggiungere/rimuovere → <code>list</code>;</li>
  <li>coordinata <code>(x, y)</code> → <code>tuple</code>;</li>
  <li>colore RGB <code>(r, g, b)</code> → <code>tuple</code> candidata;</li>
  <li>lista modificabile di coordinate → lista di tuple.</li>
</ul>

<p align="justify">Non scegliamo tuple perché “sono sempre più veloci”. Il criterio principale è il modello dei dati.</p>

---

## 3. La virgola conta

```python
x = (40)
```

<p align="justify"><code>x</code> è un intero.</p>

```python
y = (40,)
```

<p align="justify"><code>y</code> è una tupla a un elemento.</p>

<p align="justify">È la virgola che costruisce il raggruppamento tuple in questo caso.</p>

---

## 4. Packing

<p align="justify">Python può creare una tupla anche tramite comma expression:</p>

```python
punto = 3, 5
```

<p align="justify">Per il corso beginner preferiamo spesso le parentesi quando migliorano la leggibilità:</p>

```python
punto = (3, 5)
```

---

## 5. Unpacking

```python
punto = (3, 5)
x, y = punto
```

<p align="justify">Ora:</p>

```text
x → 3
y → 5
```

<p align="justify">L'unpacking dà nomi significativi ai ruoli dei valori.</p>

---

## 6. `enumerate()` riletto con unpacking

<p align="justify">Abbiamo già scritto:</p>

```python
for indice, valore in enumerate(valori):
    ...
```

<p align="justify">Ora possiamo capire meglio il modello:</p>

```text
enumerate produce coppie
→ la coppia viene unpacked in indice, valore
```

<p align="justify">Non serve approfondire il tipo interno dell'iteratore.</p>

---

## 7. Tuple contenenti oggetti mutabili

<p align="justify">Enrichment controllato:</p>

```python
t = (1, [2, 3], 4)
```

<p align="justify">Non puoi sostituire:</p>

```python
t[1] = []
```

<p align="justify">ma la lista che si trova dentro è ancora un oggetto mutabile:</p>

```python
t[1].append(9)
```

<p align="justify">Quindi:</p>

<blockquote>
<p align="justify">immutabilità della tupla significa che i riferimenti dei suoi elementi non possono essere riassegnati tramite la tupla; non significa che ogni oggetto contenuto diventi magicamente immutabile.</p>
</blockquote>

<p align="justify">Questo è enrichment, non prerequisito della scelta list/tuple.</p>

---

## 8. Liste annidate

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
```

<p align="justify">Una lista può contenere altre liste.</p>

<p align="justify">Accesso:</p>

```python
matrice[0]       # prima riga
matrice[1][2]    # 6
```

---

## 9. Dati tabellari

<p align="justify">Modello:</p>

```text
riga 0 → [1, 2, 3]
riga 1 → [4, 5, 6]
```

<p align="justify">Questo rappresenta naturalmente problemi come:</p>

<ul>
  <li>griglie;</li>
  <li>posti occupati/liberi;</li>
  <li>tabelle di misure;</li>
  <li>board semplici;</li>
  <li>matrici numeriche elementari.</li>
</ul>

<p align="justify">Non usare una matrice se una lista piatta comunica meglio il dominio.</p>

---

## 10. Attraversare una matrice

<p align="justify">Per valore:</p>

```python
for riga in matrice:
    for valore in riga:
        print(valore)
```

<p align="justify">Se servono coordinate:</p>

```python
for r in range(len(matrice)):
    for c in range(len(matrice[r])):
        print(r, c, matrice[r][c])
```

<p align="justify">La scelta riusa M12: valore soltanto vs posizione necessaria.</p>

---

## 11. Worked example: somma per riga

```python
def somme_righe(matrice):
    risultati = []

    for riga in matrice:
        totale = 0
        for valore in riga:
            totale += valore
        risultati.append(totale)

    return risultati
```

<p align="justify">Invariante interno:</p>

<blockquote>
<p align="justify"><code>totale</code> è la somma dei valori già visti nella riga corrente.</p>
</blockquote>

<p align="justify">Invariante esterno:</p>

<blockquote>
<p align="justify"><code>risultati</code> contiene le somme delle righe già elaborate.</p>
</blockquote>

---

## 12. Alias trap nella costruzione

<p align="justify">Questo sembra creare righe indipendenti:</p>

```python
matrice = [[0] * colonne] * righe
```

<p align="justify">ma le righe possono riferirsi <strong>alla stessa lista interna</strong>.</p>

<p align="justify">Poi:</p>

```python
matrice[0][0] = 1
```

<p align="justify">può modificare la prima posizione di tutte le righe.</p>

<p align="justify">È M21 che ritorna dentro le matrici.</p>

---

## 13. Costruzione sicura beginner

<p align="justify">Forma esplicita:</p>

```python
matrice = []

for _ in range(righe):
    matrice.append([0] * colonne)
```

<p align="justify">Ogni iterazione crea una nuova lista riga.</p>

<p align="justify">Una comprehension equivalente può essere mostrata solo dopo:</p>

```python
matrice = [[0] * colonne for _ in range(righe)]
```

<p align="justify">come enrichment, non come prerequisito.</p>

---

## 14. Ragged rows

<p align="justify">Non tutte le liste di liste sono matrici rettangolari:</p>

```python
dati = [
    [1, 2],
    [3, 4, 5],
]
```

<p align="justify">Per questo, quando usiamo indici, spesso il limite corretto della colonna è:</p>

```python
len(matrice[r])
```

<p align="justify">non una costante assunta senza contratto.</p>

---

## 15. List vs tuple: confronto

<table align="center">
<thead>
<tr>
<th>Domanda</th>
<th><code>list</code></th>
<th><code>tuple</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>sequenza ordinata</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>mutabile</td>
<td>sì</td>
<td>no, al primo livello del contenitore</td>
</tr>
<tr>
<td>append/remove</td>
<td>sì</td>
<td>no</td>
</tr>
<tr>
<td>record posizionale stabile</td>
<td>possibile</td>
<td>spesso naturale</td>
</tr>
<tr>
<td>collezione che cresce</td>
<td>naturale</td>
<td>di solito no</td>
</tr>
</tbody>
</table>

<p align="justify">La scelta dipende dal significato dei dati.</p>

---

## 16. Error Clinic

<ul>
  <li><code>(5)</code> pensato come tupla a un elemento;</li>
  <li>tentativo di assegnamento a elemento tuple;</li>
  <li>unpacking con numero di valori incompatibile;</li>
  <li><code>[riga][colonna]</code> invertiti;</li>
  <li>range colonne fisso su righe di lunghezza diversa;</li>
  <li><code>[[0] * C] * R</code> con righe alias;</li>
  <li>lista annidata scelta senza motivo quando bastava una lista piatta.</li>
</ul>

---

## 17. Activity candidate

<ul>
  <li><strong>A — List or tuple?</strong> struttura + motivazione;</li>
  <li><strong>B — Unpacking trace:</strong> coppie/coordinate;</li>
  <li><strong>C — Matrix traversal:</strong> somma/ricerca per righe e colonne;</li>
  <li><strong>D — Alias matrix debug:</strong> diagnosticare righe condivise;</li>
  <li><strong>E — Mini-project tabellare:</strong> più funzioni, matrice piccola, test, spiegazione del modello dati.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 18. Friedpython tuple: cosa riusiamo e cosa no

<p align="justify">Spunti validi:</p>

<ul>
  <li>immutabilità;</li>
  <li>conversione list/tuple;</li>
  <li><code>index</code>/<code>count</code>;</li>
  <li>tupla a un elemento;</li>
  <li>oggetto mutabile annidato come enrichment.</li>
</ul>

<p align="justify">Da non copiare:</p>

<ul>
  <li>sintassi <code>print T</code> Python 2;</li>
  <li>note storiche non necessarie;</li>
  <li>comprehension prima del nostro ordine didattico.</li>
</ul>

---

## 19. Exit checkpoint PY2-07

<p align="justify">Dovresti saper:</p>

<ul>
  <li>usare liste e metodi essenziali;</li>
  <li>prevedere mutazioni;</li>
  <li>spiegare alias vs copia;</li>
  <li>filtrare/trasformare senza mutazione accidentale;</li>
  <li>usare <code>sort</code>/<code>sorted</code> correttamente;</li>
  <li>usare tuple/unpacking;</li>
  <li>scegliere list vs tuple;</li>
  <li>costruire e attraversare una lista di liste;</li>
  <li>evitare righe condivise involontarie;</li>
  <li>motivare la struttura usata.</li>
</ul>

---

## 20. Sintesi

```text
list  → sequenza mutabile
 tuple → sequenza stabile/immutabile come contenitore
```

```text
matrice = lista di righe
```

```text
aliasing non sparisce nelle strutture annidate
```

<p align="justify">Checkpoint B consoliderà stringhe, liste e tuple prima di set e dizionari.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 tuple/liste/sequenze;</li>
  <li><em>Think Python / Pensare in Python</em> — tuples/lists;</li>
  <li><em>Learning Python / Imparare Python</em> — sequence types;</li>
  <li>audit <code>sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md</code>.</li>
</ul>

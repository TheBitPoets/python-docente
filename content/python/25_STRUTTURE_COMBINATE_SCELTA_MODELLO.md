# M25 — Strutture combinate e scelta del modello dati

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
La scelta del modello combina strutture semplici secondo identità, ordine, unicità e operazioni dominanti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare list, tuple, set e dict con funzioni e cicli da M20–M24.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
scegliere tra <code>str</code>, <code>list</code>, <code>tuple</code>, <code>set</code> e <code>dict</code> in base alle operazioni dominanti;<br>costruire semplici strutture combinate quando il dominio lo richiede;<br>usare una lista di tuple o una lista di dict come collezione di record semplici; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Annidare strutture deve esprimere una relazione del dominio, non aggiungere complessità senza motivo. Riprendi <a href="24_DIZIONARI_LOOKUP_FREQUENZE.md">M24 — Dizionari: chiave→valore, lookup e frequenze</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="26_FILE_TESTO_PATHLIB_ERRORI.md">M26 — File testo, <code>pathlib</code> ed errori esterni prevedibili</a>. I file conservano testo oltre l&#x27;esecuzione; percorsi e gestione mirata degli errori delimitano l&#x27;I/O.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Confronta due modelli per il catalogo prodotti e motiva quale facilita le operazioni richieste.
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
  <li>scegliere tra <code>str</code>, <code>list</code>, <code>tuple</code>, <code>set</code> e <code>dict</code> in base alle operazioni dominanti;</li>
  <li>costruire semplici strutture combinate quando il dominio lo richiede;</li>
  <li>usare una lista di tuple o una lista di dict come collezione di record semplici;</li>
  <li>usare un dict con valori lista per raggruppare elementi per chiave;</li>
  <li>usare strutture annidate senza creare profondità inutile;</li>
  <li>distinguere ordine, mutabilità, unicità, membership e lookup;</li>
  <li>confrontare due modelli corretti e motivare quale comunica meglio l'intenzione;</li>
  <li>riconoscere liste parallele fragili;</li>
  <li>capire intuitivamente perché un lookup per chiave può essere più naturale di una scansione ripetuta;</li>
  <li>preparare il passaggio record/dict → oggetto delle settimane OOP.</li>
</ul>

---

## 1. Non esiste “la struttura migliore” in assoluto

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">quali operazioni dominano questo problema?</p>
</blockquote>

<p align="justify">Criteri:</p>

```text
ordine
mutabilità
duplicati/unicità
membership
lookup per chiave
record/attributi
relazioni uno→molti
```

<p align="justify">La struttura deve rendere naturali le operazioni importanti.</p>

---

## 2. Mappa di scelta beginner

```text
sequenza testuale immutabile            → str
sequenza ordinata che cambia             → list
raggruppamento posizionale stabile        → tuple
valori unici / membership                 → set
chiave → valore / lookup                  → dict
```

<p align="justify">Questa mappa è un punto di partenza, non una legge meccanica.</p>

---

## 3. Liste parallele: modello fragile

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — liste parallele:</strong>
Le liste parallele conservano campi collegati in liste diverse: gli elementi nella stessa posizione appartengono allo stesso record. La loro corrispondenza deve rimanere sincronizzata.
</p>
</td>
</tr>
</table>

```python
nomi = ["Anna", "Luca", "Marta"]
voti = [8, 7, 9]
```

<p align="justify">Il legame è implicito:</p>

```text
nomi[i] ↔ voti[i]
```

<p align="justify">Se le due liste perdono sincronizzazione, il record si rompe.</p>

---

## 4. Alternativa: lista di tuple

```python
studenti = [
    ("Anna", 8),
    ("Luca", 7),
    ("Marta", 9),
]
```

<p align="justify">Ogni elemento raggruppa i valori del record.</p>

<p align="justify">Unpacking:</p>

```python
for nome, voto in studenti:
    ...
```

<p align="justify">È adeguato quando pochi campi hanno ruoli posizionali chiari e stabili.</p>

---

## 5. Alternativa: lista di dict

```python
studenti = [
    {"nome": "Anna", "voto": 8},
    {"nome": "Luca", "voto": 7},
]
```

<p align="justify">I campi sono nominati.</p>

<p align="justify">Vantaggio:</p>

```text
record leggibile per nome del campo
```

<p align="justify">Costo concettuale:</p>

<ul>
  <li>più struttura;</li>
  <li>chiavi ripetute;</li>
  <li>accesso tramite stringhe.</li>
</ul>

<p align="justify">Non significa che sia sempre migliore della tupla.</p>

---

## 6. Dict indicizzato per identità

<p align="justify">Se il requisito dominante è:</p>

<blockquote>
<p align="justify">dato il nome, trova rapidamente il voto</p>
</blockquote>

<p align="justify">potremmo modellare:</p>

```python
voti = {
    "Anna": 8,
    "Luca": 7,
    "Marta": 9,
}
```

<p align="justify">Il problema non richiede più una scansione della lista per ogni lookup.</p>

<p align="justify">La chiave coincide con l'identità usata dal dominio.</p>

---

## 7. Dict di liste: uno→molti

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Raggruppa parole per iniziale.</p>
</blockquote>

```python
gruppi = {}

for parola in parole:
    iniziale = parola[0]

    if iniziale not in gruppi:
        gruppi[iniziale] = []

    gruppi[iniziale].append(parola)
```

<p align="justify">Modello:</p>

```text
iniziale → lista di parole
```

---

## 8. `setdefault()` come enrichment

<p align="justify">Dopo aver compreso il pattern precedente:</p>

```python
gruppi.setdefault(iniziale, []).append(parola)
```

<p align="justify">può essere mostrato come forma standard compatta.</p>

<p align="justify">Non deve nascondere il modello:</p>

```text
se la chiave manca → crea una lista
poi aggiungi il valore
```

---

## 9. Friedpython: inversione frequenze

<p align="justify">Un esercizio legacy costruisce:</p>

```text
frequenza → lista di caratteri
```

<p align="justify">Esempio concettuale:</p>

```python
{
    3: ["a", "e"],
    1: ["x"],
}
```

<p align="justify">È un buon esempio M25 perché combina:</p>

```text
dict + valori list + accumulo per chiave
```

<p align="justify">Va riscritto, non copiato.</p>

---

## 10. Set dentro un dict

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Per ogni corso, conserva gli studenti iscritti senza duplicati.</p>
</blockquote>

```python
iscritti = {
    "python": {"Anna", "Luca"},
    "git": {"Luca", "Marta"},
}
```

<p align="justify">Modello:</p>

```text
corso → set di studenti unici
```

<p align="justify">Strutture combinate hanno senso quando ogni livello ha una semantica chiara.</p>

---

## 11. Evitare annidamento gratuito

<p align="justify">Questo tipo di struttura:</p>

```python
{"a": {"b": [{"c": ...}]}}
```

<p align="justify">non è “più professionale” perché è profonda.</p>

<p align="justify">Domande:</p>

<ul>
  <li>ogni livello rappresenta una relazione reale?;</li>
  <li>posso nominare il significato di ciascun contenitore?;</li>
  <li>il codice di accesso resta comprensibile?.</li>
</ul>

<p align="justify">Se no, il modello va semplificato.</p>

---

## 12. Lookup intuition

<p align="justify">Con una lista di record, cercare una chiave spesso significa:</p>

```text
scansiona finché trovi
```

<p align="justify">Con un dict progettato sulla chiave:</p>

```text
usa direttamente la chiave
```

<p align="justify">Non formalizziamo Big-O, ma introduciamo il principio:</p>

<blockquote>
<p align="justify">una struttura può rendere naturale ed efficiente un'operazione dominante.</p>
</blockquote>

---

## 13. Ordine vs lookup

<p align="justify">Un dict moderno preserva l'ordine di inserimento, ma la sua semantica primaria resta il mapping chiave→valore.</p>

<p align="justify">Se il problema richiede:</p>

```text
prima posizione
seconda posizione
slicing
```

<p align="justify">una sequenza resta probabilmente il modello più naturale.</p>

<p align="justify">Non scegliere dict soltanto perché può mantenere ordine.</p>

---

## 14. Worked example: catalogo prodotti

<p align="justify">Requisiti:</p>

<ul>
  <li>lookup per codice prodotto;</li>
  <li>ogni prodotto ha nome/prezzo/categoria;</li>
  <li>i codici sono unici.</li>
</ul>

<p align="justify">Modello candidato:</p>

```python
catalogo = {
    "P001": {"nome": "Penna", "prezzo": 1.5, "categoria": "scrittura"},
    "Q010": {"nome": "Quaderno", "prezzo": 3.0, "categoria": "carta"},
}
```

<p align="justify">Per il secondo anno non serve costruire un'app completa.</p>

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">perché la chiave esterna <code>P001</code> è naturale per il lookup?</p>
</blockquote>

---

## 15. Bridge verso OOP

<p align="justify">Una struttura come:</p>

```python
{"nome": "Anna", "voto": 8}
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — record:</strong>
Un record raggruppa i dati relativi a una stessa entità in campi con ruoli precisi. Nell'esempio il dizionario rappresenta un record con campi nominati.
</p>
</td>
</tr>
</table>

<p align="justify">Più avanti potremo chiederci:</p>

<blockquote>
<p align="justify">quando questi dati hanno anche comportamenti/invarianti propri, ha senso introdurre una classe?</p>
</blockquote>

<p align="justify">Questo è il ponte M25 → M27–M30.</p>

<p align="justify">Non anticipiamo ancora le classi.</p>

---

## 16. Matrix sparse come enrichment

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — matrice sparsa:</strong>
Una matrice sparsa contiene molti valori nulli. Possiamo rappresentarla conservando soltanto le celle significative, per esempio in un dizionario che associa una coppia di coordinate al valore della cella.
</p>
</td>
</tr>
</table>

<p align="justify">Dopo tuple + dict possiamo rappresentare solo celle non zero:</p>

```python
celle = {
    (0, 2): 5,
    (3, 1): 7,
}
```

<p align="justify">Lookup:</p>

```python
celle.get((r, c), 0)
```

<p align="justify">È un buon esempio di struttura scelta dalle operazioni/densità dei dati, ma non è core obbligatorio.</p>

---

## 17. Error Clinic

<ul>
  <li>liste parallele fuori sincronizzazione;</li>
  <li>set usato quando duplicati/ordine erano significativi;</li>
  <li>dict usato quando il problema era puramente posizionale;</li>
  <li>tupla usata per record con molti campi poco leggibili;</li>
  <li>annidamento senza significato;</li>
  <li>chiave non davvero unica;</li>
  <li>default che nasconde dato obbligatorio;</li>
  <li>struttura scelta per “moda” invece che per operazioni.</li>
</ul>

---

## 18. Activity candidate

<ul>
  <li><strong>A — Data model choice:</strong> scegli struttura e motiva;</li>
  <li><strong>B — Parallel lists refactor:</strong> passa a record raggruppati;</li>
  <li><strong>C — Group by:</strong> dict di liste/set;</li>
  <li><strong>D — Debug model:</strong> correggi struttura che rende innaturale il requisito;</li>
  <li><strong>E — Mini-project:</strong> piccolo dominio con almeno due strutture combinate e spiegazione del modello.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 19. Exit checkpoint PY2-08

<p align="justify">Dovresti saper:</p>

<ul>
  <li>usare set per unicità/membership;</li>
  <li>usare dict per lookup chiave→valore;</li>
  <li>gestire chiavi mancanti secondo contratto;</li>
  <li>costruire frequenze;</li>
  <li>iterare <code>items()</code>;</li>
  <li>scegliere str/list/tuple/set/dict;</li>
  <li>usare semplici strutture combinate;</li>
  <li>evitare liste parallele fragili;</li>
  <li>motivare il modello dati;</li>
  <li>collegare la scelta alle operazioni dominanti.</li>
</ul>

---

## 20. Sintesi

```text
operazioni dominanti
→ struttura candidata
→ codice più naturale
```

```text
sequenza → list/tuple
unicità → set
lookup → dict
```

<p align="justify">Nel prossimo blocco useremo queste strutture con la persistenza su file testo, mantenendo il modulo file volutamente piccolo per proteggere il tempo OOP.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 sulle built-in collections;</li>
  <li><em>Think Python / Pensare in Python</em> — lists/tuples/dictionaries;</li>
  <li><em>Fluent Python</em> — data model/collections come controllo teacher-side;</li>
  <li>audit <code>sources/FRIEDPYTHON_DICTS_AUDIT.md</code>.</li>
</ul>

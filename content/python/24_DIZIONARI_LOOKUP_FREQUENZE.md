# M24 — Dizionari: chiave→valore, lookup e frequenze

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il dizionario associa chiavi uniche a valori e sostiene lookup e conteggi di frequenza.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare cicli, membership e collezioni e distinguere unicità e posizione da M20–M23.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
creare un <code>dict</code>;<br>leggere/aggiornare/inserire un valore tramite chiave;<br>usare <code>in</code> per verificare una chiave; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Cercare per chiave è una richiesta diversa dall&#x27;accesso per posizione in una sequenza. Riprendi <a href="23_SET_UNICITA_MEMBERSHIP.md">M23 — Set: unicità, membership e operazioni insiemistiche</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md">M25 — Strutture combinate e scelta del modello dati</a>. La scelta del modello combina strutture semplici secondo identità, ordine, unicità e operazioni dominanti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia le frequenze di un testo breve, includendo la prima comparsa e una ripetizione dello stesso carattere.
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
  <li>creare un <code>dict</code>;</li>
  <li>leggere/aggiornare/inserire un valore tramite chiave;</li>
  <li>usare <code>in</code> per verificare una chiave;</li>
  <li>distinguere accesso obbligatorio <code>d[k]</code> da accesso opzionale/default con <code>get()</code>;</li>
  <li>capire <code>KeyError</code> a livello beginner;</li>
  <li>iterare su chiavi e su coppie chiave/valore con <code>items()</code>;</li>
  <li>conoscere <code>keys()</code>/<code>values()</code> come view senza materializzare liste inutilmente;</li>
  <li>usare un dizionario per contare frequenze;</li>
  <li>spiegare perché chiavi uniche e lookup sono il modello centrale;</li>
  <li>sapere che il <code>dict</code> moderno preserva l'ordine di inserimento, senza usarlo come sostituto di una struttura scelta per posizione.</li>
</ul>

---

## 1. Il modello non è posizione: è chiave→valore

<p align="justify">Lista:</p>

```python
voti = [8, 7, 9]
```

<p align="justify">Accesso naturale:</p>

```text
posizione → valore
```

<p align="justify">Dizionario:</p>

```python
voti = {
    "Anna": 8,
    "Luca": 7,
    "Marta": 9,
}
```

<p align="justify">Accesso naturale:</p>

```text
chiave → valore
```

---

## 2. Creazione e lookup

```python
voti = {"Anna": 8, "Luca": 7}
```

```python
voti["Anna"]
```

<p align="justify">restituisce <code>8</code>.</p>

<p align="justify">Non chiediamo:</p>

```text
qual è l'elemento in posizione 0?
```

<p align="justify">La chiave identifica il valore nel dominio.</p>

---

## 3. Inserire e aggiornare

```python
voti["Marta"] = 9
```

<p align="justify">crea una nuova associazione se la chiave non esiste.</p>

```python
voti["Anna"] = 10
```

<p align="justify">aggiorna il valore associato alla chiave esistente.</p>

---

## 4. Chiave mancante

```python
voti["Paolo"]
```

<p align="justify">se la chiave manca genera <code>KeyError</code>.</p>

<p align="justify">Questo può essere corretto se il contratto dice:</p>

<blockquote>
<p align="justify">questa chiave deve esistere.</p>
</blockquote>

<p align="justify">Non bisogna nascondere automaticamente ogni chiave mancante.</p>

---

## 5. Membership sulle chiavi

```python
if "Paolo" in voti:
    print(voti["Paolo"])
```

<p align="justify">Per un dict, <code>in</code> verifica le <strong>chiavi</strong>.</p>

<p align="justify">Questo rende esplicito il caso presenza/assenza.</p>

---

## 6. `get()`

```python
voto = voti.get("Paolo")
```

<p align="justify">se manca la chiave restituisce <code>None</code>.</p>

<p align="justify">Con default:</p>

```python
voto = voti.get("Paolo", 0)
```

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">la chiave è opzionale e ha davvero senso un valore di default?</p>
</blockquote>

<p align="justify">Se la chiave dovrebbe obbligatoriamente esistere, un default può nascondere un bug del modello.</p>

---

## 7. Iterare sulle chiavi

```python
for nome in voti:
    print(nome)
```

<p align="justify">itera sulle chiavi.</p>

<p align="justify">Se serve anche il valore:</p>

```python
for nome, voto in voti.items():
    print(nome, voto)
```

<p align="justify">È spesso più diretto di cercare il valore manualmente a ogni giro.</p>

---

## 8. `keys()`, `values()`, `items()`

<p align="justify">Nei Python moderni:</p>

```python
voti.keys()
voti.values()
voti.items()
```

<p align="justify">restituiscono <strong>view</strong> dinamiche del dizionario.</p>

<p align="justify">Non serve trasformarle in <code>list()</code> per una normale iterazione.</p>

<p align="justify">Materializzare una lista ha senso soltanto se il problema richiede davvero una lista indipendente/indicizzabile.</p>

---

## 9. Ordine del dict: nota moderna

<p align="justify">I <code>dict</code> Python moderni preservano l'ordine di inserimento.</p>

<p align="justify">Questo corregge vecchie dispense che descrivevano l'ordine come arbitrario.</p>

<p align="justify">Ma attenzione:</p>

<blockquote>
<p align="justify">preservare l'ordine non trasforma il dict in una lista indicizzata.</p>
</blockquote>

<p align="justify">Se la posizione è l'operazione dominante, una sequenza potrebbe essere un modello migliore.</p>

---

## 10. Pattern frequenze

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Conta quante volte compare ogni carattere in un testo.</p>
</blockquote>

```python
def frequenze(testo):
    conteggi = {}

    for carattere in testo:
        conteggi[carattere] = conteggi.get(carattere, 0) + 1

    return conteggi
```

<p align="justify">Invariante:</p>

<blockquote>
<p align="justify">per ogni chiave già incontrata, il valore è il numero di occorrenze viste finora.</p>
</blockquote>

---

## 11. Perché dict è un modello migliore della tabella ASCII 256

<p align="justify">Un vecchio esercizio legacy usava:</p>

```text
lista di 256 contatori
indice = ord(carattere)
```

<p align="justify">Problemi:</p>

<ul>
  <li>assume universo ASCII 0..255;</li>
  <li>alloca celle per caratteri mai visti;</li>
  <li>lega il modello a un codice numerico artificiale;</li>
  <li>Python <code>str</code> è Unicode.</li>
</ul>

<p align="justify">Con dict:</p>

```text
carattere realmente incontrato → conteggio
```

<p align="justify">Il modello coincide con la domanda.</p>

---

## 12. Unicode-friendly a livello beginner

```python
frequenze("caffè☕")
```

<p align="justify">usa direttamente i caratteri <code>str</code> come chiavi.</p>

<p align="justify">Non serve trasformarli in indici ASCII.</p>

<p align="justify">I dettagli Unicode avanzati restano fuori dal core.</p>

---

## 13. Worked example: inventario semplice

```python
quantita = {
    "penne": 10,
    "quaderni": 4,
}
```

<p align="justify">Aggiornamento:</p>

```python
quantita["penne"] += 3
```

<p align="justify">Lookup opzionale:</p>

```python
quantita.get("matite", 0)
```

<p align="justify">Qui il default 0 può avere senso se il contratto dice “prodotto assente = quantità zero”.</p>

---

## 14. Chiavi hashable

<p align="justify">Come per set, le chiavi devono essere hashable.</p>

<p align="justify">Comuni:</p>

```text
str
int
float
bool
tuple hashable
```

<p align="justify">Una lista mutabile non è una chiave valida.</p>

<p align="justify">Tuple <code>(riga, colonna)</code> potranno essere usate come enrichment per matrici sparse.</p>

---

## 15. Error Clinic

<ul>
  <li>accesso <code>[]</code> a chiave mancante non prevista;</li>
  <li><code>get(..., 0)</code> usato per nascondere una chiave obbligatoria;</li>
  <li><code>in d.values()</code> quando volevi cercare una chiave;</li>
  <li>conversione inutile <code>list(d.keys())</code> solo per iterare;</li>
  <li>dipendere da posizione numerica dentro il dict;</li>
  <li>chiave list non hashable;</li>
  <li>vecchia assunzione “dict sempre senza ordine”.</li>
</ul>

---

## 16. Activity candidate

<ul>
  <li><strong>A — Mapping microscope:</strong> prevedi dict dopo inserimenti/aggiornamenti;</li>
  <li><strong>B — Required or optional key?</strong> scegli <code>[]</code>, membership o <code>get</code> e motiva;</li>
  <li><strong>C — Frequenze:</strong> implementa conteggio caratteri/parole semplici;</li>
  <li><strong>D — Debug:</strong> KeyError, default che nasconde bug, chiave sbagliata, view/list inutile.</li>
</ul>

<p align="justify">Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.</p>

---

## 17. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>posizione→valore vs chiave→valore;</li>
  <li>inserimento vs aggiornamento;</li>
  <li>chiave mancante e <code>KeyError</code>;</li>
  <li><code>[]</code> vs <code>get</code>;</li>
  <li><code>for k in d</code> vs <code>d.items()</code>;</li>
  <li>view <code>keys/values/items</code>;</li>
  <li>frequenze con dict;</li>
  <li>perché dict è migliore della lista ASCII-256 per caratteri Unicode.</li>
</ol>

---

## 18. Sintesi

```text
dict → chiave unica → valore associato
```

```text
chiave obbligatoria → accesso diretto può essere corretto
chiave opzionale → membership/get secondo contratto
```

```text
frequenze → valore incontrato come chiave, conteggio come valore
```

<p align="justify">Nel prossimo modulo combineremo liste, tuple, set e dict in modelli dati più realistici e sceglieremo la struttura in base alle operazioni dominanti.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>dict</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — dictionaries;</li>
  <li><em>Learning Python / Imparare Python</em> — mapping types;</li>
  <li><em>Fluent Python</em> — controllo teacher-side su dict/hashability;</li>
  <li>audit <code>sources/FRIEDPYTHON_DICTS_AUDIT.md</code>.</li>
</ul>

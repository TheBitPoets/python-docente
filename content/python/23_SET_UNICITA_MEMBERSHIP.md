# M23 — Set: unicità, membership e operazioni insiemistiche

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-08 — Set, dizionari e modellazione dei dati  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- creare un `set` non vuoto;
- creare un set vuoto con `set()` e distinguere `{}`;
- spiegare che gli elementi sono unici;
- usare `add`, `remove`, `discard` consapevolmente;
- usare membership `in`/`not in`;
- usare unione, intersezione e differenza;
- deduplicare quando l'ordine non è requisito dominante;
- scegliere `set` vs `list` in base a unicità/membership/ordine;
- non dipendere dall'ordine di iterazione/stampa di un set;
- capire a livello beginner che gli elementi devono essere hashable.

---

# 1. Il set non è una lista senza duplicati

```python
tag = {"python", "git", "linux"}
```

Modello:

```text
set = collezione di valori distinti
```

Le domande naturali sono:

```text
questo valore appartiene all'insieme?
quali valori sono comuni?
quali valori sono presenti solo da una parte?
```

Non:

```text
qual è l'elemento in posizione 2?
```

Il set non è una sequenza indicizzata.

---

# 2. Set vuoto

Questo crea un **dict vuoto**:

```python
x = {}
```

Per un set vuoto:

```python
x = set()
```

È un Error Clinic obbligatorio.

---

# 3. Unicità

```python
nomi = ["anna", "luca", "anna", "marta"]
unici = set(nomi)
```

Semanticamente otteniamo i valori distinti.

Se l'ordine originale è requisito, convertire semplicemente in set può perdere informazione importante sul modello.

---

# 4. Membership

```python
"python" in tag
```

Quando la domanda dominante è membership ripetuta, il set è una struttura naturale.

Intuizione prestazionale:

```text
list → ricerca lungo la sequenza
set  → progettato per membership tramite hashing
```

Non introduciamo ancora Big-O formale né promesse assolute sul tempo.

---

# 5. `add()`

```python
tag.add("docker")
```

Se l'elemento è già presente, il set continua ad averne una sola copia.

Questa proprietà deriva dalla semantica del set, non da un controllo manuale sui duplicati.

---

# 6. `remove()` vs `discard()`

```python
insieme.remove(x)
```

se `x` manca, segnala un errore.

```python
insieme.discard(x)
```

se `x` manca, non genera errore.

La scelta dipende dal contratto:

- assenza inattesa → `remove` può evidenziare un problema;
- “assicura che x non ci sia” → `discard` può essere naturale.

---

# 7. Unione

```python
A | B
```

oppure:

```python
A.union(B)
```

Domanda:

> quali elementi appartengono ad almeno uno dei due insiemi?

---

# 8. Intersezione

```python
A & B
```

Domanda:

> quali elementi appartengono a entrambi?

Esempio naturale: studenti iscritti a due attività.

---

# 9. Differenza

```python
A - B
```

Domanda:

> quali elementi sono in A ma non in B?

L'ordine degli operandi conta.

---

# 10. Worked example: corsi frequentati

```python
python = {"Anna", "Luca", "Marta"}
git = {"Luca", "Paolo", "Marta"}
```

Possiamo chiedere:

```python
entrambi = python & git
almeno_uno = python | git
solo_python = python - git
```

Prima di eseguire, prevedi semanticamente i gruppi.

---

# 11. Set vs list

| Esigenza | `list` | `set` |
|---|---|---|
| ordine/posizione | naturale | non è il criterio del set |
| duplicati significativi | sì | no |
| mutazione sequenziale | sì | sì, con semantica insiemistica |
| membership dominante | possibile | naturale |
| indice/slicing | sì | no |
| unione/intersezione | manuale | naturale |

---

# 12. Hashability beginner

Per appartenere a un set, un elemento deve poter essere usato come valore hashable/stabile.

Candidati comuni:

```text
str
int
float
bool
tuple di elementi hashable
```

Non puoi inserire direttamente una `list` mutabile come elemento di un set.

Gli internals dell'hash table arrivano più avanti.

---

# 13. Non dipendere dall'ordine

Non scrivere un algoritmo che assume:

```text
"il primo elemento stampato dal set sarà..."
```

Se l'ordine è requisito del problema, scegli una struttura/strategia che lo rappresenti esplicitamente.

---

# 14. Error Clinic

- `{}` usato come set vuoto;
- aspettarsi duplicati;
- usare indice/slice su set;
- affidarsi all'ordine di iterazione;
- `remove` su elemento assente quando il contratto voleva idempotenza;
- lista mutabile usata come elemento;
- set scelto quando l'ordine di prima occorrenza era parte del requisito.

---

# 15. Activity candidate

- **A — Set microscope:** prevedi contenuto semantico dopo add/duplicati;
- **B — List or set?** scegli e motiva;
- **C — Implement:** unione/intersezione/differenza tra gruppi/tag;
- **D — Debug:** `{}`, ordine, duplicati, remove/discard, elemento non hashable.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 16. Checkpoint

Sai spiegare:

1. perché `{}` non è set vuoto;
2. unicità;
3. membership come operazione dominante;
4. `remove` vs `discard`;
5. unione/intersezione/differenza;
6. list vs set;
7. perché non usare indici/ordine come proprietà del set.

---

# 17. Sintesi

```text
set → valori unici + membership + operazioni insiemistiche
```

```text
ordine importante? → chiediti se set è davvero il modello giusto
```

Nel prossimo modulo passeremo da “appartiene?” a una domanda diversa:

```text
chiave → quale valore associato?
```

cioè il modello del dizionario.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `set`/`frozenset` (solo `set` core);
- *Fluent Python* come controllo teacher-side su hashing/collections;
- *Learning Python / Imparare Python* — set coverage;
- Pluralsight come gap-check.

`friedpython` non dispone di un blocco set centrale equivalente; M23 è quindi originale.

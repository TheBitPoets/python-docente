# M24 — Dizionari: chiave→valore, lookup e frequenze

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-08 — Set, dizionari e modellazione dei dati  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- creare un `dict`;
- leggere/aggiornare/inserire un valore tramite chiave;
- usare `in` per verificare una chiave;
- distinguere accesso obbligatorio `d[k]` da accesso opzionale/default con `get()`;
- capire `KeyError` a livello beginner;
- iterare su chiavi e su coppie chiave/valore con `items()`;
- conoscere `keys()`/`values()` come view senza materializzare liste inutilmente;
- usare un dizionario per contare frequenze;
- spiegare perché chiavi uniche e lookup sono il modello centrale;
- sapere che il `dict` moderno preserva l'ordine di inserimento, senza usarlo come sostituto di una struttura scelta per posizione.

---

# 1. Il modello non è posizione: è chiave→valore

Lista:

```python
voti = [8, 7, 9]
```

Accesso naturale:

```text
posizione → valore
```

Dizionario:

```python
voti = {
    "Anna": 8,
    "Luca": 7,
    "Marta": 9,
}
```

Accesso naturale:

```text
chiave → valore
```

---

# 2. Creazione e lookup

```python
voti = {"Anna": 8, "Luca": 7}
```

```python
voti["Anna"]
```

restituisce `8`.

Non chiediamo:

```text
qual è l'elemento in posizione 0?
```

La chiave identifica il valore nel dominio.

---

# 3. Inserire e aggiornare

```python
voti["Marta"] = 9
```

crea una nuova associazione se la chiave non esiste.

```python
voti["Anna"] = 10
```

aggiorna il valore associato alla chiave esistente.

---

# 4. Chiave mancante

```python
voti["Paolo"]
```

se la chiave manca genera `KeyError`.

Questo può essere corretto se il contratto dice:

> questa chiave deve esistere.

Non bisogna nascondere automaticamente ogni chiave mancante.

---

# 5. Membership sulle chiavi

```python
if "Paolo" in voti:
    print(voti["Paolo"])
```

Per un dict, `in` verifica le **chiavi**.

Questo rende esplicito il caso presenza/assenza.

---

# 6. `get()`

```python
voto = voti.get("Paolo")
```

se manca la chiave restituisce `None`.

Con default:

```python
voto = voti.get("Paolo", 0)
```

La domanda è:

> la chiave è opzionale e ha davvero senso un valore di default?

Se la chiave dovrebbe obbligatoriamente esistere, un default può nascondere un bug del modello.

---

# 7. Iterare sulle chiavi

```python
for nome in voti:
    print(nome)
```

itera sulle chiavi.

Se serve anche il valore:

```python
for nome, voto in voti.items():
    print(nome, voto)
```

È spesso più diretto di cercare il valore manualmente a ogni giro.

---

# 8. `keys()`, `values()`, `items()`

Nei Python moderni:

```python
voti.keys()
voti.values()
voti.items()
```

restituiscono **view** dinamiche del dizionario.

Non serve trasformarle in `list()` per una normale iterazione.

Materializzare una lista ha senso soltanto se il problema richiede davvero una lista indipendente/indicizzabile.

---

# 9. Ordine del dict: nota moderna

I `dict` Python moderni preservano l'ordine di inserimento.

Questo corregge vecchie dispense che descrivevano l'ordine come arbitrario.

Ma attenzione:

> preservare l'ordine non trasforma il dict in una lista indicizzata.

Se la posizione è l'operazione dominante, una sequenza potrebbe essere un modello migliore.

---

# 10. Pattern frequenze

Problema:

> Conta quante volte compare ogni carattere in un testo.

```python
def frequenze(testo):
    conteggi = {}

    for carattere in testo:
        conteggi[carattere] = conteggi.get(carattere, 0) + 1

    return conteggi
```

Invariante:

> per ogni chiave già incontrata, il valore è il numero di occorrenze viste finora.

---

# 11. Perché dict è un modello migliore della tabella ASCII 256

Un vecchio esercizio legacy usava:

```text
lista di 256 contatori
indice = ord(carattere)
```

Problemi:

- assume universo ASCII 0..255;
- alloca celle per caratteri mai visti;
- lega il modello a un codice numerico artificiale;
- Python `str` è Unicode.

Con dict:

```text
carattere realmente incontrato → conteggio
```

Il modello coincide con la domanda.

---

# 12. Unicode-friendly a livello beginner

```python
frequenze("caffè☕")
```

usa direttamente i caratteri `str` come chiavi.

Non serve trasformarli in indici ASCII.

I dettagli Unicode avanzati restano fuori dal core.

---

# 13. Worked example: inventario semplice

```python
quantita = {
    "penne": 10,
    "quaderni": 4,
}
```

Aggiornamento:

```python
quantita["penne"] += 3
```

Lookup opzionale:

```python
quantita.get("matite", 0)
```

Qui il default 0 può avere senso se il contratto dice “prodotto assente = quantità zero”.

---

# 14. Chiavi hashable

Come per set, le chiavi devono essere hashable.

Comuni:

```text
str
int
float
bool
tuple hashable
```

Una lista mutabile non è una chiave valida.

Tuple `(riga, colonna)` potranno essere usate come enrichment per matrici sparse.

---

# 15. Error Clinic

- accesso `[]` a chiave mancante non prevista;
- `get(..., 0)` usato per nascondere una chiave obbligatoria;
- `in d.values()` quando volevi cercare una chiave;
- conversione inutile `list(d.keys())` solo per iterare;
- dipendere da posizione numerica dentro il dict;
- chiave list non hashable;
- vecchia assunzione “dict sempre senza ordine”.

---

# 16. Activity candidate

- **A — Mapping microscope:** prevedi dict dopo inserimenti/aggiornamenti;
- **B — Required or optional key?** scegli `[]`, membership o `get` e motiva;
- **C — Frequenze:** implementa conteggio caratteri/parole semplici;
- **D — Debug:** KeyError, default che nasconde bug, chiave sbagliata, view/list inutile.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 17. Checkpoint

Sai spiegare:

1. posizione→valore vs chiave→valore;
2. inserimento vs aggiornamento;
3. chiave mancante e `KeyError`;
4. `[]` vs `get`;
5. `for k in d` vs `d.items()`;
6. view `keys/values/items`;
7. frequenze con dict;
8. perché dict è migliore della lista ASCII-256 per caratteri Unicode.

---

# 18. Sintesi

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

Nel prossimo modulo combineremo liste, tuple, set e dict in modelli dati più realistici e sceglieremo la struttura in base alle operazioni dominanti.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `dict`;
- *Think Python / Pensare in Python* — dictionaries;
- *Learning Python / Imparare Python* — mapping types;
- *Fluent Python* — controllo teacher-side su dict/hashability;
- audit `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

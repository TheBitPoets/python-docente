---
marp: true
paginate: true
size: 16:9
title: M24 — Dizionari, lookup e frequenze
---

# M24 — Dizionari: chiave → valore, lookup e frequenze

PY2-08 — Set, dizionari e modellazione dei dati

---

# Nuovo modello

```text
list → posizione → valore
dict → chiave → valore
```

```python
voti = {"Anna": 8, "Luca": 7}
```

---

# Lookup

```python
voti["Anna"]
```

La chiave identifica il dato nel dominio.

---

# Inserire / aggiornare

```python
voti["Marta"] = 9
voti["Anna"] = 10
```

Stessa sintassi, chiave nuova o esistente.

---

# Chiave mancante

```python
voti["Paolo"]
```

può generare `KeyError`.

A volte è giusto: la chiave doveva esistere.

---

# Membership

```python
if "Paolo" in voti:
    ...
```

`in` su un dict controlla le chiavi.

---

# `get()`

```python
voti.get("Paolo")
voti.get("Paolo", 0)
```

Default soltanto se ha senso nel contratto.

---

# Iterare

Solo chiavi:

```python
for nome in voti:
    ...
```

Chiave + valore:

```python
for nome, voto in voti.items():
    ...
```

---

# View moderne

```python
d.keys()
d.values()
d.items()
```

Sono view dinamiche, non serve `list(...)` solo per iterare.

---

# Ordine moderno

I dict preservano l'ordine di inserimento.

Ma:

> dict non diventa una sequenza indicizzata.

La scelta struttura resta guidata dal dominio.

---

# Frequenze

```python
conteggi = {}
for carattere in testo:
    conteggi[carattere] = conteggi.get(carattere, 0) + 1
```

```text
carattere → numero di occorrenze
```

---

# Vecchio modello ASCII-256

```text
lista[ord(carattere)] += 1
```

Problemi:

- universo ASCII artificiale;
- celle inutili;
- Python str è Unicode.

---

# Dict Unicode-friendly

```python
frequenze("caffè☕")
```

Usa direttamente i caratteri incontrati come chiavi.

---

# Chiave obbligatoria o opzionale?

```text
obbligatoria → [] può evidenziare un bug se manca
opzionale    → membership/get secondo contratto
```

Non usare `get` per nascondere ogni errore.

---

# Error Clinic

- KeyError inatteso;
- default 0 che nasconde chiave obbligatoria;
- membership sui values per errore;
- list(keys()) inutile;
- chiave mutabile;
- vecchia assunzione sull'ordine.

---

# Checkpoint

Sai:

- chiave→valore;
- [] vs get;
- membership;
- items();
- view;
- frequenze;
- dict vs ASCII-table.

---

# Recap

```text
dict → lookup per chiave
```

Prossimo: strutture combinate e scelta del modello dati.

---
marp: true
paginate: true
size: 16:9
title: M24 — Dizionari, lookup e frequenze
---

# M24 — Dizionari: chiave → valore, lookup e frequenze
## Quando il dominio identifica i dati con una chiave

PY2-08 — Set, dizionari e modellazione dei dati

---

# Che cosa deve restare davvero?

```text
dict = chiave → valore
lookup / inserimento / aggiornamento
KeyError
in controlla le chiavi
[] vs get secondo contratto
items()
frequenze + invariante
```

Views, ordine moderno e hashability sono guided exposure.

---

# Nuovo modello

```text
list → posizione → valore
set  → appartenenza
 dict → chiave → valore
```

```python
voti = {"Anna": 8, "Luca": 7}
```

La chiave rappresenta qualcosa del dominio.

---

# Lookup

```python
voti["Anna"]
```

La domanda è:

> dato questo identificatore, quale valore è associato?

---

# Inserire / aggiornare

```python
voti["Marta"] = 9
voti["Anna"] = 10
```

Stessa sintassi:

- chiave nuova → inserimento;
- chiave esistente → aggiornamento.

---

# Chiave mancante

```python
voti["Paolo"]
```

può generare `KeyError`.

A volte è corretto che l'errore emerga:

> la chiave doveva esistere.

---

# Membership

```python
if "Paolo" in voti:
    ...
```

`in` su un dict controlla le **chiavi**.

---

# `[]` o `get()`?

```python
voti["Paolo"]
```

se la chiave è obbligatoria.

```python
voti.get("Paolo", 0)
```

se la chiave è davvero opzionale e `0` ha senso come default.

Prima il contratto, poi l'API.

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

`items()` è core quando servono entrambe le parti del mapping.

---

# Frequenze = M11 per chiave

```python
conteggi = {}
for carattere in testo:
    conteggi[carattere] = conteggi.get(carattere, 0) + 1
```

Non imparare la riga come formula.

Invariante:

> per ogni chiave già incontrata, il valore è il numero di occorrenze viste finora.

---

# Perché dict è naturale qui?

Vecchio modello:

```text
lista[ord(carattere)] += 1
```

Dict:

```text
carattere realmente incontrato → conteggio
```

La chiave coincide con il dato che vogliamo ricordare.

---

# GUIDED EXPOSURE — view moderne

```python
d.keys()
d.values()
d.items()
```

sono view dinamiche nei Python moderni.

Non serve trasformarle in lista soltanto per iterare.

Questo è un dettaglio di accuratezza, non il centro del mastery.

---

# GUIDED EXPOSURE — ordine moderno

I dict moderni preservano l'ordine di inserimento.

Ma:

> preservare l'ordine non trasforma il dict in una lista indicizzata.

La sua semantica primaria resta il mapping.

---

# GUIDED EXPOSURE — chiavi hashable

Le chiavi devono essere compatibili col modello di hashing.

Comuni:

```text
str, int, float, bool, tuple hashable
```

Una lista mutabile non è una chiave valida.

Niente internals hash table in M24.

---

# Error Clinic

- KeyError inatteso;
- `get(..., 0)` che nasconde una chiave obbligatoria;
- `in d` interpretato come ricerca nei valori;
- dict usato con indici artificiali;
- formula frequenze copiata senza capire l'invariante;
- chiave mutabile.

---

# Minimum mastery checkpoint

Sai:

1. spiegare chiave→valore?;
2. creare/aggiornare un dict?;
3. usare membership sulle chiavi?;
4. scegliere `[]` o `get()` e motivarlo?;
5. usare `items()`?;
6. costruire una frequenza semplice?;
7. spiegare che cosa significa il conteggio associato a ogni chiave?.

Views, ordine moderno e hashability non devono dominare il gate.

---

# Recap

```text
dict → lookup per chiave
```

```text
frequenze → stato progressivo per chiave
```

Prossimo: scegliere e combinare strutture dati.

---
marp: true
paginate: true
size: 16:9
title: M23 — Set, unicità e membership
---

# M23 — Set: unicità, membership e operazioni insiemistiche

PY2-08 — Set, dizionari e modellazione dei dati

---

# Non è una lista senza duplicati

```python
tag = {"python", "git", "linux"}
```

Domande naturali:

```text
appartiene?
comuni?
solo da una parte?
```

---

# Set vuoto

```python
{}      # dict vuoto
set()   # set vuoto
```

---

# Unicità

```python
set(["anna", "luca", "anna"])
```

Rappresenta valori distinti.

Se l'ordine originale serve, attenzione al modello.

---

# Membership

```python
"python" in tag
```

Set è progettato per membership tramite hashing.

Niente Big-O formale per ora.

---

# `add()`

```python
tag.add("docker")
```

Aggiungere un duplicato non crea una seconda copia.

---

# `remove` vs `discard`

```python
s.remove(x)   # assenza → errore
s.discard(x)  # assenza → nessun errore
```

Dipende dal contratto.

---

# Unione

```python
A | B
```

Elementi presenti in almeno uno dei due set.

---

# Intersezione

```python
A & B
```

Elementi comuni.

---

# Differenza

```python
A - B
```

Elementi in A ma non in B.

L'ordine degli operandi conta.

---

# Set vs list

```text
ordine/posizione → list
unicità/membership → set candidato
```

La scelta segue il dominio.

---

# Hashability beginner

Elementi comuni ammessi:

```text
str, int, float, bool, tuple hashable
```

Una `list` mutabile non può essere elemento di un set.

---

# Non dipendere dall'ordine

Un algoritmo non deve assumere:

> il primo elemento iterato del set sarà X.

Se l'ordine serve, modellalo esplicitamente.

---

# Error Clinic

- `{}` come set;
- indice/slice;
- duplicati attesi;
- ordine atteso;
- remove/discard scelti male;
- lista come elemento.

---

# Checkpoint

Sai spiegare:

- unicità;
- membership;
- list vs set;
- remove vs discard;
- unione/intersezione/differenza;
- niente indice/ordine come proprietà del set.

---

# Recap

```text
set → unicità + membership + insiemi
```

Prossimo: `dict`, chiave → valore.

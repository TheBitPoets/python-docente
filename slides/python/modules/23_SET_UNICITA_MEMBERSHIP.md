---
marp: true
paginate: true
size: 16:9
title: M23 — Set, unicità e membership
---

# M23 — Set: unicità, membership e operazioni insiemistiche
## Un modello per valori distinti e appartenenza

PY2-08 — Set, dizionari e modellazione dei dati

---

# Che cosa deve restare davvero?

```text
set = valori distinti
set() vs {}
membership
add
unione / intersezione / differenza
list vs set
niente indice/posizione come modello
```

`remove/discard` e hashability sono guided exposure.

---

# Non è una lista senza duplicati

```python
tag = {"python", "git", "linux"}
```

Domande naturali:

```text
appartiene?
quali valori sono comuni?
quali sono solo da una parte?
```

Non:

```text
qual è il valore in posizione 2?
```

---

# Set vuoto

```python
{}      # dict vuoto
set()   # set vuoto
```

Questo contrasto è core.

---

# Unicità

```python
set(["anna", "luca", "anna"])
```

Rappresenta valori distinti.

Ma chiediti:

> l'ordine o i duplicati originali erano informazione importante?

Se sì, il set può essere il modello sbagliato.

---

# Membership

```python
"python" in tag
```

La domanda dominante è:

> questo valore appartiene all'insieme?

Niente Big-O formale per ora.

---

# `add()` — core

```python
tag.add("docker")
```

Aggiungere un valore già presente non crea una seconda copia.

---

# Unione

```python
A | B
```

Valori presenti in almeno uno dei due set.

---

# Intersezione

```python
A & B
```

Valori comuni.

---

# Differenza

```python
A - B
```

Valori in `A` ma non in `B`.

L'ordine degli operandi conta.

---

# Set vs list

```text
ordine/posizione/duplicati significativi → list candidata
unicità/membership/insiemi              → set candidato
```

La scelta segue il dominio.

---

# Non dipendere dall'ordine

Non costruire un algoritmo che richiede:

> il primo elemento del set sarà X.

Se la posizione/ordine è requisito, modellalo esplicitamente con una struttura adatta.

---

# GUIDED EXPOSURE — `remove` vs `discard`

```python
s.remove(x)   # assenza → errore
s.discard(x)  # assenza → nessun errore
```

Dipende dal contratto.

Devi poter leggere la differenza; non è il centro del checkpoint.

---

# GUIDED EXPOSURE — hashability

Alcuni valori comuni utilizzabili come elementi:

```text
str, int, float, bool, tuple hashable
```

Una `list` mutabile non può essere elemento del set.

Per ora basta il vincolo osservabile: niente internals delle hash table.

---

# Error Clinic

- `{}` usato come set;
- indice/slice su set;
- duplicati attesi;
- ordine atteso;
- conversione a set che perde un requisito;
- lista mutabile come elemento.

---

# Minimum mastery checkpoint

Sai:

1. creare set vuoto/non vuoto?;
2. spiegare unicità e membership?;
3. usare `add()`?;
4. interpretare unione/intersezione/differenza?;
5. scegliere list vs set e motivarlo?;
6. spiegare perché indice/slicing non appartengono al modello set?.

`remove/discard`, hashability avanzata e symmetric difference non devono dominare il gate.

---

# Recap

```text
set → valori distinti + appartenenza + operazioni insiemistiche
```

Prossimo: `dict`, chiave → valore.

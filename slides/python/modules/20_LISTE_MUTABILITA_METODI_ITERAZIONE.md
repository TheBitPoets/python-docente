---
marp: true
paginate: true
size: 16:9
title: M20 — Liste, mutabilità e metodi
---

# M20 — Liste: mutabilità, metodi e iterazione

PY2-07 — Liste, tuple e dati tabellari

---

# Stringa vs lista

```text
str  → sequenza immutabile
list → sequenza mutabile
```

```python
numeri = [10, 20, 30]
numeri[0] = 99
```

---

# Accesso riutilizza ciò che sappiamo

```python
len(numeri)
numeri[0]
numeri[-1]
numeri[1:3]
```

Indici e slicing non sono nuovi.
La mutabilità sì.

---

# `append()`

```python
numeri.append(30)
```

Aggiunge **un elemento** in coda.

---

# Bug fondamentale

```python
numeri = numeri.append(30)
```

`append()` modifica la lista e restituisce `None`.

---

# `append` vs `extend`

```python
[1, 2].append([3, 4])
```

concetto:

```text
aggiungo un elemento-lista
```

```python
x.extend([3, 4])
```

concetto:

```text
aggiungo più elementi
```

---

# `remove` vs `pop`

```python
valori.remove(7)  # valore
valori.pop(2)     # posizione + return
```

Valore ≠ indice.

---

# Iterazione diretta

```python
for numero in numeri:
    ...
```

Se ti serve soltanto il valore.

---

# Quando serve l'indice

```python
for i in range(len(numeri)):
    ...
```

Solo se la posizione fa parte del problema.

---

# `enumerate()`

```python
for i, numero in enumerate(numeri):
    ...
```

Indice + valore, senza gestire manualmente il contatore.

---

# Costruire una lista

```python
valori = []
for _ in range(n):
    valori.append(int(input()))
```

Ora i dati restano disponibili per elaborazioni successive.

---

# Error Clinic

- `lista = lista.append(x)`;
- append vs extend;
- remove vs pop;
- indice fuori range;
- indice usato senza motivo.

---

# Friedpython: confronto utile

Due esercizi legacy mostrano:

```text
while + indice
vs
for diretto
```

Noi chiediamo anche:

> quale forma comunica meglio l'intenzione?

---

# Checkpoint

Sai spiegare:

- mutabilità;
- append/extend;
- remove/pop;
- metodi mutanti e `None`;
- for diretto/indice/enumerate.

---

# Recap

```text
list = sequenza ordinata mutabile
```

Prossimo: alias, copie e mutazioni condivise.

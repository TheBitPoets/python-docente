---
marp: true
paginate: true
size: 16:9
title: M21 — Alias, copie, filtri e ordinamento
---

# M21 — Alias, copie, filtri e ordinamento

PY2-07 — Liste, tuple e dati tabellari

---

# Due nomi, un oggetto

```python
a = [10, 20]
b = a
b.append(30)
```

```text
a ─┐
   ├──> [10, 20, 30]
b ─┘
```

---

# Alias

```text
b = a
```

non crea una nuova lista.

Una mutazione è visibile tramite entrambi i nomi.

---

# Copia superficiale

```python
b = a.copy()
```

oppure:

```python
b = a[:]
```

Nuovo contenitore esterno.

---

# Strutture annidate

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
```

Gli oggetti interni possono restare condivisi.

---

# Testa anche la mutazione

```python
originale = [3, -1, 5]
risultato = solo_positivi(originale)

assert risultato == [3, 5]
assert originale == [3, -1, 5]
```

---

# Modificare mentre iteri

Rischioso:

```python
for valore in numeri:
    if valore < 0:
        numeri.remove(valore)
```

La struttura cambia mentre il `for` la percorre.

---

# Strategia chiara: nuova lista

```python
positivi = []
for valore in numeri:
    if valore >= 0:
        positivi.append(valore)
```

---

# Filtrare / trasformare

```text
input list
→ loop
→ condizione/trasformazione
→ nuova list
```

Riusa tutto il primo quadrimestre.

---

# Comprehension solo dopo

```python
positivi = [x for x in numeri if x > 0]
```

È confronto/enrichment, non prerequisito core.

---

# `sort()` vs `sorted()`

```python
numeri.sort()
```

muta e restituisce `None`.

```python
ordinati = sorted(numeri)
```

crea una nuova lista.

---

# Bug già noto

```python
numeri = numeri.sort()
```

stesso errore concettuale di:

```python
numeri = numeri.append(3)
```

---

# Friedpython: massimo

Lo spunto legacy è utile, ma va riscritto:

```text
max = ...   ❌ oscura max()
massimo = ... ✅
```

---

# Lista inversa: confronta effetti

- costruzione manuale;
- `list(reversed(x))`;
- `x[::-1]`;
- `x.reverse()`.

Domanda: nuovo oggetto o mutazione?

---

# Checkpoint

Sai spiegare:

- alias vs copy;
- shallow copy;
- mutazione durante iterazione;
- sort vs sorted;
- contratto di mutazione/non-mutazione.

---

# Recap

```text
alias → stesso oggetto
copy → nuovo contenitore
```

Prossimo: tuple e matrici.

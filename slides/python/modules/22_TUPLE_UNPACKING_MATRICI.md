---
marp: true
paginate: true
size: 16:9
title: M22 — Tuple, unpacking e matrici
---

# M22 — Tuple, unpacking e matrici

PY2-07 — Liste, tuple e dati tabellari

---

# Tuple

```python
punto = (3, 5)
```

Sequenza ordinata, ma contenitore immutabile.

---

# Tupla a un elemento

```python
x = (40)   # int
y = (40,)  # tuple
```

La virgola è fondamentale.

---

# Packing / unpacking

```python
punto = (3, 5)
x, y = punto
```

Dai nomi significativi ai ruoli.

---

# List o tuple?

```text
collezione che cresce/cambia → list
raggruppamento stabile       → tuple candidata
```

Esempio:

```text
voti → list
coordinata (x,y) → tuple
```

---

# `enumerate()` riletto

```python
for indice, valore in enumerate(valori):
    ...
```

La coppia viene unpacked.

---

# Immutabilità con oggetti annidati

```python
t = (1, [2, 3], 4)
```

La tupla non permette di riassegnare `t[1]`, ma la lista interna resta mutabile.

Enrichment, non prerequisito.

---

# Lista di liste

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
```

```python
matrice[1][2]  # 6
```

---

# Attraversamento

```python
for riga in matrice:
    for valore in riga:
        ...
```

M12 torna su dati reali.

---

# Quando servono coordinate

```python
for r in range(len(matrice)):
    for c in range(len(matrice[r])):
        print(r, c, matrice[r][c])
```

---

# Somma per riga

```text
ciclo esterno → cambia riga
ciclo interno → accumula valori della riga
```

Reset dell'accumulatore: una volta per riga.

---

# Alias trap

```python
matrice = [[0] * colonne] * righe
```

Le righe interne possono essere lo stesso oggetto condiviso.

---

# Costruzione esplicita

```python
matrice = []
for _ in range(righe):
    matrice.append([0] * colonne)
```

Ogni giro crea una nuova riga.

---

# Righe irregolari

```python
dati = [[1, 2], [3, 4, 5]]
```

Non ogni lista di liste è rettangolare.

Usa il contratto reale dei dati.

---

# Error Clinic

- `(5)` pensato come tuple;
- unpacking incompatibile;
- riga/colonna invertite;
- `[[0] * C] * R`;
- struttura annidata senza motivo.

---

# Exit checkpoint

Sai:

- tuple e unpacking;
- list vs tuple;
- lista di liste;
- `[riga][colonna]`;
- cicli annidati su dati;
- aliasing delle righe.

---

# Recap

```text
list  → mutabile
 tuple → contenitore immutabile
```

```text
matrice → lista di righe
```

Prossimo: Checkpoint B, poi set e dizionari.

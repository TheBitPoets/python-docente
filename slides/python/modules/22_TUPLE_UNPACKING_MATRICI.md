---
marp: true
paginate: true
size: 16:9
title: M22 — Tuple, unpacking e matrici
---

# M22 — Tuple, unpacking e dati tabellari
## Scegliere una struttura e riusare ciò che sappiamo

PY2-07 — Liste, tuple e dati tabellari

---

# Che cosa deve restare davvero?

```text
tuple = sequenza ordinata immutabile
unpacking
list vs tuple dal significato
lista di liste
[riga][colonna]
R × C sui dati reali
reset al livello giusto
righe condivise / alias
```

Dettagli su packing, tuple annidate mutabili e righe irregolari sono guided/enrichment.

---

# Tuple

```python
punto = (3, 5)
```

Sequenza ordinata, ma contenitore immutabile.

Puoi leggere:

```python
punto[0]
punto[1]
```

ma non riassegnare un elemento della tupla.

---

# List o tuple?

```text
collezione che cresce/cambia → list
raggruppamento stabile       → tuple candidata
```

Esempi:

```text
voti → list
coordinata (x, y) → tuple
```

La scelta viene dal modello dei dati, non dall'idea di “struttura più avanzata”.

---

# Unpacking — core

```python
punto = (3, 5)
x, y = punto
```

Ora:

```text
x → 3
y → 5
```

L'unpacking assegna nomi ai ruoli dei valori.

---

# GUIDED EXPOSURE — tupla a un elemento

```python
x = (40)   # int
y = (40,)  # tuple
```

La virgola è ciò che crea la tupla a un elemento.

È un dettaglio utile da riconoscere, non il centro della verifica.

---

# GUIDED EXPOSURE — packing

```python
punto = 3, 5
```

è possibile.

Nel corso beginner preferiamo spesso:

```python
punto = (3, 5)
```

quando rende il raggruppamento più leggibile.

---

# Lista di liste

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
```

Una “matrice” beginner è semplicemente una lista che contiene righe-lista.

---

# Accesso

```python
matrice[0]       # prima riga
matrice[1][2]    # 6
```

Leggi:

```text
matrice[riga][colonna]
```

---

# Attraversamento per valore

```python
for riga in matrice:
    for valore in riga:
        ...
```

Se ti servono solo i valori, evita indici inutili.

---

# Quando servono coordinate

```python
for r in range(len(matrice)):
    for c in range(len(matrice[r])):
        print(r, c, matrice[r][c])
```

M12 ritorna su dati reali:

```text
riga × colonna
```

---

# Somma per riga

```text
ciclo esterno → cambia riga
ciclo interno → visita valori della riga
```

L'accumulatore della riga deve essere azzerato:

```text
una volta per riga
```

M11 e M12 ritornano insieme.

---

# Alias trap — core

```python
matrice = [[0] * colonne] * righe
```

Le “righe” possono essere lo stesso oggetto interno ripetuto.

Poi:

```python
matrice[0][0] = 1
```

può modificare la prima cella di più righe.

Non è un trucco nuovo: è M21 che ritorna.

---

# Costruzione esplicita

```python
matrice = []
for _ in range(righe):
    matrice.append([0] * colonne)
```

Ogni iterazione crea una nuova riga.

Questa forma rende visibile il motivo per cui le righe sono indipendenti.

---

# GUIDED EXPOSURE — righe irregolari

```python
dati = [[1, 2], [3, 4, 5]]
```

Non ogni lista di liste è rettangolare.

Quando usi indici, il limite corretto può dipendere dalla riga:

```python
len(dati[r])
```

Mostralo solo dopo che il modello rettangolare è stabile.

---

# ENRICHMENT / BACKUP — tuple con oggetti mutabili

```python
t = (1, [2, 3], 4)
```

Il contenitore tuple è immutabile, ma la lista interna resta un oggetto mutabile.

Questa precisione è utile, ma non è prerequisito per scegliere list vs tuple in seconda.

---

# Error Clinic

- `(5)` pensato come tuple;
- unpacking incompatibile;
- riga/colonna invertite;
- `[[0] * C] * R` con righe condivise;
- reset dell'accumulatore al livello errato;
- struttura annidata senza motivo.

---

# Minimum mastery checkpoint

Sai:

1. spiegare tuple vs list?;
2. fare unpacking di una coppia?;
3. scegliere list/tuple da una specifica?;
4. accedere a `[riga][colonna]`?;
5. attraversare una lista di liste?;
6. riusare `R×C` e il reset per riga?;
7. spiegare il bug `[[0] * C] * R`?;
8. costruire righe indipendenti?.

Tuple con oggetti mutabili, packing senza parentesi e righe irregolari non devono dominare il gate.

---

# Recap

```text
list  → sequenza mutabile
 tuple → sequenza stabile/immutabile come contenitore
```

```text
matrice beginner → lista di righe
```

```text
aliasing non sparisce nelle strutture annidate
```

Prossimo: Checkpoint B, poi set e dizionari.

---
marp: true
paginate: true
size: 16:9
title: M10 — for, range e scelta del ciclo
---

# M10 — `for`, `range` e scelta del ciclo
## Quando sappiamo già quali valori attraversare

PY2-04 — Iterazione e pattern algoritmici

---

# Problema iniziale

> Stampa i valori da 0 a 4.

Con `while`:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Corretto, ma gestiamo manualmente il contatore.

---

# Lo stesso con `for`

```python
for i in range(5):
    print(i)
```

Leggi:

> per ogni valore `i` prodotto da `range(5)`.

---

# `range(5)`

```text
0, 1, 2, 3, 4
```

Regola fondamentale:

> lo stop è escluso.

---

# `range(start, stop)`

```python
range(2, 6)
```

```text
2, 3, 4, 5
```

```text
start incluso
stop escluso
step = +1
```

---

# `range(start, stop, step)`

```python
range(2, 10, 2)
```

```text
2, 4, 6, 8
```

Lo step dice come cambia il valore.

---

# Countdown

```python
range(5, 0, -1)
```

```text
5, 4, 3, 2, 1
```

Per scendere serve uno step negativo.

---

# Range vuoto

```python
range(5, 0)
```

con step `+1` non produce valori.

Il corpo del `for` viene eseguito zero volte.

---

# Off-by-one

Obiettivo:

```text
1, 2, 3, 4, 5
```

Bug:

```python
range(1, 5)
```

Manca `5` perché lo stop è escluso.

---

# Trace

```python
for i in range(2, 5):
    print(i * 10)
```

| i | output |
|---:|---:|
| 2 | 20 |
| 3 | 30 |
| 4 | 40 |

---

# `for` vs `while`

```text
for   → so quali valori/iterazioni attraversare
while → continuo finché una condizione dinamica resta vera
```

La scelta comunica il modello del problema.

---

# Microscope: scegli

1. stampa 1..10;
2. chiedi voto finché valido;
3. ripeti 8 volte;
4. leggi fino a sentinella;
5. countdown 10..1.

Prima scegli e **motiva**, poi scrivi il codice.

---

# Stato ridondante

Sospetto:

```python
contatore = 0
for i in range(5):
    print(contatore)
    contatore += 1
```

Se duplica `i`, lo stato in più non aggiunge significato.

---

# `break`

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

Interrompe il ciclo corrente.

Usalo quando rende chiaro che l'obiettivo è già raggiunto.

---

# `continue`

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Salta il resto del corpo e passa all'iterazione successiva.

Non usarlo per evitare condizioni leggibili.

---

# Bug: step nel verso sbagliato

```python
for i in range(5, 0, 1):
    print(i)
```

Range vuoto.

Start > stop + desiderio di scendere → step negativo.

---

# Refactoring `while` → `for`

```python
i = 0
while i < 100:
    elabora(i)
    i += 1
```

vs

```python
for i in range(100):
    elabora(i)
```

Meno stato manuale quando il percorso è già noto.

---

# Romeo opzionale

Riferimento pinned:

```text
romeo-y1-u15-ciclo-for
```

Esempio: ripetere quattro lati/azioni di una missione.

Prima il modello generale, poi il simulatore certificato.

---

# Activity planning

- A — prevedi `range`;
- B — `for` o `while`?;
- C — countdown/ripetizione N volte;
- D — debug off-by-one/step/range vuoto.

M04 resta il canarino P1.

---

# Checkpoint

1. Valori di `range(5)`?
2. Perché stop è escluso?
3. `range(2, 8, 2)`?
4. Perché `range(5, 0)` è vuoto?
5. Quando scegli `for`?
6. Quando scegli `while`?
7. Che fanno `break` e `continue`?

---

# Recap

```text
for → iterazioni/valori noti
range → start incluso, stop escluso
while → condizione dinamica
```

Prossimo: **contatori, accumulatori, ricerca e flag**.

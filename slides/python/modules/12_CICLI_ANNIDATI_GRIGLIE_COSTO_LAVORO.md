---
marp: true
paginate: true
size: 16:9
title: M12 — Cicli annidati, griglie e costo del lavoro
---

# M12 — Cicli annidati, griglie e costo del lavoro
## Per ogni riga, tutte le colonne

PY2-04 — Iterazione e pattern algoritmici

---

# Modello base

```python
for riga in range(R):
    for colonna in range(C):
        ...
```

Per ogni valore esterno, il ciclo interno completa il proprio percorso.

---

# Trace delle coppie

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

Prevedi tutte le coppie prima di eseguire.

---

# Quante iterazioni?

```text
R righe × C colonne
```

significa:

```text
R × C esecuzioni del corpo interno
```

Esempio:

```text
2 × 3 = 6
```

---

# Griglia rettangolare

```python
for _ in range(righe):
    for _ in range(colonne):
        print("*", end="")
    print()
```

Esterno = riga.
Interno = colonne della riga.

---

# Reset al livello giusto

Una variabile “totale della riga” deve essere azzerata:

```text
una volta per riga
```

non:

- una volta per cella;
- una sola volta per tutta la griglia.

---

# `if` dentro due cicli

```python
for riga in range(n):
    for colonna in range(n):
        if riga == colonna:
            print("#", end="")
        else:
            print(".", end="")
    print()
```

La decisione dipende dalla coppia corrente.

---

# Tutte le coppie servono davvero?

Doppio ciclo naturale:

```text
tutte le celle di una griglia
```

Domanda critica:

> il problema richiede davvero tutte le coppie?

Se no, possiamo star ripetendo lavoro inutile.

---

# Lavoro ripetuto inutile

Se un calcolo non dipende dall'iterazione:

```python
for i in range(n):
    valore = calcolo_invariabile()
```

valuta se è più corretto/chiaro calcolarlo una sola volta fuori.

---

# Primo confronto di lavoro

| N | ciclo singolo | doppio ciclo N×N |
|---:|---:|---:|
| 3 | 3 | 9 |
| 10 | 10 | 100 |
| 100 | 100 | 10000 |

Niente Big-O formale per ora.

Ma chiediamo:

> quanto lavoro sto facendo e perché?

---

# Ordine dei criteri

```text
1. correttezza
2. comprensibilità
3. struttura adatta
4. evitare lavoro chiaramente inutile
5. efficienza quando rilevante
```

Non:

```text
più corto = più veloce
```

---

# Worked example

Tabella 3×4:

```python
for riga in range(1, 4):
    for colonna in range(1, 5):
        print(riga * colonna, end=" ")
    print()
```

Previsione:

```text
3 righe
4 colonne
12 prodotti
```

---

# Error Clinic

Cerca il problema:

- `riga` usata al posto di `colonna`;
- accumulatore resettato troppo dentro;
- reset troppo esterno;
- `print()` indentato al livello sbagliato;
- calcolo invariabile ripetuto nel ciclo interno.

---

# Nested trace

```python
for i in range(2):
    for j in range(2):
        print(i + j)
```

| i | j | i+j |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 2 |

---

# Activity candidate

- A: nested trace;
- B: cambia dimensione e prevedi iterazioni;
- C: griglia con pattern condizionale;
- D: debug reset/indice/indentazione;
- E: mini-project con selezione + ciclo + stima lavoro.

Nessuna nuova Activity autogradata finché il profilo non è certificato.

---

# Exit checkpoint PY2-04

Sai:

- scegliere `for`/`while`;
- garantire terminazione;
- usare sentinelle;
- contare/accumulare;
- cercare/min-max;
- combinare `if` e loop;
- leggere doppi cicli;
- stimare esecuzioni semplici;
- riconoscere lavoro ripetuto inutile.

---

# Recap

```text
R × C = celle/coppie visitate
```

```text
correttezza
→ leggibilità
→ struttura
→ niente lavoro inutile
→ efficienza quando serve
```

Prossimo blocco: funzioni, decomposizione e testing.

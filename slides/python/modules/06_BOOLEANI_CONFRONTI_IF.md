---
marp: true
paginate: true
size: 16:9
title: M06 — Booleani, confronti e prima selezione con if
---

# M06 — Booleani, confronti e `if`
## Da una domanda vero/falso a un ramo del programma

PY2-03 — Selezione e logica

---

# Problema iniziale

> Spedizione gratuita se il totale è **almeno 50**.

```text
totale >= 50 ?
    sì → 0
    no → 5
```

La parola importante è **almeno**.

---

# Un confronto produce `bool`

Prevedi:

```python
7 > 3
7 < 3
7 == 7
```

Risultato:

```text
True oppure False
```

---

# Operatori di confronto

```text
==  uguale valore
!=  diverso
<   minore
<=  minore o uguale
>   maggiore
>=  maggiore o uguale
```

Traduci prima la frase, poi scegli il simbolo.

---

# Parole di soglia

```text
più di 10       → > 10
almeno 10       → >= 10
meno di 10      → < 10
al massimo 10   → <= 10
esattamente 10  → == 10
```

---

# `=` non è `==`

```python
eta = 15
```

assegna.

```python
eta == 15
```

confronta e produce `True`/`False`.

---

# Primo `if`

```python
temperatura = int(input())

if temperatura < 0:
    print("gelo")
```

Se la condizione è `False`, il ramo viene saltato.

Non è un errore.

---

# Indentazione = struttura

```python
if temperatura < 0:
    print("gelo")
print("fine")
```

`fine` viene stampato sempre.

Perché?

---

# Trace: input 4

```python
numero = int(input())
if numero > 0:
    print("positivo")
print("fine")
```

Con `4`:

```text
numero > 0 → True
ramo if    → eseguito
fine       → eseguito
```

---

# Trace: input -2

Con `-2`:

```text
numero > 0 → False
ramo if    → saltato
fine       → eseguito
```

Segui il valore concreto della condizione.

---

# Quando serve `else`

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

I due casi sono complementari.

Un solo ramo viene eseguito.

---

# Il confine è un test obbligatorio

Soglia: 18

| età | atteso |
|---:|---|
| 17 | minorenne |
| 18 | maggiorenne |
| 19 | maggiorenne |

`18` distingue `>` da `>=`.

---

# Worked example: spedizione

```python
totale = int(input())

if totale >= 50:
    spedizione = 0
else:
    spedizione = 5

print(spedizione)
```

Test: `49`, `50`, `51`, `0`.

---

# Decisione vs presentazione

Confronta:

```python
if totale >= 50:
    print(0)
else:
    print(5)
```

con:

```python
if totale >= 50:
    spedizione = 0
else:
    spedizione = 5
print(spedizione)
```

Quale rende più chiaro il risultato finale?

---

# Microscope: True o False?

Prevedi:

```python
5 > 2
5 < 2
5 == 5
5 != 5
10 >= 10
9 >= 10
0 <= 0
```

Poi verifica.

---

# Error Clinic — confine

Specifica:

> consentito da 18 anni compresi

Bug:

```python
if eta > 18:
```

Qual è il test minimo che lo scopre?

---

# Error Clinic — domanda invertita

Specifica:

> stampa negativo se `numero < 0`

Bug:

```python
if numero > 0:
    print("negativo")
```

Sintassi valida, logica sbagliata.

---

# Error Clinic — assegnamento

Bug:

```python
if voto = 6:
```

Per confrontare:

```python
if voto == 6:
```

---

# `is` non sostituisce `==`

Nel core beginner:

```text
uguaglianza di valore → ==
```

`is` riguarda l'identità degli oggetti e verrà contestualizzato più avanti.

---

# Dal flow chart al Python

```text
        eta >= 18 ?
       /           \
     sì             no
     |              |
maggiorenne      minorenne
```

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

Stessa decisione, notazione diversa.

---

# Romeo: applicazione opzionale

Missione pinned:

```text
romeo-y1-u14-condizioni
```

Idea:

```text
modalità sicura?
→ velocità ridotta
→ comportamento osservabile nel simulatore
```

Prima impariamo `if` con problemi generali.

---

# Activity planning

- A — Predict/Trace
- B — cambia una soglia
- C — flow chart → `if/else`
- D — debug confini/condizione/indentazione

M04 resta il canarino P1 finché `python-docente#7` non è certificato.

---

# Checkpoint

1. `7 >= 7` produce quale tipo?
2. `=` vs `==`?
3. Perché `>= 18` include 18?
4. Che succede a un `if` falso senza `else`?
5. Perché l'indentazione conta?
6. Come testi una soglia 50?
7. Perché non usiamo `is` per l'uguaglianza normale?

---

# Recap

```text
confronto → bool
```

```text
True  → ramo if
False → ramo else / continuazione
```

```text
soglia → sotto / sulla / sopra
```

```text
indentazione → blocco
```

Prossimo: **`elif`, casi esclusivi e logica composta**.

---
marp: true
paginate: true
size: 16:9
title: M09 — while, stato, sentinelle e validazione ripetuta
---

# M09 — `while`, stato, sentinelle e validazione
## Ripetere finché una condizione cambia

PY2-04 — Iterazione e pattern algoritmici

---

# Dal problema precedente

M08 sapeva rilevare:

```text
voto fuori 0..10 → dato non valido
```

Ora vogliamo:

> chiedere di nuovo finché il voto diventa valido.

---

# Modello del `while`

```text
stato iniziale
→ condizione?
→ corpo
→ aggiornamento
→ nuovo controllo
```

Se la condizione è subito falsa, il corpo viene eseguito zero volte.

---

# Primo ciclo

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

Output:

```text
0
1
2
```

---

# Quattro parti

```text
inizializzazione → i = 0
condizione       → i < 3
corpo            → print(i)
aggiornamento    → i += 1
```

Domanda obbligatoria:

> quale valore può rendere falsa la condizione?

---

# Trace

| controllo | i | condizione | output | i dopo |
|---:|---:|---|---:|---:|
| 1 | 0 | True | 0 | 1 |
| 2 | 1 | True | 1 | 2 |
| 3 | 2 | True | 2 | 3 |
| 4 | 3 | False | — | — |

---

# Perché termina?

```text
i parte da 0
→ aumenta di 1
→ prima o poi i < 3 diventa False
```

Ogni `while` deve avere una **storia di terminazione**.

---

# Ciclo infinito

```python
i = 0
while i < 3:
    print(i)
```

`i` non cambia: la condizione resta vera.

Il programma non contiene un meccanismo di uscita.

---

# Zero / una / più iterazioni

Quando il problema lo consente, progetta casi che esercitano:

```text
zero iterazioni
una iterazione
più iterazioni
```

Il confine conta anche nei cicli.

---

# Validazione ripetuta

```python
voto = int(input())
while voto < 0 or voto > 10:
    voto = int(input())
print(voto)
```

Il nuovo input è l'aggiornamento dello stato.

---

# Trace validazione

Input:

```text
12
-1
7
```

```text
12 → invalido → rileggi
-1 → invalido → rileggi
 7 → valido   → fine
```

---

# Continuazione vs uscita

```python
while voto < 0 or voto > 10:
```

significa:

> continua mentre il voto è invalido.

Il ciclo termina quando:

```text
0 <= voto <= 10
```

---

# Sentinella

```python
numero = int(input())
while numero != -1:
    print(numero)
    numero = int(input())
```

`-1` segnala la fine e non viene elaborato.

---

# Sentinella e dominio

Prima chiedi:

> la sentinella può essere un dato normale?

Se sì, il significato sarebbe ambiguo.

---

# Bug: aggiornamento solo in un ramo

```python
while numero != -1:
    if numero > 0:
        print(numero)
        numero = int(input())
```

Con `numero = 0` non avviene una nuova lettura: il ciclo non progredisce.

---

# Bug: condizione invertita

Vogliamo ripetere mentre il voto è **invalido**.

Bug:

```python
while 0 <= voto <= 10:
```

Questa ripete quando è valido.

---

# Off-by-one

Obiettivo: stampare `0 1 2`.

Bug:

```python
i = 0
while i <= 3:
    print(i)
    i += 1
```

Produce anche `3`.

---

# `while True` + `break`

È possibile:

```python
while True:
    voto = int(input())
    if 0 <= voto <= 10:
        break
```

Ma non è la forma introduttiva primaria.

> Devi comunque spiegare dove e perché termina.

---

# Romeo opzionale

Riferimento pinned:

```text
romeo-y1-u16-ciclo-while
```

Uso: rendere visibili stato, ripetizione e terminazione nel simulatore.

Solo con `romeo-sim` certificato; hardware non core.

---

# Activity planning

- A — trace iterazione/stato;
- B — modifica limiti validazione;
- C — input finché valido;
- D — debug ciclo infinito/off-by-one/sentinella.

M04 resta il canarino P1.

---

# Checkpoint

1. Quali sono le quattro parti del ciclo?
2. Perché il ciclo può terminare?
3. Che significa zero iterazioni?
4. Qual è l'aggiornamento nella validazione?
5. Che cos'è una sentinella?
6. Perché un aggiornamento in un solo ramo è rischioso?
7. Quando può avere senso `while True` + `break`?

---

# Recap

```text
while → condizione dinamica
stato → cambia → ricontrollo
terminazione → deve essere spiegabile
```

Prossimo: **`for`, `range` e scelta `for` vs `while`**.

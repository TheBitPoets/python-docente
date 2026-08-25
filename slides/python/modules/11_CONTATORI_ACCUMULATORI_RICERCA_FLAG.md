---
marp: true
paginate: true
size: 16:9
title: M11 — Contatori, accumulatori, ricerca e flag
---

# M11 — Contatori, accumulatori, ricerca e flag
## Che cosa deve ricordare il ciclo?

PY2-04 — Iterazione e pattern algoritmici

---

# Un ciclo attraversa. Lo stato ricorda.

Possibili domande sui dati:

- quanti?
- quanto in totale?
- minimo/massimo?
- esiste almeno un match?
- qual è il primo match?

Il pattern dipende da **che cosa deve sopravvivere tra le iterazioni**.

---

# Pattern contatore

```python
conteggio = 0
for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1
```

Invariante:

> `conteggio` = numero di positivi già elaborati.

---

# Trace del contatore

Valori:

```text
4, -2, 7
```

| valore | positivo? | conteggio |
|---:|---|---:|
| 4 | True | 1 |
| -2 | False | 1 |
| 7 | True | 2 |

Se l'incremento fosse fuori dall'`if`, cosa cambierebbe?

---

# Pattern accumulatore

```python
totale = 0
for _ in range(n):
    valore = int(input())
    totale += valore
```

Invariante:

> `totale` = somma dei valori già elaborati.

---

# Bug: reset dentro il ciclo

```python
for _ in range(n):
    totale = 0
    totale += int(input())
```

Domanda:

> dopo ogni iterazione, `totale` contiene davvero la somma di tutto ciò che ho già visto?

No: viene azzerato.

---

# Contatore + accumulatore

Per la media dei soli valori validi:

```python
totale = 0
conteggio = 0

for _ in range(n):
    valore = int(input())
    if valore >= 0:
        totale += valore
        conteggio += 1
```

Prima della divisione:

> `conteggio` può essere zero?

---

# Minimo progressivo

Evita:

```python
minimo = 999999
```

se il dominio non garantisce quel limite.

Meglio, se esiste almeno un dato:

```python
minimo = int(input())
for _ in range(n - 1):
    valore = int(input())
    if valore < minimo:
        minimo = valore
```

---

# Invariante del minimo

> `minimo` = il più piccolo valore visto finora.

Per il massimo:

> `massimo` = il più grande valore visto finora.

Queste frasi sono strumenti di debug.

---

# Ricerca

Domande diverse:

```text
esiste almeno un match?
qual è il primo match?
quanti match ci sono?
quali sono tutti i match?
```

Non sono lo stesso problema.

---

# Flag booleano

```python
trovato = False
```

Invariante:

> `trovato` indica se finora è comparso almeno un match.

Un flag è utile quando rappresenta davvero uno stato significativo.

---

# Flag ridondante?

Chiediti:

> questa variabile aggiunge significato o soltanto meccanica?

A volte un `break` rende la ricerca del primo match più chiara.

A volte il flag serve dopo il ciclo.

Dipende dal contratto.

---

# `if` dentro `for`

```python
conteggio = 0
for _ in range(n):
    valore = int(input())
    if 10 <= valore <= 20:
        conteggio += 1
```

La selezione decide **se aggiornare lo stato**.

---

# Ciclo dentro una decisione

```python
if n > 0:
    for _ in range(n):
        ...
else:
    print("nessun dato")
```

Non collezioniamo forme sintattiche.

La struttura deve rappresentare il problema.

---

# Worked example

Specifica:

> Leggi N interi. Stampa quanti sono positivi e la loro somma.

```python
conteggio = 0
totale = 0

for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1
        totale += valore
```

---

# Error Clinic

Cerca il problema:

- accumulatore azzerato dentro il ciclo;
- contatore incrementato fuori dal ramo;
- media con denominatore zero;
- minimo con sentinella arbitraria;
- flag dichiarato ma mai aggiornato.

---

# Lavoro della ricerca

Ricerca lineare:

```text
più dati
→ più confronti
```

Per ora niente Big-O formale.

Ma distinguiamo:

- primo match;
- tutti i match;
- conteggio dei match.

---

# Checkpoint

Sai spiegare:

1. contatore vs accumulatore?
2. perché l'accumulatore nasce prima del ciclo?
3. perché `999999` è fragile?
4. che cosa significa “minimo visto finora”?
5. primo match vs tutti i match?
6. quando un flag è utile?
7. quale test protegge una media?

---

# Recap

```text
contatore    → quanti?
accumulatore → totale
min/max      → estremo visto finora
flag         → stato sì/no
ricerca      → primo / esiste / tutti
```

Domanda guida:

> quale frase deve restare vera dopo ogni iterazione?

Prossimo modulo: cicli annidati, griglie e costo del lavoro.

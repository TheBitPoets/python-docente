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

# Un'unica famiglia, non cinque ricette

Il ciclo attraversa i dati.

Lo **stato** ricorda ciò che deve sopravvivere tra le iterazioni.

Domanda guida:

> Che cosa deve significare questa variabile dopo aver elaborato i dati visti finora?

---

# Possibili domande

```text
quanti?
quanto in totale?
qual è l'estremo visto finora?
esiste almeno un match?
qual è il primo match?
```

Prima scegli il significato dello stato.

Poi scegli inizializzazione e aggiornamento.

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

Se l'incremento fosse fuori dall'`if`, quale frase smetterebbe di essere vera?

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

La media è un'applicazione dei due stati, non un nuovo pattern.

---

# Minimo progressivo

Evita:

```python
minimo = 999999
```

se il dominio non garantisce quel limite.

Se esiste almeno un dato:

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

Per il massimo cambia il confronto, non il modello:

> `massimo` = il più grande valore visto finora.

Non imparare due ricette separate.

---

# Prima la domanda di ricerca

```text
esiste almeno un match?
qual è il primo match?
quanti match ci sono?
```

Queste richieste possono richiedere stati e comportamenti diversi.

---

# Flag booleano

```python
trovato = False
```

Invariante:

> `trovato` indica se finora è comparso almeno un match.

Un flag è utile quando questo stato serve davvero.

---

# Flag ridondante?

Chiediti:

> questa variabile aggiunge significato o soltanto meccanica?

Un flag può servire dopo il ciclo.

Per il primo match, in alcuni problemi può essere possibile fermarsi prima.

Dipende dal contratto.

---

# `if` decide se aggiornare lo stato

```python
conteggio = 0
for _ in range(n):
    valore = int(input())
    if 10 <= valore <= 20:
        conteggio += 1
```

La selezione non è decorazione:

> decide quali dati modificano lo stato.

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

Due stati, due significati diversi.

---

# Error Clinic

Cerca quale significato dello stato viene rotto:

- accumulatore azzerato dentro il ciclo;
- contatore incrementato fuori dal ramo;
- media con denominatore zero;
- minimo con sentinella arbitraria;
- flag dichiarato ma mai aggiornato.

---

# GUIDED EXPOSURE — primo match e `break`

Se il contratto permette di fermarsi appena troviamo ciò che serve, `break` può interrompere la scansione.

Ma non è sempre equivalente:

- forse dobbiamo consumare tutti gli input;
- forse dobbiamo contare tutti i match.

Prima viene la specifica, poi la scelta del flusso.

---

# ENRICHMENT / BACKUP — quantità di lavoro

Ricerca lineare:

```text
più dati
→ più confronti
```

Possiamo distinguere intuitivamente:

- primo match presto;
- primo match tardi;
- nessun match.

Niente Big-O formale in M11.

---

# Minimum mastery checkpoint

Sai:

1. scegliere quale stato serve alla specifica?;
2. distinguere contatore e accumulatore?;
3. spiegare perché lo stato nasce prima/al livello giusto?;
4. formulare una frase-invariante?;
5. inizializzare min/max senza sentinella arbitraria?;
6. distinguere esistenza, primo match e conteggio?;
7. usare un flag semplice?;
8. proteggere una media dal conteggio zero?.

---

# Recap

```text
ciclo → attraversa
stato → ricorda
```

```text
contatore    → quanti?
accumulatore → totale
min/max      → estremo visto finora
flag         → stato sì/no
ricerca      → quale domanda sto facendo?
```

Domanda finale:

> quale frase deve restare vera dopo ogni iterazione?

Prossimo modulo: cicli annidati, griglie e costo del lavoro.

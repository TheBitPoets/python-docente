---
marp: true
paginate: true
size: 16:9
title: M07 — elif, casi esclusivi e condizioni composte
---

# M07 — `elif`, casi esclusivi e logica composta
## Un solo risultato oppure più effetti?

PY2-03 — Selezione e logica

---

# Che cosa deve restare davvero?

## MUST MASTER

```text
primo ramo vero
elif vs if indipendenti
and / or / not
intervalli
confini
rami irraggiungibili
```

Short-circuit è materiale **enrichment**, non requisito del checkpoint ordinario.

---

# Problema iniziale

Classifica un voto:

```text
< 6      → insufficiente
6..7     → buono
>= 8     → ottimo
```

Per un voto vogliamo **una sola classificazione**.

---

# Catena `if / elif / else`

```python
if voto < 6:
    print("insufficiente")
elif voto < 8:
    print("buono")
else:
    print("ottimo")
```

Si esegue il **primo ramo vero**.

---

# Trace: voto 7

```text
voto < 6 → False
voto < 8 → True
ramo 2   → eseguito
else     → saltato
```

Dopo il primo ramo vero la catena è conclusa.

---

# Perché basta `voto < 8`?

Se siamo arrivati all'`elif`, sappiamo già:

```text
voto < 6 → False
```

Quindi il voto è già almeno 6.

Il ramo precedente crea un contesto logico.

---

# Problema diverso: due effetti

```text
se piove → ombrello
se fa freddo → giacca
```

Entrambe possono essere vere.

```python
if piove:
    print("ombrello")
if fa_freddo:
    print("giacca")
```

---

# Domanda guida

> Quanti rami/effetti possono essere eseguiti nella stessa esecuzione?

```text
uno solo → if / elif / else
più di uno → if indipendenti
```

Dipende dalla specifica, non dalla forma che preferiamo.

---

# `and`

> età almeno 18 **e** biglietto valido

```python
eta >= 18 and biglietto_valido
```

| A | B | A and B |
|---|---|---|
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | V |

---

# `or`

> gratis se età < 6 **oppure** età >= 65

```python
eta < 6 or eta >= 65
```

`or` è vero se almeno una parte è vera.

Non significa “esattamente una”.

---

# `not`

```python
not account_attivo
```

inverte il valore booleano.

Ma preferisci:

```python
eta >= 18
```

rispetto a:

```python
not eta < 18
```

se comunica meglio la soglia.

---

# Intervalli

Forma esplicita:

```python
x >= 0 and x <= 10
```

Dopo averla capita:

```python
0 <= x <= 10
```

Stesso intervallo, forma più naturale in Python.

---

# Worked example: tariffa

```python
if eta < 6:
    tariffa = 0
elif eta < 18:
    tariffa = 5
else:
    tariffa = 10
```

Test:

```text
5, 6, 17, 18, 70
```

I confini 6 e 18 sono obbligatori.

---

# Error Clinic — ordine soglie

```python
if voto >= 6:
    print("sufficiente")
elif voto >= 8:
    print("ottimo")
```

Con `9`, il primo ramo è già vero.

Il secondo è irraggiungibile.

---

# Error Clinic — due `if`

```python
if voto >= 6:
    print("sufficiente")
if voto >= 8:
    print("ottimo")
```

Con `9` ottieni due classificazioni.

Se ne volevi una sola, la struttura non rappresenta il problema.

---

# Error Clinic — `elif` improprio

```python
if piove:
    print("ombrello")
elif fa_freddo:
    print("giacca")
```

Se entrambe sono vere, ottieni un solo effetto.

La specifica ne richiedeva due.

---

# Error Clinic — `and` vs `or`

Gratis se:

```text
eta < 6 oppure eta >= 65
```

Bug:

```python
eta < 6 and eta >= 65
```

Può mai essere vero?

---

# Mixed retrieval

Per ogni specifica scegli prima la struttura e poi un test che distingue una soluzione corretta da una errata:

1. voto → una fascia;
2. piove → ombrello, freddo → giacca;
3. accesso se età >= 18 **e** biglietto valido;
4. valore dentro `[0, 10]`.

Non partire dal codice: parti dalla relazione fra i casi.

---

# ENRICHMENT / BACKUP — short-circuit

```python
if divisore != 0 and numero / divisore > 2:
    print("ok")
```

Se la prima parte è falsa, Python non ha bisogno della seconda.

Questa slide è **facoltativa** in M07.

Usala solo se `elif`, `if` indipendenti, `and/or/not` e confini sono già stabili.

---

# Romeo: applicazione selettiva

Possibile variante simulata:

```text
parametri missione
→ condizioni multiple
→ comportamento deterministico
```

Ma `elif`, `and`, `or` devono essere compresi prima con problemi generali.

Nessuna nuova Activity Romeo duplicata qui.

---

# Activity planning

- A — trova il primo ramo vero;
- B — `if` indipendenti o `elif`?;
- C — classificatore multi-fascia;
- D — debug soglie/rami/logica.

M04 resta il canarino P1.

---

# Minimum mastery checkpoint

1. Che significa “primo ramo vero”?
2. Quando usi più `if` indipendenti?
3. Quando `A and B` è vero?
4. Quando `A or B` è vero?
5. Che cosa fa `not`?
6. Che intervallo rappresenta `0 <= x <= 10`?
7. Quale input rende evidente un ramo irraggiungibile?

Short-circuit non fa parte del checkpoint ordinario.

---

# Recap

```text
if/elif/else → un'alternativa
```

```text
if indipendenti → effetti che possono coesistere
```

```text
and / or / not → comporre domande vero/falso
```

Prossimo: **annidamento, validazione e refactoring**.

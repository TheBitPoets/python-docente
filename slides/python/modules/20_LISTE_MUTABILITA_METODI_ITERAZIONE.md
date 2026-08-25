---
marp: true
paginate: true
size: 16:9
title: M20 — Liste, mutabilità e metodi
---

# M20 — Liste: mutabilità, metodi e iterazione
## Prima il modello mutabile, poi le API

PY2-07 — Liste, tuple e dati tabellari

---

# Che cosa deve restare davvero?

```text
str immutabile vs list mutabile
modifica per indice
append
metodo mutante → cambia oggetto / spesso None
for diretto
indice solo se serve
costruire una lista da N valori
membership
```

Non devi memorizzare tutti i metodi di modifica.

---

# Stringa vs lista

```text
str  → sequenza immutabile
list → sequenza mutabile
```

```python
numeri = [10, 20, 30]
numeri[0] = 99
```

La mutabilità è il nuovo concetto.

---

# Accesso riutilizza ciò che sappiamo

```python
len(numeri)
numeri[0]
numeri[-1]
numeri[1:3]
```

Indici e slicing non sono nuovi.

La domanda nuova è:

> questa operazione modifica la lista oppure produce un nuovo valore?

---

# `append()` — core

```python
numeri.append(30)
```

Aggiunge **un elemento** in coda e modifica la lista esistente.

È il metodo principale per costruire progressivamente una lista in M20.

---

# Bug fondamentale

```python
numeri = numeri.append(30)
```

`append()` modifica la lista e restituisce `None`.

Quindi dopo l'assegnamento:

```text
numeri → None
```

---

# Iterazione diretta

```python
for numero in numeri:
    ...
```

Se ti serve soltanto il valore.

È la forma naturale per molte scansioni.

---

# Quando serve l'indice

```python
for i in range(len(numeri)):
    ...
```

Usalo quando la posizione fa parte del problema.

Non usare l'indice come rituale.

---

# Costruire una lista

```python
valori = []
for _ in range(n):
    valori.append(int(input()))
```

Ora i dati restano disponibili per elaborazioni successive.

Questo è il vero salto rispetto alla scansione “leggi-elabora-dimentica”.

---

# Membership

```python
7 in numeri
```

Riusa il modello già visto sulle stringhe:

> questo valore compare nella sequenza?

---

# GUIDED EXPOSURE — `append` vs `extend`

```python
x = [1, 2]
x.append([3, 4])
```

aggiunge **un elemento-lista**.

```python
x = [1, 2]
x.extend([3, 4])
```

aggiunge **più elementi**.

Devi saper leggere la differenza; non è necessario usare `extend` in ogni esercizio.

---

# GUIDED EXPOSURE — `remove` vs `pop`

```python
valori.remove(7)  # valore
valori.pop(2)     # posizione + return
```

Valore ≠ indice.

Sono strumenti utili, ma non il centro del modulo.

---

# GUIDED EXPOSURE — `enumerate()`

```python
for i, numero in enumerate(numeri):
    ...
```

Indice + valore quando servono entrambi.

Se basta il valore, il `for` diretto resta più semplice.

---

# ENRICHMENT / BACKUP — `insert()`

`insert()` ha senso quando la posizione di inserimento è davvero parte del requisito.

Non usarlo soltanto perché esiste nella lista dei metodi.

---

# Error Clinic

- `lista = lista.append(x)`;
- indice fuori range;
- indice usato senza motivo;
- confusione valore/posizione;
- scegliere un metodo perché appena imparato invece che per il requisito.

---

# Friedpython: confronto utile

Due esercizi legacy mostrano:

```text
while + indice
vs
for diretto
```

Noi chiediamo:

> quale forma comunica meglio l'intenzione?

---

# Minimum mastery checkpoint

Sai:

1. spiegare `str` immutabile vs `list` mutabile?;
2. prevedere una modifica per indice?;
3. costruire una lista con `append`?;
4. spiegare il bug `lista = lista.append(x)`?;
5. attraversare una lista con `for` diretto?;
6. scegliere quando serve l'indice?;
7. usare membership?;
8. raccogliere N valori in una lista?.

`extend`, `remove`, `pop`, `enumerate`, `insert` non devono essere tutti ricordati a memoria per superare il gate.

---

# Recap

```text
list = sequenza ordinata mutabile
```

```text
metodo mutante
→ cambia l'oggetto
→ spesso restituisce None
```

Prossimo: alias, copie e mutazioni condivise.

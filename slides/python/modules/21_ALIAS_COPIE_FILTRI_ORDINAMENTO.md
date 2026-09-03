---
marp: true
paginate: true
size: 16:9
title: M21 — Alias, copie, filtri e ordinamento
---

# M21 — Alias, copie, filtri e ordinamento
## Stesso oggetto o nuova lista?

PY2-07 — Liste, tuple e dati tabellari

---

# Che cosa deve restare davvero?

```text
b = a → stesso oggetto
copy/slice → nuova lista esterna
mutazione → chi la vede?
non rimuovere ingenuamente durante iterazione
filtra costruendo una nuova lista
sort() vs sorted()
testa anche la mutazione
```

La shallow copy annidata è guided exposure, non requisito principale.

---

# Due nomi, un oggetto

```python
a = [10, 20]
b = a
b.append(30)
```

```text
a ─┐
   ├──> [10, 20, 30]
b ─┘
```

`b = a` non crea una nuova lista.

---

# Alias

Una mutazione osservata tramite un nome è visibile anche tramite gli altri nomi che indicano la stessa lista.

Domanda:

> sto creando un nuovo oggetto o solo un nuovo nome?

---

# Copia esterna

```python
b = a.copy()
```

oppure:

```python
b = a[:]
```

Per una lista piatta di valori semplici, una successiva mutazione strutturale di `b` non modifica `a`.

---

# Testa anche la mutazione

```python
originale = [3, -1, 5]
risultato = solo_positivi(originale)

assert risultato == [3, 5]
assert originale == [3, -1, 5]
```

Il secondo test verifica una parte importante del contratto:

> l'input deve restare invariato.

---

# Modificare mentre iteri

Rischioso:

```python
for valore in numeri:
    if valore < 0:
        numeri.remove(valore)
```

La struttura cambia mentre il `for` la percorre e alcuni elementi possono essere saltati.

---

# Strategia chiara: nuova lista

```python
positivi = []
for valore in numeri:
    if valore >= 0:
        positivi.append(valore)
```

```text
input
→ scansione
→ condizione
→ nuovo risultato
```

---

# Trasformare

```python
risultato = []
for valore in numeri:
    risultato.append(valore * 2)
```

La stessa struttura mentale vale per filtri e trasformazioni.

---

# `sort()` vs `sorted()`

```python
numeri.sort()
```

- modifica `numeri`;
- restituisce `None`.

```python
ordinati = sorted(numeri)
```

- produce una nuova lista;
- lascia l'input invariato.

---

# Bug già noto

```python
numeri = numeri.sort()
```

È lo stesso errore concettuale di:

```python
numeri = numeri.append(3)
```

Metodo mutante + assegnamento del suo `None`.

---

# GUIDED EXPOSURE — shallow copy annidata

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
```

Le liste esterne sono diverse, ma gli oggetti interni possono essere condivisi.

Per il core basta ricordare:

> `.copy()` crea un nuovo contenitore esterno; non promette una clonazione ricorsiva di tutto.

Non serve formalizzare un grafo completo della memoria.

---

# ENRICHMENT / BACKUP — comprehension

Dopo aver compreso il loop equivalente:

```python
positivi = [x for x in numeri if x > 0]
```

può essere confrontata come forma più compatta.

Non è prerequisito del core di seconda.

---

# ENRICHMENT / BACKUP — invertire una lista

Possibili operazioni:

- nuova lista costruita manualmente;
- `list(reversed(x))`;
- `x[::-1]`;
- `x.reverse()`.

La domanda utile non è “quale è più Pythonica?”, ma:

> creo un nuovo oggetto o modifico l'originale?

---

# Error Clinic

- alias involontario;
- copia confusa con alias;
- rimozione durante `for`;
- `sort()` assegnato;
- funzione che muta input senza dichiararlo;
- confronto solo sul risultato ignorando gli effetti collaterali.

---

# Minimum mastery checkpoint

Sai:

1. spiegare `b = a`?;
2. prevedere una mutazione tramite alias?;
3. creare una nuova lista esterna per una lista piatta?;
4. spiegare perché rimuovere durante iterazione è rischioso?;
5. filtrare costruendo una nuova lista?;
6. distinguere `sort()` e `sorted()`?;
7. testare un contratto di non-mutazione?.

Shallow copy annidata e comprehension non devono dominare il gate.

---

# Recap

```text
alias → stesso oggetto
copy  → nuovo contenitore esterno
```

```text
mutazione promessa? → testala
non-mutazione promessa? → testala
```

Prossimo: tuple, unpacking e dati tabellari.

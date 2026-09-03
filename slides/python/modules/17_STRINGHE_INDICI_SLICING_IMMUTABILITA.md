---
marp: true
paginate: true
size: 16:9
title: M17 — Stringhe, indici e slicing
---

# M17 — Stringhe: indici, slicing e immutabilità
## `str` come sequenza ordinata

PY2-06 — Stringhe come sequenze e testo

---

# Una stringa è una sequenza

```python
parola = "python"
```

```text
indice       0  1  2  3  4  5
             p  y  t  h  o  n
indice neg. -6 -5 -4 -3 -2 -1
```

---

# Lunghezza e indici validi

```python
len("python")  # 6
```

Ultimo indice positivo valido:

```text
len(testo) - 1
```

---

# Accesso singolo

```python
parola[0]
parola[5]
parola[-1]
```

Prevedi prima il carattere.

---

# `IndexError`

```python
parola[6]
```

La posizione non esiste.

Domanda:

> qual è l'ultimo indice valido?

---

# Slicing

```python
parola[1:4]
```

produce:

```text
yth
```

```text
start incluso
stop escluso
```

---

# Slice oltre il limite

```python
parola[3:100]
```

non è lo stesso caso di `parola[100]`.

Indice singolo fuori range → errore.  
Slice oltre il limite → parte disponibile.

---

# Indici negativi

```python
parola[-1]
parola[-2]
```

Utili quando il problema parla di ultimo/penultimo carattere.

---

# Step

```python
parola[::2]
parola[::-1]
```

Leggi sempre:

```text
start : stop : step
```

Non memorizzare trucchi senza modello.

---

# Immutabilità

Non puoi fare:

```python
parola[0] = "P"
```

Per ottenere un nuovo valore:

```python
nuova = "P" + parola[1:]
```

---

# Iterazione diretta

Se ti serve soltanto il carattere:

```python
for carattere in parola:
    ...
```

---

# Quando usare l'indice

Se la posizione fa parte del problema:

```python
for i in range(len(parola)):
    ...
```

La scelta deve avere una ragione.

---

# Worked example

```python
codice = "ABC-123"
prefisso = codice[:3]
suffisso = codice[-3:]
```

Prima definisci il formato atteso.

---

# Error Clinic

- usare `len(testo)` come indice valido;
- includere per errore lo stop;
- tentare una mutazione;
- usare indice quando basta il carattere;
- confondere indice e slice fuori range.

---

# Checkpoint

Sai spiegare:

1. indice 0;
2. ultimo indice valido;
3. stop escluso;
4. immutabilità;
5. for diretto vs indice;
6. slice come nuova stringa.

---

# Recap

```text
str = sequenza ordinata immutabile
```

```text
indice → posizione
slice  → nuova sottostringa
```

Prossimo: ricerca, membership e metodi stringa.

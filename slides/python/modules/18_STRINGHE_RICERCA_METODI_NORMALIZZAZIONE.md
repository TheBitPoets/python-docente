---
marp: true
paginate: true
size: 16:9
title: M18 — Ricerca, metodi e normalizzazione
---

# M18 — Ricerca, membership, metodi e normalizzazione

PY2-06 — Stringhe come sequenze e testo

---

# Prima la domanda, poi il metodo

Se serve soltanto sapere se `@` esiste:

```python
if "@" in email:
    ...
```

---

# `in` / `not in`

```python
"py" in "python"
"java" not in "python"
```

Rispondono a una domanda di membership.

---

# `find()`

```python
posizione = testo.find("@")
```

Trovato → indice della prima occorrenza.  
Non trovato → `-1`.

---

# Bug classico

```python
if testo.find("a"):
    ...
```

Problema:

- posizione `0` è falsy;
- `-1` è truthy.

Se serve esistenza, usa `in`.

---

# `count()`

```python
"banana".count("a")  # 3
```

Usalo quando coincide col requisito.

---

# Le stringhe restano immutabili

```python
testo.lower()
```

restituisce una nuova stringa.

Se vuoi conservarla:

```python
testo = testo.lower()
```

---

# Normalizzazione

```python
normalizzato = testo.strip().lower()
```

Prima chiediti:

- voglio ignorare spazi esterni?;
- voglio ignorare maiuscole?;
- sto perdendo informazione utile?.

---

# `strip()`

```python
"  ciao  ".strip()
```

Attenzione:

```python
strip(chars)
```

non rimuove una sottostringa esatta: tratta `chars` come insieme di caratteri ai bordi.

---

# Prefissi e suffissi

```python
testo.startswith("http")
testo.endswith(".py")
```

Metodi che comunicano direttamente il requisito.

---

# `replace()`

```python
nuovo = testo.replace("-", " ")
```

Produce una nuova stringa.

---

# Metodo o loop?

Per imparare l'algoritmo:

```python
def conta_vocali(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.lower() in "aeiou":
            conteggio += 1
    return conteggio
```

---

# Criterio di scelta

```text
capisco l'algoritmo
+
conosco gli strumenti standard
+
scelgo ciò che comunica meglio l'intenzione
```

---

# Error Clinic

- `find()` usato come booleano;
- risultato di `lower()` ignorato;
- `strip(chars)` frainteso;
- normalizzazione applicata al dato sbagliato;
- loop manuale inutile.

---

# Checkpoint

Sai spiegare:

1. `in` vs `find()`?
2. perché `find` usa `-1`?
3. perché i metodi non modificano la stringa?
4. quando normalizzare?
5. metodo vs loop?

---

# Recap

```text
esistenza → in
posizione → find
conteggio → count
trasformazione → nuova str
```

Prossimo: algoritmi su testo e parsing semplice.

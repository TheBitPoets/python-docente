---
marp: true
paginate: true
size: 16:9
title: M18 — Ricerca, metodi e normalizzazione
---

# M18 — Ricerca, membership, metodi e normalizzazione
## Prima la domanda, poi l'API

PY2-06 — Stringhe come sequenze e testo

---

# Che cosa deve restare davvero?

## MUST MASTER

```text
esistenza?       → in
posizione?       → find
find non trovato → -1
str immutabile   → metodo produce nuova str
normalizzazione  → scelta del contratto
metodo o loop?   → dipende dall'outcome
```

Non devi memorizzare un catalogo di metodi.

---

# Prima la domanda, poi il metodo

Se serve soltanto sapere se `@` esiste:

```python
if "@" in email:
    ...
```

La scelta comunica direttamente l'intenzione.

---

# `in` / `not in`

```python
"py" in "python"
"java" not in "python"
```

Rispondono a:

```text
questa sottostringa esiste?
```

Non danno la posizione.

---

# `find()`

```python
posizione = testo.find("@")
```

Trovato → indice della prima occorrenza.  
Non trovato → `-1`.

Se non ti serve la posizione, `in` è spesso più leggibile.

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

# Le stringhe restano immutabili

```python
testo = " Python "
testo.lower()
print(testo)
```

`testo` non cambia.

Per conservare il nuovo valore:

```python
testo = testo.lower()
```

oppure:

```python
normalizzato = testo.lower()
```

---

# Normalizzazione

```python
normalizzato = testo.strip().lower()
```

Prima chiediti:

- voglio ignorare spazi esterni?;
- voglio ignorare maiuscole/minuscole?;
- sto perdendo informazione utile?.

Normalizzare è una decisione del contratto, non un automatismo.

---

# Metodo o loop?

Per imparare/implementare l'algoritmo:

```python
def conta_vocali(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.lower() in "aeiou":
            conteggio += 1
    return conteggio
```

Se il requisito coincide con un'operazione standard, il metodo può essere più diretto.

---

# Criterio di scelta

```text
capisco il problema
→ scelgo quale informazione serve
→ scelgo algoritmo o metodo
→ verifico con casi
```

Non vale:

```text
built-in sempre migliore
```

né:

```text
loop manuale sempre migliore
```

---

# GUIDED EXPOSURE — `count()`

```python
"banana".count("a")  # 3
```

Utile quando il requisito è davvero:

> quante occorrenze?

Non è un metodo da memorizzare per forza nel checkpoint.

---

# GUIDED EXPOSURE — prefisso/suffisso

```python
testo.startswith("http")
testo.endswith(".py")
```

Quando il requisito parla proprio di prefisso/suffisso, questi metodi comunicano bene l'intenzione.

---

# GUIDED EXPOSURE — `replace()`

```python
nuovo = testo.replace("-", " ")
```

Produce una nuova stringa.

Usalo se la regola richiesta coincide con una sostituzione standard.

---

# ENRICHMENT / BACKUP — `strip(chars)`

```python
strip(chars)
```

non significa “rimuovi esattamente questa sottostringa”.

`chars` indica caratteri rimovibili ai bordi.

Questa precisione è utile, ma non deve rubare tempo al core `in/find/immutabilità/normalizzazione`.

---

# Error Clinic

- `find()` usato come booleano;
- risultato di `lower()` ignorato;
- normalizzazione applicata senza requisito;
- metodo scelto solo perché appena imparato;
- loop manuale che nasconde un'operazione standard senza obiettivo didattico.

---

# Minimum mastery checkpoint

Sai:

1. scegliere `in` o `find()`?;
2. spiegare `-1` di `find()`?;
3. diagnosticare `if testo.find(...)`?;
4. spiegare perché un metodo non muta la stringa?;
5. costruire una normalizzazione semplice e motivata?;
6. scegliere metodo o loop in un esempio concreto?.

`count`, `replace`, `startswith`, `endswith` e dettagli `strip(chars)` non devono essere tutti ricordati per superare il gate.

---

# Recap

```text
prima la domanda
→ poi l'operazione
```

```text
esistenza → in
posizione → find
trasformazione → nuova str
```

Prossimo: algoritmi su testo e parsing semplice.

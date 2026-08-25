---
marp: true
paginate: true
size: 16:9
title: M19 — Algoritmi su testo e parsing semplice
---

# M19 — Algoritmi su testo e parsing semplice

PY2-06 — Stringhe come sequenze e testo

---

# Riutilizziamo tutto

```text
funzioni
+ loop
+ if
+ contatori
+ indici/slice
+ metodi str
+ test
```

---

# Conta caratteri

```python
def conta_cifre(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.isdigit():
            conteggio += 1
    return conteggio
```

---

# Accumulatore testuale

```python
def solo_lettere(testo):
    risultato = ""
    for carattere in testo:
        if carattere.isalpha():
            risultato += carattere
    return risultato
```

---

# Palindromo: prima l'algoritmo

```text
radar
0 ↔ -1
1 ↔ -2
centro
```

Capisci il confronto prima della versione compatta.

---

# Versione compatta

```python
def palindroma(testo):
    return testo == testo[::-1]
```

Ma il contratto deve dire come trattare maiuscole, spazi e punteggiatura.

---

# Normalizzazione dichiarata

```python
normalizzato = testo.strip().lower()
```

Non normalizzare automaticamente senza requisito.

---

# Casi limite

```text
""
"a"
"Radar"
" radar "
```

Definisci prima il comportamento atteso.

---

# Parsing posizionale

Formato:

```text
ABC-123
```

```python
len(codice) == 7
codice[:3].isalpha()
codice[3] == "-"
codice[4:].isdigit()
```

---

# Niente regex per ora

Prima consolidiamo:

- indici;
- slicing;
- condizioni;
- struttura del formato.

Regex arriverà più avanti.

---

# Metodo vs loop

```python
testo.count("a")
```

vs scansione manuale.

La scelta dipende dall'outcome.

---

# `split()` = ponte verso list

```python
parti = "rosso,verde,blu".split(",")
```

Il risultato è una `list`.

La prossima UDA spiega davvero che cosa significa.

---

# `join()` preview

```python
",".join(parti)
```

```text
stringa → split → parti
parti   → join  → stringa
```

---

# Worked example

Validator username:

- strip;
- lower;
- lunghezza minima;
- caratteri ammessi;
- return booleano.

Riusa M13–M18.

---

# Error Clinic

- stringa vuota ignorata;
- off-by-one;
- parsing senza controllo lunghezza;
- normalizzazione incompleta;
- risultato metodo ignorato;
- `split()` trattato come se restituisse `str`.

---

# Exit checkpoint PY2-06

Sai:

- usare str come sequenza;
- indicizzare/slicare;
- cercare/normalizzare;
- scrivere algoritmi su testo;
- testare casi limite;
- motivare metodo vs loop;
- spiegare `split()` → list.

---

# Recap

```text
str + funzioni + loop + test
→ algoritmi su testo
```

Prossima UDA: liste, mutabilità, alias e copia.

---
marp: true
paginate: true
size: 16:9
title: M19 — Algoritmi su testo e parsing semplice
---

# M19 — Algoritmi su testo e parsing semplice
## Integrare ciò che sappiamo, non collezionare nuovi metodi

PY2-06 — Stringhe come sequenze e testo

---

# Che cosa deve restare davvero?

```text
funzione + loop + if su testo
contatore / accumulatore
casi limite
parsing posizionale
analisi separata dall'output
metodo vs algoritmo
```

`split()` è un ponte verso le liste. `join()` è enrichment.

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

La stringa cambia il dominio, non il metodo di ragionamento.

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

Invariante:

> `conteggio` = numero di caratteri cifra già elaborati.

`isdigit()` è uno strumento standard, non un nuovo algoritmo da imparare a memoria.

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

`risultato` ricorda ciò che abbiamo deciso di conservare.

---

# Casi limite

Per una funzione testuale chiediti, se pertinenti al contratto:

```text
""        stringa vuota
"a"       un carattere
"Radar"   maiuscole
" radar " spazi ai bordi
```

Definisci prima il comportamento atteso.

---

# Parsing posizionale

Formato:

```text
ABC-123
```

Prima:

```python
len(codice) == 7
```

Poi puoi verificare le parti:

```python
codice[:3]
codice[3]
codice[4:]
```

Non accedere a posizioni che il contratto non ha ancora garantito.

---

# Predicate standard come strumenti

```python
codice[:3].isalpha()
codice[4:].isdigit()
```

Servono a esprimere il requisito.

Non trasformare `isalpha/isdigit/isalnum` in un catalogo da memorizzare.

---

# Niente regex per ora

Prima consolidiamo:

- indici;
- slicing;
- condizioni;
- struttura del formato.

Regex arriverà più avanti quando non nasconderà il modello che stiamo imparando.

---

# Metodo vs loop

```python
testo.count("a")
```

vs scansione manuale.

La scelta dipende dall'outcome:

```text
imparare scansione/contatore → loop
operazione standard richiesta → metodo candidato
```

---

# GUIDED EXPOSURE — palindromo

Prima ragiona su caratteri/posizioni opposte.

Solo dopo puoi confrontare una forma compatta:

```python
testo == testo[::-1]
```

Il contratto deve dire come trattare maiuscole, spazi e punteggiatura.

---

# GUIDED EXPOSURE — `split()`

```python
parti = "rosso,verde,blu".split(",")
```

Il risultato non è una `str`.

È una:

```text
list
```

Per ora basta riconoscere il ponte. M20 insegnerà davvero che cosa significa lista mutabile.

---

# ENRICHMENT / BACKUP — `join()`

```python
",".join(parti)
```

```text
stringa → split → più parti
più parti → join → stringa
```

Utile, ma non requisito per chiudere PY2-06.

---

# Worked example

Validator username semplice:

- strip/lower secondo contratto;
- lunghezza minima;
- caratteri ammessi;
- return booleano;
- casi limite.

Riusa M13–M18.

---

# Error Clinic

- stringa vuota ignorata;
- off-by-one;
- parsing senza controllo lunghezza;
- normalizzazione non prevista dal contratto;
- risultato metodo ignorato;
- `split()` trattato come se restituisse `str`.

---

# Exit checkpoint PY2-06

Sai:

- usare `str` come sequenza immutabile;
- indicizzare/slicare;
- scegliere iterazione diretta/per indice;
- cercare/normalizzare con una scelta motivata;
- scrivere algoritmi su testo con loop/funzioni;
- testare casi limite;
- motivare metodo vs loop;
- spiegare `split()` → `list`.

`join`, regex e palindrome compatto non sono prerequisiti del gate.

---

# Recap

```text
str + funzioni + loop + test
→ algoritmi su testo
```

Prossima UDA: liste, mutabilità, alias e copia.

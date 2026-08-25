---
marp: true
paginate: true
size: 16:9
title: M08 — Annidamento, validazione e refactoring
---

# M08 — Annidamento, validazione e refactoring
## Quando una decisione dipende davvero da un'altra

PY2-03 — Selezione e logica

---

# Problema iniziale

```text
credenziali valide?
    no → accesso negato
    sì → account attivo?
             no → disabilitato
             sì → accesso
```

La seconda domanda ha senso solo dopo la prima.

---

# Annidamento

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

Il secondo `if` viene raggiunto soltanto se il primo è vero.

---

# Path trace

Caso:

```text
credenziali = True
account = False
```

```text
prima domanda → True
seconda       → False
output        → disabilitato
```

Segui un percorso alla volta.

---

# Tabella dei path

| credenziali | account | risultato |
|---|---|---|
| F | F | negato |
| F | V | negato |
| V | F | disabilitato |
| V | V | accesso |

Quando la prima è falsa, la seconda non cambia il risultato.

---

# Annidato o composto?

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

oppure:

```python
if credenziali_valide and account_attivo:
    print("accesso")
```

Se la specifica richiede solo accesso/non accesso, possono essere equivalenti.

---

# Ma attenzione alle informazioni

Se dobbiamo distinguere:

```text
credenziali errate
account disabilitato
```

una semplice condizione `A and B` può perdere una distinzione richiesta.

Refactoring ≠ accorciare a ogni costo.

---

# Validazione

Specifica:

```text
voto deve essere 0..10
```

```python
if voto < 0 or voto > 10:
    print("dato non valido")
else:
    ...
```

Prima validità, poi classificazione.

---

# Non abbiamo ancora `while`

In M08 sappiamo:

```text
rilevare input fuori dominio
```

Non sappiamo ancora:

```text
richiederlo di nuovo finché è valido
```

Quello arriva con `while` nella prossima UDA.

---

# Tipo corretto, valore non valido

```text
12
```

è un intero, ma non è valido come voto `0..10`.

Diverso da:

```text
"ciao"
```

che non può essere convertito con `int()`.

`try/except` non è ancora il tema.

---

# Worked example

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
```

Test: `-1, 0, 5, 6, 10, 11`.

---

# Booleano con un nome

```python
voto_valido = 0 <= voto <= 10
```

Poi:

```python
if voto_valido:
    ...
```

Il nome deve aggiungere significato, non rumore.

---

# Refactoring controllato

Prima:

```python
if A:
    if B:
        azione()
```

Dopo:

```python
if A and B:
    azione()
```

Prima di accettarlo:

```text
stessi casi
→ stesso comportamento
→ intenzione più chiara?
```

---

# Bug: dipendenza inventata

Specifica:

```text
piove → ombrello
freddo → giacca
```

Bug:

```python
if piove:
    if fa_freddo:
        print("giacca")
    print("ombrello")
```

La giacca ora dipende dalla pioggia, ma la specifica non lo diceva.

---

# Bug: validazione troppo tardi

```python
if voto < 6:
    print("insufficiente")
else:
    if voto < 0 or voto > 10:
        print("dato non valido")
```

Con `-1` classifichi prima di validare.

---

# Path coverage

Credenziali/account:

```text
P1 → credenziali false
P2 → credenziali true, account false
P3 → credenziali true, account true
```

Non contare solo quanti test hai.

Chiedi: **quali percorsi coprono?**

---

# Refactoring e test

```text
test prima
→ cambia struttura
→ stessi test
→ confronta comportamento
```

I test proteggono anche quando miglioriamo il codice.

---

# De Morgan: solo una lente

Condizioni negate possono essere riscritte.

Ma in questa fase:

> niente algebra booleana “furba”.

Prima linguaggio naturale + casi concreti.

---

# Microscope: dipendenza reale?

A. autenticato → poi permesso admin

B. piove → ombrello; freddo → giacca

C. voto valido → poi classifica

D. quiz → badge; progetto → bonus

Scegli la struttura soltanto dopo aver descritto la relazione.

---

# Mini-project

Classificatore validato:

```text
input/output/vincoli
→ flow chart/pseudocodice
→ tabella path
→ codice
→ test
→ spiegazione della struttura
```

Piccolo progetto, integrazione completa.

---

# Romeo: solo se aggiunge valore

Possibile uso:

```text
valida parametro missione
→ poi scegli comportamento
```

Oppure path trace di una missione già nota.

Niente hardware/networking e nessuna nuova Activity duplicata.

---

# Checkpoint PY2-03

1. Quando annidare?
2. Quando `A and B` può sostituire un annidamento?
3. Perché validare prima di classificare?
4. Perché non ripetiamo ancora l'input?
5. Che cosa significa preservare i test nel refactoring?
6. Che cosa significa coprire i path principali?

---

# Recap

```text
annidamento → dipendenza tra decisioni
```

```text
validazione → dato nel dominio?
```

```text
refactoring → struttura diversa, comportamento preservato
```

Prossima UDA: **ripetizione con `while` e `for`**.

---
marp: true
paginate: true
size: 16:9
title: M14 — Scope locale, dati e composizione
---

# M14 — Scope locale, passaggio dei dati e composizione
## Funzioni che collaborano senza dipendenze nascoste

PY2-05 — Funzioni, decomposizione e testing

---

# Contesto locale

```python
def doppio(numero):
    risultato = numero * 2
    return risultato
```

`numero` e `risultato` sono locali alla chiamata.

---

# Locale fuori dalla funzione

```python
def doppio(numero):
    risultato = numero * 2
    return risultato

print(risultato)
```

La funzione comunica con l'esterno tramite `return`.

---

# Passare ciò che serve

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

La firma rende visibili i dati necessari.

---

# Dipendenza globale nascosta

```python
prezzo = 10

def costo(quantita):
    return prezzo * quantita
```

La funzione usa un dato che non compare nel contratto.

---

# Versione esplicita

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

Più semplice da:

- capire;
- testare;
- riusare;
- provare con dati diversi.

---

# Non è un dogma

Una costante di dominio può avere senso:

```python
IVA_PERCENTUALE = 22
```

La domanda è:

> la dipendenza è chiara oppure nascosta?

---

# Comporre funzioni

```python
def area(base, altezza):
    return base * altezza


def costo_pittura(area, costo_mq):
    return area * costo_mq
```

---

# Flusso esplicito

```python
area_calcolata = area(3, 4)
costo = costo_pittura(area_calcolata, 8)
```

Il risultato di A diventa input di B.

---

# Perché variabili intermedie?

Versione compatta:

```python
costo = costo_pittura(area(3, 4), 8)
```

Versione più leggibile per beginner:

```python
area_calcolata = area(3, 4)
costo = costo_pittura(area_calcolata, 8)
```

Più corto ≠ sempre migliore.

---

# Call graph

```text
main
├─ area
└─ costo_pittura
```

Mostra quali funzioni collaborano.

---

# Flusso dei dati

```text
base, altezza
→ area
→ area_calcolata
→ costo_pittura + costo_mq
→ costo
```

Questo prepara la progettazione top-down.

---

# Due chiamate, due contesti locali

```python
x = doppio(3)
y = doppio(10)
```

Ogni chiamata usa i propri valori locali.

---

# Error Clinic

- locale usata fuori funzione;
- globale modificabile nascosta;
- parametro non passato;
- return ignorato;
- composizione troppo compressa.

---

# Git G1 entra nel workflow

```text
git status
→ quali file sono cambiati?

git diff
→ che cosa ho modificato?
```

Git osserva il refactoring; non diventa una lezione separata qui.

---

# Checkpoint

Sai spiegare:

1. che cos'è un nome locale?
2. perché passare i dati esplicitamente?
3. perché una globale può nascondere dipendenze?
4. come A alimenta B?
5. quando una variabile intermedia aiuta?
6. che cos'è un call graph?

---

# Recap

```text
input espliciti
→ nomi locali
→ return
→ composizione
```

Prossimo modulo: progettazione top-down e responsabilità.

---
marp: true
paginate: true
size: 16:9
title: M16 — Assert, regression e refactoring
---

# M16 — `assert`, regression test, debug e refactoring
## Rendere eseguibili le aspettative

PY2-05 — Funzioni, decomposizione e testing

---

# Dai casi su carta agli assert

```python
def doppio(x):
    return x * 2

assert doppio(3) == 6
assert doppio(0) == 0
assert doppio(-2) == -4
```

---

# Che cosa fa `assert`?

```python
assert condizione
```

- `True` → continua;
- `False` → `AssertionError`.

Un'aspettativa diventa eseguibile.

---

# Test verde ≠ prova assoluta

I test danno evidenza e trovano bug.

Chiediti:

- caso normale?;
- confine?;
- caso che prima falliva?.

---

# Confini

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

Testa:

```text
30
0
120
-1
121
```

---

# Test rosso = informazione

```text
quale caso?
→ atteso?
→ ottenuto?
→ bug codice o test?
→ modifica minima
→ riesegui tutti
```

---

# Anche il test può essere sbagliato

```python
assert doppio(3) == 7
```

La fonte autorevole è la specifica/contratto.

Non modificare il codice solo per compiacere un test errato.

---

# Regression test

```text
bug scoperto
→ caso che lo riproduce
→ test rosso
→ fix
→ test verde
→ tutti i vecchi test verdi
```

---

# Esempio

```python
def massimo(a, b):
    if a > b:
        return a
    return a
```

Caso:

```python
assert massimo(2, 5) == 5
```

Il test espone il bug.

---

# Refactoring

> migliorare la struttura senza cambiare il comportamento richiesto.

Esempi:

- rinominare;
- estrarre funzione;
- eliminare duplicazione;
- separare I/O/logica;
- rimuovere globale nascosta.

---

# Test prima e dopo

```text
test verdi
→ refactor
→ stessi test
```

Se diventano rossi, il comportamento può essere cambiato.

---

# `assert` non gestisce l'input utente

Non usiamo `assert` come sostituto della gestione degli errori esterni.

Qui verifica aspettative di sviluppo/test.

---

# Funzioni piccole, test chiari

```text
responsabilità chiara
→ input/output chiari
→ casi chiari
→ test semplici
```

---

# Git G1

```text
git diff
→ che cosa ho cambiato?
```

Al Checkpoint A:

```text
git add
git commit
```

per salvare uno stato significativo.

---

# P2 TheBitLab

Target:

```text
funzione + argomenti
→ sandbox
→ return/exception reale
→ confronto host-side
```

Tracciato in `2cornot2c#756`.

---

# Activity candidate

- A: test reader;
- B: add a test;
- C: implement from contract;
- D: debug regression;
- E: mini-project funzionale.

---

# Exit checkpoint PY2-05

Sai:

- usare funzioni e `return`;
- capire scope locale;
- comporre funzioni;
- progettare top-down;
- separare I/O/logica;
- scrivere `assert`;
- aggiungere regression test;
- refactorare con test verdi.

---

# Recap

```text
contratto
→ casi
→ assert
→ implementazione
→ debug
→ regression
→ refactor
```

Prossimo: Checkpoint A e primo commit Git guidato.

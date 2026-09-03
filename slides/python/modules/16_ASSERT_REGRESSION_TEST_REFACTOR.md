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

# Che cosa deve restare davvero?

```text
caso → assert
confini
atteso vs ottenuto
bug nel codice o nel test?
regression test
fix minimo
riesegui tutti
refactor con stessi test
```

Non serve conoscere pytest, coverage o dettagli del grader.

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

# Ogni test rappresenta qualcosa

Domanda:

> quale frase della specifica rappresenta questo `assert`?

Il test non è autorevole da solo.

La fonte resta:

```text
specifica / contratto
```

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

# Git G1 Observe

Durante fix/refactor puoi usare in modo guidato:

```text
git status
git diff
```

per rispondere:

> che cosa ho cambiato davvero?

Staging/commit/history arrivano al Checkpoint A.

---

# Activity candidate

- A: test reader;
- B: add a test;
- C: implement from contract;
- D: debug regression;
- E: mini-project funzionale.

---

# Minimum mastery checkpoint

Sai:

1. trasformare un caso in `assert`?;
2. scegliere un confine rilevante?;
3. spiegare atteso e ottenuto?;
4. distinguere bug nel codice e test errato?;
5. creare un test che riproduce un bug?;
6. fare fix e rieseguire tutti?;
7. refactorare con gli stessi test verdi?.

---

# Exit checkpoint PY2-05

Sai:

- usare funzioni e `return`;
- capire scope locale;
- comporre funzioni;
- progettare top-down senza burocrazia;
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

Prossimo: Checkpoint A e primo checkpoint Git guidato **embedded** nel lavoro Python.

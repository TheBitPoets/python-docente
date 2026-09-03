---
marp: true
paginate: true
size: 16:9
title: M01 — Dal problema ai passi
---

# M01 — Dal problema ai passi
## Specifica, pseudocodice, trace e test

PY2-01 — Problem solving, algoritmi e flow chart

---

# Da dove partiamo?

Problema:

> Leggi due prezzi e indica quale è maggiore.
> Se sono uguali, dichiaralo.

Prima del diagramma chiediamo:

```text
INPUT?
OUTPUT?
CASI?
```

---

# Il caso che si dimentica

```text
A > B
B > A
A = B
```

Se progetti solo i primi due casi, la soluzione è incompleta.

La specifica è un contratto da leggere con attenzione.

---

# Decomporre senza burocratizzare

```text
1. acquisisci A
2. acquisisci B
3. confronta
4. scegli il risultato
5. comunica
```

Decomporre serve a vedere decisioni e dati.

Non a moltiplicare i passi inutilmente.

---

# Algoritmo ambiguo

```text
1. prendi due numeri
2. scegli quello giusto
3. stampa
```

Problema:

> “quello giusto” non contiene una regola eseguibile.

---

# Pseudocodice leggibile

```text
SE A > B
    MOSTRA A
ALTRIMENTI SE B > A
    MOSTRA B
ALTRIMENTI
    MOSTRA "uguali"
FINE SE
```

Poche convenzioni, significato chiaro.

---

# Non serve Python travestito

Per ora preferiamo:

```text
SE x >= 10
    MOSTRA x
FINE SE
```

non:

```python
if x >= 10:
    print(x)
```

La sintassi arriverà quando l'idea sarà stabile.

---

# Dry-run

```text
LEGGI prezzo
sconto ← 0
SE prezzo > 100
    sconto ← 10
FINE SE
finale ← prezzo - sconto
MOSTRA finale
```

Proviamo `prezzo = 120`.

---

# Trace table

| passo | prezzo | sconto | finale | output |
|---:|---:|---:|---:|---:|
| start | 120 | — | — | — |
| init | 120 | 0 | — | — |
| decisione | 120 | 10 | — | — |
| calcolo | 120 | 10 | 110 | — |
| output | 120 | 10 | 110 | 110 |

Il trace rende visibile lo stato.

---

# Domanda sullo stato

> Che cosa significa questa variabile **dopo** il passo appena eseguito?

Esempio:

```text
saldo: 100 → 80 → 65
```

Capire lo stato prepara ai cicli e agli accumulatori.

---

# Ordine sbagliato

```text
1. MOSTRA totale
2. LEGGI prezzo
3. totale ← prezzo + 5
```

Qual è il primo passo impossibile?

Correggi con la modifica minima.

---

# Finisce davvero?

```text
ripeti "prova ancora"
```

Quando termina?

Non è definito.

Un algoritmo automatico deve avere una conclusione o una regola di uscita.

---

# Test prima del programma

Per “maggiore tra due prezzi”:

```text
10, 5 → primo
5, 10 → secondo
7, 7 → uguali
```

I test nascono dalla specifica, non dal codice.

---

# Error Clinic

Cerca:

- passo mancante;
- stato senza significato;
- caso non coperto;
- ordine sbagliato;
- procedura non terminante.

Poi chiedi:

```text
qual è il primo punto in cui il trace diverge?
```

---

# Laboratorio

Da una specifica produci:

```text
INPUT
OUTPUT
VINCOLI
PSEUDOCODICE
2 casi diversi
1 caso limite
1 TRACE
```

Il compagno deve poter eseguire i tuoi passi senza interpretare le tue intenzioni.

---

# Minimum mastery checkpoint

Sai:

1. leggere input/output/vincoli?;
2. decomporre?;
3. scrivere pseudocodice neutro?;
4. fare un trace?;
5. trovare un caso mancante?;
6. spiegare la terminazione?;
7. progettare test prima del codice?.

---

# Recap

```text
specifica
→ decomposizione
→ pseudocodice
→ trace
→ test
```

Prossimo: sequenza e selezione nei flow chart.

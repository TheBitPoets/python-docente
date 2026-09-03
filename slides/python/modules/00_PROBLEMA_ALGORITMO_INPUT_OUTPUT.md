---
marp: true
paginate: true
size: 16:9
title: M00 — Problema, algoritmo, programma, input e output
---

# M00 — Problema, algoritmo, programma
## Prima del codice viene il problema

Orientamento iniziale · finestra PY2-01

---

# Oggi non serve Python

Vogliamo imparare a distinguere:

```text
problema
→ algoritmo
→ programma
```

E a riconoscere:

```text
input · output · vincoli · test
```

---

# Problema iniziale

> Una bottiglia costa 2 euro.
> Il cliente paga con 5 euro.
> Quanto resto deve ricevere?

Prima domanda:

```text
quali dati servono?
```

Seconda:

```text
quale risultato vogliamo?
```

---

# Input e output

```text
INPUT
prezzo
pagato

OUTPUT
resto
```

Poi possiamo descrivere:

```text
resto ← pagato - prezzo
```

---

# Problema ≠ algoritmo

**Problema**

> che cosa voglio ottenere?

**Algoritmo**

> quali passi posso eseguire per ottenerlo?

Non confondere richiesta e soluzione.

---

# Algoritmo ≠ programma

```text
algoritmo
= procedura
```

```text
programma
= algoritmo espresso in un linguaggio eseguibile
```

Il linguaggio arriverà dopo.

---

# Un passo troppo vago

```text
1. prendi i dati
2. fai il calcolo giusto
3. mostra
```

Domanda:

> “calcolo giusto” è un'istruzione abbastanza precisa?

No: nasconde la decisione importante.

---

# Passi operativi

```text
1. acquisisci prezzo
2. acquisisci pagato
3. calcola pagato - prezzo
4. mostra il resto
```

Non servono più passi del necessario.

Servono quelli che rendono il procedimento eseguibile.

---

# Informazione inutile

> Il sensore è blu e misura 31 °C.
> La soglia è 30 °C.
> La temperatura supera la soglia?

Il colore del sensore serve?

```text
no
```

Non tutti i dati disponibili appartengono all'algoritmo.

---

# Informazione mancante

> Calcola l'area.

Possiamo procedere?

```text
no
```

Mancano forma e misure.

Non inventare ciò che la specifica non dice.

---

# Un caso riuscito basta?

Algoritmo “maggiore tra due numeri”:

```text
8, 3 → 8
```

È sufficiente?

Prova anche:

```text
3, 8
5, 5
-2, -7
```

---

# Caso normale e caso limite

Soglia = 14

```text
15 → normale
14 → sul confine
13 → appena sotto
```

I confini fanno emergere molti errori.

---

# Tre famiglie di errore

```text
ho capito male la richiesta
→ errore di comprensione

ho progettato passi sbagliati
→ errore nell'algoritmo

il futuro programma non riesce a eseguirsi
→ errore di esecuzione
```

Prima chiedi **dove** nasce il problema.

---

# Micro-lab

Per una consegna annota:

```text
INPUT
OUTPUT
VINCOLI
PASSI
CASO NORMALE
CASO LIMITE
```

Poi fai seguire i passi a un compagno.

---

# Minimum mastery checkpoint

Sai:

1. distinguere problema/algoritmo/programma?;
2. trovare input e output?;
3. riconoscere un dato inutile?;
4. segnalare un dato mancante?;
5. ordinare passi semplici?;
6. proporre più di un test?.

---

# Recap

```text
capire
→ separare dati e risultato
→ descrivere passi
→ provare casi diversi
→ correggere prima del codice
```

Prossimo: pseudocodice e trace manuale.

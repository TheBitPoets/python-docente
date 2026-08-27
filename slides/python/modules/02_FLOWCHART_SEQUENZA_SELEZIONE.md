---
marp: true
paginate: true
size: 16:9
title: M02 — Flow chart: sequenza, input/output e selezione
---

# M02 — Flow chart
## Sequenza, input/output e selezione

PY2-01 — Problem solving, algoritmi e flow chart

---

# Perché un diagramma?

Lo pseudocodice usa testo.

Il flow chart rende visibile il **flusso di controllo**:

```text
inizio
  ↓
input
  ↓
calcolo
  ↓
decisione
 ↙      ↘
...     ...
```

---

# Simboli core

| Idea | Forma | Significato |
|---|---|---|
| start/end | terminatore | inizio/fine |
| input/output | parallelogramma | dati |
| processing | rettangolo | calcolo |
| decision | rombo | scelta |
| freccia | collegamento | prossimo passo |

Poche forme, usate bene.

---

# Prima sequenza

Problema:

> Leggi due numeri e mostra la somma.

```text
START
 ↓
INPUT A
 ↓
INPUT B
 ↓
SOMMA ← A + B
 ↓
OUTPUT SOMMA
 ↓
END
```

---

# Trace della sequenza

Input: `2`, `3`

| nodo | A | B | somma | output |
|---|---:|---:|---:|---:|
| start | — | — | — | — |
| input A | 2 | — | — | — |
| input B | 2 | 3 | — | — |
| calcolo | 2 | 3 | 5 | — |
| output | 2 | 3 | 5 | 5 |

---

# Una decisione

> La temperatura supera 30?

Condizione:

```text
temperatura > 30 ?
```

Risultato possibile:

```text
true
false
```

---

# Selezione doppia

```text
        temperatura > 30?
          /        \
       true        false
        /            \
"sopra soglia"   "entro soglia"
        \            /
              END
```

Ogni input segue un ramo.

---

# Caso di confine

Soglia = 30

```text
31 → sopra soglia
30 → entro soglia
29 → entro soglia
```

Perché `30` è il test più importante?

Perché è esattamente sul confine della condizione.

---

# Selezione semplice

> Se il saldo è negativo mostra un avviso, poi continua.

```text
saldo < 0?
 true ↙    ↘ false
AVVISO       |
      \      /
      prossimo passo
```

Anche il ramo senza azione deve avere un percorso chiaro.

---

# Condizione invertita

Richiesta:

> “ammesso” se età >= 14

Diagramma:

```text
età >= 14?
true  → "non ammesso"
false → "ammesso"
```

Schema valido?

Forse sì.

Algoritmo corretto?

No.

---

# Regola importante

```text
file/schema valido
≠
algoritmo corretto
```

La piattaforma può controllare struttura e comportamento deterministico.

La qualità della soluzione resta anche responsabilità dello studente e del docente.

---

# Output troppo presto

Errore:

```text
INPUT prezzo
↓
OUTPUT prezzo
↓
decisione sconto
```

L'output avviene prima della modifica richiesta.

Il trace mostra il primo punto di divergenza.

---

# Tre casi con due decisioni

Classifica `n`:

```text
n < 0?
 true → negativo
 false → n == 0?
          true → zero
          false → positivo
```

Componiamo poche primitive.

Non serve un nuovo simbolo per ogni problema.

---

# Flowchart Lab candidate

Quando disponibile nel Classroom Environment:

```text
TheBitLab
→ Flowchart Lab locale
→ browser
→ Run / Step / Reset
→ variable watch
→ algorithm.flow.json
```

Il diagramma non esegue Python arbitrario.

---

# Fallback ancora obbligatorio

Finché la capability non è classroom-certified:

```text
carta / lavagna / template
+ trace table
+ casi di test
+ rubric docente
```

Gli outcome non dipendono dal tool.

---

# Che cosa può verificare il tool?

Deterministicamente:

- schema;
- collegamenti;
- terminazione entro limite;
- output su input dichiarati;
- trace.

Non assegna automaticamente un voto affidabile alla **qualità del diagramma**.

---

# Laboratorio guidato

Costruisci:

> Leggi `temperatura`.
> Se è maggiore di 30 mostra “sopra soglia”, altrimenti “entro soglia”.

Prima prepara:

```text
31 → sopra soglia
30 → entro soglia
29 → entro soglia
```

---

# Controlled Change

Diagramma già funzionante:

```text
soglia = 30
```

Nuovo requisito:

```text
soglia = 25
```

Cambia soltanto ciò che serve e aggiorna i test.

---

# Error Clinic

Diagnostica:

1. ramo false mancante;
2. condizione invertita;
3. output prima del calcolo;
4. nodo irraggiungibile;
5. ramo senza fine;
6. trace diverso dall'atteso.

---

# Minimum mastery checkpoint

Sai:

1. leggere i simboli core?;
2. costruire una sequenza?;
3. costruire true/false?;
4. fare un trace?;
5. scegliere un test sul confine?;
6. distinguere struttura e semantica?;
7. usare il fallback manuale?.

---

# Recap

```text
sequenza → un percorso
selezione → scelta di un ramo
trace → stato + percorso
test → soprattutto i confini
```

Prossimo: iterazione e annidamento.

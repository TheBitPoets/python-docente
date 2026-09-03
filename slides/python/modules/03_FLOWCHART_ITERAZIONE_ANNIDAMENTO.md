---
marp: true
paginate: true
size: 16:9
title: M03 — Flow chart: iterazione, terminazione e annidamento
---

# M03 — Flow chart
## Iterazione, terminazione e annidamento

PY2-01 — Problem solving, algoritmi e flow chart

---

# Quando una freccia torna indietro

> Chiedi un valore finché non è compreso tra 1 e 10.

```text
leggi valore
↓
valido?
 sì → continua
 no → torna a leggere
```

Ripetere non significa ripetere per sempre.

---

# Le quattro domande del ciclo

```text
1. quale stato esiste prima?
2. quando eseguo il corpo?
3. che cosa cambia?
4. perché prima o poi esco?
```

Queste domande vengono prima della sintassi di un linguaggio.

---

# Validazione ripetuta

```text
LEGGI valore
MENTRE valore < 1 O valore > 10
    LEGGI valore
FINE MENTRE
MOSTRA "valido"
```

Input:

```text
0
12
7
```

Quante volte ripete?

---

# Trace della validazione

| controllo | valore | invalido? | azione |
|---:|---:|---|---|
| 1 | 0 | sì | leggi |
| 2 | 12 | sì | leggi |
| 3 | 7 | no | esci |

Il numero di iterazioni dipende dai dati.

---

# Aggiornamento mancante

```text
i ← 0
MENTRE i < 3
    MOSTRA i
FINE MENTRE
```

Che cosa cambia `i`?

```text
nulla
```

La condizione resta vera.

---

# Correzione

```text
i ← 0
MENTRE i < 3
    MOSTRA i
    i ← i + 1
FINE MENTRE
```

Ora lo stato evolve:

```text
0 → 1 → 2 → 3
```

---

# Contatore

| giro | i prima | output | i dopo |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 2 | 3 |

Poi:

```text
3 < 3 → false
```

Il ciclo termina.

---

# Off-by-one

Vogliamo:

```text
1 2 3
```

Confronta:

```text
i < 3
```

con:

```text
i <= 3
```

Una piccola differenza nel confine cambia il numero di iterazioni.

---

# Accumulatore concettuale

```text
totale ← 0
contatore ← 0

MENTRE contatore < 3
    LEGGI valore
    totale ← totale + valore
    contatore ← contatore + 1
FINE MENTRE
```

Domanda:

> che cosa significa `totale` dopo ogni giro?

---

# Significato dello stato

Risposta utile:

> `totale` contiene la somma dei valori letti **finora**.

Non memorizzare una ricetta.

Spiega che cosa rappresenta lo stato.

---

# Selezione dentro un ciclo

> Leggi 5 numeri e conta quanti sono positivi.

```text
ripeti per ogni dato
    leggi valore
    valore > 0?
      true → incrementa conteggio
```

Il ciclo decide **quante osservazioni**.
La selezione decide **quando aggiornare**.

---

# Ciclo dentro una selezione

```text
scelta = esegui?
 true → ripeti operazione 3 volte
 false → end
```

Non esiste una regola grafica universale “il ciclo va sempre fuori”.

La struttura segue il problema.

---

# Primo annidamento

Griglia 2 × 3:

```text
per ogni riga
    per ogni colonna
        visita cella
```

Due stati:

```text
riga
colonna
```

---

# Trace di una griglia 2 × 2

| riga | colonna | cella |
|---:|---:|---|
| 0 | 0 | (0,0) |
| 0 | 1 | (0,1) |
| 1 | 0 | (1,0) |
| 1 | 1 | (1,1) |

Se perdi il filo, costruisci una tabella.

---

# Costo intuitivo

Se raddoppio sia righe sia colonne...

```text
2 × 2 → 4 celle
4 × 4 → 16 celle
```

Non formalizziamo Big-O oggi.

Osserviamo soltanto quanto lavoro viene ripetuto.

---

# Step limit del Flowchart Lab

Il runtime candidate usa un limite di step.

Se ottieni:

```text
limit-exceeded
```

non significa automaticamente “questo è il bug”.

Significa:

> non abbiamo raggiunto END entro il limite.

---

# Come diagnosticare un loop infinito

Controlla:

```text
inizializzazione
condizione
aggiornamento
arco di ritorno
```

Poi guarda gli ultimi valori del trace.

Non modificare a tentativi.

---

# Inizializzazione nel posto sbagliato

Errore:

```text
MENTRE ...
    conteggio ← 0
    conteggio ← conteggio + 1
FINE MENTRE
```

Il contatore viene azzerato a ogni giro.

Che cosa avrebbe dovuto ricordare?

---

# Controlled Change

Da:

```text
0 1 2
```

a:

```text
0 1 2 3 4
```

Quale confine cambia?

Poi:

```text
1 2 3 4 5
```

Quali parti cambiano adesso?

---

# Mini-project

Missione concettuale su griglia:

> percorri 5 celle, osserva se ciascuna è libera e conta gli ostacoli.

Consegna:

```text
specifica
flow chart
2 trace
1 caso limite
spiegazione della terminazione
```

Nessuna API Python o hardware obbligatorio.

---

# Fallback ancora valido

Se Flowchart Lab non è disponibile nel profilo reale:

```text
carta / lavagna / template
+ trace
+ casi di test
+ rubric docente
```

Gli outcome restano gli stessi.

---

# Exit checkpoint PY2-01

Sai:

1. progettare input/output?;
2. scrivere pseudocodice?;
3. disegnare sequenza e selezione?;
4. costruire un ciclo?;
5. spiegare la terminazione?;
6. fare un trace?;
7. trovare un caso limite?;
8. diagnosticare un errore evidente?.

---

# Recap

```text
problema
→ algoritmo
→ flow chart
→ trace
→ test
→ debug
```

Prossimo: tradurremo algoritmi già compresi nei primi programmi Python.

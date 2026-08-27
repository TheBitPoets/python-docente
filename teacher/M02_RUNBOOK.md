# M02 — Runbook docente

## Modulo

**Flow chart: sequenza, input/output e selezione**  
UDA PY2-01 — Problem solving, algoritmi e flow chart.

Stato: draft / Flowchart Lab candidate consumer disponibile ma non classroom-certified.

## Obiettivo docente

Portare lo studente da pseudocodice/trace a una rappresentazione grafica che renda espliciti percorso e decisioni:

```text
sequenza
→ decisione
→ rami true/false
→ trace
→ casi sul confine
→ debug
```

La qualità grafica non è il traguardo. Il diagramma deve essere leggibile, eseguibile/simulabile e spiegabile.

---

# Preparazione

## Materiali

- lesson `content/python/02_FLOWCHART_SEQUENZA_SELEZIONE.md`;
- slide `slides/python/modules/02_FLOWCHART_SEQUENZA_SELEZIONE.md`;
- template manuale con simboli core;
- trace table;
- diagramma soglia funzionante;
- 2–3 diagrammi difettosi.

## Ambiente

Percorso preferito quando disponibile:

```text
TheBitLab managed runtime
→ flowchart-lab
→ browser loopback
→ workspace studente
→ algorithm.flow.json
```

Il consumer candidato è tecnicamente verde su Ubuntu/Windows, ma **non equivale a certificazione dei profili classroom reali**.

Finché quella certificazione manca, predisporre sempre:

```text
carta / lavagna / template
+ trace table
+ rubric docente
```

Non perdere tempo di lezione per riparare manualmente tool non certificati.

---

# Settimana 2 — 2 ore teoria attiva + 1 laboratorio

## Ora teoria attiva 1 — simboli e sequenza

### 0–10 min — richiamo

Riprendere un pseudocodice M01 semplice.

Domanda:

> Possiamo rappresentare lo stesso algoritmo senza cambiarne il significato?

### 10–25 min — simboli core

Introdurre solo:

- start/end;
- input/output;
- processing;
- decision;
- freccia.

Evitare cataloghi di simboli avanzati.

### 25–40 min — sequenza

Costruire insieme:

> leggi A, leggi B, calcola somma, mostra.

Poi far eseguire un trace su `2,3`.

### 40–55 min — Error Clinic lineare

Mostrare:

- output prima del calcolo;
- nodo non raggiungibile;
- passo mancante.

### 55–60 min — micro-check

Far disegnare una sequenza di 4–5 nodi senza supporto.

---

# Ora teoria attiva 2 — selezione e confini

## 0–15 min — decisione

Problema soglia temperatura.

Far formulare prima la condizione in linguaggio naturale e poi come espressione semplice.

## 15–30 min — true / false

Costruire la selezione doppia e seguire entrambi i rami.

## 30–40 min — caso sul confine

Per `temperatura > 30` confrontare:

```text
31
30
29
```

Fare emergere il ruolo del test esattamente sul confine.

## 40–50 min — tre casi

Classificazione negativo/zero/positivo con due decisioni.

Non introdurre una “selezione multipla” come nuova magia: mostrare la composizione di decisioni.

## 50–60 min — struttura vs semantica

Mostrare un diagramma con archi formalmente corretti ma etichette true/false invertite.

Regola da fissare:

```text
schema valido != algoritmo corretto
```

---

# Ora laboratorio

## Percorso A — Flowchart Lab disponibile

1. lanciare dal managed path;
2. costruire/partire dal diagramma soglia;
3. salvare `algorithm.flow.json`;
4. eseguire `31`, `30`, `29`;
5. usare Step e variable watch;
6. esportare/mostrare SVG evidence se utile;
7. spiegare a voce un ramo.

Non trasformare la risposta della piattaforma in voto automatico sulla qualità del diagramma.

## Percorso B — fallback manuale

Stesse consegne usando:

- template;
- penna/frecce;
- trace table;
- casi di test.

Gli outcome e la rubric restano gli stessi.

---

# Controlled Change

Partire da soglia 30 e modificare a 25.

Chiedere:

- quale nodo cambia?;
- quali test devono cambiare?;
- che cosa non deve essere riscritto?.

Obiettivo: modifica minima e spiegabile.

---

# Debug task

Usare a rotazione:

- false branch mancante;
- true/false invertiti;
- output prima del calcolo;
- nodo non raggiungibile;
- percorso che non termina.

Per ogni bug lo studente registra:

```text
sintomo
caso che lo rivela
primo nodo problematico
correzione minima
```

---

# Rubric formativa minima

Osservare separatamente:

1. corrispondenza con la specifica;
2. completezza dei percorsi;
3. trace corretto;
4. scelta dei test;
5. chiarezza/spiegazione.

La piattaforma può aiutare sui punti deterministici, ma non sostituisce 1 e 5 come giudizio didattico complessivo.

---

# Minimum mastery gate

Prima di M03 lo studente dovrebbe saper:

- costruire una sequenza;
- usare una decisione true/false;
- seguire entrambi i rami;
- compilare un trace;
- scegliere un caso di confine;
- diagnosticare almeno un ramo errato.

---

# Handoff a M03

Chiudere con un problema che richiede una ripetizione non nota in anticipo:

> “Continua a chiedere un valore finché è valido.”

Domanda:

> Come rappresentiamo una freccia che torna indietro **senza creare un ciclo infinito**?

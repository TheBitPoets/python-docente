# M03 — Runbook docente

## Modulo

**Flow chart: iterazione, terminazione e annidamento**  
UDA PY2-01 — Problem solving, algoritmi e flow chart.

Stato: draft / Flowchart Lab candidate consumer disponibile ma non classroom-certified.

## Obiettivo docente

Chiudere PY2-01 facendo comprendere il ciclo come **stato che evolve fino a rendere falsa una condizione**, non come forma grafica da copiare.

Progressione:

```text
ripetizione
→ inizializzazione
→ condizione
→ corpo
→ aggiornamento
→ terminazione
→ trace
→ selezione + ciclo
→ primo annidamento
```

---

# Preparazione

## Materiali

- lesson `content/python/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md`;
- slide `slides/python/modules/03_FLOWCHART_ITERAZIONE_ANNIDAMENTO.md`;
- trace table per cicli;
- diagramma contatore funzionante;
- diagramma con aggiornamento mancante;
- mini-project su griglia.

## Ambiente

Come M02:

- Flowchart Lab managed candidate se il profilo reale lo rende disponibile;
- fallback carta/lavagna/template sempre pronto;
- nessun requisito `romeo-sim`;
- nessun Python necessario per raggiungere gli outcome.

Il tool può evidenziare `limit-exceeded`, ma non deve sostituire la diagnosi dello studente.

---

# Settimana 3 — 2 ore teoria attiva + 1 laboratorio

## Ora teoria attiva 1 — ciclo e terminazione

### 0–10 min — problema motivante

> Chiedi un valore finché non è compreso tra 1 e 10.

Far notare che il numero di tentativi non è noto in anticipo.

### 10–25 min — quattro domande del ciclo

Fissare:

```text
stato iniziale
condizione
cambiamento nel corpo
ragione della terminazione
```

### 25–40 min — contatore

Costruire insieme:

```text
i ← 0
MENTRE i < 3
    MOSTRA i
    i ← i + 1
FINE MENTRE
```

Fare trace completo.

### 40–50 min — aggiornamento mancante

Rimuovere `i ← i + 1` e chiedere di prevedere il comportamento prima dell'esecuzione.

### 50–60 min — off-by-one

Confrontare `< 3` e `<= 3` usando casi sul confine.

---

# Ora teoria attiva 2 — composizione e annidamento

## 0–15 min — accumulatore concettuale

Somma di tre valori.

Domanda chiave:

> Che cosa rappresenta `totale` dopo ogni iterazione?

Accettare la spiegazione “somma dei valori letti finora”; non introdurre ancora formalismi inutili.

## 15–30 min — selezione dentro ciclo

Problema:

> Conta quanti dei 5 numeri letti sono positivi.

Separare responsabilità:

```text
ciclo → quante osservazioni
if concettuale → quando aggiornare
```

## 30–40 min — ciclo dentro selezione

Mostrare che la struttura deriva dal problema, non da una regola grafica fissa.

## 40–50 min — primo annidamento

Griglia 2 × 2 o 2 × 3.

Usare una trace table riga/colonna; niente Big-O formale.

## 50–60 min — Error Clinic

Mostrare almeno:

- inizializzazione nel posto sbagliato;
- aggiornamento nella direzione sbagliata;
- arco di ritorno errato.

---

# Ora laboratorio — exit checkpoint

## Fase A — trace loop

Far prevedere:

- numero di iterazioni;
- stato finale;
- output.

## Fase B — controlled change

Da `0..2` a `0..4`, poi a `1..5`.

Far distinguere quando basta cambiare condizione e quando cambia anche l'inizializzazione.

## Fase C — design

Costruire un diagramma con:

- ciclo;
- almeno una selezione;
- terminazione spiegabile.

## Fase D — mini-project

Missione concettuale su griglia:

> percorri 5 celle e conta gli ostacoli.

Output richiesto:

```text
specifica
flow chart
2 trace
1 caso limite
spiegazione della terminazione
```

Romeo è solo scenario motivante; non introdurre API o hardware.

---

# Uso del Flowchart Lab candidate

Se disponibile, far usare:

- Run;
- Step;
- variable watch;
- `algorithm.flow.json`;
- SVG evidence.

Se il diagramma supera il limite di step:

1. non dire subito “ciclo infinito”;
2. far osservare gli ultimi valori;
3. chiedere quale condizione resta vera;
4. cercare aggiornamento/arco responsabile.

Il runtime dichiara esplicitamente `authoritative_grading=false`: la qualità dell'algoritmo resta rubric/manual evidence.

---

# Exit checkpoint PY2-01

Su problemi semplici lo studente dovrebbe saper:

- identificare input/output;
- produrre pseudocodice;
- disegnare sequenza + selezione + iterazione;
- fare trace;
- scegliere un caso limite;
- spiegare la terminazione;
- riconoscere un errore evidente;
- spiegare una correzione minima.

Non richiedere perfezione estetica del diagramma.

---

# Recupero prima di M04

Se uno studente non supera la soglia:

1. tornare a una sequenza lineare;
2. usare una sola variabile;
3. far eseguire fisicamente i passi;
4. introdurre una sola decisione sì/no;
5. introdurre un ciclo con tre iterazioni note;
6. solo dopo tornare a validazione/annidamento.

Python M04 può iniziare con problemi molto semplici, ma non deve diventare il modo per evitare il recupero del ragionamento algoritmico.

---

# Handoff a M04

Chiudere con un algoritmo già noto:

```text
LEGGI A
LEGGI B
somma ← A + B
MOSTRA somma
```

Domanda:

> Ora che sappiamo progettare, simulare e testare questi passi, come li esprimiamo in un linguaggio che il computer può eseguire?

La risposta apre il REPL e il primo script Python.

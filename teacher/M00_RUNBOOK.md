# M00 — Runbook docente

## Modulo

**Problema, algoritmo, programma, input e output**  
Orientamento iniziale integrato nella prima settimana di PY2-01.

Stato: draft.

## Obiettivo docente

Aprire il corso senza trasformare la prima lezione in una lista di definizioni. Lo studente deve iniziare a usare questo ciclo mentale:

```text
capisco la richiesta
→ separo dati e risultato
→ descrivo passi eseguibili
→ provo casi diversi
→ correggo il modello
```

Python, Flowchart Lab e Romeo non sono richiesti in M00.

---

# Preparazione

## Ambiente

Nessun requisito digitale obbligatorio.

Sono sufficienti:

- lavagna;
- foglio/quaderno;
- consegne brevi proiettate o stampate.

Se il Classroom Environment è già disponibile, non usarlo per anticipare sintassi: l'obiettivo è diagnosticare il ragionamento iniziale.

## Materiali

- lesson `content/python/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md`;
- slide `slides/python/modules/00_PROBLEMA_ALGORITMO_INPUT_OUTPUT.md`;
- 3–4 consegne brevi;
- cartoncini/passaggi riordinabili opzionali.

---

# Collocazione temporale

M00 occupa circa **45–60 minuti** della prima ora di corso e si integra con M01 nella stessa settimana.

Non assegnargli una settimana autonoma: PY2-01 ha 9 ore totali e M00 è orientamento/metodo.

---

# Sequenza consigliata

## 0–10 min — problema concreto

Usare un esempio quotidiano:

> prezzo 2 €, pagamento 5 €, calcola il resto.

Chiedere prima di mostrare termini tecnici:

- che cosa conosciamo?;
- che cosa dobbiamo ottenere?;
- quale informazione sarebbe inutile?;
- quale dato mancherebbe in una versione incompleta?.

## 10–20 min — problema / algoritmo / programma

Costruire le tre idee partendo dall'esempio.

Evitare definizioni da memorizzare alla lettera.

Domanda diagnostica:

> Un algoritmo può esistere prima di aver scelto Python?

Risposta attesa: sì.

## 20–35 min — input/output/vincoli

Dare due specifiche e far annotare:

```text
INPUT
OUTPUT
VINCOLI
```

Inserire volontariamente un dato inutile in una consegna.

## 35–45 min — casi diversi

Per “maggiore tra due valori” far proporre almeno:

```text
8,3
3,8
5,5
```

Far emergere che un solo esempio riuscito non basta.

## 45–60 min — diagnostic non valutativo

Micro-task individuale:

1. dati necessari;
2. risultato atteso;
3. ordine di 4 passi;
4. un caso limite;
5. identificazione di un'informazione mancante.

Raccogliere evidence per calibrare M01, non per attribuire un voto.

---

# Misconception da osservare

- “programma” = qualunque insieme di passi;
- usare tutti i dati solo perché presenti;
- inventare informazioni mancanti;
- confondere output con il calcolo che lo produce;
- pensare che un esempio positivo dimostri la correttezza generale;
- saltare passaggi essenziali perché “ovvi”.

---

# Remediation immediata

Per studenti in difficoltà:

- usare un problema fisico/concreto;
- mettere input e output su due cartoncini separati;
- ordinare passi già scritti invece di produrli da zero;
- lavorare su un solo caso prima di chiedere un caso limite.

Non introdurre ancora pseudocodice formale se la distinzione dati/risultato non è stabile.

---

# Evidence minima

Alla fine di M00 lo studente dovrebbe riuscire, su una consegna nuova, a produrre:

```text
INPUT
OUTPUT
3–5 passi
1 caso normale
1 caso limite o alternativo
```

La terminologia può essere ancora imperfetta; il ragionamento deve essere osservabile.

---

# Handoff a M01

Chiudere con:

> “Abbiamo una procedura. Come facciamo a scriverla in modo che un'altra persona possa eseguirla senza indovinare ciò che intendiamo?”

Questa domanda apre pseudocodice, decomposizione e trace di M01.

# M15 — Runbook docente

## Modulo

**Progettazione top-down e responsabilità**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo docente

Far progettare le funzioni **prima** di implementarle tutte. Lo studente deve imparare a riconoscere responsabilità, input/output e relazioni tra funzioni, senza trasformare la progettazione in burocrazia.

---

# Ritmo consigliato — settimana 15

## Ora teoria attiva 1 — decomposizione

### 0–15 min — problema completo

Presentare una specifica piccola ma non banale (ordine, prenotazione, tariffa).

### 15–30 min — responsabilità

Far proporre nomi di funzioni prima di scrivere codice.

### 30–45 min — firme

Definire parametri e return attesi.

### 45–55 min — smell

Mostrare una funzione che legge, calcola e stampa tutto e chiedere quali parti potrebbero essere testate separatamente.

---

# Ora teoria attiva 2 — contratti e call graph

## 0–20 min — contratto intuitivo

Per ogni funzione:

```text
input
vincoli
output
side effect sì/no
```

## 20–35 min — pre/post-condizioni

Solo linguaggio naturale, niente formalismo pesante.

## 35–50 min — call graph

Disegnare relazioni tra `main` e funzioni di logica.

## 50–55 min — piano di implementazione

Scegliere quale funzione piccola testare per prima.

---

# Ora laboratorio

## Fase A — decomposition cards

Raggruppare azioni della specifica in responsabilità.

## Fase B — firme

Scrivere soltanto `def`, parametri e breve contratto.

## Fase C — una funzione alla volta

Implementare la più piccola, provarla, poi integrare.

## Fase D — extract function

Partire da codice monolitico e isolare un calcolo coerente.

## Fase E — review con `git diff`

Se Git managed è disponibile, usare il diff per osservare esattamente il refactoring.

---

# Misconception watchlist

## M1 — top-down = scrivere tutto su carta e non provare mai

No: è una mappa iterativa. Progetto, provo una parte, aggiorno la mappa se serve.

## M2 — ogni riga deve diventare una funzione

No. La funzione deve rappresentare una responsabilità utile.

## M3 — funzione corta = funzione buona

Non esiste una soglia magica di righe.

## M4 — `main()` deve contenere tutta la logica

`main()` organizza il flusso; la logica testabile dovrebbe stare in funzioni dedicate quando ha senso.

## M5 — una funzione può leggere input e calcolare se “funziona”

Può funzionare, ma il corso chiede di ragionare su testabilità e separazione delle responsabilità.

---

# Differenziazione

## Recupero

- problema con 2 funzioni candidate;
- contratti già parzialmente compilati;
- call graph fornito da completare;
- una sola estrazione di funzione.

## Enrichment

- confrontare due decomposizioni plausibili;
- discutere funzione troppo generica vs troppo frammentata;
- progettare una variante con stessa logica ma input/output differenti;
- giustificare l'ordine di implementazione.

---

# Evidence docente

Raccogliere almeno:

- elenco responsabilità;
- 2–4 firme;
- un contratto intuitivo;
- call graph;
- un refactoring osservato tramite diff o confronto before/after.

---

# Git G1

M15 rende `git diff` pedagogicamente significativo: lo studente può verificare che un refactoring abbia cambiato struttura senza introdurre modifiche casuali.

Il corso Git resta separato. `add/commit` verranno formalizzati al Checkpoint A.

---

# Cosa NON anticipare

- architetture software formali;
- design pattern;
- dependency injection;
- package multi-file;
- docstring API complete;
- typing formale;
- pytest fixtures/mocking.

---

# Handoff a M16

M15 definisce contratti e casi.

M16 rende i casi eseguibili con `assert` e introduce il ciclo:

```text
bug → regression test → fix → tutti i test → refactor
```

# M15 — Runbook docente

## Modulo

**Progettazione top-down e responsabilità**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo docente

Far progettare le funzioni **prima** di implementarle tutte. Lo studente deve imparare a riconoscere responsabilità, input/output e relazioni tra funzioni, senza trasformare la progettazione in burocrazia.

Regola:

> il design deve ridurre il carico mentale del problema, non creare un secondo compito cartaceo parallelo al codice.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. individuare 2–4 responsabilità in un problema adeguato;
2. dare un nome alle funzioni candidate prima dei corpi;
3. proporre parametri e risultato atteso;
4. separare input/output dalla logica quando porta testabilità;
5. costruire un piccolo call graph;
6. implementare e verificare una funzione alla volta;
7. riconoscere una funzione che aggrega responsabilità non correlate.

## GUIDED EXPOSURE

- contratto intuitivo;
- termini pre-condizione/post-condizione in linguaggio naturale;
- `git diff` come lente sul refactoring/estrazione.

## ENRICHMENT / BACKUP

- confronto fra due decomposizioni plausibili;
- smell più sottili;
- contratti più ricchi;
- call graph più articolati.

---

# Regola anti-burocrazia

Per un esercizio piccolo non richiedere pagine di analisi.

Quando serve pianificare una funzione, può bastare:

```text
nome
responsabilità in una riga
parametri
return
2–4 casi
```

Per problemi più grandi aggiungere il call graph o una breve mappa delle responsabilità.

Non premiare la quantità di documentazione scollegata dalla qualità della decomposizione.

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

# Ora teoria attiva 2 — contratto e call graph

## 0–18 min — contratto intuitivo

Per una funzione:

```text
input
vincoli essenziali
output
side effect rilevante sì/no
```

Non richiedere questa scheda per funzioni ovvie di due righe: il contratto deve aiutare il ragionamento.

## 18–30 min — pre/post-condizioni

Usare soltanto linguaggio naturale:

```text
prima della chiamata deve essere vero...
dopo una chiamata corretta deve essere vero...
```

I termini sono guided exposure; l'obiettivo è chiarire i confini del comportamento.

## 30–45 min — call graph

Disegnare relazioni tra `main` e funzioni di logica.

## 45–55 min — piano di implementazione

Scegliere quale funzione piccola testare per prima e perché.

---

# Ora laboratorio

## Fase A — decomposition cards

Raggruppare azioni della specifica in responsabilità.

## Fase B — firme

Scrivere `def`, parametri, return atteso e una riga di responsabilità.

## Fase C — una funzione alla volta

Implementare la più piccola, provarla, poi integrare.

## Fase D — extract function

Partire da codice monolitico e isolare un calcolo coerente.

## Fase E — review con Git G1 Observe

Se il profilo managed è disponibile, riusare:

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
```

Prima e dopo il refactoring:

```text
git status
git diff
```

La spiegazione di working tree/diff resta nel corso Git canonico. Non trasformare questa fase in una seconda lezione Git.

---

# Minimum mastery gate — prima di M16

Considerare M15 consolidato quando lo studente riesce a:

- proporre 2–4 responsabilità sensate;
- scrivere firme con dati in ingresso e risultato atteso;
- separare un calcolo testabile dall'I/O in un caso semplice;
- disegnare un call graph piccolo;
- scegliere quale funzione implementare/testare per prima;
- estrarre una responsabilità coerente da codice monolitico;
- spiegare in una frase perché la decomposizione aiuta.

Non richiedere terminologia formale sulle pre/post-condizioni per superare il gate se il concetto è stato soltanto introdotto in forma guidata.

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

## M6 — più diagrammi/contratti = progettazione migliore

No. Ogni artefatto deve aiutare una decisione reale sul codice.

---

# Differenziazione

## Recupero

- problema con 2 funzioni candidate;
- contratti già parzialmente compilati;
- call graph fornito da completare;
- una sola estrazione di funzione.

## Enrichment

- due decomposizioni plausibili;
- funzione troppo generica vs troppo frammentata;
- stessa logica con input/output differenti;
- giustificare l'ordine di implementazione.

---

# Evidence docente

Raccogliere almeno:

- elenco responsabilità;
- 2–4 firme;
- breve contratto quando utile;
- call graph;
- un refactoring osservato tramite `git diff` o confronto before/after.

---

# Git G1 boundary

M15 rende `git diff` pedagogicamente significativo ma non aggiunge nuovi outcome Git rispetto a M14. La dipendenza machine-readable resta `config/git-g1-consumer.json`.

`add`, `diff --staged`, `commit`, `log/show` arrivano al Checkpoint A attraverso il consumer embedded G1, non tramite materiale duplicato in Python.

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

M15 definisce responsabilità, contratti e casi.

M16 rende i casi eseguibili con `assert` e introduce il ciclo:

```text
bug → regression test → fix → tutti i test → refactor
```

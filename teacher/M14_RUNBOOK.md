# M14 — Runbook docente

## Modulo

**Scope locale, passaggio dei dati e composizione**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo docente

Far emergere il principio:

> una funzione dovrebbe ricevere esplicitamente ciò che le serve e restituire ciò che produce.

Il focus non è LEGB. È costruire un modello beginner corretto di nomi locali, dipendenze esplicite e composizione.

---

# Ritmo consigliato — settimana 14

## Ora teoria attiva 1 — nomi locali e dipendenze

### 0–15 min — locale

Usare `doppio(numero)` e chiedere dove esistono `numero` e `risultato`.

### 15–30 min — locale fuori funzione

Mostrare un `NameError` dovuto a uso esterno di un nome locale.

### 30–45 min — dipendenza globale

Confrontare funzione che usa `prezzo` globale con funzione che lo riceve come parametro.

### 45–55 min — costanti vs dati di lavoro

Distinguere una costante di dominio da stato di lavoro modificabile.

---

# Ora teoria attiva 2 — composizione e call graph

## 0–20 min — composizione

`area_rettangolo` → `costo_pittura` con variabile intermedia.

## 20–35 min — call graph

Disegnare a mano:

```text
main
├─ area_rettangolo
└─ costo_pittura
```

## 35–50 min — flusso dati

Far annotare input/output di ogni funzione e frecce tra risultati e parametri.

## 50–55 min — Git G1

Se il workflow managed è disponibile:

```text
git status
git diff
```

per osservare il refactoring, senza aprire il corso Git completo.

---

# Ora laboratorio

## Fase A — scope trace

Per ogni nome, indicare:

- dove nasce;
- dove può essere usato;
- come il risultato esce dalla funzione.

## Fase B — remove global

Refactoring controllato: sostituire una dipendenza globale con parametro/return.

Prima e dopo il refactoring, usare gli stessi casi di test.

## Fase C — compose

Costruire 2–3 funzioni che collaborano tramite variabili intermedie.

## Fase D — debug

- locale fuori scope;
- parametro mancante;
- risultato ignorato;
- globale nascosta;
- chiamata annidata illeggibile.

---

# Misconception watchlist

## M1 — tutte le variabili del file sono visibili ovunque

Correzione: trace di una variabile locale e tentativo di accesso esterno.

## M2 — usare globali evita parametri quindi è più semplice

Mostrare come il contratto diventa meno visibile e i test dipendono dallo stato esterno.

## M3 — nessuna globale è mai ammessa

Non trasformare il principio in dogma. Distinguere costante/configurazione da dato di lavoro.

## M4 — composizione = annidare tutte le chiamate in una riga

Le variabili intermedie possono rendere il flusso più chiaro.

## M5 — due chiamate condividono le variabili locali

Far eseguire due call trace con argomenti diversi.

---

# Differenziazione

## Recupero

- una funzione alla volta;
- call graph con massimo 2 funzioni;
- variabili intermedie obbligatorie;
- firma semplice con 1–2 parametri;
- niente costanti/globali nel primo esercizio.

## Enrichment

- confrontare composizione diretta vs variabili intermedie;
- riconoscere una costante di dominio sensata;
- piccolo call graph a tre livelli;
- discutere quando una funzione dipende da troppe informazioni esterne.

---

# Evidence docente

Raccogliere almeno:

- scope trace;
- refactoring globale→parametro;
- due funzioni composte;
- call graph semplice;
- `git diff` del refactoring se Git managed è disponibile.

---

# P2 TheBitLab

Il profilo `2cornot2c#756` dovrà testare il comportamento della funzione, non il modo in cui lo studente ha scritto la firma oltre il contratto dichiarato.

Fino alla certificazione:

- test manuali/assert formativi;
- nessun fake P2;
- nessun parsing fragile del sorgente.

---

# Git G1 — qui iniziano a servire le dispense

M14 è il primo punto in cui il workflow Git entra davvero nel corso Python tramite `status` e `diff` per osservare un refactoring.

Il materiale Git canonico deve però restare separato. Prima di produrre il micro-modulo G1 definitivo (`status`, `diff`, poi `add/commit` al Checkpoint A) è utile auditare le dispense Git del docente.

---

# Cosa NON anticipare

- LEGB formale;
- `global`/`nonlocal` come strumenti da usare;
- closure;
- moduli/package;
- dependency injection formale;
- classi;
- pytest.

---

# Handoff a M15

M14 ha reso esplicito il flusso dei dati.

M15 cambia scala:

> prima di scrivere le funzioni, come decido quali responsabilità esistono e come collaborano?

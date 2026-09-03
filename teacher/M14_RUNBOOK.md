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

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. riconoscere parametri e variabili locali alla chiamata;
2. capire che un nome locale non è disponibile fuori dalla funzione;
3. passare esplicitamente i dati necessari;
4. riconoscere una dipendenza nascosta da stato globale di lavoro;
5. usare il valore restituito da una funzione come dato per un'altra;
6. seguire il flusso con variabili intermedie;
7. leggere un call graph semplice.

## GUIDED EXPOSURE

- costante di dominio a livello modulo vs dato di lavoro globale;
- `G1.OBSERVE.STATUS` / `G1.OBSERVE.DIFF` per osservare un refactoring.

## ENRICHMENT / BACKUP

- call graph a tre livelli;
- confronto composizione compatta vs variabili intermedie;
- dipendenze esterne più articolate.

Git è un outcome G1 guidato e non deve togliere tempo al mastery Python del modulo.

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

Distinguere una costante di dominio da stato di lavoro modificabile. Questa distinzione è guided exposure: non aprire LEGB, moduli o configurazione avanzata.

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

## 50–55 min — Git G1 Observe

Da M14 il corso Python consuma due outcome G1 canonici a livello **guided**:

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
```

Usare il materiale del corso `TheBitPoets/git` come source/remediation:

```text
G1-M02 — working tree / status
G1-M03 — diff
```

Nel workspace Python l'istruzione contestuale resta breve:

```text
git status
git diff
```

per osservare il refactoring. Non ricreare qui una mini-lesson Git e non richiedere il completamento del track G1 standalone.

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

Se resta tempo e il profilo managed è disponibile, osservare la modifica con `status/diff`.

---

# Minimum mastery gate — prima di M15

Considerare M14 consolidato quando lo studente riesce a:

- indicare quali nomi sono locali a una funzione;
- spiegare perché un locale non è disponibile fuori;
- rimuovere una semplice dipendenza globale passando il dato come parametro;
- comporre due funzioni tramite un valore restituito;
- usare una variabile intermedia per rendere visibile il flusso;
- leggere/disegnare un call graph di 2–3 funzioni.

La distinzione fine costante/configurazione e il workflow Git non devono diventare criteri principali del gate Python.

---

# Misconception watchlist

## M1 — tutte le variabili del file sono visibili ovunque

Correzione: trace di una variabile locale e tentativo di accesso esterno.

## M2 — usare globali evita parametri quindi è più semplice

Mostrare come il contratto diventa meno visibile e i test dipendono dallo stato esterno.

## M3 — nessuna globale è mai ammessa

Non trasformare il principio in dogma. Distinguere, come exposure, costante/configurazione da dato di lavoro.

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

- composizione diretta vs variabili intermedie;
- costante di dominio sensata;
- call graph a tre livelli;
- funzione che dipende da troppe informazioni esterne.

---

# Evidence docente

Raccogliere almeno:

- scope trace;
- refactoring globale→parametro;
- due funzioni composte;
- call graph semplice;
- opzionalmente `git status`/`git diff` del refactoring se il profilo managed è disponibile.

---

# P2 TheBitLab

Il profilo `2cornot2c#756` dovrà testare il comportamento della funzione. Questa è una concern docente/piattaforma, non un outcome da studente.

Fino alla certificazione:

- test manuali/assert formativi;
- nessun fake P2;
- nessun parsing fragile del sorgente.

---

# Git G1 boundary

La dipendenza è dichiarata in `config/git-g1-consumer.json` e il design completo in `tracks/secondo/GIT_G1_INTEGRATION.md`.

M14 non insegna staging, commit o history: prepara soltanto l'osservazione dello stato e del cambiamento. `add/commit/log` arrivano al Checkpoint A tramite il corso Git canonico.

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

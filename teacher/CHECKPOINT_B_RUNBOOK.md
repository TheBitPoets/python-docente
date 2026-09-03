# Checkpoint B — Runbook docente

## Funzione

Settimana 24: consolidamento e recupero di stringhe/liste/tuple, mini-project e preparazione alla prova V3.

Non introduce nuovi prerequisiti e **non deve forzare l'uso contemporaneo di tutte le strutture studiate**.

Il checkpoint misura soprattutto:

```text
modello mentale
→ scelta della struttura/operazione
→ mutabilità consapevole
→ funzioni/test/debug
```

---

# Outcome raggruppati

## A — Sequenze testuali

Verificare:

- `str` come sequenza immutabile;
- indici/slicing;
- normalizzazione motivata;
- algoritmo testuale con loop/funzione;
- casi limite.

## B — Mutabilità e riferimenti

Verificare:

- `list` mutabile;
- metodo mutante vs nuovo valore;
- alias vs copia;
- contratto di mutazione/non-mutazione;
- filtro sicuro.

## C — Operazioni sulle liste

Verificare:

- costruzione progressiva con `append`;
- iterazione appropriata;
- `sort()` vs `sorted()`;
- uso di altre API soltanto se realmente svolte e pertinenti.

## D — Modello dati

Verificare:

- tuple/unpacking;
- list vs tuple;
- lista di liste;
- row aliasing;
- scelta motivata della struttura.

## E — Metodo

Continuano a contare:

- funzioni;
- trace;
- casi/assert;
- debug;
- spiegazione.

---

# Mini-project

Richiedere un problema piccolo con:

```text
analisi
→ modello dati
→ 2–4 funzioni
→ implementazione
→ assert/casi limite
→ breve motivazione
```

Il dominio decide quali strutture servono.

Non richiedere artificialmente:

```text
stringa + lista + tuple + matrice
```

nello stesso progetto solo per copertura.

Rubriche prioritarie:

- correttezza;
- modello dati;
- mutabilità gestita consapevolmente;
- decomposizione;
- test;
- spiegazione.

La quantità di feature usate non è un criterio di qualità.

---

# Recovery

Priorità:

1. indice/slicing e immutabilità;
2. mutabilità list + `append`/`None`;
3. alias/copia;
4. modifica durante iterazione;
5. list vs tuple;
6. matrice/lista di liste e righe condivise.

Non introdurre set/dict se aliasing e mutabilità sono ancora completamente instabili: usare il checkpoint come buffer previsto dal freeze.

Dettagli guided/enrichment non devono bloccare il recupero del core.

---

# Preparazione V3

V3 è teorico/scritta e può essere collocata tra fine settimana 24 e inizio 25 secondo calendario reale.

Evidenze candidate:

- trace;
- previsione output/errore;
- alias diagram;
- scelta struttura;
- debug;
- spiegazione mutazione vs nuovo valore.

Non inserire automaticamente in prova ogni API vista come exposure/enrichment (`insert`, `casefold`, nested tuple mutabili, ecc.).

---

# `friedpython`

L'audit specifico è `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.

Nessun esercizio legacy viene importato automaticamente. Eventuali Activity devono essere riscritte con:

```text
outcome preciso
→ Python 3.12-compatible
→ casi limite
→ starter/solution separati
→ provenance
```

---

# Git — riuso G1, nessun G2

Checkpoint B non introduce nuovi outcome Git.

Se il mini-project usa Git, riusare il workflow G1 già acquisito:

```text
git status
→ git diff
→ test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log / git show
```

Git resta evidence di processo nel lavoro Python.

Non abbreviare il modello in:

```text
status → diff → commit
```

perché perderebbe proprio il passaggio Working Tree → Index → History introdotto al Checkpoint A.

Nessun comando G2 nuovo.

---

# Handoff a PY2-08

Dopo il checkpoint entra il criterio di scelta delle strutture:

```text
unicità/membership dominante → set candidato
lookup chiave→valore          → dict candidato
sequenza ordinata/mutabile    → list
record stabile posizionale    → tuple
```

L'obiettivo non sarà imparare collezioni “sempre più avanzate”, ma scegliere la struttura coerente con le operazioni dominanti del dominio.

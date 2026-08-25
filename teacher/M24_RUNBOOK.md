# M24 — Runbook docente

## Modulo

**Dizionari: chiave→valore, lookup e frequenze**  
UDA PY2-08 — Set, dizionari e modellazione dei dati

Stato: draft editoriale controllato.

## Obiettivo docente

Far emergere il cambio di modello:

```text
list → posizione
set  → appartenenza/unicità
dict → chiave → valore
```

Il corso deve evitare due errori opposti:

- usare dict come “lista con nomi” senza capire il lookup;
- usare `get()` ovunque nascondendo chiavi che invece dovrebbero esistere.

## Ora teoria attiva 1

1. Mapping chiave→valore.
2. Creazione, lookup, inserimento/aggiornamento.
3. `KeyError` come informazione.
4. Membership sulle chiavi.
5. `[]` vs `get()` in base al contratto.

## Ora teoria attiva 2

1. Iterazione: chiavi vs `items()`.
2. `keys/values/items` come view.
3. Nota moderna sull'ordine di inserimento.
4. Pattern frequenze con `get(k, 0) + 1`.
5. Confronto vecchio modello ASCII-256 vs dict Unicode-friendly.

## Laboratorio

- mapping microscope;
- inventario/voti semplici;
- required-vs-optional key;
- frequenze caratteri;
- Debug Clinic su KeyError/default/views/chiave sbagliata;
- confronto strutturale lista indicizzata vs dict.

## Misconception watchlist

- `get` sempre più sicuro di `[]`;
- `in d` cerca nei valori;
- `keys()` è una lista;
- ordine di dict “casuale” come nelle vecchie note;
- dict usato con indici numerici artificiali quando una lista sarebbe il modello naturale;
- lista mutabile usata come chiave.

## Differenziazione

### Recupero

- dict piccoli `str→int`;
- una sola operazione per esercizio;
- membership prima di `get`/KeyError;
- frequenze su parole corte.

### Enrichment

- `setdefault` dopo il pattern frequenze;
- tuple key `(r,c)`;
- matrice sparsa come confronto;
- ordine di inserimento vs ordinamento esplicito.

## Evidence docente

Raccogliere:

- lookup/aggiornamento;
- scelta `[]`/`get` motivata;
- iterazione `items()`;
- funzione frequenze;
- spiegazione perché dict supera il modello ASCII-256.

## Friedpython

Audit canonico: `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

Da correggere prima di riuso:

- note sull'ordine non più attuali;
- descrizione di `keys()` non precisa per Python 3 moderno;
- esempi/output storici.

Esercizio frequenze è un ottimo spunto, ma va riscritto come materiale originale.

## Cosa NON anticipare

- defaultdict/Counter come core;
- internals hash table;
- JSON come persistenza;
- ORM/database;
- dict comprehension come prerequisito.

## Handoff a M25

M24 introduce lookup e frequenze.
M25 chiede:

> come combino strutture diverse e quale modello rende più naturali le operazioni del problema?

# M23 — Runbook docente

## Modulo

**Set: unicità, membership e operazioni insiemistiche**  
UDA PY2-08 — Set, dizionari e modellazione dei dati

Stato: draft editoriale controllato.

## Obiettivo docente

Far percepire il `set` come un **modello dati diverso**, non come una lista a cui Python toglie i duplicati.

Domande guida:

```text
l'ordine conta?
i duplicati contano?
la domanda dominante è membership?
servono unione/intersezione/differenza?
```

## Ora teoria attiva 1

1. `{}` vs `set()`.
2. Unicità.
3. Membership.
4. `add`, `remove`, `discard`.
5. Set vs list da specifiche brevi.

## Ora teoria attiva 2

1. Unione/intersezione/differenza.
2. Problemi con gruppi/tag/iscrizioni.
3. Hashability beginner.
4. Perché non usare indice/slicing.
5. Perché non fare affidamento sull'ordine del set.

## Laboratorio

- set microscope;
- deduplicazione con discussione sull'ordine;
- problemi insiemistici;
- scelta list/set motivata;
- Debug Clinic su `{}`, remove/discard, ordine e valori non hashable.

## Misconception watchlist

- `{}` = set vuoto;
- set = lista senza duplicati;
- iterazione del set come ordine significativo;
- `remove` e `discard` sinonimi;
- list dentro set ammessa;
- conversione a set usata quando l'ordine della prima occorrenza è requisito.

## Differenziazione

### Recupero

- set piccoli di stringhe/interi;
- Venn diagram su carta;
- una operazione insiemistica alla volta;
- nessuna tuple-key finché il set base non è stabile.

### Enrichment

- symmetric difference;
- subset/superset;
- tuple hashable come elemento;
- confronto membership list/set solo qualitativo.

## Evidence docente

Raccogliere:

- creazione set corretta;
- una scelta list/set;
- unione/intersezione/differenza;
- debug `{}` o ordine;
- spiegazione di hashability a livello beginner.

## Cosa NON anticipare

- frozenset come core;
- internals hash table;
- Big-O formale;
- dict prima che set/unicità sia compreso.

## Handoff a M24

Il set risponde bene a:

> il valore appartiene?

Il dict introduce una domanda nuova:

> data una chiave, quale valore le è associato?

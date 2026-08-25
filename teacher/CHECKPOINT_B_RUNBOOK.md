# Checkpoint B — Runbook docente

## Funzione

Settimana 24: consolidamento e recupero di stringhe/liste/tuple, mini-project e preparazione alla prova V3.

Non introduce nuovi prerequisiti.

## Outcome

Verificare:

1. `str` come sequenza immutabile;
2. indici/slicing/metodi/normalizzazione;
3. algoritmi testuali con funzioni;
4. liste e metodi mutanti;
5. alias vs copia;
6. contratto di mutazione/non-mutazione;
7. filtraggio/ordinamento;
8. tuple/unpacking;
9. list vs tuple;
10. matrici/liste annidate e row aliasing.

## Mini-project

Richiedere un problema tabellare piccolo con:

```text
analisi
→ modello dati
→ funzioni
→ implementazione
→ assert/casi limite
→ breve motivazione
```

Rubriche prioritarie:

- correttezza;
- modello dati;
- mutabilità gestita consapevolmente;
- decomposizione;
- test;
- spiegazione.

## Recovery

Priorità:

1. indice/slicing;
2. metodi mutanti e `None`;
3. alias/copia;
4. modifica durante iterazione;
5. tuple/list choice;
6. matrici e righe condivise.

Non introdurre set/dict se aliasing e mutabilità sono ancora completamente instabili: usare il checkpoint come buffer previsto dal freeze.

## Preparazione V3

V3 è teorico/scritta e può essere collocata tra fine settimana 24 e inizio 25 secondo calendario reale.

Evidenze candidate:

- trace;
- previsione output/errore;
- alias diagram;
- scelta struttura;
- debug;
- spiegazione di mutazione vs nuovo valore.

## `friedpython`

L'audit specifico è `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.

Nessun esercizio legacy viene importato automaticamente. Eventuali Activity devono essere riscritte con Python 3.12-compatible, casi limite e separazione student/teacher.

## Git

Continuare il workflow G1 già introdotto:

```text
status → diff → test → add/commit quando il lavoro è significativo
```

Nessun comando G2 nuovo.

## Handoff a PY2-08

Dopo il checkpoint entra il criterio di scelta delle strutture:

```text
unicità/membership dominante → set candidato
lookup chiave→valore → dict candidato
sequenza ordinata/mutabile → list
record stabile posizionale → tuple
```

L'obiettivo non sarà imparare quattro collezioni separate, ma scegliere la struttura coerente con le operazioni del dominio.

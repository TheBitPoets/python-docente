# M25 — Runbook docente

## Modulo

**Strutture combinate e scelta del modello dati**  
UDA PY2-08 — Set, dizionari e modellazione dei dati

Stato: draft editoriale controllato.

## Obiettivo docente

Portare la classe da:

```text
conosco list/tuple/set/dict
```

verso:

```text
riconosco le operazioni dominanti
→ scelgo il modello
→ motivo la scelta
```

È un modulo di design, non un catalogo di nesting.

## Ora teoria attiva 1 — confronto modelli

1. Mappa `str/list/tuple/set/dict`.
2. Liste parallele come smell.
3. Lista di tuple vs lista di dict.
4. Dict indicizzato per identità.
5. Ordine/duplicati/lookup come criteri.

## Ora teoria attiva 2 — strutture combinate

1. Dict di liste per raggruppamento.
2. Dict di set per relazione uno→molti con unicità.
3. Esercizio legacy frequenza→lista come spunto.
4. Annidamento con significato vs profondità gratuita.
5. Bridge record/dict → classe futura.

## Laboratorio

- data-model choice cards;
- refactoring liste parallele;
- group-by con dict di liste;
- dict di set per iscrizioni/tag;
- mini-project con due strutture combinate;
- spiegazione scritta delle operazioni dominanti.

## Misconception watchlist

- dict scelto sempre perché “più potente”;
- set usato perdendo ordine/duplicati richiesti;
- tuple usata per record con molti campi poco leggibili;
- nesting profondo considerato sofisticazione;
- ordine di inserimento del dict confuso con semantica posizionale;
- default usato per nascondere dato obbligatorio.

## Differenziazione

### Recupero

- scegliere tra due sole strutture candidate;
- record con 2 campi;
- dict di liste già schematizzato;
- tabella criteri ordine/unicità/lookup.

### Enrichment

- matrice sparsa con tuple-key;
- setdefault dopo pattern esplicito;
- confrontare lista di dict vs dict di dict;
- discutere costo qualitativo di scansione vs lookup.

## Evidence docente

Raccogliere:

- almeno 3 scelte struttura motivate;
- refactoring liste parallele;
- una struttura combinata;
- mini call/data model diagram;
- spiegazione del ponte record→oggetto.

## Friedpython

Audit: `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

Esercizi 5–6 sono buoni spunti per frequenze e dict di liste, ma vanno riscritti. Le vecchie note su ordine/keys non vanno propagate.

## Cosa NON anticipare

- dataclass/classi;
- defaultdict/Counter come core;
- database/ORM;
- JSON persistence;
- generics/type hints avanzati.

## Exit checkpoint PY2-08

Verificare:

1. set/unicità/membership;
2. dict/lookup;
3. chiavi mancanti;
4. frequenze;
5. items/views;
6. scelta str/list/tuple/set/dict;
7. strutture combinate;
8. operazioni dominanti e motivazione.

## Handoff a PY2-09

Il modello dati ora è abbastanza ricco. M26 aggiunge soltanto il confine minimo di persistenza:

```text
workspace path
→ file testo UTF-8
→ with/open
→ errori esterni prevedibili
```

senza sottrarre tempo all'OOP.

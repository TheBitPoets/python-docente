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

---

# Priorità didattica

## MUST MASTER

1. spiegare che il set rappresenta valori distinti e non una sequenza indicizzata;
2. creare un set e un set vuoto con `set()`;
3. sapere che `{}` crea un dict vuoto;
4. usare membership `in/not in`;
5. aggiungere con `add()`;
6. usare unione/intersezione/differenza in problemi naturali;
7. scegliere `set` vs `list` in base a ordine, duplicati e membership;
8. non dipendere da indici/posizioni del set.

## GUIDED EXPOSURE

- `remove()` vs `discard()`;
- concetto beginner di elemento hashable;
- deduplicazione `set(lista)` con discussione sull'eventuale perdita di informazione d'ordine.

## ENRICHMENT / BACKUP

- symmetric difference;
- subset/superset;
- tuple hashable come elemento;
- confronto qualitativo membership list/set.

Hashability deve impedire errori concettuali, non aprire un mini-corso sugli hash table.

---

# Ora teoria attiva 1 — semantica del set

1. `{}` vs `set()` come Error Clinic breve.
2. Unicità con esempi concreti.
3. Membership come domanda naturale.
4. `add()` come mutazione core.
5. Scelte list/set da specifiche brevi.

Solo se la semantica è stabile, mostrare `remove/discard` come guided exposure legato al contratto.

---

# Ora teoria attiva 2 — operazioni insiemistiche

1. Unione su gruppi/tag.
2. Intersezione su appartenenza comune.
3. Differenza con attenzione all'ordine degli operandi.
4. Confronto list vs set.
5. Nota breve: non fare affidamento su posizione/indice/ordine come proprietà del modello set.

Hashability compare alla fine come spiegazione di un errore concreto, non come teoria autonoma.

---

# Laboratorio

- set microscope;
- deduplicazione con discussione sull'ordine;
- problemi insiemistici;
- scelta list/set motivata;
- Debug Clinic su `{}`, ordine e uso dell'indice;
- `remove/discard` soltanto come variante guidata se realmente svolti.

---

# Minimum mastery gate — prima di M24

Considerare M23 consolidato quando lo studente riesce a:

- creare correttamente un set vuoto/non vuoto;
- spiegare unicità e membership;
- usare `add()`;
- calcolare/interpretare unione, intersezione e differenza in casi semplici;
- scegliere list/set e motivarlo;
- spiegare perché indice/slicing non appartengono al modello set;
- riconoscere che convertire a set può perdere informazione importante se ordine/duplicati erano requisiti.

`remove/discard`, tuple hashable e symmetric difference non devono dominare il gate.

---

# Misconception watchlist

- `{}` = set vuoto;
- set = lista senza duplicati;
- ordine di iterazione usato come dato significativo;
- `remove` e `discard` trattati come un nuovo blocco da memorizzare;
- list dentro set usata senza capire l'errore;
- conversione a set quando l'ordine della prima occorrenza è requisito.

---

# Differenziazione

## Recupero

- set piccoli di stringhe/interi;
- Venn diagram su carta;
- una operazione insiemistica alla volta;
- scelta list/set con tabella ordine/duplicati/membership.

## Enrichment

- symmetric difference;
- subset/superset;
- tuple hashable;
- confronto membership list/set solo qualitativo.

---

# Evidence docente

Raccogliere:

- creazione set corretta;
- una scelta list/set;
- unione/intersezione/differenza;
- debug `{}` o uso improprio dell'ordine;
- spiegazione del modello “valori distinti + appartenenza”.

Hashability può essere evidence solo se realmente approfondita.

---

# Cosa NON anticipare

- frozenset come core;
- internals hash table;
- Big-O formale;
- dict prima che set/unicità sia compreso.

---

# Handoff a M24

Il set risponde bene a:

> il valore appartiene?

Il dict introduce una domanda nuova:

> data una chiave, quale valore le è associato?

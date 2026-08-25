# M20 — Runbook docente

## Modulo

**Liste: mutabilità, metodi essenziali e iterazione**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Usare il contrasto con `str` per introdurre la mutabilità senza presentare le liste come un catalogo di metodi.

Modello target:

```text
nome → oggetto list mutabile
operazione mutante → cambia quell'oggetto
```

## Ora teoria attiva 1

1. `str` vs `list`.
2. Creazione, indice, slicing.
3. Mutazione per indice.
4. `append` e bug `lista = lista.append(x)`.
5. `append` vs `extend` con prediction della struttura risultante.

## Ora teoria attiva 2

1. `insert`, `remove`, `pop`.
2. Valore vs posizione.
3. `for` diretto vs indice.
4. `enumerate` quando servono entrambi.
5. Membership `in`.

## Laboratorio

- prediction di sequenze di mutazioni;
- scelta del metodo dalla specifica;
- costruzione lista da N input;
- confronto esercizi legacy `while+indice` vs `for` diretto;
- Debug Clinic su `None`, indice, remove/pop, append/extend.

## Misconception watchlist

- lista come “stringa con parentesi”;
- metodi mutanti pensati come funzioni che restituiscono la lista;
- `append` e `extend` considerati sinonimi;
- `remove` usato con un indice;
- indice usato sempre perché sembra più tecnico;
- slice interpretato come vista live invece di nuova lista superficiale.

## Differenziazione

### Recupero

- liste di 3–5 valori;
- un metodo alla volta;
- prediction prima dell'esecuzione;
- `for` diretto prima di `enumerate`.

### Enrichment

- slice assignment controllato;
- confronto concatenazione vs `extend`;
- progettare un caso in cui `insert` è realmente giustificato.

## Evidence docente

Raccogliere:

- prediction di una mutazione;
- spiegazione `append`/`extend`;
- debug `lista = lista.append(...)`;
- iterazione scelta e motivata;
- costruzione progressiva di lista.

## Friedpython

Usare soltanto come source pack auditato. Gli esercizi 1–2 sono buoni per il confronto tra indice e iterazione diretta; non importare automaticamente codice/commenti legacy.

## Cosa NON anticipare

- aliasing profondo prima di M21;
- comprehensions come forma primaria;
- set/dict;
- type hints generici;
- NumPy.

## Handoff a M21

M20 mostra che la lista può cambiare.
M21 risponde:

> se due nomi indicano la stessa lista, chi vede la mutazione? E quando ho davvero creato una copia?

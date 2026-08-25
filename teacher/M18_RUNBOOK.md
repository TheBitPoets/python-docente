# M18 — Runbook docente

## Modulo

**Ricerca, membership, metodi e normalizzazione delle stringhe**  
UDA PY2-06 — Stringhe come sequenze e testo

Stato: draft editoriale controllato.

## Obiettivo docente

Far scegliere l'operazione in base alla domanda, non in base al metodo appena imparato:

```text
esistenza? → in
posizione? → find
conteggio? → count quando coincide col requisito
trasformazione? → metodo str
algoritmo didattico? → loop esplicito
```

## Ora teoria attiva 1

1. Membership `in/not in`.
2. `find()` e valore `-1`.
3. Error Clinic su `if testo.find(...)`.
4. `count()` e differenza tra obiettivo algoritmico e uso di un metodo standard.

## Ora teoria attiva 2

1. Immutabilità dei metodi stringa.
2. `lower/upper`, `strip`, `replace`, `startswith/endswith`.
3. Normalizzazione come scelta del requisito.
4. Confronto loop manuale vs metodo built-in.

## Laboratorio

- choose-the-operation;
- confronto case-sensitive vs normalizzato;
- validator semplice;
- debug `find`, `strip`, risultato metodo ignorato;
- funzione `conta_vocali` come esercizio algoritmico.

## Misconception watchlist

- `find()` interpretato come booleano;
- metodi pensati come mutanti;
- `strip(chars)` interpretato come rimozione di una sottostringa;
- normalizzare tutto automaticamente;
- credere che built-in o loop manuale siano sempre superiori.

## Differenziazione

### Recupero

- una sola operazione per esercizio;
- confronto diretto `in` vs `find`;
- stringhe brevi;
- variabile separata per il risultato del metodo.

### Enrichment

- `casefold()` come nota controllata;
- più normalizzazioni confrontate;
- spiegare perché una normalizzazione perde informazione;
- confronto tra loop e metodo con stesso contratto.

## Evidence docente

Raccogliere:

- scelta corretta `in/find`;
- un debug `find()`;
- una trasformazione con nuovo valore;
- una normalizzazione motivata;
- una scelta metodo vs loop spiegata.

## `friedpython`

Il materiale legacy resta fonte di gap-check. Non importare esercizi fino all'audit individuale e alla rimozione dei residui Python 2.

## P2

Le funzioni testuali pure sono candidate naturali al profilo `2cornot2c#756`; fino alla certificazione usare `assert`/manual evidence.

## Cosa NON anticipare

- regex;
- liste come struttura già padroneggiata;
- comprehension;
- bytes/encoding;
- ottimizzazioni stringa avanzate.

## Handoff a M19

M18 conosce gli strumenti standard. M19 li combina con cicli/funzioni per costruire algoritmi di testo, validatori e parsing semplice.

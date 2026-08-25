# M22 — Runbook docente

## Modulo

**Tuple, unpacking, liste annidate e matrici**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Chiudere l'UDA facendo usare la mutabilità/aliasing in un modello dati più ricco:

```text
list vs tuple
→ packing/unpacking
→ liste annidate
→ matrici
→ alias delle righe
```

## Ora teoria attiva 1 — tuple e scelta struttura

1. Tuple come sequenze ordinate immutabili.
2. `(x,)` e ruolo della virgola.
3. Packing/unpacking.
4. Rilettura di `enumerate()`.
5. Casi list vs tuple motivati dal dominio.

Enrichment controllato: tupla che contiene una lista mutabile, soltanto dopo il modello base.

## Ora teoria attiva 2 — matrici

1. Lista di liste e accesso `[riga][colonna]`.
2. Attraversamento per valore e per coordinate.
3. Riutilizzo di M12 `R × C`.
4. Totale per riga con reset al livello corretto.
5. Alias trap `[[0] * C] * R`.
6. Righe irregolari e limiti derivati da `len(matrice[r])`.

## Laboratorio

- scelta list/tuple;
- unpacking di coordinate;
- matrice piccola con somma per riga;
- ricerca di valore + posizione;
- Debug Clinic su righe condivise;
- mini-project tabellare con funzioni/test.

## Misconception watchlist

- parentesi = tuple anche senza virgola;
- tuple scelte “per velocità” invece che per modello dati;
- immutabilità della tuple trasferita magicamente agli oggetti interni;
- confusione riga/colonna;
- costruzione `[[0]*C]*R` considerata righe indipendenti;
- ogni lista di liste considerata matrice rettangolare.

## Differenziazione

### Recupero

- coordinate `(x, y)`;
- matrici 2×3;
- attraversamento per valore prima degli indici;
- diagramma delle righe come oggetti separati.

### Enrichment

- lista di tuple;
- tuple contenente lista;
- righe irregolari;
- comprehension di costruzione solo dopo aver compreso il bug alias;
- massimo/somma per riga.

## Evidence docente

Raccogliere:

- scelta list/tuple motivata;
- unpacking;
- trace matrice;
- debug alias righe;
- funzione su dati tabellari.

## Friedpython

Il materiale tuple legacy è solo riferimento:

- riusare concetti di immutabilità/conversione/unpacking dopo riscrittura;
- non copiare sintassi Python 2 `print T`;
- non introdurre comprehension prima del loop equivalente.

## Cosa NON anticipare

- NumPy;
- dataclass/NamedTuple come core;
- generics/type hints avanzati;
- deep copy come requisito;
- matrici sparse/dict: arriveranno dopo i dizionari.

## Exit checkpoint PY2-07

Verificare:

1. mutabilità liste;
2. metodi mutanti/None;
3. alias/copia;
4. filtraggio sicuro;
5. sort/sorted;
6. tuple/unpacking;
7. list vs tuple;
8. lista di liste;
9. alias righe;
10. struttura scelta e motivata.

## Handoff al Checkpoint B

Il checkpoint consolida **stringhe + liste + tuple** prima di introdurre strutture con semantiche diverse: set per unicità/membership e dict per mapping chiave→valore.

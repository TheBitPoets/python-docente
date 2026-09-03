# M22 — Runbook docente

## Modulo

**Tuple, unpacking, liste annidate e matrici**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Chiudere l'UDA riusando concetti già acquisiti:

```text
str immutabile
→ list mutabile
→ alias/copia
→ tuple come sequenza stabile
→ liste annidate come dati tabellari
→ M12 ritorna sui dati reali
```

Il modulo non deve sembrare due corsi separati “tuple” + “matrici”: entrambi servono a scegliere e attraversare strutture coerenti col dominio.

---

# Priorità didattica

## MUST MASTER

1. riconoscere una `tuple` come sequenza ordinata immutabile;
2. usare unpacking semplice;
3. scegliere intuitivamente `list` vs `tuple` dal significato dei dati;
4. creare/leggere una lista di liste;
5. usare accesso `[riga][colonna]`;
6. attraversare dati tabellari per valore o coordinate quando serve;
7. riusare M12 `R×C` e M11 sul reset dello stato per riga;
8. diagnosticare il bug di righe condivise in `[[0] * C] * R`;
9. motivare la struttura scelta.

## GUIDED EXPOSURE

- tupla a un elemento `(x,)`;
- packing senza parentesi;
- `enumerate()` riletto come coppie/unpacking;
- righe irregolari e `len(matrice[r])`.

## ENRICHMENT / BACKUP

- tuple che contengono oggetti mutabili;
- comprehension per costruire righe indipendenti;
- strutture miste/lista di tuple più articolate.

Il nested mutable dentro tuple non è prerequisito del modello list-vs-tuple.

---

# Ora teoria attiva 1 — tuple e scelta struttura

1. Partire da coordinate `(x, y)`.
2. Confrontare con una lista che deve crescere/modificarsi.
3. Unpacking semplice.
4. Scelta list/tuple su 4–5 domini.
5. Mostrare `(x,)` soltanto come guided detail, non come trappola da verifica dominante.

Domanda guida:

> questi valori rappresentano una collezione che deve cambiare o un raggruppamento posizionale stabile?

---

# Ora teoria attiva 2 — liste annidate e matrici

1. Lista di righe e `[riga][colonna]`.
2. Attraversamento per valore.
3. Attraversamento per coordinate solo quando la posizione serve.
4. Richiamo M12 `R×C`.
5. Totale per riga: reset al livello corretto.
6. Alias trap `[[0] * C] * R` come riuso diretto del modello M21.

Le righe irregolari sono guided exposure se il core rettangolare non è ancora stabile.

---

# Laboratorio

- scelta list/tuple;
- unpacking di coordinate;
- matrice piccola con somma per riga;
- ricerca di valore + posizione;
- Debug Clinic su righe condivise;
- mini-project tabellare solo se non comprime il mastery.

Per il recupero usare matrici 2×3 e nomi `riga/colonna`, non `i/j`.

---

# Minimum mastery gate — prima del Checkpoint B

Considerare M22 consolidato quando lo studente riesce a:

- spiegare list mutabile vs tuple immutabile;
- fare unpacking di una coppia;
- scegliere list/tuple in un dominio semplice;
- accedere a una cella `[r][c]`;
- attraversare una lista di liste;
- calcolare un totale per riga con reset corretto;
- spiegare perché `[[0] * C] * R` può condividere le righe;
- costruire righe indipendenti con una forma esplicita;
- motivare il modello dati scelto.

Tuple contenenti oggetti mutabili, packing senza parentesi e righe irregolari non devono dominare il gate.

---

# Misconception watchlist

- parentesi = tuple anche senza virgola;
- tuple scelte “per velocità” invece che per modello dati;
- immutabilità della tuple trasferita magicamente agli oggetti interni;
- confusione riga/colonna;
- `[[0]*C]*R` considerato righe indipendenti;
- ogni lista di liste considerata matrice rettangolare;
- credere che la matrice sia un nuovo costrutto Python invece di una lista di liste.

---

# Differenziazione

## Recupero

- coordinate `(x, y)`;
- matrici 2×3;
- attraversamento per valore prima degli indici;
- diagramma delle righe come oggetti separati;
- costruzione esplicita con loop.

## Enrichment

- lista di tuple;
- tuple contenente lista;
- righe irregolari;
- comprehension di costruzione dopo il loop;
- massimo/somma per riga.

---

# Evidence docente

Raccogliere:

- scelta list/tuple motivata;
- unpacking;
- trace matrice;
- debug alias righe;
- funzione su dati tabellari.

---

# Friedpython

Il materiale tuple legacy è solo riferimento:

- riusare concetti dopo riscrittura;
- non copiare sintassi Python 2;
- non anticipare comprehension;
- audit individuale prima dell'import.

---

# Cosa NON anticipare

- NumPy;
- dataclass/NamedTuple come core;
- generics/type hints avanzati;
- deep copy come requisito;
- matrici sparse/dict.

---

# Exit checkpoint PY2-07 — raggruppato

## A — Mutabilità

- list mutabile;
- metodi mutanti/None;
- alias/copia.

## B — Trasformare dati

- filtro sicuro;
- sort/sorted;
- contratto di mutazione.

## C — Modello dati

- tuple/unpacking;
- list vs tuple;
- lista di liste;
- righe indipendenti.

## D — Metodo

- funzioni;
- trace;
- test;
- scelta motivata.

Checkpoint B consolida queste competenze prima di set e dizionari.

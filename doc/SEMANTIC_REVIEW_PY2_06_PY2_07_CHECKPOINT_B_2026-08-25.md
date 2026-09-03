# Review didattica/semantica — PY2-06 + PY2-07 + Checkpoint B

> Data: 2026-08-25  
> Scope: M17–M22 + Checkpoint B.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Proteggere il passaggio:

```text
str immutabile
→ algoritmi su testo
→ list mutabile
→ alias/copia
→ tuple
→ dati tabellari
```

senza trasformare stringhe/liste in cataloghi di metodi o anticipare un modello di memoria troppo formale.

Regola invariata:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# Architettura complessiva

La progressione è corretta e riusa bene il materiale precedente:

```text
M17  sequence model + indexing/slicing
M18  choose text operation + normalization
M19  integrate loops/functions/tests on text
M20  same sequence model, now mutable
M21  aliases/copies + mutation contracts
M22  tuple + nested data + M12/M21 reuse
```

Non serve cambiare ordine o monte ore.

---

# M17 — `str` come sequenza immutabile

## MUST MASTER

1. `str` come sequenza ordinata immutabile;
2. `len()` e indici da zero;
3. ultimo indice positivo valido;
4. indice singolo vs slice;
5. `start` incluso / `stop` escluso;
6. immutabilità e costruzione di un nuovo valore;
7. iterazione diretta vs indice quando la posizione serve.

## GUIDED EXPOSURE

- indici negativi oltre il semplice `-1`;
- step nello slicing;
- differenza fra slice oltre il limite e indice fuori range.

## ENRICHMENT / BACKUP

- `[::-1]` come inversione;
- escape meno comuni;
- nota Unicode teacher-side;
- raw/triple strings.

La capacità di spiegare `[::-1]` non è un prerequisito per M18.

---

# M18 — metodi senza catalogo

## Finding principale

Il modulo elenca molti metodi (`lower`, `upper`, `strip`, `replace`, `startswith`, `endswith`, `find`, `count`). Se tutti diventano mastery, il carico si sposta dal ragionamento alla memorizzazione.

## MUST MASTER

1. scegliere `in` quando serve esistenza;
2. scegliere `find()` quando serve la posizione e interpretare `-1`;
3. evitare `if testo.find(...)`;
4. capire che i metodi di `str` restituiscono una nuova stringa;
5. usare `strip()`/`lower()` in una normalizzazione semplice e motivata;
6. decidere quando usare un metodo standard e quando il loop è l'outcome didattico.

## GUIDED EXPOSURE

- `count()`;
- `startswith()` / `endswith()`;
- `replace()`;
- `upper()`.

## ENRICHMENT / BACKUP

- `strip(chars)` e la sua semantica non-substring;
- `casefold()`;
- catene di normalizzazione più ricche.

Il criterio di uscita è **scegliere l'operazione dalla domanda**, non recitare i metodi disponibili.

---

# M19 — algoritmi su testo e parsing semplice

## MUST MASTER

1. combinare funzione + loop + `if` su una stringa;
2. riusare contatore/accumulatore su caratteri;
3. costruire una nuova stringa in un piccolo esercizio;
4. progettare casi limite: vuota, un carattere, maiuscole/spazi quando rilevanti;
5. validare un formato posizionale semplice con `len`/indici/slicing;
6. separare analisi e presentazione;
7. motivare metodo standard vs algoritmo manuale.

## GUIDED EXPOSURE

- `isalpha()` / `isdigit()` / `isalnum()` come predicate standard disponibili;
- palindromo come caso di confronto fra algoritmo e shortcut;
- `split()` come ponte: **riconoscere che produce una list**, senza richiedere ancora padronanza della lista.

## ENRICHMENT / BACKUP

- `join()`;
- palindrome tramite `[::-1]` dopo il modello manuale;
- `enumerate()` sul testo;
- validator più ricchi.

`split/join` non devono comprimere la chiusura dell'UDA: M20 insegna davvero la lista.

---

# M20 — list: prima mutabilità, poi metodi

## MUST MASTER

1. `str` immutabile vs `list` mutabile;
2. creare/accedere/modificare una lista per indice;
3. `append()` e bug `lista = lista.append(...)`;
4. capire che un metodo mutante cambia l'oggetto e spesso restituisce `None`;
5. iterazione diretta sugli elementi;
6. usare indice soltanto quando serve la posizione;
7. costruire progressivamente una lista da N valori;
8. membership `in`.

## GUIDED EXPOSURE

- `extend()`;
- `remove()` vs `pop()`;
- `enumerate()`;
- slicing di lista come nuova lista superficiale.

## ENRICHMENT / BACKUP

- `insert()`;
- slice assignment;
- confronto concatenazione/extend.

Non serve memorizzare cinque metodi di modifica per capire la mutabilità.

---

# M21 — alias, copia e contratti di mutazione

## MUST MASTER

1. `b = a` significa due nomi verso lo stesso oggetto;
2. prevedere una mutazione osservata tramite alias;
3. creare una nuova lista esterna con `.copy()`/slice;
4. distinguere alias vs copia per liste piatte;
5. evitare rimozione ingenua durante iterazione;
6. costruire una nuova lista filtrata/trasformata con loop esplicito;
7. distinguere `sort()` in-place da `sorted()` nuova lista;
8. testare se una funzione promette di mutare o non mutare l'input.

## GUIDED EXPOSURE

- shallow copy su struttura annidata;
- iterare su una copia quando la mutazione in-place è veramente il contratto;
- performance intuitiva di ricerca/inserimento.

## ENRICHMENT / BACKUP

- comprehension dopo loop equivalente;
- inversione con più API;
- confronto contratti in-place vs new-result.

`deepcopy` non è core.

---

# M22 — tuple e dati tabellari

## Finding principale

M22 unisce tuple e matrici. È sostenibile perché entrambe riusano concetti già noti, ma alcuni dettagli devono rimanere guided/enrichment.

## MUST MASTER

1. tuple come sequenza ordinata immutabile;
2. unpacking semplice;
3. scelta intuitiva list vs tuple dal significato dei dati;
4. lista di liste e accesso `[riga][colonna]`;
5. attraversamento per valore e, quando serve, per coordinate;
6. riuso di M12 `R×C` e reset per riga;
7. diagnosticare righe condivise nel pattern `[[0] * C] * R`;
8. motivare la struttura scelta.

## GUIDED EXPOSURE

- tupla a un elemento `(x,)`;
- packing senza parentesi;
- `enumerate()` riletto come coppia/unpacking;
- righe irregolari.

## ENRICHMENT / BACKUP

- tuple che contengono oggetti mutabili;
- comprehension per costruire righe indipendenti;
- strutture miste più articolate.

Il bug delle righe condivise è importante come **riuso del modello alias M21**, non come trucco da memorizzare.

---

# Checkpoint B — consolidamento, non nuova UDA

## Competenze raggruppate

### A — Sequenze testuali

- indici/slice;
- immutabilità;
- normalizzazione/algoritmo su testo.

### B — Mutabilità e riferimenti

- list mutabile;
- alias vs copia;
- contratto di mutazione/non-mutazione.

### C — Operazioni su liste

- append/iterazione;
- filtro/trasformazione;
- sort vs sorted.

### D — Modello dati

- list vs tuple;
- nested list/tabella;
- righe indipendenti.

### E — Metodo di lavoro

- funzioni;
- casi/assert;
- scelta motivata dell'operazione/struttura.

## Mini-project

Non forzare contemporaneamente stringa + lista + tuple + matrice solo per “coprire tutto”. Il dominio deve determinare quali strutture servono.

Un buon mini-project dimostra **scelta**, non quantità di feature.

## Git

Checkpoint B non introduce G2.

Se si usa Git sul mini-project, si riusa il workflow G1 già acquisito:

```text
status
→ diff
→ test
→ add
→ diff --staged
→ commit
→ status
→ log/show
```

Git resta evidence di processo, non nuovo contenuto del checkpoint.

---

# Friedpython boundary

Gli audit esistenti possono fornire candidati, ma ogni esercizio richiede:

```text
audit individuale
→ outcome preciso M17–M22
→ riscrittura Python 3.12
→ casi limite
→ starter/solution
→ provenance
```

Nessun import wholesale e nessuna comprehension anticipata per fedeltà al legacy.

---

# Esito

```text
PY2-06 architecture/order       PASS
M17 pacing                      PASS with slicing-step enrichment
M18 pacing                      PASS after method tiering
M19 pacing                      PASS with split/join as bridge only
PY2-07 architecture/order       PASS
M20 pacing                      PASS after method tiering
M21 pacing                      PASS with nested shallow-copy guided
M22 pacing                      PASS with tuple/matrix detail tiering
Checkpoint B                    PASS after feature-forcing + Git cleanup
```

Nessun curriculum change richiesto.

## Next review

```text
PY2-08 — M23–M25
PY2-09 — M26
```

Focus:

- set/dict scelti dalle operazioni dominanti, non come strutture “più avanzate”;
- frequenze e lookup senza nascondere il modello chiave→valore;
- nested structures senza combinazioni artificiali;
- file/error handling in sole 3 ore core: evitare di comprimere OOP.

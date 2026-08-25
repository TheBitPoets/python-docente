# Review didattica/semantica — PY2-08 + PY2-09

> Data: 2026-08-25  
> Scope: M23–M26.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Proteggere due obiettivi congelati molto importanti:

```text
scegliere la struttura dati dalle operazioni dominanti
+
introdurre persistenza/error boundary in sole 3 ore
```

senza trasformare set/dict in cataloghi di API e senza sottrarre tempo alle 12 ore OOP di PY2-10.

Regola invariata:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# Architettura complessiva

La progressione è corretta:

```text
M23  appartenenza / unicità
 ↓
M24  chiave → valore
 ↓
M25  scegli/combina il modello
 ↓
M26  persisti il dato con un boundary minimo
 ↓
M27  quando dati + comportamento richiedono un oggetto?
```

Non serve cambiare ordine né monte ore.

---

# M23 — Set

## MUST MASTER

1. spiegare che un set rappresenta valori distinti, non una sequenza indicizzata;
2. creare un set e un set vuoto con `set()`;
3. capire che `{}` crea un dict vuoto;
4. usare membership `in`/`not in`;
5. usare `add()`;
6. usare unione/intersezione/differenza in problemi naturali;
7. scegliere `set` vs `list` in base a ordine, duplicati e membership;
8. non costruire logica che dipende da posizione/indice del set.

## GUIDED EXPOSURE

- `remove()` vs `discard()`;
- idea beginner di elemento hashable;
- deduplicazione tramite `set()` con discussione sull'informazione d'ordine persa.

## ENRICHMENT / BACKUP

- symmetric difference;
- subset/superset;
- tuple hashable come elemento;
- confronto qualitativo membership list/set.

### Finding

La hashability è importante per evitare errori concettuali, ma non deve diventare un mini-capitolo sugli hash table. Il modello core resta:

```text
valori unici + appartenenza + operazioni insiemistiche
```

---

# M24 — Dizionari

## MUST MASTER

1. spiegare `dict` come mapping `chiave → valore`;
2. creare un dict;
3. leggere/inserire/aggiornare tramite chiave;
4. capire `KeyError` a livello beginner;
5. sapere che `in d` verifica le chiavi;
6. scegliere accesso diretto `d[k]` vs `get()` secondo il contratto;
7. iterare su chiavi e con `items()` quando servono chiave+valore;
8. implementare un semplice pattern di frequenze;
9. spiegare perché il dict rende naturale un lookup per chiave.

## GUIDED EXPOSURE

- `keys()`/`values()` come view;
- ordine di inserimento dei dict moderni come nota di accuratezza;
- chiavi hashable;
- Unicode-friendly rispetto alla vecchia tabella ASCII-256.

## ENRICHMENT / BACKUP

- `setdefault()`;
- tuple-key;
- matrici sparse;
- confronto con `Counter` soltanto in livelli futuri.

### Finding

Il pattern frequenze deve essere insegnato come riuso di M11:

> per ogni chiave incontrata, il valore ricorda il conteggio visto finora.

Non come formula `get(k,0)+1` da copiare senza significato.

---

# M25 — Scelta del modello dati

## Giudizio

È il **vero modulo di sintesi** del blocco strutture dati e deve restare un modulo di design, non di nesting.

## MUST MASTER

1. scegliere `str/list/tuple/set/dict` dalle operazioni dominanti;
2. motivare la scelta usando ordine, mutabilità, duplicati, membership, lookup e ruolo dei campi;
3. riconoscere liste parallele come modello fragile in molti casi;
4. confrontare almeno due modelli plausibili;
5. usare una semplice struttura combinata quando il dominio la richiede;
6. evitare profondità di nesting priva di significato;
7. spiegare il ponte record/dict → oggetto senza anticipare classi.

## GUIDED EXPOSURE

- lista di tuple vs lista di dict;
- dict di liste come relazione uno→molti;
- dict indicizzato per identità;
- lookup diretto vs scansione ripetuta in linguaggio qualitativo.

## ENRICHMENT / BACKUP

- dict di set;
- `setdefault()`;
- matrice sparsa con tuple-key;
- lista di dict vs dict di dict;
- inversione frequenza→lista.

### Finding

Il mini-project non deve richiedere “almeno due strutture combinate” per principio. Deve richiedere:

```text
modello sufficiente e motivato
```

Una sola struttura ben scelta può essere migliore di tre contenitori annidati usati per dimostrare varietà.

---

# M26 — File testo, pathlib ed errori prevedibili

## Vincolo

```text
3 ore core
```

La priorità è proteggere l'OOP. M26 deve lasciare un boundary minimo e corretto, non una panoramica del filesystem Python.

## MUST MASTER

1. distinguere dato in memoria e persistenza;
2. distinguere percorso e contenuto;
3. costruire un `Path` relativo al workspace;
4. leggere/scrivere un piccolo file testo dichiarando UTF-8;
5. usare un context manager `with` quando lavora esplicitamente con un file object;
6. iterare sulle righe in un esempio semplice;
7. separare I/O e logica di elaborazione;
8. gestire `FileNotFoundError` in modo mirato quando l'assenza è prevista;
9. distinguere bug del programma ed errore esterno prevedibile.

## GUIDED EXPOSURE

- `read_text/write_text` vs `Path.open` come due superfici per casi diversi;
- newline nelle righe;
- `PermissionError` come altro esempio di errore esterno;
- perché `except Exception: pass` è troppo ampio.

## ENRICHMENT / BACKUP

- append mode;
- confronto streaming vs lettura completa;
- trasformazioni per riga più ricche.

## TEACHER / DELIVERY ONLY

- P4 `2cornot2c#757`;
- fixture read-only/workdir isolato/verifica host-side;
- dettagli del grader filesystem.

### Finding

Il deck/lesson può contenere `PermissionError` e P4 come riferimento docente, ma il mastery della settimana non deve dipendere da questi dettagli.

CSV, JSON, binario, pickle, custom exceptions e traversal restano correttamente fuori dal core.

---

# Exit gate PY2-08/PY2-09

Prima di OOP lo studente deve saper rispondere a queste domande:

## A — Quale struttura?

```text
ordine/posizione?
mutabilità?
duplicati?
appartenenza?
lookup per chiave?
record posizionale o campi nominati?
```

## B — Quale stato?

Per frequenze/raggruppamenti:

> che cosa significa il valore associato a ciascuna chiave dopo i dati già elaborati?

## C — Quale persistenza minima?

```text
Path relativo
→ UTF-8
→ I/O piccolo
→ logica separata
→ errore esterno mirato
```

Non richiedere:

- hash internals;
- Big-O;
- Counter/defaultdict;
- JSON/CSV;
- P4;
- gerarchie di eccezioni.

---

# Esito

```text
PY2-08 architecture/order       PASS
M23 pacing                      PASS with hash/remove-discard guided
M24 pacing                      PASS with views/order/hash guided
M25 pacing                      PASS if model choice dominates nesting
PY2-09 architecture/order       PASS
M26 pacing                      PASS with strict 3h mastery boundary
```

Nessun curriculum change richiesto.

## Next review

```text
PY2-10 — M27–M30 + Checkpoint C
```

Focus:

- classe/istanza senza metafore fuorvianti;
- `self` e stato senza internals prematuri;
- invarianti realmente testabili;
- composizione prima dell'ereditarietà;
- capstone piccolo ma completo;
- evitare che il capstone introduca nuovi prerequisiti o tool non certificati.

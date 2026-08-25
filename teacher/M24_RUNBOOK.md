# M24 — Runbook docente

## Modulo

**Dizionari: chiave→valore, lookup e frequenze**  
UDA PY2-08 — Set, dizionari e modellazione dei dati

Stato: draft editoriale controllato.

## Obiettivo docente

Far emergere il cambio di modello:

```text
list → posizione
set  → appartenenza/unicità
dict → chiave → valore
```

Il corso deve evitare due errori opposti:

- usare dict come “lista con nomi” senza capire il lookup;
- usare `get()` ovunque nascondendo chiavi che invece dovrebbero esistere.

---

# Priorità didattica

## MUST MASTER

1. spiegare `dict` come mapping `chiave → valore`;
2. creare un dict;
3. leggere/inserire/aggiornare tramite chiave;
4. capire `KeyError` a livello beginner;
5. sapere che `in d` verifica le chiavi;
6. scegliere `d[k]` vs `get()` secondo il contratto;
7. iterare sulle chiavi e usare `items()` quando servono chiave+valore;
8. implementare un semplice pattern di frequenze;
9. spiegare perché il dict rende naturale un lookup per chiave.

## GUIDED EXPOSURE

- `keys()` / `values()` come view;
- ordine di inserimento dei dict moderni come nota di accuratezza;
- chiavi hashable;
- confronto con la vecchia tabella ASCII-256.

## ENRICHMENT / BACKUP

- `setdefault()`;
- tuple-key;
- matrice sparsa;
- `Counter`/`defaultdict` in livelli successivi.

Il pattern frequenze deve essere spiegato come **stato progressivo per chiave**, non come formula `get(k, 0) + 1` da recitare.

---

# Ora teoria attiva 1 — mapping e lookup

1. Posizione→valore vs chiave→valore.
2. Creazione e lookup.
3. Inserimento/aggiornamento.
4. `KeyError` come informazione quando una chiave richiesta manca.
5. Membership sulle chiavi.
6. `[]` vs `get()` in base al contratto.

Domanda ricorrente:

> la chiave deve esistere oppure è opzionale?

---

# Ora teoria attiva 2 — attraversare e ricordare per chiave

1. `for k in d` come iterazione sulle chiavi.
2. `items()` quando servono anche i valori.
3. Frequenze su una stringa/parole semplici.
4. Invariante:

```text
per ogni chiave già incontrata,
il valore associato è il conteggio visto finora
```

5. Nota breve su `keys/values/items` come view soltanto se utile alla precisione.
6. Nota moderna sull'ordine del dict come accuracy correction, senza cambiare la semantica primaria del mapping.

---

# Laboratorio

- mapping microscope;
- inventario/voti semplici;
- required-vs-optional key;
- funzione frequenze;
- Debug Clinic su KeyError/default/chiave sbagliata;
- confronto strutturale lista indicizzata vs dict.

Le view e la hashability possono essere osservate come guided exposure, non come esercizi separati obbligatori.

---

# Minimum mastery gate — prima di M25

Considerare M24 consolidato quando lo studente riesce a:

- spiegare posizione→valore vs chiave→valore;
- creare e aggiornare un dict;
- usare membership sulle chiavi;
- scegliere `[]` o `get()` e motivarlo;
- iterare su chiavi/coppie chiave-valore;
- costruire una semplice funzione di frequenze;
- spiegare l'invariante del conteggio per chiave;
- motivare perché un dict è naturale quando il lookup usa un'identità/chiave.

Dettagli di view, ordine moderno e hashability non devono dominare il gate.

---

# Misconception watchlist

- `get` sempre più sicuro di `[]`;
- `in d` cerca nei valori;
- dict pensato come lista indicizzata;
- `get(k, 0)` copiato senza chiedersi se zero è un default semantico;
- ordine di inserimento confuso con accesso posizionale;
- pattern frequenze imparato come formula priva di invariante;
- lista mutabile usata come chiave senza capire il limite.

---

# Differenziazione

## Recupero

- dict piccoli `str→int`;
- una sola operazione per esercizio;
- membership prima di `get`;
- frequenze su parole corte;
- tabella “chiave richiesta / opzionale”.

## Enrichment

- `setdefault` dopo il pattern esplicito;
- tuple-key `(r,c)`;
- matrice sparsa;
- ordine di inserimento vs ordinamento esplicito.

---

# Evidence docente

Raccogliere:

- lookup/aggiornamento;
- scelta `[]`/`get` motivata;
- iterazione `items()`;
- funzione frequenze con invariante spiegato;
- scelta dict vs lista motivata.

---

# Friedpython

Audit canonico: `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

Da correggere prima di riuso:

- note sull'ordine non più attuali;
- descrizione di `keys()` non precisa per Python 3 moderno;
- esempi/output storici.

L'esercizio frequenze è un ottimo spunto, ma va riscritto come materiale originale e collegato al modello M11 dello stato progressivo.

---

# Cosa NON anticipare

- defaultdict/Counter come core;
- internals hash table;
- JSON come persistenza;
- ORM/database;
- dict comprehension come prerequisito.

---

# Handoff a M25

M24 introduce lookup e frequenze.
M25 chiede:

> come combino strutture diverse e quale modello rende più naturali le operazioni del problema?

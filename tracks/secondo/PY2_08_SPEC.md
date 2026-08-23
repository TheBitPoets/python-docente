# PY2-08 — Set, dizionari e modellazione dei dati

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 25–27;
- monte ore nominale: 9 ore;
- prerequisiti: liste/tuple, funzioni, cicli, selezione e test;
- baseline: Python 3.12;
- output: lo studente sceglie `set` quando unicità/membership sono centrali, `dict` quando serve una relazione chiave→valore, costruisce frequenze/lookup, usa strutture annidate e confronta list/tuple/set/dict in base alle operazioni richieste.

## Perché questa UDA esiste

Finora le collezioni sono state prevalentemente **sequenze**. Qui introduciamo due modelli differenti:

```text
set  → quali valori unici appartengono all'insieme?
dict → quale valore è associato a questa chiave?
```

La domanda guida dell'intera UDA è:

> **Quali operazioni sono dominanti nel problema?**

Non esiste una struttura "migliore" in assoluto.

---

# M23 — Set: unicità, membership e operazioni insiemistiche

## Obiettivi osservabili

Lo studente sa:

1. creare un `set` non vuoto;
2. creare un set vuoto con `set()` e distinguere `{}` (dict vuoto);
3. spiegare che gli elementi sono unici;
4. aggiungere/rimuovere elementi con `add`, `remove`, `discard` a livello appropriato;
5. usare membership `in`;
6. eliminare duplicati da una sequenza quando l'ordine non è requisito dominante;
7. usare unione, intersezione e differenza su problemi naturali;
8. scegliere set vs list in base a unicità/membership/ordine;
9. non dipendere dall'ordine di iterazione/stampa di un set;
10. comprendere intuitivamente che gli elementi devono essere hashable/stabili come chiavi di appartenenza, senza entrare negli internals dell'hash table.

## Modello mentale

```text
set = collezione di valori distinti
```

Non pensare:

```text
set = lista senza ordine
```

È una struttura con semantica diversa.

## Set vuoto

Errore classico:

```python
insieme = {}
```

Questo crea un dizionario.

Corretto:

```python
insieme = set()
```

## Unicità

```python
nomi = ["anna", "luca", "anna"]
unici = set(nomi)
```

Risultato semantico: i valori duplicati vengono collassati.

Teacher note:

- la conversione perde l'ordine come requisito semantico del set;
- non usare `set` se serve preservare un preciso ordine di prima occorrenza senza un'ulteriore strategia.

## Membership e costo intuitivo

Confronto concettuale:

```text
lista → in generale devo cercare lungo la sequenza
set   → è progettato per membership/lookup efficiente
```

Non promettere O(1) come legge assoluta al beginner; spiegare che set/dict usano hashing e **normalmente** sono la scelta naturale quando membership/lookup domina.

## Operazioni insiemistiche

Problemi naturali:

- studenti iscritti a due corsi;
- parole presenti in due testi;
- permessi/ruoli;
- tag/categorie;
- elementi presenti in A ma non B.

Usare:

- `|` / `.union()`;
- `&` / `.intersection()`;
- `-` / `.difference()`.

La notazione matematica può essere collegata a quella informatica senza farne una UDA di teoria degli insiemi.

## `remove` vs `discard`

- `remove(x)` segnala errore se manca;
- `discard(x)` rende idempotente la rimozione se il requisito lo vuole.

Scegliere in base al contratto, non alla paura delle eccezioni.

## Activity candidate

### A — Membership/uniqueness microscope

Prevedere contenuto semantico dopo aggiunte/duplicati.

### B — List or set?

Classificare problemi e motivare la scelta.

### C — Implement

Confrontare due gruppi/tag/insiemi con unione/intersezione/differenza.

### D — Debug

- `{}` usato come set vuoto;
- aspettarsi duplicati;
- affidarsi all'ordine;
- `remove` su elemento assente non previsto;
- mettere una lista come elemento del set.

---

# M24 — Dizionari: chiavi, valori, lookup, iterazione e frequenze

## Obiettivi osservabili

Lo studente sa:

- creare un `dict` con literal;
- leggere/scrivere un valore per chiave;
- aggiungere/modificare una coppia;
- cancellare con `del`/`pop` quando appropriato;
- verificare presenza chiave con `in`;
- distinguere lookup diretto `d[key]` e `d.get(key, default)`;
- comprendere `KeyError` come segnale di contratto/chiave assente;
- iterare su chiavi;
- usare `.values()` e `.items()`;
- usare unpacking `(chiave, valore)` in `.items()`;
- costruire una tabella di frequenze;
- scegliere tra controllo esplicito e `.get(..., 0)` dopo aver compreso entrambi;
- non confondere membership sulle chiavi con membership sui valori;
- sapere che in Python moderno il dict conserva l'ordine di inserimento, senza sceglierlo principalmente per questo motivo.

## Modello mentale

```text
chiave ──> valore
```

Una chiave identifica un'associazione.

Esempi naturali:

```text
codice studente → nome
prodotto → prezzo
parola → frequenza
sigla → descrizione
```

## Lookup vs scansione

Confrontare:

```python
studenti = [
    ("A12", "Anna"),
    ("B07", "Luca"),
]
```

con:

```python
studenti = {
    "A12": "Anna",
    "B07": "Luca",
}
```

Se l'operazione dominante è:

> "dammi lo studente con codice X"

il dizionario esprime direttamente il modello.

## Chiavi e hashability

Core beginner:

- stringhe, numeri, tuple semplici immutabili possono essere chiavi candidate;
- liste/dict/set mutabili non sono chiavi;
- una chiave deve poter identificare stabilmente la posizione logica.

Gli internals di hashing/collisioni appartengono al livello avanzato.

## Chiave assente

### Il requisito considera l'assenza un errore

```python
prezzo = prezzi[codice]
```

### L'assenza ha un valore di default significativo

```python
conteggio = frequenze.get(parola, 0)
```

Non usare `.get` ovunque per nascondere errori di modello.

## Frequenze

Progressione:

### esplicita

```python
if parola in frequenze:
    frequenze[parola] += 1
else:
    frequenze[parola] = 1
```

### dopo comprensione

```python
frequenze[parola] = frequenze.get(parola, 0) + 1
```

La forma compatta arriva dopo il pattern.

## Iterazione

```python
for chiave in dizionario:
    ...
```

```python
for valore in dizionario.values():
    ...
```

```python
for chiave, valore in dizionario.items():
    ...
```

Lo studente deve scegliere in base a ciò che usa davvero.

## Activity candidate

### A — Lookup trace

Prevedere stato dict dopo insert/update/delete.

### B — Missing key

Scegliere direct access vs `get` in specifiche diverse.

### C — Frequency table

Contare parole/caratteri/categorie.

### D — Debug

- membership cercata nei valori pensando alle chiavi;
- `KeyError` nascosto con default sbagliato;
- chiave mutabile;
- iterazione `.items()` senza unpacking corretto;
- aggiornamento della chiave sbagliata.

---

# M25 — Strutture composte e scelta del modello dati

## Obiettivi osservabili

Lo studente sa:

1. scegliere tra `str`, `list`, `tuple`, `set`, `dict` per un problema semplice;
2. motivare la scelta con operazioni e vincoli;
3. costruire lista di tuple;
4. costruire lista di dizionari;
5. costruire dict di liste;
6. costruire dict di dict;
7. leggere/aggiornare strutture annidate a due livelli;
8. evitare annidamenti gratuiti quando una struttura semplice basta;
9. progettare un piccolo record con dict e riconoscerne i limiti quando comportamento e invarianti crescono;
10. confrontare dense matrix (lista di liste) e sparse mapping come enrichment;
11. considerare ordine, unicità, mutabilità e lookup nella decisione;
12. testare struttura e contenuto senza dipendere da rappresentazioni accidentali.

## Matrice di scelta

| Esigenza dominante | Struttura candidata | Domanda da farsi |
|---|---|---|
| testo ordinato immutabile | `str` | sto modellando testo? |
| sequenza modificabile | `list` | ordine e duplicati servono? |
| record/sequenza fissa | `tuple` | i campi sono posizionali/stabili? |
| valori unici / membership | `set` | l'ordine è secondario? |
| associazione chiave→valore | `dict` | ho una chiave naturale di lookup? |

È una **euristica**, non una tabella di verità assoluta.

## Lista di dict vs dict di dict

### elenco di record

```python
studenti = [
    {"id": "A12", "nome": "Anna"},
    {"id": "B07", "nome": "Luca"},
]
```

Naturale se elaboro tutti i record in sequenza.

### lookup diretto per id

```python
studenti = {
    "A12": {"nome": "Anna"},
    "B07": {"nome": "Luca"},
}
```

Naturale se l'ID è la chiave dominante.

La scelta dipende dalle operazioni.

## Dict di liste

Esempio:

```python
voti_per_studente = {
    "Anna": [7, 8, 7],
    "Luca": [6, 9],
}
```

Qui il mapping identifica lo studente; la lista modella la sequenza modificabile dei voti.

## Ponte verso OOP

Un dict è ottimo per dati dinamici/record semplici.

Quando iniziamo a dire:

```text
questo tipo di entità ha stato + comportamenti + invarianti
```

potrebbe diventare più chiaro introdurre una classe.

Non dire:

> "i dict sono sbagliati, bisogna usare classi"

ma:

> "le operazioni e le responsabilità del dominio stanno crescendo: quale modello le rende più esplicite?"

Questo prepara PY2-10.

## Sparse matrix — enrichment

Il legacy `friedpython` contiene un esempio di matrice sparsa con dict.

Può mostrare una scelta di struttura guidata dai dati:

```text
matrice enorme
+ pochissimi valori non-zero
→ forse non conviene memorizzare tutte le celle
```

Rappresentazione candidata:

```python
sparse = {
    (riga, colonna): valore,
}
```

È enrichment perché richiede già tuple come chiavi e una buona comprensione del modello; non è requisito di uscita.

## Performance intuitiva integrata

Confrontare:

```text
cercare una chiave scorrendo una lista di record
vs
lookup diretto in dict
```

oppure:

```text
verificare membership molte volte in list
vs
set
```

Regola:

- modellare prima correttamente;
- se l'operazione dominante è lookup/membership, scegliere una struttura progettata per quello;
- non sacrificare chiarezza per micro-ottimizzazioni.

## Activity candidate

### A — Structure choice cards

Dato un requisito, scegliere struttura e scrivere 1–2 motivazioni.

### B — Remodel

Trasformare lista di record in dict indicizzato quando cambia il requisito di lookup.

### C — Implement

Mini-dominio con strutture annidate + funzioni di ricerca/aggiornamento.

### D — Debug

- struttura troppo complessa;
- chiave sbagliata;
- lista usata per lookup ripetitivo senza motivo;
- set usato quando l'ordine era requisito;
- aliasing in valori list condivisi.

### E — Mini-project data model

Dalla specifica:

1. elencare operazioni principali;
2. scegliere struttura;
3. disegnare esempio dati;
4. implementare funzioni;
5. testare casi limite;
6. motivare almeno un trade-off.

---

# `friedpython` — policy specifica PY2-08

Snapshot:

`TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f`

Materiale individuato:

- operazioni base dict;
- gestione chiave mancante;
- iterazione;
- modifica sul posto;
- ordinamento sulle chiavi;
- creazione dizionari;
- metodi aggiuntivi;
- dizionari come strutture flessibili;
- matrice sparsa;
- 6 esercizi + PDF revisionato.

## Riutilizzo

Core candidate:

- operazioni base;
- missing key;
- iterazione;
- frequenze/lookup se presenti negli esercizi.

Enrichment:

- molti modi alternativi di costruire dict;
- ordinamenti avanzati;
- sparse matrix.

Non vogliamo trasformare la lezione in un inventario di constructor/method syntax.

## Set

Non c'è un equivalente legacy centrale: il materiale set sarà originale e controllato con fonti Python/Fluent Python/Pluralsight.

---

# Piano delle tre settimane

## Settimana 25 — M23

- set, unicità, membership;
- set vs list;
- unione/intersezione/differenza;
- lab problemi insiemistici.

## Settimana 26 — M24

- dict lookup/mutazione;
- chiavi/hashability beginner;
- key missing/get;
- iterazione/items;
- frequenze;
- lab frequency/lookup.

## Settimana 27 — M25

- strutture composte;
- scelta struttura;
- performance intuitiva;
- ponte OOP;
- lab mini-project data model.

---

# Exit checkpoint UDA

Lo studente dovrebbe saper:

- usare set per unicità/membership;
- usare operazioni insiemistiche base;
- creare e aggiornare dict;
- scegliere direct lookup vs get;
- iterare keys/values/items;
- costruire frequenze;
- usare chiavi appropriate;
- scegliere list/tuple/set/dict con motivazione;
- costruire/leggere strutture annidate semplici;
- riconoscere quando una chiave naturale rende utile un dict;
- riconoscere quando set/dict possono evitare scansioni ripetute;
- collegare record dict al futuro passaggio a oggetti senza considerarli intercambiabili in modo automatico.

---

# Remediation

- usare schede fisiche chiave→valore;
- dict con 2–3 chiavi;
- set con duplicati visibili;
- prima direct access, poi `get`;
- frequenze su parola corta;
- scegliere struttura da un solo requisito dominante prima di casi multi-criterio.

# Enrichment

- `frozenset` come concetto;
- tuple key;
- merge operator dict come preview se utile;
- `setdefault` soltanto dopo frequenze esplicite;
- sparse matrix;
- confronto empirico membership list vs set su dati grandi come demo docente, non benchmark scientifico.

---

# Fonti

- *Think Python / Pensare in Python*: dictionaries, tuples/data structures;
- *Learning Python / Imparare Python*: dict/set coverage;
- *Fluent Python*: mapping/set/hashability come controllo docente;
- *Python in a Nutshell*: reference;
- documentazione Python 3.12 dict/set;
- Pluralsight Python Data Structures;
- `friedpython` pinned legacy pack.

---

# Dipendenze piattaforma

- Python 3.12;
- P1 per programmi completi;
- P2 #756 utile per funzioni che restituiscono set/dict/strutture annidate; richiede value codec deterministico e type-aware;
- nessun runtime speciale.

---

# Criteri per produzione

- audit esercizi dict completato;
- nuovo materiale set originale;
- almeno una Activity di **scelta** struttura;
- `dict.get` non insegnato come modo per nascondere ogni `KeyError`;
- set order non trattato come contrattuale;
- dict insertion order spiegato senza renderlo criterio primario;
- frequenze costruite prima in forma esplicita;
- sparse matrix enrichment, non core;
- ponte a OOP esplicito ma senza anticipare classi.

# Python — mappa moduli del secondo anno (DRAFT)

> Obiettivo: trasformare il piano annuale in moduli piccoli, componibili e producibili con lo stesso contratto di delivery usato in TPSI5.
>
> Vincolo: **33 settimane × 3 ore = 99 ore nominali**, ma il corso non assume 99 ore nette di nuovo contenuto. Il design riserva settimane/checkpoint a recupero, verifica, laboratorio e capstone.

## Principio di progettazione

Il percorso è **spirale**, non puramente lineare.

Alcune competenze iniziano presto e vengono rinforzate durante tutto l'anno:

- casi di test: dal primo algoritmo;
- trace/manual execution: dal primo flow chart;
- debugging: dal primo script Python;
- funzioni: prima come chiamate e piccole definizioni, poi come vera decomposizione;
- leggibilità/naming: da subito;
- confronto tra soluzioni: dalla selezione in poi;
- efficienza: intuizioni operative dentro loop e strutture dati;
- spiegazione delle scelte: in ogni Activity significativa.

La priorità nel secondo anno è sempre:

```text
correttezza
→ comprensibilità
→ decomposizione/modello dati adeguati
→ robustezza
→ efficienza quando rilevante
```

Non si insegna la micro-ottimizzazione a scapito della chiarezza.

---

# UDA PY2-00 — Orientamento e metodo

## M00 — Come si risolve un problema con un computer

**Durata:** 1–2 ore distribuite nella prima settimana.

- cosa significa programmare;
- problema, algoritmo, programma;
- input, output, vincoli;
- esempi e controesempi;
- come sarà usato il corso: teoria → trace → codice → test → debug → spiegazione;
- diagnostic iniziale non valutativo.

Non richiede ancora Python.

---

# UDA PY2-01 — Problem solving, algoritmi e flow chart

**Finestra:** settimane 1–3 — 9 ore nominali.

## M01 — Dal problema ai passi

- leggere una specifica semplice;
- dati disponibili e risultato atteso;
- decomposizione;
- algoritmo finito/non ambiguo/eseguibile;
- pseudocodice;
- casi normali e casi limite.

## M02 — Sequenza, input/output e selezione nei diagrammi

- simboli fondamentali del flow chart;
- sequenza;
- input/output;
- condizioni;
- selezione semplice e doppia;
- selezione multipla;
- trace table.

## M03 — Iterazione e annidamento nei diagrammi

- ripetizione;
- ciclo controllato da condizione;
- ciclo controllato da contatore;
- selezione dentro ciclo;
- ciclo dentro selezione;
- primi cicli annidati;
- dry-run manuale;
- progettare casi di test prima della codifica.

**Soglia di uscita:** lo studente sa rappresentare e simulare un piccolo algoritmo senza dipendere da Python.

---

# UDA PY2-02 — Primi programmi Python

**Finestra:** settimane 4–5 — 6 ore nominali.

## M04 — Interprete, script, valori e I/O

- interprete/REPL e file `.py`;
- `print`;
- `input`;
- literal;
- nomi/variabili;
- `int`, `float`, `bool`, `str`;
- conversioni;
- primi errori di sintassi e runtime;
- leggere traceback molto semplici.

## M05 — Espressioni, operatori e prime funzioni

- operatori aritmetici;
- precedenza;
- confronto tra espressioni equivalenti;
- formattazione output / f-string;
- chiamare funzioni built-in;
- definire una prima funzione molto piccola;
- parametro, argomento e `return` a livello introduttivo;
- distinguere calcolo da stampa;
- naming e formattazione leggibile.

> La decomposizione completa in funzioni arriverà più avanti. Qui evitiamo però di insegnare implicitamente che ogni programma debba essere un unico blocco monolitico.

---

# UDA PY2-03 — Selezione e logica

**Finestra:** settimane 6–8 — 9 ore nominali.

## M06 — Booleani, confronti e `if`

- espressioni booleane;
- confronti;
- `if`;
- `if/else`;
- trace dei rami;
- casi di test per decisioni.

## M07 — `elif` e condizioni composte

- `if/elif/else`;
- più `if` indipendenti vs rami mutuamente esclusivi;
- `and`, `or`, `not`;
- range e condizioni composte;
- semplificazione di condizioni.

## M08 — Selezioni annidate, validazione e refactoring

- annidamento;
- casi limite;
- validazione logica;
- guard conditions introduttive;
- riconoscere annidamenti inutili;
- Activity di confronto tra più soluzioni corrette.

**Extension:** `match/case` solo dopo piena padronanza di `if/elif/else` e soltanto quando migliora il modello del problema.

---

# UDA PY2-04 — Iterazione e pattern algoritmici

**Finestra:** settimane 9–12 — 12 ore nominali.

## M09 — `while`, sentinelle e validazione ripetuta

- ciclo pre-condizionale;
- contatore;
- accumulatore;
- sentinella;
- loop infinito;
- off-by-one;
- input ripetuto;
- trace.

## M10 — `for`, `range` e iterazione controllata

- `for`;
- `range`;
- iterazione per numero noto di passi;
- scegliere `for` vs `while`;
- `break`/`continue` con uso disciplinato.

## M11 — Selezione + iterazione

- `if` dentro `for/while`;
- loop dentro rami condizionali;
- conteggio condizionale;
- somma/media;
- min/max progressivo;
- flag;
- ricerca lineare.

## M12 — Cicli annidati e confronto delle soluzioni

- cicli annidati;
- tabelle, griglie e coppie;
- riconoscere lavoro ripetuto;
- intuizione lineare vs quadratica;
- refactoring di annidamenti accidentali;
- scegliere la soluzione più leggibile a parità di correttezza.

**Soglia di uscita:** lo studente compone selezione e iterazione senza dipendere da pattern memorizzati meccanicamente.

---

# UDA PY2-05 — Funzioni, decomposizione e testing

**Finestra:** settimane 13–16 — 12 ore nominali.

## M13 — Funzioni produttive

- definizione/chiamata;
- parametri/argomenti;
- `return`;
- valori di ritorno;
- funzioni vs procedure che stampano;
- casi di test deterministici.

## M14 — Scope e composizione

- scope locale essenziale;
- passaggio dei dati;
- evitare globali come scorciatoia;
- funzione che chiama funzione;
- composizione.

## M15 — Progettazione top-down

- decomporre un problema;
- responsabilità;
- separare input, logica, output;
- contratti intuitivi;
- pre/post-condizioni semplici;
- pseudocodice modulare.

## M16 — Test, debug e refactoring

- `assert` introduttivo;
- tabella casi di test;
- edge cases;
- debug di funzioni;
- eliminare duplicazione;
- naming;
- confronto tra API di funzione alternative.

---

# Checkpoint A — consolidamento primo nucleo

**Finestra consigliata:** settimana 17 — 3 ore flessibili.

Uso possibile:

- recupero;
- verifica pratica;
- mini-progetto strutturato;
- correzione ragionata;
- settimana assorbibile da imprevisti scolastici.

Non introduce un prerequisito nuovo per il resto del corso.

---

# UDA PY2-06 — Stringhe come sequenze

**Finestra:** settimane 18–20 — 9 ore nominali.

## M17 — Indici, slicing, immutabilità

- `str` come sequenza;
- `len`;
- indici positivi/negativi;
- slicing;
- immutabilità;
- iterazione per carattere.

## M18 — Ricerca, conteggio e metodi

- membership;
- `find`/conteggio;
- normalizzazione;
- case conversion;
- strip/split/join;
- validazione e trasformazione.

## M19 — Algoritmi su testo e parsing semplice

- parole/frasi/codici;
- frequenze;
- tokenizzazione semplice;
- costruzione di output;
- confronto loop esplicito vs metodi built-in;
- problemi integrati con funzioni.

---

# UDA PY2-07 — Liste, tuple e dati tabellari

**Finestra:** settimane 21–23 — 9 ore nominali + eventuale checkpoint/lab nella settimana 24.

## M20 — Liste: creare, accedere, modificare

- literal;
- accesso/slicing;
- append/insert/remove/pop;
- mutabilità;
- iterazione.

## M21 — Alias, copie e algoritmi sulle liste

- reference condivise a livello intuitivo;
- alias vs copia;
- mutazione durante iterazione;
- ricerca, filtro, aggregazione;
- ordinamento;
- scelta tra operazione in-place e nuovo risultato.

## M22 — Tuple, unpacking, matrici

- tuple;
- immutabilità;
- packing/unpacking;
- lista vs tupla;
- lista di liste;
- matrici;
- doppi indici;
- cicli annidati sui dati.

**Extension:** comprehension semplice soltanto dopo che la stessa trasformazione è padroneggiata con loop esplicito.

---

# Checkpoint B — laboratorio strutture sequenziali

**Finestra consigliata:** settimana 24 — 3 ore flessibili.

- recupero o verifica;
- import selettivo/revisione degli esercizi `friedpython` su stringhe/liste;
- mini-progetto;
- confronto di modellazioni alternative.

---

# UDA PY2-08 — Set, dizionari e modellazione dei dati

**Finestra:** settimane 25–27 — 9 ore nominali.

## M23 — Set e unicità

- creazione;
- membership;
- add/remove;
- unione/intersezione/differenza dove utile;
- quando il set è migliore di una lista.

## M24 — Dizionari

- chiave/valore;
- lookup;
- inserimento/modifica/cancellazione;
- chiave assente;
- iterazione su keys/values/items;
- frequenze.

## M25 — Strutture composte e scelta del modello

- lista di tuple;
- lista di dict;
- dict di liste;
- dict di dict;
- record semplici;
- scegliere tra list/tuple/set/dict;
- intuizione: lookup per chiave vs scansione lineare;
- ponte concettuale verso gli oggetti.

---

# UDA PY2-09 — Persistenza ed errori prevedibili

**Finestra minima:** settimana 28 — 3 ore core; estendibile a 6 ore usando buffer se disponibile.

## M26 — File di testo e `try/except` essenziale

- `with open(...)`;
- read/write;
- iterazione per riga;
- UTF-8;
- `pathlib` introduttivo;
- errori prevedibili;
- `try/except` essenziale;
- distinguere dato non valido, risorsa assente e bug;
- persistere dati semplici.

**Extension:** CSV/JSON e file binari sono materiale successivo/enrichment, non prerequisito per OOP.

---

# UDA PY2-10 — Classi, oggetti e capstone

**Finestra:** settimane 29–32 — 12 ore nominali.

## M27 — Dal record all'oggetto

- limiti di tuple/dict quando cresce il comportamento;
- classe;
- istanza;
- attributi;
- più istanze indipendenti;
- `self`.

## M28 — Costruzione e comportamento

- `__init__`;
- metodi;
- stato;
- invarianti semplici;
- responsabilità della classe;
- testare il comportamento.

## M29 — Collaborazione tra oggetti

- composizione;
- oggetti che contengono/collaborano con altri oggetti;
- evitare classi onnivore;
- separare I/O e dominio;
- refactoring da dict-based a object-based quando porta valore.

## M30 — Mini-capstone OOP

Prodotto piccolo ma completo che richieda almeno:

- analisi del problema;
- modello dati;
- più funzioni/metodi;
- una o più classi;
- collezioni;
- casi limite;
- test/checklist;
- spiegazione delle scelte.

**Extension:** `__str__/__repr__`, property introduttiva, inheritance semplice, dataclass come confronto dopo la classe esplicita.

---

# Checkpoint C — settimana 33

Tre usi possibili, scelti in base alla classe e al calendario reale:

1. capstone/finalizzazione;
2. recupero + verifica finale;
3. enrichment OOP / Romeo / Git minimo.

La settimana 33 non deve contenere un concetto obbligatorio senza il quale il corso risulta incompleto.

---

# Budget temporale

| Blocco | Settimane nominali |
|---|---:|
| PY2-01 algoritmi | 3 |
| PY2-02 primi programmi | 2 |
| PY2-03 selezione | 3 |
| PY2-04 iterazione | 4 |
| PY2-05 funzioni | 4 |
| Checkpoint A | 1 |
| PY2-06 stringhe | 3 |
| PY2-07 liste/tuple | 3 |
| Checkpoint B | 1 |
| PY2-08 set/dict | 3 |
| PY2-09 file/errori | 1 |
| PY2-10 OOP | 4 |
| Checkpoint C | 1 |
| **Totale** | **33** |

I tre checkpoint equivalgono a **9 ore esplicitamente flessibili**. Inoltre molte verifiche/pratiche sono integrate nelle UDA e non richiedono settimane aggiuntive di nuovo contenuto.

# Artefatti standard per modulo

Ogni modulo definitivo dovrà avere, dove appropriato:

```text
lesson canonica
slide
microscope/demo
worked example
Activity A/B/C/D
starter
solution/reference
checkpoint
misconception/debug notes
teacher notes
source mapping
```

Le Activity E/F sono più spesso collocate a fine UDA/checkpoint/capstone.

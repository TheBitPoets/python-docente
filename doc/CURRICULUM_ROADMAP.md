# Python curriculum — roadmap generale (DRAFT)

> Questa roadmap descrive l'intero percorso **da zero a Python professionale**. Il track di secondo anno seleziona soltanto la prima parte e ha un confine esplicito.

## Stage A — Foundation: secondo anno

**Target:** 33 settimane × 3 ore = 99 ore. Nessun prerequisito di programmazione.

### A0 — Problem solving, algoritmi e flow chart

- leggere un problema e distinguere dati, vincoli e risultato atteso;
- decomporre un problema in passi;
- proprietà di un algoritmo;
- pseudocodice;
- trace table / esecuzione manuale;
- flow chart: sequenza, input, output, selezione, iterazione;
- diagrammi con selezioni e cicli annidati;
- casi normali, casi limite e casi di test.

### A1 — Fondamenti Python

- interprete, script, REPL/IDE;
- `print`, `input`;
- assegnamento, nomi, oggetti e tipi;
- `int`, `float`, `bool`, `str`;
- conversioni esplicite;
- espressioni e operatori;
- precedenza;
- formattazione dell'output;
- primi errori: sintassi, runtime, logica.

### A2 — Selezione e logica booleana

- confronti;
- operatori logici;
- `if`, `elif`, `else`;
- `if` indipendenti vs catene mutuamente esclusive;
- condizioni composte;
- selezioni annidate;
- validazione dell'input;
- scelta del costrutto più leggibile;
- cenno opzionale a `match/case` dopo la padronanza di `if`.

### A3 — Iterazione

- ripetizione e invarianti intuitive;
- `while`;
- contatori, accumulatori, sentinelle;
- validazione ripetuta;
- `for` e `range`;
- differenza tra iterazione per condizione e per collezione/intervallo;
- `break`, `continue` con uso disciplinato;
- cicli annidati;
- pattern numerici, tabelle, griglie;
- selezioni dentro cicli e cicli dentro selezioni;
- evitare loop infiniti e off-by-one.

### A4 — Pattern algoritmici composti

- minimo/massimo;
- conteggio condizionale;
- somma/media;
- ricerca lineare;
- flag e sentinelle;
- frequenze;
- confronto tra soluzioni equivalenti;
- primi ragionamenti su lavoro lineare vs quadratico;
- refactoring di codice profondamente annidato.

### A5 — Funzioni e decomposizione

- perché creare funzioni;
- definizione e chiamata;
- parametri e argomenti;
- `return`;
- funzioni produttive/non produttive;
- scope essenziale;
- composizione di funzioni;
- validazione e pre/post-condizioni intuitive;
- progettare top-down;
- separare input/output dalla logica;
- semplici `import` e uso della standard library;
- testare funzioni pure con casi noti.

### A6 — Stringhe

- sequenze e immutabilità;
- indicizzazione e slicing;
- iterazione;
- ricerca e conteggio;
- metodi principali;
- normalizzazione del testo;
- parsing semplice;
- costruzione efficiente di stringhe a livello introduttivo;
- problemi su parole, frasi, codici e formati.

### A7 — Liste e tuple

- collezioni ordinate;
- creazione, accesso, slicing;
- mutabilità delle liste;
- metodi fondamentali;
- iterazione per elemento e per indice;
- aliasing/reference condivise a livello intuitivo;
- copia vs alias;
- ordinamento;
- tuple e immutabilità;
- packing/unpacking;
- scegliere lista vs tupla;
- matrici/list-of-lists;
- semplici comprehension solo dopo la padronanza dei loop espliciti.

### A8 — Set, dizionari e scelta della struttura dati

- set: unicità e membership;
- operazioni insiemistiche utili;
- dizionari chiave/valore;
- inserimento, modifica, cancellazione, lookup;
- iterazione su chiavi/valori/coppie;
- frequenze e raggruppamenti;
- gestione chiave assente;
- strutture annidate;
- record semplici con dizionari;
- scegliere lista/tupla/set/dict in base alle operazioni necessarie;
- intuizione dei lookup veloci nei dict/set senza formalismi prematuri.

### A9 — File ed errori gestibili

- percorsi e file di testo;
- `with open(...)`;
- lettura/scrittura;
- elaborazione riga per riga;
- encoding UTF-8;
- introduzione a `pathlib`;
- errori prevedibili;
- `try/except` di base;
- separare errore dell'utente, dato non valido e bug del programma;
- CSV/JSON come estensione se il calendario lo consente.

### A10 — Classi e oggetti

- quando i dati strutturati iniziano a richiedere un modello;
- dal dizionario all'oggetto;
- classe e istanza;
- attributi;
- metodi e `self`;
- `__init__`;
- rappresentazione essenziale (`__str__` o `__repr__` introduttivo);
- stato e comportamento;
- composizione tra oggetti;
- responsabilità di una classe;
- encapsulation come principio, non come rituale;
- inheritance solo introduttiva/estensione se il gruppo è pronto;
- mini-capstone OOP.

**Confine ufficiale proposto del secondo anno: qui.**

---

## Stage B — Core Python avanzato

Pensato per anni successivi o studenti che proseguono.

### B1 — Modello dati Python

- identità, uguaglianza, mutabilità;
- references e garbage collection a livello utile;
- shallow/deep copy;
- hashability;
- truth value;
- special methods;
- protocolli Python e duck typing.

### B2 — Iterables, comprehensions e generators

- comprehensions complete;
- generator expressions;
- iterable vs iterator;
- protocollo di iterazione;
- `yield`;
- lazy evaluation;
- pipeline di trasformazione.

### B3 — Funzioni come oggetti

- first-class functions;
- higher-order functions;
- `lambda` con moderazione;
- closures;
- decorators;
- callable objects;
- strategie e callback.

### B4 — Moduli, package e import system

- moduli;
- package;
- `__name__`;
- import assoluti/relativi;
- organizzazione di un progetto;
- namespace;
- dipendenze.

### B5 — Eccezioni e robustezza

- gerarchie di eccezioni;
- `raise`;
- eccezioni custom;
- `else/finally`;
- EAFP vs LBYL;
- context managers;
- fail-fast e boundary validation.

### B6 — OOP Python avanzata

- class/instance attributes;
- properties;
- classmethod/staticmethod;
- dataclasses;
- enums;
- inheritance e overriding;
- composition over inheritance;
- abstract base classes/protocols;
- multiple inheritance/MRO come approfondimento;
- special methods per tipi pythonic.

### B7 — Algoritmi e strutture dati

- complessità asintotica intuitiva → formale;
- ricerca lineare/binaria;
- ordinamenti fondamentali;
- stack, queue, deque;
- heap/priority queue;
- recursion;
- linked structures per comprensione;
- alberi e grafi introduttivi;
- trade-off tempo/memoria.

---

## Stage C — Professional Python

### C1 — Type hints e contratti

- annotazioni;
- collection generics;
- unions/optional;
- type aliases;
- protocols;
- gradual typing;
- checker statici.

### C2 — Testing professionale

- unit/integration/E2E;
- pytest;
- fixture;
- parametrizzazione;
- mocking con criterio;
- coverage;
- property-based testing come estensione;
- testability by design.

### C3 — Tooling e qualità

- virtual environments;
- `pyproject.toml`;
- dependency management;
- formatter/linter;
- type checker;
- Git e CI;
- logging;
- debugging con IDE/debugger;
- profiling.

### C4 — I/O e formati reali

- `pathlib` avanzato;
- CSV/JSON;
- serialization;
- regex;
- Unicode;
- date/time;
- filesystem automation.

### C5 — Database

- SQLite;
- DB-API;
- SQL parametrico;
- transazioni;
- repository/data access;
- ORM come livello successivo, non sostituto della comprensione SQL.

### C6 — HTTP, API e networking

- client HTTP;
- JSON API;
- timeout/retry/error handling;
- socket foundations;
- API server con framework moderno come specializzazione.

### C7 — Concorrenza e async

- processi/thread/event loop;
- I/O-bound vs CPU-bound;
- `concurrent.futures`;
- `asyncio`, coroutine, task;
- cancellation/timeouts;
- race conditions e synchronization basics.

### C8 — Packaging e distribuzione

- struttura progetto;
- build;
- wheel/sdist;
- metadata;
- versioning;
- pubblicazione privata/pubblica;
- CLI installabili.

### C9 — Performance e memoria

- misurare prima di ottimizzare;
- `timeit`/profiling;
- complessità;
- allocazioni;
- iterazione lazy;
- scelta strutture dati;
- caching con criterio.

### C10 — Design e maintainability

- cohesion/coupling;
- API design;
- dependency inversion a livello pragmatico;
- refactoring;
- patterns solo quando risolvono un problema;
- documentazione e manutenzione.

---

## Stage D — Applied Python / specializzazioni

Track selezionabili:

- automazione e scripting;
- web/API backend;
- networking;
- data engineering/data science;
- cybersecurity/forensics in ambiente didattico sicuro;
- robotica/IoT;
- AI/ML;
- sistemi distribuiti;
- tooling/DevOps.

## Capstone professionale

Il curriculum completo dovrebbe terminare con un prodotto che richieda:

```text
analisi
→ modello dati
→ architettura
→ package
→ typing
→ test
→ persistenza/I/O
→ error handling
→ logging
→ CI
→ documentazione
→ performance evidence
```

## Fonti guida

- **Pensare in Python / Think Python**: problem solving e progressione beginner.
- **Imparare Python / Learning Python**: copertura sistematica del core language.
- **Fluent Python**: Python data model, idiomi, protocolli, funzioni, strutture dati e OOP pythonic.
- **Python in a Nutshell**: riferimento tecnico compatto e ponte al professionale.
- **Pluralsight Python Essentials / Python 3 / Core Python**: controllo di copertura e laboratori moderni.
- **Documentazione ufficiale Python**: autorità normativa per sintassi, semantica e standard library.
- **friedpython**: source pack legacy da auditare, non curriculum canonico.

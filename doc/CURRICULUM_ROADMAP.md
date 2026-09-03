# Python curriculum — roadmap generale (DRAFT)

> Questa roadmap descrive l'intero percorso **da zero a Python developer professionale**. Il track di secondo anno seleziona soltanto la prima parte e ha un confine esplicito.

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
- namespace;
- organizzazione di un progetto;
- dipendenze tra moduli;
- API pubblica di un package.

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

### B8 — Standard library essenziale

- `collections`;
- `itertools`;
- `functools`;
- `pathlib`;
- `datetime`;
- `enum`;
- `dataclasses`;
- `json`, `csv`;
- `re`;
- `argparse`;
- `logging`;
- `subprocess` come introduzione.

---

# Stage C — Professional Python Engineering

Questo stage non insegna solo nuove feature del linguaggio: insegna **come si costruisce, verifica, distribuisce, osserva e mantiene software Python reale**.

## C1 — Ambienti, interpreti e dipendenze

- installazioni/versioni Python e selezione dell'interprete;
- perché isolare i progetti;
- `venv` come fondamento standard;
- `pip` e package index;
- version constraints;
- dipendenze dirette vs transitive;
- reproducibility e lock file;
- development/test/docs dependency groups;
- `pyproject.toml` come centro del progetto moderno;
- workflow moderno con un project/dependency manager (candidato: `uv`), distinguendo sempre il concetto dallo strumento;
- cache, ambienti CI e reproducibility cross-platform.

## C2 — Struttura professionale di progetto e packaging

- script vs application vs library;
- flat layout vs `src/` layout;
- package/module boundaries;
- `pyproject.toml` metadata;
- build backend;
- entry points / CLI;
- wheel e sdist;
- editable installs;
- semantic/versioning policy pragmatica;
- TestPyPI/PyPI o registry privato;
- trusted publishing/CI quando appropriato;
- licensing e README di distribuzione.

## C3 — Code quality toolchain

- stile come automazione, non discussione manuale;
- formatter;
- linter;
- import hygiene;
- dead code / suspicious code checks;
- target Python version;
- configurazione centralizzata in `pyproject.toml`;
- candidato toolchain moderno: Ruff per lint/format;
- quality gate locale + CI;
- pre-commit hooks come estensione.

## C4 — Typing e contratti

- type annotations;
- generics delle collection;
- union/optional;
- literals e aliases;
- callable types;
- `TypedDict`;
- dataclass + typing;
- protocols e structural typing;
- gradual typing;
- type narrowing;
- checker statici (Pyright/mypy come candidati);
- typing di API pubbliche e library;
- distinguere runtime validation e static typing.

## C5 — Testing professionale

Progressione:

```text
assert semplici
→ test di funzione
→ pytest
→ parametrizzazione
→ fixture
→ temp files / DB fixture
→ mocking/monkeypatch con criterio
→ integration tests
→ E2E
→ coverage
→ property-based testing
```

Competenze:

- test pyramid e limiti del modello;
- arrange/act/assert;
- unit vs integration vs E2E;
- determinismo e isolamento;
- test doubles solo ai boundary opportuni;
- pytest fixture e parametrizzazione;
- testing di error paths;
- database tests con transazioni/isolamento;
- HTTP/API tests;
- coverage come segnale, non obiettivo numerico cieco;
- Hypothesis/property-based testing come livello avanzato;
- testability by design;
- regressions e CI.

## C6 — Error handling, validation e configuration

- error taxonomy;
- exception boundaries;
- custom exceptions;
- input validation;
- config file / environment / CLI precedence;
- environment variables;
- configuration objects;
- secrets separati dalla configurazione ordinaria;
- fail-fast startup validation;
- graceful degradation quando appropriato;
- retry solo per errori transitori.

## C7 — File, serialization e data formats

- `pathlib` avanzato;
- encoding/Unicode;
- CSV/JSON;
- serialization/deserialization;
- schema/versioning dei dati;
- regex con criterio;
- archivi/compressione come estensione;
- atomic writes;
- temporary files/directories;
- streaming per file grandi.

## C8 — Database: DB-API e SQL prima dell'ORM

- database relazionali e responsabilità del DB;
- SQLite per sviluppo/esercizi;
- DB-API / `sqlite3`;
- connessione/cursor/result;
- SQL parametrico e SQL injection;
- CRUD;
- transazioni, commit/rollback;
- constraints;
- JOIN e query necessarie al codice applicativo;
- connection lifetime;
- repository/data-access boundary;
- test del persistence layer.

**Regola:** l'ORM non deve sostituire la comprensione di SQL e transazioni.

## C9 — SQLAlchemy Core e ORM

- Engine e connectivity;
- Core expression language;
- metadata/schema;
- CRUD Core;
- declarative mappings;
- model/row distinction;
- `Session` e unit of work;
- identity map;
- flush/commit/rollback;
- query/select;
- relazioni e join;
- eager/lazy loading e problemi N+1;
- transaction boundaries;
- sync vs async DB access;
- repository/service boundaries;
- evitare il modello "ORM magic".

## C10 — Schema migrations con Alembic

- perché lo schema deve essere versionato;
- migration environment;
- revisioni;
- upgrade/downgrade;
- autogenerate e necessità di review;
- data migration vs schema migration;
- deploy order e backward compatibility;
- migration test/smoke;
- gestione sicura dei cambi distruttivi.

## C11 — HTTP client, API e networking

- URL/HTTP fundamentals;
- client HTTP;
- JSON API;
- headers/status/error model;
- timeout;
- retry/backoff con criterio;
- pagination;
- auth client-side;
- socket foundations;
- API server come specializzazione (es. FastAPI);
- validation/schema/OpenAPI nel track backend;
- idempotenza e boundary design.

## C12 — Concorrenza, parallelismo e async

- sequential vs concurrent vs parallel;
- I/O-bound vs CPU-bound;
- thread/process;
- `concurrent.futures`;
- event loop;
- `async`/`await`;
- coroutine/task;
- cancellation e timeout;
- synchronization/race conditions;
- structured concurrency concepts;
- async HTTP/DB dove realmente utile;
- benchmark prima di scegliere il modello.

## C13 — Logging, observability e operations

- `logging` e livelli;
- structured logging come estensione;
- correlation/request IDs;
- metriche;
- tracing concettuale;
- health/liveness/readiness;
- diagnostics senza leak di segreti;
- error reporting;
- runbook operativo;
- distinguere log applicativi, audit e telemetry.

## C14 — Security engineering di base

- input non fidato;
- SQL injection e parameter binding;
- command injection;
- path traversal;
- secret handling;
- dependency vulnerabilities;
- least privilege;
- temp files sicuri;
- deserialization risks;
- logging di dati sensibili;
- hashing/password concepts nel track web;
- secure defaults e fail-closed behavior.

## C15 — Performance e memoria

- misurare prima di ottimizzare;
- `timeit`;
- profiler;
- memory awareness;
- complessità;
- scelta strutture dati;
- lazy iteration;
- batching;
- caching con invalidation esplicita;
- DB query performance;
- evitare premature optimization.

## C16 — CLI, OS integration e automation

- `argparse` o framework CLI come specializzazione;
- exit codes;
- stdin/stdout/stderr;
- environment;
- filesystem;
- `subprocess` sicuro;
- signals/shutdown;
- cron/scheduling concepts;
- automazione ripetibile e idempotente.

## C17 — Git, collaboration e CI/CD

- branch/commit/merge/rebase a livello operativo;
- pull request;
- code review;
- issue-driven work;
- semantic commit discipline pragmatica;
- CI matrix;
- lint/type/test/build gates;
- artifact generation;
- release pipeline;
- rollback concepts;
- secrets in CI;
- dependency/update automation.

## C18 — Container e deployment

- processo vs container;
- Dockerfile;
- image layers;
- dependency/runtime separation;
- non-root execution;
- environment/config injection;
- health check;
- volumes/persistence;
- networking essenziale;
- immutable image/tag/digest concepts;
- local compose come estensione;
- deployment target specifico rinviato ai track applicativi.

## C19 — Design e maintainability

- cohesion/coupling;
- separation of concerns;
- dependency direction;
- pure core / impure shell come pattern utile;
- repository/service boundaries dove servono;
- API design;
- refactoring;
- design patterns solo se risolvono un problema osservabile;
- backward compatibility;
- deprecation;
- technical debt;
- architectural decision records per scelte importanti.

## C20 — Documentazione professionale

- README operativo;
- docstring utili;
- API docs;
- examples;
- architecture docs;
- changelog/release notes;
- troubleshooting;
- onboarding;
- documentare il perché, non duplicare il codice.

---

# Stage D — Applied Python / specializzazioni

Il core professionale alimenta track applicativi. Nessun singolo sviluppatore deve diventare specialista in tutti, ma deve possedere i foundation comuni.

Track selezionabili:

- automazione e scripting;
- web/API backend;
- database/data access;
- networking;
- data engineering/data science;
- cybersecurity/forensics in ambiente didattico sicuro;
- robotica/IoT;
- AI/ML;
- sistemi distribuiti;
- tooling/DevOps;
- CLI developer tooling.

---

# Capstone professionale

Il curriculum completo dovrebbe terminare con almeno un prodotto che richieda:

```text
analisi del problema
→ modello dati
→ architettura/package boundaries
→ ambiente riproducibile
→ pyproject + dipendenze
→ typing
→ lint/format
→ unit/integration tests
→ DB + SQL
→ ORM + migration se appropriati
→ API/CLI boundary
→ error handling + configuration
→ logging/health
→ CI
→ package/container artifact
→ documentazione
→ performance/security evidence
```

Il capstone deve essere eseguibile da un altro sviluppatore partendo dal repository e dalle istruzioni, non solo sulla macchina dell'autore.

---

# Fonti guida

- **Pensare in Python / Think Python**: problem solving e progressione beginner.
- **Imparare Python / Learning Python**: copertura sistematica del core language.
- **Fluent Python**: Python data model, idiomi, protocolli, funzioni, strutture dati e OOP pythonic.
- **Python in a Nutshell**: riferimento tecnico compatto e ponte al professionale.
- **Pluralsight Python Essentials / Core Python e corsi specialistici**: gap check e laboratori moderni.
- **Documentazione ufficiale Python e PyPA**: autorità normativa per linguaggio e packaging.
- **SQLAlchemy/Alembic docs**: reference canonico per DB toolkit/ORM/migrazioni.
- **pytest/Hypothesis docs**: reference per testing.
- **friedpython**: source pack legacy da auditare, non curriculum canonico.

# Python curriculum — catalogo fonti (DRAFT)

Questo documento cataloga le fonti usate per **progettare e verificare** il curriculum. Nessuna fonte viene copiata o seguita linearmente. La documentazione ufficiale resta autoritativa per sintassi, semantica e standard correnti.

## Legenda

- **P** — pedagogia/progressione per studenti;
- **C** — coverage/checklist di completezza;
- **I** — Python idiomatico/professionale;
- **R** — riferimento tecnico;
- **L** — laboratori/esercizi;
- **S** — source pack legacy.

---

## Libri

### Pensare in Python / Think Python — Allen Downey

**Ruolo:** P, L  
**Uso:** soprattutto Stage A / secondo anno.

Punti utili:

- problem solving e mentalità da informatico;
- funzioni, condizioni, iterazione;
- debugging continuo;
- stringhe e strutture dati;
- file;
- classi e oggetti.

Il curriculum aggiunge esplicitamente ciò che per noi deve essere più forte: algoritmi e flow chart prima del codice, scelta dei costrutti, composizione/annidamento, qualità della soluzione e progressione Activity.

Riferimenti pubblici:

- https://greenteapress.com/wp/think-python-3rd-edition/
- traduzione italiana storica: https://www.python.it/doc/Howtothink/Howtothink-html-it/index.htm

### Imparare Python / Learning Python — Mark Lutz

**Ruolo:** C, R  
**Uso:** verifica sistematica del core language e approfondimenti Stage B.

Aree da usare come checklist:

- built-in object types;
- statement e sintassi;
- funzioni/scope;
- moduli/package;
- OOP;
- eccezioni;
- iterators/comprehensions/generators;
- strumenti avanzati.

Non determina l'ordine del secondo anno: la copertura è molto più ampia del track beginner.

### Fluent Python, 2nd Edition — Luciano Ramalho

**Ruolo:** I, C, R  
**Uso:** Stage B/C e controllo della correttezza dei modelli mentali anche nelle spiegazioni beginner.

Aree chiave:

- Python data model;
- sequenze e unpacking;
- mapping/set/hashability;
- functions as objects;
- closures/decorators;
- iterables/iterators/generators;
- type hints;
- OOP pythonic;
- protocols/ABCs;
- concurrency/async.

Riferimento:

- https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

### Python in a Nutshell, 4th Edition — Martelli, Ravenscroft, Holden, McGuire

**Ruolo:** R, C, I  
**Uso:** Stage B/C.

Particolarmente utile come checklist compatta di:

- core language;
- control flow;
- functions/generators;
- OOP;
- type annotations;
- exceptions;
- standard library;
- file/text;
- networking/web;
- packaging/distribution.

Riferimento:

- https://www.oreilly.com/library/view/python-in-a/9781098113544/

---

# Fonti ufficiali

## Python documentation

**Ruolo:** R, autoritativa  
**Uso:** tutti gli stage.

- Tutorial: https://docs.python.org/3/tutorial/
- Language Reference: https://docs.python.org/3/reference/
- Library Reference: https://docs.python.org/3/library/
- HOWTO: https://docs.python.org/3/howto/
- Typing: https://typing.python.org/

La versione Python target viene fissata prima del Content Pack 1.0.

## Python Packaging Authority — PyPA

**Ruolo:** R, C  
**Uso:** Stage C1/C2/C17.

Da usare per:

- virtual environments e installazione;
- `pyproject.toml`;
- dependencies/dependency groups;
- build/distribution;
- wheel/sdist;
- package indexes;
- modern publishing.

- https://packaging.python.org/

## SQLAlchemy 2.x

**Ruolo:** R, I  
**Uso:** Stage C8/C9.

Progressione di riferimento:

```text
Engine/connectivity
→ transactions + DBAPI
→ metadata
→ CRUD/Core
→ ORM mappings
→ Session/unit of work
→ relationships
```

- https://docs.sqlalchemy.org/en/20/tutorial/

## Alembic

**Ruolo:** R  
**Uso:** Stage C10.

- migration environment;
- revision history;
- upgrade/downgrade;
- autogenerate con review;
- configuration anche via `pyproject.toml`.

- https://alembic.sqlalchemy.org/en/latest/

## pytest

**Ruolo:** R, L  
**Uso:** Stage C5.

- assertions;
- fixtures;
- parametrization;
- temporary resources;
- monkeypatching;
- integration testing patterns.

- https://docs.pytest.org/en/stable/

## Hypothesis

**Ruolo:** I, L  
**Uso:** Stage C5 avanzato.

Property-based testing per generare input, casi limite e verificare proprietà/invarianti.

- https://hypothesis.readthedocs.io/

## Ruff

**Ruolo:** R, tooling candidate  
**Uso:** Stage C3.

Linter + formatter moderno configurabile tramite `pyproject.toml`. È un candidato pratico per il toolchain del corso, non un concetto curricolare obbligatorio.

- https://docs.astral.sh/ruff/

## Pyright / typing tools

**Ruolo:** R, tooling candidate  
**Uso:** Stage C4.

Un checker statico deve far parte della pratica professionale; la scelta definitiva Pyright vs mypy resta una decisione di toolchain.

- https://github.com/microsoft/pyright
- https://mypy.readthedocs.io/

## uv

**Ruolo:** tooling candidate, L  
**Uso:** Stage C1/C2.

Workflow moderno per:

- interpreti/venv;
- dependencies;
- dependency groups;
- lock/sync;
- `pyproject.toml`;
- run/build.

Prima si insegnano i concetti standard `venv`/`pip`; poi il tool moderno. Il curriculum non deve diventare dipendente da un singolo package manager.

- https://docs.astral.sh/uv/

---

# Pluralsight — gap check e pratica

L'accesso disponibile viene usato per studiare e confrontare corsi/lab durante la produzione. Le fonti Pluralsight sono complementari, non canoniche.

## Python Essentials

**Ruolo:** C, L  
**Uso:** Stage A → C.

Copertura corrente utile:

- Foundations;
- Data Types and I/O;
- VS Code;
- Data Structures;
- Functions and Modules;
- OOP;
- File Operations;
- labs.

https://www.pluralsight.com/paths/python-essentials

## An Introduction to Algorithmics

**Ruolo:** P, C  
**Uso:** intuizioni PY2-05 e Stage B7.

Utile per introdurre algoritmi, strutture dati e costo computazionale con esempi e intuizione prima della formalizzazione matematica.

https://www.pluralsight.com/courses/algorithmics-introduction

## Python: Data Structures

**Ruolo:** C, L  
**Uso:** PY2-08/PY2-09 + Stage B.

Liste, tuple, set, dizionari e collection specializzate.

https://www.pluralsight.com/courses/python-data-structures

## Python: Object-oriented Programming

**Ruolo:** C, L  
**Uso:** PY2-11 + Stage B6.

Interessante in particolare la progressione dai dati in dizionari agli oggetti e alle classi.

https://www.pluralsight.com/courses/python-object-oriented-programming

## Python: Development Environments

**Ruolo:** C, L  
**Uso:** Stage C1.

Copertura: pip, ambienti virtuali e strumenti moderni quali uv/Poetry.

https://www.pluralsight.com/courses/python-development-environments

## uv Foundations

**Ruolo:** L, tooling  
**Uso:** Stage C1/C2.

https://www.pluralsight.com/courses/uv-foundations

## Guided: uv Development Workflows

**Ruolo:** L  
**Uso:** Stage C1/C2/C5.

Lab integrato su ambienti, dependencies, test e build di un package.

https://www.pluralsight.com/labs/codeLabs/guided-uv-development-workflows

## Python: Relational Database Integration

**Ruolo:** C, L  
**Uso:** Stage C8/C9.

Progressione utile: SQLite standard library → SQLAlchemy/ORM → transazioni → async → evoluzione del modello dati.

https://www.pluralsight.com/courses/python-relational-database-integration

## Python: Database Management with SQLAlchemy

**Ruolo:** C, L  
**Uso:** Stage C9/C10.

SQLAlchemy Core + ORM, CRUD, schema e Alembic migrations.

https://www.pluralsight.com/courses/python-database-management-sqlalchemy

## Python: Testing Strategies

**Ruolo:** C, I, L  
**Uso:** Stage C5.

pytest, unit/integration, test doubles, parametrization e design testabile.

https://www.pluralsight.com/courses/python-testing-strategies

## Unit Testing with Python 3

**Ruolo:** C, L  
**Uso:** Stage C5.

`unittest`, pytest, doctest, test doubles, parametrizzazione, coverage.

https://www.pluralsight.com/courses/using-unit-testing-python

## Python: Structuring Larger Projects with Modern Packaging

**Ruolo:** C, I  
**Uso:** Stage C2/C17/C19.

Project layout, dipendenze, CI/CD, packaging/distribution e architetture estensibili.

https://www.pluralsight.com/courses/python-structuring-larger-projects-modern-packaging

---

# Source pack legacy

## TheBitPoets/friedpython

**Ruolo:** S, L  
**Uso:** soprattutto PY2-07/08/09/10.

Materiale già presente:

- stringhe + esercizi;
- liste, slicing, metodi, matrici + esercizi;
- tuple;
- dizionari, iterazione, missing keys, ordering, matrici sparse + esercizi;
- file di testo/binari/context manager;
- verifiche PDF e raccolte cumulative.

Policy:

```text
friedpython
→ audit
→ classificazione
→ modernizzazione
→ test
→ trasformazione in Activity/microscope/problem
→ import selettivo in python-docente
```

Non copiare in blocco e non modificare `friedpython` per adattarlo al nuovo curriculum.

Repository: https://github.com/TheBitPoets/friedpython

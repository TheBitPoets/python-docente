# Python curriculum — raccomandazioni di progettazione (DRAFT)

Questo documento distingue le scelte già abbastanza mature da poter diventare default del progetto dalle decisioni che richiedono ancora un audit o una scelta esplicita.

Nessuna voce di questo documento costituisce ancora `CURRICULUM_FREEZE`.

## Raccomandazioni da trattare come default salvo obiezioni

### R1 — Architettura Stage → UDA → Modulo

Usare:

```text
Curriculum generale
└── Stage
    └── UDA
        └── Modulo
```

I track scolastici selezionano una porzione ordinata del curriculum senza duplicare la fonte canonica.

### R2 — Secondo anno: OOP fondamentale è core

Il corso di seconda deve arrivare realmente a:

- classe/istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato/comportamento;
- composizione semplice;
- responsabilità;
- mini-capstone.

Inheritance/dataclass/properties restano enrichment, non requisito minimo.

### R3 — Curriculum spirale

Non aspettare un capitolo unico per competenze trasversali:

- test case dal problem solving;
- trace dal flow chart;
- debug dal primo script;
- funzioni piccole già nei primi programmi;
- decomposizione formale più avanti;
- efficienza intuitiva dentro loop/strutture dati;
- spiegazione delle scelte durante tutto l'anno.

### R4 — Testing precoce

Progressione:

```text
casi di test su carta
→ input/output attesi
→ trace
→ assert semplici
→ test di funzioni
→ suite strutturate nei livelli successivi
→ pytest professionale
```

Il testing non è un argomento finale: è parte del metodo di programmazione.

### R5 — Loop espliciti prima delle comprehension

Le comprehension entrano solo quando lo studente sa già esprimere e spiegare la stessa trasformazione con un loop esplicito.

Nel secondo anno:

- comprehension semplice = INTRO/EXT;
- nested/advanced comprehension = Stage B.

### R6 — `match/case` dopo `if/elif/else`

Non usarlo come scorciatoia didattica. Prima lo studente padroneggia selezione, esclusività dei rami e logica booleana.

### R7 — Set nel core di seconda

Sì, con meno tempo di liste/dict, perché completa la capacità di scegliere una struttura dati in funzione di membership/unicità.

### R8 — Eccezioni in seconda: solo boundary essenziale

Core:

- errori prevedibili;
- `try/except` essenziale;
- input/file;
- distinzione tra dato non valido, risorsa assente e bug.

Gerarchie, custom exceptions, `else/finally`, EAFP/LBYL appartengono allo Stage B.

### R9 — File/persistenza non deve bloccare OOP

File di testo + `with open` + UTF-8 + `pathlib` introduttivo sono core piccolo.

CSV/JSON/binario sono enrichment/Stage B se il calendario è stretto.

### R10 — Database professionale: SQL prima dell'ORM

Progressione target:

```text
SQL fundamentals
→ sqlite3 / DB-API
→ transazioni
→ repository/data access
→ SQLAlchemy Core
→ SQLAlchemy ORM
→ relazioni/session lifecycle
→ Alembic
→ async DB nei track appropriati
```

L'ORM non deve nascondere la comprensione di query, transazioni e schema.

### R11 — Standard/concept prima del tool

Esempio:

```text
virtual environment concept
→ venv/pip come baseline standard
→ pyproject/dependency graph/lock
→ tool moderno scelto (es. uv)
```

Analogo principio per lint, typing, ORM, CI e packaging.

Questo rende il curriculum stabile anche se cambia il tool pratico.

### R12 — Delivery standard derivato da TPSI5

Riutilizzare, adattando la densità all'età:

- lesson canonica;
- slide modulari;
- student guide;
- teacher guide;
- Activity A–F;
- starter;
- solution/reference;
- rubric/manual evidence;
- HTML/PDF/PPTX riproducibili;
- Quality CI;
- TheBitLab handoff;
- curriculum freeze vs delivery changelog.

## Decisioni che restano realmente aperte

### O1 — Versione Python target 2026/27

**Raccomandazione provvisoria:** scegliere una versione stabile compatibile con il runner TheBitLab e disponibile uniformemente nei laboratori, evitando di rendere il curriculum dipendente da feature troppo recenti.

Da verificare prima del freeze.

### O2 — Flow chart toolchain

Possibile modello ibrido:

- carta/lavagna per apprendimento immediato;
- tool visuale per consegne strutturate;
- formato versionabile soltanto quando non aumenta il carico cognitivo.

Da confrontare almeno: diagrams.net, Flowgorithm e Mermaid/alternative.

### O3 — Progetto longitudinale

Raccomandazione candidata:

```text
micro-progetti indipendenti nel primo nucleo
→ spine longitudinale dal blocco funzioni in poi
→ Romeo simulato come candidato forte del secondo semestre
```

Non congelare Romeo finché non verifichiamo che il boundary/simulatore sia semplice, testabile e non richieda hardware.

### O4 — Git nel secondo anno

Raccomandazione candidata:

- non usarlo come prerequisito iniziale;
- introdurre un toolbox minimo nel secondo semestre (`status`, `diff`, `add`, `commit`) se il flusso di laboratorio lo rende utile;
- Git completo diventa core nel percorso avanzato/professionale.

### O5 — Tool profile professionale

Candidati attuali:

- env/project/deps: standard `venv`/`pip`, workflow moderno candidato `uv`;
- lint/format: Ruff;
- typing: Pyright o mypy;
- tests: pytest;
- property based: Hypothesis;
- DB/ORM: SQLAlchemy 2.x;
- migrations: Alembic.

Questi sono **tool profile**, non concetti curricolari immutabili. Vanno versionati separatamente.

### O6 — TheBitLab contract per `python-docente`

Da definire dopo l'approvazione architetturale:

- versione runner Python;
- Activity schema;
- sandbox;
- test pubblici/privati;
- limiti risorse;
- output/evidence;
- flow chart/manual evidence;
- import di Activity da `friedpython`;
- policy di fallback.

### O7 — Distribuzione Stage B/C negli anni successivi

Non serve per congelare il secondo anno.

La roadmap deve però continuare a contenere l'intero profilo professionale, così il materiale di seconda non crea vicoli ciechi o modelli che dovremo disimparare.

## Criterio di freeze

Prima di creare in massa lesson/slide/Activity del Content Pack 1.0, devono essere risolte almeno:

- O1 Python target;
- O2 flow chart workflow;
- O3 progetto longitudinale;
- O6 contract TheBitLab.

O4/O5 possono essere congelate come profili di delivery/tooling con più facilità di revisione rispetto al curriculum.

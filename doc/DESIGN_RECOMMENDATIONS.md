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

### R13 — IDE unico: VS Code, semplificato per il secondo anno

Default proposto:

- VS Code fin dall'inizio;
- Python extension ufficiale;
- profilo del corso minimale, senza estensioni AI durante le Activity valutative;
- terminale, debugger e test introdotti progressivamente;
- stesso ambiente riutilizzato nei livelli professional per virtual environment, pytest, linting, typing e Git.

Motivo: evitare una migrazione artificiale da un IDE beginner-only a un ambiente professionale dopo pochi mesi. La complessità dell'interfaccia viene ridotta dalla configurazione del corso, non cambiando strumento.

## Decisioni che restano realmente aperte

### O1 — Baseline Python 2026/27

**Raccomandazione aggiornata:** separare il contratto del linguaggio dal runtime di laboratorio.

```text
core curriculum compatibility: Python 3.12–3.14
reference/current local interpreter: Python 3.14.x
TheBitLab runner: versione certificata separatamente
CI curriculum: almeno Python 3.12 + 3.14
```

Il core di seconda non deve dipendere da feature introdotte soltanto in 3.13/3.14. In questo modo gli esempi restano riproducibili sul runner scolastico e contemporaneamente il corso può usare l'interprete stabile corrente sui PC.

Fatto tecnico rilevante al 2026-08-23: Python 3.14 è la serie stabile più recente; il TheBitLab corrente dichiara ancora `minimum-python = 3.11` e `recommended-python = 3.12`. Prima del freeze va eseguita una smoke reale su 3.14 e deciso il runner certificato di `python-docente`.

### O2 — Flow chart workflow

**Raccomandazione aggiornata:** modello ibrido carta + Flowgorithm.

1. carta/lavagna per imparare simboli e progettare senza dipendere dal software;
2. Flowgorithm come tool digitale principale, perché permette esecuzione passo-passo, osservazione delle variabili e traduzione del diagramma anche verso Python;
3. l'eventuale codice Python generato dal tool è materiale di confronto, non una consegna accettabile al posto della codifica dello studente;
4. esportazione del diagramma come evidence; diagrams.net resta fallback grafico se Flowgorithm non è installabile;
5. Mermaid non è richiesto ai principianti: potrà servire più avanti per documentazione versionabile.

Questa proposta dipende da una conferma pratica: i PC del laboratorio devono poter eseguire/installare Flowgorithm.

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

### O8 — Vincoli reali del laboratorio scolastico

Da raccogliere prima del freeze:

- Windows/Linux e versioni;
- diritti di installazione;
- accesso Internet durante laboratorio/verifiche;
- VS Code/Python già installati o immagine da predisporre;
- possibilità di installare Flowgorithm;
- disposizione delle 3 ore settimanali (3 consecutive, 2+1, altro);
- uso individuale o condiviso delle postazioni.

Questi dati non cambiano gli obiettivi del curriculum, ma cambiano molto la delivery e il tipo di Activity realisticamente sostenibile.

## Criterio di freeze

Prima di creare in massa lesson/slide/Activity del Content Pack 1.0, devono essere risolte almeno:

- O1 Python baseline/runner;
- O2 flow chart workflow;
- O3 progetto longitudinale;
- O6 contract TheBitLab;
- O8 vincoli reali del laboratorio almeno per quanto noto.

O4/O5 possono essere congelate come profili di delivery/tooling con più facilità di revisione rispetto al curriculum.

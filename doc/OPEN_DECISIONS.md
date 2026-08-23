# Python curriculum — decisioni aperte (DRAFT)

Questo documento impedisce che scelte importanti vengano fatte implicitamente durante la produzione dei contenuti.

## D1 — Versione Python target

Da decidere prima del Content Pack 1.0.

Criteri:

- versione stabile e supportata per tutto l'anno scolastico;
- disponibilità uniforme su Windows/Linux e TheBitLab;
- compatibilità con tooling e dipendenze del corso;
- nessuna dipendenza didattica da feature troppo recenti se non necessarie.

## D2 — Confine OOP del secondo anno

Proposta corrente:

**core:** classi, istanze, attributi, `self`, `__init__`, metodi, stato/comportamento, composizione semplice, responsabilità di classe, mini-capstone.

**extension:** `__str__/__repr__`, properties introduttive, inheritance semplice, dataclass come confronto.

Da approvare.

## D3 — Progetto longitudinale

Candidati:

1. **Romeo / robot simulato**;
2. applicazione CLI crescente;
3. gioco/avventura testuale;
4. dominio gestionale/dataset;
5. micro-progetti + capstone finale senza un unico progetto annuale;
6. modello ibrido: micro-progetti nel primo quadrimestre + Romeo/capstone nel secondo.

Criteri:

- deve funzionare senza hardware fisico;
- deve crescere insieme alle competenze;
- non deve introdurre framework prima dei concetti fondamentali;
- deve essere testabile in CI/TheBitLab almeno in parte;
- deve motivare studenti di seconda.

## D4 — Flow chart tooling

Da scegliere:

- carta + simboli standard;
- diagrams.net/draw.io;
- Flowgorithm o strumento didattico equivalente;
- Mermaid per versionabilità;
- approccio misto.

Criteri: facilità per principianti, esportabilità, versionabilità, uso a scuola e valutazione.

## D5 — Introduzione di Git nel secondo anno

Opzioni:

- nessun Git nel core, repository gestito da piattaforma/docente;
- Git minimo nel secondo quadrimestre (`clone/status/add/commit`);
- Git come extension per studenti pronti.

Il curriculum professionale lo considera obbligatorio; resta da decidere quando introdurlo.

## D6 — Toolchain professionale

Concetti obbligatori:

- `venv`/isolamento;
- package/dependency management;
- `pyproject.toml`;
- formatter/linter;
- static type checker;
- pytest;
- build/package.

Candidati pratici attuali:

- project/dependency manager: **uv**;
- lint/format: **Ruff**;
- typing: **Pyright** o **mypy**;
- tests: **pytest**;
- property-based: **Hypothesis**;
- DB/ORM: **SQLAlchemy 2.x**;
- migrations: **Alembic**.

Regola proposta: insegnare prima lo standard/concept, poi il tool scelto. Tool sostituibili senza cambiare il curriculum.

## D7 — Database nel percorso pluriennale

Proposta:

```text
SQL fundamentals
→ sqlite3 / DB-API
→ repository/data access
→ SQLAlchemy Core
→ SQLAlchemy ORM
→ Alembic
→ async DB in track avanzato
```

Da coordinare con eventuale corso SQL/TPSI per evitare duplicazioni inutili mantenendo il curriculum Python autosufficiente.

## D8 — Testing: quanto presto?

Proposta:

- secondo anno: casi di test fin dal problem solving; `assert`/test deterministici dopo le funzioni;
- advanced: test suite strutturate;
- professional: pytest, fixtures, parametrizzazione, integration/E2E, coverage, property-based.

Da approvare come standard trasversale.

## D9 — `match/case`

Proposta: non usarlo per evitare di imparare bene `if/elif/else`; introdurlo solo dopo la padronanza della selezione e come extension/pattern matching quando porta valore.

## D10 — Comprehensions

Proposta: loop espliciti prima; comprehension semplice in seconda soltanto dopo piena padronanza dell'iterazione; comprehension annidate/avanzate in Stage B.

## D11 — Set nel secondo anno

Proposta: sì, perché completa la capacità di scegliere strutture dati e rende naturale membership/unicità. Meno tempo rispetto a liste/dict.

## D12 — Eccezioni nel secondo anno

Proposta: solo `try/except` essenziale attorno a input/file e distinzione tra errori prevedibili e bug. Gerarchie, custom exceptions, `else/finally`, EAFP/LBYL in Stage B.

## D13 — TheBitLab

Da fissare dopo l'architettura:

- Activity schema/contract;
- Python runner version;
- sandbox policy;
- autograding boundaries;
- diagrammi/flow chart e spiegazioni come rubric/manual evidence;
- import selettivo di `friedpython` come Activity.

Non progettare esercizi intorno a capability non ancora verificate.

## D14 — Tassonomia UDA/moduli

La roadmap Stage A contiene A0–A10, mentre il track secondo propone 11 UDA PY2-01..PY2-11. Da decidere se:

- una UDA = una macro-area;
- ogni UDA contiene più moduli/lesson;
- mantenere numerazione indipendente per track e curriculum.

Proposta: **Stage → UDA → moduli**, con 2–4 moduli per UDA quando serve. Evitare una lesson enorme per ogni UDA.

## D15 — Standard slide e guide

Proposta: riutilizzare lo standard TPSI5:

- slide per modulo;
- HTML/PDF/PPTX riproducibili;
- `student/README.md`;
- `teacher/README.md`;
- lesson runbook;
- assessment guide;
- TheBitLab handoff;
- delivery changelog;
- curriculum freeze.

Da adattare a studenti più giovani: meno densità per slide, più trace visuale, animazione concettuale e problemi guidati.

## D16 — Livello “professionale” e track scolastici successivi

La roadmap completa è più ampia di un singolo anno. Da decidere in seguito come distribuirla tra:

- terzo anno;
- quarto anno;
- quinto anno;
- corsi opzionali;
- percorsi personali avanzati.

Non serve decidere questa distribuzione per approvare il track di seconda, ma non bisogna eliminare dalla roadmap le competenze future.

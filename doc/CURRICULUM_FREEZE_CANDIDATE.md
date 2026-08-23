# Python secondo — Curriculum Freeze Candidate 2026/27

> Stato: **CANDIDATE — curriculum architecture**.
>
> Questo documento non dichiara `Content Pack 1.0.0 / approved` e non dichiara la piattaforma pronta agli studenti. Congela soltanto la proposta di **cosa insegnare, in quale progressione e con quali outcome core** dopo la review architetturale.

## Candidate identity

```text
track: python-secondo-2026-2027
33 settimane
3 ore/settimana
2 ore teoria attiva + 1 ora laboratorio
99 ore nominali
Python baseline didattica: 3.12
```

## Struttura candidata

| Finestra | UDA | Core |
|---|---|---|
| 1–3 | PY2-01 | problem solving, algoritmi, pseudocodice, flow chart, trace, test case |
| 4–5 | PY2-02 | REPL, script, valori/tipi, variabili, input/output, conversioni, operatori |
| 6–8 | PY2-03 | booleani, confronti, if/else/elif, logica, annidamento, validazione |
| 9–12 | PY2-04 | while, for/range, sentinelle, contatori, accumulatori, ricerca, nested loops |
| 13–16 | PY2-05 | funzioni, return, scope locale, composizione, top-down, assert, regression/refactor |
| 17 | Checkpoint A | recupero/verifica/mini-project + primo checkpoint Git guidato |
| 18–20 | PY2-06 | stringhe, slicing, immutabilità, metodi, algoritmi/parsing semplice |
| 21–23 | PY2-07 | liste, mutabilità, alias/copia, tuple, unpacking, matrici |
| 24 | Checkpoint B | consolidamento/valutazione/mini-project |
| 25–27 | PY2-08 | set, dict, lookup/frequenze, strutture composte, scelta data model |
| 28 | PY2-09 | pathlib, file testo UTF-8, with/open, error boundary essenziale |
| 29–32 | PY2-10 | classi/istanze, self, init, stato/metodi/invarianti, composizione, capstone |
| 33 | Checkpoint C | finalizzazione/recupero/enrichment; nessun prerequisito nuovo |

Core UDA: **90 ore nominali**.  
Checkpoint/buffer espliciti: **9 ore**.

---

# Outcome obbligatori di uscita

Lo studente che completa il track core deve saper:

1. leggere un problema semplice e individuare input/output/vincoli;
2. progettare una soluzione tramite algoritmo/pseudocodice/flow chart quando appropriato;
3. eseguire trace e progettare casi normali/limite;
4. tradurre l'algoritmo in Python 3.12;
5. leggere input, convertire tipi, produrre output;
6. costruire selezioni semplici, multiple, composte e annidate;
7. distinguere condizioni indipendenti e casi mutuamente esclusivi;
8. scegliere `for` o `while` e motivarlo;
9. comporre selezioni/cicli, inclusi semplici cicli annidati;
10. usare contatori, accumulatori, sentinelle, min/max progressivo e ricerca;
11. decomporre un problema in funzioni;
12. distinguere parametro/argomento e `return`/`print`;
13. passare dati esplicitamente e comprendere scope locale essenziale;
14. scrivere semplici `assert`, diagnosticare bug e aggiungere un regression test;
15. usare stringhe come sequenze immutabili;
16. usare liste/tuple comprendendo mutabilità, alias e copia;
17. usare set/dizionari e strutture annidate;
18. scegliere `str/list/tuple/set/dict` in funzione delle operazioni dominanti;
19. comprendere intuizioni elementari sul costo del lavoro senza formalismo Big-O;
20. leggere/scrivere file di testo in workspace usando `pathlib`, UTF-8 e context manager;
21. distinguere errori esterni prevedibili da bug del programma;
22. definire classi/istanze, attributi, `self`, `__init__`, metodi e stato;
23. mantenere invarianti semplici;
24. usare composizione tra oggetti;
25. realizzare un piccolo capstone OOP testabile e spiegabile.

---

# Decisioni curricolari candidate al freeze

## C1 — Curriculum a spirale

- test case dal problem solving;
- trace dal flow chart;
- debugging dal primo script;
- piccole funzioni mostrate presto, formalizzate in PY2-05;
- efficienza contestuale dentro loop/data structure;
- confronto fra soluzioni durante tutto l'anno.

## C2 — OOP è core

Obbligatori:

- classe/istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato/comportamento;
- invarianti semplici;
- più istanze indipendenti;
- composizione/responsabilità;
- capstone.

Enrichment:

- `__str__/__repr__`;
- property;
- inheritance semplice;
- dataclass solo dopo classe esplicita.

## C3 — Loop espliciti prima delle comprehension

Comprehension semplice = enrichment/preview soltanto dopo padronanza del loop equivalente.

## C4 — `match/case` non sostituisce `if/elif/else`

Può comparire soltanto come enrichment quando risolve un problema reale meglio della selezione già padroneggiata.

## C5 — Data structure choice è outcome core

Non basta conoscere i metodi delle collezioni. Lo studente deve motivare la scelta in base a:

- ordine;
- mutabilità;
- duplicati/unicità;
- membership;
- lookup per chiave;
- struttura/record;
- operazioni previste.

## C6 — File/error handling resta piccolo

3 ore core per non compromettere OOP. CSV/JSON/binario/eccezioni avanzate sono Stage B/enrichment.

## C7 — Testing non è un capitolo finale

Progressione:

```text
paper cases
→ stdin/stdout
→ assert
→ regression thinking
→ direct function/object/filesystem grading quando la piattaforma lo supporta
→ pytest nel curriculum professionale
```

## C8 — Git è curriculum separato ma G1 entra nel workflow

Python seconda introduce soltanto G1:

- status;
- diff;
- add;
- commit;
- log/history essenziale.

Introduzione progressiva da PY2-05; primo commit guidato al Checkpoint A. Non dipende dalla settimana 33.

## C9 — Container è curriculum separato

Il track di seconda non introduce container come argomento obbligatorio. Il curriculum professionale Python consumerà container literacy dal futuro corso Container/Docker.

## C10 — Romeo è spine selettiva, non syllabus

Romeo entra soprattutto in:

- condizioni;
- cicli;
- funzioni/decomposizione/debug;
- OOP/capstone.

Non viene forzato in stringhe/set/dict/file.

Core sempre completabile senza hardware fisico. Capstone generico equivalente disponibile se `romeo-sim` non è certificato.

---

# Decisioni di metodo/delivery che NON cambiano il curriculum

Queste possono evolvere come profili/strumenti senza riaprire C1–C10 finché gli outcome restano invariati:

- versione patch Python del Classroom Environment;
- VS Code managed integration;
- Flowchart Lab implementation/UX;
- grader P1/P2/P3/P4;
- runtime plugin Romeo;
- slide tooling;
- Course Board UX;
- Git UI/CLI presentation;
- exact Activity count.

---

# Blocker di delivery ancora aperti

## B1 — Classroom Environment

`python-docente#2` / `TheBitPoets/2cornot2c#753/#754`.

## B2 — Course Workspace UX / bundle inspection

`TheBitPoets/2cornot2c#755`.

## B3 — P1 vertical slice

`python-docente#7`.

Runner generico esiste, ma il consumer course non è ancora certificato. Gli ultimi run Actions osservati falliscono pre-execution senza step eseguiti; non sono una prova di failure del grader.

## B4 — P2 function behavior

`TheBitPoets/2cornot2c#756`.

## B5 — P4 filesystem behavior

`TheBitPoets/2cornot2c#757`.

## B6 — P3 object behavior

`TheBitPoets/2cornot2c#758`.

## B7 — Flowchart Lab

Architecture in PR #754; manual/paper flowchart evidence resta fallback valido.

## B8 — Romeo cross-profile certification

Il mapping curricolare è completato; runtime install/probe/launch/run deve essere certificato nel Classroom Environment prima di essere core delivery.

---

# Cosa non è ancora congelato

- testo finale delle lesson;
- numero esatto delle Activity per modulo;
- esercizi `friedpython` da importare dopo audit individuale;
- slide finali;
- rubric weights definitivi oltre il modello approvato;
- variante concreta del capstone OOP;
- distribution degli Stage B/C tra terzo/quarto/quinto;
- tool profile professionale futuro.

Questi elementi possono essere progettati sopra il curriculum candidate senza cambiare gli outcome core.

---

# Gate per promuovere CANDIDATE → FROZEN

1. nessuna obiezione didattica emersa dalla review delle 10 SPEC;
2. Course Design e Content Pack indicizzano le stesse SPEC/review;
3. mapping Romeo completato — **DONE**;
4. Git G1 integration completata — **DONE**;
5. architecture review completata — **DONE**;
6. nessun nuovo gap core emerso — **DONE nella review corrente**;
7. decision owner approva esplicitamente il freeze.

Il freeze del curriculum può precedere la certificazione completa di B1–B8; il `Content Pack 1.0.0 / approved` e la dichiarazione "ready for classroom" no.

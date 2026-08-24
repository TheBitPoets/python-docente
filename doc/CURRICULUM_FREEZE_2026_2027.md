# Python secondo — Curriculum Freeze 2026/27

> Stato: **FROZEN — curriculum architecture**  
> Approvazione decision owner: **2026-08-24**  
> Track: `python-secondo-2026-2027`

Questo documento congela **cosa insegnare, in quale progressione e con quali outcome core** per il track Python di seconda 2026/27.

Non dichiara:

- `Content Pack 1.0.0 / approved`;
- piattaforma pronta agli studenti;
- grading P1/P2/P3/P4 certificato;
- `romeo-sim` certificato in tutti i profili;
- GO pilot/classroom-ready.

Questi restano gate di authoring/delivery successivi e possono evolvere senza riaprire il curriculum finché non cambiano gli outcome congelati.

## Identità congelata

```text
track: python-secondo-2026-2027
33 settimane
3 ore/settimana
2 ore teoria attiva + 1 ora laboratorio
99 ore nominali
30 settimane core = 90 ore
3 checkpoint/buffer = 9 ore
Python baseline didattica iniziale: 3.12
```

## Struttura congelata

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

## Outcome obbligatori congelati

Lo studente che completa il track core deve saper:

1. leggere un problema semplice e individuare input/output/vincoli;
2. progettare una soluzione tramite algoritmo/pseudocodice/flow chart quando appropriato;
3. eseguire trace e progettare casi normali/limite;
4. tradurre l'algoritmo in Python 3.12-compatible;
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
20. leggere/scrivere file di testo usando `pathlib`, UTF-8 e context manager;
21. distinguere errori esterni prevedibili da bug del programma;
22. definire classi/istanze, attributi, `self`, `__init__`, metodi e stato;
23. mantenere invarianti semplici;
24. usare composizione tra oggetti;
25. realizzare un piccolo capstone OOP testabile e spiegabile.

## Decisioni curricolari congelate

### C1 — Curriculum a spirale

- test case dal problem solving;
- trace dal flow chart;
- debugging dal primo script;
- piccole funzioni mostrate presto, formalizzate in PY2-05;
- efficienza contestuale dentro loop/data structure;
- confronto fra soluzioni durante tutto l'anno.

### C2 — OOP è core

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

### C3 — Loop espliciti prima delle comprehension

Le comprehension semplici possono comparire solo dopo la padronanza del loop equivalente e non sostituiscono il core esplicito.

### C4 — `match/case` non sostituisce `if/elif/else`

Può comparire come enrichment quando risolve un problema reale meglio della selezione già padroneggiata.

### C5 — Scelta della struttura dati è outcome core

Lo studente deve motivare `str/list/tuple/set/dict` in base a ordine, mutabilità, duplicati/unicità, membership, lookup per chiave, struttura/record e operazioni previste.

### C6 — File/error handling resta piccolo

Tre ore core per non compromettere OOP. CSV/JSON/binario/eccezioni avanzate restano Stage B/enrichment.

### C7 — Testing è progressivo

```text
paper cases
→ stdin/stdout
→ assert
→ regression thinking
→ direct function/object/filesystem grading quando supportato
→ pytest nel curriculum professionale
```

### C8 — Git è curriculum separato; G1 entra nel workflow

Python seconda consuma soltanto:

- `status`;
- `diff`;
- `add`;
- `commit`;
- `log`/history essenziale.

Introduzione progressiva da PY2-05; primo commit guidato al Checkpoint A.

### C9 — Container è curriculum separato

Nessun modulo Container/Docker obbligatorio in seconda. Il curriculum Python professionale consumerà container literacy dal corso Container dedicato.

### C10 — Romeo è spine selettiva, non syllabus

Uso forte soprattutto in condizioni, cicli, funzioni/decomposizione/debug e OOP/capstone. Non viene forzato in stringhe, set/dict o file. Il core deve essere completabile senza hardware fisico.

## Metodo di delivery che può cambiare senza riaprire il freeze

Finché gli outcome precedenti non cambiano, possono evolvere:

- patch/minor runtime compatibile del Classroom Environment;
- managed VS Code workflow;
- Flowchart Lab implementation/UX;
- grader P1/P2/P3/P4;
- runtime plugin Romeo;
- slide tooling;
- Course Board UX;
- Git UI/CLI presentation;
- numero esatto di Activity per modulo.

## Elementi non congelati

Restano editoriali/delivery:

- testo finale delle lesson;
- numero esatto e forma finale delle Activity;
- esercizi `friedpython` selezionati dopo audit individuale;
- slide finali;
- pesi rubric definitivi entro il modello approvato;
- variante concreta del capstone OOP;
- distribuzione Stage B/C tra terzo/quarto/quinto;
- tool profile professionale futuro.

## Change-control dopo il freeze

Riaprire il curriculum solo se una modifica cambia uno o più di:

- outcome obbligatori;
- prerequisiti core;
- ordine necessario delle UDA;
- monte ore/core-vs-enrichment in modo sostanziale;
- presenza obbligatoria dell'OOP;
- ruolo curricolare di Git/Container/Romeo;
- criteri fondamentali di problem solving/testing/data-structure choice.

Correzioni editoriali, lesson, slide, Activity, rubric, tooling, runner e UX restano **delivery changes** se rispettano il curriculum congelato.

## Blocker delivery noti al momento del freeze

- `python-docente#2` — Classroom Environment;
- `python-docente#6` — beginner REPL/editor workflow;
- `python-docente#7` — P1 vertical slice certification;
- `python-docente#8` — GitHub Actions pre-execution failure;
- `2cornot2c#753/#754` — environment contract + Flowchart Lab;
- `2cornot2c#755` — Course Workspace/Open course UX;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior;
- `romeo-sim` cross-profile certification.

Questi blocker **non riaprono il curriculum**; bloccano i rispettivi livelli di delivery/autograding/readiness.

## Gate successivi

### Content Pack `1.0.0 / approved`

Richiede contenuti revisionati, provenance/coverage, teacher review e almeno il vertical slice end-to-end certificato.

### Ready for classroom / GO pilot

Richiede rehearsal reale del Classroom Environment/TheBitLab. Non deriva automaticamente né dal freeze né dalla CI.

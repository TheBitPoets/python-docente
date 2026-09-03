# Python curriculum — decisioni approvate 2026/27

> Stato: **registro storico pre-freeze, riallineato alle decisioni congelate**.  
> Il documento canonico corrente è `doc/CURRICULUM_FREEZE_2026_2027.md` (FROZEN, decision-owner approval 2026-08-24).

Questo file conserva le decisioni maturate durante il design. In caso di conflitto, prevale il Curriculum Freeze.

## D1 — Ambiente didattico unico

Tutti i corsi TheBitPoets devono usare il **Classroom Environment gestito da TheBitLab / 2cornot2c** come percorso supportato per gli studenti, sia a scuola sia sui PC personali.

Non sono ammessi prerequisiti impliciti del tipo “installa manualmente sul PC il tool X” se quel tool non fa parte del percorso installa/ripara di TheBitLab.

Il modello corrente prevede:

- host Windows/macOS;
- profilo Docker student-dev leggero per macchine con poca RAM;
- VM Linux grafica per il profilo completo;
- workspace condiviso;
- runner di grading separato;
- runtime plugin esterni per capability specialistiche come `romeo-sim`.

Delivery/certification: `TheBitPoets/2cornot2c#753` e issue correlate.

## D2 — Python baseline del track di seconda

Il Content Pack iniziale usa **Python 3.12** come baseline didattica certificabile.

Regole:

- niente feature obbligatorie introdotte solo in Python 3.13/3.14;
- il codice può essere testato anche su versioni più recenti come forward-compatibility;
- la versione effettiva del laboratorio appartiene al profilo ambiente TheBitLab, non al curriculum concettuale.

## D3 — Orario reale: 2 teoria + 1 laboratorio

Il secondo anno ha tre ore settimanali:

- **2 ore di teoria/classe**;
- **1 ora di laboratorio**.

Il corso resta volutamente pratico. “Ora di teoria” non significa lezione frontale continua: quando disponibili i portatili si usano REPL, trace, micro-esercizi, guided coding, debugging, confronto tra soluzioni e brevi Activity.

L'ora di laboratorio privilegia esercizi più lunghi, Activity C/D/E/F, consegne, Romeo simulato, prove pratiche e progetto.

## D4 — REPL → script → editor

Progressione approvata:

1. primi concetti con il REPL standard `python`;
2. transizione precoce a file `.py`;
3. VS Code come editor di lungo periodo quando installazione/configurazione sono gestite dal Classroom Environment;
4. debugger introdotto solo quando è didatticamente utile;
5. IPython opzionale e non requisito core finché non è parte del profilo certificato.

## D5 — Flow chart

Il flow chart è **core curricolare**.

Flowgorithm può essere riferimento/companion Windows, ma non dipendenza canonica.

Target architetturale: **Flowchart Lab cross-platform gestito da TheBitLab**, browser-based e salvabile nel workspace studente.

Capability desiderate:

- sequenza, input/output, selezione, cicli, funzioni;
- annidamento;
- esecuzione/step-by-step;
- variable watch;
- input/output deterministico;
- artifact versionabile;
- export SVG/immagine;
- collegamento pseudocodice/Python solo quando pedagogicamente opportuno;
- validazione strutturale automatica dove deterministica;
- qualità progettuale valutata con rubric/manual checks.

Delivery blocker: `TheBitPoets/2cornot2c#753/#754`.

## D6 — Romeo

Romeo è approvato come **filo applicativo ricorrente**, non come curriculum alternativo.

Modello:

```text
problemi generali e micro-progetti
+ missioni Romeo simulate ricorrenti
+ capstone OOP con Romeo simulato o fallback generico equivalente
```

Vincoli:

- ogni concetto Python deve avere anche esercizi generali/non-Romeo;
- hardware fisico mai necessario per completare il core;
- usare `romeo-sim` attraverso il boundary TheBitLab;
- non importare nel secondo anno beginner la parte networking/FastAPI/WebSocket dell'attuale curriculum Romeo year 2.

Mapping corrente: `tracks/secondo/ROMEO_MAPPING.md`.

## D7 — Git nel secondo anno

**Decisione finale congelata:** Git è un curriculum trasversale separato; Python seconda consuma il sottoinsieme G1 necessario al proprio workflow e non duplica le lesson Git.

Source of truth corrente:

```text
TheBitPoets/git
G1 candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
provider contract: doc/G1_CONSUMER_CONTRACT.md
```

Consumer Python machine-readable:

```text
config/git-g1-consumer.json
```

Progressione:

```text
M14–M16
  status / diff — guided

Checkpoint A
  status
  → diff
  → test
  → add
  → diff --staged
  → commit
  → status
  → log/show

secondo semestre
  checkpoint/recovery G1 progressivamente autonomi
```

Branching, merge, remotes, PR, rebase, reflog e internals restano fuori dal core Python di seconda.

Il materiale Git legacy è stato auditato nel repository Git ed è fonte pedagogica privata, non lesson canonica.

## D8 — OOP obbligatoria in seconda

La OOP è parte del core, non enrichment finale.

Obbligatorio:

- classe vs istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato + comportamento;
- istanze indipendenti;
- composizione semplice;
- responsabilità di classe;
- mini-capstone.

`__str__/__repr__`, ereditarietà semplice, properties e dataclass restano enrichment secondo il Curriculum Freeze.

## D9 — Valutazioni minime

Per ogni quadrimestre devono essere previste almeno:

- **1 prova teorica/scritta**;
- **1 prova pratica o pratica/scritta**.

Il corso raccoglie comunque evidenze formative più frequenti: trace, flow chart, coding, debug, spiegazione delle scelte, mini-progetti e Activity.

Il calendario/rubriche correnti sono nei file del track `tracks/secondo/`.

## D10 — Policy AI

Nei fondamenti e nelle verifiche core non è consentito usare AI generativa per produrre la soluzione.

Più avanti sono ammesse Activity controllate di AI-assisted review/debugging, con obbligo per lo studente di:

- verificare;
- testare;
- correggere;
- spiegare il codice e le scelte.

L'AI non sostituisce la capacità di progettare algoritmo, trace e soluzione.

## D11 — Standard di delivery

Riutilizzare lo standard maturato con TPSI5, adattato a studenti più giovani:

- lesson canoniche;
- slide modulari meno dense e più visuali;
- student guide;
- teacher guide;
- Activity A–F;
- starter;
- solution/reference;
- rubric/manual evidence;
- CI/Quality;
- TheBitLab handoff;
- curriculum freeze separato dal delivery changelog.

M04–M30 sono oggi materializzati editorialmente; ciò non equivale a Content Pack approved o classroom-ready.

---

# Stato dei vecchi blocker “prima del freeze”

La lista storica è stata superata dal freeze del 2026-08-24. Gli elementi ancora aperti sono oggi **delivery gates**, non decisioni curricolari pre-freeze:

1. Classroom Environment / Flowchart Lab (`2cornot2c#753/#754`, `python-docente#2`);
2. beginner REPL/editor certification (`python-docente#6`);
3. P1 canary (`python-docente#7`);
4. private Actions pre-runner blocker (`python-docente#8`);
5. P2/P3/P4 (`2cornot2c#756/#758/#757`);
6. Git G1 consumer CI/rehearsal evidence;
7. `romeo-sim` cross-profile certification;
8. slide artifact build/quality;
9. teacher/provenance/coverage review;
10. Content Pack approval e rehearsal reale.

Per lo stato operativo corrente usare `doc/PROJECT_STATUS.md`.

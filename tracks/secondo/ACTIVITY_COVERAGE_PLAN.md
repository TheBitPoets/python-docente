# Python secondo — Activity & Evidence Coverage Plan

> Stato: **planning contract / no mass materialization authorized**  
> Curriculum source: `doc/CURRICULUM_FREEZE_2026_2027.md`  
> Coverage source: `doc/COVERAGE.md`  
> Activity strategy: `tracks/secondo/ACTIVITY_STRATEGY.md`

## Scopo

Trasformare il coverage editoriale in evidence didattica **senza** assumere che ogni outcome debba avere un grader automatico.

Principio:

```text
outcome
→ evidence migliore
→ profilo corretto
→ Activity soltanto quando il profilo è disponibile/certificato
```

Non:

```text
grader disponibile
→ deformo l'outcome per farlo entrare nel grader
```

---

# 1. Profili di evidence

## P0 — manual / trace / design

Adatto a:

- algoritmo/pseudocodice/flow chart;
- trace;
- spiegazione di scelte;
- data-model design;
- decomposizione;
- rubriche capstone;
- mutabilità/alias quando l'osservazione dello stato non è supportata dal grader disponibile.

P0 è evidence reale. Non è “assenza di valutazione”.

## P1 — stdin/stdout

Adatto quando il contratto naturale del problema è veramente:

```text
stdin → programma → stdout
```

Non usarlo per fingere test diretti di funzioni/oggetti/filesystem.

## P2 — function behavior

Target:

- argomenti → funzione → return/exception;
- funzioni pure/deterministiche;
- alcuni algoritmi su stringhe/collezioni.

Blocker/certification:

```text
2cornot2c#756
```

Non assumere supporto a side effect/mutazione dell'argomento finché il contratto P2 non lo certifica esplicitamente.

## P3 — object behavior

Target:

- costruzione oggetti;
- metodi;
- stato;
- invarianti;
- collaborazione/composizione quando il profilo supporta l'evidence necessaria.

Blocker:

```text
2cornot2c#758
```

## P4 — filesystem behavior

Target:

- fixture;
- workdir isolato;
- file prodotti/modificati;
- verifica host-side.

Blocker:

```text
2cornot2c#757
```

## Domain evidence — `romeo-sim`

È un profilo applicativo separato. Non sostituisce P1/P2/P3 e non è obbligatorio finché non certificato cross-profile.

---

# 2. Stato attuale — unica Activity Python materializzata

```text
py2-activity-b-input-somma-001
```

Modulo:

```text
M04
```

Profilo:

```text
P1
```

Ruolo:

- canarino tecnico/didattico;
- starter deve fallire;
- solution deve passare i casi deterministici;
- scaffold studente non deve esporre solution/teacher/expected answers.

Gate:

```text
python-docente#7
```

Fino alla certificazione del canarino **non materializzare una famiglia P1 in massa**.

---

# 3. Piano per UDA

## PY2-01 — Problem solving / flow chart

### Outcome

- problema/input/output/vincoli;
- algoritmo;
- pseudocodice/flow chart;
- trace;
- casi di test.

### Evidence corretta

```text
P0 manual/design/trace
```

### Candidate surfaces

- A — ordina i passi / individua input-output-vincoli;
- B — completa un flow chart controllato;
- C — progetta flow chart da specifica breve;
- D — debug di un diagramma;
- E — algoritmo + trace + casi.

### Stato

```text
PEDAGOGIA READY / DIGITAL DELIVERY BLOCKED
```

Il fallback manuale è valido; la versione digitale definitiva aspetta `2cornot2c#753/#754`.

Non creare una Activity che finga validazione strutturale digitale prima del Flowchart Lab.

---

## PY2-02 — M04–M05 primi programmi

### M04

Existing:

```text
py2-activity-b-input-somma-001 — P1 canary
```

Nessuna seconda Activity P1 prima della certificazione del canarino.

### M05 candidate evidence

- A/P0 — trace di espressioni e precedenza;
- B/P0 — confronta due espressioni e spiega equivalenza/differenza;
- C/P1 future — piccolo calcolo deterministico solo se il contratto naturale è stdin/stdout;
- D/P0 — debug di `/ // %` / precedenza / print-vs-return preview.

### Priorità

```text
P0 designable now
P1 materialization waits for #7
```

---

## PY2-03 — M06–M08 selezione/logica

### Evidence mix

```text
P0 trace/boundary reasoning
+
P1 deterministic behavior after P1 certification
```

### Candidate set

- A/P0 — branch trace + casi di confine;
- B/P0 — independent `if` vs mutually exclusive branches;
- C/P1 future — classificazione deterministica con confini espliciti;
- D/P0/P1 — debug di condizione/annidamento;
- E/P0 — confronto/refactor con comportamento preservato.

### Regola

Non usare short-circuit/De Morgan come criterio discriminante se sono rimasti guided/enrichment nella classe reale.

---

## PY2-04 — M09–M12 iterazione

### Evidence mix

```text
P0 trace/termination/invariant
+
P1 deterministic loops after P1 certification
```

### Candidate set

- A/P0 — trace `while` zero/una/più iterazioni;
- B/P0 — scegli `for`/`while` e motiva;
- C/P1 future — elaborazione ripetuta deterministica;
- D/P0/P1 — debug off-by-one/terminazione/reset;
- E/P1 future — contatore/accumulatore/min-max/ricerca in programma deterministico;
- F/P0 — nested loop `R×C` + quantità di lavoro intuitiva.

### Finding

M11 deve valutare il significato dello **stato progressivo**, non il riconoscimento del nome della ricetta.

---

## PY2-05 — M13–M16 funzioni/testing

### Evidence mix

```text
P0 design/trace
+
P2 function behavior
```

### Candidate set

- M13 A/P0 — call trace parametro/argomento/return;
- M13 C/P2 future — implement function from contract;
- M14 B/P0 — remove hidden global / explain data flow;
- M14 C/P2 future — compose pure functions;
- M15 C/P0 — top-down design + signatures + call graph;
- M16 B/P0/P2 — add a boundary test;
- M16 D/P0/P2 — regression: reproduce → test → fix.

### Gate

```text
no P2 materialization until 2cornot2c#756 is certified
```

Non trasformare funzioni in CLI stdin/stdout soltanto per usare P1.

---

## Checkpoint A

### Python evidence

Può usare P0/P1/P2 **in funzione del problema reale**, non un profilo prefissato.

### Git evidence

Riusa il consumer G1 embedded:

```text
status → diff → test → add → diff --staged → commit → status → log/show
```

Canonical Git Activity:

```text
g1-stage-selettivo-001
```

### Regola

Nessuna seconda prova Git high-stakes. Il checkpoint resta prima di tutto Python/recupero.

---

## PY2-06 — M17–M19 stringhe

### Evidence mix

```text
P0 choice/trace
+
P2 pure text functions after certification
```

### Candidate set

- A/P0 — index/slice prediction;
- B/P0 — choose `in` vs `find` / method vs loop;
- C/P2 future — pure text transformation/validator;
- D/P0/P2 — debug index/immutability/find;
- E/P2 future — parser/testuale semplice con contract + edge cases.

### Regola

Non far diventare `count/replace/startswith/endswith/join` una checklist obbligatoria se non sono mastery.

---

## PY2-07 — M20–M22 liste/tuple/dati tabellari

### Evidence mix

```text
P0 mutation/alias/model reasoning
+
P2 only for behaviors P2 can represent faithfully
```

### Candidate set

- M20 A/P0 — predict list mutation;
- M20 B/P0 — debug `lista = lista.append(...)`;
- M20 C/P2 future — pure list-processing function when contract does not depend on hidden side effects;
- M21 A/P0 — alias microscope;
- M21 B/P0 — mutation/non-mutation contract;
- M21 C/P2 future — pure filter returning new list;
- M22 A/P0 — tuple/list model choice;
- M22 C/P0 — matrix trace/reset/row alias bug.

### Important boundary

Non usare P2 per affermare mutation/alias coverage se il profilo certificato osserva soltanto return/exception e non lo stato mutato degli argomenti.

---

## Checkpoint B

### Evidence

```text
P0 project/rubric
+ eventuali P2 componenti pure certificate
```

### Regola

Il progetto dimostra **scelta del modello**, non numero di strutture usate.

Git riusa G1; nessun G2 nuovo.

---

## PY2-08 — M23–M25 set/dict/model choice

### Evidence mix

```text
P0 model-choice/rubric
+
P2 pure functions if profile supports values involved
```

### Candidate set

- M23 A/P0 — list vs set choice;
- M23 C/P2 future — pure set operation if serialization/argument contract is certified;
- M24 B/P0 — required vs optional key;
- M24 C/P2 future — frequency function;
- M25 A/P0 — data-model choice cards;
- M25 C/P0 — refactor parallel lists;
- M25 E/P0 — mini data-model project.

### Regola

Outcome #18 “scegli la struttura” resta principalmente rubric/manual evidence: un grader di output non può sostituire la spiegazione della scelta.

---

## PY2-09 — M26 file/error boundary

### Evidence mix

```text
P0/manual
+
P4 filesystem behavior after certification
```

### Candidate set

- A/P0 — memory vs persistence / path vs content;
- B/P0 — separate file I/O from pure logic;
- C/P4 future — read fixture + produce expected UTF-8 artifact;
- D/P4 future — missing-file behavior;
- E/P0 — classify bug vs external error.

### Gate

```text
no P4 autograding claim before 2cornot2c#757
```

Non espandere la UDA a JSON/CSV/binario per giustificare un grader.

---

## PY2-10 — M27–M30 OOP

### Evidence mix

```text
P0/manual/assert
+
P3 object behavior after certification
```

### Candidate set

- M27 A/P0 — class/instance/self trace;
- M27 C/P3 future — independent instances + method behavior;
- M28 B/P0/P3 — valid/rejected transition + state invariant;
- M29 B/P0 — responsibilities/composition map;
- M29 C/P3 future — collaboration behavior if P3 supports graph/state evidence;
- M30 E/P0 — capstone rubric/manual evidence;
- selected deterministic sub-behaviors may use P3 later.

### Gate

```text
no P3 generic object autograding claim before 2cornot2c#758
```

### Composition

Composizione è frozen core. Se P3 non sa osservarla in modo affidabile, raccogliere evidence manuale/diagramma/test spiegato: **non cancellare l'outcome**.

---

## Checkpoint C

### Evidence

```text
P0 capstone/recovery/evidence
+ optional certified P3 sub-checks
```

### Regola

- nessun nuovo prerequisito;
- composizione deve essere dimostrata;
- recovery riduce il dominio, non gli outcome;
- Git riusa G1;
- Romeo/file solo se utili/certificati.

---

# 4. Roadmap di materializzazione

## Wave 0 — adesso

```text
NO mass Activity materialization
```

Consentito:

- rifinire candidate specs;
- rubriche/manual evidence;
- preparare fixture/contract senza dichiarare autograding;
- mantenere M04 come unico canarino Python materializzato.

## Wave 1 — dopo P1 canary certification

Priorità:

```text
PY2-03 selezione
PY2-04 iterazione
```

Materializzare poche Activity P1 che abbiano un contratto naturalmente stdin/stdout.

Non produrre una Activity per ogni lesson solo per aumentare il conteggio.

## Wave 2 — dopo P2 certification

Priorità:

```text
M13/M16 funzioni
PY2-06 stringhe
pure list/dict functions selezionate
```

Prima verificare esattamente che evidence P2 osserva su argomenti/return/exceptions/mutation.

## Wave 3 — dopo P4 certification

```text
M26 filesystem
```

Una piccola Activity rappresentativa può bastare a certificare il profilo prima di espandere.

## Wave 4 — dopo P3 certification

```text
M27–M29 object behavior
```

Capstone resta prevalentemente rubric/manual anche quando alcuni sub-behavior sono autogradabili.

---

# 5. Priorità didattica > quantità

Una UDA può essere didatticamente completa con:

```text
lesson/deck/runbook
+ micro-evidence formative
+ una Activity ben scelta
+ assessment/checkpoint
```

Non serve:

```text
A+B+C+D+E+F autogradate per ogni modulo
```

La tassonomia A–F descrive **tipi/livelli di attività**, non una quota da riempire meccanicamente.

---

# 6. Dashboard futura

Mostrare separatamente:

```text
editorial coverage
manual evidence coverage
materialized Activity coverage
P1/P2/P3/P4 automated coverage
platform certification
teacher sign-off
```

Una UDA con rubric/manual evidence valida non è “0%” soltanto perché non ha un grader automatico.

---

# 7. Gate per iniziare una Wave

Prima di materializzare una nuova Activity automatica:

- outcome preciso identificato;
- profilo evidence appropriato;
- profilo certificato;
- starter/solution boundary definito;
- casi deterministici quando applicabile;
- no teacher/solution leakage;
- source/provenance refs;
- semantic review rispettata;
- non richiede enrichment come falso prerequisito;
- consumer smoke possibile.

Se uno di questi punti manca, restare su candidate/manual evidence invece di fingere readiness.
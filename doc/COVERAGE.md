# Python secondo — Coverage & Provenance Map

> Stato: **curriculum coverage audit / editorial draft**  
> Track: `python-secondo-2026-2027`  
> Curriculum canonico: `doc/CURRICULUM_FREEZE_2026_2027.md`

Questo documento risponde a tre domande diverse, che **non devono essere confuse**:

```text
1. l'outcome è coperto dal curriculum/materiale?
2. esiste una Activity/evidence eseguibile adatta?
3. il relativo delivery è stato realmente certificato?
```

Perciò:

```text
coverage editoriale ≠ autograding coverage ≠ classroom readiness
```

---

# 1. Legenda degli stati

## Coverage editoriale

- **SPEC** — outcome progettato e congelato, ma lesson finale non ancora materializzata;
- **DRAFT** — lesson/deck/runbook materializzati e semanticamente revisionati, non ancora `approved`;
- **APPROVED** — riservato a una futura promotion editoriale esplicita.

## Activity / evidence

- **P0/manual** — trace, design, rubric o evidence docente;
- **P1** — programma stdin/stdout;
- **P2** — comportamento diretto di funzioni;
- **P3** — comportamento di oggetti;
- **P4** — filesystem;
- **candidate** — esercizi/Activity candidate presenti nel materiale, ma non materializzati come Activity certificata;
- **none** — nessuna Activity canonica ancora materializzata.

## Delivery

- **not certified** — nessuna prova end-to-end sufficiente;
- **blocked** — esiste un blocker noto di piattaforma/runner/runtime;
- **certified** — da usare soltanto con evidence reale.

---

# 2. Coverage dei 25 outcome frozen

| # | Outcome frozen | Coverage canonica | Editoriale | Activity / evidence attuale | Delivery |
|---:|---|---|---|---|---|
| 1 | leggere un problema e individuare input/output/vincoli | PY2-01 M01–M03 SPEC; riusato in tutto il track | **SPEC** | P0/manual candidate | **blocked** Flowchart Lab per delivery digitale finale |
| 2 | progettare algoritmo/pseudocodice/flow chart quando appropriato | PY2-01 M01–M03 SPEC | **SPEC** | P0/manual fallback carta/lavagna | **blocked** `2cornot2c#753/#754` |
| 3 | eseguire trace e progettare casi normali/limite | PY2-01 SPEC + spirale M04–M30 | **SPEC + DRAFT reinforcement** | P0/manual; casi/assert nei moduli successivi | not certified |
| 4 | tradurre l'algoritmo in Python 3.12-compatible | M04–M05, poi rinforzo annuale | **DRAFT** | M04 P1 canary = evidence parziale, non certificazione dell'outcome annuale | **blocked** `python-docente#7/#8` |
| 5 | leggere input, convertire tipi, produrre output | M04–M05 | **DRAFT** | `py2-activity-b-input-somma-001` — P1 canary | **blocked** `python-docente#7/#8` |
| 6 | selezioni semplici, multiple, composte e annidate | M06–M08 | **DRAFT** | candidate/P0; nessuna Activity autogradata canonica materializzata | not certified |
| 7 | distinguere condizioni indipendenti e casi mutuamente esclusivi | M07–M08 | **DRAFT** | candidate/P0 | not certified |
| 8 | scegliere `for` o `while` e motivarlo | M09–M10 | **DRAFT** | candidate/P0 | not certified |
| 9 | comporre selezioni/cicli, inclusi semplici cicli annidati | M09–M12 | **DRAFT** | candidate/P0/P1 secondo consegna futura | not certified |
| 10 | contatori, accumulatori, sentinelle, min/max progressivo e ricerca | M09 + M11 | **DRAFT** | candidate; M11 review protegge stato progressivo/invariante | not certified |
| 11 | decomporre un problema in funzioni | M13–M15 | **DRAFT** | P0/manual; future P2 dove l'outcome è comportamento funzione | **blocked** P2 `2cornot2c#756` per autograding diretto |
| 12 | distinguere parametro/argomento e `return`/`print` | M13 | **DRAFT** | candidate/P0; future P2 | **blocked** P2 per autograding diretto |
| 13 | passare dati esplicitamente e comprendere scope locale essenziale | M14–M15 | **DRAFT** | candidate/P0; future P2 | **blocked** P2 per autograding diretto |
| 14 | scrivere `assert`, diagnosticare bug e aggiungere regression test | M16 + Checkpoint A | **DRAFT** | workspace `assert` / P0; future P2 dove appropriato | not certified |
| 15 | usare stringhe come sequenze immutabili | M17–M19 | **DRAFT** | candidate; future P2 per funzioni testuali | **blocked** P2 solo per autograding diretto |
| 16 | usare liste/tuple comprendendo mutabilità, alias e copia | M20–M22 + Checkpoint B | **DRAFT** | P0/manual + candidate; future P2 per funzioni pure | not certified |
| 17 | usare set/dizionari e strutture annidate | M23–M25 | **DRAFT** | candidate/P0/P2 secondo outcome futuro | not certified |
| 18 | scegliere `str/list/tuple/set/dict` dalle operazioni dominanti | M17–M25, sintesi M25 | **DRAFT** | P0/manual rubric; non riducibile correttamente a un semplice grader stdout | not certified |
| 19 | intuizioni elementari sul costo del lavoro senza Big-O formale | M12 + M25 | **DRAFT** | P0/manual explanation/trace | not certified |
| 20 | leggere/scrivere file testo con `pathlib`, UTF-8 e context manager | M26 | **DRAFT** | candidate/P0; future P4 per filesystem behavior | **blocked** P4 `2cornot2c#757` per autograding filesystem |
| 21 | distinguere errori esterni prevedibili da bug | M26 | **DRAFT** | P0/manual; eventuale P4 | not certified |
| 22 | classi/istanze, attributi, `self`, `__init__`, metodi e stato | M27–M28 | **DRAFT** | P0/manual/assert; future P3 | **blocked** P3 `2cornot2c#758` per object autograding |
| 23 | mantenere invarianti semplici | M28 + M30 | **DRAFT** | P0/manual/assert; future P3 | **blocked** P3 per autograding diretto |
| 24 | usare composizione tra oggetti | M29–M30 + Checkpoint C | **DRAFT** | P0/manual/assert; future P3 | **blocked** P3 per autograding diretto |
| 25 | realizzare un piccolo capstone OOP testabile e spiegabile | M30 + Checkpoint C | **DRAFT** | rubric/manual evidence; future P3 solo per parti deterministiche | not certified / rehearsal pending |

## Lettura corretta della tabella

Il fatto che gli outcome **4–25** abbiano materiale `DRAFT` significa che il percorso editoriale canonico esiste ed è stato sottoposto alla review semantica del 2026-08-25.

Non significa che:

- ogni outcome abbia una Activity;
- ogni Activity sia autogradata;
- P1/P2/P3/P4 siano tutti certificati;
- la CI privata abbia eseguito i gate;
- il corso sia pronto per una classe reale.

PY2-01 è diverso: gli outcome 1–3 sono già congelati e specificati, ma la lesson/delivery digitale finale resta volutamente sospesa finché il Flowchart Lab non ha un boundary veritiero. Il fallback manuale conserva gli outcome.

---

# 3. Coverage Activity attuale

## Materializzato

Attualmente il corso Python materializza una sola nuova Activity canonica autogradabile:

```text
py2-activity-b-input-somma-001
```

Profilo target:

```text
P1 — stdin/stdout
```

Ruolo:

- canarino tecnico/didattico M04;
- starter discriminante;
- solution con casi deterministici;
- student/teacher asset separation;
- **non** autorizza produzione massiva delle Activity successive.

Certification gate:

```text
python-docente#7
```

## Non materializzato in massa

M05–M30 contengono esercizi e Activity candidate, ma la policy corrente è intenzionale:

```text
outcome didattico
→ profilo di evidence corretto
→ profilo certificato
→ Activity materializzata
```

Non:

```text
grader disponibile
→ deformo l'outcome per farlo entrare nel grader
```

Esempi:

- decomposizione/design → P0/manual;
- funzione pura → P2;
- filesystem → P4;
- comportamento oggetto → P3;
- scelta struttura dati → spesso rubric/manual evidence anche quando il codice è testabile.

---

# 4. Cross-course coverage — Git G1

Git non è uno dei 25 outcome Python numerati, ma è una decisione curricolare frozen (`C8`) e un workflow trasversale.

Source of truth:

```text
TheBitPoets/git
G1 candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
```

Consumer Python:

```text
config/git-g1-consumer.json
mode = embedded-outcome-subset
```

Progressione:

```text
M14–M16
  status / diff — guided

Checkpoint A
  status → diff → test → add → diff --staged → commit → status → log/show

secondo semestre / Checkpoint B/C / capstone
  riuso del workflow + recovery G1 progressivo
```

Coverage Git nel corso Python significa **evidence di processo**, non completamento del track standalone G1 e non una seconda prova high-stakes.

---

# 5. Applied coverage — Romeo

Romeo è una spine applicativa selettiva, non un requisito del syllabus.

Regole:

- ogni outcome Python deve restare dimostrabile anche senza hardware fisico;
- le missioni Romeo possono rinforzare soprattutto condizioni, cicli, funzioni/debug e OOP;
- `romeo-sim` deve essere certificato prima di diventare delivery obbligatoria;
- deve esistere sempre un fallback generale equivalente.

Quindi una missione Romeo **non aumenta artificialmente la percentuale di coverage** di un outcome già coperto: è un dominio applicativo/evidence alternativa.

---

# 6. Provenance model

## Materiale canonico

Le lesson, deck, runbook, Activity e review del corso sono materiale originale TheBitPoets, con provenance dichiarata nel Content Pack e nei source mapping.

## Gerarchia delle fonti

### A — autorità tecnica

```text
Python 3 documentation
```

Ruolo:

- sintassi/semantica corrente;
- built-in e standard library;
- correzione di affermazioni tecniche.

Non è una progressione pedagogica da copiare integralmente.

### B — riferimenti pedagogici/docente

```text
Think Python / Pensare in Python
Learning Python / Imparare Python
Fluent Python
Python in a Nutshell
Pluralsight catalog
```

Ruolo:

- coverage/gap-check;
- esempi di progressione e chiarimento per il docente;
- confronto con il curriculum.

Le fonti licensed restano **teacher-reference only**: nessuna riproduzione wholesale nel materiale studente.

### C — legacy source pack

```text
TheBitPoets/friedpython
```

Ruolo:

- inventario di esercizi/esempi legacy;
- fonte di candidati dopo audit.

Regola:

```text
audit individuale
→ outcome preciso
→ riscrittura/modernizzazione Python 3.12
→ casi limite
→ starter/solution
→ provenance
```

Nessun import wholesale.

### D — cross-course / applied sources

```text
TheBitPoets/git
TheBitPoets/romeo / romeo-sim
TheBitLab / 2cornot2c contracts
```

Ruolo:

- Git G1: curriculum trasversale consumato;
- Romeo: dominio applicativo selettivo;
- TheBitLab: delivery/runtime/grading contract.

Nessuno di questi sostituisce gli outcome Python congelati.

---

# 7. Provenance audit dei moduli materializzati

Il gate `tests/course_authoring_catalog.py` richiede che ogni content item materializzato:

- punti alla lesson canonica;
- sia presente nella source `python-course-content`;
- sia esposto al Course Design/Course Board;
- abbia `source_refs` con `content-origin` alla lesson;
- mantenga gli eventuali `activity_ids` coerenti;
- non esponga asset teacher/solution agli indici studente.

La semantic review aggiunge un secondo livello:

```text
presenza/provenance strutturale
+
confine didattico MUST/GUIDED/ENRICHMENT
```

Entrambi restano da **eseguire realmente** in CI appena il blocker `python-docente#8` viene risolto.

---

# 8. Gap reali dopo il coverage audit

## Gap editoriale

```text
PY2-01 final lesson/deck/runbook delivery
```

Motivo: Flowchart Lab/Classroom Environment boundary non ancora certificato.

## Gap Activity/evidence

```text
M05–M30 Activity materialization
```

Non è un difetto di coverage editoriale: è il prossimo layer, da pianificare per profilo di evidence.

## Gap grading/delivery

- P1 canary non certificato;
- P2/P3/P4 non disponibili come promessa generale del corso;
- private Actions non parte;
- `romeo-sim` non ancora certificato cross-profile;
- slide artifact build/quality non ancora completata;
- teacher sign-off finale mancante;
- rehearsal reale TheBitLab mancante.

---

# 9. Criterio per future percentuali/dashboard

Una dashboard futura deve mostrare **assi separati**, per esempio:

```text
Curriculum coverage
Editorial materialization
Semantic review
Activity coverage
Automated grading coverage
Platform certification
Teacher sign-off
Classroom rehearsal
```

È vietato condensare questi assi in un unico numero “corso 95% completo” senza dichiarare esattamente che cosa misura.

---

# 10. Stato audit

```text
Frozen outcomes mapped          25/25
M04–M30 editorial coverage      complete / draft
M04–M30 semantic review         complete / draft
PY2-01 design coverage          complete / final delivery pending
Python Activities materialized  1 canary
P1 certification                pending
P2/P3/P4 certification          pending/open
Git G1 structural consumer      complete / delivery evidence pending
Romeo applied mapping           present / runtime certification pending
Teacher sign-off                pending
Classroom rehearsal             pending
```

Questo è il baseline corretto per il prossimo lavoro su Activity planning, artifact quality e approval.
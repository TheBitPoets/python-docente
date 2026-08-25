# python-docente — project status

## Current phase

**Curriculum FROZEN + core editorial authoring M04–M30 complete; semantic review / delivery QA phase.**

Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`  
Decision-owner approval: **2026-08-24**.  
Branch: `agent/course-architecture`  
Draft PR: `#1`.

`Content Pack 1.0 / approved` and `ready for classroom` remain separate future gates.

---

# 1. Curriculum — DONE / FROZEN

- 33 weeks × 3h = 99 nominal hours;
- 90h core + 9h checkpoint/buffer;
- 2 active-theory + 1 lab hour weekly;
- M00–M30 and PY2-01…PY2-10 specified;
- OOP mandatory weeks 29–32;
- testing/trace/debug/refactor spiral;
- Git G1 progressive, standalone Git curriculum separate;
- Container curriculum separate;
- Romeo selective, never hardware-dependent core.

---

# 2. Editorial authoring — M04…M30 COMPLETE

Audit del repository conferma lesson canoniche, Marp deck e teacher runbook per tutti i moduli **M04–M30**.

```text
PY2-01  problem solving / flow chart        SPEC-only (Flowchart Lab pending)
PY2-02  M04–M05                             COMPLETE editorial
PY2-03  M06–M08                             COMPLETE editorial
PY2-04  M09–M12                             COMPLETE editorial
PY2-05  M13–M16                             COMPLETE editorial
Checkpoint A                               materializzato
PY2-06  M17–M19                             COMPLETE editorial
PY2-07  M20–M22                             COMPLETE editorial
Checkpoint B                               materializzato
PY2-08  M23–M25                             COMPLETE editorial
PY2-09  M26                                 COMPLETE editorial
PY2-10  M27–M30                             COMPLETE editorial
Checkpoint C                               materializzato
```

Student/teacher navigation arriva fino al capstone. La settimana 33 non introduce nuovi prerequisiti.

---

# 3. Semantic review — PY2-02 + PY2-03 COMPLETE

Documento:

```text
doc/SEMANTIC_REVIEW_PY2_02_PY2_03_2026-08-25.md
```

Esito:

```text
PY2-02 architecture/order     PASS
M04 pacing                    PASS with mastery gate
M05 pacing                    PASS after priority tiering
PY2-03 architecture/order     PASS
M06 pacing                    PASS with mastery gate
M07 pacing                    PASS after short-circuit demotion
M08 pacing                    PASS with De Morgan/mini-project optional
```

Regola introdotta stabilmente:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

Correzioni principali:

- M04: `bool` preview; niente tassonomia errori da memorizzare;
- M05: built-in secondarie fuori dal core temporizzato; `min/max` non sostituiscono M11;
- M06: gate su confronti/confini/if/trace;
- M07: short-circuit enrichment;
- M08: De Morgan enrichment; mini-project estendibile.

---

# 4. Semantic review — PY2-04 COMPLETE

Documento:

```text
doc/SEMANTIC_REVIEW_PY2_04_2026-08-25.md
```

Esito:

```text
PY2-04 architecture/order     PASS
M09 pacing                    PASS with while-True demotion
M10 pacing                    PASS with break/continue guided-only
M11 pacing                    PASS as one state/invariant family
M12 pacing                    PASS; complexity intuitive only
```

Progressione resa esplicita:

```text
M09  perché continuo / termino?
M10  percorso noto o durata dinamica?
M11  che cosa deve ricordare il ciclo?
M12  che cosa accade con due dimensioni?
```

Correzioni principali:

- M09: `while True`/`break` enrichment, non mastery;
- M10: `break/continue` guided exposure, non gate;
- M11: contatore/accumulatore/min-max/flag/ricerca insegnati come famiglia di **stato progressivo + invariante**, non ricette;
- M12: `R×C`, reset al livello giusto e lavoro inutile core; niente Big-O formale.

---

# 5. Semantic review — PY2-05 + Checkpoint A COMPLETE

Documento:

```text
doc/SEMANTIC_REVIEW_PY2_05_CHECKPOINT_A_2026-08-25.md
```

Esito:

```text
PY2-05 architecture/order       PASS
M13 pacing                      PASS after retrieval + Git boundary fix
M14 pacing                      PASS
M15 pacing                      PASS with anti-bureaucracy rule
M16 pacing                      PASS; P2 teacher/delivery-side
Checkpoint A                    PASS after embedded-G1 clarification
```

Correzioni principali:

- M13: formalizza la preview M05; `None`/predicate guided; nessun Git prima di M14;
- M14: scope beginner, passaggio esplicito e composizione; Git status/diff guided;
- M15: top-down proporzionato, niente documentazione fine a sé stessa;
- M16: `assert`/regression/refactor core; P2 rimosso dal deck studente e confinato al delivery docente;
- Checkpoint A: Git G1 dichiarato **embedded outcome subset**, non completamento del track standalone.

Consumer Git machine-readable:

```text
config/git-g1-consumer.json
mode = embedded-outcome-subset
full_g1_track_completion_required = false
full_canonical_lesson_completion_required = false
```

`tests/git_g1_consumer_contract.py` protegge anche questo boundary.

Next semantic review:

```text
PY2-06 — M17–M19
PY2-07 — M20–M22 + Checkpoint B
```

---

# 6. Unico buco editoriale core — PY2-01

PY2-01 resta volutamente **SPEC-only** perché il workflow digitale flow chart dipende dal Flowchart Lab TheBitLab.

Fallback didattico valido:

```text
carta/lavagna
→ pseudocodice
→ flow chart manuale
→ trace
→ casi di test
```

Non produrre una lesson finale che promette capability inesistenti/non certificate.

Blocker: `2cornot2c#753/#754`.

---

# 7. Git G1 consumer — STRUCTURAL INTEGRATION COMPLETE

Source of truth:

```text
TheBitPoets/git
G1 candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
contract: doc/G1_CONSUMER_CONTRACT.md
```

Progressione:

```text
M14–M16
  G1.OBSERVE.STATUS / G1.OBSERVE.DIFF — guided

Checkpoint A
  status → diff → test → add → diff --staged → commit → status → log/show

secondo semestre
  G1.WORKFLOW.CHECKPOINT + G1.RECOVERY.BASIC — independent progressivo
```

Canary Git Lab:

```text
g1-stage-selettivo-001
```

Platform candidate verde:

```text
TheBitPoets/2cornot2c#761/#762
24570f7a3af67634ec0cfbf54f486660359baaf2
```

Restano delivery gates:

- esecuzione reale del consumer test appena i runner privati tornano disponibili;
- freeze/decision-owner finale G1 o accettazione esplicita del candidate ref per pilot;
- rehearsal Classroom Environment/TheBitLab.

---

# 8. Golden technical vertical slice — M04 / P1

Activity:

```text
py2-activity-b-input-somma-001
```

Canary contract:

```text
starter must fail
solution must pass 3 deterministic cases
student scaffold must not leak teacher/solution/expected answers
```

Certification: `python-docente#7`.

Solo M04 materializza per ora una nuova Activity P1. Gli altri moduli mantengono esercizi/Activity candidate fino alla certificazione del profilo richiesto.

---

# 9. Authoring automation / QA

- `tests/course_authoring_catalog.py` — catalogo scalabile dei moduli materializzati;
- `scripts/sync_authoring_catalog.py` — parità Content Pack ↔ Course Board source list;
- `tests/git_g1_consumer_contract.py` — contratto Python→Git G1;
- `tests/m04_vertical_slice_static.py` — golden M04;
- `tests/m05_authoring_static.py` — QA pedagogica M05;
- `tests/course_board_workspace_roundtrip.py` — external workspace save/reopen;
- `tests/thebitlab_python_smoke.py` — Activity/Content Pack/scaffold/grading P1.

Il Content Pack resta il catalogo autorevole dei moduli materializzati.

---

# 10. GitHub Actions blocker #8

Root cause ristretto al layer pre-runner dei repository privati.

Evidence:

- job diagnostico con solo `runs-on + echo`, senza action esterne, fallisce con `steps = null` su Ubuntu/Windows;
- private `tpsi-quarto-docente` aveva CI verde il 2026-08-19 e failure pre-step dal 2026-08-21.

Leading hypothesis: quota/budget/spending Actions privati; alternativa: policy hosted-runner dell'organizzazione modificata. Billing state non è esposto dal connector e non viene inventato.

Issue: `python-docente#8`.

Un run che termina prima del runner non è evidence che i test abbiano passato o fallito.

---

# 11. Grading profiles TheBitLab

- P0 — manual/trace/design;
- P1 — stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — `romeo-sim` external runtime.

Non adattare artificialmente un outcome P2/P3/P4 a P1 solo per ottenere un voto automatico.

---

# 12. Platform gates

- `python-docente#2` — managed Classroom Environment;
- `python-docente#6` — beginner REPL/editor workflow;
- `python-docente#7` — P1 canary;
- `python-docente#8` — private Actions runners;
- `2cornot2c#753/#754` — Course Environment + Flowchart Lab;
- `2cornot2c#755` — Course Workspace/Open Course UX;
- `2cornot2c#756` — P2;
- `2cornot2c#757` — P4;
- `2cornot2c#758` — P3;
- `romeo-sim` cross-profile certification.

---

# 13. Source audit / friedpython

Thematic inventory e snapshot sono pronti. Prima del riuso ogni esercizio/example deve essere auditato singolarmente, modernizzato e ricostruito con provenance. Nessun wholesale import.

Audit presenti includono liste/tuple, dict e file.

---

# 14. Next work — priorità corrente

Non generare altre lesson core M04–M30: esistono già.

Ordine corrente:

1. semantic review PY2-06 + PY2-07/Checkpoint B;
2. poi PY2-08 + PY2-09;
3. poi PY2-10 OOP/capstone + Checkpoint C;
4. continuare stale-document cleanup quando emerge;
5. chiudere il boundary PY2-01 prima della materializzazione finale;
6. risolvere #8 e far eseguire i gate già scritti;
7. certificare M04/P1;
8. materializzare Activity per profilo, UDA per UDA;
9. P2 prima delle Activity function behavior;
10. P4 prima delle Activity filesystem;
11. P3 prima delle Activity OOP generiche;
12. certificare `romeo-sim` prima delle missioni obbligatorie;
13. slide build/artifact pipeline + teacher review;
14. provenance/coverage finale;
15. promozione Content Pack `1.0.0 / approved`;
16. rehearsal reale TheBitLab e GO classroom.

---

# Gate status

```text
Curriculum architecture        FROZEN ✅
Editorial lessons M04-M30      COMPLETE 🟡 draft
Semantic review PY2-02/03      COMPLETE 🟡
Semantic review PY2-04         COMPLETE 🟡
Semantic review PY2-05 + A     COMPLETE 🟡
Checkpoint A/B/C               COMPLETE 🟡 draft
Git G1 structural consumer     COMPLETE 🟡 delivery evidence pending
PY2-01 final editorial         BLOCKED/WAITING Flowchart Lab 🟡
P1 golden vertical slice       CREATED / NOT CERTIFIED 🟡
Private Actions runners        BLOCKED 🔴 #8
P2/P3/P4 grading               OPEN ⏳
romeo-sim certification        OPEN ⏳
Content Pack 1.0 approved      NOT YET ⏳
Ready for classroom / GO       NOT YET ⏳
```

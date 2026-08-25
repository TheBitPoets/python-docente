# python-docente — project status

## Current phase

**Curriculum FROZEN + core editorial authoring M04–M30 complete; delivery/QA phase.**

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

# 3. Unico buco editoriale core — PY2-01

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

# 4. Git G1 consumer — STRUCTURAL INTEGRATION COMPLETE

Python seconda consuma il curriculum Git separato senza duplicarlo.

Source of truth corrente:

```text
TheBitPoets/git
G1 candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
contract: doc/G1_CONSUMER_CONTRACT.md
```

Dipendenza locale machine-readable:

```text
config/git-g1-consumer.json
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

Canary Git Lab del corso Git:

```text
g1-stage-selettivo-001
```

Platform Git Lab candidate verde:

```text
TheBitPoets/2cornot2c#761/#762
24570f7a3af67634ec0cfbf54f486660359baaf2
```

Aggiunto `tests/git_g1_consumer_contract.py` e relativo gate nella workflow privata per impedire divergenze future.

Restano **delivery gates**, non design gaps:

- esecuzione reale del consumer test appena i runner privati tornano disponibili;
- freeze/decision-owner finale G1 o accettazione esplicita del candidate ref per pilot;
- rehearsal nel Classroom Environment/TheBitLab.

---

# 5. Golden technical vertical slice — M04 / P1

Activity: `py2-activity-b-input-somma-001`.

Canary contract:

```text
starter must fail
solution must pass 3 deterministic cases
student scaffold must not leak teacher/solution/expected answers
```

Certification: `python-docente#7`.

Solo M04 materializza per ora una nuova Activity P1. Gli altri moduli mantengono esercizi/Activity candidate fino alla certificazione del profilo richiesto.

---

# 6. Authoring automation / QA

- `tests/course_authoring_catalog.py` — catalogo scalabile dei moduli materializzati;
- `scripts/sync_authoring_catalog.py` — parità Content Pack ↔ Course Board source list;
- `tests/git_g1_consumer_contract.py` — contratto cross-course Python→Git G1;
- `tests/m04_vertical_slice_static.py` — golden M04;
- `tests/m05_authoring_static.py` — QA pedagogica M05;
- `tests/course_board_workspace_roundtrip.py` — external workspace save/reopen;
- `tests/thebitlab_python_smoke.py` — Activity/Content Pack/scaffold/grading P1.

Il Content Pack resta il catalogo autorevole dei moduli materializzati.

---

# 7. GitHub Actions blocker #8

Root cause ristretto al layer pre-runner dei repository privati.

Evidence:

- job diagnostico con solo `runs-on + echo`, senza action esterne, fallisce con `steps = null` su Ubuntu/Windows;
- private `tpsi-quarto-docente` aveva CI verde il 2026-08-19 e failure pre-step dal 2026-08-21.

Leading hypothesis: quota/budget/spending Actions privati; alternativa: policy hosted-runner dell'organizzazione modificata. Billing state non è esposto dal connector e non viene inventato.

Issue: `python-docente#8`.

Un run che termina prima del runner non è evidence che i test abbiano passato o fallito.

---

# 8. Grading profiles TheBitLab

- P0 — manual/trace/design;
- P1 — stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — `romeo-sim` external runtime.

Non adattare artificialmente un outcome P2/P3/P4 a P1 solo per ottenere un voto automatico.

---

# 9. Platform gates

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

# 10. Source audit / friedpython

Thematic inventory e snapshot sono pronti. Prima del riuso ogni esercizio/example deve essere auditato singolarmente, modernizzato e ricostruito con provenance. Nessun wholesale import.

Audit già presente per liste/tuple: `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.

---

# 11. Next work — priorità corrente

Non generare altre lesson core M04–M30: esistono già.

Ordine consigliato:

1. completare audit/QA strutturale M04–M30 + checkpoint + navigazione;
2. ripulire riferimenti editoriali obsoleti dopo l'integrazione Git G1;
3. Flowchart Lab / Course Environment: chiudere il boundary PY2-01 (`2cornot2c#753/#754`);
4. materializzare PY2-01 senza promettere capability inesistenti;
5. risolvere #8 amministrativamente e far eseguire i gate già scritti;
6. certificare M04/P1;
7. pianificare/materializzare Activity per profilo, UDA per UDA;
8. P2 prima delle Activity di function behavior;
9. P4 prima delle Activity filesystem;
10. P3 prima delle Activity OOP generiche;
11. certificare `romeo-sim` prima delle missioni obbligatorie;
12. slide build/artifact pipeline + teacher review;
13. provenance/coverage finale;
14. promozione Content Pack `1.0.0 / approved`;
15. rehearsal reale TheBitLab e GO classroom.

---

# Gate status

```text
Curriculum architecture        FROZEN ✅
Editorial lessons M04-M30      COMPLETE 🟡 draft
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

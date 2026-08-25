# python-docente — project status

## Current phase

**Curriculum FROZEN + controlled module-by-module authoring.**

Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`  
Decision-owner approval: **2026-08-24**.

Branch: `agent/course-architecture`  
Draft PR: `#1`.

Content Pack approval and classroom readiness remain separate gates.

---

# 1. Curriculum — DONE / FROZEN

- 33 weeks × 3h = 99 nominal hours;
- 90h core + 9h explicit checkpoint/buffer;
- 2 active-theory + 1 lab hour weekly;
- M00–M30 and PY2-01…PY2-10 specified;
- OOP mandatory weeks 29–32;
- spiral problem→algorithm→cases→code→test→debug→refactor;
- Git G1 progressive; Git course separate;
- Container course separate;
- Romeo selective, never hardware-dependent core.

---

# 2. Materialized editorial content — M04…M10

The draft Content Pack now contains **7 consecutive materialized modules**:

```text
M04 interpreter / REPL / values / I-O
M05 expressions / operators / first function preview
M06 booleans / comparisons / if
M07 elif / exclusive vs independent branches / and-or-not
M08 nesting / validation / refactoring
M09 while / state / termination / sentinel / repeated validation
M10 for / range / for-vs-while / break-continue intro
```

Every materialized module has:

```text
canonical lesson
+ Marp slide source
+ teacher runbook
+ Content Pack item
+ Course Board source
+ student/teacher navigation
```

Only **M04** materializes a new P1 Activity. M05–M10 contain exercises and Activity candidates but deliberately add no new autograded Activity until the P1 canary is certified.

Status by UDA:

- PY2-01: specification only; final delivery waits on Flowchart Lab;
- PY2-02: editorially materialized (M04–M05);
- PY2-03: editorially materialized (M06–M08);
- PY2-04: partially materialized (M09–M10; M11–M12 remain).

Next module: **M11 — counters, accumulators, progressive min/max, search and flags**.

---

# 3. Golden technical vertical slice — M04

Activity: `py2-activity-b-input-somma-001`.

Canary contract:

```text
starter must fail
solution must pass 3 cases
student scaffold must not leak teacher/solution/expected answers
```

Cases:

```text
2 + 3   → 5
0 + 0   → 0
-4 + 10 → 6
```

Certification remains open: `python-docente#7`.

---

# 4. Course Workspace / dashboard model

- repo = mutable Course Workspace;
- Content Pack = module/file identity;
- Course Board = heading-tree editorial granularity;
- Git = history/review;
- Course Bundle = immutable publication release.

`2cornot2c#755` tracks Open Course UX and bulk “add whole module/file”.

---

# 5. Authoring automation / QA

## Scalable QA

`tests/course_authoring_catalog.py` checks every materialized module for:

- numbered lesson/order consistency;
- lesson + Marp deck + runbook;
- student/teacher navigation;
- provenance;
- Course Board visibility;
- declared Activity identity/provenance;
- no student links to reserved teacher/solution assets;
- Content Pack/Course Design lesson-source parity.

M04 retains technical canary tests; M05 retains a dedicated pedagogical static QA.

## Catalog synchronization helper

`scripts/sync_authoring_catalog.py` derives the lesson source list from Content Pack `content_items`.

```text
python scripts/sync_authoring_catalog.py          → check only
python scripts/sync_authoring_catalog.py --write  → synchronize pack/design source lists
```

The workflow runs the helper in fail-closed check mode before the authoring QA.

---

# 6. GitHub Actions blocker #8 — ROOT CAUSE NARROWED

A diagnostic job containing only `runs-on` + one `echo`, with no external action, still failed on Ubuntu and Windows with:

```text
conclusion = failure
steps = null
```

Therefore checkout/setup-python/action allow-list/course tests are ruled out: a hosted runner is not starting.

Cross-repo evidence:

- private `tpsi-quarto-docente` had a successful private Actions run on **2026-08-19**;
- the same private repo shows equivalent pre-step failures from **2026-08-21**.

Leading hypothesis: private Actions quota/budget/spending stop. Alternative: organization hosted-runner policy changed in that window. Exact Billing state is not exposed by the connector and must not be guessed.

The temporary diagnostic job has been removed. `python-docente#8` records the admin checks.

No `steps: null` run is evidence that the authored tests passed or failed.

---

# 7. TheBitLab grading/runtime architecture

- P0 — manual/trace/design evidence;
- P1 — single-file stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — external `romeo-sim` runtime.

Never distort P2/P3/P4 outcomes into P1 just to obtain a score.

---

# 8. Open delivery/platform gates

- `python-docente#2` — managed Classroom Environment;
- `python-docente#6` — beginner REPL/editor workflow;
- `python-docente#7` — P1 canary;
- `python-docente#8` — private Actions runner blocker;
- `2cornot2c#753/#754` — Course Environment + Flowchart Lab;
- `2cornot2c#755` — Course Workspace/Open Course UX;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior;
- `romeo-sim` cross-profile certification.

P2/P3/P4 block only the promise of deterministic autograding, not teaching the concept.

---

# 9. Sources / friedpython

Thematic inventory is complete and snapshot pinned. Each candidate exercise/example still requires individual review and modernization before reuse; no wholesale import.

---

# 10. Git / Container

Git remains a separate progressive curriculum; Python consumes only G1 from PY2-05/Checkpoint A. Existing Git handouts will be requested when definitive G1 or the standalone Git course enters production.

Container/Docker remains a separate future course (`kinderp/docker101#1`).

---

# 11. Next controlled work

1. M11 — counters/accumulators/min-max/search/flags;
2. M12 — nested loops + intuitive work/cost reasoning;
3. then PY2-04 will be fully materialized;
4. continue module-by-module without new autograded Activities until profile certification;
5. when #8 is resolved, execute the already-written catalog/M04/M05/Course Board/P1 gates;
6. certify M04 golden slice;
7. later implement/certify Flowchart Lab, P2/P4/P3 and `romeo-sim` as required.

---

# Gate status

```text
Curriculum architecture        FROZEN ✅
Editorial modules M04-M10      CREATED 🟡 draft
PY2-02 editorial               COMPLETE 🟡 draft
PY2-03 editorial               COMPLETE 🟡 draft
PY2-04 editorial               2/4 modules 🟡
P1 golden vertical slice       CREATED / NOT CERTIFIED 🟡
Private Actions runners        BLOCKED 🔴 #8
Content Pack 1.0 approved      NOT YET ⏳
Ready for classroom / GO       NOT YET ⏳
```

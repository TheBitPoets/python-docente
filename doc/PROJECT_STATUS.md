# python-docente — project status

## Current phase

**Curriculum FROZEN + controlled module-by-module authoring.**

Canonical curriculum freeze:

`doc/CURRICULUM_FREEZE_2026_2027.md`

Decision owner approval: **2026-08-24**.

The second-year *what/sequence/outcomes* are stable. Content Pack approval and classroom readiness remain separate later gates.

## Current branch / review surface

- branch: `agent/course-architecture`
- draft PR: `#1 — Frozen Python second-year curriculum + M04 vertical slice`

The PR remains draft because delivery certification is not complete.

---

# 1. Curriculum — DONE / FROZEN

- 33 weeks × 3h = 99 nominal hours;
- 30 core weeks = 90h;
- 3 checkpoint/buffer weeks = 9h;
- 2 active-theory hours + 1 lab hour;
- M00–M30;
- UDA specs `PY2_01_SPEC.md` … `PY2_10_SPEC.md` complete;
- OOP mandatory weeks 29–32;
- no mandatory new prerequisite week 33;
- spiral test/trace/debug/refactor/data-model reasoning.

Frozen sequence:

```text
PY2-01 problem solving / algorithms / flow charts
PY2-02 REPL / first Python / types / I-O
PY2-03 selection / Boolean logic
PY2-04 loops / algorithmic patterns
PY2-05 functions / decomposition / assert / regression
Checkpoint A
PY2-06 strings
PY2-07 lists / tuples / alias-copy / matrices
Checkpoint B
PY2-08 set / dict / data-model choice
PY2-09 text files / pathlib / predictable errors
PY2-10 classes / objects / composition / OOP capstone
Checkpoint C
```

---

# 2. Editorial content materialized — M04…M08

The draft Content Pack currently materializes **five consecutive modules**.

## M04 — Interprete, REPL, valori e I/O

- lesson `content/python/04_INTERPRETE_REPL_VALORI_IO.md`;
- Marp deck;
- teacher runbook;
- one real P1 Activity canary: `py2-activity-b-input-somma-001`;
- dedicated static QA + Course Board round-trip + TheBitLab consumer smoke.

M04 remains the **golden technical vertical slice** and is not yet certified (`#7`).

## M05 — Espressioni, operatori e prime funzioni

- lesson/deck/runbook present;
- `/`, `//`, `%`, precedence, f-string, built-ins intro;
- first small pure-function preview;
- `return` vs `print` preview;
- dedicated pedagogical static QA;
- no new materialized P1 Activity.

## M06 — Booleani, confronti e `if`

- lesson/deck/runbook present;
- comparisons, `=` vs `==`, `if/else`, indentation, branch trace;
- boundary tests below/on/above threshold;
- Romeo `y1-u14-condizioni` only as optional applied reference;
- no new materialized P1 Activity.

## M07 — `elif`, exclusive cases and Boolean composition

- lesson/deck/runbook present;
- first-true branch semantics;
- independent `if` vs mutually exclusive `if/elif/else`;
- `and`, `or`, `not`;
- intervals/chained comparisons after explicit logical form;
- short-circuit only as controlled intuition;
- no new materialized P1 Activity.

## M08 — nesting, validation and refactoring

- lesson/deck/runbook present;
- genuine vs accidental nesting;
- path trace/coverage;
- domain validation before classification;
- explicit boundary: detect invalid input now, repeat with `while` later;
- refactoring protected by unchanged test cases;
- no `try/except` or `while` introduced prematurely;
- no new materialized P1 Activity.

Therefore **PY2-02 and PY2-03 are editorially materialized**. PY2-01 remains specification-only until Flowchart Lab delivery is resolved.

---

# 3. Authoring model / Course Board — ACTIVE

`python-docente` is a Course Workspace:

- `doc/course_design.json` contains the frozen UDA/checkpoint skeleton;
- `content/python/content-pack.json` is `thebitlab.content-pack.v1 / 0.1.0 / draft`;
- Course Board sources now expose M04…M08 plus all design/freeze docs;
- Content Pack = module/file identity;
- Course Board = heading-tree editorial granularity;
- repository = mutable source of truth;
- Git = history/review;
- Course Bundle = immutable publication state.

`2cornot2c#755` tracks first-class Open Course UX and bulk “add whole module/file” insertion.

---

# 4. Scalable authoring QA — WRITTEN

`tests/course_authoring_catalog.py` uses the Content Pack as the authoritative catalog of materialized modules and checks for every module:

- canonical numbered lesson filename/order;
- lesson H1;
- Marp deck;
- teacher runbook;
- student/teacher navigation;
- Content Pack provenance;
- Course Board source visibility;
- declared Activity directories/IDs/provenance;
- no student-facing links to teacher/solution/hidden assets;
- Content Pack/Course Design lesson-source parity.

M04 retains technical canary tests. M05 retains a dedicated pedagogical QA. M06–M08 are covered by the scalable catalog plus review criteria in their lessons/runbooks.

The workflow includes the scalable catalog check, but no current green evidence exists because #8 prevents runner startup.

---

# 5. P1 technical canary — CREATED, NOT CERTIFIED

`py2-activity-b-input-somma-001`:

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

Certification issue: `python-docente#7`.

No additional P1 Activities are materialized until this canary has evidence.

---

# 6. GitHub Actions private-repo blocker #8 — ROOT CAUSE NARROWED

Diagnostic commit `355f3e25fe7ec05cd793c80a04d41b71c079a3ca` temporarily added a `runner-diagnostic` matrix job containing only:

```text
runs-on
+ one echo step
```

No checkout, setup-python or third-party action.

Run `32805406089` still reported on Ubuntu and Windows:

```text
conclusion = failure
steps = null
```

Therefore the course YAML/test body/action allow-list are ruled out: a GitHub-hosted runner is not starting.

Cross-repo evidence:

- private `tpsi-quarto-docente` had successful Actions run `32235106172` on **2026-08-19**;
- its later private PR records the same pre-step failure from **2026-08-21**;
- public repositories do not consume private-repository included Actions minutes.

Leading hypothesis: private GitHub Actions quota/budget/spending stop. Alternative: organization hosted-runner policy changed in the same window. Exact billing state is not available through the connector and must not be guessed.

The temporary diagnostic job has been removed. #8 records the admin checks for Organization Actions settings and Billing/Budgets.

---

# 7. TheBitLab grading/runtime architecture — DESIGNED, IMPLEMENTATION GATES OPEN

`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`:

- P0 — manual/trace/design evidence;
- P1 — single-file stdin/stdout;
- P2 — function behavior (`2cornot2c#756`);
- P3 — object behavior (`2cornot2c#758`);
- P4 — filesystem behavior (`2cornot2c#757`);
- Romeo — external `romeo-sim` runtime.

Never distort a P2/P3/P4 learning outcome into P1 solely to obtain a score.

---

# 8. Classroom Environment / platform gates — OPEN

- `python-docente#2` — managed Classroom Environment certification;
- `python-docente#6` — beginner REPL/editor workflow;
- `python-docente#7` — P1 canary certification;
- `python-docente#8` — private Actions pre-execution blocker;
- `2cornot2c#753/#754` — Course Environment + Flowchart Lab;
- `2cornot2c#755` — Course Workspace/Open Course UX;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior;
- `romeo-sim` cross-profile certification.

P2/P3/P4 block the promise of deterministic autograding, not teaching the concepts.

---

# 9. Romeo — MAPPING DONE, DELIVERY OPEN

Strong selective use remains:

- PY2-03 conditions;
- PY2-04 loops;
- PY2-05 functions/top-down/debug;
- PY2-10 OOP/capstone.

No forced Romeo in strings/dicts/files. Hardware is never core.

---

# 10. Git / Container — ARCHITECTURE DONE

Git is a separate progressive curriculum; Python second year consumes G1 from PY2-05 / Checkpoint A. Existing Git handouts are requested only when definitive G1 or the standalone Git course enters production.

Container/Docker remains a separate future curriculum based on `kinderp/docker101#1`.

---

# 11. Sources / friedpython

Thematic audit is done for strings/lists/tuples/dicts/files and the snapshot is pinned. Before reuse each candidate exercise/example still requires individual audit and modernization; no wholesale import.

---

# 12. Next controlled work

1. proceed with **M09** (`while`, state change, termination, repeated validation);
2. then M10–M12 to materialize PY2-04 loops;
3. continue module-by-module, no new autograded Activity until the corresponding profile is certified;
4. resolve #8 administratively when possible and execute the already-written M04/M05/catalog/Course Board/P1 gates;
5. certify M04 golden vertical slice;
6. build/verify slide artifact pipeline;
7. implement/certify Flowchart Lab before declaring PY2-01 delivery ready;
8. later P2/P4/P3 before relying on those grading profiles;
9. certify `romeo-sim` before making Romeo missions mandatory.

---

# Gate status

```text
Curriculum architecture        FROZEN ✅
Editorial modules M04-M08      CREATED 🟡 draft
P1 golden vertical slice       CREATED / NOT CERTIFIED 🟡
Private Actions runners        BLOCKED 🔴 #8
Content Pack 1.0 approved      NOT YET ⏳
Ready for classroom / GO       NOT YET ⏳
```

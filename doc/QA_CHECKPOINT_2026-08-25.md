# Python secondo — QA checkpoint 2026-08-25

> Audit base head: `0140c5b4917633075853d700f98d35f8a921e0dc`  
> Scope: **repository structure + editorial state + Git G1 cross-course boundary**.  
> This is **not** a runtime/CI certification and **not** classroom-ready evidence.

## Result summary

```text
Curriculum freeze                         VERIFIED PRESENT
M04–M30 canonical lessons                 27/27 PRESENT
M04–M30 Marp source decks                 27/27 PRESENT
M04–M30 teacher runbooks                  27/27 PRESENT
Checkpoint A/B/C student guides           3/3 PRESENT
Checkpoint A/B/C teacher runbooks         3/3 PRESENT
Git G1 consumer config                    PRESENT
Git G1 anti-divergence test               PRESENT
M04 P1 canary Activity                    PRESENT
PY2-01 final digital lesson               INTENTIONALLY ABSENT / SPEC-only
Runtime/CI gates                          NOT EXECUTED — pre-runner blocker #8
Content Pack approved                     NO
Classroom ready                           NO
```

## 1. Annual editorial surface

Recursive tree inspection confirms a contiguous canonical Python editorial surface:

```text
content/python/04_...md
...
content/python/30_CAPSTONE_OOP.md
```

with matching source decks:

```text
slides/python/modules/04_...md
...
slides/python/modules/30_CAPSTONE_OOP.md
```

and matching teacher runbooks:

```text
teacher/M04_RUNBOOK.md
...
teacher/M30_RUNBOOK.md
```

This proves **presence and naming continuity**, not semantic correctness of every lesson/deck/runbook.

The stronger invariant remains encoded in `tests/course_authoring_catalog.py`, which must execute once CI/runtime capacity is restored.

## 2. Checkpoints

Present:

```text
student/CHECKPOINT_A.md
student/CHECKPOINT_B.md
student/CHECKPOINT_C.md
teacher/CHECKPOINT_A_RUNBOOK.md
teacher/CHECKPOINT_B_RUNBOOK.md
teacher/CHECKPOINT_C_RUNBOOK.md
```

Checkpoint A has been realigned to canonical Git G1 consumption.

## 3. Git G1 boundary

Structural integration is complete.

Provider candidate:

```text
TheBitPoets/git
G1 ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
provider contract: doc/G1_CONSUMER_CONTRACT.md
```

Python consumer:

```text
config/git-g1-consumer.json
```

Progression:

```text
M14–M16
  G1.OBSERVE.STATUS / G1.OBSERVE.DIFF — guided

Checkpoint A
  status → diff → test → add → diff --staged → commit → status → log/show

second-semester projects
  G1.WORKFLOW.CHECKPOINT + G1.RECOVERY.BASIC — progressive independence
```

Static anti-divergence gate:

```text
tests/git_g1_consumer_contract.py
```

Workflow gate is present in `.github/workflows/thebitlab-python-smoke.yml`.

## 4. Stale-document cleanup performed

The audit found legacy statements that no longer matched current architecture.

Corrected:

- `doc/CROSS_COURSE_CURRICULA.md` — Git is no longer described as a future course; it points to `TheBitPoets/git` and current G1;
- `doc/OPEN_DECISIONS.md` — Git G1 structural design is no longer listed as an unresolved future design decision;
- `doc/APPROVED_DECISIONS_2026_2027.md` — explicitly marked historical pre-freeze and aligned with the final rule that Git is a separate cross-course curriculum.

Canonical authority remains:

```text
doc/CURRICULUM_FREEZE_2026_2027.md
```

## 5. PY2-01 is not an accidental missing module

PY2-01 remains SPEC-only by design while the digital Flowchart Lab / Classroom Environment boundary is unresolved.

Valid fallback remains:

```text
paper / whiteboard
→ pseudocode
→ manual flow chart
→ trace
→ test cases
```

Do not create a final digital lesson merely to remove the apparent gap before `2cornot2c#753/#754` is truthful/certified.

## 6. Activity/grading boundary

Current materialized Python canary:

```text
py2-activity-b-input-somma-001
```

Its P1 certification remains `python-docente#7`.

Do not mass-produce autograded Activities until the needed profile is certified:

- P1 stdin/stdout;
- P2 function behavior;
- P3 object behavior;
- P4 filesystem behavior;
- external `romeo-sim` domain evidence.

## 7. CI status

Latest run observed on audit base head:

```text
run 32883608048 / #207
Ubuntu: failure, steps=null
Windows: failure, steps=null
```

Therefore no workflow step started. In particular, none of these can be claimed PASS or FAIL from that run:

- authoring catalog sync;
- full authoring catalog QA;
- Git G1 consumer test;
- M04/M05 static QA;
- Course Board round-trip;
- TheBitLab Python consumer smoke.

Issue: `python-docente#8`.

## 8. QA conclusion

### Structural/editorial inventory

**PASS at repository-tree level.** The expected M04–M30 lesson/deck/runbook surfaces and all three checkpoints are present.

### Cross-course Git architecture

**PASS at structural-contract level.** Python consumes canonical G1 through an explicit contract and does not duplicate the Git curriculum.

### Executable validation

**BLOCKED.** Private Actions still fails before runner startup; authored gates remain unexecuted.

### Classroom readiness

**NOT YET.** Requires platform/profile certification, PY2-01 delivery resolution, artifact QA, teacher/provenance review and real TheBitLab rehearsal.

## Next QA slice

1. inspect remaining historical/design documents for stale status claims;
2. review Content Pack/Course Design source parity once executable validation is available;
3. perform targeted semantic review of lesson/deck/runbook consistency by UDA rather than generating new content;
4. resolve Flowchart Lab boundary before PY2-01 final materialization;
5. restore private Actions and rerun unchanged gates first.

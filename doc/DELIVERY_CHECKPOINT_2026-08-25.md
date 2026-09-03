# Python secondo — Delivery Checkpoint 2026-08-25

> Stato: **post-semantic-review / pre-certification**  
> Branch: `agent/course-architecture`  
> PR: `#1` — keep DRAFT.

## Stato vero del corso

```text
Curriculum architecture        FROZEN
M04–M30 editorial surfaces     COMPLETE / draft
Semantic review M04–M30        COMPLETE / draft
Checkpoint A/B/C review        COMPLETE / draft
25 frozen outcomes             MAPPED
Python automated Activities    1 canary
Git G1 structural consumer     COMPLETE / delivery evidence pending
PY2-01 final digital delivery  SPEC-only / Flowchart Lab pending
Slide source decks             27/27 present
Slide artifacts HTML/PDF/PPTX  NOT BUILT/NOT CERTIFIED
Teacher sign-off               PENDING
Private Actions                BLOCKED before runner startup
Content Pack 1.0 approved      NO
Classroom-ready / GO           NO
```

---

# Completed layers

## Curriculum

Canonical freeze:

```text
doc/CURRICULUM_FREEZE_2026_2027.md
```

## Semantic review

Index:

```text
doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md
```

Shared pacing boundary:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

## Coverage

```text
doc/COVERAGE.md
config/curriculum-coverage.json
tests/coverage_contract.py
```

Coverage axes remain separated from Activity/grading/readiness.

## Git G1

```text
config/git-g1-consumer.json
tracks/secondo/GIT_G1_INTEGRATION.md
tests/git_g1_consumer_contract.py
```

Mode:

```text
embedded-outcome-subset
```

## Activity planning

```text
tracks/secondo/ACTIVITY_COVERAGE_PLAN.md
```

No mass materialization is authorized before the relevant profile/canary is certified.

## Slide source / release design

```text
tests/slide_source_quality.py
doc/SLIDE_ARTIFACT_PIPELINE.md
config/slide-build-profile.json
```

Renderer/runtime pins are intentionally still unset; floating `latest` is forbidden.

## Teacher sign-off

```text
teacher/TEACHER_SIGNOFF_CHECKLIST.md
```

Status remains intentionally `PENDING`.

---

# Provenance finding

Audit:

```text
doc/PROVENANCE_AUDIT_2026-08-25.md
```

The canonical friedpython audit set now includes:

```text
SOURCE_CATALOG.md
FRIEDPYTHON_MAPPING.md
FRIEDPYTHON_LISTS_TUPLES_AUDIT.md
FRIEDPYTHON_DICTS_AUDIT.md
FRIEDPYTHON_FILES_AUDIT.md
```

The older `python-source-audits` explicit manifest in Content Pack/Course Design must be aligned.

Helper added:

```text
scripts/sync_source_audit_manifest.py
```

The helper patches only the `files` array of the target source object and validates semantic convergence; it does not re-dump the entire documents.

A dedicated open issue tracks the manifest fix. Until fixed, provenance approval remains blocked.

---

# Static validation entrypoint

Added:

```text
python scripts/run_static_quality.py
```

It aggregates repository-only checks:

- authoring source sync;
- authoring catalog;
- semantic review boundary;
- Git G1 consumer;
- frozen outcome coverage;
- slide source QA;
- M04 static QA;
- M05 static QA.

Important:

```text
static suite
≠ TheBitLab consumer/rehearsal
```

The entrypoint has been authored but is not claimed PASS until run in an actual clone/runner.

---

# CI truth

`python-docente#8` still prevents hosted-runner startup for this private repository.

Observed pattern:

```text
job created
→ runner never starts
→ steps=null
```

Therefore:

- a red Actions run is not evidence that the static checks failed;
- no authored gate is called green without an executed step/log;
- do not rewrite course semantics merely to make a pre-runner infrastructure failure disappear.

---

# Next executable sequence

## 1. Provenance manifest

Run in a controlled clone:

```text
python scripts/sync_source_audit_manifest.py
python scripts/sync_source_audit_manifest.py --write
python scripts/sync_source_audit_manifest.py
```

Review the minimal diff before commit.

## 2. Static quality

```text
python scripts/run_static_quality.py
```

Fix actual failures only after they execute.

## 3. Slide renderer/toolchain

- verify authoritative current renderer/version;
- pin exact renderer + Node/runtime requirements;
- implement one build entrypoint;
- produce 27× HTML/PDF/PPTX according to release profile;
- structural artifact QA;
- visual review sample M04/M11/M18/M22/M26/M30.

## 4. Teacher sign-off

Use the human checklist. Do not auto-fill approval fields.

## 5. Platform/delivery

- PY2-01 Flowchart boundary;
- M04/P1 certification;
- P2/P4/P3 as needed;
- Git consumer rehearsal;
- Romeo only when certified;
- Course Workspace round-trip;
- real student-profile rehearsal.

## 6. Promotion

Only after the relevant gates:

```text
Content Pack 1.0.0 / approved
→ real TheBitLab rehearsal
→ GO classroom
```

No current artifact authorizes those claims yet.

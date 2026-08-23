# python-docente — project status

## Current phase

**Curriculum architecture / first vertical-spec design.**

Do not generate the full set of lessons, slides or Activities yet.

## Current branch

`agent/course-architecture`

## What exists

### Curriculum / track

- overall course architecture;
- full roadmap from beginner to professional Python;
- second-year 33-week track;
- detailed second-year module map M00–M30;
- spiral curriculum model;
- 2 theory-active + 1 lab delivery profile;
- mandatory OOP boundary;
- professional skills matrix;
- assessment model + four-assessment calendar;
- AI policy;
- cross-course Git/Container boundary.

### Sources / provenance

- source catalog;
- Think/Pensare in Python, Learning/Imparare Python, Fluent Python, Python in a Nutshell, Pluralsight and official docs roles;
- `friedpython` source mapping/snapshot;
- source → module → Activity planning matrix.

### TheBitLab authoring compatibility

- `doc/course_design.json` exists and contains the full 33-week UDA/checkpoint structure;
- Course Design declares explicit local Markdown sources;
- `content/python/content-pack.json` is a draft `thebitlab.content-pack.v1` manifest referencing the same Course Design;
- `activities/python/` is the reserved Activity 1.0 root;
- Content Pack sources and Course Design sources are kept semantically aligned;
- `doc/THEBITLAB_AUTHORING_COMPATIBILITY.md` records the dashboard round-trip;
- TheBitLab Course Board already supports external course workspaces through `--root`;
- product-level `Open course` / bundle inspection is tracked by `TheBitPoets/2cornot2c#755`.

### Platform decisions

- TheBitLab Classroom Environment is the only supported student environment;
- Python 3.12 is the initial certified baseline;
- standard Python REPL precedes scripts/VS Code; IPython optional;
- target cross-platform Flowchart Lab; Flowgorithm optional Windows companion only;
- Romeo is an external simulated applied thread/runtime, not the curriculum;
- environment/Flowchart architecture is tracked by `TheBitPoets/2cornot2c#753` and draft PR `#754`.

### First vertical specification

- `tracks/secondo/PY2_01_SPEC.md` specifies the first UDA in detail;
- M00–M03 objectives, misconceptions, active-theory rhythm, Activity A–E candidates, evidence, remediation/enrichment and platform fallback are defined;
- the first UDA spec is already included in the Course Board/Content Pack source catalog.

## Open blockers before Content Pack 1.0 freeze

1. implement/certify the cross-course Classroom Environment contract;
2. implement/certify Flowchart Lab artifact + execution/evidence contract;
3. define the Python Activity/runner contract and resource limits;
4. certify managed VS Code host/guest workflow;
5. complete selective Romeo mapping by module;
6. review/finalize assessment rubric weights;
7. convert final lesson Markdown into stable Course Design items;
8. run a real Course Board `--root` round-trip smoke against `python-docente`;
9. produce/review one small complete vertical slice before mass content production.

## Next Python design steps

1. review PY2-01 specification as the template for subsequent UDA specs;
2. define stable Activity IDs/contracts for PY2-01 without pretending Flowchart Lab is implemented;
3. specify PY2-02 (REPL, first scripts, types/I/O, expressions, first tiny functions);
4. define the minimal Python runner/autograding boundary for deterministic exercises;
5. map Romeo only where it adds a genuine applied problem;
6. after the first two UDA specs, reassess time/load before expanding to the whole course.

## External curricula queued

### Git

A future separate progressive Git curriculum is planned for all school years. Python second year consumes only a small G1 slice (`status`, `diff`, `add`, `commit`, history concept). Existing teacher Git handouts will be requested when the Git curriculum or the concrete G1 micro-module enters production.

### Container

The future Container/Docker curriculum remains separate and is tracked in `kinderp/docker101#1`. Python professional stages consume container literacy but do not duplicate that course.

## Explicit non-goals in the current phase

- no mass lesson generation;
- no mass slide generation;
- no importing all of `friedpython`;
- no forcing Romeo into every module;
- no treating Git/Container as duplicated sub-courses inside Python;
- no freezing tool choices as if they were language concepts;
- no claim that Flowchart Lab/VS Code/bundle UX is implemented merely because architecture exists;
- no claim that the course is ready for students yet.

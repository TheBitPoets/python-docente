# Slide artifact review — real build 2026-08-27

Status: **REAL BUILD + STRUCTURAL QA PASS; sampled PDF visual review PASS; PPTX LibreOffice consumer PASS WITH LIMITATION; Microsoft PowerPoint review still pending.**

This document records engineering evidence only. It does **not** replace `teacher/SLIDE_VISUAL_REVIEW.md`, human teacher sign-off, or classroom GO.

## Build identity

GitHub Actions:

```text
workflow: Python slide release artifacts
run:      33116692428 / #1
job:      98673027862
result:   SUCCESS
artifact: 9664877644
artifact name: python-slide-release-c6b57d98184e5937a5d449c50b5d726dc2130aa7
artifact ZIP digest: sha256:4693a11cf7c77c987e7396e2375911566409746c0378498a925b38b4e105d268
```

Build manifest:

```text
schema: python.slide-artifact-manifest.v1
source commit: c6b57d98184e5937a5d449c50b5d726dc2130aa7
build id: github-33116692428-1
module count: 27
```

Toolchain reported by the real build:

```text
Marp CLI: @marp-team/marp-cli v4.5.0
Marp Core: v4.4.0
Node: v26.5.0
browser: Google Chrome for Testing 149.0.7827.55
PDF parser: pypdf 6.16.2
platform: linux/amd64
container: ghcr.io/marp-team/marp-cli@sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
```

## Generated surface

The uploaded and independently inspected artifact contains:

```text
27 × deck.html
27 × deck.pdf
27 × deck.pptx
1  × build-manifest.json
```

Total source/rendered slides across M04–M30: **515**.

Aggregate artifact bytes recorded in the manifest:

```text
HTML:  3,308,759 bytes
PDF:   2,609,992 bytes
PPTX: 53,549,137 bytes
```

The workflow's `Build and validate HTML PDF PPTX artifacts` step and artifact upload both completed successfully. Therefore the real generated files, not only source Markdown, passed `tests/slide_artifact_quality.py`.

## Mandatory sampled PDF visual review

The generated PDFs for the required sample were rasterized from the actual artifact and visually inspected:

| Module | Pages | Engineering visual result |
|---|---:|---|
| M04 | 23 | PASS |
| M11 | 20 | PASS |
| M18 | 17 | PASS |
| M22 | 19 | PASS |
| M26 | 18 | PASS |
| M30 | 18 | PASS |

Observed across the sample:

- no unexpected blank slides;
- no title overlap or clipping;
- no visible text outside the canvas;
- code blocks remain contained and legible;
- tables/trace blocks inspected remain inside their slide;
- hierarchy between headings, prose and code remains consistent;
- `MUST MASTER`, `GUIDED EXPOSURE` and `ENRICHMENT / BACKUP` labels remain visually distinguishable;
- no obvious teacher/grader-only implementation detail appears in the sampled rendered PDF decks.

This is an engineering visual inspection of rendered artifacts, not the teacher's final pedagogical sign-off.

## PPTX consumer spot-check

The six mandatory sample PPTX files were opened headlessly by **LibreOffice Impress** and successfully converted back to PDF:

```text
M04: 23 PPTX slides -> 23 PDF pages
M11: 20 PPTX slides -> 20 PDF pages
M18: 17 PPTX slides -> 17 PDF pages
M22: 19 PPTX slides -> 19 PDF pages
M26: 18 PPTX slides -> 18 PDF pages
M30: 18 PPTX slides -> 18 PDF pages
```

Selected first/middle/last pages were raster-compared with the canonical generated PDFs. Mean absolute RGB differences remained small (roughly 1.85–3.22 on a 0–255 channel scale), consistent with a re-render rather than a layout change.

### Important PPTX editability limitation

Inspection of the generated PPTX OOXML shows that Marp places each rendered slide image as the **slide background**. The sampled slide XML contains no native editable text shapes for the rendered deck content; the background relationship points to PNG media such as `Slide-1-image-1.png`.

Therefore the supported statement is:

```text
PPTX presentation/render compatibility: observed in LibreOffice Impress
full native PowerPoint editability: NOT PROVIDED by this Marp export model
Microsoft PowerPoint target opening: still requires real consumer verification
```

Do not advertise these PPTX files as fully editable PowerPoint decks.

## HTML boundary

All 27 HTML artifacts passed the real structural QA, including rendered section counts matching the corresponding source/PDF/PPTX slide counts. The current engineering review does not claim a separate human browser-by-browser visual sign-off; the PDF sample is the completed visual layer inspected here.

## Remaining #10 gates

The real-build and structural-artifact blockers are now cleared. Before closing #10:

1. perform the explicit target **Microsoft PowerPoint** open/presentation check on the mandatory PPTX sample (or document an accepted limitation if PowerPoint is intentionally not a supported target);
2. complete the human `teacher/SLIDE_VISUAL_REVIEW.md` decision;
3. expand visual review if the human reviewer finds a systematic issue.

No Content Pack approval or classroom-readiness claim follows automatically from this artifact PASS.

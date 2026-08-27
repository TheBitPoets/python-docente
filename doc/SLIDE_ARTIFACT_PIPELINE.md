# Python secondo — Slide Artifact Pipeline

> Stato: **toolchain pinned / M04–M30 real build PASS / final M00–M30 rebuild pending**  
> Scope release corrente: **31 deck Marp M00–M30**.  
> Gli artifact sono derivati: il Markdown resta l'unica fonte editoriale.

## Obiettivo

```text
31 Markdown canonici M00–M30
→ source QA
→ renderer/runtime pinned
→ 31 HTML + 31 PDF + 31 PPTX
→ structural artifact QA
→ engineering sample review
→ human/target-consumer review
```

La materializzazione di M00–M03 è successiva al primo build reale M04–M30; quindi quel build rimane evidence valida per il sottoinsieme storico, ma **non** soddisfa il release target finale a 31 moduli.

---

# Gate 0 — source inventory

Gate:

```text
tests/slide_source_quality.py
```

Richiede esattamente:

```text
M00 ... M30 = 31 deck
```

oltre a:

- frontmatter Marp;
- `paginate: true`;
- `size: 16:9`;
- titolo/H1 modulo;
- nessun link teacher/solution/hidden-test;
- nessun leak di dettagli grader/delivery interni;
- deck non accidentalmente ridotti a poche card.

Source QA non equivale al rendering reale.

---

# Gate 1 — toolchain pinned

Profilo canonico:

```text
config/slide-build-profile.json
```

Pin:

```text
@marp-team/marp-cli 4.5.0
platform: linux/amd64
image:
  ghcr.io/marp-team/marp-cli@sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
multiarch manifest:
  sha256:4982f2f4e9b9ba6dc97f5cbb0eb0e286ae7654642ccf0778169d57c1c552a65a
Node: 26.5.0
PDF structural parser: pypdf 6.16.2
browser: Chromium binary congelato dall'image digest e riportato nel build manifest
```

Non usare `latest` nella release pipeline.

Il digest del container è l'autorità runtime perché congela anche il browser effettivamente installato nell'immagine pubblicata.

---

# Gate 2 — build reale

Entrypoint:

```text
scripts/build_slide_artifacts.py
```

Esecuzione:

```bash
python scripts/build_slide_artifacts.py --build-id <release-id>
```

Il builder usa `module_range` dal profilo e quindi ora richiede M00–M30. Per ogni modulo costruisce:

```text
deck.html
deck.pdf
deck.pptx
```

poi registra:

- source commit SHA;
- source SHA-256;
- build id/timestamp;
- Marp/Node/browser/pypdf provenance;
- artifact path/byte/SHA-256;
- source/rendered slide count.

Manifest:

```text
dist/slides/python/build-manifest.json
```

`dist/` resta non versionato.

---

# Gate 3 — structural artifact QA

Gate:

```text
tests/slide_artifact_quality.py
```

Per ogni modulo richiede coerenza tra source, HTML, PDF e PPTX.

## HTML

- `<section>` renderizzate;
- numero section = slide sorgente.

## PDF

- PDF leggibile tramite page tree reale;
- non cifrato;
- page count = slide sorgente;
- MediaBox ~16:9;
- rotazione coerente.

## PPTX

- package ZIP valido;
- parti OOXML minime presenti;
- numero slide XML = slide sorgente.

Il conteggio atteso è profile-driven, non hardcoded a 27.

---

# Evidence reale già acquisita — M04–M30

Il 2026-08-27 il vecchio scope 27-moduli ha completato:

```text
workflow run: 33116692428 / #1
job:          98673027862
result:       SUCCESS
artifact id:  9664877644
```

Artifact:

```text
27 HTML + 27 PDF + 27 PPTX
515 slide complessive
```

Toolchain osservata:

```text
Marp CLI 4.5.0
Marp Core 4.4.0
Node 26.5.0
Chrome for Testing 149.0.7827.55
pypdf 6.16.2
```

Engineering PDF sample M04/M11/M18/M22/M26/M30: PASS. I sei PPTX campione sono stati aperti anche con LibreOffice Impress mantenendo il numero di slide.

Dettaglio:

```text
doc/SLIDE_ARTIFACT_REVIEW_2026-08-27.md
```

Questa evidence non viene cancellata dall'aggiunta di M00–M03; semplicemente non basta più per il release completo.

---

# PPTX truthfulness

L'ispezione OOXML del build reale ha mostrato che Marp esporta il contenuto renderizzato come **immagine di background della slide**.

Quindi possiamo affermare:

```text
PPTX presentabile/renderizzabile: observed
full native PowerPoint editability: NOT PROVIDED by this export model
```

Resta richiesto il vero open/presentation check in Microsoft PowerPoint se PowerPoint è consumer target.

---

# Gate 4 — visual review campionata

Per il nuovo scope minimo:

```text
M00 — orientamento / testo
M01 — pseudocodice + anti-esempio
M02 — flow chart / decisioni
M03 — loop / tabelle
M04 — primo Python/codice
M11 — trace/stato
M18 — testo/metodi
M22 — matrici
M26 — file/errori
M30 — capstone
```

Controllare artifact generati, non Markdown:

- overflow/tagli;
- codice leggibile;
- tabelle;
- slide bianche;
- differenze HTML/PDF/PPTX;
- apertura PPTX nel consumer target.

Se un difetto è sistemico, ampliare il campione.

---

# Quality boundary

Le slide non devono diventare una lesson compressa. Il confine didattico resta:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

M00–M03 devono inoltre preservare:

```text
pre-Python pedagogy
+ Flowchart candidate/fallback boundary
+ no fake diagram autograding
```

---

# CI/release workflow

```text
.github/workflows/slide-artifacts.yml
```

Resta `workflow_dispatch` only durante il normale sviluppo. Un trigger PR temporaneo può essere usato esclusivamente per ottenere una specifica evidence reale e deve essere rimosso subito dopo il run.

GitHub Actions è ora funzionante: il vecchio blocker #8 è chiuso.

---

# Promotion gate slide

Prima di `Content Pack 1.0.0 / approved` richiedere:

- source QA M00–M30 verde;
- real build **31/31 × HTML/PDF/PPTX**;
- structural artifact QA verde;
- sample review M00/M01/M02/M03/M04/M11/M18/M22/M26/M30;
- PowerPoint target decision/open check se supportato;
- problemi sistemici risolti;
- human visual decision;
- teacher sign-off generale separato.

## Non-goal

La pipeline slide non riapre il curriculum freeze e non trasforma artifact derivati in fonti editoriali.

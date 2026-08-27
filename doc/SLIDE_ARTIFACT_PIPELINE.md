# Python secondo — Slide Artifact Pipeline

> Stato: **toolchain pinned / build+artifact QA implemented / real build pending**  
> Scope: deck Marp M04–M30.  
> Non dichiara artifact già costruiti o visualmente approvati.

## Obiettivo

Trasformare i 27 deck Markdown canonici:

```text
slides/python/modules/04_...md
...
slides/python/modules/30_...md
```

in artifact riproducibili per delivery senza creare una seconda fonte di verità.

Principio:

```text
Markdown canonico
→ source QA
→ renderer/runtime pinned
→ HTML / PDF / PPTX
→ structural artifact QA
→ teacher visual review
```

Gli artifact sono **derivati**. Le modifiche editoriali partono sempre dal Markdown sorgente.

---

# 1. Gate 0 — source inventory

Gate:

```text
tests/slide_source_quality.py
```

Controlla almeno:

- 27/27 deck M04–M30;
- frontmatter Marp;
- `paginate: true`;
- `size: 16:9`;
- titolo e H1 modulo;
- nessun link teacher/solution/hidden-test;
- nessun leak di issue/profili P2/P3/P4 teacher-only;
- deck non ridotto accidentalmente a poche card.

Questo è **source QA**, non prova che PDF/PPTX siano renderizzati bene.

---

# 2. Gate 1 — toolchain pinned

Profilo canonico:

```text
config/slide-build-profile.json
```

Pin verificato il 2026-08-27:

```text
@marp-team/marp-cli 4.5.0
release tag v4.5.0
runtime strategy: official Marp container by immutable digest
platform: linux/amd64
image:
  ghcr.io/marp-team/marp-cli@sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
multi-arch manifest:
  sha256:4982f2f4e9b9ba6dc97f5cbb0eb0e286ae7654642ccf0778169d57c1c552a65a
Node in upstream v4.5.0 Dockerfile: 26.5.0
browser: Chromium binary contained in the exact image digest
```

Perché il digest container è l'autorità runtime:

- Marp CLI 4.5.0 richiede Node >=18 e supporta HTML/PDF/PPTX;
- PDF/PPTX richiedono un browser compatibile;
- l'immagine ufficiale v4.5.0 usa Node 26.5.0 e installa Chromium tramite Playwright;
- il Dockerfile upstream usa `playwright@latest` **al momento della costruzione dell'immagine**;
- quindi ricostruire oggi soltanto dal Dockerfile/tag potrebbe scegliere un browser diverso;
- il digest linux/amd64 congela invece i byte dell'immagine già pubblicata, incluso il browser effettivamente installato.

Il build manifest registra inoltre le versioni riportate a runtime da:

```text
marp --version
node --version
/usr/local/bin/chrome --version
```

Non usare `latest` nella release pipeline.

Riferimenti upstream verificati:

```text
https://www.npmjs.com/package/@marp-team/marp-cli
https://github.com/marp-team/marp-cli/releases/tag/v4.5.0
https://github.com/marp-team/marp-cli/blob/v4.5.0/Dockerfile
https://github.com/marp-team/marp-cli/pkgs/container/marp-cli
```

---

# 3. Build entrypoint

```text
scripts/build_slide_artifacts.py
```

Prerequisito locale/CI:

```text
Docker con supporto linux/amd64
```

Esecuzione release:

```bash
python scripts/build_slide_artifacts.py --build-id <release-id>
```

Il builder:

1. carica Content Pack e profilo;
2. richiede esattamente M04–M30;
3. pulisce `dist/slides/python/` salvo `--keep`;
4. verifica Marp/Node/browser nel container pinned;
5. costruisce per ogni modulo:
   - `deck.html`;
   - `deck.pdf`;
   - `deck.pptx`;
6. calcola SHA-256 e dimensione degli artifact;
7. registra source SHA-256, source commit SHA, build id e toolchain;
8. scrive:

```text
dist/slides/python/build-manifest.json
```

9. esegue automaticamente:

```text
tests/slide_artifact_quality.py
```

`dist/` è ignorato da Git: Markdown resta la fonte editoriale versionata.

---

# 4. Output target

```text
dist/slides/python/
  M04/
    deck.html
    deck.pdf
    deck.pptx
  ...
  M30/
    deck.html
    deck.pdf
    deck.pptx
  build-manifest.json
```

Decisione:

```text
Markdown = versionato
artifact = generati
release/course bundle = include artifact approvati
```

Non committare copie derivate soltanto per far sembrare il corso più completo.

---

# 5. Gate 2/3 — build completeness + structural artifact QA

Gate:

```text
tests/slide_artifact_quality.py
```

Per ogni modulo richiede:

```text
source presente e hash coerente
HTML presente / non vuoto / hash coerente
PDF presente / non vuoto / hash coerente
PPTX presente / non vuoto / hash coerente
numero slide/pagine coerente con il source
```

## HTML

- documento leggibile come testo;
- almeno una `<section>` renderizzata;
- numero di section uguale alle slide sorgente.

## PDF

- header PDF valido;
- EOF presente;
- conteggio delle page dictionary coerente con le slide sorgente.

## PPTX

- ZIP package valido;
- `[Content_Types].xml` presente;
- `ppt/presentation.xml` presente;
- parti `ppt/slides/slideN.xml` presenti;
- numero slide coerente col source.

Il gate controlla anche che manifest e profilo concordino su container digest, piattaforma, renderer e Node.

---

# 6. PPTX truthfulness

Marp CLI supporta la generazione PowerPoint, ma la presenza di un file `.pptx` non autorizza a promettere automaticamente:

- editabilità completa degli elementi;
- equivalenza dei font;
- oggetti PowerPoint nativi;
- fedeltà perfetta rispetto a HTML/PDF;
- comportamento identico in PowerPoint e LibreOffice.

La release può dichiarare soltanto:

```text
PPTX structurally valid
```

finché la review reale nel consumer target non documenta il comportamento effettivo.

---

# 7. Gate 4 — visual review campionata

Prima del teacher sign-off eseguire review visuale almeno su:

```text
M04 — REPL + codice
M11 — tabelle/trace/stato progressivo
M18 — testo/metodi/scelte
M22 — matrici/diagrammi
M26 — file/codice
M30 — capstone/recap
```

Controllare almeno:

- overflow;
- codice troppo piccolo;
- tabelle illeggibili;
- sovrapposizioni;
- pagine bianche;
- differenze importanti HTML/PDF/PPTX;
- apertura PPTX nel consumer target.

Se emerge un problema sistemico, estendere la review a tutti i deck interessati.

---

# 8. Quality criteria per studenti di seconda

Le slide non devono essere la lesson Markdown compressa.

Criteri:

- una domanda/modello principale per slide quando possibile;
- codice leggibile a distanza;
- trace e tabelle piccoli;
- termini nuovi solo se necessari;
- dettagli GUIDED/ENRICHMENT riconoscibili;
- niente issue id/grader internals teacher-only;
- niente setup unmanaged;
- più contenuto non significa automaticamente deck migliore.

La semantic review resta autorevole sul confine:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# 9. Source-to-artifact traceability

Manifest:

```text
python.slide-artifact-manifest.v1
```

Registra almeno:

```text
course_id
source commit SHA
build id / timestamp
Marp CLI reported version
Node reported version
browser reported version
container image + digest
module/source path
source SHA-256
expected slide count
artifact path / bytes / SHA-256
```

Gli artifact non sono nuove fonti editoriali.

---

# 10. CI boundary corrente

`python-docente#8` impedisce ancora l'avvio dei runner privati.

Quindi oggi possiamo affermare:

```text
27 source deck presenti
source quality gate scritto
toolchain pinned
builder implementato
structural artifact QA implementato
```

Non possiamo ancora affermare:

```text
27 HTML PASS
27 PDF PASS
27 PPTX PASS
visual review PASS
```

finché la build reale non viene eseguita.

---

# 11. Promotion gate

Prima di `Content Pack 1.0.0 / approved` per il layer slide richiedere:

- source QA realmente eseguito;
- container pinned disponibile;
- build completa 27/27 × HTML/PDF/PPTX;
- structural artifact QA verde;
- visual review campionata;
- problemi sistemici risolti;
- teacher sign-off.

## Non-goal

Il renderer non riapre il curriculum freeze. Outcome/progressione restano congelati; artifact/build sono delivery versionabile.

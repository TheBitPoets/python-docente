# Python secondo — Slide Artifact Pipeline

> Stato: **design/QA contract**  
> Scope: deck Marp M04–M30.  
> Non dichiara artifact già costruiti o validati.

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
→ renderer pinned
→ HTML / PDF / PPTX
→ artifact QA
→ teacher visual review
```

Gli artifact sono **derivati**. Le modifiche editoriali devono partire dal Markdown sorgente.

---

# 1. Gate 0 — source inventory

Il Content Pack determina quali moduli M04–M30 sono materializzati.

Per ogni modulo deve esistere esattamente un deck:

```text
content/python/NN_NOME.md
↔
slides/python/modules/NN_NOME.md
```

Gate:

```text
tests/slide_source_quality.py
```

Controlla almeno:

- 27/27 deck M04–M30;
- frontmatter Marp;
- `paginate: true`;
- `size: 16:9`;
- titolo;
- H1 del modulo;
- nessun link teacher/solution/hidden-test;
- nessun leak di issue/profili P2/P3/P4 teacher-only;
- deck non ridotto a poche card accidentali.

Questo è **source QA**, non prova che PDF/PPTX siano renderizzati bene.

---

# 2. Gate 1 — toolchain renderer

La pipeline definitiva deve usare lo stesso principio cross-course maturato in TPSI5:

```text
renderer/versione esatti
→ dichiarati nel repository
→ nessun "latest" implicito in CI
```

Prima della promotion del Content Pack si deve fissare esplicitamente:

- renderer Marp CLI/versione;
- runtime Node/versione se richiesto;
- browser/runtime usato dal renderer PDF quando pertinente;
- font/system dependencies realmente necessarie;
- eventuali flag PDF/PPTX.

Non dichiarare la pipeline riproducibile finché queste versioni non sono pinning esplicito.

## Regola PPTX

Il requisito è produrre un artifact PowerPoint utilizzabile per la delivery.

La pipeline deve verificare il comportamento effettivo del renderer scelto prima di promettere:

- editabilità completa;
- font equivalenti;
- oggetti nativi vs rasterizzati;
- compatibilità PowerPoint/LibreOffice.

Queste proprietà non vanno dedotte dal solo fatto che esista un file `.pptx`.

---

# 3. Output target

Struttura proposta:

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
```

Oppure artifact CI equivalenti se si decide di non versionare `dist/` nel repository.

Decisione consigliata:

```text
Markdown = versionato
artifact = generati dalla pipeline
release/course bundle = contiene artifact approvati
```

Non committare copie derivate soltanto per far sembrare il corso più completo.

---

# 4. Gate 2 — build completeness

Per ogni deck M04–M30 la build deve produrre tutti gli output richiesti dalla release profile.

Checklist machine-checkable futura:

```text
27 source deck
27 HTML
27 PDF
27 PPTX
nessun file vuoto
nessun errore renderer
```

Un fallimento su un formato non deve essere mascherato costruendo soltanto gli altri due.

Se il profilo release decide che un formato è opzionale, ciò va dichiarato nel profilo; non dedotto dinamicamente dalla riuscita della build.

---

# 5. Gate 3 — structural artifact QA

## HTML

Verificare almeno:

- file apribile;
- numero di slide non nullo;
- nessun riferimento locale rotto a asset obbligatori;
- title/module identity corretti.

## PDF

Verificare almeno:

- file PDF valido;
- numero pagine coerente col deck;
- nessuna pagina vuota inattesa;
- dimensione pagina coerente col profilo 16:9;
- testo/codice non troncato nei campioni visuali.

## PPTX

Verificare almeno:

- archivio PPTX valido;
- numero slide coerente;
- apertura in PowerPoint/consumer target;
- nessun asset mancante;
- comportamento di font/layout noto e documentato.

---

# 6. Gate 4 — visual review campionata

La source QA non trova problemi come:

- testo che esce dalla slide;
- codice troppo piccolo;
- tabelle illeggibili;
- titoli sovrapposti;
- pagine PDF bianche;
- differenze importanti tra HTML/PDF/PPTX.

Prima del teacher sign-off eseguire una review visuale almeno su deck rappresentativi della complessità:

```text
M04 — deck iniziale ricco / REPL + codice
M11 — tabelle/trace/stato progressivo
M18 — testo/metodi/scelte
M22 — matrici/diagrammi
M26 — file/codice
M30 — capstone/recap
```

Se emerge un problema sistemico, allargare la review a tutti i deck interessati; non trattarlo come problema isolato della singola slide.

---

# 7. Quality criteria per studenti di seconda

Le slide non devono essere la lesson Markdown compressa.

Criteri:

- una domanda/modello principale per slide quando possibile;
- codice leggibile a distanza;
- trace e tabelle piccoli;
- termini nuovi introdotti solo se necessari;
- dettagli GUIDED/ENRICHMENT visivamente riconoscibili;
- niente issue id/grader internals teacher-only;
- niente istruzioni di setup unmanaged;
- non confondere “più contenuto” con “migliore deck”.

La semantic review resta autorevole sul confine:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# 8. Source-to-artifact traceability

Ogni artifact deve poter dichiarare almeno:

```text
course_id
module_id / Mxx
source path
source commit SHA
renderer/toolchain version
build timestamp/release id
```

Il Course Bundle può usare questi dati per provenance/reproducibility.

Non serve inserirli tutti visivamente nelle slide; possono vivere nel manifest di build.

---

# 9. CI boundary corrente

La workflow privata contiene gate statici, ma `python-docente#8` impedisce ancora l'avvio dei runner.

Quindi oggi possiamo affermare:

```text
27 source deck presenti
source quality gate scritto
artifact pipeline progettata
```

Non possiamo ancora affermare:

```text
27 HTML PASS
27 PDF PASS
27 PPTX PASS
visual review PASS
```

finché una build reale non viene eseguita.

---

# 10. Promotion gate

Prima di `Content Pack 1.0.0 / approved` per il layer slide richiedere:

- source QA eseguito;
- renderer/toolchain pinned;
- build completa del release profile;
- structural artifact QA;
- visual review campionata;
- problemi sistemici risolti;
- teacher sign-off.

## Non-goal

Non bloccare il curriculum freeze su un dettaglio del renderer. Il freeze definisce outcome/progressione; artifact/build restano delivery versionabile.

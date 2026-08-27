# Python secondo — Provenance Audit 2026-08-25

> Stato: **audit editoriale/provenance aggiornato dopo allineamento manifest**  
> Non equivale a license legal review o Content Pack approval.

## Scopo

Verificare che il materiale canonico M04–M30 abbia una provenienza comprensibile e che i source package dichiarati non nascondano drift fra:

```text
file realmente presenti
↔ SOURCE_CATALOG
↔ Content Pack sources
↔ Course Design sources
↔ source_refs dei moduli
```

---

# 1. Materiale canonico

Il materiale studente/docente canonico del corso è originale TheBitPoets:

- lesson M04–M30;
- deck Marp M04–M30;
- runbook docente;
- checkpoint;
- Activity originali;
- semantic review;
- coverage map.

Le fonti esterne sono usate come technical authority, pedagogical/coverage reference, legacy candidate source o cross-course/runtime contract; non diventano copie wholesale nel materiale canonico.

---

# 2. Technical / teacher reference boundary

Python documentation resta `technical-reference` per sintassi/semantica corrente.

Riferimenti teacher/licensed includono Think Python, Learning Python, Fluent Python, Python in a Nutshell e Pluralsight.

Regola:

```text
licensed/reference material
→ teacher reference / gap check
→ no wholesale reproduction
```

Stato: **boundary corretto**. Prima del publish finale resta necessaria la normale review di licenza/provenance degli asset effettivamente riusati.

---

# 3. `friedpython` legacy source pack

Policy:

```text
legacy exercise/example
→ audit individuale
→ outcome preciso
→ riscrittura/modernizzazione
→ Python 3.12
→ test/casi limite
→ starter/solution separation
→ provenance
```

Audit canonici correnti:

```text
SOURCE_CATALOG.md
FRIEDPYTHON_MAPPING.md
FRIEDPYTHON_LISTS_TUPLES_AUDIT.md
FRIEDPYTHON_DICTS_AUDIT.md
FRIEDPYTHON_FILES_AUDIT.md
```

## Finding P1 — RESOLVED structurally

Il precedente drift del package `python-source-audits` è stato corretto in:

```text
content/python/content-pack.json
doc/course_design.json
```

Entrambi dichiarano esattamente i cinque file sopra.

Helper/gate:

```text
scripts/sync_source_audit_manifest.py
```

Il check è incluso anche in:

```text
scripts/run_static_quality.py
```

Stato corretto:

```text
manifest alignment = implemented / structurally verified
real GitHub Actions execution = pending #8 pre-runner blocker
```

Il finding non è più un catalog/provenance drift aperto. Resta separato il final release provenance/license sign-off.

---

# 4. Content item provenance M04–M30

Il Content Pack ora materializza esattamente M04–M30.

`tests/course_authoring_catalog.py` protegge per ogni modulo:

- lesson canonica presente;
- source `python-course-content` coerente;
- Course Design visibility;
- `content-origin` verso la lesson;
- lesson/deck/runbook/navigation;
- Activity ids coerenti;
- no reserved asset link nello student surface;
- esatta sequenza M04–M30;
- esatto mapping UDA → content item.

Il Content Pack e il Course Design espongono la stessa source list M04–M30.

Una validazione sintetica del nuovo contratto ha prodotto PASS; la suite completa sul checkout reale non è ancora stata eseguita da Actions perché `#8` impedisce l'avvio del runner.

---

# 5. Cross-course sources

## Git G1

```text
TheBitPoets/git
```

Ruolo: curriculum trasversale esterno. Python consuma outcome tramite `config/git-g1-consumer.json` e non copia lesson Git.

Stato: **boundary corretto / delivery evidence pending**.

## Romeo

Ruolo: selective applied domain / technical reference. Non sostituisce il syllabus Python e non rende hardware fisico requisito core.

Stato: **mapping presente / runtime certification pending**.

## TheBitLab / 2cornot2c

Ruolo: delivery/runtime/grading contract. P1/P2/P3/P4 non sono fonti pedagogiche da copiare nelle slide studente.

Stato: **boundary corretto / certification pending**.

---

# 6. Slide provenance

Il source Markdown è autorevole.

Gli artifact HTML/PDF/PPTX futuri devono essere tracciabili a:

```text
source path
source commit SHA
renderer/toolchain version
release/build id
```

Vedi `doc/SLIDE_ARTIFACT_PIPELINE.md` e issue `#10`.

---

# 7. Activity provenance

Oggi l'unica nuova Activity Python materializzata è:

```text
py2-activity-b-input-somma-001
```

Le future Activity devono seguire:

```text
curriculum outcome
→ canonical lesson/spec
→ Activity originale
→ eventuali external refs come reference/provenance
```

Non:

```text
esercizio licensed/legacy
→ copia quasi letterale
→ Activity
```

---

# 8. Approval gate provenance

Prima di `1.0.0 / approved` richiedere ancora:

- [x] source-package `python-source-audits` riallineato;
- [x] Content Pack ↔ Course Design source parity materializzata M04–M30;
- [ ] esecuzione reale dei gate sul checkout dopo risoluzione `#8`;
- [ ] tutti i source ref del release candidate verificati;
- [ ] audit individuale di ogni asset legacy effettivamente riusato;
- [ ] nessun licensed source trasformato in student content per copia;
- [ ] slide build manifest con provenance;
- [ ] Activity provenance finale verificata;
- [ ] teacher sign-off;
- [ ] eventuale license review finale del release candidate.

---

# 9. Esito aggiornato

```text
Canonical course material origin       OK / original-course-material
Technical-reference model              OK
Licensed teacher-reference boundary    OK
Git cross-course boundary              OK
Romeo applied boundary                 OK / runtime pending
TheBitLab delivery boundary            OK / certification pending
friedpython reuse policy               OK
friedpython source-audit manifest       ALIGNED
Content Pack/Course Design source       ALIGNED M04–M30
Final executable CI evidence            BLOCKED by #8
Final release provenance sign-off       PENDING
```

Il precedente finding concreto di manifest è stato risolto strutturalmente; non è stata implicata alcuna promozione a `Content Pack 1.0 / approved`.

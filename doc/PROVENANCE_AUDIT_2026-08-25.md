# Python secondo — Provenance Audit 2026-08-25

> Stato: **audit editoriale/provenance**  
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

Le fonti esterne sono usate come:

- technical authority;
- pedagogical/coverage reference;
- legacy candidate source;
- cross-course/runtime contract.

Non devono diventare copie wholesale dentro il materiale canonico.

---

# 2. Technical authority

## Python documentation

Ruolo:

```text
technical-reference
```

Uso corretto:

- sintassi e semantica attuali;
- comportamento built-in/stdlib;
- correzione di affermazioni storiche;
- non come syllabus da riprodurre.

Stato: **OK** come reference model.

---

# 3. Teacher/licensed references

Riferimenti includono:

- Think Python / Pensare in Python;
- Learning Python / Imparare Python;
- Fluent Python;
- Python in a Nutshell;
- Pluralsight catalog.

Regola:

```text
licensed/reference material
→ teacher reference / gap check
→ no wholesale reproduction
```

Stato: **boundary corretto** nei documenti di progetto.

Prima del publish finale resta necessaria una normale review di licenza/provenance dei singoli asset eventualmente importati.

---

# 4. `friedpython` — legacy source pack

Policy corretta:

```text
legacy exercise/example
→ audit individuale
→ outcome preciso
→ riscrittura originale/modernizzazione
→ Python 3.12
→ test/casi limite
→ starter/solution separation
→ provenance
```

Nessun wholesale import.

File audit attualmente presenti includono:

```text
sources/FRIEDPYTHON_MAPPING.md
sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md
sources/FRIEDPYTHON_DICTS_AUDIT.md
sources/FRIEDPYTHON_FILES_AUDIT.md
```

## Finding P1 — source-package manifest drift

Il package `python-source-audits` nel Content Pack/Course Design è nato prima degli audit dict/file e deve essere verificato/aggiornato affinché l'elenco esplicito `files` rappresenti tutti gli audit canonici correnti.

Target manifest:

```text
SOURCE_CATALOG.md
FRIEDPYTHON_MAPPING.md
FRIEDPYTHON_LISTS_TUPLES_AUDIT.md
FRIEDPYTHON_DICTS_AUDIT.md
FRIEDPYTHON_FILES_AUDIT.md
```

Questo è un **catalog/provenance drift**, non un curriculum gap.

Non promuovere `Content Pack 1.0 / approved` finché il manifest non è riallineato e il check source-package è verde.

---

# 5. Source refs dei moduli

Il gate esistente `tests/course_authoring_catalog.py` verifica già per ogni content item materializzato:

- lesson canonica presente;
- source `python-course-content` coerente;
- Course Design visibility;
- `content-origin` source ref verso la lesson;
- Activity ids coerenti;
- no reserved asset link nello student surface.

Il coverage audit aggiunge una seconda vista:

```text
25 frozen outcomes
→ refs alle lesson/spec/checkpoint
```

Stato strutturale: **designed / gate written, runtime execution pending #8**.

---

# 6. Cross-course sources

## Git G1

```text
TheBitPoets/git
```

Ruolo:

```text
external cross-course curriculum
```

Python consuma outcome G1 tramite `config/git-g1-consumer.json`; non copia lesson Git.

Stato: **boundary corretto**.

## Romeo

Ruolo:

```text
selective applied domain / technical reference
```

Non sostituisce il syllabus Python e non rende hardware fisico requisito core.

Stato: **mapping presente / runtime certification pending**.

## TheBitLab / 2cornot2c

Ruolo:

```text
delivery/runtime/grading contract
```

P1/P2/P3/P4 non sono fonti pedagogiche da copiare nelle slide studente.

Stato: **boundary corretto** dopo semantic review; certification pending.

---

# 7. Slide provenance

Il source Markdown è autorevole.

Gli artifact HTML/PDF/PPTX futuri devono essere derivati e tracciabili a:

```text
source path
source commit SHA
renderer/toolchain version
release/build id
```

Vedi `doc/SLIDE_ARTIFACT_PIPELINE.md`.

Non considerare un artifact derivato una nuova fonte editoriale.

---

# 8. Activity provenance

Oggi l'unica nuova Activity Python materializzata è:

```text
py2-activity-b-input-somma-001
```

La sua `source_refs` deve puntare alla lesson canonica e non a materiale licensed copiato.

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

# 9. Approval gate provenance

Prima di `1.0.0 / approved` richiedere:

- [ ] source-package `python-source-audits` riallineato;
- [ ] Content Pack ↔ Course Design source parity;
- [ ] tutti i source ref risolvibili;
- [ ] audit individuale di ogni asset legacy effettivamente riusato;
- [ ] nessun licensed source trasformato in student content per copia;
- [ ] slide build manifest con provenance;
- [ ] Activity provenance verificata;
- [ ] teacher sign-off;
- [ ] eventuale license review finale del release candidate.

---

# 10. Esito

```text
Canonical course material origin       OK / original-course-material
Technical-reference model              OK
Licensed teacher-reference boundary    OK
Git cross-course boundary              OK
Romeo applied boundary                 OK / runtime pending
TheBitLab delivery boundary            OK / certification pending
friedpython reuse policy               OK
friedpython source-audit manifest       DRIFT TO FIX
Final release provenance sign-off       PENDING
```

Il solo finding concreto di manifest emerso in questo audit è il riallineamento degli audit dict/file nel source package. Va chiuso prima della promotion, ma non richiede alcuna modifica agli outcome frozen.
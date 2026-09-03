# Python curriculum — checklist freeze

> **Curriculum architecture: FROZEN 2026-08-24.**  
> Documento canonico: `doc/CURRICULUM_FREEZE_2026_2027.md`.

Questa checklist distingue **curriculum architecture freeze**, **authoring/editorial completion**, **Content Pack approval** e **classroom readiness**.

## A. Curriculum architecture — FROZEN

### Architettura

- [x] Stage → UDA → Modulo definito
- [x] curriculum spirale definito
- [x] track secondo 33 settimane definito
- [x] 3 checkpoint/buffer = 9 ore esplicite
- [x] confine OOP di seconda definito e obbligatorio
- [x] architecture load review completata (`tracks/secondo/ARCHITECTURE_REVIEW.md`)
- [x] decision owner ha approvato esplicitamente il freeze il 2026-08-24
- [x] freeze canonico registrato in `CURRICULUM_FREEZE_2026_2027.md`

### Metodo didattico

- [x] problema → algoritmo → test → codice → debug → refactor
- [x] test case dal primo nucleo
- [x] trace dal flow chart
- [x] funzioni preview precoce + approfondimento PY2-05
- [x] complessità/efficienza intuitiva e contestuale
- [x] confronto soluzioni come competenza obbligatoria
- [x] loop espliciti prima delle comprehension
- [x] `match/case` fuori dal core finché `if/elif/else` non è padroneggiato

### Valutazione

- [x] tassonomia Activity A–F riusata dallo standard TheBitLab
- [x] assessment model definito
- [x] almeno 1 teoria + 1 pratica per quadrimestre pianificate
- [x] confine autograding/manual evidence definito concettualmente P0–P4
- [x] rubrica trasversale definita
- [x] AI policy definita

### Progetto / competenze trasversali

- [x] Romeo = spine selettiva, non curriculum
- [x] mapping Romeo M00–M30 completato (`ROMEO_MAPPING.md`)
- [x] hardware fisico non è requisito core
- [x] fallback capstone non-Romeo definito
- [x] Git = curriculum separato; G1 integrato progressivamente (`GIT_G1_INTEGRATION.md`)
- [x] Git G1 consumer machine-readable creato (`config/git-g1-consumer.json`)
- [x] Container = curriculum separato

### Fonti

- [x] Think/Pensare in Python ruolo definito
- [x] Learning/Imparare Python ruolo definito
- [x] Fluent Python ruolo definito
- [x] Python in a Nutshell ruolo definito
- [x] Pluralsight gap-check iniziale completato
- [x] documentazione ufficiale Python come riferimento tecnico
- [x] snapshot `friedpython` fissato
- [x] inventory/audit tematico stringhe/liste/tuple/dict/file eseguito a livello architetturale
- [ ] audit individuale degli esercizi `friedpython` prima dell'import effettivo

L'ultimo punto non riapre il curriculum congelato; blocca soltanto l'import/publish degli esercizi legacy non ancora revisionati.

---

# B. Authoring / Content Pack — CORE EDITORIAL SURFACE COMPLETE, APPROVAL OPEN

- [x] lesson authoring contract definito
- [x] Activity planning strategy definita
- [x] Content Pack v1 draft creato
- [x] `doc/course_design.json` creato come Course Board workspace
- [x] tutte le SPEC PY2-01…PY2-10 indicizzate
- [x] architecture review / Git mapping / Romeo mapping indicizzati
- [x] first Activity P1 vertical slice materializzata
- [x] lesson canoniche M04–M30 presenti (27/27)
- [x] deck sorgente Marp M04–M30 presenti (27/27)
- [x] runbook docente M04–M30 presenti (27/27)
- [x] Checkpoint A/B/C guide studente presenti (3/3)
- [x] Checkpoint A/B/C runbook docente presenti (3/3)
- [x] student/teacher navigation aggiornata fino al capstone
- [x] Git G1 structural consumer integrato in M14–M16 + Checkpoint A
- [x] static Git consumer gate scritto (`tests/git_g1_consumer_contract.py`)
- [x] scalable authoring catalog gate scritto (`tests/course_authoring_catalog.py`)
- [x] repository-tree QA checkpoint registrato (`doc/QA_CHECKPOINT_2026-08-25.md`)
- [ ] PY2-01 lesson/deck/runbook digitali finali — intenzionalmente sospesi finché Flowchart Lab non è certificato
- [ ] Content Pack/Course Design executable parity gate eseguito su runner corrente
- [ ] slide HTML/PDF/PPTX build + quality gate eseguito per il set annuale
- [ ] teacher semantic review finale UDA-by-UDA
- [ ] provenance/coverage finale
- [ ] Content Pack promosso a `1.0.0 / approved`

La presenza 27/27 di lesson/deck/runbook è **inventory evidence**, non sostituisce l'esecuzione dei test né la review semantica.

---

# C. Git G1 consumer — STRUCTURAL COMPLETE / DELIVERY EVIDENCE OPEN

- [x] source of truth `TheBitPoets/git` definita
- [x] G1 candidate ref dichiarato: `65d8aff8c9a590560c500762d4dc7378a3239bf2`
- [x] provider contract dichiarato: `doc/G1_CONSUMER_CONTRACT.md`
- [x] M14–M16 → `G1.OBSERVE.STATUS` + `G1.OBSERVE.DIFF`
- [x] Checkpoint A → working tree → index → history
- [x] `g1-stage-selettivo-001` referenziato come canary canonico
- [x] `git.basic.v1` richiesto dal Course Environment
- [x] nessun account GitHub/network richiesto per il core
- [x] Git Lab platform candidate verde su `2cornot2c#761/#762`
- [x] anti-divergence test inserito in workflow
- [ ] consumer test realmente eseguito in CI privata o ambiente equivalente
- [ ] G1 final freeze/decision-owner oppure candidate ref accettato per pilot
- [ ] rehearsal reale nel Classroom Environment

---

# D. Tooling / delivery — blocker prima di `1.0.0 / approved`

- [x] Python baseline scelta: 3.12
- [x] flow chart pedagogical workflow scelto: Flowchart Lab target + manual fallback
- [x] Classroom Environment come unico ambiente supportato
- [x] Course Workspace mutable / Course Bundle immutable boundary definito
- [ ] Course Environment contract implementato/certificato (`python-docente#2`, `2cornot2c#753/#754`)
- [ ] Flowchart Lab implementato/certificato
- [ ] managed VS Code workflow certificato (`python-docente#6`)
- [ ] Course Workspace `Open course` UX/round-trip certificato (`2cornot2c#755`)
- [ ] P1 vertical slice certificato (`python-docente#7`)
- [ ] GitHub Actions pre-execution blocker risolto (`python-docente#8`)
- [ ] P2 function behavior implementato/certificato quando richiesto (`2cornot2c#756`)
- [ ] P4 filesystem behavior implementato/certificato quando richiesto (`2cornot2c#757`)
- [ ] P3 object behavior implementato/certificato quando richiesto (`2cornot2c#758`)
- [ ] `romeo-sim` certificato nei profili Classroom Environment necessari

P2/P3/P4 non bloccano la spiegazione dei rispettivi concetti: bloccano soltanto la promessa di autograding su quel profilo. Activity manual/formative rimangono possibili.

### Evidenza Actions corrente

Su head `0140c5b4917633075853d700f98d35f8a921e0dc`, run `32883608048` / #207:

```text
Ubuntu  failure  steps=null
Windows failure  steps=null
```

Quindi nessun gate del workflow è stato realmente eseguito. `steps=null` non è evidence di pass/fail dei test del corso.

---

# E. Gate

## Curriculum architecture freeze — DONE

Completato il 2026-08-24. Le modifiche successive che cambiano outcome/prerequisiti/order/core devono passare come **curriculum change**.

## Core editorial authoring M04–M30 — DONE / DRAFT

Le superfici canoniche sono presenti e navigabili. Restano QA semantica, artifact build, provenance e delivery evidence.

## Content Pack `1.0.0 / approved` — NOT YET

Richiede inoltre:

- lesson/slide/Activity content revisionato;
- provenance/coverage completa;
- teacher review;
- delivery capability necessarie certificate;
- almeno il vertical slice end-to-end verde;
- PY2-01 delivery coerente con il Flowchart Lab o fallback ufficialmente accettato.

## Ready for classroom / GO pilot — NOT YET

È un gate ancora successivo e richiede rehearsal reale TheBitLab; non deriva automaticamente dal freeze, dalla presenza dei file o dalla CI.

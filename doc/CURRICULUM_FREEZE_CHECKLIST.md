# Python curriculum — checklist freeze

Questa checklist distingue **curriculum architecture freeze** da **Content Pack 1.0 / classroom readiness**.

## A. Curriculum architecture — candidate review

### Architettura

- [x] Stage → UDA → Modulo definito
- [x] curriculum spirale definito
- [x] track secondo 33 settimane definito
- [x] 3 checkpoint/buffer = 9 ore esplicite
- [x] confine OOP di seconda definito e obbligatorio
- [x] architecture load review completata (`tracks/secondo/ARCHITECTURE_REVIEW.md`)
- [ ] decision owner approva esplicitamente `CURRICULUM_FREEZE_CANDIDATE.md`

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

L'ultimo punto **non blocca il freeze della struttura del curriculum**; blocca l'import/publish degli esercizi legacy non ancora revisionati.

---

# B. Authoring / Content Pack

- [x] lesson authoring contract definito
- [x] Activity planning strategy definita
- [x] Content Pack v1 draft creato
- [x] `doc/course_design.json` creato come Course Board workspace
- [x] tutte le SPEC PY2-01…PY2-10 indicizzate
- [x] architecture review / Git mapping / Romeo mapping indicizzati
- [x] first Activity P1 vertical slice materializzata
- [ ] lesson M04 vertical slice prodotta/revisionata
- [ ] slide M04 vertical slice prodotta/revisionata
- [ ] Course Design item reale M04 round-trip testato nella dashboard
- [ ] quality CI del repo stabilizzata

---

# C. Tooling / delivery — blocker prima di `1.0.0 / approved`

- [x] Python baseline scelta: 3.12
- [x] flow chart pedagogical workflow scelto: Flowchart Lab target + manual fallback
- [x] Classroom Environment come unico ambiente supportato
- [x] Course Workspace mutable / Course Bundle immutable boundary definito
- [ ] Course Environment contract implementato/certificato (`python-docente#2`, `2cornot2c#753/#754`)
- [ ] Flowchart Lab implementato/certificato
- [ ] managed VS Code workflow certificato
- [ ] Course Workspace `Open course` UX/round-trip certificato (`2cornot2c#755`)
- [ ] P1 vertical slice certificato (`python-docente#7`)
- [ ] P2 function behavior implementato quando richiesto (`2cornot2c#756`)
- [ ] P4 filesystem behavior implementato quando richiesto (`2cornot2c#757`)
- [ ] P3 object behavior implementato quando richiesto (`2cornot2c#758`)
- [ ] `romeo-sim` certificato nei profili Classroom Environment necessari

P2/P3/P4 non devono bloccare la spiegazione dei rispettivi concetti: bloccano soltanto la promessa di autograding su quel profilo. Activity manual/formative rimangono possibili.

---

# D. Gate

## Curriculum architecture freeze

Può avvenire quando:

- A è completata;
- il decision owner approva esplicitamente il candidate;
- nessun nuovo gap core emerge dalla review.

## Content Pack `1.0.0 / approved`

Richiede inoltre:

- lesson/slide/Activity content revisionato;
- provenance/coverage completa;
- teacher review;
- delivery capability necessarie certificate;
- almeno il vertical slice end-to-end verde.

## Ready for classroom / GO pilot

È un gate ancora successivo e richiede rehearsal reale TheBitLab; non deriva automaticamente dal freeze o dalla CI.

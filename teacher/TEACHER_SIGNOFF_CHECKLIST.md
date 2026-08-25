# Python secondo — Teacher Sign-off Checklist

> Stato iniziale: **PENDING**  
> Questa checklist prepara il sign-off umano finale. Non viene auto-approvata da CI o AI.

## Scopo

Prima di promuovere il Content Pack a `1.0.0 / approved`, il docente/decision owner deve verificare che il corso sia non soltanto coerente nel repository, ma **realmente insegnabile** nel calendario scolastico e corretto per la classe target.

Regola:

```text
static QA + semantic review + build verde
≠
teacher sign-off
```

Il sign-off richiede giudizio didattico umano.

---

# 1. Identità del corso

- [ ] track corretto: `python-secondo-2026-2027`;
- [ ] 33 settimane × 3 ore confermate;
- [ ] 2 ore teoria attiva + 1 ora laboratorio confermate;
- [ ] 3 checkpoint/buffer realmente preservati;
- [ ] OOP settimane 29–32 preservata;
- [ ] settimana 33 non introduce nuovi prerequisiti.

Note docente:

```text
____________________________________________________________
____________________________________________________________
```

---

# 2. Curriculum frozen

Confrontare con:

```text
doc/CURRICULUM_FREEZE_2026_2027.md
```

- [ ] tutti i 25 outcome congelati restano presenti;
- [ ] nessun outcome core è stato trasformato in enrichment;
- [ ] nessun enrichment è diventato implicitamente prerequisito;
- [ ] composizione OOP resta core;
- [ ] Git/Container/Romeo rispettano il boundary frozen;
- [ ] eventuali modifiche post-freeze sono delivery/editorial, non curriculum change nascosto.

---

# 3. Semantic review M04–M30

Indice:

```text
doc/SEMANTIC_REVIEW_INDEX_2026-08-25.md
```

Per ogni UDA verificare che la distinzione sia sensata per la classe reale:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

- [ ] PY2-02/03 — primi programmi + selezione;
- [ ] PY2-04 — iterazione;
- [ ] PY2-05 — funzioni/testing;
- [ ] Checkpoint A;
- [ ] PY2-06/07 — stringhe/liste/tuple;
- [ ] Checkpoint B;
- [ ] PY2-08/09 — set/dict/file;
- [ ] PY2-10 — OOP/capstone;
- [ ] Checkpoint C.

## Regola high-stakes

Una prova ad alto peso può assumere come prerequisito soltanto:

- outcome MUST MASTER già erogati/consolidati;
- outcome GUIDED soltanto se il docente li ha esplicitamente promossi a mastery nella classe reale e ha fornito tempo/evidence sufficiente;
- mai un ENRICHMENT non effettivamente svolto.

- [ ] calendario verifiche controllato con questa regola;
- [ ] domande/esercizi di prova non richiedono accidentalmente dettagli enrichment.

---

# 4. Carico reale settimanale

Per un campione di settimane rappresentative, simulare realmente il ritmo:

```text
retrieval / attivazione
→ nuovo modello
→ prediction/trace
→ guided coding
→ laboratorio
→ exit evidence
```

Campione minimo suggerito:

- [ ] M04 — primo Python;
- [ ] M07 — logica composta;
- [ ] M09 — `while` e terminazione;
- [ ] M11 — stato progressivo;
- [ ] M13 — funzioni formalizzate;
- [ ] M16 — regression/refactor;
- [ ] M18 — string methods senza catalogo;
- [ ] M21 — alias/copia;
- [ ] M25 — scelta modello dati;
- [ ] M26 — file/errori in 3 ore;
- [ ] M28 — invarianti;
- [ ] M29/M30 — composizione/capstone.

Per ogni campione chiedere:

- entra davvero in 2h teoria attiva + 1h lab?;
- il recupero ha spazio?;
- il deck è proiettabile senza leggere tutta la lesson?;
- il laboratorio produce evidence osservabile?;

---

# 5. Assessment model

Verificare `tracks/secondo/ASSESSMENT_CALENDAR.md` e `ASSESSMENT_MODEL.md`.

- [ ] almeno 1 prova teorica/scritta per quadrimestre;
- [ ] almeno 1 prova pratica/pratica-scritta per quadrimestre;
- [ ] formative evidence non viene confusa con voto sommativo automatico;
- [ ] rubriche privilegiano correttezza/comprensione/scelte/test;
- [ ] sintassi/API ricordate a memoria non dominano il voto;
- [ ] Git nel corso Python resta evidence di processo e non seconda prova high-stakes;
- [ ] una difficoltà Git beginner non annulla automaticamente una evidence Python valida;
- [ ] P2/P3/P4 non vengono promessi finché non certificati;
- [ ] nessuna prova dipende da Romeo non certificato o hardware fisico.

---

# 6. Checkpoint A

- [ ] resta settimana Python di consolidamento/recupero;
- [ ] G1 è `embedded-outcome-subset`;
- [ ] non richiede completamento standalone G1;
- [ ] `status/diff` sono già stati introdotti in M14–M16;
- [ ] staging/commit/history sono guidati e contestuali;
- [ ] se il tempo non basta, Git non comprime la prova/recupero Python.

Workflow:

```text
status
→ diff
→ test
→ add
→ diff --staged
→ commit
→ status
→ log/show
```

---

# 7. Checkpoint B

- [ ] misura modello/semantica, non catalogo API;
- [ ] non forza string+list+tuple+matrix nello stesso progetto;
- [ ] alias/copia è compreso prima di nested structures;
- [ ] Git riusa G1 senza nuovi outcome G2;
- [ ] eventuali esercizi `friedpython` sono stati auditati individualmente.

---

# 8. OOP e Checkpoint C

- [ ] classe/istanza e `self` sono comprensibili senza internals prematuri;
- [ ] invarianti sono proprietà del dominio e generano casi di test;
- [ ] una transizione rifiutata lascia lo stato coerente;
- [ ] `return False` non viene insegnato come unica policy OOP;
- [ ] composizione viene insegnata e dimostrata;
- [ ] capstone completo contiene composizione reale;
- [ ] nel recovery si riduce il dominio, non gli outcome frozen;
- [ ] persistenza file resta opzionale nel capstone;
- [ ] M29/week31 → skeleton, M30/week32 → integration/review, week33 → finalizzazione/recupero.

---

# 9. Coverage / provenance

Verificare:

```text
doc/COVERAGE.md
config/curriculum-coverage.json
sources/SOURCE_CATALOG.md
```

- [ ] 25/25 outcome mappati;
- [ ] PY2-01 segnalato correttamente come SPEC/final delivery pending;
- [ ] una sola Activity Python automatica dichiarata oggi: M04 canary;
- [ ] nessuna percentuale unica confonde editorial/activity/readiness;
- [ ] source refs delle lesson sono plausibili;
- [ ] materiale licensed è teacher-reference only;
- [ ] `friedpython` non viene importato wholesale;
- [ ] Git/Romeo/TheBitLab hanno ruoli distinti dalla provenance Python canonica.

---

# 10. Slide / visual delivery

Verificare:

```text
doc/SLIDE_ARTIFACT_PIPELINE.md
tests/slide_source_quality.py
```

- [ ] 27/27 source deck M04–M30;
- [ ] nessun leak teacher/P2/P3/P4 interno nei deck studente;
- [ ] renderer/toolchain pinning definito prima della release;
- [ ] build HTML reale;
- [ ] build PDF reale;
- [ ] build PPTX reale;
- [ ] artifact structural QA;
- [ ] visual sample review almeno M04/M11/M18/M22/M26/M30;
- [ ] eventuali problemi sistemici corretti nei source deck.

Non spuntare le build finché i file non sono stati realmente generati e aperti/verificati.

---

# 11. TheBitLab / Classroom Environment

- [ ] `python-docente#2` chiuso o pilot-boundary esplicitamente accettato;
- [ ] beginner REPL/editor workflow certificato;
- [ ] PY2-01 Flowchart Lab/fallback delivery resa veritiera;
- [ ] M04/P1 canary realmente eseguito;
- [ ] student scaffold senza asset riservati;
- [ ] Course Workspace open/save/reopen provato;
- [ ] Git G1 consumer provato nel workspace;
- [ ] P2/P3/P4 usati solo dove certificati;
- [ ] `romeo-sim` usato come obbligatorio solo se certificato;
- [ ] rehearsal su profilo studente reale.

---

# 12. Inclusione e recupero

Per i moduli ad alto carico verificare che il runbook contenga una via di recupero reale:

- [ ] trace più piccoli;
- [ ] una sola variabile/concetto per volta;
- [ ] starter controllati;
- [ ] output/casi ridotti;
- [ ] dominio ridotto senza cancellare l'outcome;
- [ ] enrichment separato dal recupero;
- [ ] nessun tool esterno non gestito come prerequisito implicito.

Il recupero deve ridurre **complessità accidentale**, non abbassare silenziosamente il curriculum core.

---

# 13. Teacher visual/content spot-check

Aprire almeno una lesson + deck + runbook per ogni UDA e verificare:

- [ ] terminologia coerente;
- [ ] italiano naturale per studenti;
- [ ] esempi leggibili;
- [ ] niente contraddizioni lesson/deck/runbook;
- [ ] codice eseguibile/coerente a vista;
- [ ] nessuna affermazione tecnica dubbia;
- [ ] nessun riferimento storico/legacy presentato come comportamento corrente.

---

# 14. Decisione finale

Compilare soltanto dopo i gate precedenti.

```text
Teacher reviewer: ______________________________
Date: _________________________________________
Reviewed commit / release candidate: __________

[ ] APPROVE for Content Pack promotion
[ ] APPROVE for limited pilot only
[ ] CHANGES REQUIRED

Blocking notes:
____________________________________________________________
____________________________________________________________
____________________________________________________________
```

## Importante

`APPROVE for Content Pack promotion` non equivale automaticamente a `GO classroom`.

Il GO richiede anche il rehearsal reale del Classroom Environment/TheBitLab sul release candidate approvato.
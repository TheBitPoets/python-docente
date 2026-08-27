# PY2-01 — Semantic review 2026-08-27

> Scope: M00–M03 + delivery boundary Flowchart Lab/fallback.  
> Stato: **semantic review complete / editorial draft**.  
> **Nessun curriculum change** rispetto al freeze: questa review materializza e protegge la pedagogia già approvata; non certifica il Classroom Environment e non sostituisce il teacher sign-off.

## Riferimenti canonici

- `tracks/secondo/PY2_01_SPEC.md`;
- `tracks/secondo/MODULE_MAP.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `config/course-environment.json`;
- `config/flowchart-lab-candidate.json`;
- candidate consumer `tests/py2_01_flowchart_candidate.py`.

---

# Decisione di pacing

Il freeze assegna a PY2-01 **3 settimane / 9 ore**.

La materializzazione è:

```text
settimana 1
  M00 orientamento/metodo ~45–60 min
  M01 specifica → pseudocodice → trace → test

settimana 2
  M02 flow chart: sequenza + selezione

settimana 3
  M03 flow chart: iterazione + terminazione + primo annidamento
```

M00 non crea una quarta settimana e non viene modellato come nuova UDA nel Course Design: è un modulo di orientamento integrato in `py2-01`.

Finding: **PASS** — il carico resta dentro 9 ore e protegge l'avvio da zero assoluto.

---

# M00 — Problema, algoritmo, programma, input/output

## MUST MASTER

- problema ≠ algoritmo ≠ programma;
- input/output/vincoli;
- informazioni necessarie, inutili e mancanti;
- procedura finita a passi;
- più casi di test, incluso almeno un confine/alternativa;
- distinzione intuitiva tra errore di comprensione, algoritmo ed esecuzione.

## GUIDED EXPOSURE

- controesempio come strumento di verifica;
- debug come ricerca del primo punto in cui il modello diverge.

## ENRICHMENT / BACKUP

- classificazioni formali degli algoritmi;
- definizioni teoriche più rigorose di correttezza/terminazione.

Finding: **PASS** — nessun Python, Flowchart Lab o Romeo come prerequisito. M00 resta diagnostico/metodologico e non diventa un'unità teorica autonoma.

---

# M01 — Specifica, pseudocodice e trace

## MUST MASTER

- estrazione di input/output/vincoli;
- decomposizione in passi controllabili;
- pseudocodice leggibile e language-neutral;
- trace con stato prima/dopo;
- caso non coperto;
- ragione della terminazione;
- test progettati prima del programma.

## GUIDED EXPOSURE

- notazione `←` per assegnamento concettuale;
- modifica minima durante il debug;
- un piccolo blocco Python mostrato **solo come anti-esempio esplicito** di “Python travestito”.

## ENRICHMENT / BACKUP

- formalismi di specifica/pre/postcondizioni;
- sintassi Python completa.

Finding: **PASS** — l'anti-esempio Python non introduce mastery di sintassi e il gate statico lo consente soltanto se chiaramente marcato come negativo.

---

# M02 — Sequenza e selezione nei flow chart

## MUST MASTER

- simboli core: start/end, input/output, processing, decision, freccia;
- sequenza;
- selezione true/false;
- trace del percorso;
- caso sul confine;
- distinzione `schema valido != algoritmo corretto`;
- fallback manuale equivalente se il tool non è disponibile.

## GUIDED EXPOSURE

- tre casi tramite composizione di decisioni;
- Flowchart Lab: Run/Step/Reset, variable watch, artifact `algorithm.flow.json`;
- structural/behavioral checks deterministici.

## ENRICHMENT / BACKUP

- simboli flow-chart avanzati;
- formati proprietari;
- scoring automatico della qualità del diagramma.

Finding: **PASS** — il tool è una superficie di delivery, non il curriculum. La lesson esplicita che qualità, chiarezza e scelta dei costrutti restano rubric/manual evidence.

---

# M03 — Iterazione, terminazione e annidamento

## MUST MASTER

Per ogni ciclo lo studente deve poter identificare:

```text
inizializzazione
condizione
corpo
aggiornamento
ragione della terminazione
```

Inoltre:

- trace di contatore/accumulatore;
- off-by-one intuitivo;
- selezione dentro ciclo e ciclo dentro selezione;
- primo annidamento riga/colonna;
- diagnosi di aggiornamento mancante/errato;
- spiegazione della terminazione.

## GUIDED EXPOSURE

- accumulatore come stato progressivo “finora”;
- `limit-exceeded` come evidence di mancata conclusione entro il budget, non diagnosi automatica;
- costo intuitivo di una griglia.

## ENRICHMENT / BACKUP

- Big-O formale;
- loop idiomatici Python;
- `break`/`continue`;
- simulatori robotici/API Romeo obbligatorie.

Finding: **PASS** — il modulo introduce l'idea di lavoro ripetuto senza trasformarla in analisi asintotica e usa Romeo solo come possibile scenario motivante.

---

# Flowchart Lab delivery boundary

Candidate pinned lato corso:

```text
config/flowchart-lab-candidate.json
status = candidate-not-certified
```

Real consumer evidence ha già verificato su Ubuntu e Windows:

- built-in runtime probe/registry;
- loopback launch;
- browser UI;
- managed `algorithm.flow.json` save/load;
- deterministic Run;
- Session/Step + variable watch;
- SVG evidence;
- `authoritative_grading=false`.

Il corso mantiene comunque:

```text
flowchart.manual-evidence.v1
```

come fallback obbligatorio finché non sono completati supported-profile rehearsal e human usability review.

Finding: **PASS WITH DELIVERY LIMITATION** — la boundary è sufficientemente definita per materializzare le lesson, ma non per dichiarare `flowchart.lab.v1` classroom-certified.

---

# Anti-autograding boundary

La review conferma:

```text
validazione schema
+ trace deterministico
+ output deterministico
!=
voto automatico sulla qualità algoritmica
```

Restano manual/rubric almeno:

- qualità della decomposizione;
- chiarezza;
- scelta appropriata della struttura;
- annidamento non necessario;
- spiegazione della terminazione e delle scelte.

Non materializzare una Flowchart Activity con grading autorevole prima della certificazione esplicita di un profilo adatto.

---

# Handoff M03 → M04

Il passaggio corretto è:

```text
algoritmo già compreso
→ stessa procedura espressa in Python
```

Non:

```text
impara sintassi Python
→ spera di capire il problema dopo
```

M04 può quindi iniziare da input/output/somma/trace già concettualmente noti.

Finding: **PASS** — la progressione riduce il carico cognitivo all'ingresso nel linguaggio.

---

# Review outcome

```text
M00 reviewed
M01 reviewed
M02 reviewed
M03 reviewed
pacing 9h protected
pre-Python boundary protected
manual fallback protected
Flowchart candidate boundary explicit
authoritative diagram grading forbidden
M03→M04 bridge coherent
```

## Cosa NON significa

Non significa:

- Flowchart Lab classroom-certified;
- teacher sign-off;
- Activities PY2-01 complete;
- slide release artifacts M00–M03 built/reviewed;
- Content Pack approved;
- GO classroom.

La semantic review può essere considerata completa; i gate rimanenti sono delivery/release/human evidence, non un motivo per reintrodurre PY2-01 come SPEC-only.

# Python — guida docente

> Stato: **curriculum FROZEN 2026/27 / produzione editoriale controllata**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

Questo indice è il punto di ingresso del docente per progettazione, conduzione e delivery.

## Architettura del corso

Documenti da leggere nell'ordine:

1. [`doc/CURRICULUM_FREEZE_2026_2027.md`](../doc/CURRICULUM_FREEZE_2026_2027.md) — baseline curricolare congelata e change-control.
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md) — audit delle 33 settimane e del carico.
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md) — struttura di seconda.
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md) — quattro prove principali e checkpoint.
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md) — profili P0/P1/P2/P3/P4 e boundary del grading.
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md) — round-trip Course Workspace ↔ dashboard ↔ Git.

Il precedente `CURRICULUM_FREEZE_CANDIDATE.md` resta traccia della fase di review; `CURRICULUM_FREEZE_2026_2027.md` è il documento autorevole.

## Moduli editoriali materializzati

### M04 — Interprete, REPL, script, valori e input/output

Materiali canonici:

- lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md);
- slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md);
- runbook: [`teacher/M04_RUNBOOK.md`](M04_RUNBOOK.md);
- Activity: `py2-activity-b-input-somma-001`;
- gate tecnico: `python-docente#7`;
- blocker CI pre-esecuzione: `python-docente#8`.

M04 resta il **golden vertical slice tecnico**: è l'unico modulo che per ora materializza anche una nuova Activity P1 da certificare end-to-end.

### M05 — Espressioni, operatori e prime funzioni

Materiali canonici:

- lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md);
- slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md);
- runbook: [`teacher/M05_RUNBOOK.md`](M05_RUNBOOK.md).

M05 è una **continuazione editoriale controllata**, non un secondo canarino P1. Contiene esercizi e Activity candidate A–E, ma non aggiunge una nuova Activity autogradata finché M04/#7 non ha evidenza.

Focus M05:

```text
problema
→ espressione
→ / // %
→ precedenza leggibile
→ valore/tipo
→ f-string/built-in essenziali
→ prima funzione pura
→ return vs print (preview)
```

La progettazione formale delle funzioni resta PY2-05.

## Change-control curricolare

Dopo il freeze non riaprire la struttura annuale per normali modifiche editoriali.

Richiedono una **curriculum change** soltanto modifiche a outcome obbligatori, prerequisiti core, ordine necessario delle UDA, monte ore core sostanziale, OOP obbligatoria o ruolo curricolare di Git/Container/Romeo.

Lesson, slide, Activity, rubric, tooling, runner e UX sono **delivery changes** se rispettano il freeze.

## Regola di delivery

Il repository del corso è il **Course Workspace mutabile**. La Course Board deve aprire questo workspace tramite il boundary TheBitLab previsto; Git conserva storia e review. Il Course Bundle futuro è una release immutabile, non un secondo source of truth.

Non modificare direttamente una release pubblicata come se fosse il progetto autore.

## Regola Course Board

Le lesson canoniche vengono dichiarate come `sources` nel `doc/course_design.json` / Content Pack.

### Due granularità intenzionalmente diverse

```text
Content Pack
  modulo = file/lesson canonica

Course Board
  item = heading + relativo sottoalbero
```

Questa differenza è intenzionale:

- il Content Pack conserva l'identità editoriale del modulo;
- la Course Board permette al docente di includere, spostare, omettere o riordinare sezioni della fonte dentro le UDA;
- ogni item della board mantiene ID heading, path, riga, digest e provenienza dello snapshot.

Una lesson può avere più H1. In quel caso il modulo completo corrisponde a tutti gli H1 top-level del file, ciascuno con il proprio sottoalbero. Non creare un secondo oggetto `module` dentro il Course Design solo per raggrupparli.

La UX futura `Aggiungi intero modulo/file alla UDA` è tracciata in `2cornot2c#755`: deve equivalere all'aggiunta atomica di tutti gli H1 del file in ordine, senza cambiare il modello dati.

### Inserimento dalla dashboard

1. aprire il workspace `python-docente` nella Course Board;
2. sincronizzare le fonti;
3. selezionare/trascinare gli heading desiderati nella UDA oppure, quando disponibile, usare l'azione bulk dell'intero modulo;
4. lasciare che la board registri ID heading, line, digest e provenienza dello snapshot;
5. salvare il Course Design;
6. verificare il diff Git e riaprire il progetto.

Non fabbricare manualmente item parziali se la dashboard può generare i sottoalberi dagli heading verificati.

Per M04 esiste `tests/course_board_workspace_roundtrip.py`, che esercita server-side il boundary external workspace → tutti gli H1 M04 → PY2-02 → save → reopen. Il rehearsal browser/UX reale resta un gate separato.

## Ambiente studente

Tutti i corsi devono usare il **Classroom Environment TheBitLab**. Per Python seconda:

- baseline didattica iniziale: Python 3.12;
- REPL standard prima di VS Code;
- VS Code solo come capability gestita dalla piattaforma;
- Flowchart Lab target cross-platform;
- Romeo resta runtime/plugin esterno `romeo-sim`;
- grading autorevole separato dall'ambiente interattivo.

Blocker piattaforma principali:

- `2cornot2c#753` — Classroom Environment + Flowchart Lab;
- `2cornot2c#755` — Open course / workspace authoring UX + bulk module add;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior.

## CI del vertical slice

Il workflow prova, nell'ordine:

1. QA statico M04;
2. Course Board external-workspace round-trip;
3. Activity/Content Pack/scaffold/grading consumer smoke.

`python-docente#8` ha ormai escluso un errore del workflow: persino un job diagnostico con un solo `echo` e nessuna action esterna fallisce pre-step su Ubuntu/Windows. Un private repo dell'organizzazione (`tpsi-quarto-docente`) aveva CI verde il 19 agosto e lo stesso failure dal 21: il candidato principale è quota/budget Actions dei repository privati; la verifica amministrativa resta Billing/Actions settings dell'organizzazione.

Non interpretare `steps: null` come PASS/FAIL del contenuto.

## Git e Container

Git e Container non vengono duplicati dentro Python.

- Git G1 viene introdotto progressivamente nel track Python e poi rimanda al futuro corso Git autonomo.
- Il futuro corso Container/Docker resta separato e parte dal backlog `kinderp/docker101#1`.

Le dispense Git verranno richieste quando inizierà la produzione del curriculum Git o del micro-modulo G1 definitivo.

## Criterio per continuare la produzione

Il curriculum è congelato. Possiamo produrre **in modo controllato** un modulo alla volta, mantenendo M04 come golden vertical slice tecnico; non dobbiamo però materializzare in serie nuove Activity autogradate prima dell'evidenza P1.

```text
lesson
+ slide
+ runbook
+ eventuale Activity solo se il profilo è certificato
+ Course Board source
+ student path
+ QA
```

Un contenuto presente nel repository non equivale automaticamente a contenuto certificato per la classe.

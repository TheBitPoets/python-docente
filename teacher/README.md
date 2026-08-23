# Python — guida docente

> Stato: **curriculum freeze candidate / vertical slice draft**. Non dichiarare il corso pronto per studenti finché i gate di delivery non sono chiusi.

Questo indice è il punto di ingresso del docente per progettazione, conduzione e delivery.

## Architettura del corso

Documenti da leggere nell'ordine:

1. [`doc/CURRICULUM_FREEZE_CANDIDATE.md`](../doc/CURRICULUM_FREEZE_CANDIDATE.md) — cosa proponiamo di congelare a livello curricolare.
2. [`tracks/secondo/ARCHITECTURE_REVIEW.md`](../tracks/secondo/ARCHITECTURE_REVIEW.md) — audit delle 33 settimane e del carico.
3. [`tracks/secondo/COURSE_DESIGN.md`](../tracks/secondo/COURSE_DESIGN.md) e [`MODULE_MAP.md`](../tracks/secondo/MODULE_MAP.md) — struttura di seconda.
4. [`tracks/secondo/ASSESSMENT_CALENDAR.md`](../tracks/secondo/ASSESSMENT_CALENDAR.md) — quattro prove principali e checkpoint.
5. [`doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`](../doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md) — profili P0/P1/P2/P3/P4 e boundary del grading.
6. [`doc/THEBITLAB_AUTHORING_COMPATIBILITY.md`](../doc/THEBITLAB_AUTHORING_COMPATIBILITY.md) — round-trip Course Workspace ↔ dashboard ↔ Git.

## Vertical slice M04

Materiali canonici:

- lesson studente: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md);
- slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md);
- runbook docente: [`teacher/M04_RUNBOOK.md`](M04_RUNBOOK.md);
- Activity: `py2-activity-b-input-somma-001`;
- gate tecnico: `python-docente#7`;
- blocker CI pre-esecuzione: `python-docente#8`.

Il runbook M04 contiene ritmo 2 ore teoria attiva + 1 laboratorio, misconception, remediation, enrichment, evidence e fallback se il grading P1 non è certificato.

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

La UX futura `Aggiungi intero modulo/file alla UDA` è tracciata come miglioramento di `2cornot2c#755`: deve equivalere all'aggiunta atomica di tutti gli H1 del file in ordine, senza cambiare il modello dati.

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

1. QA statico M04 (`tests/m04_vertical_slice_static.py`);
2. Course Board external-workspace round-trip;
3. Activity/Content Pack/scaffold/grading consumer smoke.

Al momento i GitHub-hosted job osservati falliscono prima di eseguire qualsiasi step (`steps: null`); questo è tracciato in `python-docente#8`. Non interpretarlo come PASS/FAIL del contenuto o dei test.

## Git e Container

Git e Container non vengono duplicati dentro Python.

- Git G1 viene introdotto progressivamente nel track Python e poi rimanda al futuro corso Git autonomo.
- Il futuro corso Container/Docker resta separato e parte dal backlog `kinderp/docker101#1`.

Le dispense Git del docente verranno richieste quando inizierà la produzione del curriculum Git o del micro-modulo G1 definitivo.

## Criterio per continuare la produzione

Prima di produrre in serie M05, M06... bisogna usare M04 per verificare il modello completo:

```text
lesson
+ slide
+ runbook
+ Activity
+ scaffold
+ grading
+ Course Board
+ student path
+ QA
```

Un contenuto presente nel repository non equivale automaticamente a contenuto certificato per la classe.

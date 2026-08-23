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
- gate tecnico: `python-docente#7`.

Il runbook M04 contiene ritmo 2 ore teoria attiva + 1 laboratorio, misconception, remediation, enrichment, evidence e fallback se il grading P1 non è certificato.

## Regola di delivery

Il repository del corso è il **Course Workspace mutabile**. La Course Board deve aprire questo workspace tramite il boundary TheBitLab previsto; Git conserva storia e review. Il Course Bundle futuro è una release immutabile, non un secondo source of truth.

Non modificare direttamente una release pubblicata come se fosse il progetto autore.

## Regola Course Board

Le lesson canoniche vengono dichiarate come `sources` nel `doc/course_design.json` / Content Pack.

Per inserire una lesson nell'UDA dalla dashboard:

1. aprire il workspace `python-docente` nella Course Board;
2. sincronizzare le fonti;
3. selezionare/trascinare l'heading canonico della lesson nell'UDA;
4. lasciare che la board registri ID heading, line, digest e provenienza dello snapshot;
5. salvare il Course Design;
6. verificare il diff Git e riaprire il progetto.

Non fabbricare manualmente un item parziale se la dashboard può generare il sottoalbero completo degli heading.

Per M04 questo round-trip è ancora un gate aperto: la lesson è indicizzata, ma l'inserimento/salvataggio/reopen reale della UDA deve essere collaudato nel flusso dashboard.

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
- `2cornot2c#755` — Open course / workspace authoring UX;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior.

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

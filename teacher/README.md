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

- lesson: [`content/python/04_INTERPRETE_REPL_VALORI_IO.md`](../content/python/04_INTERPRETE_REPL_VALORI_IO.md);
- slide: [`slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`](../slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md);
- runbook: [`teacher/M04_RUNBOOK.md`](M04_RUNBOOK.md);
- Activity canarino: `py2-activity-b-input-somma-001`;
- gate tecnico: `python-docente#7`;
- blocker CI: `python-docente#8`.

M04 resta il **golden vertical slice tecnico**.

### M05 — Espressioni, operatori e prime funzioni

- lesson: [`content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md);
- slide: [`slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`](../slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md);
- runbook: [`teacher/M05_RUNBOOK.md`](M05_RUNBOOK.md).

Focus: espressioni, `/ // %`, precedenza, f-string/built-in essenziali, prima funzione pura e preview `return` vs `print`. Nessuna nuova Activity P1 materializzata prima della certificazione M04.

### M06 — Booleani, confronti e prima selezione con `if`

- lesson: [`content/python/06_BOOLEANI_CONFRONTI_IF.md`](../content/python/06_BOOLEANI_CONFRONTI_IF.md);
- slide: [`slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`](../slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md);
- runbook: [`teacher/M06_RUNBOOK.md`](M06_RUNBOOK.md).

Focus:

```text
linguaggio naturale della soglia
→ confronto
→ bool
→ if / if-else
→ indentazione
→ trace del ramo
→ test sotto/sulla/sopra il confine
```

M06 introduce Romeo soltanto come **applicazione opzionale** dopo esempi generali, tramite la missione pinned `romeo-y1-u14-condizioni` e solo quando `romeo-sim` è certificato. Non dichiara nuove Activity P1 obbligatorie.

## Change-control curricolare

Dopo il freeze non riaprire la struttura annuale per normali modifiche editoriali. Richiedono una curriculum change solo modifiche a outcome obbligatori, prerequisiti core, ordine necessario delle UDA, monte ore core sostanziale, OOP obbligatoria o ruolo curricolare di Git/Container/Romeo.

Lesson, slide, Activity, rubric, tooling, runner e UX sono delivery changes se rispettano il freeze.

## Regola di delivery

Il repository del corso è il **Course Workspace mutabile**. La Course Board deve aprire questo workspace tramite il boundary TheBitLab previsto; Git conserva storia e review. Il Course Bundle futuro è una release immutabile, non un secondo source of truth.

## Regola Course Board

```text
Content Pack: modulo = file/lesson canonica
Course Board: item = heading + relativo sottoalbero
```

La differenza è intenzionale: il Content Pack conserva l'identità editoriale, mentre la Course Board permette al docente di includere/spostare/omettere/riordinare sezioni. L'UX futura `Aggiungi intero modulo/file alla UDA` resta tracciata in `2cornot2c#755`.

Non fabbricare manualmente item parziali se la dashboard può generare i sottoalberi dagli heading verificati.

Per M04 esiste `tests/course_board_workspace_roundtrip.py`; il rehearsal browser/UX reale resta un gate separato.

## Ambiente studente

Tutti i corsi usano il **Classroom Environment TheBitLab**. Per Python seconda:

- baseline didattica iniziale Python 3.12-compatible;
- REPL standard prima di VS Code;
- VS Code soltanto come capability gestita;
- Flowchart Lab target cross-platform;
- Romeo = runtime/plugin esterno `romeo-sim`;
- grading autorevole separato dall'ambiente interattivo.

Blocker principali:

- `2cornot2c#753` — Classroom Environment + Flowchart Lab;
- `2cornot2c#755` — Open course/workspace UX + bulk module add;
- `2cornot2c#756` — P2 function behavior;
- `2cornot2c#757` — P4 filesystem behavior;
- `2cornot2c#758` — P3 object behavior.

## QA authoring

`tests/course_authoring_catalog.py` controlla in modo scalabile tutti i moduli materializzati: lesson, Marp deck, runbook, navigazione, provenance, Course Board source e Activity dichiarate.

M04 conserva in aggiunta i gate canarino specifici; M05 ha il proprio controllo pedagogico statico. M06 viene coperto dal catalogo generico e dai review criteria del runbook/lesson.

## CI del vertical slice

`python-docente#8` ha escluso un errore dello YAML: persino un job diagnostico con un solo `echo` e nessuna action esterna fallisce pre-step su Ubuntu/Windows. Il private repo TPSI4 aveva CI verde il 19 agosto e lo stesso problema dal 21; quota/budget Actions dei repository privati è l'ipotesi principale, da verificare nelle impostazioni Billing/Actions dell'organizzazione.

Non interpretare `steps: null` come PASS/FAIL del contenuto.

## Git e Container

Git e Container non vengono duplicati dentro Python. Git G1 entra progressivamente nel track; Container/Docker resta corso separato. Le dispense Git verranno richieste quando inizierà la produzione G1 definitiva o il corso Git autonomo.

## Criterio per continuare la produzione

Possiamo produrre **un modulo editoriale alla volta** mantenendo M04 come golden vertical slice tecnico, ma non materializziamo in serie nuove Activity autogradate prima dell'evidenza P1.

```text
lesson
+ slide
+ runbook
+ eventuale Activity solo se il profilo è certificato
+ Course Board source
+ student path
+ QA
```

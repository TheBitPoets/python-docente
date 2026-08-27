# Python secondo — Semantic Review Index

> Stato: **core M00–M30 revisionato semanticamente / editorial draft**.  
> Review M04–M30 completate il 2026-08-25; PY2-01 M00–M03 completata il 2026-08-27 dopo la definizione/consumer evidence del Flowchart Lab candidate.  
> Questo indice non equivale a teacher sign-off, runtime certification, Content Pack approval o classroom readiness.

## Scope completo

```text
PY2-01
  doc/SEMANTIC_REVIEW_PY2_01_2026-08-27.md

PY2-02 / PY2-03
  doc/SEMANTIC_REVIEW_PY2_02_PY2_03_2026-08-25.md

PY2-04
  doc/SEMANTIC_REVIEW_PY2_04_2026-08-25.md

PY2-05 + Checkpoint A
  doc/SEMANTIC_REVIEW_PY2_05_CHECKPOINT_A_2026-08-25.md

PY2-06 + PY2-07 + Checkpoint B
  doc/SEMANTIC_REVIEW_PY2_06_PY2_07_CHECKPOINT_B_2026-08-25.md

PY2-08 + PY2-09
  doc/SEMANTIC_REVIEW_PY2_08_PY2_09_2026-08-25.md

PY2-10 + Checkpoint C
  doc/SEMANTIC_REVIEW_PY2_10_CHECKPOINT_C_2026-08-25.md
```

PY2-01 non è più SPEC-only: M00–M03 sono materializzati come draft. Il Flowchart Lab resta `candidate-not-certified` e il fallback manuale resta obbligatorio finché non sono completati supported-profile rehearsal e human usability review.

---

# Regola didattica comune

Per ogni modulo il runbook deve distinguere, quando utile:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

Scopo:

- impedire che tutto ciò che compare nella lesson diventi automaticamente materia di verifica;
- proteggere il tempo reale 2h teoria attiva + 1h lab;
- mantenere materiale ricco per differenziazione senza sovraccaricare il core;
- rendere espliciti i prerequisiti per il modulo successivo.

---

# Finding trasversali consolidati

## F0 — Algoritmo prima del linguaggio

PY2-01 protegge la progressione:

```text
problema → pseudocodice → flow chart → trace → test → debug → Python
```

M00/M01 condividono la prima settimana; M02 e M03 completano le 9 ore frozen. Flowchart Lab è delivery, non prerequisito concettuale, e il fallback manuale preserva gli stessi outcome.

## F1 — API ≠ curriculum

String/list/set/dict non vengono insegnati come cataloghi di metodi.

```text
specifica / operazione dominante
→ modello
→ algoritmo/API
```

## F2 — Stato progressivo prima delle ricette

Contatore, accumulatore, min/max, ricerca e flag vengono ricondotti a:

> che cosa deve significare questa variabile dopo i dati già elaborati?

La stessa idea nasce già nel trace di PY2-01.

## F3 — Dettagli di controllo non diventano falsi prerequisiti

`while True`, `break`, `continue`, short-circuit, De Morgan e Big-O restano guided/enrichment dove appropriato. In M03 il costo di una griglia resta solo intuitivo.

## F4 — Funzioni formalizzano una preview già fatta

M13 non ripete M05 da zero e Git non inizia prima di M14.

## F5 — Git G1 è embedded outcome subset

```text
full G1 track completion required = false
full canonical lesson completion required = false
```

Python usa Git come processo; non assorbe il corso Git standalone e non aggiunge una seconda verifica Git high-stakes.

## F6 — P2/P3/P4 e Flowchart sono delivery boundary

I profili di grading/runtime non sono mastery studente. Il corso insegna gli outcome anche con manual/assert evidence finché il relativo profilo non è certificato. Flowchart Lab oggi dichiara esplicitamente `authoritative_grading=false`.

## F7 — Composizione OOP è core

Checkpoint C non può rendere la composizione facoltativa nel capstone completo. Nel recovery si può ridurre il dominio, ma l'evidence dell'outcome deve comunque esistere.

## F8 — M26 protegge OOP

File/error handling resta un boundary di 3 ore:

```text
Path relativo
→ UTF-8
→ read/write
→ with
→ I/O separato
→ FileNotFoundError mirato
```

Niente espansione a CSV/JSON/binario/eccezioni avanzate nel core.

## F9 — Capstone piccolo ma completo

Il capstone misura:

```text
responsabilità
+ invariante
+ composizione
+ scelta struttura dati
+ test/edge
+ regression/refactor
+ spiegazione
```

Non numero di classi, righe, framework o feature.

---

# Review coverage

```text
M00–M03    reviewed
M04–M08    reviewed
M09–M12    reviewed
M13–M16    reviewed
Checkpoint A reviewed
M17–M22    reviewed
Checkpoint B reviewed
M23–M26    reviewed
M27–M30    reviewed
Checkpoint C reviewed
```

Quindi il **core editorialmente materializzato M00–M30 ha una review semantica completa**.

---

# Cosa NON significa

Non significa:

- lesson approved;
- teacher sign-off finale;
- Activities complete;
- P1/P2/P3/P4 certified per tutti i profili classroom;
- Flowchart Lab classroom-certified;
- `romeo-sim` certified;
- nuovo release build slide M00–M30 completato;
- Content Pack `1.0.0 / approved`;
- GO classroom.

---

# Layer successivi

Ordine corrente:

1. mantenere static QA M00–M30 verde;
2. nuovo real slide build M00–M30 + visual/PowerPoint review;
3. supported-profile Classroom Environment / Flowchart rehearsal;
4. teacher review finale;
5. P2/P3/P4 e `romeo-sim` certification quando richiesti dalle Activity;
6. Activity materialization progressiva con profilo corretto;
7. provenance/license review finale;
8. Content Pack approval;
9. GO classroom.

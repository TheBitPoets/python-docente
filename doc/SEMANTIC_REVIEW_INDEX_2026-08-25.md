# Python secondo — Semantic Review Index 2026-08-25

> Stato: **core M04–M30 revisionato semanticamente / editorial draft**.  
> Questo indice non equivale a teacher sign-off, runtime certification, Content Pack approval o classroom readiness.

## Scope completo

```text
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

PY2-01 resta volutamente fuori dalla review delle lesson finali perché è ancora SPEC-only in attesa del boundary Flowchart Lab/Classroom Environment. La pedagogia frozen è già definita e il fallback manuale resta valido.

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

## F3 — Dettagli di controllo non diventano falsi prerequisiti

`while True`, `break`, `continue`, short-circuit, De Morgan e Big-O restano guided/enrichment dove appropriato.

## F4 — Funzioni formalizzano una preview già fatta

M13 non ripete M05 da zero e Git non inizia prima di M14.

## F5 — Git G1 è embedded outcome subset

```text
full G1 track completion required = false
full canonical lesson completion required = false
```

Python usa Git come processo; non assorbe il corso Git standalone e non aggiunge una seconda verifica Git high-stakes.

## F6 — P2/P3/P4 sono delivery boundary

I profili di grading non sono mastery studente. Il corso insegna gli outcome anche con manual/assert evidence finché il relativo profilo non è certificato.

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

Quindi il **core editorialmente materializzato M04–M30 ha una review semantica completa**.

---

# Cosa NON significa

Non significa:

- lesson approved;
- slide artifacts built/validated;
- teacher sign-off finale;
- Activities complete;
- P1/P2/P3/P4 certified;
- private CI verde;
- `romeo-sim` certified;
- PY2-01 delivery completata;
- Content Pack `1.0.0 / approved`;
- GO classroom.

---

# Layer successivi

Ordine consigliato:

1. static semantic-review contract;
2. coverage/provenance audit finale;
3. slide source/artifact quality pipeline;
4. teacher review finale;
5. grading-profile certification + Activity materialization;
6. PY2-01 Flowchart Lab boundary;
7. private CI execution;
8. TheBitLab rehearsal reale;
9. Content Pack approval;
10. GO classroom.

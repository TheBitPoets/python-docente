# Checkpoint A — Runbook docente

## Funzione del checkpoint

Settimana 17: consolidamento, recupero, prova pratica V2 e primo checkpoint Git guidato.

Stato: **draft controllato / consumer Git G1 collegato al corso canonico**.

## Outcome da verificare

Il checkpoint misura il primo grande nucleo:

- selezione;
- `for` / `while`;
- cicli e condizioni annidate;
- contatori/accumulatori/sentinelle;
- min/max/ricerca;
- funzioni;
- parametri/argomenti;
- `return`;
- scope locale beginner;
- decomposizione;
- casi di test / `assert`;
- debugging;
- regression/refactoring.

## Prova pratica V2

Struttura consigliata:

```text
specifica
→ analisi breve
→ algoritmo/pseudocodice essenziale
→ funzioni candidate
→ implementazione
→ test richiesti
→ bug-fix o spiegazione finale
```

Rubrica indicativa:

- 30% correttezza;
- 15% comprensione/algoritmo;
- 15% scelta costrutti;
- 15% decomposizione/funzioni;
- 10% test/casi limite;
- 10% leggibilità/naming;
- 5% spiegazione/debug.

Non irrigidire le percentuali finché non è stata prototipata la prova reale.

## Variante Romeo

È possibile una variante simulata Romeo soltanto se:

- `romeo-sim` è certificato nel Classroom Environment;
- esiste variante generale equivalente;
- la prova non misura competenze robotiche extra rispetto agli outcome Python.

## Recovery Python

Il checkpoint può assorbire recupero mirato. Ordine dei deficit:

1. correttezza dei costrutti base;
2. terminazione dei cicli;
3. pattern contatore/accumulatore;
4. `return` e passaggio dati;
5. decomposizione;
6. test/debug/refactor.

Non introdurre nuovi prerequisiti finché il nucleo non è stabile.

---

# Git G1 — primo checkpoint guidato

Il corso Python non possiede il curriculum Git. Consuma il contratto G1 canonico dichiarato in:

```text
config/git-g1-consumer.json
```

Source of truth corrente:

```text
TheBitPoets/git
candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
contract: doc/G1_CONSUMER_CONTRACT.md
```

Outcome guidati del checkpoint:

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
G1.STAGE.INTENTIONAL
G1.COMMIT.INTENTIONAL
G1.HISTORY.INSPECT
G1.MODEL.HEAD
G1.WORKFLOW.CHECKPOINT
```

Lesson canoniche da consumare:

```text
G1-M02 working tree / status
G1-M03 diff
G1-M04 index / staging
G1-M05 commit / HEAD
G1-M06 log / show
```

Canary Activity disponibile nel corso Git:

```text
g1-stage-selettivo-001
```

Workflow target:

```text
git status
→ git diff
→ test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log / git show
```

## Obiettivo didattico

Lo studente deve comprendere:

```text
working tree
→ index
→ history
```

e saper spiegare perché il commit rappresenta uno stato scelto e verificato, non semplicemente “tutti i file modificati”.

## Evidence minima

- interpreta `status`;
- legge il diff prima del commit;
- esegue i test rilevanti;
- sceglie cosa mettere in staging;
- verifica lo staged diff;
- crea un commit coerente;
- legge il checkpoint con `log`/`show`;
- sa descrivere il modello beginner `HEAD → branch corrente → commit corrente`.

Git resta prevalentemente evidence di processo nel voto Python; non deve dominare la valutazione della competenza disciplinare.

## Boundary

Non introdurre come outcome Python di seconda:

- branch/merge;
- rebase;
- remotes/push/pull;
- PR/review;
- reflog/reset avanzato;
- internals.

Per spiegazione, remediation e recovery usare il corso Git canonico, non creare una seconda mini-dispensa divergente nel repository Python.

---

# TheBitLab

Il Course Environment Python richiede `git.basic.v1` e non richiede rete/account GitHub per il core G1.

Il Git Lab repository-state della piattaforma ha candidate verde:

```text
TheBitPoets/2cornot2c#761
TheBitPoets/2cornot2c#762
24570f7a3af67634ec0cfbf54f486660359baaf2
```

La certificazione del consumer Python resta separata: `python-docente#8` blocca ancora la CI privata prima dell'avvio del runner. Nessun run `steps=null` vale come prova di pass/fail dei test.

## AI

Nella prova V2:

- nessuna AI generativa per algoritmo/codice/soluzione;
- eventuali strumenti AI dell'editor disabilitati secondo la policy del corso;
- il docente può usare AI fuori dalla prova per preparazione/review dei materiali, non come fonte primaria.

## Handoff al secondo quadrimestre

Dopo il checkpoint il corso entra in PY2-06:

```text
stringhe come sequenze
→ indexing/slicing
→ metodi
→ parsing/frequenze
```

Le funzioni, i test e Git restano workflow trasversali e vengono riutilizzati progressivamente nei progetti successivi.

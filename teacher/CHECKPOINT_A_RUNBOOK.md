# Checkpoint A — Runbook docente

## Funzione del checkpoint

Settimana 17: consolidamento, recupero, prova pratica/mini-project e primo checkpoint Git guidato.

Stato: **draft controllato / consumer Git G1 embedded collegato al corso canonico**.

Il Checkpoint A resta prima di tutto una settimana Python. Git entra come workflow di processo, non come secondo corso standalone da completare nelle stesse tre ore.

## Outcome Python da verificare

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

Git non aggiunge automaticamente una nuova componente ad alto peso a questa rubrica. Resta prevalentemente evidence di processo/formativa nel track Python.

## Variante Romeo

È possibile una variante simulata Romeo soltanto se:

- `romeo-sim` è certificato nel Classroom Environment;
- esiste variante generale equivalente;
- la prova non misura competenze robotiche extra rispetto agli outcome Python.

## Recovery Python

Il checkpoint può assorbire recupero mirato. Ordine dei deficit:

1. correttezza dei costrutti base;
2. terminazione dei cicli;
3. pattern di stato;
4. `return` e passaggio dati;
5. decomposizione;
6. test/debug/refactor.

Non introdurre nuovi prerequisiti finché il nucleo non è stabile.

---

# Git G1 — consumer embedded, non corso standalone

Il corso Python non possiede il curriculum Git. Consuma il contratto G1 canonico dichiarato in:

```text
config/git-g1-consumer.json
```

Il delivery mode è:

```text
embedded-outcome-subset
```

Quindi:

```text
full G1 track completion required = NO
full G1 lesson completion required = NO
```

Source of truth corrente:

```text
TheBitPoets/git
candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
contract: doc/G1_CONSUMER_CONTRACT.md
```

## Che ruolo hanno G1-M02…M06

Sono superfici canoniche per:

- spiegazione;
- remediation;
- richiamo;
- Activity/rubric Git;
- riferimenti contestuali.

Non sono cinque lezioni da erogare integralmente dentro la settimana 17.

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

Canary Activity disponibile nel corso Git:

```text
g1-stage-selettivo-001
```

---

# Git incorporato nel lavoro Python

M14–M16 hanno già introdotto in modo guidato:

```text
git status
git diff
```

Al Checkpoint A il lavoro Python verificato diventa il contesto reale per:

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

Lo studente deve comprendere:

```text
working tree
→ index
→ history
```

e spiegare perché il commit rappresenta uno stato scelto e verificato, non semplicemente “tutti i file modificati”.

## Evidence minima

- interpreta `status`;
- legge il diff prima del commit;
- esegue i test rilevanti;
- sceglie cosa mettere in staging;
- verifica lo staged diff;
- crea un commit coerente;
- legge il checkpoint con `log`/`show`;
- riconosce il modello beginner `HEAD → branch corrente → commit corrente`.

---

# Gestione reale delle tre ore

Il checkpoint ha usi flessibili; non imporre una scaletta unica.

## Variante assessment-focused

La prova Python resta dominante.

Git viene incorporato come:

```text
preflight breve status/diff
...
lavoro Python + test
...
checkpoint finale Git 10–20 min guidati, se il lavoro è pronto
```

Se il tempo non consente un checkpoint Git completo senza comprimere la prova/recupero Python, usare la parte flessibile del checkpoint o una successiva sessione guidata: non abbassare la qualità della valutazione disciplinare per “finire i comandi”.

## Variante lab/consolidation-focused

```text
mini-project Python
→ status/diff durante il lavoro
→ test
→ staging/commit/history guidati
```

Questa è la modalità più naturale per far percepire Git come parte del processo.

---

# Se status/diff non sono ancora acquisiti

Non tentare di insegnare in emergenza l'intero G1 durante una prova valutativa.

Usare:

- lesson/heading G1 canonici come remediation;
- `g1-stage-selettivo-001` in un momento guidato;
- evidence Git separata dalla correttezza Python;
- eventuale recupero nel tempo flessibile.

La difficoltà iniziale con Git non deve oscurare un'evidenza Python valida quando Git non è l'outcome principale della consegna.

---

# Boundary

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

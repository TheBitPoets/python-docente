# Git G1 — integrazione trasversale nel track Python di seconda

> Stato: **consumer contract materializzato / G1 ancora freeze-candidate draft**.  
> Python consuma Git G1; non possiede né duplica il curriculum Git.

## Source of truth canonica

```text
repository: TheBitPoets/git
track: G1
candidate ref: 65d8aff8c9a590560c500762d4dc7378a3239bf2
consumer contract: doc/G1_CONSUMER_CONTRACT.md
content pack: content/git/content-pack.json
```

Nel repository Python la dipendenza machine-readable è:

```text
config/git-g1-consumer.json
```

Il vecchio `README.md` radice di `TheBitPoets/git` resta materiale legacy privato e non è la dispensa canonica.

Il corso Git G1 canonico contiene M01–M08, con lesson, slide, runbook e un Git Lab canary. G1 non è ancora dichiarato frozen/approved, quindi il consumer usa un candidate ref esplicito e dovrà essere riallineato se il contratto G1 cambia prima del freeze.

---

# Principio di integrazione

Git entra nel Python quando gli studenti hanno programmi che vale la pena osservare e versionare:

```text
programma che evolve
→ refactoring
→ bisogno di vedere cosa è cambiato
→ status / diff
→ test
→ staging intenzionale
→ commit
→ storia leggibile
```

Python può avere istruzioni contestuali brevi, ma per spiegazioni, remediation, Activity e rubric Git rimanda al corso G1 canonico.

Regola:

```text
Python G1-Core ⊂ Git G1
```

---

# Outcome consumati

## M14–M16 — evidence `guided`

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
```

Lesson canoniche:

```text
G1-M02  content/git/g1/02_WORKING_TREE_STATUS.md
G1-M03  content/git/g1/03_DIFF.md
```

Uso didattico:

- `status` prima/dopo una modifica;
- `diff` per leggere un refactoring;
- collegare cambiamento osservato e test da rieseguire.

## Checkpoint A — evidence `guided`

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
G1.STAGE.INTENTIONAL
G1.COMMIT.INTENTIONAL
G1.HISTORY.INSPECT
G1.MODEL.HEAD
G1.WORKFLOW.CHECKPOINT
```

Lesson canoniche:

```text
G1-M02 status
G1-M03 diff
G1-M04 index / staging
G1-M05 commit / HEAD
G1-M06 log / show
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

Canary Git Lab canonico:

```text
g1-stage-selettivo-001
```

Il canary valuta lo **stato reale del repository**, non la trascrizione dei comandi.

## Secondo semestre — independent progressivo

Nei progetti selezionati il workflow diventa routine:

```text
status
→ modifica
→ test
→ diff
→ staging intenzionale
→ verifica staged
→ commit
→ history
```

Entrano progressivamente anche:

```text
G1.RECOVERY.BASIC
G1.WORKFLOW.CHECKPOINT
```

Riferimenti G1-M07/M08 per recovery beginner e storia intenzionale.

---

# Cosa Python NON deve insegnare come proprio contenuto

Non sono outcome core del consumer Python di seconda:

- branch;
- merge;
- rebase;
- remotes/push/pull;
- pull request;
- conflitti;
- reflog;
- reset avanzato;
- internals/plumbing.

Questi restano nel curriculum Git progressivo G2–G4.

---

# TheBitLab boundary

Il corso Python dichiara:

```text
git.basic.v1
```

in `config/course-environment.json`.

Requisiti del consumer G1:

- nessun account GitHub obbligatorio;
- nessun remote richiesto;
- nessuna rete richiesta per il core;
- workspace gestito da TheBitLab;
- identità/autore gestita dal profilo;
- recovery beginner fail-safe;
- nessun comando distruttivo improvvisato.

Il Git Lab repository-state è stato implementato nella piattaforma in:

```text
TheBitPoets/2cornot2c#761
TheBitPoets/2cornot2c#762
```

Candidate platform pin con evidence verde:

```text
24570f7a3af67634ec0cfbf54f486660359baaf2
```

Questo non rende automaticamente verde il consumer privato `python-docente`: la CI del corso resta separatamente bloccata da `python-docente#8` prima dell'avvio del runner.

---

# Recovery policy beginner

Quando lo stato non è quello atteso:

```text
1. non cancellare file a caso
2. non usare --force
3. leggere git status
4. osservare git diff / git diff --staged
5. distinguere working tree e index
6. applicare solo la procedura G1 di recovery pertinente
```

`reset --hard`, force push, rebase e recovery avanzato non appartengono a G1-Core Python.

---

# Valutazione nel corso Python

Git è prevalentemente competenza di processo/formativa.

Può contribuire alle rubriche di progetto per:

- processo ordinato;
- lettura del proprio diff;
- staging coerente;
- checkpoint significativi;
- messaggi di commit comprensibili;
- capacità di leggere una storia breve.

Non deve diventare il criterio dominante del voto Python.

---

# Verifica anti-divergenza

`tests/git_g1_consumer_contract.py` deve verificare almeno:

- pin e repository G1 dichiarati;
- `git.basic.v1` richiesto dall'ambiente;
- outcome M14–M16 e Checkpoint A coerenti col contratto;
- presenza di `status/diff` nelle lesson Python interessate;
- presenza del workflow completo nel Checkpoint A;
- nessuna dipendenza da GitHub account/network per il core;
- separazione curriculum Python/Git.

La CI privata attuale può non eseguire il test a causa del blocker `#8`; il test resta comunque parte del gate appena i runner tornano disponibili.

---

# Criteri per dichiarare il consumer Python G1 chiuso

- [x] source of truth `TheBitPoets/git` identificata;
- [x] candidate ref G1 registrato;
- [x] contratto consumer machine-readable creato;
- [x] `status`/`diff` presenti in M14–M16;
- [x] primo checkpoint Git previsto al Checkpoint A;
- [x] `git.basic.v1` dichiarato nel Course Environment;
- [x] Git Lab platform candidate verde;
- [ ] test consumer eseguito realmente in CI privata o ambiente equivalente;
- [ ] G1 freeze/decision-owner finalizzato oppure candidate ref esplicitamente accettato per il pilot;
- [ ] rehearsal reale nel Classroom Environment/TheBitLab.

Quindi l'**integrazione strutturale** può essere completata adesso; la **certificazione delivery** resta un gate successivo.

# Git G1 — integrazione trasversale nel track Python di seconda

> Stato: **design approvato / materiale G1 in ingresso editoriale**. Git resta un curriculum autonomo; questo documento definisce soltanto il sottoinsieme G1 consumato dal Python di seconda.

## Principio

Git non deve diventare:

- una nuova UDA che sottrae settimane al Python;
- un blocco tutto alla fine dell'anno;
- un prerequisito delle prime settimane;
- una serie di comandi da memorizzare senza un problema reale.

Entra quando gli studenti hanno programmi che vale la pena versionare:

```text
programma che evolve
→ refactoring
→ bisogno di vedere cosa è cambiato
→ status/diff
→ stato verificato
→ primo commit
```

## Relazione col futuro corso Git

Il curriculum Git autonomo sarà la fonte canonica. Python consumerà soltanto G1.

**Il trigger per l'audit delle dispense docente è ora raggiunto:** M14–M16 e Checkpoint A sono materializzati. Le dispense possono quindi essere fornite e classificate prima di promuovere il micro-materiale G1 a versione definitiva.

Workflow di intake:

1. audit delle dispense e della versione Git a cui fanno riferimento;
2. classificazione dei contenuti in G1/G2/G3/G4;
3. selezione delle sole parti G1 necessarie a Python seconda;
4. adattamento originale al formato TheBitLab;
5. collegamento da `student/CHECKPOINT_A.md` / `teacher/CHECKPOINT_A_RUNBOOK.md` al futuro materiale Git canonico;
6. riuso futuro dallo standalone Git course, senza duplicazioni.

---

# Outcome G1 nel secondo anno

Entro la fine dell'anno lo studente dovrebbe saper, in un repository didattico controllato:

- spiegare a cosa serve uno storico delle modifiche;
- distinguere file modificato e versione registrata/commit;
- usare `git status`;
- usare `git diff` per leggere cosa è cambiato;
- selezionare modifiche con `git add` nel workflow guidato;
- creare un `git commit` con messaggio comprensibile;
- leggere una storia breve con `git log`/vista equivalente;
- capire che commit diversi identificano stati differenti del progetto;
- evitare comandi distruttivi improvvisati;
- seguire una procedura sicura di recovery quando non comprende lo stato.

Non è richiesto in G1:

- branch;
- merge;
- rebase;
- remotes/push/pull;
- PR;
- conflitti;
- reset avanzato;
- Git internals.

---

# Progressione nel track Python

## Settimane 1–12

Nessun Git come obiettivo curricolare. TheBitLab può usarlo internamente, ma lo studente non deve gestire contemporaneamente algoritmi, sintassi, runner e versionamento.

## M13–M14 — osservare lo stato

Micro-introduzione:

```text
git status
```

Attività tipica:

1. stato prima del refactoring;
2. modifica di una funzione;
3. stato dopo;
4. spiegazione di `modified`.

## M14–M16 — leggere il cambiamento

```text
git diff
```

Collegamento naturale con il refactoring:

> che cosa è cambiato nella struttura e quali test devono restare verdi?

## Checkpoint A — primo commit guidato

Workflow canonico target:

```text
status
→ diff
→ test
→ add
→ commit
→ log
```

Il commit deve raccontare un cambiamento coerente e verificato.

Messaggi:

```text
Completa checkpoint funzioni e test
```

è migliore di:

```text
modifiche
```

## Secondo semestre

Git diventa routine di processo in alcune Activity/progetti:

```text
status → modifica → test → diff → add/commit
```

Non serve una lezione Git ogni settimana.

## OOP/capstone

Utili 2–3 checkpoint guidati, ad esempio:

- skeleton classi;
- comportamento;
- bug-fix/refactor.

Git non deve diventare criterio dominante del voto Python.

---

# TheBitLab boundary

Il Classroom Environment deve fornire un profilo equivalente a:

```text
git.basic.v1
```

G1 deve poter essere completamente locale:

- nessun account GitHub obbligatorio;
- nessun remote richiesto;
- workspace confinato;
- identità/autore gestita in modo appropriato dal profilo;
- messaggi sicuri in caso di stato inatteso.

---

# Recovery policy beginner

Regola studente:

```text
se lo stato Git non è quello atteso:
1. non cancellare file a caso
2. non usare --force
3. leggi status
4. salva/copia il lavoro se indicato
5. segui la procedura di recovery del corso
```

`reset --hard`, force push e rebase non appartengono a G1.

`git restore` può comparire solo in scenario guidato dopo aver chiarito che può scartare modifiche non registrate.

---

# Micro-evidence G1

## G1-A — Observe

Leggere `git status`: clean / modified / staged.

## G1-B — Diff

Leggere un diff di una funzione e descrivere il cambiamento.

## G1-C — Guided commit

```text
status → diff → test → add → commit → log
```

## G1-D — Safe diagnose

Dato uno stato semplice, scegliere il prossimo passo sicuro senza comandi distruttivi.

Queste micro-evidence dovrebbero diventare materiale canonico del futuro corso Git e venire richiamate da Python.

---

# Valutazione

Git G1 è prevalentemente competenza di processo/formativa. Non aggiunge una quinta verifica obbligatoria.

Può contribuire alle rubriche di progetto su:

- processo ordinato;
- checkpoint significativi;
- capacità di leggere il proprio diff;
- messaggi di commit comprensibili.

Non penalizzare pesantemente un buon programma Python per una svista Git beginner se Git non è l'outcome esplicito della consegna.

---

# Criteri per dichiarare G1 integrato

- `status`/`diff` dentro funzioni/refactoring;
- primo commit al Checkpoint A;
- alcuni checkpoint nel secondo semestre;
- nessun remote/account obbligatorio;
- toolchain gestita da TheBitLab;
- dispense docente auditate;
- materiale G1 canonico pubblicato/collegato;
- nessuna duplicazione del futuro corso Git autonomo.

# Git G1 — integrazione trasversale nel track Python di seconda

> Stato: **design approvato / source of truth Git ora attivo**. Git resta un curriculum autonomo; questo documento definisce soltanto il sottoinsieme G1 consumato dal Python di seconda.

## Source of truth

Il curriculum Git canonico è ora:

```text
TheBitPoets/git
branch di progettazione: agent/git-course-architecture
```

Documenti autorevoli in costruzione:

- `doc/COURSE_ARCHITECTURE.md` — curriculum trasversale G0→G4;
- `doc/CURRICULUM_ROADMAP.md` — progressione quinquennale;
- `tracks/g1/COURSE_DESIGN.md` — G1 Local Git;
- `tracks/g1/COMPETENCY_MATRIX.md`;
- `tracks/g1/ASSESSMENT_MODEL.md`;
- `sources/MANNING_AUDIT.md`;
- `sources/PRO_GIT_MAPPING.md`.

Il vecchio `README.md` di `TheBitPoets/git` è una traduzione legacy/incompleta di Manning e **non è materiale canonico del corso**.

L'audit ha verificato che contiene i capitoli 1–10 su 20; non verrà completata la traduzione. Il nuovo corso è originale, verificato contro Git official docs e usa Pro Git come coverage/concept map.

---

# Principio di integrazione

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

Python **consuma G1-Core**, ma non possiede né duplica le lesson Git.

Quando il materiale Git G1 canonico è disponibile, `student/CHECKPOINT_A.md` e i runbook Python devono linkarlo/importarlo come prerequisito/side-course invece di mantenerne una copia divergente.

---

# Outcome G1 consumati dal Python di seconda

Entro la fine dell'anno lo studente dovrebbe saper, in un repository didattico controllato:

- spiegare a cosa serve uno storico delle modifiche;
- distinguere working tree, staging/index e versione registrata/commit a livello beginner;
- usare `git status`;
- usare `git diff` per leggere cosa è cambiato;
- selezionare modifiche con `git add` nel workflow guidato;
- creare un `git commit` con messaggio comprensibile;
- leggere una storia breve con `git log`/vista equivalente;
- capire che commit diversi identificano stati differenti del progetto;
- evitare comandi distruttivi improvvisati;
- seguire una procedura sicura di recovery quando non comprende lo stato.

Non è richiesto nel consumer Python G1-Core:

- branch;
- merge;
- rebase;
- remotes/push/pull;
- PR;
- conflitti;
- reset avanzato;
- Git internals.

Questi appartengono al curriculum Git G2–G4.

---

# Progressione nel track Python

## Settimane 1–12

Nessun Git come obiettivo curricolare. TheBitLab può usarlo internamente, ma lo studente non deve gestire contemporaneamente algoritmi, sintassi, runner e versionamento.

## M13–M14 — osservare lo stato

Micro-introduzione dal corso Git G1:

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

Workflow canonico G1-Core:

```text
status
→ diff
→ test
→ add
→ status / diff --staged
→ commit
→ log
```

L'aggiunta di `diff --staged` serve a costruire il modello corretto Working Tree → Index → Repository e non trasforma `git add` in una formula da memorizzare.

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
status → modifica → test → diff → add → verifica staging → commit
```

Non serve una lezione Git ogni settimana.

## OOP/capstone

Utili 2–3 checkpoint guidati, ad esempio:

- skeleton classi;
- comportamento;
- bug-fix/refactor.

Git non deve diventare criterio dominante del voto Python.

---

# Relazione con G1 standalone

Il corso Git G1 completo aggiunge rispetto al consumer Python:

- staging intenzionale/partial staging;
- lifecycle tracked/untracked/ignored;
- `.gitignore`;
- safe undo;
- revision selection e confronto;
- `git help` / autoapprendimento;
- checkpoint Git dedicato.

Quindi:

```text
Python G1-Core ⊂ Git G1
```

---

# TheBitLab boundary

Il Classroom Environment deve fornire:

```text
git.basic.v1
```

G1 deve poter essere completamente locale:

- nessun account GitHub obbligatorio;
- nessun remote richiesto;
- workspace confinato;
- identità/autore gestita in modo appropriato dal profilo;
- messaggi sicuri in caso di stato inatteso.

Per il grading repository-state è aperto il requisito piattaforma:

```text
TheBitPoets/2cornot2c#759
```

Target: `thebitlab.git-evidence.v1`, con ispezione sicura di index, graph, refs e tree. Fino alla sua certificazione, Git resta evidence manuale/formativa o viene valutato tramite workflow esplicito; non simuliamo autograding con stdout.

---

# Recovery policy beginner

Regola studente:

```text
se lo stato Git non è quello atteso:
1. non cancellare file a caso
2. non usare --force
3. leggi status
4. osserva diff / diff --staged
5. salva/copia il lavoro se indicato
6. segui la procedura di recovery del corso
```

`reset --hard`, force push e rebase non appartengono a G1.

`git restore` compare soltanto dopo aver chiarito quale stato viene scartato e con un recovery scenario controllato.

---

# Micro-evidence G1 consumate da Python

## G1-A — Observe

Leggere `git status`: clean / modified / staged.

## G1-B — Diff

Leggere un diff di una funzione e descrivere il cambiamento.

## G1-C — Guided commit

```text
status → diff → test → add → diff --staged → commit → log
```

## G1-D — Safe diagnose

Dato uno stato semplice, scegliere il prossimo passo sicuro senza comandi distruttivi.

Le Activity canoniche devono vivere nel corso Git e venire richiamate/consumate da Python.

---

# Valutazione

Git G1 è prevalentemente competenza di processo/formativa nel track Python. Non aggiunge una quinta verifica obbligatoria.

Può contribuire alle rubriche di progetto su:

- processo ordinato;
- checkpoint significativi;
- capacità di leggere il proprio diff;
- messaggi di commit comprensibili.

Non penalizzare pesantemente un buon programma Python per una svista Git beginner se Git non è l'outcome esplicito della consegna.

Il corso Git standalone possiede invece la propria assessment model G1.

---

# Criteri per dichiarare G1 integrato

- source of truth `TheBitPoets/git` stabile;
- G1 lesson/Activity canoniche pubblicate;
- `status`/`diff` dentro funzioni/refactoring;
- primo commit al Checkpoint A;
- alcuni checkpoint nel secondo semestre;
- nessun remote/account obbligatorio;
- toolchain gestita da TheBitLab;
- nessuna duplicazione del corso Git autonomo;
- grader Git #759 usato solo quando realmente certificato.

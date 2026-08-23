# Git G1 — integrazione trasversale nel track Python di seconda

> Stato: **design DRAFT**. Git resta un curriculum autonomo futuro; questo documento definisce soltanto il sottoinsieme G1 necessario al workflow Python di seconda.

## Principio

Git non deve diventare:

- una nuova UDA che sottrae settimane al Python;
- un blocco tutto alla fine dell'anno;
- un prerequisito delle prime settimane;
- una serie di comandi da memorizzare senza un problema reale.

Deve entrare quando gli studenti hanno ormai file/programmi che vale la pena versionare.

```text
prima programmi usa-e-getta / Activity gestite
→ poi progetto che evolve
→ nasce il bisogno di vedere cosa ho cambiato
→ Git G1
```

## Relazione col futuro corso Git

Il curriculum Git autonomo sarà la fonte canonica.

Python userà soltanto:

```text
G1 — fondamenti
```

Quando il repository del corso Git esisterà, queste micro-lesson potranno diventare riferimenti/import controllati invece di essere duplicate.

Le dispense Git esistenti del docente saranno auditate quando:

1. inizierà il corso Git autonomo; oppure
2. inizierà la produzione materiale definitiva di G1 per Python.

Non sono necessarie per il freeze architetturale Python.

---

# Outcome G1 nel secondo anno

Entro la fine dell'anno lo studente dovrebbe saper, in un repository didattico controllato:

- spiegare a cosa serve uno storico delle modifiche;
- distinguere file modificato e versione salvata/commit;
- usare `git status`;
- usare `git diff` per leggere cosa è cambiato;
- selezionare modifiche con `git add` nel workflow guidato;
- creare un `git commit` con messaggio comprensibile;
- leggere una storia breve con `git log`/vista equivalente;
- capire che commit diversi identificano stati differenti del progetto;
- evitare comandi distruttivi improvvisati per "far sparire" un errore;
- chiedere/seguire una procedura sicura di recupero quando non capisce lo stato del repository.

Non è richiesto in G1:

- branch;
- merge;
- rebase;
- remotes/push/pull;
- PR;
- conflitti;
- reset avanzato;
- Git internals.

Questi appartengono ai livelli G2+.

---

# Quando introdurlo

## Settimane 1–12

**Nessun Git come obiettivo curricolare.**

TheBitLab può usare Git internamente per delivery/versionamento, ma lo studente non deve gestire contemporaneamente:

- algoritmi;
- sintassi Python;
- flow chart;
- runner;
- Git.

Riduciamo il carico cognitivo.

## Settimane 13–14 — osservare lo stato

Con PY2-05/funzioni, i programmi iniziano a essere composti da più responsabilità e refactoring.

Micro-introduzione:

```text
repository
working tree
status
```

Attività da 10–15 minuti dentro una normale lezione/lab:

1. aprire un piccolo progetto già versionato;
2. `git status` prima della modifica;
3. cambiare una funzione;
4. `git status` dopo;
5. spiegare cosa significa `modified`.

Nessun commit autonomo ancora necessario.

## Settimane 15–16 — leggere il cambiamento

Introdurre:

```text
git diff
```

Collegamento didattico perfetto col refactoring:

> cosa è cambiato nel codice e cosa è rimasto semanticamente uguale?

Micro-task:

- estrai una funzione;
- osserva `git diff`;
- individua righe aggiunte/rimosse;
- esegui i test;
- spiega la relazione diff ↔ refactoring.

## Checkpoint A — primo commit guidato

Nel mini-project/pratica del checkpoint:

```text
status
→ diff
→ add
→ commit
```

Il docente/TheBitLab guida il workflow.

Messaggio commit semplice:

```text
Aggiungi validazione dei voti
```

non:

```text
modifiche
```

Il focus è:

> un commit racconta un cambiamento coerente verificato.

## Secondo semestre — routine crescente

Non serve una lezione Git ogni settimana.

In alcune Activity/progetti:

1. controlla `status`;
2. modifica/testa;
3. guarda `diff`;
4. quando il checkpoint è corretto, `add` + `commit`.

Git diventa uno strumento del processo, come REPL/test, non un argomento estraneo.

## OOP/capstone

Nel capstone:

- almeno 2–3 checkpoint Git guidati sono utili;
- un commit può corrispondere a:
  - skeleton classi;
  - implementazione comportamento;
  - correzione bug/refactoring.

L'evidence Git non deve diventare un criterio dominante del voto Python.

## Settimana 33

Può ospitare consolidamento/history/troubleshooting semplice, ma **non è la prima esposizione a Git**.

---

# TheBitLab boundary

Il Classroom Environment deve fornire:

```text
git.basic.v1
```

Git è già presente nei profili correnti, ma il corso non deve chiedere configurazioni host manuali.

TheBitLab dovrebbe, dove possibile:

- creare/aprire il repository didattico;
- garantire identità/autore appropriata per ambiente scolastico senza richiedere account personali quando non necessario;
- mantenere workspace confinato;
- evitare che credenziali remote siano necessarie nel G1;
- offrire messaggi sicuri se il repository è in stato inatteso.

G1 può essere completamente **locale**: non richiede GitHub remoto.

---

# Recovery policy beginner

Non insegnare una lista di comandi potenti prima del modello.

Regola studente:

```text
se lo stato Git non è quello atteso:
1. non cancellare file a caso
2. non usare --force
3. leggi status
4. salva/copia il lavoro se indicato
5. chiedi/segui la procedura di recovery del corso
```

Comandi come `reset --hard`, force push o rebase non appartengono a G1.

`git restore` può essere mostrato solo in uno scenario guidato e dopo aver spiegato che **scarta modifiche non salvate**.

---

# Activity/evidence Git dentro Python

## G1-A — Observe

Dato un `git status`, distinguere:

- clean;
- modified;
- staged.

## G1-B — Diff

Leggere un diff di una funzione modificata e descrivere cosa è cambiato.

## G1-C — Guided commit

Con progetto già testato:

```text
status → diff → add → commit → log
```

## G1-D — Safe diagnose

Dato uno stato semplice, scegliere il prossimo passo sicuro; niente comandi distruttivi.

Queste evidence possono vivere come micro-attività del futuro corso Git e venire richiamate dal track Python.

---

# Valutazione

Git G1 nel secondo anno è prevalentemente **competenza di processo/formativa**.

Non aggiungerei una quinta verifica obbligatoria.

Può contribuire alle rubriche progetto in dimensioni come:

- processo ordinato;
- checkpoint significativi;
- capacità di leggere il proprio cambiamento;
- messaggi di commit comprensibili.

Non penalizzare pesantemente un buon programma Python per una svista Git beginner, salvo che la consegna abbia esplicitamente quell'outcome.

---

# Criteri per dichiarare G1 integrato

- nessuna introduzione Git prima che serva realmente;
- `status`/`diff` introdotti durante funzioni/refactoring;
- primo commit entro Checkpoint A;
- almeno alcuni commit/checkpoint nel secondo semestre;
- nessuna dipendenza dalla settimana 33;
- nessun remote/account GitHub necessario al core;
- toolchain gestita da TheBitLab;
- materiali definitivi allineati al futuro corso Git autonomo;
- dispense docente auditate prima della pubblicazione delle lesson G1 definitive.

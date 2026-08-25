# Checkpoint A — Consolidamento del primo nucleo

> Stato: **draft controllato / Git G1 consumer collegato al corso canonico**.

## Dove siamo

Hai completato il primo grande blocco del corso:

```text
problema / algoritmo
→ Python di base
→ selezione
→ cicli
→ pattern iterativi
→ funzioni
→ test / debug / refactor
```

Il Checkpoint A serve a:

- verificare ciò che sai fare;
- consolidare i punti fragili;
- recuperare outcome mancanti;
- svolgere la prova pratica del primo quadrimestre;
- creare il primo checkpoint Git significativo del tuo lavoro.

---

# 1. Competenze da portare al checkpoint

Devi saper:

- leggere una specifica e individuare input/output/vincoli;
- scegliere `if`, `for` o `while` e motivarlo;
- usare contatore, accumulatore, sentinella, min/max o ricerca quando il problema lo richiede;
- eseguire trace di cicli e condizioni;
- definire funzioni con parametri e `return`;
- distinguere `return` da `print`;
- passare dati esplicitamente tra funzioni;
- decomporre un problema in responsabilità;
- scrivere casi di test e semplici `assert`;
- diagnosticare un bug;
- aggiungere un regression test;
- refactorare mantenendo i test verdi.

---

# 2. Forma della prova pratica V2

La prova può seguire questo flusso:

```text
specifica
→ analisi breve
→ algoritmo / pseudocodice essenziale
→ funzioni candidate
→ implementazione
→ casi / assert
→ debug o correzione
→ breve spiegazione finale
```

Il dominio concreto può cambiare. Non devi imparare una soluzione a memoria.

---

# 3. Strategia durante la prova

## Prima del codice

Scrivi almeno:

```text
input
output
vincoli
2–4 casi di test
```

Se il problema è abbastanza grande, aggiungi:

```text
funzioni candidate
parametri
return
```

## Durante il codice

Lavora per passi piccoli:

```text
una responsabilità
→ prova
→ successiva
→ integra
```

## Se qualcosa fallisce

Non cambiare righe casualmente.

Usa:

```text
caso che fallisce
→ atteso
→ ottenuto
→ punto probabile
→ modifica minima
→ riesegui
```

---

# 4. Mini-checklist tecnica

Prima della consegna controlla:

- [ ] il programma rispetta davvero la specifica;
- [ ] i casi normali passano;
- [ ] i confini rilevanti sono testati;
- [ ] nessun `while` può restare infinito per aggiornamento mancante;
- [ ] accumulatori/contatori sono inizializzati al livello corretto;
- [ ] le funzioni di calcolo restituiscono valori invece di stampare per errore;
- [ ] i dati necessari vengono passati in modo esplicito;
- [ ] gli `assert` rappresentano la specifica;
- [ ] dopo un fix hai rieseguito anche i test precedenti;
- [ ] i nomi comunicano il significato.

---

# 5. Primo checkpoint Git G1

Git è un corso separato. Da qui il corso Python **consuma** alcune competenze del livello G1 senza ricopiare le lezioni Git.

Source of truth:

```text
TheBitPoets/git
G1 — Local Git
```

Per questo checkpoint userai in TheBitLab le lesson canoniche G1-M02…G1-M06 e, quando assegnata, l'Activity:

```text
g1-stage-selettivo-001
```

Workflow guidato:

```text
git status
→ git diff
→ esegui i test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log
```

L'obiettivo non è memorizzare una sequenza di comandi. Devi capire che stai passando da:

```text
modifiche nel working tree
→ modifiche scelte nell'index
→ checkpoint registrato nella storia
```

Prima del commit devi saper spiegare:

- quali file sono cambiati;
- che cosa mostra il diff;
- quali modifiche stai preparando;
- perché i test sono verdi;
- che cosa racconterà il commit.

Dopo il commit devi saper riconoscere il nuovo checkpoint nella storia.

Per spiegazioni e recovery usa sempre il materiale Git G1 canonico fornito nel Course Workspace/TheBitLab.

---

# 6. Che cosa NON serve ancora sapere di Git

Non sono richiesti in questo checkpoint:

- branch e merge;
- rebase;
- pull request;
- remotes/push/pull;
- reset/reflog avanzati;
- Git internals.

Questi appartengono ai livelli successivi del curriculum Git.

Se lo stato del repository non è quello atteso:

```text
non usare comandi distruttivi a caso
→ leggi status
→ osserva diff / diff --staged
→ segui la procedura G1 di recovery
```

---

# 7. Dopo il checkpoint

Il corso riparte con una nuova famiglia di problemi:

```text
testo come sequenza
→ stringhe
→ indicizzazione/slicing
→ parsing semplice
→ poi liste e altre strutture dati
```

Funzioni, test e Git non scompaiono: diventano strumenti trasversali che userai progressivamente nei progetti successivi.

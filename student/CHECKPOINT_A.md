# Checkpoint A — Consolidamento del primo nucleo

> Stato: **draft controllato / Git G1 consumer embedded collegato al corso canonico**.

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
- svolgere una prova pratica o un mini-progetto del primo quadrimestre;
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

# 2. Forma possibile della prova pratica

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

# 3. Strategia durante il lavoro Python

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

# 5. Primo checkpoint Git G1 — modalità embedded

Git è un corso separato. Nel corso Python usiamo un **embedded outcome subset** di G1: soltanto le competenze Git necessarie a osservare e registrare in modo ordinato il lavoro Python.

Questo significa una cosa importante:

> **non devi completare il corso G1 standalone dentro il Checkpoint A.**

Source of truth:

```text
TheBitPoets/git
G1 — Local Git
```

Le lesson canoniche G1-M02…G1-M06 possono essere aperte da TheBitLab come:

- spiegazione;
- richiamo;
- remediation;
- riferimento al passaggio che stai svolgendo.

Non sono cinque lezioni aggiuntive da studiare integralmente nella stessa settimana.

Quando assegnata, puoi usare anche l'Activity canonica:

```text
g1-stage-selettivo-001
```

---

# 6. Git incorporato nel lavoro Python

Durante M14–M16 hai già iniziato a usare in modo guidato:

```text
git status
git diff
```

Nel Checkpoint A completi il primo ciclo:

```text
git status
→ git diff
→ esegui i test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log / git show
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

---

# 7. Se Git non ti è ancora chiaro

Non usare comandi distruttivi per “sistemare” lo stato.

Procedura:

```text
leggi git status
→ osserva git diff / git diff --staged
→ conserva il lavoro
→ apri il riferimento/remediation G1 canonico
→ chiedi supporto se lo stato non è quello atteso
```

Una difficoltà beginner su Git non trasforma automaticamente in sbagliato un programma Python corretto: nel track Python Git è soprattutto evidence di processo.

---

# 8. Che cosa NON serve ancora sapere di Git

Non sono richiesti in questo checkpoint:

- branch e merge;
- rebase;
- pull request;
- remotes/push/pull;
- reset/reflog avanzati;
- Git internals.

Questi appartengono ai livelli successivi del curriculum Git.

---

# 9. Dopo il checkpoint

Il corso riparte con una nuova famiglia di problemi:

```text
testo come sequenza
→ stringhe
→ indicizzazione/slicing
→ parsing semplice
→ poi liste e altre strutture dati
```

Funzioni, test e Git non scompaiono: diventano strumenti trasversali che userai progressivamente nei progetti successivi.

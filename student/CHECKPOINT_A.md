# Checkpoint A — Consolidamento del primo nucleo

> Stato: **draft controllato**. La parte Git G1 sarà riallineata alle dispense docente prima della promozione editoriale.

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

Git è un curriculum separato, ma da questo checkpoint iniziamo a usarne il livello G1 nel lavoro Python.

Workflow target:

```text
git status
→ git diff
→ test
→ git add
→ git commit
→ git log
```

## `git status`

Serve a vedere quali file sono modificati/non tracciati e lo stato del workspace.

## `git diff`

Serve a vedere che cosa è cambiato rispetto allo stato precedente.

## `git add`

Seleziona le modifiche che vuoi includere nel prossimo checkpoint.

## `git commit`

Registra uno stato significativo con un messaggio comprensibile.

Esempio di messaggio:

```text
Complete first functions checkpoint
```

oppure, se il corso usa convenzioni italiane:

```text
Completa checkpoint funzioni e test
```

## `git log`

Mostra la storia dei checkpoint registrati.

La sintassi/guida definitiva G1 verrà fornita dal corso Git/dispensa canonica integrata in TheBitLab.

---

# 6. Che cosa NON serve ancora sapere di Git

Non sono richiesti in questo checkpoint:

- branch avanzati;
- merge/rebase;
- pull request;
- reset/reflog;
- stash;
- remote workflow complessi;
- CI/CD.

Questi appartengono ai livelli successivi del curriculum Git.

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

Il controllo del flusso e le funzioni non scompaiono: verranno riusati continuamente.

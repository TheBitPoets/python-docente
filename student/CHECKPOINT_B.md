# Checkpoint B — Stringhe, liste, tuple e dati tabellari

> Stato: **draft controllato**. Settimana 24; non introduce nuovi prerequisiti.

## Scopo

Consolidare il secondo blocco del corso:

```text
str come sequenza immutabile
→ algoritmi su testo
→ list mutabile
→ alias/copie
→ tuple/unpacking
→ dati tabellari
```

Il checkpoint può ospitare recupero, mini-project e preparazione alla prova teorico/scritta V3.

Non serve usare tutte le strutture e tutti i metodi nello stesso esercizio: il checkpoint misura soprattutto **scelta e comprensione del modello**.

---

# 1. Competenze raggruppate

## A — Sequenze testuali

Devi saper:

- usare indici/slicing;
- spiegare immutabilità;
- iterare su una stringa;
- scegliere una normalizzazione coerente;
- costruire un piccolo algoritmo su testo;
- progettare casi limite.

## B — Mutabilità e riferimenti

Devi saper:

- spiegare `list` mutabile vs `str` immutabile;
- prevedere una mutazione;
- distinguere alias e copia esterna;
- evitare mutazioni strutturali ingenue durante iterazione;
- verificare se una funzione muta o non muta l'input secondo il contratto.

## C — Operazioni sulle liste

Devi saper:

- costruire una lista con `append`;
- attraversarla in modo appropriato;
- filtrare/trasformare costruendo un nuovo risultato;
- distinguere `sort()` e `sorted()`.

Non devi ricordare a memoria ogni metodo visto come guided/enrichment.

## D — Modello dati

Devi saper:

- usare tuple/unpacking semplici;
- scegliere list vs tuple;
- costruire/attraversare una lista di liste;
- riconoscere righe condivise involontariamente;
- motivare la struttura scelta.

## E — Metodo di lavoro

Devi continuare a usare:

- funzioni;
- casi/assert;
- trace;
- debug;
- spiegazione della scelta.

---

# 2. Mini-project candidato

Un piccolo registro/tabella dati può contenere, **solo quando il dominio lo richiede**:

- testo da normalizzare;
- una lista principale;
- tuple o righe tabellari;
- 2–4 funzioni;
- ricerca/aggregazione;
- almeno 5 casi complessivi;
- spiegazione della struttura dati scelta.

Non forzare contemporaneamente:

```text
stringa + lista + tuple + matrice
```

solo per “coprire tutto”.

Un buon progetto dimostra che hai scelto la struttura giusta, non che hai usato il maggior numero di feature.

---

# 3. Error Clinic

Devi saper diagnosticare almeno alcuni bug rappresentativi:

- metodo mutante assegnato (`lista = lista.append(...)` / `lista = lista.sort()`);
- alias involontario;
- rimozione mentre iteri;
- indice/slice errato;
- matrice costruita con righe condivise;
- list/tuple scelta senza coerenza col requisito.

La diagnosi deve spiegare **perché** il modello è sbagliato, non soltanto fornire la riga corretta.

---

# 4. Preparazione V3

La prova teorico/scritta successiva potrà chiedere:

- trace su stringhe/liste;
- mutabilità e alias;
- output/errore previsto;
- scelta list vs tuple;
- confronto di due soluzioni;
- correzione di bug;
- motivazione della struttura.

Dettagli enrichment non svolti realmente in classe non entrano automaticamente nella prova.

---

# 5. Git G1 — riuso, non nuovo contenuto

Checkpoint B non introduce G2 e non aggiunge nuovi comandi Git.

Se il mini-project usa Git, riusa il workflow G1 già acquisito:

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

Git resta evidence di processo. La difficoltà principale del checkpoint è Python/modellazione dati, non il versionamento.

Se lo stato Git è inatteso, usa la remediation G1 canonica invece di comandi distruttivi improvvisati.

---

# 6. Dopo il checkpoint

Entrano strutture con semantiche diverse dalla semplice sequenza:

```text
set  → unicità / membership
dict → chiave → valore / lookup
```

La domanda diventa:

> quali operazioni devo fare più spesso e quale struttura le rende naturali?

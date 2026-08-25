# Checkpoint A — Runbook docente

## Funzione del checkpoint

Settimana 17: consolidamento, recupero, prova pratica V2 e primo checkpoint Git guidato.

Stato: **draft controllato**. La parte Git G1 deve essere riallineata alle dispense docente prima della promozione editoriale.

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

Rubrica indicativa già definita nel calendario valutazioni:

- 30% correttezza;
- 15% comprensione/algoritmo;
- 15% scelta costrutti;
- 15% decomposizione/funzioni;
- 10% test/casi limite;
- 10% leggibilità/naming;
- 5% spiegazione/debug.

Non irrigidire le percentuali finché non abbiamo prototipato la prova reale.

## Variante Romeo

È possibile una variante simulata Romeo soltanto se:

- `romeo-sim` è certificato nel Classroom Environment;
- esiste variante generale equivalente;
- la prova non misura competenze robotiche extra rispetto agli outcome Python.

## Recovery

Il checkpoint può assorbire recupero mirato. Ordine dei deficit da recuperare:

1. correttezza dei costrutti base;
2. terminazione dei cicli;
3. pattern contatore/accumulatore;
4. `return` e passaggio dati;
5. decomposizione;
6. test/debug/refactor.

Non introdurre nuovi prerequisiti finché il nucleo non è stabile.

## Git G1 — primo checkpoint guidato

Target minimo:

```text
git status
→ git diff
→ test
→ git add
→ git commit
→ git log essenziale
```

### Obiettivo didattico

Git non viene valutato come corso autonomo completo. Qui serve a far capire:

```text
workspace modificato
→ controllo delle differenze
→ stato verificato/testato
→ checkpoint registrato
→ storia leggibile
```

### Evidence minima

- `status` compreso;
- diff letto prima del commit;
- commit eseguito su uno stato funzionante;
- messaggio che descrive il checkpoint;
- `log` usato per vedere il commit.

### Boundary

Non introdurre ancora:

- branching complesso;
- merge/rebase;
- PR/review;
- stash/reset/reflog;
- remote workflow avanzato.

Questi appartengono al corso Git progressivo separato.

## Dipendenza dalle dispense Git

Questo è il **primo punto del corso Python in cui le dispense Git del docente servono realmente**.

Workflow previsto quando vengono fornite:

1. audit contenuto e versione Git;
2. classificazione materiale in G1/G2/G3/G4;
3. estrazione delle sole parti G1;
4. riscrittura/adattamento nel formato TheBitLab;
5. collegamento dal Checkpoint A al materiale Git canonico;
6. nessuna duplicazione del futuro corso Git completo dentro `python-docente`.

## TheBitLab

Per il checkpoint finale serve il Classroom Environment gestito. Il grading automatico deve restare limitato ai profili certificati:

- P1 se il problema è realmente stdin/stdout;
- P2 solo dopo certificazione function-behavior;
- rubric/manual evidence per decomposizione, spiegazione e design.

Non deformare la prova per farla entrare in un grader disponibile.

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

Le funzioni, i test e Git restano workflow trasversali e continuano a essere riutilizzati.

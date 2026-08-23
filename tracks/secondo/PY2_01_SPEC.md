# PY2-01 — Problem solving, algoritmi e flow chart

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 1–3;
- monte ore nominale: 9 ore;
- organizzazione reale: 2 ore teoria attiva + 1 ora laboratorio per settimana;
- prerequisiti: nessuna esperienza di programmazione;
- Python: non richiesto come prerequisito della UDA;
- output: lo studente sa analizzare, rappresentare, simulare e verificare un piccolo algoritmo prima di codificarlo.

## Perché questa UDA esiste

Il corso non deve insegnare a riconoscere sintassi Python senza saper risolvere un problema.

La prima soglia di competenza è:

```text
problema
→ dati e vincoli
→ risultato atteso
→ decomposizione
→ algoritmo
→ rappresentazione
→ trace
→ casi di test
```

Python arriva subito dopo, nella UDA PY2-02, come linguaggio con cui tradurre modelli già compresi.

---

# M00 — Come si risolve un problema con un computer

## Durata

Circa 1–2 ore distribuite nella prima settimana, integrate con M01.

## Obiettivi osservabili

Lo studente sa:

1. distinguere problema, algoritmo e programma;
2. individuare input e output in una specifica molto semplice;
3. riconoscere informazioni necessarie, inutili o mancanti;
4. descrivere una soluzione come sequenza finita di passi;
5. usare un esempio concreto per verificare se ha capito il problema;
6. distinguere almeno in modo intuitivo errore di comprensione, errore nell'algoritmo ed errore di esecuzione.

## Modello mentale

Un computer non "capisce il problema": esegue istruzioni.

Perciò il programmatore deve trasformare una richiesta vaga in una procedura sufficientemente precisa da poter essere eseguita e verificata.

## Problemi introduttivi candidati

- calcolare il resto dovuto da una piccola spesa;
- decidere se una temperatura supera una soglia;
- ordinare i passi per preparare una bevanda;
- trovare il maggiore tra pochi valori senza ancora scrivere codice;
- descrivere un percorso semplice per un robot su una griglia.

Il problema del robot può anticipare Romeo come dominio motivante senza usare ancora API o hardware.

## Misconception da cercare

- confondere "cosa voglio ottenere" con "come lo calcolo";
- assumere dati non presenti nella consegna;
- saltare passaggi perché "sono ovvi";
- scrivere già pseudo-codice Python invece di spiegare l'algoritmo;
- pensare che un esempio riuscito dimostri sempre la correttezza generale.

## Evidence

- breve analisi dati/input/output;
- sequenza di passi;
- un caso normale e un caso limite;
- spiegazione orale molto breve.

---

# M01 — Dal problema ai passi

## Obiettivi osservabili

Lo studente sa:

- leggere una specifica breve;
- elencare input, output e vincoli;
- decomporre un problema in passi;
- riconoscere un algoritmo ambiguo o non terminante;
- scrivere pseudocodice semplice e leggibile;
- costruire esempi e casi limite;
- eseguire un dry-run manuale su una sequenza lineare.

## Concetti

- specifica;
- input/output;
- stato iniziale e risultato;
- algoritmo;
- finitezza;
- determinismo operativo al livello richiesto dall'esercizio;
- decomposizione;
- pseudocodice;
- esempio, controesempio, edge case.

## Attività di teoria attiva

La lezione alterna spiegazioni brevi e micro-task:

```text
leggi una consegna
→ sottolinea input
→ cerchia output
→ segnala un vincolo
→ ordina passi mescolati
→ prova l'algoritmo con un esempio
```

## Activity candidate

### A — Observe/Trace

**Titolo:** `Ordina i passi`

Lo studente riceve una soluzione scomposta e deve:

- rimettere i passi nell'ordine corretto;
- prevedere l'output su un esempio;
- individuare un passaggio mancante.

### B — Controlled Change

**Titolo:** `Ripara un algoritmo ambiguo`

Viene fornito un pseudocodice volutamente incompleto/ambiguo. Lo studente modifica soltanto i punti necessari.

### C — Implement/Design

**Titolo:** `Dal testo all'algoritmo`

Da una specifica nuova, produce:

- input;
- output;
- passi;
- due casi di test.

### D — Debug/Diagnose

**Titolo:** `Perché questa procedura non funziona?`

Diagnosticare:

- un passo nell'ordine sbagliato;
- una variabile concettuale mai definita;
- un algoritmo che non copre un caso;
- una procedura che non termina.

## Grading boundary

Questa UDA è prevalentemente manuale/rubric-based.

Elementi deterministici eventualmente verificabili dalla piattaforma:

- presenza dei campi richiesti;
- ordine di una sequenza in esercizi chiusi;
- risultato di trace predefiniti.

Qualità della decomposizione e chiarezza restano valutazione docente.

---

# M02 — Sequenza, input/output e selezione nei diagrammi

## Obiettivi osservabili

Lo studente sa:

1. leggere i simboli fondamentali di un flow chart;
2. costruire sequenze con input, elaborazione e output;
3. rappresentare una condizione;
4. costruire selezione semplice e doppia;
5. rappresentare una selezione a più casi senza creare diagrammi inutilmente confusi;
6. seguire un diagramma passo-passo con dati concreti;
7. compilare una trace table elementare.

## Simboli core

- start/end;
- input/output;
- processing/assignment;
- decision;
- frecce di controllo.

I simboli avanzati non entrano finché non risolvono un bisogno reale.

## Flowchart Lab capability

Target futuro:

```text
flowchart.lab.v1
```

Funzioni minime necessarie per questo modulo:

- creare/nominare variabili;
- input;
- assegnamento/espressione;
- output;
- decisione booleana;
- rami true/false;
- step;
- variable watch;
- input deterministico;
- salvataggio artifact.

Fallback autorizzato finché la capability non è certificata:

```text
carta / template stampato / diagramma digitale manuale
+ trace table
+ rubric docente
```

Flowgorithm può essere usato come riferimento/companion Windows, non come requisito canonico.

## Attività candidate

### A — Trace

Seguire un diagramma e compilare:

| passo | dato/variabile | condizione | output |
|---|---|---|---|

### B — Controlled Change

Modificare una soglia o aggiungere un ramo a un diagramma già funzionante.

### C — Design

Problemi candidati:

- maggiore/minore tra due valori;
- tariffa semplice a soglia;
- classificazione elementare;
- validazione di un valore entro range.

### D — Debug

Errori da diagnosticare:

- ramo che non porta a fine;
- output posto prima del calcolo;
- condizione invertita;
- casi non coperti;
- rami logicamente sovrapposti quando dovrebbero essere esclusivi.

## Ponte futuro verso Python

Non mostrare subito la traduzione automatica completa.

Dopo che il costrutto è compreso, si può mostrare la corrispondenza concettuale:

```text
decision node
    ↓
if / else
```

senza trasformare il Flowchart Lab in generatore di soluzioni.

---

# M03 — Iterazione e annidamento nei diagrammi

## Obiettivi osservabili

Lo studente sa:

- riconoscere quando un'azione deve essere ripetuta;
- rappresentare un ciclo controllato da condizione;
- rappresentare un ciclo controllato da contatore a livello algoritmico;
- identificare inizializzazione, condizione, corpo e aggiornamento;
- prevedere la terminazione;
- usare una selezione dentro un ciclo;
- usare un ciclo dentro una selezione;
- leggere un primo esempio di cicli annidati;
- progettare casi che evidenziano off-by-one o mancata terminazione.

## Concetti

- iterazione;
- stato che cambia;
- condizione di continuazione/uscita;
- contatore;
- accumulatore concettuale;
- sentinella concettuale;
- terminazione;
- annidamento;
- trace ripetuta.

## Problemi candidati

- ripetere una domanda finché l'input è valido;
- sommare N valori a livello algoritmico;
- contare quanti dati soddisfano una condizione;
- stampare/descrivere una griglia;
- controllare una sequenza di celle in un percorso robotico;
- produrre una piccola tabella con due livelli di ripetizione.

## Activity candidate

### A — Trace loop

Prevedere quante volte viene eseguito il corpo e lo stato finale.

### B — Controlled Change

Cambiare limite/condizione mantenendo invariata la struttura.

### C — Design

Costruire flow chart per:

- validazione ripetuta;
- contatore;
- selezione dentro ciclo.

### D — Debug

Esempi:

- ciclo infinito;
- aggiornamento mancante;
- condizione invertita;
- off-by-one;
- variabile inizializzata nel punto sbagliato.

### E — Mini-project

**Missione algoritmica:** progettare una piccola missione su griglia/robot simulato a livello di algoritmo, senza API Python.

Output possibile:

- specifica sintetica;
- diagramma;
- trace su almeno due casi;
- elenco di casi limite;
- spiegazione della scelta dei costrutti.

Romeo può essere usato soltanto come scenario visuale/concettuale; nessun requisito del runtime `romeo-sim` in questa UDA.

---

# Piano delle tre settimane

## Settimana 1

### Ora teoria attiva 1

- diagnostic non valutativo;
- problema vs algoritmo vs programma;
- input/output/vincoli;
- micro-esercizi di classificazione.

### Ora teoria attiva 2

- M01 decomposizione;
- ordinamento passi;
- pseudocodice;
- casi normali/limite;
- Activity A/B breve.

### Ora laboratorio

- problemi C/D;
- trace manuale;
- consegna di un algoritmo semplice.

## Settimana 2

### Ora teoria attiva 1

- simboli flow chart;
- sequenza/input/output;
- trace.

### Ora teoria attiva 2

- selezione;
- casi esclusivi/indipendenti a livello algoritmico;
- debugging di diagrammi.

### Ora laboratorio

- Flowchart Lab se disponibile;
- altrimenti template/carta + evidence manuale;
- Activity M02 A–D.

## Settimana 3

### Ora teoria attiva 1

- iterazione;
- terminazione;
- contatore/condizione.

### Ora teoria attiva 2

- annidamento;
- selezione + ciclo;
- primi cicli annidati;
- casi limite/off-by-one.

### Ora laboratorio

- Activity M03;
- mini-project E;
- exit checkpoint.

---

# Exit checkpoint UDA

Prima di passare a Python lo studente dovrebbe riuscire, con problemi semplici, a:

- identificare input/output;
- scrivere passi ordinati;
- produrre pseudocodice leggibile;
- disegnare sequenza + selezione + iterazione;
- seguire il proprio algoritmo a mano;
- individuare almeno un caso limite;
- spiegare perché il diagramma termina;
- riconoscere un errore evidente in un algoritmo altrui.

Non è richiesta perfezione grafica del diagramma.

---

# Valutazione formativa

Questa UDA non necessita necessariamente di un voto principale.

Evidence consigliate:

- 2–3 micro-trace;
- 1 algoritmo da specifica;
- 1 flow chart con selezione;
- 1 flow chart con ciclo;
- 1 debug task;
- mini-project finale o equivalente.

I risultati alimentano recupero e differenziazione prima di entrare nella sintassi Python.

---

# Remediation

Per studenti in difficoltà:

1. ridurre il problema a sequenze lineari;
2. usare valori concreti e carte/passaggi fisici;
3. trace con una sola variabile;
4. introdurre selezione con domande sì/no;
5. introdurre loop come ritorno grafico controllato;
6. evitare annidamento finché singoli costrutti non sono stabili.

# Enrichment

Per studenti rapidi:

- confrontare due algoritmi equivalenti;
- cercare casi che rompono una soluzione apparentemente corretta;
- ridurre duplicazioni nel diagramma;
- primo confronto intuitivo tra soluzione con una scansione e soluzione con doppi cicli;
- formalizzare meglio pre/post-condizioni.

---

# Fonti di progettazione

## Principale pedagogica

- Allen Downey, *Think Python / Pensare in Python*: problem solving, modello di esecuzione, debugging e progressione beginner.

## Gap/algoritmi

- Pluralsight, *An Introduction to Algorithmics*: esempi e intuizioni su algoritmi/costo senza anticipare formalismi pesanti.

## Controllo curricolare

- `tracks/secondo/MODULE_MAP.md`;
- `tracks/secondo/COURSE_DESIGN.md`;
- `doc/CURRICULUM_ROADMAP.md`.

Le fonti sono riferimenti per produrre materiale originale; non copiare testi o esercizi licensed.

---

# Dipendenze piattaforma

## Core didattico

Nessuna dipendenza da Python o Romeo.

## Capability target

```text
flowchart.lab.v1
```

## Fallback temporaneo

```text
manual-flowchart-evidence
```

Il Content Pack 1.0 non deve dichiarare Flowchart Lab come disponibile finché TheBitLab non ha implementato/collaudato la capability.

---

# Criteri per passare dalla SPEC alla lesson

Prima di dichiarare PY2-01 pronta per produzione:

- Flowchart artifact/UX boundary deciso;
- simboli/convenzioni del corso congelati;
- Activity IDs definiti;
- rubriche minime definite;
- almeno un dry-run docente delle tre settimane;
- verifica che il carico reale stia nelle 9 ore;
- fonti/provenienza registrate nel Content Pack.

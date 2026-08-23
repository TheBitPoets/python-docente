# Python — track secondo anno (DRAFT)

> Stato: architettura candidata, non ancora congelata.
>
> Dettaglio dei moduli: [`MODULE_MAP.md`](MODULE_MAP.md).

## Profilo

- durata nominale: **33 settimane**;
- carico: **3 ore/settimana = 99 ore nominali**;
- ingresso: nessun prerequisito di programmazione;
- uscita: programmazione strutturata solida, decomposizione in funzioni, stringhe e strutture dati fondamentali, persistenza/error handling essenziali, classi e oggetti fondamentali.

Il corso deve produrre studenti capaci non solo di ricordare sintassi, ma di:

1. comprendere un problema;
2. formalizzare una soluzione;
3. prevedere e tracciare l'esecuzione;
4. scegliere costrutti e strutture dati appropriati;
5. implementare una soluzione leggibile;
6. testarla e fare debugging;
7. confrontare alternative;
8. spiegare perché la soluzione funziona e quali trade-off presenta.

## Principio: curriculum spirale

Il percorso non aspetta un singolo capitolo per introdurre competenze trasversali.

- **test case** dal primo algoritmo;
- **trace/manual execution** dal primo flow chart;
- **debugging** dal primo script;
- **funzioni** introdotte in forma minima nei primi programmi e poi approfondite in una UDA dedicata;
- **naming/leggibilità** da subito;
- **efficienza intuitiva** dentro loop e strutture dati;
- **spiegazione delle scelte** in ogni problema significativo.

Ordine di priorità:

```text
correttezza
→ comprensibilità
→ decomposizione e modello dati
→ robustezza
→ efficienza quando rilevante
```

## Budget realistico

Le 99 ore sono nominali. Il design non assume 99 ore nette di nuovo programma.

Tre settimane sono checkpoint esplicitamente flessibili:

- settimana 17 — consolidamento controllo del flusso/funzioni;
- settimana 24 — laboratorio strutture sequenziali;
- settimana 33 — capstone, recupero o enrichment.

Queste **9 ore di buffer esplicito** si aggiungono alle verifiche/pratiche integrate nelle UDA. Nessun concetto indispensabile viene introdotto soltanto nella settimana 33.

## Piano 33 settimane

| Settimane | Blocco | Ore nominali | Focus |
|---|---|---:|---|
| 1–3 | PY2-01 Problem solving e algoritmi | 9 | decomposizione, pseudocodice, flow chart, trace, casi di test, selezione/iterazione nei diagrammi |
| 4–5 | PY2-02 Primi programmi Python | 6 | ambiente, `print`/`input`, tipi, variabili, operatori, conversioni, primi errori, prime piccole funzioni |
| 6–8 | PY2-03 Selezione | 9 | bool, confronti, `if/elif/else`, condizioni composte/annidate, validazione, confronto alternative |
| 9–12 | PY2-04 Iterazione e pattern | 12 | `while`, `for/range`, sentinelle, contatori, accumulatori, ricerca/min/max, annidamento, scelta `for`/`while` |
| 13–16 | PY2-05 Funzioni e decomposizione | 12 | parametri, `return`, scope, composizione, top-down, `assert`, test e refactoring |
| 17 | Checkpoint A | 3 | recupero, verifica pratica o mini-progetto; nessun prerequisito nuovo |
| 18–20 | PY2-06 Stringhe | 9 | sequenze, indicizzazione, slicing, metodi, ricerca, parsing e problemi testuali |
| 21–23 | PY2-07 Liste e tuple | 9 | mutabilità, metodi, alias/copia, algoritmi, tuple, matrici, scelta struttura |
| 24 | Checkpoint B | 3 | laboratorio/recupero/verifica su stringhe e strutture sequenziali |
| 25–27 | PY2-08 Set e dizionari | 9 | membership, lookup, frequenze, record, strutture annidate, scelta/modellazione dei dati |
| 28 | PY2-09 File ed errori | 3 core | `with/open`, testo, UTF-8, `pathlib` introduttivo, `try/except` essenziale; estendibile se c'è margine |
| 29–32 | PY2-10 Classi e oggetti | 12 | classi, istanze, attributi, metodi, `__init__`, stato/comportamento, composizione, mini-capstone |
| 33 | Checkpoint C | 3 | finalizzazione capstone, recupero oppure enrichment |

Totale nominale: **99 ore**.

## Ritmo indicativo delle 3 ore

Non è una gabbia, ma il default progettuale è:

```text
30–45 min   nuovo concetto / modello mentale
20–30 min   trace / esempi / domande
45–60 min   guided coding / Activity A-B
45–60 min   problem solving / Activity C-D
15–30 min   recap, confronto soluzioni, evidence
```

Alcune settimane saranno invece interamente laboratorio, verifica, recupero o mini-progetto.

## Progressione algoritmica obbligatoria

### Prima del Python

Lo studente deve saper rappresentare in flow chart:

- sequenza;
- input/output;
- selezione semplice;
- selezione doppia;
- selezione multipla;
- ciclo pre-condizionale;
- ciclo controllato da contatore;
- selezione dentro un ciclo;
- ciclo dentro una selezione;
- cicli annidati.

### Durante tutto il corso

Per problemi significativi chiedere periodicamente:

```text
1. dati in ingresso
2. output
3. vincoli
4. esempi/casi limite
5. algoritmo/pseudocodice
6. eventuale flow chart
7. trace manuale
8. codice Python
9. test
10. spiegazione delle scelte
```

Non è necessario produrre sempre tutti gli artefatti: vengono scelti in base all'obiettivo della Activity.

## Selezione: soglia minima

Lo studente deve distinguere:

```python
if a:
    ...
if b:
    ...
```

da:

```python
if a:
    ...
elif b:
    ...
else:
    ...
```

Deve capire quando le condizioni sono indipendenti e quando sono mutuamente esclusive.

Deve saper costruire e semplificare condizioni con `and`, `or`, `not` e confronti, evitando annidamenti inutili.

`match/case` non sostituisce questa padronanza: è un'eventuale estensione successiva.

## Iterazione: soglia minima

Lo studente deve padroneggiare:

- `while` quando la durata dipende da una condizione;
- `for` quando si itera su una sequenza/intervallo;
- contatore;
- accumulatore;
- valore sentinella;
- min/max progressivo;
- ricerca lineare;
- flag con consapevolezza;
- cicli annidati;
- `if` dentro `for/while`;
- `for/while` dentro rami condizionali;
- controllo di loop infiniti e off-by-one;
- uso disciplinato di `break`/`continue`.

Non basta riconoscere il costrutto: deve saper scegliere tra `for` e `while` e motivarlo.

## Funzioni: due passaggi

### Introduzione precoce

Nei primi programmi:

- chiamare built-in;
- definire una funzione piccola;
- parametro/argomento;
- `return` semplice;
- distinguere calcolo da output.

### Padronanza nella UDA PY2-05

Prima delle strutture dati complesse, lo studente deve saper:

- estrarre una funzione da codice duplicato;
- restituire risultati invece di stampare tutto;
- separare acquisizione dati, logica e presentazione;
- chiamare funzioni da altre funzioni;
- comprendere scope locale essenziale;
- progettare un piccolo programma top-down;
- usare casi di test e `assert` semplici;
- fare refactoring di una soluzione monolitica.

## Strutture dati: criterio di scelta

La domanda ricorrente sarà: **quali operazioni dobbiamo fare sui dati?**

| Esigenza dominante | Struttura candidata |
|---|---|
| testo | `str` |
| sequenza ordinata modificabile | `list` |
| sequenza/record immutabile semplice | `tuple` |
| elementi unici / membership | `set` |
| associazione chiave → valore / lookup | `dict` |

Gli studenti devono anche combinare strutture:

- lista di tuple;
- lista di dizionari;
- dizionario di liste;
- dizionario di dizionari;
- matrice come lista di liste.

L'obiettivo non è memorizzare combinazioni, ma modellare i dati in funzione del problema.

## Efficienza nel secondo anno

Non è un corso formale di analisi asintotica, ma vengono introdotte intuizioni operative:

- una scansione completa cresce con la quantità di dati;
- due cicli annidati sulla stessa collezione possono crescere molto più velocemente;
- un dizionario/set è spesso più adatto di una scansione ripetuta quando il problema dominante è lookup/membership;
- evitare lavoro ripetuto dentro un loop quando può essere calcolato una volta;
- scegliere prima un modello dati corretto;
- leggibilità e semplicità restano criteri fondamentali: una micro-ottimizzazione non giustifica codice incomprensibile.

## File/errori: core deliberatamente piccolo

La persistenza è utile ma non deve impedire di arrivare bene all'OOP.

Core obbligatorio:

- file di testo;
- `with open(...)`;
- lettura/scrittura essenziale;
- UTF-8;
- `pathlib` introduttivo;
- `try/except` per errori prevedibili.

Extension:

- CSV/JSON;
- file binari;
- eccezioni più articolate.

Questi temi continuano nello Stage B/C.

## OOP: confine di seconda

### Core obbligatorio

- perché introdurre un oggetto;
- passaggio da record/dict a modello con comportamento;
- classe vs istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato + comportamento;
- più istanze indipendenti;
- composizione semplice;
- responsabilità di una classe;
- test del comportamento;
- mini-capstone.

### Estensione se il gruppo è pronto

- `__str__` / `__repr__`;
- property introduttiva;
- ereditarietà semplice;
- dataclass come confronto dopo aver compreso una classe esplicita.

### Fuori dal core di seconda

- multiple inheritance/MRO;
- descriptors/metaclasses;
- ABC/protocols avanzati;
- decorators avanzati;
- iterator protocol custom;
- async/concurrency;
- packaging professionale.

## Valutazione

Distribuire le evidenze durante tutto l'anno:

- flow chart/pseudocodice;
- trace/previsione dell'esecuzione;
- esercizi di implementazione;
- debug di codice difettoso;
- confronto e refactoring;
- scelta del costrutto/struttura dati motivata;
- verifiche pratiche a tempo;
- mini-progetti;
- capstone OOP.

### Rubrica trasversale candidata

- comprensione del problema;
- correttezza;
- qualità dell'algoritmo;
- scelta dei costrutti;
- decomposizione;
- scelta/modellazione dei dati;
- leggibilità/naming;
- gestione casi limite;
- test/debugging;
- capacità di spiegazione.

La prestazione viene valutata in modo proporzionato all'obiettivo: non ogni esercizio usa tutti i criteri.

## Activity mix

Tassonomia condivisa con TPSI5:

```text
A Observe / Trace
B Controlled Change
C Implement
D Debug / Diagnose
E Mini-project
F Integrated Product / Capstone
```

Nel primo nucleo prevalgono A/B/C/D. E/F aumentano con funzioni, strutture dati e OOP.

## `friedpython`

Il materiale esistente entra soprattutto nelle UDA PY2-06, PY2-07, PY2-08 e, selettivamente, PY2-09 dopo audit.

Non va copiato in blocco e non determina l'ordine del corso. La provenienza viene registrata rispetto allo snapshot legacy scelto.

## Progetto longitudinale

Ancora da congelare.

Architettura raccomandata: **micro-progetti indipendenti nel primo nucleo + possibile spine longitudinale dal momento in cui gli studenti padroneggiano funzioni**.

Romeo resta un candidato forte per il secondo semestre, ma il corso deve essere completabile senza hardware fisico. Qualunque uso di Romeo richiede quindi simulazione/boundary testabile in laboratorio, CI e/o TheBitLab.

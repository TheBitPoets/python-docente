# Python curriculum — decisioni approvate 2026/27

> Stato: decisioni di design approvate. Questo documento **non** equivale ancora al `CURRICULUM_FREEZE` del Content Pack 1.0.

## D1 — Ambiente didattico unico

Tutti i corsi TheBitPoets devono usare il **Classroom Environment gestito da TheBitLab / 2cornot2c** come percorso supportato per gli studenti, sia a scuola sia sui PC personali.

Non sono ammessi prerequisiti impliciti del tipo “installa manualmente sul PC il tool X” se quel tool non fa parte del percorso installa/ripara di TheBitLab.

Il modello corrente prevede:

- host Windows/macOS;
- profilo Docker student-dev leggero per macchine con poca RAM;
- VM Linux grafica per il profilo completo;
- workspace condiviso;
- runner di grading separato;
- runtime plugin esterni per capability specialistiche come `romeo-sim`.

Blocker piattaforma: `TheBitPoets/2cornot2c#753`.

## D2 — Python baseline del track di seconda

Il Content Pack iniziale usa **Python 3.12** come baseline didattica certificata, coerente con l'attuale student-dev TheBitLab (`3.12.3`) e con la versione raccomandata dal progetto 2cornot2c.

Regole:

- niente feature obbligatorie introdotte solo in Python 3.13/3.14;
- il codice può essere testato anche su versioni più recenti come forward-compatibility;
- la versione effettiva del laboratorio appartiene al profilo ambiente TheBitLab, non al curriculum concettuale.

## D3 — Orario reale: 2 teoria + 1 laboratorio

Il secondo anno ha tre ore settimanali:

- **2 ore di teoria/classe**;
- **1 ora di laboratorio**.

Il corso resta volutamente pratico. “Ora di teoria” non significa lezione frontale continua: quando disponibili i portatili si usano REPL, trace, micro-esercizi, guided coding, debugging, confronto tra soluzioni e brevi Activity.

L'ora di laboratorio privilegia esercizi più lunghi, Activity C/D/E/F, consegne, Romeo simulato, prove pratiche e progetto.

## D4 — REPL → script → editor

Progressione approvata:

1. primi concetti con il REPL standard `python`;
2. transizione precoce a file `.py`;
3. VS Code come editor di lungo periodo quando la sua installazione/configurazione è gestita dal Classroom Environment;
4. debugger introdotto solo quando è didatticamente utile;
5. IPython è opzionale e non può essere requisito del core finché non fa parte del profilo ambiente certificato.

## D5 — Flow chart

Il flow chart è **core curricolare**.

Flowgorithm è utile come riferimento funzionale ma non può essere dipendenza canonica perché è Windows-only.

Target architetturale: **Flowchart Lab cross-platform gestito da TheBitLab**, browser-based e salvabile nel workspace studente.

Capability desiderate:

- sequenza, input/output, selezione, cicli, funzioni;
- annidamento;
- esecuzione/step-by-step;
- variable watch;
- input/output deterministico;
- artifact versionabile;
- export SVG/immagine;
- collegamento pseudocodice/Python solo quando pedagogicamente opportuno;
- validazione strutturale automatica dove deterministica;
- qualità progettuale valutata con rubric/manual checks.

Blocker piattaforma: `TheBitPoets/2cornot2c#753`.

## D6 — Romeo

Romeo è approvato come **filo applicativo ricorrente**, non come curriculum alternativo.

Modello:

```text
problemi generali e micro-progetti
+ missioni Romeo simulate ricorrenti
+ capstone OOP con Romeo simulato
```

Vincoli:

- ogni concetto Python deve avere anche esercizi generali/non-Romeo;
- hardware fisico mai necessario per completare il core;
- usare `romeo-sim` attraverso il boundary TheBitLab;
- non importare nel secondo anno beginner la parte networking/FastAPI/WebSocket dell'attuale curriculum Romeo year 2.

Mapping dettagliato: `python-docente#4`.

## D7 — Git nel secondo anno

Git entra in forma minima nel secondo anno, senza diventare un corso separato.

Core proposto:

- concetto di storico/versione;
- `status`;
- `diff`;
- `add`;
- `commit`;
- lettura semplice della history.

Materiale docente esistente verrà integrato successivamente. Branching/collaboration avanzata resta ai livelli successivi.

## D8 — OOP obbligatoria in seconda

La OOP è parte del core, non enrichment finale.

Obbligatorio:

- classe vs istanza;
- attributi;
- `self`;
- `__init__`;
- metodi;
- stato + comportamento;
- istanze indipendenti;
- composizione semplice;
- responsabilità di classe;
- mini-capstone.

`__str__/__repr__` è altamente raccomandato. Ereditarietà semplice, properties e dataclass restano enrichment finché il calendario non dimostra di sostenerle senza comprimere i fondamentali.

## D9 — Valutazioni minime

Per ogni quadrimestre devono essere previste almeno:

- **1 prova teorica/scritta**;
- **1 prova pratica o pratica/scritta**.

Il corso raccoglie comunque evidenze formative più frequenti: trace, flow chart, coding, debug, spiegazione delle scelte, mini-progetti e Activity.

Design dettagliato: `python-docente#5`.

## D10 — Policy AI

Nei fondamenti e nelle verifiche core non è consentito usare AI generativa per produrre la soluzione.

Più avanti sono ammesse Activity controllate di AI-assisted review/debugging, con obbligo per lo studente di:

- verificare;
- testare;
- correggere;
- spiegare il codice e le scelte.

L'AI non sostituisce la capacità di progettare algoritmo, trace e soluzione.

## D11 — Standard di delivery

Riutilizzare lo standard maturato con TPSI5, adattato a studenti più giovani:

- lesson canoniche;
- slide modulari meno dense e più visuali;
- student guide;
- teacher guide;
- Activity A–F;
- starter;
- solution/reference;
- rubric/manual evidence;
- CI/Quality;
- TheBitLab handoff;
- curriculum freeze separato dal delivery changelog.

## Decisioni ancora bloccanti prima del freeze

Restano da chiudere:

1. contratto Classroom Environment cross-course (`2cornot2c#753` / `python-docente#2`);
2. architettura Flowchart Lab;
3. profilo Python/VS Code certificato sui due ambienti Docker-light e VM grafica;
4. Activity/runner contract Python TheBitLab;
5. mapping Romeo dettagliato;
6. calendario/rubriche delle verifiche;
7. mapping fonti → UDA → moduli.

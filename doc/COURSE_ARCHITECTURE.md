# Python curriculum — architettura del corso (DRAFT)

> Stato: proposta da discutere. Questo documento definisce **come** è costruito il corso, non congela ancora i contenuti.

## 1. Obiettivo

Costruire un curriculum Python a più livelli che:

- parta da zero assoluto;
- insegni prima di tutto **problem solving algoritmico**;
- renda lo studente capace di tradurre un problema in passi, pseudocodice/flow chart, casi di test e infine codice;
- sviluppi padronanza reale di selezione, iterazione, annidamento e composizione dei costrutti;
- insegni a scegliere la struttura dati e il costrutto più adeguati per correttezza, leggibilità e costo computazionale quando rilevante;
- arrivi nel track di secondo anno a classi e programmazione a oggetti di base;
- continui, senza cambiare architettura, verso Python professionale negli anni successivi.

## 2. Due livelli separati

### Curriculum generale

È la mappa completa delle competenze Python. Non è vincolata a un singolo anno scolastico.

### Track didattici

Selezionano una porzione ordinata del curriculum per un contesto specifico.

Il primo track è:

```text
Secondo anno
33 settimane
3 ore/settimana
99 ore nominali
nessun prerequisito di programmazione
```

Il confine del track viene dichiarato esplicitamente; gli argomenti avanzati non vengono eliminati, ma restano fuori dal percorso obbligatorio di seconda.

## 3. Unità logiche

La gerarchia proposta è:

```text
Curriculum
└── Stage
    └── UDA
        └── Modulo
            ├── lesson canonica
            ├── slide
            ├── demo/esempi
            ├── Activity
            ├── starter
            ├── solution/reference
            ├── test/checklist
            └── rubric/evidence
```

### Stage

Macro-livello di maturità:

1. **Foundation / Secondo anno** — dal problem solving alla OOP fondamentale.
2. **Core Python** — modello dati, moduli/package, robustezza, OOP avanzata.
3. **Professional Python** — typing, testing, tooling, I/O strutturato, DB, API, async, packaging, performance e architettura.
4. **Applied/Capstone** — progetti reali e specializzazioni.

## 4. Contratto di ogni modulo

Ogni modulo definitivo dovrebbe dichiarare almeno:

- prerequisiti;
- obiettivi osservabili;
- concetti e vocabolario;
- modello mentale;
- algoritmo/pseudocodice prima del codice quando applicabile;
- esempi minimi;
- esempi composti/annidati;
- errori comuni e debugging;
- criteri di scelta tra alternative;
- cenno al costo computazionale quando utile;
- esercizi graduati;
- Activity collegate;
- checkpoint formativo;
- riferimenti alle fonti;
- collegamento al progetto longitudinale, se approvato.

## 5. Metodo didattico

Il ciclo fondamentale è:

```text
problema
→ comprensione dei dati e del risultato atteso
→ decomposizione
→ algoritmo
→ pseudocodice / flow chart
→ casi di test
→ trace/manual dry-run
→ implementazione Python
→ esecuzione
→ debugging
→ refactoring
→ spiegazione delle scelte
```

L'obiettivo non è produrre codice che "sembra funzionare", ma sviluppare la capacità di progettare, verificare e spiegare una soluzione.

## 6. Progressione delle Activity

Riutilizziamo la tassonomia maturata in TPSI5:

- **A — Observe/Trace**: esegui, traccia, prevedi l'output, spiega.
- **B — Controlled Change**: modifica un programma esistente con vincoli precisi.
- **C — Implement**: realizza autonomamente una soluzione da specifica.
- **D — Debug/Diagnose**: trova e correggi errori logici, sintattici o di progettazione.
- **E — Mini-project**: combina più competenze in un artefatto piccolo ma completo.
- **F — Integrated product / Capstone**: prodotto integrato con evidenze e rubrica.

Per i principianti A e B hanno peso elevato; C e D crescono progressivamente; E e F arrivano dopo che i costrutti necessari sono stati realmente esercitati.

## 7. Competenza trasversale: scegliere, non solo conoscere

Per ogni famiglia di costrutti lo studente deve arrivare a rispondere a domande come:

- perché `if/elif/else` invece di più `if` indipendenti?
- perché `for` invece di `while`, o viceversa?
- quando un ciclo annidato è necessario e quando indica una progettazione migliorabile?
- perché una lista, una tupla, un set o un dizionario?
- quando una struttura annidata è naturale e quando è preferibile introdurre un oggetto?
- quando estrarre una funzione?
- quando la soluzione è corretta ma poco leggibile?
- quale operazione cresce linearmente, quadraticamente o resta circa costante rispetto alla dimensione dei dati?

Nel secondo anno la complessità viene introdotta in modo intuitivo e operativo; la formalizzazione può proseguire nei track avanzati.

## 8. Teoria, esempi ed esercizi

Ogni UDA deve contenere tre strati distinti:

### Theory

Spiegazione progressiva e rigorosa, scritta per studenti.

### Microscopes / demo

Programmi molto piccoli per isolare un comportamento.

### Problems

Problemi autentici che richiedono scelta e composizione.

La banca `friedpython` viene trattata come materiale grezzo: un esempio esistente può diventare microscope, Activity, esercizio, verifica o reference, ma solo dopo audit.

## 9. Valutazione

Il modello target combina:

- trace/previsione dell'esecuzione;
- costruzione di algoritmi e flow chart;
- coding;
- debugging;
- spiegazione orale/scritta delle scelte;
- esercizi a tempo;
- mini-progetti;
- capstone;
- rubriche per correttezza, decomposizione, leggibilità, test e scelta dei costrutti.

Non tutto deve essere autograded. TheBitLab viene usato per ciò che può essere verificato in modo affidabile; progettazione, diagrammi, spiegazioni e alcune decisioni architetturali restano rubric/manual checks.

## 10. Materiale studente

Previsto:

```text
student/README.md
content/python/*.md
slides/python/*
activities/python/*/student/
starters/
checklist
rubriche pubbliche quando appropriate
```

Il percorso studente deve essere navigabile senza conoscere la struttura interna del repository.

## 11. Materiale docente

Previsto:

```text
teacher/README.md
teacher/LESSON_RUNBOOK.md
teacher/ASSESSMENT_GUIDE.md
teacher/THEBITLAB_HANDOFF.md
solution/reference
rubriche complete
misconception notes
alternative explanations
extension/remediation paths
```

## 12. Slide

Come in TPSI5:

- sorgente versionato;
- deck per modulo/UDA;
- build riproducibile HTML/PDF/PPTX;
- slide come supporto alla lezione, non sostituto della dispensa.

## 13. TheBitLab

Il corso deve essere progettato **TheBitLab-aware fin dall'inizio**, ma non dipendere da capability inesistenti.

Regole:

- Activity canoniche versionate;
- runner deterministico quando appropriato;
- test pubblici/privati secondo il contratto;
- fallback espliciti quando una capability non esiste;
- nessun finto autograding di diagrammi, spiegazioni o qualità progettuale.

## 14. Progetto longitudinale

Il curriculum deve supportare un progetto crescente, ma il progetto non è ancora scelto.

Candidati da valutare:

- **Romeo / robot simulato**: forte motivazione e ponte verso robotica, ma richiede un adapter/simulatore che non renda l'hardware un prerequisito.
- applicazione CLI gestionale;
- gioco/avventura testuale;
- dataset/problem domain scolastico;
- combinazione di micro-progetti + capstone finale.

La scelta resta una decisione di curriculum e viene registrata in `doc/OPEN_DECISIONS.md`.

## 15. Fonti

Le fonti devono essere catalogate con:

- titolo/autore;
- edizione/versione;
- lingua;
- URL/repository se pubblico;
- licenza;
- capitoli rilevanti;
- UDA/moduli a cui contribuiscono;
- tipo di uso: riferimento, adattamento, esercizi, approfondimento.

`Pensare da informatico` è fonte primaria per la progressione iniziale. La documentazione Python moderna è fonte normativa per il linguaggio.

## 16. Governance

Prima del primo Content Pack approvato:

- architettura;
- roadmap;
- track secondo anno;
- tassonomia Activity;
- fonti;
- progetto longitudinale;
- grading policy;
- versione Python target;
- integrazione TheBitLab

devono essere esplicitamente decisi.

Dopo il freeze, separare come in TPSI5:

```text
curriculum-change
vs
errata / clarification / slides / lab-fix / setup
```

# Python secondo anno — Activity strategy (DRAFT)

Il corso usa Activity schema 1.0 e tassonomia A–F già accettate da TheBitLab.

## Obiettivo

Portare gradualmente lo studente da:

```text
leggere/eseguire
→ prevedere
→ modificare
→ implementare
→ fare debug
→ progettare
→ integrare
```

senza saltare direttamente a “scrivi tutto da zero”.

---

# A — Observe / Trace

Uso forte nel primo quadrimestre, ma presente tutto l'anno.

Esempi:

- prevedi output;
- completa tabella variabili;
- esegui flow chart step-by-step;
- osserva cosa cambia tra due `if` indipendenti e `if/elif`;
- traccia un loop;
- osserva alias vs copia;
- osserva stato di due istanze;
- osserva trajectory/event log Romeo.

Autograding possibile solo per risultati deterministici; spiegazioni e interpretazione restano manuali quando necessario.

# B — Controlled Change

Lo studente riceve un programma/diagramma funzionante o quasi e applica una modifica precisa.

Esempi:

- aggiungi un ramo;
- cambia condizione di terminazione;
- parametrizza una funzione;
- sostituisci lista con set dove richiesto;
- aggiungi un metodo a una classe;
- modifica una missione Romeo.

Serve a isolare un concetto nuovo senza sovraccaricare il problem solving.

# C — Implement

Costruzione autonoma da specifica.

La specifica deve indicare outcome e vincoli senza trasformarsi in pseudocodice completo.

Progressione:

```text
piccolo problema numerico
→ selezione
→ loop
→ funzione
→ stringa/struttura dati
→ modello composto
→ classe/oggetto
```

# D — Debug / Diagnose

Obbligatoria in ogni grande UDA.

Categorie:

- syntax/runtime;
- logica;
- condizioni;
- off-by-one;
- loop infinito;
- return/stampa;
- scope/globali;
- mutabilità/alias;
- dict/missing key;
- file/path;
- stato oggetto;
- regressione introdotta da una modifica.

Lo studente deve spesso produrre non solo il fix ma una diagnosi breve.

# E — Mini-project

Entra dopo che lo studente padroneggia funzioni e cresce nel secondo quadrimestre.

Caratteristiche:

- 1–3 ore circa;
- più concetti combinati;
- specifica non completamente proceduralizzata;
- test/checklist;
- breve reflection/design note.

Esempi candidati:

- analizzatore di testo;
- registro/mini-gestionale in memoria;
- elaborazione di dati tabellari;
- missione Romeo composta;
- piccolo tool file-based.

# F — Integrated Product / Capstone

Usato per M30/checkpoint finale.

Richiede almeno:

- analisi;
- decomposizione;
- funzioni/metodi;
- strutture dati;
- classi/oggetti;
- test;
- casi limite;
- spiegazione delle scelte;
- evidence riproducibile.

Romeo simulato è candidato principale, ma deve esistere un capstone generale equivalente.

---

# Mix per fase

## Settimane 1–8

Prevalenza:

```text
A > B > C ≈ D
```

E molto flow chart/trace.

## Settimane 9–16

```text
A/B/C/D bilanciate
+ primo E al checkpoint A
```

## Settimane 18–27

```text
C/D > A/B
+ E regolari
```

## Settimane 28–33

```text
C/D/E
→ F
```

---

# Evidence types

## Deterministiche / candidate autograding

- stdout/return;
- file prodotto;
- funzione/API;
- casi di test;
- stato finale di una struttura;
- trajectory/event/final state Romeo;
- schema valido Flowchart Lab;
- vincoli strutturali semplici.

## Manual/rubric

- qualità algoritmo;
- qualità flow chart;
- motivazione costrutto;
- leggibilità oltre regole banali;
- decomposizione;
- scelta struttura dati;
- responsabilità OOP;
- spiegazione orale/scritta;
- trade-off.

TheBitLab non deve trasformare questi ultimi in score automatici fittizi.

---

# Activity bundle

Forma target:

```text
activity.json
student/
starter/
examples/        # se realmente pubblici
fixtures/        # se pubbliche
visible_tests/   # se opportuni
teacher/
solution/
tests/           # hidden grading
```

Student/teacher/grading separation è obbligatoria.

# Flow chart Activities

Bloccate sull'architettura `Flowchart Lab` di `2cornot2c#753`.

Target artifact:

```text
algorithm.flow.json   # nome/schema da definire
```

Possibili checks deterministici:

- schema;
- start/end;
- nodi raggiungibili;
- presenza di decision/loop richiesti;
- input fixture → output atteso se il diagramma è eseguibile.

Checks manuali:

- algoritmo sensato;
- chiarezza;
- annidamento non accidentale;
- corrispondenza con la specifica.

# Python Activities

Baseline iniziale: Python 3.12.

Il runner deve poter:

- eseguire file/script;
- importare funzioni da student submission;
- passare input deterministico;
- verificare return/stdout/file;
- imporre timeout e limiti;
- impedire rete/segreti per default;
- distinguere visible vs hidden tests;
- produrre feedback didattico senza rivelare test riservati.

Contratto preciso bloccato su `python-docente#2` / `2cornot2c#753`.

# Romeo Activities

Usare runtime plugin `romeo-sim`.

Una missione deve dichiarare:

- obiettivo Python;
- scenario;
- API consentita;
- evidence del runtime;
- fallback/general exercise equivalente.

Hardware fisico è enrichment separato.

# Git evidence

Quando Git entra nel corso, alcuni E/F possono chiedere:

- almeno N commit significativi;
- messaggi sensati;
- diff comprensibile;
- nessuna solution/history artificiale.

Non valutare la capacità Git avanzata nel secondo anno.

# AI policy nelle Activity

Tag concettuale previsto:

```text
ai_policy: forbidden | review-only | allowed-with-evidence
```

La sintassi effettiva dipende dal contratto piattaforma.

Default secondo anno core: `forbidden`.

Activity dedicate più avanti possono usare `review-only`, richiedendo test e spiegazione.

# PY2-10 — Classi, oggetti e capstone

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 29–32;
- monte ore nominale: 12 ore;
- settimana 33: checkpoint/finalizzazione/recupero/enrichment;
- prerequisiti: funzioni, strutture dati, file/error boundaries essenziali;
- baseline: Python 3.12;
- output: lo studente sa riconoscere quando stato e comportamento appartengono alla stessa entità, definire classi/istanze, inizializzare attributi, scrivere metodi, mantenere invarianti semplici, creare più istanze indipendenti, usare composizione e realizzare un piccolo capstone OOP testabile e spiegabile.

## Perché OOP è core di seconda

L'obiettivo non è "imparare la sintassi delle classi".

Dopo funzioni e strutture dati lo studente ha già visto programmi del tipo:

```python
studente = {
    "nome": "Anna",
    "voti": [7, 8, 9],
}
```

più funzioni separate che manipolano quel record.

La domanda diventa:

> **Quando dati, regole e comportamenti descrivono un'unica entità che merita un tipo esplicito?**

Modello:

```text
entità/dominio
→ stato
→ comportamenti
→ invarianti
→ classe
→ più istanze indipendenti
→ collaborazione/composizione
```

Non ogni dict deve diventare una classe. Una classe deve aggiungere chiarezza al modello.

---

# M27 — Dal record all'oggetto: classe, istanza, attributi e `self`

## Obiettivi osservabili

Lo studente sa:

1. distinguere classe e istanza;
2. spiegare che una classe descrive un tipo/comportamento comune e un'istanza è un oggetto concreto;
3. definire una classe semplice;
4. creare più istanze;
5. leggere/scrivere attributi di istanza a livello beginner;
6. capire il ruolo di `self` come riferimento all'istanza su cui il metodo opera;
7. sapere che `self` è convenzione Python fortissima, non una parola chiave riservata;
8. prevedere che due istanze hanno stato indipendente se gli attributi sono inizializzati correttamente;
9. confrontare dict record e object model;
10. riconoscere una classe vuota/usata solo come contenitore senza comportamento come possibile segnale da valutare, non errore assoluto.

## Modello mentale

```python
class Conto:
    ...
```

crea un nuovo tipo.

```python
conto_a = Conto()
conto_b = Conto()
```

crea due oggetti distinti.

Visualizzazione:

```text
conto_a ──> Conto instance { ... }
conto_b ──> Conto instance { ... }
```

Riutilizzare il modello nome→oggetto già costruito con aliasing delle liste.

## `self`

Esempio semplificato:

```python
class Contatore:
    def incrementa(self):
        self.valore += 1
```

Chiamata:

```python
contatore.incrementa()
```

Modello beginner:

> Python chiama il metodo associandolo all'istanza `contatore`; dentro il metodo `self` permette di riferirsi proprio a quell'oggetto.

Non serve entrare subito nel descriptor/bound-method protocol.

## Dict vs oggetto

Confrontare:

```python
studente["voti"].append(8)
```

con:

```python
studente.aggiungi_voto(8)
```

Domanda:

- quale versione rende più esplicita la regola del dominio?
- serve davvero una classe per il problema corrente?

## Activity candidate

### A — Class/instance microscope

Prevedere quali attributi appartengono a quali istanze.

### B — Controlled Change

Aggiungere un attributo/comportamento a una piccola classe esistente.

### C — Model choice

Dato un dominio semplice, scegliere dict vs classe e motivare.

### D — Debug

- dimenticare `self`;
- usare nome globale dell'oggetto dentro il metodo;
- confondere classe e istanza;
- modificare l'istanza sbagliata.

---

# M28 — `__init__`, metodi, stato e invarianti

## Obiettivi osservabili

Lo studente sa:

- usare `__init__` per inizializzare lo stato dell'istanza;
- capire che `__init__` viene eseguito nel processo di costruzione/inizializzazione dell'istanza e non deve restituire l'oggetto;
- assegnare attributi da parametri;
- scrivere metodi che leggono/modificano stato;
- scrivere metodi che restituiscono risultati;
- distinguere metodo mutante e query/calcolo;
- mantenere un invariante semplice;
- validare valori in ingresso nel punto appropriato;
- usare eccezioni già note per input/programmatic contract non valido quando il modello lo richiede;
- testare comportamento prima/dopo una chiamata;
- creare due istanze con stati differenti.

## Esempio core

```python
class Conto:
    def __init__(self, titolare, saldo=0):
        self.titolare = titolare
        self.saldo = saldo

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("importo non valido")
        self.saldo += importo

    def saldo_corrente(self):
        return self.saldo
```

Teacher note:

- il default argument semplice può essere spiegato localmente se usato, senza trasformarlo in un modulo su firme avanzate;
- se vogliamo evitare default in core, usare sempre saldo esplicito.

## Invariante

Esempio:

```text
speed_limit deve essere > 0 e <= 1
```

Questo si collega direttamente al `Robot` reale di Romeo, che valida `speed_limit` in `__init__` e velocità nei propri metodi.

Un invariante è una regola che lo stato valido dell'oggetto deve rispettare.

## Stato pubblico e incapsulamento Python

Nel beginner core è accettabile leggere attributi semplici direttamente.

Non fingere che Python abbia campi privati come Java/C++.

Introduzione leggera della convenzione `_nome` soltanto quando serve distinguere dettaglio interno, senza security theater.

Properties restano enrichment.

## Activity candidate

### A — State trace

Tabella:

| chiamata | stato prima | return | stato dopo |
|---|---|---|---|

### B — Add invariant

Aggiungere validazione a costruttore/metodo.

### C — Implement

Classe piccola con 2–3 attributi e 2–3 metodi significativi.

### D — Debug

- attributo non inizializzato;
- stato condiviso accidentalmente tramite class attribute mutabile (teacher-selected simple example);
- `return` confuso con modifica stato;
- invariante controllato solo in alcuni path;
- `__init__` che restituisce un valore.

## Class attributes

Non sono core come feature da usare.

Possono apparire in Debug Clinic per mostrare il rischio di una lista mutabile dichiarata sulla classe quando si voleva stato per istanza.

---

# M29 — Collaborazione tra oggetti e composizione

## Obiettivi osservabili

Lo studente sa:

1. riconoscere quando un oggetto **ha** un altro oggetto/servizio come collaboratore;
2. passare una dipendenza al costruttore in un esempio semplice;
3. usare composizione senza copiare tutta la logica del collaboratore;
4. separare dominio e I/O;
5. evitare una classe "onnivora" che fa input, file, calcoli, UI e dominio insieme;
6. modellare una relazione semplice fra due classi;
7. testare un oggetto usando un collaboratore semplice/fake predisposto dal docente quando necessario;
8. confrontare composizione e annidamento di dict;
9. capire che ereditarietà non è necessaria per far collaborare oggetti;
10. descrivere responsabilità di ciascuna classe in una frase.

## Composizione core

Esempio concettuale:

```python
class Missione:
    def __init__(self, robot):
        self.robot = robot

    def quadrato(self):
        for _ in range(4):
            self.robot.forward()
            self.robot.left()
```

`Missione` **ha un** robot/collaboratore.

La classe non eredita da Robot: usa Robot.

## Dipendenza esplicita

Passare il collaboratore:

```python
missione = Missione(robot)
```

è preferibile a recuperarlo da una variabile globale nascosta se vogliamo testabilità e chiarezza.

Questo collega scope/dipendenze delle funzioni all'OOP.

## Separare I/O e dominio

Target:

```text
input/menu
→ chiama oggetti dominio
→ print/report
```

non:

```text
oggetto dominio legge input() in ogni metodo
```

salvo che l'I/O sia davvero la responsabilità dell'oggetto.

## Classi onnivore

Smell beginner:

```text
classe Programma
  legge input
  salva file
  muove robot
  calcola tutto
  stampa tutto
```

Domanda di refactoring:

> quali responsabilità possono essere separate?

## Ereditarietà

Non è requisito M29.

Se la classe è pronta, enrichment:

- base/subclass;
- "is-a" come euristica prudente;
- override semplice;
- preferire composizione quando la relazione è collaborazione.

Niente multiple inheritance/MRO.

## Activity candidate

### A — Responsibility cards

Associare comportamenti alla classe/collaboratore più naturale.

### B — Inject collaborator

Rimuovere dipendenza globale e passarla al costruttore.

### C — Implement composition

Due classi piccole che collaborano.

### D — Refactor god class

Separare almeno due responsabilità.

---

# M30 — Capstone OOP

## Obiettivo

Integrare il metodo dell'intero anno:

```text
specifica
→ algoritmo
→ modello dati
→ funzioni
→ classi/oggetti
→ strutture dati
→ test
→ debug
→ spiegazione
```

Non deve essere un progetto enorme. Deve essere **abbastanza piccolo da poter essere compreso interamente dallo studente**.

## Requisiti core del capstone

Il prodotto deve includere almeno:

- analisi input/output/vincoli o requisiti;
- modello delle entità/responsabilità;
- almeno una classe significativa;
- più istanze oppure composizione quando il dominio lo giustifica;
- almeno una collezione (`list`/`dict`/set secondo il problema);
- almeno 3 metodi significativi complessivi;
- una regola/invariante o validazione;
- separazione ragionevole I/O vs logica;
- almeno 5 casi di test/checkpoint;
- un bug diagnosticato o regression test documentato;
- README/relazione breve con scelte e limiti.

Non imporre un numero di classi artificiale.

## Variante preferita — Romeo simulato

Romeo offre già una API OOP reale:

```python
from romeo.robot import Robot

robot = Robot(...)
robot.forward()
robot.left()
robot.stop()
```

Capstone candidato:

### `Missione`

Responsabilità possibili:

- contiene/riceve un `Robot`;
- memorizza parametri missione;
- esegue segmenti/movimenti;
- mantiene stato missione semplice;
- valida parametri;
- usa lista/tuple di step o waypoint dove appropriato;
- produce una missione verificabile dal simulatore.

Possibile composizione:

```text
Missione
  └── Robot
```

Non chiedere agli studenti di reimplementare l'hardware/backend di Romeo.

## Progressione Romeo autentica

Durante l'anno:

```text
romeo.easy.forward()
→ funzioni utente che compongono comandi
→ strutture dati per missioni
→ Robot instance
→ Missione che compone Robot
```

Questo rende visibile perché l'API a oggetti può essere utile.

## Runtime

Core del capstone Romeo deve usare:

```text
runtime.romeo-sim.v1
```

attraverso TheBitLab.

Hardware fisico = enrichment/collaudo separato, mai requisito per voto/core.

## Fallback capstone non-Romeo

Se `romeo-sim` non è certificato sul Classroom Environment in tempo, il corso deve avere un capstone con gli **stessi outcome OOP** senza hardware/runtime speciale.

Candidati:

- gestione studenti/voti (`Studente`, `Registro`);
- catalogo/prestiti semplificato (`Libro`, `Biblioteca`);
- inventario (`Prodotto`, `Inventario`);
- gioco testuale molto piccolo (`Personaggio`, `Stanza`) se non introduce troppa logica accidentale.

Il fallback non è una versione "facile": deve misurare le stesse competenze OOP.

## Activity F — Integrated Product

Il capstone è la principale Activity F del secondo anno.

Fasi:

1. proposta/requisiti;
2. modello responsabilità;
3. skeleton classi/metodi;
4. implementazione incrementale;
5. test/debug;
6. demo;
7. spiegazione orale/scritta breve;
8. eventuale refactoring finale.

## Evidence

- diagramma semplice classi/responsabilità (non UML formale obbligatorio);
- codice;
- test/checklist;
- output/trace del simulatore se Romeo;
- breve changelog/refactoring;
- spiegazione di almeno un trade-off.

---

# Estensioni se il gruppo è pronto

## `__str__` / `__repr__`

`__str__` è il primo special method candidato perché collega oggetto e rappresentazione leggibile.

`__repr__` può essere mostrato come confronto/diagnostica, senza richiedere piena padronanza del data model.

## Property

Mostrare soltanto se serve controllare accesso/calcolo di un attributo senza cambiare l'API esterna.

Non insegnare getter/setter Java-style come requisito universale.

## Inheritance semplice

Un solo esempio naturale.

Requisiti:

- relazione semantica chiara;
- override piccolo;
- confronto con composizione.

Non usarla per dire di aver "completato OOP".

## Dataclass

Solo **dopo** aver scritto una classe esplicita.

Usarla come confronto per data-centric classes, spiegando cosa genera/riduce, non come magia iniziale.

---

# Cose fuori dal core di seconda

- multiple inheritance/MRO;
- descriptors;
- metaclasses;
- ABC/protocols formali;
- advanced dunder/data model;
- decorators;
- generic typing;
- ORM entities;
- design pattern catalog;
- dependency injection framework;
- SOLID come elenco mnemonico.

Possiamo seminare responsabilità/composizione/testabilità senza nomenclatura professionale prematura.

---

# TheBitLab generic object grading — P3

Per classi generiche sarebbe utile un profilo:

```text
P3 — object behavior
```

Requisiti futuri:

- istanziare una classe dichiarata con argomenti built-in;
- chiamare sequenza di metodi;
- osservare return values;
- osservare attributi/properties esplicitamente dichiarati;
- verificare indipendenza di due istanze;
- catturare eccezioni;
- mantenere expected host-side;
- eseguire tutto nel sandbox Docker.

P3 non deve bloccare la didattica: `assert`/manual evidence e `romeo-sim` coprono i primi casi. Ma non creare un autograder fragile basato su regex/AST superficiale per verificare OOP.

---

# Piano delle quattro settimane

## Settimana 29 — M27

- dict record → object;
- class/instance;
- attributi;
- self;
- più istanze;
- lab microscope/model choice.

## Settimana 30 — M28

- `__init__`;
- metodi;
- stato/invarianti;
- test state transitions;
- lab classe completa piccola.

## Settimana 31 — M29

- composizione;
- collaboratori/dipendenze;
- separazione I/O;
- refactoring responsabilità;
- introduzione Robot API come consumer reale.

## Settimana 32 — M30

- capstone implementation/test/demo;
- possibile prova pratica finale integrata;
- refactoring e spiegazione.

## Settimana 33 — Checkpoint C

In base alla classe:

1. finalizzazione capstone;
2. recupero/verifica;
3. enrichment `__str__`/inheritance/dataclass;
4. Romeo demo fisica soltanto se già sicura/collaudata;
5. Git G1 minimo se il calendario lo permette.

Nessun concetto core nuovo obbligatorio.

---

# Exit profile del secondo anno

Uno studente che completa il core dovrebbe riuscire a:

- analizzare un problema e progettare algoritmo/flow chart;
- implementare controllo del flusso anche annidato;
- scegliere `for`/`while`;
- decomporre in funzioni;
- testare/debuggare;
- lavorare con stringhe/list/tuple/set/dict e strutture annidate;
- scegliere struttura dati con motivazione;
- leggere/scrivere file testo essenziali;
- definire classi/istanze/metodi;
- modellare stato + comportamento;
- usare composizione semplice;
- mantenere invarianti;
- costruire un piccolo prodotto integrato e spiegarlo.

Questo è **fine track secondo anno**, non fine curriculum Python.

---

# Fonti

- *Think Python / Pensare in Python*: classes/objects + problem solving;
- *Learning Python / Imparare Python*: OOP coverage;
- Pluralsight Python Object-oriented Programming: progressione dict→object/class;
- *Fluent Python*: data model/composition correctness come fonte docente, non densità beginner;
- *Python in a Nutshell*: reference;
- documentazione Python 3.12 classes;
- Romeo `romeo.easy` + `romeo.robot.Robot` come API reale da mappare;
- issue `python-docente#4` per mapping dettagliato Romeo.

---

# Dipendenze piattaforma

Core generico:

- Python 3.12;
- P1/P2 dove applicabili;
- P3 object behavior futuro per autograding generico.

Capstone Romeo:

- `runtime.romeo-sim.v1` certificato attraverso Classroom Environment;
- nessun hardware fisico obbligatorio.

Fallback generic capstone richiesto se Romeo non è certificato.

---

# Criteri per produzione

- Romeo mapping issue #4 completato per M27–M30;
- nessuna dipendenza dal corso Romeo year-2 networking/web;
- almeno due esempi OOP non-Romeo prima/durante il capstone;
- class vs instance/self/__init__ testati concettualmente;
- alias/reference collegato alle istanze;
- composition core;
- inheritance/dataclass enrichment;
- capstone piccolo e completamente spiegabile;
- generic P3 progettato oppure grading manual/P2/romeo-sim esplicitamente dichiarato;
- hardware fisico mai gate del risultato didattico.

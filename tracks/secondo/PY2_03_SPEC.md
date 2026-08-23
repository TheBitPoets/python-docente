# PY2-03 — Selezione e logica

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 6–8;
- monte ore nominale: 9 ore;
- organizzazione reale: 2 ore teoria attiva + 1 ora laboratorio per settimana;
- prerequisiti: PY2-01 algoritmi/flow chart + PY2-02 programmi lineari, input/output, tipi, conversioni e operatori;
- baseline: Python 3.12;
- output: lo studente traduce decisioni algoritmiche in condizioni Python corrette, sceglie tra `if`, `if/else`, `if/elif/else` e più `if` indipendenti, compone condizioni con logica booleana e sa diagnosticare rami mancanti, sovrapposti o irraggiungibili.

## Perché questa UDA esiste

Una selezione non è soprattutto una parola chiave Python: è una **partizione dei casi possibili**.

Il modello da costruire è:

```text
quali casi esistono?
→ quali condizioni li identificano?
→ i casi sono indipendenti o esclusivi?
→ quale ramo deve essere eseguito?
→ quali casi limite devo provare?
→ il codice rappresenta davvero quella decisione?
```

Il corso deve impedire il pattern meccanico:

```text
"vedo una condizione → scrivo un if"
```

senza ragionare sulla relazione tra i casi.

---

# M06 — Booleani, confronti e `if`

## Obiettivi osservabili

Lo studente sa:

1. riconoscere un'espressione booleana;
2. usare correttamente `==`, `!=`, `<`, `<=`, `>`, `>=`;
3. distinguere assegnamento `=` e confronto `==`;
4. prevedere il risultato di confronti semplici;
5. scrivere un `if` con indentazione corretta;
6. scrivere un `if/else` quando i due casi sono complementari;
7. eseguire il trace di un ramo con dati concreti;
8. scegliere casi di test sotto/sulla/sopra una soglia;
9. riconoscere una condizione invertita;
10. capire che un ramo non eseguito non è un errore: dipende dal valore della condizione.

## Modello mentale

```text
condizione
   |
 true? ---- sì ----> ramo TRUE
   |
   no
   v
ramo FALSE / continuazione
```

L'indentazione non è decorazione: definisce quali istruzioni appartengono al ramo.

## Concetti core

- `bool` come risultato di una domanda vero/falso;
- operatori di confronto;
- `if`;
- `else`;
- blocco indentato;
- casi di frontiera;
- uguaglianza di valore.

## Cose da NON anticipare come scorciatoie

- truthiness sofisticata di collezioni/oggetti;
- ternary expression;
- `match/case`;
- uso di `is` come alternativa a `==`;
- condizioni compatte difficili da leggere.

`is` viene citato soltanto nell'Error Clinic: **non si usa per confrontare normalmente valori numerici/stringhe**.

## Problemi candidati

- maggiorenne/minorenne;
- temperatura sopra una soglia;
- numero positivo/non positivo;
- sconto applicabile/non applicabile;
- accesso consentito se un valore soddisfa una condizione semplice;
- coordinata dentro/fuori un limite singolo.

## Activity candidate

### A — Predict/Trace

Per coppie `valore → condizione`, prevedere:

- `True/False`;
- ramo eseguito;
- output.

### B — Controlled Change

Cambiare una soglia e aggiornare i casi di test che stanno esattamente sul confine.

### C — Implement

Da flow chart già noto a `if/else` Python.

### D — Debug

Correggere:

- `=` al posto di confronto;
- condizione invertita;
- indentazione errata;
- `>` quando serve `>=`;
- output nel ramo sbagliato.

---

# M07 — `elif`, casi esclusivi e condizioni composte

## Obiettivi osservabili

Lo studente sa:

- costruire una catena `if/elif/else`;
- spiegare che viene scelto il **primo ramo vero** della catena;
- distinguere più `if` indipendenti da una catena mutuamente esclusiva;
- usare `and`, `or`, `not`;
- leggere e costruire semplici tabelle di verità;
- esprimere un intervallo;
- usare confronti concatenati semplici (`a <= x <= b`) dopo aver compreso la forma logica equivalente;
- riconoscere condizioni sovrapposte;
- ordinare correttamente soglie/casi;
- progettare test per ogni ramo e per i confini.

## Decisione fondamentale: `if` indipendenti vs `elif`

### Condizioni indipendenti

```python
if piove:
    ...

if fa_freddo:
    ...
```

Entrambi i rami possono essere eseguiti.

### Casi mutuamente esclusivi

```python
if voto < 6:
    ...
elif voto < 8:
    ...
else:
    ...
```

Un solo ramo della catena viene scelto.

Lo studente deve saper **motivare** la scelta, non soltanto riconoscere la sintassi.

## Logica booleana

### `and`

Tutte le condizioni richieste devono essere vere.

### `or`

È sufficiente che almeno una sia vera.

### `not`

Nega una condizione già compresa.

Prima scrivere la condizione in linguaggio naturale, poi tradurla.

## Tabelle di verità minime

| A | B | A and B | A or B |
|---|---|---|---|
| F | F | F | F |
| F | V | F | V |
| V | F | F | V |
| V | V | V | V |

`not` viene trattato separatamente.

## Short-circuit

Introduzione **intuitiva**, non tecnica avanzata:

- Python valuta `and`/`or` da sinistra a destra;
- può non essere necessario valutare la seconda parte;
- ordinare condizioni semplici/sicure può evitare operazioni non valide.

Esempio guidato, non ancora pattern da memorizzare:

```python
if divisore != 0 and numero / divisore > 2:
    ...
```

Il focus resta la correttezza logica.

## Problemi candidati

- fascia d'età;
- classificazione voto;
- tariffa per fasce;
- valore dentro/fuori intervallo;
- triangolo possibile a partire da vincoli molto semplici (solo se non distrae);
- coordinate in una zona rettangolare;
- requisiti multipli per un accesso.

## Activity candidate

### A — Classifica il caso

Dato un input, indicare quale ramo deve essere eseguito senza eseguire il codice.

### B — Due `if` o `elif`?

Ricevere piccole specifiche e scegliere la struttura, motivando in una riga.

### C — Implement

Classificatore a 3–4 fasce con casi di test per tutti i confini.

### D — Debug

Esempi obbligatori:

- soglie nell'ordine sbagliato;
- ramo irraggiungibile;
- condizioni sovrapposte;
- `and` al posto di `or`;
- più `if` quando si voleva un solo risultato;
- `elif` quando due effetti possono coesistere.

---

# M08 — Selezioni annidate, validazione e refactoring

## Obiettivi osservabili

Lo studente sa:

1. leggere e scrivere una selezione annidata semplice;
2. seguire il percorso dei rami con un trace;
3. riconoscere quando l'annidamento rappresenta davvero una dipendenza tra decisioni;
4. riconoscere annidamenti inutili;
5. validare un dato e separare caso valido/non valido;
6. progettare casi di test che percorrono i principali path;
7. semplificare condizioni senza cambiare il comportamento;
8. preferire codice leggibile a condizioni artificiosamente compatte;
9. usare un risultato booleano intermedio con un nome quando migliora la comprensione;
10. confrontare due implementazioni corrette e motivare quale comunica meglio l'intenzione.

## Quando annidare

Annidamento sensato:

```text
prima condizione stabilisce se la seconda domanda ha senso
```

Esempio concettuale:

```python
if credenziali_valide:
    if account_attivo:
        ...
```

Ma spesso una condizione composta può risultare più chiara:

```python
if credenziali_valide and account_attivo:
    ...
```

Non esiste una regola "meno righe = meglio": si confrontano significato e leggibilità.

## Validazione nel punto attuale del corso

Lo studente sa **rilevare** input non valido:

```python
if voto < 0 or voto > 10:
    print("dato non valido")
else:
    ...
```

Non sa ancora ripetere automaticamente la richiesta finché il dato non è valido: questo arriverà con `while` in PY2-04.

Questa distinzione è importante per costruire prerequisiti corretti.

## Variabili booleane nominate

Quando migliora il modello:

```python
eta_valida = 0 <= eta <= 120
```

poi:

```python
if eta_valida:
    ...
```

Non trasformare ogni condizione in una variabile: il nome deve aggiungere significato.

## De Morgan / algebra booleana

Solo introduzione leggera e concreta, se utile per semplificare una negazione. Nessuna UDA formale di algebra booleana in questa fase.

## Activity candidate

### A — Path trace

Dato codice annidato, segnare il percorso effettivamente seguito per più input.

### B — Controlled refactor

Trasformare un annidamento ridondante in una condizione composta oppure viceversa, mantenendo gli stessi casi di test.

### C — Implement

Problema con:

- validazione iniziale;
- almeno tre casi validi;
- output deterministico;
- tabella casi di test prima del codice.

### D — Debug Clinic

Correggere una soluzione apparentemente plausibile ma con un ramo mancante o casi sovrapposti.

### E — Mini-project

**Configuratore/regole semplici**: da una piccola specifica (es. tariffa, accesso, classificazione) costruire:

1. input/output/vincoli;
2. flow chart o pseudocodice;
3. tabella casi;
4. implementazione Python;
5. spiegazione della struttura di selezione scelta.

---

# Romeo nella UDA

Romeo può essere un **dominio applicativo opzionale**, non un requisito per comprendere la selezione.

Esempi possibili, solo se coerenti con l'API simulata disponibile:

- scegliere un comportamento in base a un parametro della missione;
- scegliere velocità/azione da un valore dato;
- validare un comando prima di inviarlo al simulatore.

Regole:

- ogni concetto ha sempre esercizi generali non-Romeo;
- nessun sensore/hardware fisico necessario;
- non importare networking/eventi dal corso Romeo avanzato;
- il mapping preciso resta governato da issue #4.

---

# Piano delle tre settimane

## Settimana 6 — M06

### Ora teoria attiva 1

- domanda vero/falso;
- confronti;
- previsione di espressioni booleane;
- confini `<`/`<=`;
- micro-trace.

### Ora teoria attiva 2

- `if` e `if/else`;
- indentazione;
- flow chart → Python;
- Error Clinic.

### Ora laboratorio

- Activity A/B/C;
- primi test branch-based;
- debug guidato.

## Settimana 7 — M07

### Ora teoria attiva 1

- `elif`;
- primo ramo vero;
- casi mutuamente esclusivi;
- più `if` indipendenti.

### Ora teoria attiva 2

- `and`, `or`, `not`;
- intervalli;
- confini;
- semplici truth table;
- short-circuit intuitivo.

### Ora laboratorio

- classificatore multi-ramo;
- Activity B/C/D;
- test per ogni ramo.

## Settimana 8 — M08

### Ora teoria attiva 1

- annidamento;
- path trace;
- validazione senza ripetizione;
- condizioni dipendenti.

### Ora teoria attiva 2

- refactoring;
- condizioni composte vs annidate;
- leggibilità;
- confronto tra due soluzioni corrette.

### Ora laboratorio

- Debug Clinic;
- Activity E / mini-problema integrato;
- exit checkpoint;
- possibile evidence preparatoria alla prima prova teorica/scritta.

---

# Exit checkpoint UDA

Prima di passare ai cicli lo studente dovrebbe saper:

- valutare una condizione booleana;
- scegliere correttamente `<`, `<=`, `==`, `!=`, `>=`, `>`;
- costruire `if`, `if/else`, `if/elif/else`;
- distinguere rami indipendenti ed esclusivi;
- usare `and`, `or`, `not` in condizioni semplici;
- costruire un controllo di intervallo;
- seguire selezioni annidate;
- progettare almeno un test per ogni ramo significativo;
- identificare un ramo mancante/sovrapposto/irraggiungibile;
- spiegare perché ha scelto una determinata struttura;
- rilevare un input non valido senza ancora doverlo richiedere nuovamente.

---

# Valutazione ed evidence

Evidence formative:

- trace di 2–3 decisioni;
- tabella casi per un `elif`;
- esercizio `if` indipendenti vs `elif`;
- debug task;
- implementazione multi-ramo;
- breve motivazione della scelta.

Questa UDA prepara naturalmente la prima prova teoria/scritta prevista dal calendario, che include algoritmi, flow chart, semantica di base e controllo del flusso.

---

# Remediation

Per studenti in difficoltà:

1. partire da una sola domanda sì/no;
2. usare una linea dei numeri per le soglie;
3. colorare i casi coperti dai rami;
4. provare un valore per volta e segnare `True/False`;
5. evitare condizioni composte finché i confronti singoli non sono stabili;
6. costruire `elif` da una tabella casi già completa;
7. tornare al flow chart se il codice nasconde il ragionamento.

# Enrichment

Per studenti rapidi:

- chained comparisons dopo la forma con `and`;
- short-circuit con casi sicuri;
- minimizzazione di condizioni ridondanti;
- semplici controesempi per dimostrare che due condizioni non sono equivalenti;
- confronto leggibilità tra condizioni composte e annidamento;
- `match/case` soltanto come **preview non-core** se esiste un problema che lo rende davvero più espressivo.

---

# Fonti di progettazione

## Pedagogia

- *Think Python / Pensare in Python*: conditional execution, Boolean expressions, debugging;
- *Learning Python / Imparare Python*: statement, espressioni e controllo del flusso;
- Pluralsight Python Essentials: coverage/lab beginner.

## Controllo tecnico

- documentazione Python 3.12: `if` statements, comparisons, Boolean operations.

## Controllo idiomatico

- *Fluent Python* / *Python in a Nutshell* soltanto per evitare modelli mentali falsi e scorciatoie improprie; non determinano la densità beginner.

---

# Dipendenze piattaforma

Core:

- `workspace.v1`;
- `shell.v1`;
- `python.v1` / Python 3.12;
- runner P1 single-file stdin/stdout per Activity autogradabili.

Optional:

- `flowchart.lab.v1` per confrontare diagramma e codice;
- `runtime.romeo-sim.v1` per una missione applicativa selezionata.

Nessuna Activity di questa UDA deve richiedere Romeo per ottenere gli outcome core.

---

# Criteri per passare dalla SPEC alla produzione

- vertical slice PY2-02 certificato o blocker esplicitamente gestito;
- lesson M06–M08 originali e revisionate;
- test/Activity non confondono più `if` indipendenti con `elif`;
- casi limite di soglia presenti;
- almeno un Debug Clinic per modulo;
- source mapping completato;
- eventuale Romeo Activity verificata separatamente;
- nessun uso obbligatorio di `match/case` nel core.

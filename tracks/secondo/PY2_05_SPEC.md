# PY2-05 — Funzioni, decomposizione e testing

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 13–16;
- monte ore nominale: 12 ore;
- organizzazione reale: 2 ore teoria attiva + 1 ora laboratorio per settimana;
- prerequisiti: programmi lineari, selezione, `for`/`while`, pattern iterativi e debugging di base;
- baseline: Python 3.12;
- output: lo studente sa decomporre un problema in funzioni con responsabilità chiare, distinguere parametri/argomenti e `return`/`print`, comporre funzioni, ragionare sullo scope locale, progettare top-down e verificare funzioni con casi deterministici e `assert` semplici.

## Perché questa UDA esiste

Fin qui lo studente può già scrivere programmi non banali, ma rischia di produrre un unico blocco crescente di codice.

La domanda cambia:

> **Come divido il problema in parti che posso capire, verificare, riusare e modificare senza rompere tutto?**

Modello:

```text
problema grande
→ responsabilità più piccole
→ funzione per una trasformazione/decisione coerente
→ input tramite parametri
→ risultato tramite return
→ test separato
→ composizione delle parti
```

La funzione non viene presentata soltanto come "modo per evitare di ripetere righe", ma come **unità di ragionamento e contratto**.

---

# M13 — Funzioni produttive: parametri, argomenti e `return`

## Obiettivi osservabili

Lo studente sa:

1. definire e chiamare una funzione;
2. distinguere nome della funzione e chiamata;
3. distinguere parametro e argomento;
4. usare uno o più parametri semplici;
5. usare `return` per produrre un valore;
6. usare il valore restituito in un'espressione o assegnamento;
7. distinguere una funzione che **calcola** da una funzione che **stampa**;
8. spiegare cosa accade quando una funzione termina senza `return` esplicito (`None` a livello introduttivo);
9. scegliere nomi di funzione che esprimono un'azione/domanda;
10. verificare una funzione su più input senza ripetere manualmente l'intero programma.

## Modello mentale della chiamata

```text
argomenti
   ↓
parametri locali
   ↓
corpo funzione
   ↓
return
   ↓
valore al punto di chiamata
```

## `print` non è `return`

Confronto obbligatorio:

```python
def somma(a, b):
    print(a + b)
```

vs

```python
def somma(a, b):
    return a + b
```

Domande:

- quale posso usare in `x = somma(2, 3)`?
- quale posso testare facilmente confrontando un valore?
- quale separa calcolo e interfaccia?

`print` resta corretto quando la responsabilità della funzione è davvero presentare output, ma non deve sostituire il risultato del calcolo.

## Funzioni predicate

Dopo la selezione è naturale introdurre funzioni che restituiscono `bool`:

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

Questo collega naming e logica:

```python
if eta_valida(eta):
    ...
```

## Cose fuori dal core M13

- `*args`/`**kwargs`;
- decorators;
- lambda;
- type hints formali;
- funzioni come oggetti;
- closure;
- recursion.

## Activity candidate

### A — Call trace

Dato un programma con 2–3 chiamate, completare:

| chiamata | parametri locali | return |
|---|---|---|

### B — Controlled Change

Trasformare una funzione che stampa in una funzione che restituisce un valore e aggiornare il chiamante.

### C — Implement

Funzioni numeriche/predicate semplici con casi di test dichiarati.

### D — Debug

- parentesi mancanti nella chiamata;
- `return` mancante;
- codice dopo `return` irraggiungibile;
- parametro con nome sbagliato;
- valore calcolato ma non restituito.

---

# M14 — Scope locale, passaggio dei dati e composizione

## Obiettivi osservabili

Lo studente sa:

- capire che parametri e variabili definite nella funzione sono locali;
- distinguere una variabile locale da una variabile esterna;
- passare esplicitamente alla funzione i dati di cui ha bisogno;
- evitare variabili globali come scorciatoia;
- usare il risultato di una funzione come argomento di un'altra;
- far collaborare più funzioni;
- leggere un piccolo call graph;
- seguire il flusso dei dati tra chiamate;
- riconoscere una dipendenza nascosta da stato globale;
- usare costanti semplici a livello modulo soltanto quando rappresentano davvero configurazione immutabile/dominio e non dati di lavoro.

## Scope: modello beginner corretto

Esempio:

```python
def doppio(numero):
    risultato = numero * 2
    return risultato
```

`numero` e `risultato` appartengono alla chiamata della funzione.

Non serve ancora formalizzare LEGB; basta costruire il principio:

> una funzione dovrebbe ricevere esplicitamente ciò che le serve e restituire ciò che produce.

## Perché evitare globali

Confronto:

```python
saldo = 100

def preleva():
    ...  # dipende da stato esterno
```

contro una trasformazione esplicita:

```python
def nuovo_saldo(saldo, importo):
    return saldo - importo
```

Il secondo esempio è più facile da comprendere e testare.

Non trasformare questo in dogma: lo studente deve capire il problema delle dipendenze nascoste.

## Composizione

```python
def area_rettangolo(base, altezza):
    return base * altezza


def costo_pittura(area, costo_mq):
    return area * costo_mq
```

Poi:

```python
area = area_rettangolo(base, altezza)
costo = costo_pittura(area, prezzo)
```

La versione con variabili intermedie è spesso preferibile per studenti beginner perché rende visibile il flusso dei dati.

## Activity candidate

### A — Scope trace

Identificare per ogni nome dove nasce e dove può essere usato.

### B — Remove global

Refactoring controllato per sostituire una dipendenza globale con parametro/return.

### C — Compose

Costruire 2–3 funzioni che collaborano su un piccolo calcolo.

### D — Debug

- uso di variabile locale fuori funzione;
- globale modificata accidentalmente;
- parametro non passato;
- risultato di funzione ignorato.

---

# M15 — Progettazione top-down e responsabilità

## Obiettivi osservabili

Lo studente sa:

1. partire da una specifica e individuare sotto-problemi;
2. dare un nome alle responsabilità prima di scrivere il corpo delle funzioni;
3. separare acquisizione dati, logica e presentazione;
4. scrivere una firma/bozza della funzione prima dell'implementazione;
5. definire input e output attesi della funzione;
6. formulare pre-condizioni/post-condizioni semplici in linguaggio naturale;
7. evitare funzioni che fanno troppe cose non correlate;
8. evitare duplicazione significativa estraendo una responsabilità comune;
9. costruire un piccolo call graph/top-down plan;
10. implementare una funzione alla volta e integrarle progressivamente.

## Processo top-down

Per un problema non banale:

```text
1. cosa deve fare il programma nel complesso?
2. quali responsabilità indipendenti riconosco?
3. quale dato entra in ciascuna?
4. quale risultato deve uscire?
5. quali funzioni dipendono da quali altre?
6. quale funzione posso testare per prima?
```

## Separazione I/O – logica – presentazione

Pattern beginner target:

```python
def calcola_qualcosa(...):
    return ...


def main():
    dato = int(input())
    risultato = calcola_qualcosa(dato)
    print(risultato)

main()
```

La funzione `main()` può essere introdotta come organizzazione del flusso, senza anticipare ancora il guard `if __name__ == "__main__"` come obbligo.

## Contratto intuitivo

Esempio:

```text
funzione: calcola_sconto
input: prezzo >= 0, percentuale 0..100
output: importo sconto >= 0
non stampa
```

Questo prepara testing, typing e design by contract futuri senza formalismo eccessivo.

## Quanto deve essere grande una funzione?

Niente regole tipo "massimo 10 righe".

Domande migliori:

- ha una responsabilità che posso nominare?
- posso descriverla senza usare "e poi anche" molte volte?
- riceve dati necessari in modo esplicito?
- produce un risultato comprensibile?
- è testabile separatamente?

## Activity candidate

### A — Decomposition cards

Dato un problema, raggruppare azioni in responsabilità/funzioni candidate.

### B — Extract function

Estrarre codice duplicato o un calcolo coerente da un programma monolitico.

### C — Top-down design

Produrre prima:

- elenco funzioni;
- parametri;
- return;
- casi di test;

poi implementare.

### D — Smell/debug

Identificare:

- funzione che legge, calcola e stampa tutto;
- funzione con dipendenza globale;
- duplicazione;
- responsabilità troppo ampia.

---

# M16 — Test, `assert`, debug e refactoring

## Obiettivi osservabili

Lo studente sa:

- progettare casi di test prima/dopo la funzione;
- distinguere caso normale, confine, caso non valido quando previsto dal contratto;
- usare `assert` semplice per confrontare risultato atteso e ottenuto;
- scrivere più `assert` indipendenti;
- leggere un `AssertionError` elementare;
- capire che i test sono esempi/evidence, non una prova matematica automatica di correttezza;
- correggere una funzione mantenendo i test verdi;
- aggiungere un test quando scopre un bug;
- refactorare mantenendo il comportamento osservabile;
- distinguere bug nel codice e test scritto male;
- usare test per confrontare due implementazioni con lo stesso contratto.

## Progressione testing

```text
casi su carta
→ expected result
→ chiamata funzione
→ assert
→ gruppo di assert
→ futuro test runner/pytest
```

Esempio:

```python
def doppio(x):
    return x * 2

assert doppio(3) == 6
assert doppio(0) == 0
assert doppio(-2) == -4
```

## Test fallito come informazione

Workflow:

```text
rosso
→ quale caso fallisce?
→ cosa mi aspettavo?
→ cosa è accaduto?
→ bug nel codice o nel test?
→ modifica minima
→ riesegui tutti i test
```

Non premiare il pattern "modifica finché diventa verde" senza spiegazione.

## Regression test introduttivo

Quando viene scoperto un bug:

1. costruire un caso che lo riproduce;
2. verificare che fallisca;
3. correggere;
4. verificare che il nuovo test e i precedenti passino.

È una pratica professionale introdotta in forma beginner.

## Refactoring

Definizione operativa:

> migliorare la struttura senza cambiare il comportamento richiesto.

Esempi:

- estrarre funzione;
- rinominare;
- eliminare duplicazione;
- semplificare condizione;
- spostare calcolo fuori da I/O.

I test proteggono il comportamento durante il refactoring.

## TheBitLab P2

Questa UDA crea il primo bisogno reale del futuro profilo:

```text
P2 — function behavior
```

Il runner dovrebbe poter importare il modulo studente e testare funzioni/return senza costringere il corso a trasformare tutto in stdin/stdout.

Fino alla certificazione P2:

- `assert` nel workspace/lab come evidence formativa;
- Activity P1 wrapper soltanto quando non distorce l'obiettivo;
- niente fake P2 basato su parsing fragile del sorgente.

## Activity candidate

### A — Test reader

Dati funzione e assert, prevedere quali passano/falliscono.

### B — Add a test

Aggiungere caso limite che espone un bug.

### C — Implement from contract

Implementare funzione a partire da input/output/pre-condizioni + test.

### D — Debug regression

Riprodurre bug, aggiungere test, correggere, rieseguire.

### E — Mini-project funzionale

Piccolo programma top-down con:

- almeno 3 responsabilità/funzioni;
- I/O separato;
- logica testabile;
- selezione/cicli già appresi;
- almeno 5 casi di test complessivi;
- breve call graph;
- spiegazione di un refactoring eseguito.

---

# Cose volutamente rinviate

Non fanno parte del core di questa UDA:

- type hints formali;
- default arguments complessi;
- keyword-only/positional-only;
- `*args` / `**kwargs`;
- recursion;
- lambda;
- closure;
- decorators;
- first-class functions;
- docstring API formali;
- moduli/package multi-file;
- pytest come framework studente;
- mocking.

Questi concetti restano nella roadmap avanzata/professionale.

Keyword arguments semplici possono comparire come enrichment soltanto dopo la padronanza di parametro/argomento.

---

# Romeo nella UDA

Romeo è molto adatto a mostrare il valore della decomposizione:

prima:

```text
forward
sleep
left
forward
sleep
...
```

poi funzioni nominate:

```text
vai_avanti_per(...)
gira_a_sinistra(...)
percorri_lato(...)
```

Infine una missione scomposta in responsabilità.

Regole:

- prima la funzione generale/non-Romeo;
- Romeo come applicazione e feedback visivo;
- simulator-only core;
- niente hardware obbligatorio;
- mapping reale verificato separatamente in issue #4.

---

# Piano delle quattro settimane

## Settimana 13 — M13

### Ora teoria attiva 1

- chiamata/definizione;
- parametro vs argomento;
- call trace;
- `return`.

### Ora teoria attiva 2

- `return` vs `print`;
- funzioni predicate;
- errori tipici;
- casi di test semplici.

### Ora laboratorio

- Activity A/B/C;
- refactoring di piccoli programmi precedenti.

## Settimana 14 — M14

### Ora teoria attiva 1

- scope locale;
- passaggio dati;
- dipendenze esplicite;
- trace chiamate.

### Ora teoria attiva 2

- composizione;
- risultati intermedi;
- globali come smell;
- call graph semplice.

### Ora laboratorio

- Remove global;
- Compose;
- Debug Clinic.

## Settimana 15 — M15

### Ora teoria attiva 1

- decomposizione top-down;
- responsabilità;
- firma prima del corpo.

### Ora teoria attiva 2

- I/O vs logica;
- contratti intuitivi;
- funzione `main` come orchestrazione;
- extraction/refactoring.

### Ora laboratorio

- design prima del codice;
- implementazione incrementale di mini-problema.

## Settimana 16 — M16

### Ora teoria attiva 1

- test case;
- `assert`;
- failure/debug;
- regression test.

### Ora teoria attiva 2

- refactoring protetto dai test;
- confrontare due implementazioni;
- preparazione checkpoint A.

### Ora laboratorio

- Activity D/E;
- mini-project funzionale;
- exit checkpoint.

---

# Exit checkpoint UDA

Prima del checkpoint A e delle strutture dati, lo studente dovrebbe saper:

- definire/chiamare funzioni;
- distinguere parametro/argomento;
- usare `return` e spiegare perché non coincide con `print`;
- passare dati esplicitamente;
- usare variabili locali senza dipendere da globali di lavoro;
- comporre più funzioni;
- separare input, logica e output in un piccolo programma;
- decomporre top-down un problema;
- dare a una funzione una responsabilità nominabile;
- progettare casi di test;
- usare semplici `assert`;
- aggiungere un regression test dopo un bug;
- refactorare mantenendo test verdi;
- spiegare il flusso dati/call graph del proprio programma.

---

# Valutazione/evidence

Evidence formative:

- call trace;
- `return` vs `print` task;
- scope/debug task;
- decomposition plan;
- 3+ assert su una funzione;
- regression bug-fix;
- mini-project top-down.

Questa UDA confluisce direttamente nella prova pratica del primo quadrimestre/checkpoint A.

---

# Remediation

Per studenti in difficoltà:

1. una funzione a un parametro e una sola espressione;
2. scrivere chiamata → sostituzione parametro → risultato;
3. separare sempre funzione e `print` nel chiamante;
4. niente composizione finché `return` non è stabile;
5. disegnare box per variabili locali;
6. usare contratti input/output in tabella;
7. scrivere un assert per volta;
8. estrarre funzioni da codice già compreso invece di progettare subito da zero.

# Enrichment

Per studenti rapidi:

- keyword arguments semplici;
- piccoli docstring descrittivi;
- funzioni predicate riusabili;
- confrontare API alternative;
- progettare funzione prima dei test vs test prima della funzione;
- missione Romeo top-down;
- primi cenni a pure function/side effect senza formalismo FP.

---

# Fonti di progettazione

## Pedagogia

- *Think Python / Pensare in Python*: functions, fruitful functions, incremental development, debugging;
- *Learning Python / Imparare Python*: functions/scope come coverage;
- Pluralsight Python Essentials e OOP path per lab/decomposizione.

## Controllo tecnico

- documentazione Python 3.12: function definitions, return, scopes/namespaces a livello appropriato.

## Controllo idiomatico

- *Fluent Python* e *Python in a Nutshell* per evitare modelli falsi, senza importare first-class/decorators nel beginner core.

---

# Dipendenze piattaforma

Core:

- `workspace.v1`;
- `shell.v1`;
- `python.v1` / Python 3.12.

Grading:

- P1 resta disponibile per programmi completi stdin/stdout;
- questa UDA definisce il bisogno di `P2 function behavior`;
- P2 deve essere progettato/certificato prima di autogradare direttamente API di funzione;
- fino ad allora gli `assert` possono essere evidence formativa/manuale senza inventare un grader fragile.

Optional:

- `runtime.romeo-sim.v1` per decomposizione di missioni.

---

# Criteri per passare dalla SPEC alla produzione

- P1 vertical slice #7 certificato o blocker esplicito;
- decisione piattaforma sul P2 function behavior;
- lesson M13–M16 revisionate;
- `return` vs `print` trattato esplicitamente;
- scope senza introduzione prematura dell'intero LEGB;
- almeno un refactoring monolite → funzioni;
- `assert` e regression testing presenti;
- mini-project top-down con più funzioni;
- Romeo mapping selettivo verificato;
- niente pytest obbligatorio nel core di seconda.

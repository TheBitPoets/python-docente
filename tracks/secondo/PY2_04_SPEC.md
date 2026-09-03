# PY2-04 — Iterazione e pattern algoritmici

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 9–12;
- monte ore nominale: 12 ore;
- organizzazione reale: 2 ore teoria attiva + 1 ora laboratorio per settimana;
- prerequisiti: sequenza, input/output, condizioni, `if/elif/else`, logica booleana e trace;
- baseline: Python 3.12;
- output: lo studente sa scegliere e combinare `while` e `for`, controllare la terminazione, usare contatori/accumulatori/sentinelle/flag, comporre iterazione e selezione, costruire cicli annidati e confrontare soluzioni anche rispetto al lavoro svolto.

## Perché questa UDA esiste

La domanda guida non è:

> "Qual è la sintassi del ciclo?"

ma:

> **"Che cosa determina quando e quante volte devo ripetere questa azione?"**

Modello:

```text
ripetizione richiesta
→ durata nota o dipendente da una condizione?
→ quale stato cambia?
→ come garantisco la terminazione?
→ cosa devo ricordare durante il ciclo?
→ quali casi limite devo provare?
→ sto ripetendo lavoro inutile?
```

La scelta del costrutto fa parte della soluzione.

---

# M09 — `while`, stato, sentinelle e validazione ripetuta

## Obiettivi osservabili

Lo studente sa:

1. spiegare che `while` ripete finché una condizione resta vera;
2. identificare inizializzazione, condizione, corpo e aggiornamento;
3. eseguire manualmente il trace di un `while`;
4. riconoscere un ciclo infinito;
5. riconoscere un aggiornamento mancante o nel punto sbagliato;
6. usare un contatore in un `while`;
7. usare una sentinella;
8. ripetere una richiesta finché un input è valido;
9. distinguere condizione di continuazione e condizione di uscita;
10. costruire test che includano zero iterazioni, una iterazione e più iterazioni quando il problema lo consente.

## Modello mentale

```text
stato iniziale
     ↓
condizione? ── false ──> fine
     |
    true
     ↓
   corpo
     ↓
aggiornamento
     └───────────────↺
```

Ogni `while` deve rispondere a:

- quale valore può far cambiare la condizione?
- chi lo aggiorna?
- esiste un percorso in cui non viene aggiornato?

## Validazione ripetuta

Ponte naturale da PY2-03:

prima:

```python
if voto < 0 or voto > 10:
    print("dato non valido")
```

ora:

```python
voto = int(input())
while voto < 0 or voto > 10:
    voto = int(input())
```

Il focus è il modello **controlla → correggi/richiedi → ricontrolla**.

## Sentinella

Esempio concettuale:

```text
leggi valore
finché valore != valore_di_fine:
    elabora
    leggi nuovo valore
```

Prima flow chart/trace, poi Python.

## `while True` + `break`

Non è la forma introduttiva primaria.

Può essere mostrata dopo che il ciclo condizionale è compreso, come alternativa quando la condizione di uscita nasce naturalmente **dentro** il corpo. Lo studente deve saper spiegare dove e perché il ciclo termina.

Evitare `while True` come scorciatoia per non progettare la condizione.

## Activity candidate

### A — Trace

Compilare tabella:

| iterazione | variabile | condizione | output |
|---:|---:|---|---|

### B — Controlled Change

Modificare i limiti di una validazione e aggiornare i casi di test.

### C — Implement

Richiedere un dato finché rientra in un intervallo valido.

### D — Debug

- aggiornamento mancante;
- condizione invertita;
- variabile aggiornata solo in un ramo;
- inizializzazione errata;
- off-by-one con contatore.

---

# M10 — `for`, `range` e scelta `for` vs `while`

## Obiettivi osservabili

Lo studente sa:

- usare `for` con `range`;
- leggere `range(stop)`, `range(start, stop)`, `range(start, stop, step)`;
- ricordare che il limite finale di `range` è escluso;
- prevedere valori prodotti da un `range`;
- ripetere un numero noto di volte;
- contare avanti e indietro;
- scegliere `for` quando il numero/insieme di iterazioni è noto o naturalmente iterabile;
- scegliere `while` quando la durata dipende da una condizione dinamica;
- riscrivere un semplice `while` contatore come `for` e confrontare le due versioni;
- usare `break`/`continue` solo quando migliorano realmente il flusso.

## Modello di scelta

### `for`

```text
so quali passi/valori attraversare
```

### `while`

```text
continuo finché una condizione dipendente dallo stato resta vera
```

Esempio da confrontare:

```python
for i in range(5):
    print(i)
```

vs

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Entrambi corretti, ma il primo comunica meglio l'intenzione quando la ripetizione è controllata da un intervallo noto.

## Off-by-one

Tema obbligatorio:

- stop escluso;
- primo/ultimo valore;
- quante iterazioni?
- valori negativi/step;
- intervallo vuoto.

Prima previsione, poi REPL.

## `break` e `continue`

### `break`

Interrompe il ciclo quando un obiettivo/condizione di stop è già raggiunto.

### `continue`

Salta al passo successivo.

Regola didattica:

> usarli quando rendono il flusso più chiaro, non per evitare di progettare correttamente il ciclo.

Niente `for/else` nel core di seconda.

## Activity candidate

### A — Range microscope

Prevedere l'elenco di valori prodotto da diversi `range`.

### B — `for` o `while`?

Classificare problemi e motivare la scelta in una frase.

### C — Implement

Ripetizioni a numero noto, countdown, serie di calcoli semplici.

### D — Debug

Off-by-one, step errato, range vuoto, contatore duplicato inutilmente.

## Romeo opzionale

Missioni naturali:

- ripetere quattro lati di un quadrato con `for`;
- ripetere una sequenza di movimento N volte;
- confrontare versione duplicata vs loop.

Sempre con simulatore, mai hardware core.

---

# M11 — Selezione + iterazione: contatori, accumulatori, ricerca e flag

## Obiettivi osservabili

Lo studente sa:

1. usare `if` dentro `for/while`;
2. usare un ciclo dentro un ramo condizionale quando il problema lo richiede;
3. distinguere contatore e accumulatore;
4. contare elementi/casi che soddisfano una condizione;
5. accumulare somma/prodotto quando appropriato;
6. calcolare una media conoscendo conteggio e somma;
7. mantenere un minimo/massimo progressivo senza dipendere da collezioni avanzate;
8. eseguire una ricerca lineare concettuale;
9. usare un flag booleano quando rappresenta chiaramente uno stato;
10. riconoscere quando un flag è ridondante rispetto a una condizione o a `break`;
11. progettare casi di test per nessun match, un match e più match.

## Pattern: contatore

```python
conteggio = 0
for ...:
    if condizione:
        conteggio += 1
```

## Pattern: accumulatore

```python
totale = 0
for ...:
    totale += valore
```

## Pattern: minimo/massimo progressivo

Prima spiegare il problema dell'inizializzazione.

Evitare sentinel numeriche arbitrarie tipo:

```python
minimo = 999999
```

se il dominio non le garantisce.

Nelle prime attività si può usare un primo dato letto separatamente, così lo studente comprende l'invariante:

```text
"minimo è il più piccolo valore visto finora"
```

## Pattern: ricerca

Domanda:

```text
ho già trovato ciò che cerco?
```

Possibili forme:

- flag;
- `break` dopo match;
- continuazione completa se servono tutti i match.

Il corso deve distinguere **trovare il primo** da **contare/trovare tutti**.

## Invarianti intuitive

Senza formalismo matematico pesante, introdurre frasi come:

- `totale` contiene la somma dei valori già elaborati;
- `conteggio` contiene il numero di valori validi già visti;
- `minimo` contiene il più piccolo valore già visto.

Queste frasi aiutano debugging e preparano algoritmi più avanzati.

## Activity candidate

### A — Trace pattern

Seguire contatore/accumulatore su 4–5 valori concreti.

### B — Controlled Change

Da "conta positivi" a "conta valori in un intervallo".

### C — Implement

Serie di N dati con somma/media/conteggio condizionale.

### D — Debug

- reset dell'accumulatore dentro il ciclo;
- incremento fuori dal ramo corretto;
- divisione per conteggio zero;
- minimo inizializzato male;
- flag mai aggiornato.

---

# M12 — Cicli annidati, griglie e costo del lavoro

## Obiettivi osservabili

Lo studente sa:

- leggere un ciclo dentro un altro ciclo;
- distinguere iterazione esterna e interna;
- determinare quante volte viene eseguito il corpo interno in casi semplici;
- generare tabelle/griglie/pattern;
- usare `if` dentro cicli annidati;
- costruire coppie di indici;
- riconoscere quando due cicli annidati sono naturali al problema;
- riconoscere annidamento accidentale o lavoro ripetuto evitabile;
- confrontare intuitivamente una scansione singola con un lavoro quadratico;
- preferire una soluzione più semplice/leggibile quando la differenza di costo non è rilevante al problema;
- evitare micro-ottimizzazione senza misura o motivo.

## Modello mentale

```python
for riga in range(R):
    for colonna in range(C):
        ...
```

Per ogni valore del ciclo esterno, il ciclo interno completa il proprio percorso.

Trace consigliato:

| riga | colonna | azione |
|---:|---:|---|

## Quante iterazioni?

Se:

```text
R righe × C colonne
```

il corpo interno viene eseguito `R × C` volte.

Per due cicli entrambi su `N`:

```text
N × N
```

Introduzione intuitiva alla crescita del lavoro, senza formalizzare ancora Big-O.

## Esempi naturali

- tabellina;
- griglia di coordinate;
- rettangolo di simboli;
- tutte le coppie di due piccoli intervalli;
- matrice concettuale prima delle vere liste di liste;
- percorso/griglia Romeo come scenario.

## Esempio di lavoro ripetuto

Confrontare:

```text
per ogni elemento
    ricalcolo ogni volta qualcosa che non cambia
```

con:

```text
calcolo una volta fuori dal ciclo
poi riuso il risultato
```

Lo studente deve iniziare a chiedersi:

> questa operazione dipende davvero dall'iterazione corrente?

## Performance: livello di seconda

Criteri ordinati:

```text
1. correttezza
2. comprensibilità
3. struttura adatta al problema
4. evitare lavoro chiaramente inutile
5. efficienza quando i dati/ripetizioni la rendono rilevante
```

Non insegnare "più corto = più veloce" né "più Pythonico = sempre migliore".

## Activity candidate

### A — Nested trace

Compilare tutte le coppie `(i, j)` prodotte da due range piccoli.

### B — Controlled Change

Cambiare dimensioni di una griglia e prevedere numero di iterazioni/output.

### C — Implement

Generare tabella/griglia con un pattern condizionale.

### D — Debug

- variabile interna/esterna confusa;
- indentazione sbagliata;
- accumulatore resettato al livello errato;
- condizione applicata al ciclo sbagliato;
- range interno costruito con limite errato.

### E — Mini-project

Problema con almeno:

- un ciclo;
- una selezione;
- contatore/accumulatore oppure annidamento;
- test progettati prima del codice;
- breve motivazione `for` vs `while`.

---

# Progressione delle combinazioni obbligatorie

Entro la fine della UDA lo studente deve aver incontrato e scritto almeno una volta:

```text
if dentro for
if dentro while
for dentro if/else
while dentro if/else
for dentro for
if dentro for dentro for
```

Non come esercizio di annidamento fine a sé stesso: ogni composizione deve avere un problema che la giustifica.

La profondità di annidamento didattica resta controllata. Tre/quattro livelli senza necessità reale sono un segnale da refactoring, non un obiettivo.

---

# Piano delle quattro settimane

## Settimana 9 — M09

### Ora teoria attiva 1

- dal flow chart al `while`;
- stato/condizione/aggiornamento;
- trace;
- terminazione.

### Ora teoria attiva 2

- validazione ripetuta;
- sentinelle;
- zero/una/molte iterazioni;
- Debug Clinic ciclo infinito.

### Ora laboratorio

- Activity A–D `while`;
- validazione input;
- trace/report.

## Settimana 10 — M10

### Ora teoria attiva 1

- `for` e `range`;
- stop escluso;
- step;
- previsione.

### Ora teoria attiva 2

- `for` vs `while`;
- refactoring;
- `break`/`continue` disciplinati;
- Romeo loop come optional demo.

### Ora laboratorio

- Activity range;
- scelta costrutto;
- missione/mini-problema.

## Settimana 11 — M11

### Ora teoria attiva 1

- contatore e accumulatore;
- trace;
- `if` dentro loop.

### Ora teoria attiva 2

- media;
- min/max progressivo;
- ricerca/flag;
- invarianti intuitive.

### Ora laboratorio

- problemi integrati;
- Debug Clinic pattern;
- casi limite.

## Settimana 12 — M12

### Ora teoria attiva 1

- cicli annidati;
- coppie/griglie;
- trace a due indici.

### Ora teoria attiva 2

- quantità di lavoro;
- annidamento naturale vs accidentale;
- refactoring;
- leggibilità vs efficienza.

### Ora laboratorio

- Activity C/D;
- mini-project E;
- exit checkpoint.

---

# Exit checkpoint UDA

Prima di passare alla decomposizione formale in funzioni lo studente dovrebbe saper:

- scegliere `for` o `while` e motivarlo;
- costruire un `while` che termina;
- usare validazione ripetuta;
- usare sentinella/contatore/accumulatore;
- leggere e creare `range` con start/stop/step;
- usare `if` dentro un ciclo;
- usare un ciclo dentro una selezione;
- risolvere problemi con conteggio/somma/media/min/max progressivo;
- riconoscere ricerca del primo match vs elaborazione di tutti i match;
- leggere/scrivere un semplice ciclo annidato;
- stimare quante volte viene eseguito un corpo in semplici annidamenti;
- riconoscere almeno un caso di lavoro ripetuto inutilmente;
- diagnosticare loop infinito e off-by-one;
- progettare casi di test per i confini dell'iterazione.

---

# Valutazione/evidence

Evidence formative consigliate:

- trace `while`;
- esercizio `for` vs `while` motivato;
- debug loop infinito;
- problema contatore/accumulatore;
- problema `if` dentro ciclo;
- nested-loop trace;
- mini-project integrato.

Queste evidence alimentano la successiva prova pratica del primo quadrimestre/checkpoint A.

---

# Remediation

Per studenti in difficoltà:

1. simulare fisicamente le iterazioni con una tabella;
2. scrivere a lato il valore della condizione a ogni passo;
3. separare inizializzazione/corpo/aggiornamento;
4. partire da `for range` per ripetizioni note;
5. usare `while` su una sola variabile di stato;
6. evitare `break` finché il ciclo base non è stabile;
7. introdurre annidamento solo con range 2×3 o griglie piccole;
8. colorare variabile esterna e interna con ruoli diversi.

# Enrichment

Per studenti rapidi:

- confrontare più strategie di ricerca;
- early exit con `break` quando appropriato;
- ragionare su numero di operazioni per N e N×N;
- trovare e spostare fuori dal loop calcoli invarianti;
- generare pattern più complessi senza aumentare inutilmente la profondità di annidamento;
- missioni Romeo parametrizzate e ripetute nel simulatore.

---

# Fonti di progettazione

## Pedagogia

- *Think Python / Pensare in Python*: iteration, debugging, incremental development;
- *Learning Python / Imparare Python*: loop statements/control flow;
- Pluralsight *An Introduction to Algorithmics*: intuizione su costo e pattern;
- Pluralsight Python Essentials: coverage/lab.

## Controllo tecnico

- documentazione Python 3.12: `while`, `for`, `range`, `break`, `continue`.

## Controllo professionale

- *Fluent Python* / *Python in a Nutshell* come verifica dei modelli mentali, senza anticipare iterator protocol/comprehension avanzate.

---

# Dipendenze piattaforma

Core:

- `workspace.v1`;
- `shell.v1`;
- `python.v1` / Python 3.12;
- runner Python P1 single-file per gli esercizi autogradabili.

Optional:

- `flowchart.lab.v1` per trace visuale dei loop;
- `runtime.romeo-sim.v1` per missioni selezionate.

Nessuna missione Romeo può sostituire gli esercizi generali o richiedere hardware fisico.

---

# Criteri per passare dalla SPEC alla produzione

- vertical slice Python P1 certificato o blocker documentato;
- lesson M09–M12 revisionate;
- almeno un esempio reale per `while`, `for`, sentinella, accumulatore e nested loop;
- `for` vs `while` valutato esplicitamente in Activity;
- loop infinito/off-by-one presenti nei Debug Clinic;
- performance trattata come intuizione del lavoro, non Big-O formale;
- Romeo mapping selettivo verificato in issue #4;
- nessuna comprehension usata prima della padronanza dei loop espliciti.

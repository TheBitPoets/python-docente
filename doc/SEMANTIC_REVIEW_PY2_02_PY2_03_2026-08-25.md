# Review didattica/semantica — PY2-02 e PY2-03

> Data: 2026-08-25  
> Scope: M04–M08, lesson + deck + runbook + SPEC.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Verificare che il materiale già presente sia realmente insegnabile a una classe seconda nel vincolo:

```text
3 ore/settimana
= 2 ore teoria attiva
+ 1 ora laboratorio
```

La review non riapre il curriculum frozen. Interviene su pacing, priorità, linguaggio, retrieval, misconception, esercizi e carico cognitivo.

## Regola introdotta

Ogni modulo deve essere letto su tre livelli:

```text
MUST MASTER
  outcome senza i quali il modulo successivo diventa fragile

GUIDED EXPOSURE
  concetti che lo studente deve incontrare e usare con guida,
  ma non devono diventare un nuovo blocco di memorizzazione

ENRICHMENT / BACKUP
  materiale utile per classi rapide, recuperi inversi, approfondimenti
  o slide di riserva; non entra nell'exit gate ordinario
```

La lesson può rimanere più ricca del tempo frontale. Il runbook decide che cosa insegnare davvero in quella settimana.

---

# PY2-02 — Primi programmi Python

## M04 — Interprete, REPL, script, valori e I/O

### Giudizio

**Ben costruito / carico alto ma sostenibile con disciplina di pacing.**

Punti forti:

- parte da un algoritmo noto invece che dalla sintassi;
- prediction prima del REPL;
- distinzione `"42"` vs `42`;
- `input()` → `str` dimostrato sperimentalmente;
- REPL vs script chiarito presto;
- Error Clinic include errore logico senza traceback;
- Activity B richiede modifica minima, non riscrittura opportunistica;
- test come evidenza, non come prova assoluta.

### MUST MASTER

A fine M04 lo studente deve saper:

1. distinguere REPL e script;
2. spiegare che `input()` restituisce testo;
3. convertire con `int()` quando il problema richiede un intero;
4. seguire il flusso `input → conversione → calcolo → output`;
5. eseguire e modificare un piccolo `main.py`;
6. prevedere almeno un caso prima dell'esecuzione;
7. riconoscere che assenza di traceback non implica correttezza.

### GUIDED EXPOSURE

- nomi dei tipi `int/float/str/bool`;
- `type()` come lente;
- distinzione preliminare syntax/name/conversion error;
- lettura minima del traceback.

`bool` in M04 è **preview**. La comprensione operativa dei booleani viene formalizzata in M06.

### ENRICHMENT

- più conversioni `float`;
- esplorazioni aggiuntive con `type()`;
- input che rompe `int()`;
- quarto/quinto test progettato dagli studenti.

### Rischio da evitare

Non trasformare M04 in una lezione sulla tassonomia completa degli errori o sugli internals CPython.

---

## M05 — Espressioni, operatori e prime funzioni

### Giudizio

**Materiale forte ma sovraccarico se tutto viene trattato come core in 3 ore.**

Il rischio è sommare nella stessa settimana:

```text
/, //, %, **
+ precedenza
+ tipo/valore
+ risultati intermedi
+ built-in
+ f-string
+ prima funzione
+ return vs print
+ test di funzione
```

La soluzione non è tagliare gli outcome frozen, ma assegnare priorità.

### MUST MASTER

1. espressione → valore;
2. scelta dell'operatore dal problema;
3. distinzione `/`, `//`, `%` nei casi beginner;
4. precedenza essenziale + parentesi per rendere l'intenzione esplicita;
5. risultati intermedi con nomi significativi;
6. una prima funzione di calcolo semplice;
7. distinzione operativa `return` vs `print`;
8. tre casi per una trasformazione numerica semplice.

`**` resta core come operatore da riconoscere/usare in problemi elementari, ma non merita un blocco lungo.

### GUIDED EXPOSURE

- f-string;
- tipo risultante di `/`;
- forma `a = (a // b) * b + a % b` come controllo;
- funzione già fornita da completare/modificare.

### ENRICHMENT

- comportamento di `//` con numeri negativi;
- conversione ore/minuti/secondi più articolata;
- `abs`, `round`, `min`, `max`, `len` come panoramica delle funzioni già fornite da Python;
- confronto esteso fra più formulazioni equivalenti.

Le built-in non sono un exit outcome autonomo della settimana. In particolare `min/max` non devono sostituire il successivo apprendimento del min/max progressivo in M11.

### Modifica di pacing raccomandata

L'ora teoria 2 deve privilegiare:

```text
valore/tipo
→ leggibilità del calcolo
→ f-string breve
→ prima funzione
→ return vs print
```

Le built-in si spostano fuori dal percorso temporizzato principale.

---

# PY2-03 — Selezione e logica

## M06 — Booleani, confronti e prima selezione

### Giudizio

**Molto ben calibrato.**

Punti forti:

- frase naturale → confronto;
- focus sui confini;
- `=` vs `==`;
- `if` senza `else` prima di `if/else`;
- ramo non eseguito ≠ errore;
- indentazione come struttura;
- flow chart → codice;
- casi sotto/sulla/sopra soglia.

### MUST MASTER

1. confronto → `True/False`;
2. `=` vs `==`;
3. `< <= > >=` con confini;
4. `if` e `if/else`;
5. indentazione del blocco;
6. trace di ramo;
7. test sotto/sulla/sopra.

### ENRICHMENT

- `is` solo come avvertenza, non come argomento;
- Romeo solo dopo mastery generale;
- specifica inversa a partire dal codice.

Nessuna modifica architetturale necessaria.

---

## M07 — `elif`, casi esclusivi e logica composta

### Giudizio

**Concettualmente eccellente, ma è il secondo punto di rischio di carico cognitivo.**

Nella stessa settimana entrano:

```text
elif / first-true
if indipendenti vs catena
and / or / not
truth table
intervalli concatenati
short-circuit
```

Short-circuit non è necessario per raggiungere l'exit outcome di PY2-03.

### MUST MASTER

1. primo ramo vero in `if/elif/else`;
2. casi mutuamente esclusivi vs effetti indipendenti;
3. `and` e `or` con casi concreti;
4. `not` in forme semplici;
5. intervallo con forma esplicita e poi concatenata;
6. test di tutti i confini di una classificazione;
7. diagnosticare soglie ordinate male / rami irraggiungibili.

### GUIDED EXPOSURE

- tabelle di verità minime;
- contesto logico creato dai rami precedenti;
- confronto fra soglie crescenti/decrescenti.

### ENRICHMENT

- short-circuit;
- esempio del divisore sicuro;
- varianti Romeo multi-regola.

Short-circuit deve essere etichettato come **backup/enrichment**, non come contenuto che sottrae tempo alla distinzione `elif` vs `if` indipendenti.

---

## M08 — Annidamento, validazione e refactoring

### Giudizio

**Ben calibrato se il mini-project resta estendibile e De Morgan rimane enrichment.**

Punti forti:

- annidamento introdotto da dipendenza reale;
- path trace prima del refactoring;
- validazione di dominio separata da conversione;
- niente `while` anticipato;
- refactoring protetto da stessi casi;
- confronto struttura vs informazione persa.

### MUST MASTER

1. riconoscere una dipendenza reale fra decisioni;
2. seguire un path annidato;
3. validare il dominio prima di classificare;
4. distinguere valore fuori dominio da conversione impossibile;
5. confrontare annidamento e condizione composta;
6. preservare gli stessi casi durante un refactoring;
7. motivare la struttura scelta.

### GUIDED EXPOSURE

- booleano nominato;
- idea di copertura dei path senza metriche quantitative;
- mini-project integrato se il tempo lo consente.

### ENRICHMENT

- De Morgan;
- confronto fra più refactoring equivalenti;
- Romeo path trace.

Il mini-project può proseguire come compito/recupero: non deve comprimere l'handoff a `while`.

---

# Coerenza verticale M04 → M08

La progressione risulta didatticamente solida:

```text
M04
valori / input / output / errori
        ↓
M05
espressioni / trasformazioni / prima funzione
        ↓
M06
confronto → bool → ramo
        ↓
M07
più casi / casi indipendenti / logica composta
        ↓
M08
dipendenze / path / validazione / refactor
        ↓
M09
while / stato / validazione ripetuta
```

Non sono emersi prerequisiti invertiti o concetti core collocati nel modulo sbagliato.

---

# Regole di delivery approvate dalla review

1. **La lesson è una risorsa, non uno script da recitare integralmente.**
2. Il runbook definisce la priorità temporale.
3. Ogni modulo chiude con 4–7 outcome osservabili di mastery, non con una lista di termini ricordati.
4. Gli studenti devono produrre evidence: prediction, trace, codice, test, spiegazione.
5. Romeo resta applicazione dopo la comprensione generale.
6. Non si aggiunge una nuova Activity autogradata solo per “coprire” un modulo finché il profilo TheBitLab necessario non è certificato.
7. Enrichment non compare nella verifica ordinaria se non è stato realmente svolto.

# Esito

```text
PY2-02 architecture/order     PASS
M04 pacing                    PASS with explicit mastery gate
M05 pacing                    PASS after priority tiering
PY2-03 architecture/order     PASS
M06 pacing                    PASS
M07 pacing                    PASS after short-circuit demotion
M08 pacing                    PASS with De Morgan/mini-project optional
```

Nessun curriculum change richiesto.

## Next review

Dopo le correzioni ai runbook/deck:

```text
PY2-04 — M09–M12
```

con focus specifico su:

- `while` vs `for`;
- terminazione e off-by-one;
- accumulatore/contatore/min-max;
- nested loops;
- rischio di insegnare pattern come formule invece che come invarianti di stato.

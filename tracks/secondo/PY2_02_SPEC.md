# PY2-02 — Primi programmi Python

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 4–5;
- monte ore nominale: 6 ore;
- organizzazione reale: 2 ore teoria attiva + 1 ora laboratorio per settimana;
- prerequisito didattico: PY2-01, capacità di leggere un problema semplice, individuare input/output e seguire un algoritmo;
- baseline runtime: Python 3.12 nel Classroom Environment TheBitLab;
- output: lo studente sa usare il REPL per esplorare espressioni e tipi, trasformare un piccolo algoritmo in uno script Python, leggere input, produrre output, convertire dati e diagnosticare errori elementari.

## Perché questa UDA esiste

La transizione da algoritmo a codice deve mantenere il modello mentale costruito nella UDA precedente:

```text
problema
→ algoritmo
→ dati
→ istruzioni Python
→ esecuzione
→ output
→ confronto con il risultato atteso
```

Il primo obiettivo non è memorizzare molta sintassi, ma capire che Python è un linguaggio con cui esprimere istruzioni precise e osservabili.

---

# M04 — Interprete, REPL, script, valori e I/O

## Obiettivi osservabili

Lo studente sa:

1. distinguere REPL e file `.py`;
2. eseguire un'espressione nel REPL e prevederne il risultato;
3. riconoscere valori `int`, `float`, `str`, `bool` a livello introduttivo;
4. assegnare un valore a un nome;
5. usare `print()`;
6. usare `input()` e sapere che restituisce testo;
7. applicare conversioni semplici con `int()`, `float()` e `str()`;
8. leggere un traceback molto semplice e distinguere almeno errore di sintassi, errore di nome e conversione fallita;
9. salvare ed eseguire un piccolo script `.py` dentro il workspace gestito TheBitLab;
10. verificare manualmente l'output su più casi.

## Modello mentale

### REPL

Il REPL è un laboratorio per una istruzione/espressione alla volta:

```text
Read
→ Eval
→ Print
→ Loop
```

Serve a esplorare, formulare ipotesi e vedere subito il risultato.

### Script

Uno script è una sequenza salvata di istruzioni ripetibile:

```text
file .py
→ interprete
→ istruzioni in ordine
→ stato che cambia
→ output/errori
```

## Concetti core

- interprete Python;
- prompt del REPL;
- espressione vs istruzione a livello intuitivo;
- literal;
- nomi/variabili;
- assegnamento;
- `print()`;
- `input()`;
- tipi fondamentali introduttivi;
- conversione;
- esecuzione sequenziale;
- errore come informazione diagnostica.

## Sequenza didattica consigliata

### 1. Prevedi prima di eseguire

Domande REPL del tipo:

```python
2 + 3
10 / 2
10 // 3
"ciao"
len("ciao")
```

Prima previsione, poi esecuzione.

### 2. Dai un nome a un valore

```python
eta = 15
eta
eta + 1
```

Mostrare che il nome e il valore non sono la stessa cosa.

### 3. Primo I/O

```python
nome = input()
print(nome)
```

Poi:

```python
eta = int(input())
print(eta + 1)
```

## Error clinic

Bug/esempi obbligatori:

- parentesi o virgolette mancanti;
- nome scritto diversamente;
- `input()` trattato come numero senza conversione;
- `int("ciao")`;
- differenza tra `"2" + "3"` e `2 + 3`;
- output extra che rompe un contratto di test deterministico.

## Activity candidate

### A — Observe / Predict

**Titolo:** `Prima prevedi, poi prova`

Serie di espressioni REPL. Lo studente compila prima una tabella previsione, poi verifica nel REPL e corregge la propria spiegazione.

### B — Controlled Change — vertical slice TheBitLab

**Titolo:** `Completa la somma`

Starter già predisposto:

- legge due interi;
- contiene una variabile `risultato` volutamente errata;
- stampa il risultato.

Lo studente modifica solo il calcolo.

Questa Activity è il primo canarino tecnico per:

```text
Course Workspace
→ Activity 1.0
→ scaffold main.py
→ Python runner core
→ Docker grading
→ report deterministico
```

### C — Implement

**Titolo:** `Età tra N anni`

Leggere età e incremento, calcolare il valore futuro e stamparlo. Prima input/output ed esempio, poi codice.

### D — Debug

**Titolo:** `Stringa o numero?`

Correggere piccoli programmi che concatenano o convertono dati in modo errato.

## Regola output per Activity autogradate beginner

Quando il focus è la logica e non l'interfaccia utente, evitare prompt come:

```python
input("Inserisci il numero: ")
```

se il test confronta `stdout` esatto.

Usare preferibilmente:

```python
numero = int(input())
```

La lesson spiega che in applicazioni reali un'interfaccia può avere prompt e messaggi; qui il contratto di I/O è volutamente minimale per rendere osservabile la trasformazione input → output.

---

# M05 — Espressioni, operatori e prime funzioni

## Obiettivi osservabili

Lo studente sa:

- costruire espressioni aritmetiche leggibili;
- usare `+`, `-`, `*`, `/`, `//`, `%`, `**` quando appropriato;
- leggere la precedenza degli operatori e usare parentesi per chiarezza;
- distinguere `/` e `//`;
- usare `%` in problemi semplici;
- usare f-string per output leggibile;
- chiamare built-in semplici come `abs`, `round`, `len`, `min`, `max` quando già comprensibili;
- definire una prima funzione minuscola senza trasformare ancora l'UDA in un corso formale sulle funzioni;
- distinguere calcolo e presentazione;
- scegliere nomi comprensibili.

## Perché anticipare una piccola funzione

Non vogliamo far passare implicitamente questo modello:

```text
programma = un unico blocco di righe
```

Mostriamo quindi presto che una trasformazione può avere un nome:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Senza entrare ancora in scope, progettazione top-down o API: questi arriveranno formalmente in PY2-05.

## Pattern di problemi

- prezzo, quantità e totale;
- conversioni di unità semplici;
- area/perimetro;
- secondi → minuti/resto;
- divisione con quoziente/resto;
- media di pochi valori;
- distanza o formula numerica molto semplice.

## Confronto di soluzioni

Esempio:

```python
x = a + b * c
```

vs

```python
x = a + (b * c)
```

vs decomposizione in risultati intermedi quando chiarisce il significato.

Criterio:

```text
correttezza
→ chiarezza
→ assenza di lavoro inutile
```

## Activity candidate

### A — Trace espressioni

Calcolare a mano tipo e valore di espressioni brevi.

### B — Controlled Change

Cambiare formula mantenendo invariato il contratto di input/output.

### C — Implement

Problema numerico completo con analisi, algoritmo, script e almeno tre casi di test.

### D — Debug

Errori di precedenza, conversione, divisione, nomi e output.

### E — Mini-programma

Piccolo calcolatore testuale a operazione unica, senza selezioni complesse che appartengono all'UDA successiva.

---

# Piano delle due settimane

## Settimana 4

### Ora teoria attiva 1

- algoritmo → Python;
- interprete/REPL;
- previsione ed esecuzione;
- valori, nomi, assegnamento;
- micro-task al REPL.

### Ora teoria attiva 2

- `print`, `input`, tipi e conversioni;
- error clinic;
- primo script `.py`;
- esecuzione dal Classroom Environment.

### Ora laboratorio

- Activity A breve;
- Activity B `Completa la somma`;
- lettura del report deterministico;
- correzione ragionata degli errori.

## Settimana 5

### Ora teoria attiva 1

- operatori;
- precedenza;
- `/`, `//`, `%`;
- trace di espressioni;
- confronto fra forme equivalenti.

### Ora teoria attiva 2

- f-string;
- built-in essenziali;
- prima funzione minuscola;
- naming e separazione calcolo/output.

### Ora laboratorio

- Activity C/D;
- mini-problema integrato;
- exit checkpoint.

---

# Exit checkpoint UDA

Prima di entrare in selezione/logica lo studente dovrebbe saper:

- aprire il REPL gestito e provare un'espressione;
- eseguire un file `.py`;
- leggere dati con `input()`;
- convertire testo in numero quando necessario;
- usare variabili e operatori;
- produrre output esatto;
- prevedere il risultato di una sequenza lineare breve;
- leggere un errore semplice e indicare la riga probabile;
- verificare lo stesso programma con almeno due input differenti;
- spiegare a parole il passaggio algoritmo → istruzioni Python.

---

# Valutazione formativa

Evidence consigliate:

- tabella di previsione REPL;
- 1 trace di script;
- 1 Activity B autogradata;
- 1 debug task;
- 1 piccolo programma C;
- breve spiegazione di un errore incontrato.

Non è necessario un voto principale in questa UDA.

---

# Remediation

Per studenti in difficoltà:

1. una sola variabile alla volta nel REPL;
2. valori concreti, poi nomi;
3. separare lettura, conversione, calcolo, stampa su quattro righe;
4. confrontare `"2"` e `2` visualmente e con `type()`;
5. leggere traceback corti indicando solo ultima riga e riga del proprio file;
6. starter controllati prima della scrittura autonoma.

# Enrichment

Per studenti rapidi:

- confrontare formulazioni equivalenti;
- provare edge case numerici;
- sperimentare `type()` e `repr()` con guida;
- introdurre una funzione pura minuscola;
- scrivere casi di test prima del programma.

---

# Fonti di progettazione

## Pedagogia

- *Think Python / Pensare in Python*: modello di esecuzione, valori, variabili, funzioni, debugging;
- *Learning Python / Imparare Python*: controllo sistematico di tipi, espressioni, statement e funzioni;
- Pluralsight Python Essentials: confronto coverage/lab e workflow beginner.

## Riferimento tecnico

- documentazione Python 3.12: tutorial, built-in types, built-in functions.

Le fonti sono riferimenti per materiale originale; non copiare testi/esercizi licensed.

---

# Dipendenze piattaforma

## Richieste

- `workspace.v1`;
- `shell.v1`;
- `python.v1` baseline 3.12.

## Editor

VS Code non è prerequisito per completare la UDA finché l'integrazione gestita non è certificata. Il core deve poter funzionare da shell/REPL e file `.py` nel workspace TheBitLab.

## Grading

Per le Activity autogradate di questa UDA:

```text
Activity 1.0
language = python
single main.py
stdin/stdout deterministic tests
Docker grading authoritative
AI feedback = false
```

Nessun runtime plugin specifico.

---

# Criteri per passare dalla SPEC alla lesson

- workflow REPL/script nel Classroom Environment certificato;
- Activity B validata con schema/scaffold/runner reali;
- Python 3.12 confermato nel profilo corso;
- esempi/error clinic revisionati;
- lesson M04/M05 prodotte come contenuto originale;
- slide e teacher notes generate soltanto dopo la validazione del vertical slice.

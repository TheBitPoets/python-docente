# M04 — Interprete, REPL, script, valori e input/output

> **Stato:** draft / vertical slice di authoring  
> **UDA:** PY2-02 — Primi programmi Python  
> **Baseline:** Python 3.12 nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- spiegare in modo semplice che cosa fa l'interprete Python;
- usare il REPL per provare un'espressione alla volta;
- distinguere un valore, un nome/variabile e un'espressione;
- riconoscere i tipi fondamentali `int`, `float`, `str` e `bool` nei casi più semplici;
- assegnare un valore a una variabile;
- usare `print()` per produrre output;
- usare `input()` e ricordare che restituisce una stringa;
- convertire dati con `int()`, `float()` e `str()` quando serve;
- salvare ed eseguire un piccolo programma `.py`;
- leggere la parte essenziale di un errore/traceback;
- provare lo stesso programma con più casi e confrontare risultato atteso e ottenuto.

## Prerequisiti

Dovresti già saper, almeno su problemi semplici:

- individuare input e output;
- descrivere un algoritmo come passi ordinati;
- eseguire un trace manuale;
- proporre qualche caso di test.

Non serve conoscere già Python.

---

# 1. Problema iniziale: dal procedimento al programma

Considera questo problema:

> Leggi due numeri interi e mostra la loro somma.

Prima del codice possiamo descriverlo così:

```text
INPUT: primo numero, secondo numero
OUTPUT: somma

1. acquisisci il primo numero
2. acquisisci il secondo numero
3. calcola primo + secondo
4. mostra il risultato
```

Il programma Python non inventa la soluzione: **traduce questo algoritmo in istruzioni che l'interprete può eseguire**.

Una possibile traduzione è:

```python
primo = int(input())
secondo = int(input())
risultato = primo + secondo
print(risultato)
```

Non preoccuparti ancora di ricordare tutto. In questo modulo smonteremo il programma riga per riga.

---

# 2. Che cosa fa l'interprete Python

Un file Python contiene testo con istruzioni Python.

Quando esegui:

```text
python programma.py
```

stai chiedendo all'interprete Python di leggere ed eseguire il programma.

Un modello mentale sufficiente per iniziare è:

```text
sorgente .py
    ↓
interprete Python
    ↓
esecuzione delle istruzioni
    ↓
output oppure errore
```

Python svolge internamente molti passaggi più complessi, ma non servono ancora per capire i primi programmi. Più avanti potremo approfondire bytecode, virtual machine e modello di esecuzione.

## Una regola utile

Il computer non esegue ciò che **intendevi** scrivere.

Esegue ciò che il programma **dice realmente**, secondo le regole del linguaggio.

Per questo impariamo a:

```text
prevedere
→ eseguire
→ osservare
→ confrontare
→ correggere
```

---

# 3. Il REPL: un laboratorio per fare esperimenti

Python può essere usato in modalità interattiva.

Nel Classroom Environment apri il REPL Python secondo il comando/launcher indicato dalla guida TheBitLab. Vedrai un prompt simile a:

```text
>>>
```

REPL significa:

```text
Read   → leggi ciò che scrivi
Eval   → valutalo/eseguilo
Print  → mostra il risultato quando appropriato
Loop   → torna al prompt
```

## Primo esperimento

Prima **prevedi** il risultato:

```python
2 + 3
```

Poi esegui.

Dovresti osservare:

```text
5
```

Prova allo stesso modo:

```python
10 - 4
3 * 5
10 / 2
```

## Il REPL non è un indovino

Se scrivi:

```python
2 +
```

l'espressione non rispetta la sintassi richiesta e Python segnala un errore.

Un errore non è una sconfitta: è **informazione sul programma che hai realmente scritto**.

---

# 4. Valori e tipi

Un programma lavora con dati.

Python distingue diversi tipi di valore.

## Interi: `int`

```python
42
-7
0
```

sono valori interi.

Nel REPL:

```python
>>> type(42)
<class 'int'>
```

## Numeri con parte decimale: `float`

```python
3.5
-0.25
2.0
```

Nel REPL:

```python
>>> type(3.5)
<class 'float'>
```

## Testo: `str`

```python
"ciao"
"42"
"Python"
```

sono stringhe.

Nota importante:

```text
42      numero intero
"42"    testo formato dai caratteri 4 e 2
```

Non sono lo stesso valore.

## Booleani: `bool`

I valori booleani sono:

```python
True
False
```

Diventeranno fondamentali quando studieremo le decisioni con `if`.

---

# 5. Variabili: dare un nome a un valore

Nel REPL prova:

```python
eta = 15
```

Poi:

```python
eta
```

Il risultato è:

```text
15
```

Possiamo usare il nome in un'espressione:

```python
eta + 1
```

## Modello mentale iniziale

Per ora pensa a:

```text
eta ──> 15
```

Il nome `eta` permette di riferirsi al valore.

Più avanti renderemo questo modello più preciso quando studieremo oggetti, mutabilità e alias.

## `=` non significa "è uguale" nel senso matematico

In:

```python
eta = 15
```

`=` rappresenta un **assegnamento**: associa il nome `eta` al valore prodotto a destra.

Se poi scrivi:

```python
eta = 16
```

il nome ora fa riferimento al nuovo valore.

## Nomi leggibili

Preferisci:

```python
prezzo_totale = 25
```

rispetto a:

```python
x = 25
```

quando il nome aiuta a capire il significato del dato.

Un nome breve non è automaticamente migliore.

---

# 6. `print()`: produrre output

Nel REPL:

```python
print("ciao")
```

mostra:

```text
ciao
```

Possiamo stampare una variabile:

```python
nome = "Anna"
print(nome)
```

oppure un'espressione:

```python
print(2 + 3)
```

## REPL e `print()` non sono la stessa cosa

Nel REPL:

```python
>>> 2 + 3
5
```

il REPL visualizza il valore dell'espressione.

In un file `.py`, invece:

```python
2 + 3
```

calcola il valore, ma non hai chiesto al programma di mostrarlo.

Per produrre l'output:

```python
print(2 + 3)
```

Questa differenza è importante nel passaggio REPL → script.

---

# 7. `input()`: ricevere dati

Prova:

```python
nome = input()
```

Il programma aspetta che tu scriva qualcosa e prema Invio.

Poi:

```python
print(nome)
```

## Il punto fondamentale: `input()` restituisce testo

Anche se digiti:

```text
12
```

il risultato di `input()` è una stringa.

Verificalo:

```python
dato = input()
print(type(dato))
```

Se digiti `12`, vedrai comunque:

```text
<class 'str'>
```

---

# 8. Perché `"2" + "3"` non fa `5`

Prima prevedi:

```python
"2" + "3"
```

Il risultato è:

```text
'23'
```

Per le stringhe, `+` concatena testo.

Con gli interi:

```python
2 + 3
```

il risultato è:

```text
5
```

Il simbolo è lo stesso, ma l'operazione dipende dai tipi coinvolti.

Questa è una delle ragioni per cui **capire i tipi** è importante.

---

# 9. Conversioni: trasformare il dato quando il problema lo richiede

Se vuoi usare come numero ciò che è stato letto con `input()`, devi convertirlo.

```python
testo = input()
numero = int(testo)
```

Spesso si scrive direttamente:

```python
numero = int(input())
```

## `int()`

Converte un testo compatibile in intero:

```python
int("42")
```

produce:

```text
42
```

Ma:

```python
int("ciao")
```

non può produrre un intero valido e genera un errore.

## `float()`

```python
float("3.5")
```

produce un `float`.

## `str()`

```python
str(42)
```

produce il testo:

```text
"42"
```

## Non convertire per abitudine

La domanda deve essere:

> Quale tipo mi serve per l'operazione che devo fare?

Se stai leggendo un nome, non ha senso convertirlo in `int`.

---

# 10. Dal REPL al primo script

Un esperimento REPL scompare quando chiudi la sessione.

Un programma che vuoi conservare e rieseguire va scritto in un file.

Crea nel workspace gestito dal corso un file:

```text
main.py
```

con:

```python
nome = input()
print(nome)
```

Eseguilo con il workflow TheBitLab indicato dalla guida.

## Perché passare presto agli script

Il REPL è ottimo per:

- esperimenti;
- espressioni;
- controllare un'ipotesi;
- capire un errore piccolo.

Lo script è migliore quando vuoi:

- conservare il programma;
- eseguirlo di nuovo;
- modificarlo;
- testarlo;
- versionarlo;
- costruire qualcosa di più grande.

Non sono concorrenti: sono strumenti diversi.

---

# 11. Microscope: esegui mentalmente questo programma

Prima di provarlo, completa il trace:

```python
primo = 4
secondo = 6
risultato = primo + secondo
print(risultato)
```

| Passo | `primo` | `secondo` | `risultato` | output |
|---|---:|---:|---:|---|
| dopo riga 1 | 4 | — | — | — |
| dopo riga 2 | 4 | 6 | — | — |
| dopo riga 3 | 4 | 6 | ? | — |
| dopo riga 4 | 4 | 6 | ? | ? |

Soltanto dopo eseguilo.

## Variante

Cambia:

```python
secondo = -2
```

Prevedi di nuovo prima dell'esecuzione.

Questa abitudine — **predict before run** — continuerà per tutto il corso.

---

# 12. Worked example: somma di due numeri letti dall'utente

Riprendiamo il problema iniziale.

## Specifica

```text
INPUT: due interi, uno per riga
OUTPUT: la loro somma
```

## Casi di test prima del codice

| input 1 | input 2 | output atteso |
|---:|---:|---:|
| 2 | 3 | 5 |
| 0 | 0 | 0 |
| -4 | 10 | 6 |

## Codice

```python
primo = int(input())
secondo = int(input())
risultato = primo + secondo
print(risultato)
```

## Trace con `-4` e `10`

```text
input()             → "-4"
int("-4")           → -4
primo               → -4

input()             → "10"
int("10")           → 10
secondo             → 10

primo + secondo     → 6
risultato           → 6
print(risultato)    → mostra 6
```

Notare la distinzione tra:

```text
"10"   stringa letta
10      intero ottenuto dopo conversione
```

---

# 13. Confronto: due programmi che sembrano simili

## Versione A

```python
primo = input()
secondo = input()
print(primo + secondo)
```

Con input:

```text
2
3
```

produce:

```text
23
```

## Versione B

```python
primo = int(input())
secondo = int(input())
print(primo + secondo)
```

produce:

```text
5
```

## Domanda

Entrambi i programmi "funzionano" nel senso che Python li esegue.

Ma soltanto uno rispetta la specifica **somma di due interi**.

Quindi:

> programma eseguibile ≠ programma corretto rispetto al problema.

---

# 14. Error Clinic

Gli errori fanno parte del lavoro del programmatore.

## Caso 1 — errore di sintassi

```python
print("ciao"
```

Python non riesce a interpretare correttamente la struttura del programma.

Non guardare cento righe a caso. Inizia dall'informazione che l'errore fornisce e dalla riga indicata, controllando anche ciò che la precede.

## Caso 2 — nome non definito

```python
prezzo = 10
print(prezzo_totale)
```

Hai assegnato un valore a `prezzo`, ma chiedi di usare `prezzo_totale`.

Python non corregge automaticamente il nome in base a ciò che probabilmente intendevi.

## Caso 3 — conversione impossibile

```python
numero = int("ciao")
```

La sintassi è valida, ma il valore non può essere convertito nel modo richiesto.

## Caso 4 — errore logico

```python
primo = int(input())
secondo = int(input())
risultato = primo - secondo
print(risultato)
```

Il programma può terminare senza traceback, ma non calcola ciò che la specifica chiede.

Questo è un punto fondamentale:

```text
nessun errore Python
≠
soluzione corretta
```

I casi di test ci aiutano a scoprirlo.

---

# 15. Come leggere un traceback beginner

Non devi capire subito ogni riga.

Per ora usa questa strategia:

1. individua il **tipo di errore** nell'ultima parte;
2. leggi il messaggio;
3. individua la riga del tuo file indicata;
4. collega l'errore a ciò che quella riga sta tentando di fare;
5. modifica una cosa alla volta;
6. riesegui il caso che falliva.

Esempio concettuale:

```text
ValueError: invalid literal for int() ...
```

Domanda utile:

> quale testo sto tentando di convertire in intero?

Non:

> come faccio a far sparire il messaggio?

---

# 16. Output deterministico e TheBitLab

In alcune Activity automatiche il contratto dice esattamente quale output deve produrre il programma.

Se la specifica è:

```text
leggi due interi e stampa soltanto la somma
```

questa soluzione è coerente:

```python
primo = int(input())
secondo = int(input())
print(primo + secondo)
```

Questa invece aggiunge output non richiesto:

```python
primo = int(input("Inserisci il primo numero: "))
secondo = int(input("Inserisci il secondo numero: "))
print("La somma è", primo + secondo)
```

In un'applicazione reale i prompt possono essere utilissimi. Qui, però, **l'interfaccia testuale non è l'obiettivo** e il test automatico deve poter confrontare input e output in modo deterministico.

La regola non è "non usare mai prompt".

La regola è:

> rispetta il contratto dell'interfaccia che stai implementando.

---

# 17. Activity B — Completa la somma

Il primo vertical slice TheBitLab del corso è:

```text
py2-activity-b-input-somma-001
```

Ricevi uno starter simile a:

```python
primo = int(input())
secondo = int(input())
risultato = 0
print(risultato)
```

Devi modificare **soltanto ciò che serve** affinché rispetti la specifica.

Prima di eseguire, prevedi l'output per:

```text
2, 3
0, 0
-4, 10
```

Poi usa il report per confrontare il comportamento reale con quello atteso.

## Perché è un'Activity B

Non stai progettando ancora tutto il programma da zero.

Stai facendo una **modifica controllata** a una struttura già comprensibile.

In Activity successive passeremo a implementazione autonoma, debug e mini-progetti.

---

# 18. Esercizi brevi

## A — Prevedi il tipo e il valore

Senza REPL, scrivi prima la previsione:

```python
3 + 4
"3" + "4"
int("8") + 2
str(5)
```

Poi verifica.

## B — Trova la differenza

Spiega perché:

```python
eta = input()
print(eta + "1")
```

non significa "aumenta l'età di uno".

Scrivi poi la versione corretta per un'età intera.

## C — Dal problema al codice

Specifica:

> Leggi un numero intero e mostra il suo doppio.

Produci:

1. input;
2. output;
3. algoritmo;
4. due casi di test;
5. codice.

## D — Debug

Correggi il programma:

```python
prezzo = int(input())
quantita = int(input())
totale = prezzo + quantita
print(totale)
```

se la specifica chiede il costo totale di `quantita` pezzi allo stesso prezzo.

Non limitarti a cambiare il simbolo: spiega perché.

---

# 19. Verifica rapida

Rispondi senza eseguire Python.

1. Che tipo restituisce `input()`?
2. Che differenza c'è tra `42` e `"42"`?
3. A cosa serve `int()` in `int(input())`?
4. Perché il REPL mostra il risultato di `2 + 3`, mentre una riga `2 + 3` in uno script non produce necessariamente output visibile?
5. Un programma senza traceback è sicuramente corretto? Perché?
6. Qual è il primo passo utile quando compare un traceback?

Dopo aver risposto, verifica con piccoli esperimenti soltanto le risposte di cui non sei sicuro.

---

# 20. Sintesi

Porta con te questi modelli:

```text
Python esegue il programma scritto, non quello immaginato.
```

```text
input() → str
```

```text
conversione solo quando serve al tipo di operazione
```

```text
REPL = esperimento rapido
script = programma salvato/ripetibile
```

```text
prevedi → esegui → confronta → correggi
```

```text
nessun traceback ≠ correttezza
```

Nel prossimo modulo useremo espressioni e operatori con maggiore precisione e inizieremo a dare un nome a piccole trasformazioni tramite funzioni.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione e verifica tecnica usa:

- Allen Downey, *Think Python / Pensare in Python* — modello beginner, valori/variabili/funzioni/debugging;
- Mark Lutz, *Learning Python / Imparare Python* — coverage di tipi, espressioni e statement;
- documentazione Python 3.12 — tutorial, built-in `input`, `print`, `int`, `float`, `str`, `type`;
- Pluralsight Python Essentials — gap-check di percorso/laboratorio.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

## Activity correlate

- `py2-activity-b-input-somma-001` — **Completa la somma**.

## Collegamenti di progettazione

- `tracks/secondo/PY2_02_SPEC.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`;
- `tracks/secondo/ARCHITECTURE_REVIEW.md`.

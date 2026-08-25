# M11 — Contatori, accumulatori, minimo/massimo, ricerca e flag

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-04 — Iterazione e pattern algoritmici  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- riconoscere quando un problema richiede un contatore oppure un accumulatore;
- usare `if` dentro `for` e `while` per elaborare solo i casi rilevanti;
- mantenere una somma progressiva e ricavarne una media quando il conteggio è valido;
- mantenere un minimo o un massimo progressivo senza usare valori-sentinella arbitrari;
- distinguere “trova il primo” da “conta/trova tutti”;
- usare un flag booleano quando rappresenta davvero uno stato utile;
- riconoscere quando un flag è ridondante;
- progettare casi di test per nessun match, un match, più match e confini significativi;
- descrivere con una frase che cosa rappresenta una variabile durante il ciclo.

---

# 1. Il problema non è il ciclo: è che cosa devo ricordare

Considera una sequenza di valori:

```text
4  -2  7  0  5
```

Potremmo voler sapere:

- quanti sono positivi;
- qual è la loro somma;
- qual è il valore più piccolo;
- se compare almeno uno zero;
- dove si trova il primo valore maggiore di 6.

Il ciclo attraversa i dati. La parte importante è capire **quale informazione deve sopravvivere da un'iterazione alla successiva**.

Modello:

```text
valore corrente
      ↓
condizione / elaborazione
      ↓
stato aggiornato
      ↓
iterazione successiva
```

Quello stato può essere un contatore, un totale, un minimo, un massimo, un flag o un risultato di ricerca.

---

# 2. Pattern contatore

Problema:

> Leggi `N` valori e conta quanti sono positivi.

Una forma tipica è:

```python
conteggio = 0

for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1

print(conteggio)
```

## Invariante intuitivo

Dopo ogni iterazione:

> `conteggio` è il numero di valori positivi già elaborati.

Questa frase ci permette di controllare il programma.

Se `conteggio += 1` fosse fuori dall'`if`, la frase non sarebbe più vera.

## Trace

Per i valori:

```text
4, -2, 7
```

| valore | `valore > 0` | `conteggio` dopo l'iterazione |
|---:|---|---:|
| 4 | True | 1 |
| -2 | False | 1 |
| 7 | True | 2 |

---

# 3. Pattern accumulatore

Problema:

> Calcola la somma di `N` valori.

```python
totale = 0

for _ in range(n):
    valore = int(input())
    totale += valore

print(totale)
```

## Invariante

> `totale` è la somma dei valori già elaborati.

Questa frase spiega perché `totale` deve essere inizializzato **prima** del ciclo.

Errore classico:

```python
for _ in range(n):
    totale = 0
    valore = int(input())
    totale += valore
```

Qui il totale viene azzerato a ogni iterazione.

---

# 4. Contatore + accumulatore: la media

Per una media servono almeno:

```text
somma
conteggio
```

Se il numero di valori è noto e tutti sono validi:

```python
totale = 0

for _ in range(n):
    totale += int(input())

media = totale / n
```

Ma se contiamo soltanto i valori che soddisfano una condizione:

```python
totale = 0
conteggio = 0

for _ in range(n):
    valore = int(input())
    if valore >= 0:
        totale += valore
        conteggio += 1
```

prima della divisione dobbiamo chiederci:

> `conteggio` può essere zero?

Una soluzione deve gestire esplicitamente quel caso.

---

# 5. Minimo e massimo progressivo

Problema:

> Tra più valori trova il minimo.

Una cattiva abitudine è inventare una sentinella numerica:

```python
minimo = 999999
```

Funziona soltanto se il dominio garantisce che nessun valore possa essere maggiore o uguale a quella scelta. Se il dominio cambia, il programma può diventare sbagliato.

## Strategia robusta con primo dato

Se sappiamo che esiste almeno un valore:

```python
minimo = int(input())

for _ in range(n - 1):
    valore = int(input())
    if valore < minimo:
        minimo = valore

print(minimo)
```

## Invariante

> `minimo` è il più piccolo valore visto finora.

Per il massimo:

> `massimo` è il più grande valore visto finora.

Queste frasi sono più importanti della forma esatta del codice.

---

# 6. Ricerca: primo match oppure tutti i match?

Domanda:

> Tra i valori compare almeno un numero uguale a 0?

Se ci interessa soltanto sapere se esiste, possiamo fermarci al primo match.

Esempio concettuale:

```python
trovato = False

for _ in range(n):
    valore = int(input())
    if valore == 0:
        trovato = True
```

Al termine:

```python
if trovato:
    print("presente")
else:
    print("assente")
```

## Ma devo davvero leggere tutti i valori?

Dipende dal contratto del problema.

Se i dati arrivano da una struttura già disponibile, una ricerca del primo match può fermarsi con `break`.

Se i dati arrivano uno alla volta da input e il contratto richiede comunque di consumarli tutti, il comportamento può essere diverso.

Il pattern non si sceglie isolatamente: dipende dall'interfaccia e dall'obiettivo.

---

# 7. Flag booleani

Un flag è una variabile booleana che rappresenta uno stato significativo.

Esempio:

```python
trovato = False
```

Invariante:

> `trovato` indica se finora abbiamo incontrato almeno un valore che soddisfa la ricerca.

## Flag utile

Quando il valore booleano viene usato dopo il ciclo o rappresenta chiaramente uno stato.

## Flag ridondante

Se serve solo per imitare una condizione già disponibile o se un `break`/`return` futuro renderebbe il flusso più diretto.

Non esiste la regola “i flag sono sbagliati”. La domanda è:

> questa variabile aggiunge significato o aggiunge soltanto meccanica?

---

# 8. Selezione dentro iterazione

Molti algoritmi combinano:

```text
ripeti
→ osserva un valore
→ decidi se interessa
→ aggiorna lo stato
```

Esempio: conta quanti valori sono compresi tra 10 e 20 inclusi.

```python
conteggio = 0

for _ in range(n):
    valore = int(input())
    if 10 <= valore <= 20:
        conteggio += 1
```

Questo è un uso naturale di `if` dentro `for`.

---

# 9. Ciclo dentro una decisione

Anche il contrario può essere naturale:

```python
if n > 0:
    for _ in range(n):
        ...
else:
    print("nessun dato")
```

Il punto non è collezionare combinazioni sintattiche.

La domanda resta:

> la struttura rappresenta davvero il problema?

---

# 10. Worked example: statistiche sui valori positivi

Specifica:

> Leggi `N` interi. Stampa quanti sono positivi e la loro somma.

Casi da progettare prima:

| valori | positivi | somma positiva |
|---|---:|---:|
| `2, 5, -1` | 2 | 7 |
| `-3, 0, -2` | 0 | 0 |
| `4` | 1 | 4 |

Codice:

```python
n = int(input())
conteggio = 0
totale = 0

for _ in range(n):
    valore = int(input())
    if valore > 0:
        conteggio += 1
        totale += valore

print(conteggio)
print(totale)
```

Invarianti:

```text
conteggio = numero di positivi già visti
totale    = somma dei positivi già visti
```

---

# 11. Error Clinic

## A — accumulatore resettato

```python
for _ in range(n):
    totale = 0
    totale += int(input())
```

Domanda: quale invariante viene distrutto?

## B — contatore incrementato sempre

```python
if valore > 0:
    print(valore)
conteggio += 1
```

Se volevamo contare soltanto i positivi, l'aggiornamento è nel livello sbagliato.

## C — media con denominatore zero

```python
media = totale / conteggio
```

Quale caso di test lo mette in crisi?

## D — minimo sentinella fragile

```python
minimo = 999999
```

Quale assunzione nascosta stiamo facendo?

## E — flag mai aggiornato

```python
trovato = False
for ...:
    if condizione:
        print("trovato")
```

Dopo il ciclo `trovato` è ancora `False`.

---

# 12. Ricerca lineare: ragionare sul lavoro

Se controlliamo i valori uno dopo l'altro, nel caso peggiore possiamo doverli esaminare tutti.

Per ora basta questa intuizione:

```text
più dati
→ più confronti
```

Non introduciamo ancora il formalismo Big-O.

Ma iniziamo a distinguere:

- ricerca del primo match;
- conteggio di tutti i match;
- elaborazione completa obbligatoria.

Queste tre richieste possono produrre algoritmi diversi.

---

# 13. Activity candidate

## A — Trace pattern

Completa tabelle con `conteggio`, `totale`, `minimo` e `trovato` dopo ogni iterazione.

## B — Controlled Change

Trasforma “conta positivi” in “conta valori nell'intervallo `[10, 20]`”, aggiornando prima i casi di test.

## C — Implement

Leggi `N` dati e calcola:

- somma;
- conteggio di quelli validi;
- eventuale media solo se il conteggio è diverso da zero.

## D — Debug

Correggi accumulatori resettati, update fuori dal ramo, minimo inizializzato male e flag incoerenti.

Nessuna nuova Activity autogradata viene materializzata finché il profilo P1 canarino non è certificato.

---

# 14. Romeo come applicazione selettiva

Una missione simulata può richiedere di:

- contare quante azioni soddisfano una condizione;
- accumulare una distanza/tempo concettuale;
- rilevare se un checkpoint è stato raggiunto;
- fermare una ricerca quando l'obiettivo è trovato.

Romeo non sostituisce gli esercizi generali e non introduce hardware fisico nel core.

---

# 15. Checkpoint

Dovresti saper spiegare senza eseguire il codice:

1. differenza tra contatore e accumulatore;
2. perché un accumulatore si inizializza prima del ciclo;
3. perché `minimo = 999999` può essere fragile;
4. quale invariante rappresenta un minimo progressivo;
5. differenza tra “trova il primo” e “conta tutti”;
6. quando un flag aggiunge significato;
7. quale test protegge una media da divisione per zero.

---

# 16. Sintesi

```text
ciclo = attraversa/ripete
stato = ricorda ciò che serve
```

```text
contatore    → quanti?
accumulatore → quanto in totale?
min/max      → estremo visto finora
flag         → stato sì/no
ricerca      → primo / esiste / tutti?
```

La domanda di debugging più potente del modulo è:

> quale frase dovrebbe essere vera su questa variabile dopo ogni iterazione?

Nel prossimo modulo useremo più cicli insieme e inizieremo a ragionare su griglie, coppie di indici e quantità di lavoro svolto.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — `for`, `while`, `if`, `break` e semantica di base;
- *Think Python / Pensare in Python* — iterazione, accumulator patterns e debugging;
- *Learning Python / Imparare Python* — controllo del flusso come reference di copertura;
- Romeo pinned — dominio applicativo opzionale.

Le fonti licensed sono riferimenti, non testo da riprodurre.

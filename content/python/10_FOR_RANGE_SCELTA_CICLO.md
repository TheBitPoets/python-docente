# M10 — `for`, `range` e scelta `for` vs `while`

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-04 — Iterazione e pattern algoritmici  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- usare `for` con `range`;
- prevedere i valori prodotti da `range(stop)`, `range(start, stop)` e `range(start, stop, step)`;
- ricordare che il limite finale di `range` è escluso;
- contare avanti e indietro con step appropriato;
- riconoscere un `range` vuoto;
- spiegare quante iterazioni produce un semplice `range`;
- scegliere `for` quando l'insieme/numero di iterazioni è noto o naturalmente attraversabile;
- scegliere `while` quando la durata dipende da una condizione dinamica;
- riscrivere un semplice `while` contatore come `for` e confrontare le due versioni;
- usare `break` e `continue` con disciplina, soltanto quando chiariscono il flusso;
- diagnosticare off-by-one, stop errato, step errato e contatori manuali inutili.

## Prerequisiti

Da M09 dovresti già saper:

- leggere un `while` come stato + condizione + aggiornamento;
- fare trace di un ciclo;
- spiegare la terminazione;
- riconoscere zero/una/più iterazioni;
- usare validazione ripetuta e sentinella.

---

# 1. Problema iniziale: stampa esattamente cinque valori

Specifica:

> Stampa i numeri da 0 a 4.

Con `while` possiamo scrivere:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

È corretto.

Ma qui conosciamo già esattamente i valori da attraversare:

```text
0, 1, 2, 3, 4
```

Python offre una struttura che comunica direttamente questa intenzione:

```python
for i in range(5):
    print(i)
```

---

# 2. Modello del `for`

Nel nostro primo uso:

```python
for i in range(5):
    print(i)
```

puoi leggere:

```text
per ogni valore i prodotto da range(5)
    esegui il corpo
```

A differenza del `while`, non gestiamo manualmente:

```text
inizializzazione del contatore
condizione sul contatore
incremento del contatore
```

quando tutto ciò è già espresso da `range`.

---

# 3. `range(stop)`

```python
range(5)
```

produce concettualmente:

```text
0, 1, 2, 3, 4
```

Il valore `5` non è incluso.

Questa è una regola fondamentale:

> lo `stop` è escluso.

Per vedere i valori nel REPL puoi usare temporaneamente:

```python
list(range(5))
```

La lista qui è soltanto una lente di osservazione: studieremo le liste formalmente più avanti.

---

# 4. `range(start, stop)`

```python
range(2, 6)
```

produce:

```text
2, 3, 4, 5
```

Modello:

```text
start incluso
stop escluso
step predefinito = +1
```

Prima di eseguire un `range`, chiediti sempre:

```text
primo valore?
ultimo valore effettivo?
quanti valori?
```

---

# 5. `range(start, stop, step)`

```python
range(2, 10, 2)
```

produce:

```text
2, 4, 6, 8
```

Lo step indica come cambia il valore a ogni passo.

Esempio decrescente:

```python
range(5, 0, -1)
```

produce:

```text
5, 4, 3, 2, 1
```

Per scendere serve uno step negativo.

---

# 6. Range vuoto

```python
range(5, 0)
```

con lo step predefinito `+1` non produce valori.

Perché?

Partendo da 5 e aumentando, non possiamo avvicinarci allo stop 0 nel verso richiesto.

Invece:

```python
range(5, 0, -1)
```

ha senso per un countdown.

Un ciclo `for` su un range vuoto esegue il corpo zero volte.

---

# 7. Off-by-one: il confine conta

Obiettivo:

> stampa 1, 2, 3, 4, 5.

Bug:

```python
for i in range(1, 5):
    print(i)
```

Output:

```text
1, 2, 3, 4
```

Per includere 5:

```python
range(1, 6)
```

Non memorizzare “aggiungi sempre 1”: ragiona sul fatto che lo stop è escluso.

---

# 8. Trace di un `for`

```python
for i in range(2, 5):
    print(i * 10)
```

| iterazione | `i` | output |
|---:|---:|---:|
| 1 | 2 | 20 |
| 2 | 3 | 30 |
| 3 | 4 | 40 |

Dopo l'ultimo valore del range, il ciclo termina.

Non serve aggiornare manualmente `i`.

---

# 9. `for` vs `while`: stessa possibilità, intenzione diversa

Versione `while`:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Versione `for`:

```python
for i in range(5):
    print(i)
```

Entrambe sono corrette.

Nel problema “attraversa i valori 0..4” la versione `for` comunica meglio:

```text
so già quali valori devo visitare
```

e riduce il rischio di dimenticare l'aggiornamento.

---

# 10. Modello di scelta

## Preferisci `for` quando

```text
conosci i valori/iterazioni da attraversare
```

Esempi:

- ripeti N volte;
- attraversa un intervallo;
- più avanti: attraversa elementi di una sequenza.

## Preferisci `while` quando

```text
continui finché una condizione dipendente dallo stato resta vera
```

Esempi:

- input finché valido;
- continua fino a sentinella;
- ripeti finché una condizione dinamica cambia.

Non è una regola assoluta di sintassi: è un criterio di comunicazione dell'algoritmo.

---

# 11. Microscope: `for` o `while`?

Per ogni problema scegli prima il costrutto e motiva in una frase.

1. stampa i numeri 1..10;
2. chiedi un voto finché è valido;
3. ripeti una trasformazione esattamente 8 volte;
4. leggi dati fino alla sentinella `-1`;
5. countdown da 10 a 1;
6. continua finché il saldo è negativo e arrivano nuovi versamenti.

Il voto non dipende soltanto dalla scelta corretta, ma dalla motivazione.

---

# 12. Non duplicare il contatore dentro un `for`

Codice sospetto:

```python
contatore = 0
for i in range(5):
    print(contatore)
    contatore += 1
```

Se `contatore` serve soltanto a replicare esattamente `i`, abbiamo introdotto stato ridondante.

Può bastare:

```python
for i in range(5):
    print(i)
```

Un contatore separato è corretto quando rappresenta **un'altra quantità**, per esempio quanti valori soddisfano una condizione; questo sarà M11.

---

# 13. Countdown

Specifica:

> stampa 5, 4, 3, 2, 1.

```python
for i in range(5, 0, -1):
    print(i)
```

Domande:

```text
start = ?
stop escluso = ?
step = ?
ultimo valore effettivo = ?
```

Per includere `0` dovremmo modificare lo stop.

---

# 14. `break`: interrompere quando l'obiettivo è già raggiunto

Esempio controllato:

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

`break` interrompe il ciclo corrente.

Non è obbligatorio usare `break` ogni volta che esiste una condizione di stop. Lo usiamo quando rende il flusso più diretto e il motivo dell'interruzione è chiaro.

In M11 lo vedremo nel pattern “trova il primo elemento”.

---

# 15. `continue`: passa all'iterazione successiva

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Quando `i == 2`, il resto del corpo viene saltato e il `for` passa al valore successivo.

Regola didattica:

> non usare `continue` per evitare di strutturare una condizione leggibile.

Confronta sempre con una versione basata su `if` normale.

---

# 16. Error Clinic: stop incluso per errore

Obiettivo:

```text
0, 1, 2, 3, 4
```

Bug:

```python
for i in range(6):
    print(i)
```

Produce anche `5`.

Prima di cambiare codice, scrivi la sequenza prevista.

---

# 17. Error Clinic: step nel verso sbagliato

Bug:

```python
for i in range(5, 0, 1):
    print(i)
```

Il range è vuoto.

Se start > stop e vogliamo scendere, lo step deve essere negativo.

---

# 18. Error Clinic: `while` manuale quando `for` comunica meglio

```python
i = 0
while i < 100:
    elabora(i)
    i += 1
```

Può essere corretto.

Ma se l'unico scopo dello stato `i` è attraversare 0..99, confronta con:

```python
for i in range(100):
    elabora(i)
```

Il refactoring elimina gestione manuale non necessaria.

---

# 19. Romeo: ripetere una missione a numero noto

Romeo è un'applicazione naturale del `for`.

Esempio concettuale:

> ripeti quattro volte il comando necessario per un lato/una rotazione e costruisci una missione quadrata.

Il repo Romeo pinned contiene attività `for` coerenti con questo livello, tra cui:

```text
romeo-y1-u15-ciclo-for
```

Prima risolvi problemi generali con `range`; il simulatore viene dopo e solo quando `romeo-sim` è certificato.

---

# 20. Activity planning — M10

Candidati, senza nuova Activity P1 materializzata:

### A — Range microscope

Prevedere i valori di diversi `range` senza eseguire.

### B — `for` o `while`?

Classificare problemi e motivare la scelta.

### C — Implement

Countdown, ripetizione N volte, serie di trasformazioni semplici.

### D — Debug

Correggere:

- stop errato;
- step errato;
- range vuoto;
- off-by-one;
- contatore manuale duplicato;
- `break`/`continue` usati senza necessità.

M04 resta il canarino P1 fino a certificazione.

---

# 21. Esercizi brevi

## A — Prevedi il range

Scrivi la sequenza prodotta da:

```python
range(4)
range(2, 6)
range(1, 8, 2)
range(5, 0, -1)
range(5, 0)
```

## B — Ripeti N volte

Leggi `n` e stampa `ciao` esattamente `n` volte per `n >= 0`.

## C — Countdown

Stampa da `n` a `1` con `for` e `range`.

## D — Refactoring

Ricevi un `while` contatore corretto e riscrivilo con `for`. Spiega quale gestione manuale hai eliminato.

---

# 22. Checkpoint M10

Senza eseguire Python, spiega:

1. Che valori produce `range(5)`?
2. Perché lo stop non viene incluso?
3. Che produce `range(2, 6, 2)`?
4. Perché `range(5, 0)` è vuoto?
5. Quando `for` comunica meglio l'algoritmo rispetto a `while`?
6. Quando `while` resta la scelta naturale?
7. Perché aggiungere un contatore che duplica `i` può essere inutile?
8. Che cosa fa `break`?
9. Che cosa fa `continue`?
10. Perché non li usiamo come scorciatoie automatiche?

---

# 23. Sintesi

Porta con te questi modelli:

```text
for → so quali valori/iterazioni attraversare
```

```text
range → start incluso, stop escluso, step controlla il verso
```

```text
while → durata dipendente dallo stato
```

```text
scelta del ciclo → comunica il modello del problema
```

Nel prossimo modulo metteremo `if` dentro i cicli e impareremo pattern fondamentali: contatori, accumulatori, minimo/massimo progressivo, ricerca e flag.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione/verifica:

- documentazione Python 3.12 — `for`, `range`, `break`, `continue` e control flow;
- Allen Downey, *Think Python / Pensare in Python* — iteration e debugging;
- Mark Lutz, *Learning Python / Imparare Python* — loop semantics;
- Romeo pinned `45e5f7e131802fccc89358a23a25dbed1884bbfa` — `y1-u15-ciclo-for` come riferimento applicativo.

## Collegamenti di progettazione

- `tracks/secondo/PY2_04_SPEC.md`;
- `tracks/secondo/ROMEO_MAPPING.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`.

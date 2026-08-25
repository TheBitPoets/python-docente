# M07 — `elif`, casi esclusivi e condizioni composte

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-03 — Selezione e logica  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- costruire una catena `if/elif/else` con più casi;
- spiegare che in una catena viene eseguito il **primo ramo vero**;
- distinguere più `if` indipendenti da casi mutuamente esclusivi;
- usare `and`, `or`, `not` in condizioni semplici;
- leggere una piccola tabella di verità;
- esprimere intervalli numerici in modo corretto;
- comprendere la forma concatenata `a <= x <= b` dopo aver compreso la forma con `and`;
- progettare un test per ogni ramo e per ogni confine importante;
- individuare soglie nell'ordine sbagliato, rami irraggiungibili e condizioni sovrapposte;
- spiegare perché una soluzione usa `elif` oppure più `if`.

## Prerequisiti

Da M06 dovresti già saper:

- valutare confronti semplici;
- usare `if` e `if/else`;
- distinguere `=` e `==`;
- fare il trace di un ramo;
- testare una soglia sotto/sulla/sopra;
- comprendere l'indentazione come struttura del blocco.

---

# 1. Problema iniziale: classificare un voto

Specifica:

```text
voto < 6      → insufficiente
6 <= voto < 8 → buono
voto >= 8     → ottimo
```

I tre casi si escludono a vicenda: per un singolo voto vogliamo **una sola classificazione**.

Possiamo descrivere la decisione così:

```text
voto < 6 ?
   sì → insufficiente
   no → voto < 8 ?
           sì → buono
           no → ottimo
```

In Python questa struttura si esprime naturalmente con:

```python
if voto < 6:
    print("insufficiente")
elif voto < 8:
    print("buono")
else:
    print("ottimo")
```

---

# 2. `elif` significa “altrimenti, se…”

Una catena:

```python
if condizione_1:
    ...
elif condizione_2:
    ...
else:
    ...
```

si legge concettualmente:

```text
se condizione_1 è vera
    esegui ramo 1
altrimenti, se condizione_2 è vera
    esegui ramo 2
altrimenti
    esegui ramo finale
```

Punto fondamentale:

> dopo il primo ramo vero, gli altri rami della stessa catena non vengono più scelti.

---

# 3. Trace della catena: il primo ramo vero vince

Programma:

```python
voto = int(input())

if voto < 6:
    print("insufficiente")
elif voto < 8:
    print("buono")
else:
    print("ottimo")
```

## Caso `5`

```text
voto < 6 → True
ramo 1   → eseguito
resto catena → saltato
```

## Caso `7`

```text
voto < 6 → False
voto < 8 → True
ramo 2   → eseguito
else     → saltato
```

## Caso `9`

```text
voto < 6 → False
voto < 8 → False
else     → eseguito
```

---

# 4. Perché nel secondo `elif` basta `voto < 8`?

La specifica del caso centrale è:

```text
6 <= voto < 8
```

Eppure il codice usa:

```python
elif voto < 8:
```

Perché?

Se siamo arrivati a quell'`elif`, sappiamo già che:

```python
voto < 6
```

è falso.

Quindi il voto è già almeno 6.

Il contesto creato dai rami precedenti può rendere inutile ripetere una parte della condizione.

Questo non significa che dobbiamo sempre scrivere condizioni più corte: la condizione deve restare comprensibile.

---

# 5. Più `if` indipendenti: quando possono verificarsi più effetti

Problema diverso:

> Se piove, porta l'ombrello. Se fa freddo, indossa la giacca.

Le due condizioni sono indipendenti: possono essere vere entrambe.

```python
if piove:
    print("ombrello")

if fa_freddo:
    print("giacca")
```

Possibili risultati:

```text
nessun messaggio
solo ombrello
solo giacca
ombrello + giacca
```

Se trasformassimo il secondo `if` in `elif`, impediremmo l'esecuzione di entrambi i comportamenti nella stessa esecuzione.

---

# 6. Domanda guida: “quanti rami possono essere eseguiti?”

Prima di scegliere la sintassi chiediti:

```text
I casi sono mutuamente esclusivi?
```

Se vogliamo **un solo risultato** tra alternative:

```text
if / elif / else
```

Se più condizioni possono produrre **più effetti contemporaneamente**:

```text
if indipendenti
```

Non è una regola basata sul numero di condizioni, ma sulla relazione tra i casi del problema.

---

# 7. `and`: devono essere vere entrambe

Specifica:

> Accesso consentito se l'età è almeno 18 **e** il biglietto è valido.

Possiamo modellare:

```python
eta >= 18 and biglietto_valido
```

`and` produce `True` solo quando entrambe le parti sono vere.

| A | B | `A and B` |
|---|---|---|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

Prima formula la frase in linguaggio naturale; poi traduci in Python.

---

# 8. `or`: basta che almeno una sia vera

Specifica:

> Accesso gratuito se sei minore di 6 anni **oppure** hai almeno 65 anni.

```python
eta < 6 or eta >= 65
```

| A | B | `A or B` |
|---|---|---|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

`or` non significa “scegli una delle due condizioni a caso”.

Significa che il risultato complessivo è vero se almeno una parte è vera.

---

# 9. `not`: nega una condizione già compresa

Se:

```python
account_attivo
```

è un booleano, allora:

```python
not account_attivo
```

produce il valore opposto.

| A | `not A` |
|---|---|
| False | True |
| True | False |

Non usare `not` per rendere artificialmente più complicata una condizione che potresti esprimere direttamente.

Confronta:

```python
not eta < 18
```

con:

```python
eta >= 18
```

La seconda forma comunica direttamente la soglia che ci interessa.

---

# 10. Intervalli: prima la logica, poi la forma compatta

Specifica:

> `x` deve essere compreso tra 0 e 10, estremi inclusi.

Forma logica esplicita:

```python
x >= 0 and x <= 10
```

Dopo aver compreso questa forma, Python permette anche:

```python
0 <= x <= 10
```

Nel corso useremo la forma concatenata quando rende la condizione più naturale da leggere.

Non la impariamo come formula magica: rappresenta lo stesso intervallo che sappiamo già spiegare con `and`.

---

# 11. Worked example: tariffa per fasce

Specifica semplificata:

```text
eta < 6        → 0 euro
6 <= eta < 18  → 5 euro
eta >= 18      → 10 euro
```

Casi di test:

| età | tariffa |
|---:|---:|
| 5 | 0 |
| 6 | 5 |
| 17 | 5 |
| 18 | 10 |
| 70 | 10 |

Codice:

```python
eta = int(input())

if eta < 6:
    tariffa = 0
elif eta < 18:
    tariffa = 5
else:
    tariffa = 10

print(tariffa)
```

I test sui confini `6` e `18` sono essenziali.

---

# 12. Error Clinic: soglie nell'ordine sbagliato

Bug:

```python
if voto >= 6:
    print("sufficiente")
elif voto >= 8:
    print("ottimo")
```

Per `9`:

```text
voto >= 6 → True
```

Il primo ramo viene eseguito e il secondo non viene mai raggiunto.

Il problema non è la sintassi: è l'ordine dei casi.

Una possibile struttura coerente è:

```python
if voto >= 8:
    print("ottimo")
elif voto >= 6:
    print("sufficiente")
else:
    print("insufficiente")
```

---

# 13. Error Clinic: più `if` quando volevamo un solo risultato

Bug concettuale:

```python
if voto >= 6:
    print("sufficiente")

if voto >= 8:
    print("ottimo")
```

Con `9` otteniamo due classificazioni.

Se la specifica chiede **una sola fascia**, i due `if` indipendenti non rappresentano correttamente il problema.

---

# 14. Error Clinic: `elif` quando due effetti possono coesistere

Specifica:

```text
se piove → ombrello
se fa freddo → giacca
```

Bug:

```python
if piove:
    print("ombrello")
elif fa_freddo:
    print("giacca")
```

Se piove **e** fa freddo, viene stampato soltanto `ombrello`.

Il problema richiede due condizioni indipendenti.

---

# 15. Error Clinic: `and` invece di `or`

Specifica:

> gratis se età < 6 oppure età >= 65.

Bug:

```python
if eta < 6 and eta >= 65:
    print("gratis")
```

Nessuna età può soddisfare contemporaneamente entrambe le condizioni.

La traduzione della parola **oppure** è stata sbagliata.

---

# 16. Short-circuit: un'intuizione utile

Python valuta `and` e `or` da sinistra a destra e può non aver bisogno di valutare la seconda parte.

Esempio guidato:

```python
if divisore != 0 and numero / divisore > 2:
    print("ok")
```

Se `divisore != 0` è `False`, l'intera condizione `and` è già falsa: non serve valutare la divisione.

Per ora non memorizziamo trucchi.

Portiamo con noi soltanto due idee:

- l'ordine delle condizioni può avere un significato;
- una condizione semplice/sicura può precedere un'operazione che ha senso solo in alcuni casi.

Approfondiremo questi temi quando avremo più esperienza.

---

# 17. Microscope: classifica la struttura prima del codice

Per ogni specifica indica prima:

```text
A) un solo ramo possibile
B) più effetti possibili
```

1. “classifica il voto come insufficiente/buono/ottimo”;
2. “se piove prendi ombrello; se fa freddo prendi giacca”;
3. “scegli una tariffa tra tre fasce”;
4. “se hai completato il quiz assegna badge; se hai completato il progetto assegna bonus”.

Soltanto dopo scegli:

```text
if / elif / else
oppure
if indipendenti
```

---

# 18. Activity planning — M07

Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:

### A — Classifica il caso

Dato input + catena, prevedere il primo ramo eseguito.

### B — Due `if` o `elif`?

Diverse specifiche brevi: scegliere la struttura e motivarla.

### C — Implement

Classificatore a 3–4 fasce con test sui confini.

### D — Debug

Correggere:

- soglie nell'ordine sbagliato;
- ramo irraggiungibile;
- due `if` quando serviva un solo risultato;
- `elif` quando due effetti possono coesistere;
- `and`/`or` sbagliato.

M04 resta il canarino P1 fino alla certificazione `python-docente#7`.

---

# 19. Romeo come applicazione selettiva

Romeo non è necessario per imparare `elif`, `and` o `or`.

Dopo i problemi generali, il simulatore può offrire una variante di missione con regole multiple, ad esempio:

```text
modalità sicura + limite di velocità
oppure
selezione di un comportamento da un parametro della missione
```

La variante deve:

- usare soltanto API già appropriate al livello;
- rimanere deterministica;
- non introdurre sensori/networking non ancora studiati;
- essere opzionale finché `romeo-sim` non è certificato nel Classroom Environment.

Non duplichiamo ora una nuova Activity Romeo nel repo Python.

---

# 20. Esercizi brevi

## A — Fasce

Classifica una temperatura:

```text
< 0      → gelo
0..24    → normale
>= 25    → caldo
```

Scrivi prima i casi `-1`, `0`, `24`, `25`.

## B — Indipendenti o esclusivi?

Per ciascuna specifica scegli `if` indipendenti o catena `elif` e motiva in una riga.

## C — Accesso composto

Specifica:

> consentito se età >= 18 e biglietto valido.

Progetta i quattro casi della tabella di verità e poi il codice.

## D — Intervallo

Verifica se un numero appartiene all'intervallo chiuso `[10, 20]` prima con `and`, poi con confronto concatenato.

Spiega perché le due condizioni rappresentano lo stesso insieme di valori.

---

# 21. Checkpoint M07

Senza eseguire Python, spiega:

1. Che cosa significa “primo ramo vero” in una catena `if/elif/else`?
2. Perché `elif voto < 8` può essere sufficiente dopo `if voto < 6`?
3. Quando sono corretti due `if` indipendenti?
4. Quando è preferibile una catena mutuamente esclusiva?
5. Quando `A and B` è vero?
6. Quando `A or B` è vero?
7. Che cosa produce `not True`?
8. Che insieme di valori rappresenta `0 <= x <= 10`?
9. Perché l'ordine `if voto >= 6` poi `elif voto >= 8` è problematico?

---

# 22. Sintesi

Porta con te questi modelli:

```text
if / elif / else → scegli il primo ramo vero
```

```text
if indipendenti → più effetti possono coesistere
```

```text
and → tutte vere
or  → almeno una vera
not → negazione
```

```text
intervallo → confini + casi di test
```

Nel prossimo modulo useremo selezioni annidate, validazione e refactoring per capire quando una decisione dipende realmente da un'altra e quando invece il codice può essere reso più semplice.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione/verifica:

- documentazione Python 3.12 — `if` statement, Boolean operations, comparisons e chained comparisons;
- Allen Downey, *Think Python / Pensare in Python* — conditional execution, recursion-free beginner reasoning e debugging;
- Mark Lutz, *Learning Python / Imparare Python* — Boolean expressions, control flow e statement semantics;
- Romeo pinned `45e5f7e131802fccc89358a23a25dbed1884bbfa` — solo riferimento applicativo selettivo.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

## Collegamenti di progettazione

- `tracks/secondo/PY2_03_SPEC.md`;
- `tracks/secondo/ROMEO_MAPPING.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

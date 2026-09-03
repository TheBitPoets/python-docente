# M09 — `while`, stato, sentinelle e validazione ripetuta

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-04 — Iterazione e pattern algoritmici  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- spiegare che `while` ripete un blocco finché una condizione resta vera;
- identificare stato iniziale, condizione, corpo e aggiornamento;
- eseguire il trace di un ciclo `while`;
- spiegare quale valore deve cambiare perché il ciclo possa terminare;
- riconoscere un ciclo infinito e un aggiornamento mancante;
- usare un contatore in un `while`;
- ripetere una richiesta finché un valore rientra nel dominio valido;
- usare una sentinella per indicare la fine di una sequenza di input;
- distinguere condizione di continuazione e condizione di uscita;
- progettare test con zero, una e più iterazioni quando il problema lo consente;
- usare `while True`/`break` soltanto dopo aver compreso e motivato la condizione di terminazione.

## Prerequisiti

Da PY2-03 dovresti già saper:

- costruire condizioni con confronti, `and`, `or`, `not`;
- validare un valore con `if/else`;
- fare path trace;
- distinguere dato fuori dominio da errore di conversione;
- progettare casi di test sui confini.

---

# 1. Problema iniziale: chiedi di nuovo finché il voto è valido

In M08 sapevamo fare questo:

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    print("dato valido")
```

Ma la specifica ora cambia:

> Continua a chiedere un voto finché l'utente inserisce un intero tra 0 e 10.

Non basta più una decisione eseguita una sola volta.

Serve una **ripetizione controllata da una condizione**.

---

# 2. Il modello del `while`

Schema:

```text
stato iniziale
     ↓
condizione? ── False ──> fine
     |
    True
     ↓
   corpo
     ↓
aggiornamento dello stato
     └───────────────↺
```

In Python:

```python
while condizione:
    corpo
```

Il corpo viene ripetuto finché la condizione continua a produrre `True`.

---

# 3. Primo ciclo con contatore

```python
i = 0

while i < 3:
    print(i)
    i = i + 1
```

Output:

```text
0
1
2
```

Quattro parti da riconoscere:

```text
inizializzazione → i = 0
condizione       → i < 3
corpo            → print(i)
aggiornamento    → i = i + 1
```

---

# 4. Trace riga per riga

Per:

```python
i = 0
while i < 3:
    print(i)
    i = i + 1
```

| controllo | `i` prima | `i < 3` | output | `i` dopo aggiornamento |
|---:|---:|---|---:|---:|
| 1 | 0 | True | 0 | 1 |
| 2 | 1 | True | 1 | 2 |
| 3 | 2 | True | 2 | 3 |
| 4 | 3 | False | — | — |

L'ultimo controllo esiste anche se il corpo non viene più eseguito.

---

# 5. Domanda obbligatoria: “perché questo ciclo può finire?”

Nel ciclo precedente:

```text
i parte da 0
→ ogni iterazione aumenta di 1
→ prima o poi i < 3 diventa False
```

Ogni volta che scrivi un `while`, devi saper rispondere:

1. quale parte della condizione dipende dallo stato?
2. quale istruzione cambia quello stato?
3. esiste un percorso in cui l'aggiornamento non avviene?
4. può la condizione diventare falsa?

Questa è una regola di progettazione, non soltanto di debugging.

---

# 6. Ciclo infinito: aggiornamento mancante

Bug:

```python
i = 0

while i < 3:
    print(i)
```

`i` resta sempre `0`.

Quindi:

```text
0 < 3 → True
```

continua a essere vero.

Il problema non è “Python si è bloccato”: il programma non contiene alcun meccanismo che renda falsa la condizione.

---

# 7. Zero iterazioni è un comportamento valido

```python
i = 5

while i < 3:
    print(i)
```

La condizione iniziale è subito `False`.

Il corpo viene eseguito **zero volte**.

Per questo i test di un `while` devono considerare, quando la specifica lo permette:

```text
zero iterazioni
una iterazione
più iterazioni
```

---

# 8. Validazione ripetuta

Specifica:

> Leggi un voto finché è compreso tra 0 e 10.

```python
voto = int(input())

while voto < 0 or voto > 10:
    voto = int(input())

print(voto)
```

Modello:

```text
leggi
→ non valido?
    sì → leggi di nuovo
    no → continua dopo il ciclo
```

Il nuovo input è l'aggiornamento dello stato.

---

# 9. Trace della validazione

Input forniti, uno dopo l'altro:

```text
12
-1
7
```

Trace:

```text
voto = 12
12 fuori 0..10 → True  → nuova lettura

voto = -1
-1 fuori 0..10 → True  → nuova lettura

voto = 7
7 fuori 0..10 → False → fine ciclo
```

Output finale:

```text
7
```

Il numero di iterazioni non era noto in anticipo.

---

# 10. Condizione di continuazione vs condizione di uscita

Nel codice:

```python
while voto < 0 or voto > 10:
    voto = int(input())
```

la condizione dice:

> **continua** mentre il voto è invalido.

La condizione di uscita equivalente, in linguaggio naturale, è:

> esci quando `0 <= voto <= 10`.

Non confondere le due frasi.

Se la specifica dice “ripeti finché non è valido”, prima scrivi chiaramente quale condizione mantiene attivo il ciclo.

---

# 11. Variante con booleano nominato

Possiamo scrivere:

```python
voto = int(input())
voto_non_valido = voto < 0 or voto > 10

while voto_non_valido:
    voto = int(input())
    voto_non_valido = voto < 0 or voto > 10
```

È corretto, ma introduce un obbligo in più:

> aggiornare anche `voto_non_valido` ogni volta che cambia `voto`.

Nel problema semplice la condizione diretta è più difficile da desincronizzare:

```python
while voto < 0 or voto > 10:
```

Un nome booleano è utile quando aggiunge significato senza creare stato duplicato inutile.

---

# 12. Sentinella: un valore che segnala “fine”

Problema:

> Leggi numeri e stampali. Il valore `-1` indica che l'inserimento è terminato e non deve essere elaborato.

Schema:

```text
leggi valore
finché valore != -1:
    elabora valore
    leggi nuovo valore
```

Python:

```python
numero = int(input())

while numero != -1:
    print(numero)
    numero = int(input())
```

`-1` è la **sentinella**.

---

# 13. La sentinella deve essere fuori dai dati normali

Se `-1` è un valore valido del dominio, usarlo come segnale di fine crea ambiguità.

Prima di scegliere una sentinella chiediti:

```text
può comparire come dato normale?
```

In esercizi scolastici la specifica dichiarerà chiaramente il valore sentinella.

In applicazioni reali esistono molte altre forme di terminazione; qui impariamo il pattern.

---

# 14. Trace della sentinella

Input:

```text
4
8
-1
```

| valore letto | `numero != -1` | elaborato? | nuova lettura? |
|---:|---|---|---|
| 4 | True | sì | sì |
| 8 | True | sì | sì |
| -1 | False | no | no |

Il valore di fine controlla il ciclo ma non viene elaborato.

---

# 15. Error Clinic: aggiornamento solo in un ramo

Bug:

```python
numero = int(input())

while numero != -1:
    if numero > 0:
        print(numero)
        numero = int(input())
```

Che succede se `numero` vale `0`?

```text
numero != -1 → True
numero > 0   → False
nuova lettura → non avviene
numero resta 0
```

Il ciclo diventa infinito.

L'aggiornamento deve avvenire su tutti i percorsi che devono far progredire il ciclo.

---

# 16. Error Clinic: condizione invertita

Specifica:

> ripeti mentre il voto è fuori 0..10.

Bug:

```python
while 0 <= voto <= 10:
    voto = int(input())
```

Questa condizione ripete **quando il voto è valido**.

Prima del codice verbalizza sempre:

```text
quando devo continuare?
```

---

# 17. Error Clinic: off-by-one con contatore

Obiettivo:

> stampa `0`, `1`, `2`.

Bug:

```python
i = 0
while i <= 3:
    print(i)
    i += 1
```

Produce anche `3`.

I test del primo/ultimo valore sono fondamentali anche nei cicli.

---

# 18. `while True` e `break`: non come scorciatoia iniziale

Python permette:

```python
while True:
    voto = int(input())
    if 0 <= voto <= 10:
        break
```

Questa forma può essere utile quando la condizione di uscita emerge naturalmente **dentro** il corpo.

Ma non è il nostro modello introduttivo primario.

Prima devi saper progettare:

```text
stato
condizione
aggiornamento
terminazione
```

Regola:

> `while True` non serve a evitare di pensare alla condizione di fine.

Se usi `break`, devi indicare con precisione quale percorso lo raggiunge e perché.

---

# 19. Confronto di due validazioni

Versione A:

```python
voto = int(input())
while voto < 0 or voto > 10:
    voto = int(input())
```

Versione B:

```python
while True:
    voto = int(input())
    if 0 <= voto <= 10:
        break
```

Entrambe possono essere corrette.

Per il primo apprendimento preferiamo A perché rende la condizione di continuazione visibile nella testata del ciclo.

B diventa utile quando il flusso interno rende più chiara l'uscita.

La scelta va motivata, non trasformata in una regola assoluta.

---

# 20. Microscope: individua le quattro parti

Per ciascun ciclo identifica:

```text
stato iniziale
condizione
corpo
aggiornamento
```

### A

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

### B

```python
parola = input()
while parola != "fine":
    print(parola)
    parola = input()
```

Poi rispondi:

> quale valore può rendere falsa la condizione?

---

# 21. Romeo: ripetizione controllata nel simulatore

Romeo può rendere visibile un ciclo, ma soltanto dopo il modello generale.

Il repo Romeo pinned contiene attività su `while` e simulazione deterministica, ad esempio:

```text
romeo-y1-u16-ciclo-while
```

Uso didattico possibile:

```text
contatore/stato
→ invia un numero controllato di comandi
→ terminazione
→ stop
```

Il simulatore deve essere certificato nel Classroom Environment prima di diventare delivery obbligatoria. Hardware fisico non è richiesto.

---

# 22. Activity planning — M09

Candidati, senza materializzare ancora una nuova Activity P1:

### A — Trace

Compilare tabella iterazione/stato/condizione/output.

### B — Controlled Change

Cambiare limiti di una validazione e aggiornare i test.

### C — Implement

Richiedere un valore finché appartiene a un intervallo valido.

### D — Debug

Correggere:

- aggiornamento mancante;
- aggiornamento in un solo ramo;
- condizione invertita;
- inizializzazione errata;
- off-by-one;
- sentinella elaborata per errore.

M04 resta il canarino P1 fino alla certificazione `python-docente#7`.

---

# 23. Esercizi brevi

## A — Trace contatore

Prevedi l'output:

```python
i = 2
while i < 6:
    print(i)
    i += 2
```

## B — Validazione

Leggi un intero finché è compreso tra `1` e `5` inclusi. Progetta una sequenza di input che provochi:

```text
zero ripetizioni
una ripetizione
tre ripetizioni
```

## C — Sentinella

Leggi parole finché non compare `stop`; stampa ogni parola normale, ma non la sentinella.

## D — Debug terminazione

Trova un input che rende infinito il programma:

```python
x = int(input())
while x != 0:
    if x > 0:
        x -= 1
```

Spiega perché.

---

# 24. Checkpoint M09

Senza eseguire Python, spiega:

1. Che cosa significa “`while` ripete finché la condizione è vera”?
2. Quali sono le quattro parti del nostro modello di ciclo?
3. Perché `i = 0; while i < 3:` richiede un aggiornamento di `i`?
4. Che cosa significa zero iterazioni?
5. Qual è l'aggiornamento nella validazione ripetuta del voto?
6. Che differenza c'è tra condizione di continuazione e condizione di uscita?
7. Che cos'è una sentinella?
8. Perché una sentinella deve essere distinguibile dai dati normali?
9. Perché un aggiornamento presente solo in un ramo può creare un ciclo infinito?
10. Perché `while True` non deve essere una scorciatoia per evitare di progettare la terminazione?

---

# 25. Sintesi

Porta con te questi modelli:

```text
while → ripeti finché una condizione resta vera
```

```text
stato iniziale
→ condizione
→ corpo
→ aggiornamento
→ nuovo controllo
```

```text
ogni while → deve avere una storia di terminazione
```

```text
validazione ripetuta → controlla / rileggi / ricontrolla
```

```text
sentinella → valore che segnala la fine
```

Nel prossimo modulo confronteremo `while` con `for`: quando sappiamo già quali valori/iterazioni attraversare, `for` spesso comunica meglio l'intenzione e riduce gli errori di gestione manuale del contatore.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione/verifica:

- documentazione Python 3.12 — `while`, `break`, control flow;
- Allen Downey, *Think Python / Pensare in Python* — iteration, reassignment, debugging;
- Mark Lutz, *Learning Python / Imparare Python* — loops and control-flow semantics;
- Romeo pinned `45e5f7e131802fccc89358a23a25dbed1884bbfa` — `y1-u16-ciclo-while` come riferimento applicativo.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

## Collegamenti di progettazione

- `tracks/secondo/PY2_04_SPEC.md`;
- `tracks/secondo/ROMEO_MAPPING.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

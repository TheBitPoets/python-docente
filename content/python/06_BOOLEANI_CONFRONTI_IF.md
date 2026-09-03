# M06 — Booleani, confronti e prima selezione con `if`

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-03 — Selezione e logica  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- riconoscere un'espressione che produce `True` o `False`;
- usare `==`, `!=`, `<`, `<=`, `>`, `>=` nei casi semplici;
- distinguere assegnamento `=` e confronto `==`;
- prevedere il risultato di un confronto prima di eseguirlo;
- tradurre una decisione sì/no in un `if`;
- usare `if/else` quando i due casi sono complementari;
- capire che l'indentazione definisce il blocco eseguito dal ramo;
- fare il trace di una selezione con dati concreti;
- progettare test **sotto, sulla e sopra** una soglia;
- diagnosticare condizioni invertite, confini sbagliati e rami con output errato;
- spiegare a parole perché un certo input percorre un certo ramo.

## Prerequisiti

Da M04–M05 dovresti già saper:

- leggere input e convertire tipi;
- usare variabili, espressioni e output;
- distinguere `/`, `//`, `%` nei problemi appropriati;
- prevedere valore e tipo di espressioni semplici;
- progettare più casi di test;
- leggere errori beginner e correggere una modifica alla volta.

---

# 1. Problema iniziale: lo sconto si applica oppure no?

Specifica:

> Se il totale dell'ordine è almeno 50 euro, la spedizione è gratuita. Altrimenti costa 5 euro.

Prima di Python dobbiamo capire la **decisione**.

```text
totale >= 50 ?
    sì  → spedizione = 0
    no  → spedizione = 5
```

La parte più importante è la soglia:

```text
almeno 50
```

significa che **50 è incluso**.

Quindi la domanda corretta è:

```python
totale >= 50
```

non:

```python
totale > 50
```

---

# 2. Una condizione è un'espressione che produce `bool`

Nel REPL, prima prevedi:

```python
7 > 3
```

Il risultato è:

```python
True
```

Poi:

```python
7 < 3
```

produce:

```python
False
```

Il tipo è:

```python
bool
```

Modello mentale:

```text
valori
  ↓
confronto
  ↓
True oppure False
```

Questa risposta vero/falso può controllare quale ramo del programma viene eseguito.

---

# 3. Operatori di confronto

| Operatore | Domanda | Esempio |
|---|---|---|
| `==` | ha lo stesso valore? | `voto == 6` |
| `!=` | ha valore diverso? | `voto != 6` |
| `<` | minore di? | `eta < 18` |
| `<=` | minore o uguale? | `temperatura <= 0` |
| `>` | maggiore di? | `punti > 100` |
| `>=` | maggiore o uguale? | `totale >= 50` |

Non scegliere l'operatore guardando soltanto il simbolo.

Traduci prima la frase:

```text
più di 10        → > 10
almeno 10        → >= 10
meno di 10       → < 10
al massimo 10    → <= 10
esattamente 10   → == 10
```

---

# 4. `=` e `==` fanno lavori diversi

In M04 abbiamo usato:

```python
eta = 15
```

Questo è un **assegnamento**: associa un nome a un valore.

Per fare una domanda di uguaglianza usiamo:

```python
eta == 15
```

che produce:

```text
True oppure False
```

Modello:

```text
=   → assegna
==  → confronta
```

Python non considera questi due operatori intercambiabili.

---

# 5. Primo `if`: esegui qualcosa soltanto quando la condizione è vera

Specifica:

> Se la temperatura è sotto zero, stampa `gelo`.

```python
temperatura = int(input())

if temperatura < 0:
    print("gelo")
```

Se l'input è `-3`, la condizione è vera e il ramo viene eseguito.

Se l'input è `5`, la condizione è falsa e quel `print` non viene eseguito.

Questo **non è un errore**: è proprio il comportamento richiesto da un `if` senza `else`.

---

# 6. I due punti e l'indentazione fanno parte della struttura

Osserva:

```python
if temperatura < 0:
    print("gelo")
```

Due elementi sono strutturali:

1. `:` dopo la condizione;
2. il blocco indentato sotto `if`.

L'indentazione non è soltanto estetica.

Indica quali istruzioni appartengono al ramo.

Confronta:

```python
if temperatura < 0:
    print("gelo")
print("fine")
```

`print("fine")` viene eseguito comunque perché non appartiene al blocco dell'`if`.

---

# 7. Trace di un `if`

Programma:

```python
numero = int(input())

if numero > 0:
    print("positivo")

print("fine")
```

## Caso A — input `4`

```text
numero           → 4
numero > 0       → True
ramo if          → eseguito
output            → positivo
print("fine")    → eseguito
output            → fine
```

## Caso B — input `-2`

```text
numero           → -2
numero > 0       → False
ramo if          → saltato
print("fine")    → eseguito
output            → fine
```

Il trace deve seguire il valore concreto della condizione, non ciò che "sembra probabile".

---

# 8. Quando serve `else`

Specifica:

> Stampa `maggiorenne` se l'età è almeno 18, altrimenti stampa `minorenne`.

I casi sono complementari:

```text
eta >= 18
oppure
eta < 18
```

Possiamo scrivere:

```python
eta = int(input())

if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

`else` significa:

> se la condizione dell'`if` non è vera, esegui questo altro ramo.

Non serve riscrivere la condizione opposta.

---

# 9. Un solo ramo di `if/else` viene eseguito

Con:

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

per ogni singola esecuzione:

```text
condizione True  → ramo if
condizione False → ramo else
```

Non vengono eseguiti entrambi.

Questa idea diventerà importante in M07 quando confronteremo:

```text
più if indipendenti
```

con:

```text
if / elif / else
```

---

# 10. I casi di frontiera: sotto, sulla, sopra

Per una soglia `18`, non basta provare un valore lontano.

Casi minimi:

| età | atteso |
|---:|---|
| 17 | minorenne |
| 18 | maggiorenne |
| 19 | maggiorenne |

Perché `18` è fondamentale?

Perché distingue:

```python
eta > 18
```

da:

```python
eta >= 18
```

Un test sul confine trova errori che un caso come `25` non vede.

---

# 11. Worked example: spedizione gratuita

## Specifica

```text
INPUT: totale ordine, intero non negativo
OUTPUT: costo spedizione
REGOLA: se totale >= 50 → 0, altrimenti → 5
```

## Casi prima del codice

| totale | spedizione attesa |
|---:|---:|
| 49 | 5 |
| 50 | 0 |
| 51 | 0 |
| 0 | 5 |

## Codice

```python
totale = int(input())

if totale >= 50:
    spedizione = 0
else:
    spedizione = 5

print(spedizione)
```

Il `print` è fuori dalla selezione perché in entrambi i casi vogliamo mostrare il valore finale di `spedizione`.

---

# 12. Confronto: duplicare output oppure calcolare prima?

Versione A:

```python
if totale >= 50:
    print(0)
else:
    print(5)
```

Versione B:

```python
if totale >= 50:
    spedizione = 0
else:
    spedizione = 5

print(spedizione)
```

Entrambe possono essere corrette per questa specifica.

La B separa meglio:

```text
decisione / calcolo
→ presentazione finale
```

Ma non trasformiamo questa preferenza in una regola meccanica: confrontiamo sempre chiarezza e obiettivo del problema.

---

# 13. Microscope: prevedi `True` o `False`

Senza REPL, completa prima:

| Espressione | Risultato previsto |
|---|---|
| `5 > 2` | ? |
| `5 < 2` | ? |
| `5 == 5` | ? |
| `5 != 5` | ? |
| `10 >= 10` | ? |
| `9 >= 10` | ? |
| `0 <= 0` | ? |

Poi verifica.

Il simbolo `=` singolo non compare nella tabella perché non è un confronto.

---

# 14. Error Clinic

## Caso 1 — confine sbagliato

Specifica:

> accesso consentito da 18 anni compresi.

Bug:

```python
if eta > 18:
    print("consentito")
```

Quale input distingue subito il bug?

```text
18
```

## Caso 2 — condizione invertita

Specifica:

> stampa `negativo` se il numero è minore di zero.

Bug:

```python
if numero > 0:
    print("negativo")
```

Il programma è sintatticamente valido ma rappresenta la domanda sbagliata.

## Caso 3 — `=` al posto di `==`

```python
if voto = 6:
    print("sei")
```

Qui stai tentando di usare un assegnamento dove Python richiede un'espressione valida come condizione.

Per confrontare il valore:

```python
if voto == 6:
```

## Caso 4 — indentazione

```python
if temperatura < 0:
print("gelo")
```

Il blocco non è strutturato correttamente.

## Caso 5 — output nel ramo sbagliato

```python
if eta >= 18:
    print("minorenne")
else:
    print("maggiorenne")
```

La sintassi è valida; il comportamento non rispetta la specifica.

---

# 15. `is` non è il sostituto di `==`

Per confrontare normalmente valori numerici o stringhe nel nostro corso usiamo:

```python
==
```

Non insegniamo:

```python
is
```

come scorciatoia per l'uguaglianza di valore.

`is` riguarda l'identità degli oggetti e verrà contestualizzato molto più avanti, quando avremo un modello degli oggetti sufficiente.

Regola beginner:

```text
uguaglianza di valore → ==
```

---

# 16. Dal flow chart al Python

Decisione algoritmica:

```text
        eta >= 18 ?
       /           \
     sì             no
     |              |
maggiorenne      minorenne
```

Python:

```python
if eta >= 18:
    print("maggiorenne")
else:
    print("minorenne")
```

La sintassi cambia, ma il modello della decisione è lo stesso.

Per questo il flow chart non era un esercizio separato da Python: rappresentava la struttura che ora codifichiamo.

---

# 17. Activity planning — M06

Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:

### A — Predict/Trace

Dato valore + condizione, prevedere:

- `True`/`False`;
- ramo eseguito;
- output.

### B — Controlled Change

Cambiare una soglia e aggiornare i casi `sotto / sulla / sopra`.

### C — Implement

Da un flow chart sì/no già noto a un programma `if/else`.

### D — Debug

Correggere:

- `>` vs `>=`;
- condizione invertita;
- `=` vs `==`;
- indentazione;
- messaggi nei rami sbagliati.

M04 resta il canarino P1 finché `python-docente#7` non è certificato.

---

# 18. Romeo come applicazione opzionale

Il concetto di selezione deve essere padroneggiato anche senza Romeo.

Dopo gli esercizi generali possiamo usare il simulatore come problema concreto.

La piattaforma Romeo pinned contiene già una missione didattica:

```text
romeo-y1-u14-condizioni — Decidi con if
```

Idea della missione:

> se la modalità sicura è attiva, usa una velocità ridotta; completa la missione e fermati.

Il valore didattico è vedere che:

```text
condizione
→ scelta di comportamento
→ effetto osservabile nel simulatore
```

Regole:

- `romeo-sim` soltanto nel Classroom Environment certificato;
- hardware fisico non richiesto;
- niente networking/FastAPI/WebSocket;
- la missione è applicazione del concetto, non il suo prerequisito.

---

# 19. Esercizi brevi

## A — Soglia

Specifica:

> Se il punteggio è almeno 100, stampa `livello`; altrimenti stampa `continua`.

Scrivi prima i casi `99`, `100`, `101`, poi il codice.

## B — Positivo o non positivo

Leggi un intero e stampa:

```text
positivo
```

se è maggiore di zero, altrimenti:

```text
non positivo
```

Quale ramo percorre `0`?

## C — Debug del confine

Correggi:

```python
if temperatura > 0:
    print("sopra zero")
else:
    print("zero o sotto")
```

solo se una nuova specifica dice:

> `sopra zero` deve essere stampato anche per `0`.

Quale operatore cambia e perché?

## D — Flow chart → codice

Ricevi un flow chart con una sola decisione e produci:

1. tabella di tre casi;
2. condizione Python;
3. `if/else`;
4. trace di un caso.

---

# 20. Checkpoint M06

Senza eseguire Python, spiega:

1. Che tipo produce `7 >= 7`?
2. Differenza fra `=` e `==`?
3. Perché `eta >= 18` include il valore 18?
4. Che cosa succede al blocco `if` se la condizione è `False` e non esiste `else`?
5. Perché l'indentazione non è soltanto estetica?
6. Quali tre valori sceglieresti per testare una soglia 50?
7. Perché non usiamo `is` come sostituto di `==`?
8. In che modo il flow chart della decisione corrisponde a `if/else`?

---

# 21. Sintesi

Porta con te questi modelli:

```text
confronto → bool
```

```text
True  → esegui ramo if
False → salta ramo if / usa else se presente
```

```text
=  → assegnamento
== → confronto di valore
```

```text
soglia → test sotto / sulla / sopra
```

```text
indentazione → appartenenza al blocco
```

Nel prossimo modulo passeremo da due casi a più casi e capiremo quando usare `elif`, quando usare più `if` indipendenti e come comporre condizioni con `and`, `or`, `not`.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione/verifica:

- documentazione Python 3.12 — confronti, `if` e control flow;
- Allen Downey, *Think Python / Pensare in Python* — conditional execution e debugging;
- Mark Lutz, *Learning Python / Imparare Python* — espressioni booleane, statement e controllo;
- Romeo pinned `45e5f7e131802fccc89358a23a25dbed1884bbfa` — riferimento tecnico/applicativo per `romeo-y1-u14-condizioni`.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

## Collegamenti di progettazione

- `tracks/secondo/PY2_03_SPEC.md`;
- `tracks/secondo/ROMEO_MAPPING.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

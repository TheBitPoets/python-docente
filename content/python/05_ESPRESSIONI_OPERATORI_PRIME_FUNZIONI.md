# M05 — Espressioni, operatori e prime funzioni

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-02 — Primi programmi Python  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- costruire espressioni aritmetiche leggibili;
- usare `+`, `-`, `*`, `/`, `//`, `%` e `**` nei problemi appropriati;
- prevedere il valore e il tipo di espressioni semplici;
- usare parentesi per rendere esplicita l'intenzione del calcolo;
- distinguere divisione `/`, divisione intera verso il basso `//` e resto `%`;
- usare `%` per problemi di quoziente/resto e divisibilità elementare;
- produrre output leggibile con f-string;
- usare alcune funzioni built-in quando rendono il programma più chiaro;
- riconoscere la differenza fra **calcolare**, **restituire** e **stampare**;
- definire e chiamare una prima funzione pura molto semplice;
- progettare casi di test prima di considerare concluso un piccolo programma.

## Prerequisiti

Da M04 dovresti già saper:

- usare REPL e script `.py`;
- riconoscere `int`, `float`, `str`, `bool` nei casi base;
- usare variabili, `input()`, `print()` e conversioni semplici;
- leggere un traceback beginner;
- verificare uno script con più input.

---

# 1. Problema iniziale: quanti minuti e quanti secondi?

Problema:

> Leggi un numero intero di secondi e mostra quanti minuti completi contiene e quanti secondi restano.

Esempio:

```text
INPUT: 137
OUTPUT: 2 17
```

Prima del codice:

```text
137 secondi
= 2 gruppi completi da 60
+ 17 secondi rimanenti
```

Quindi servono **due risultati diversi**:

```text
quoziente intero → 2
resto             → 17
```

Python possiede operatori che esprimono direttamente queste due idee.

---

# 2. Un'espressione produce un valore

Nel REPL:

```python
2 + 3
```

è un'espressione.

Produce il valore:

```text
5
```

Anche:

```python
prezzo * quantita
```

è un'espressione se i nomi hanno già un valore associato.

Possiamo usare il risultato in un assegnamento:

```python
totale = prezzo * quantita
```

Modello mentale:

```text
valori / nomi
     ↓
espressione
     ↓
valore risultante
     ↓
assegnamento / return / print / altra espressione
```

---

# 3. Operatori aritmetici fondamentali

Con numeri, incontreremo spesso:

| Operatore | Idea | Esempio | Risultato |
|---|---|---|---:|
| `+` | somma | `7 + 3` | `10` |
| `-` | differenza | `7 - 3` | `4` |
| `*` | prodotto | `7 * 3` | `21` |
| `/` | divisione | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | resto/modulo | `7 % 2` | `1` |
| `**` | potenza | `2 ** 3` | `8` |

Non scegliere un operatore perché "sembra giusto".

Chiediti:

> Quale trasformazione richiede il problema?

---

# 4. `/`, `//` e `%` non sono la stessa divisione

## `/` — divisione

```python
8 / 2
```

produce:

```text
4.0
```

In Python 3, `/` produce un risultato di tipo `float`, anche quando matematicamente il risultato è intero.

## `//` — floor division

```python
17 // 3
```

produce:

```text
5
```

Per numeri positivi puoi leggerlo inizialmente come:

> quanti gruppi completi da 3 stanno in 17?

Attenzione però: `//` è **floor division**, non una generica regola "taglia la parte decimale". Con numeri negativi vedremo che il comportamento segue il pavimento matematico. Per il core beginner useremo soprattutto casi positivi quando modelliamo gruppi completi.

## `%` — resto

```python
17 % 3
```

produce:

```text
2
```

I tre valori sono collegati:

```text
17 = (17 // 3) * 3 + (17 % 3)
17 = 5 * 3 + 2
```

Questa relazione è un ottimo strumento di controllo.

---

# 5. Worked example: secondi → minuti + resto

## Specifica

```text
INPUT: secondi_totali, intero non negativo
OUTPUT: minuti_completi e secondi_restanti
```

## Casi di test

| input | minuti | resto |
|---:|---:|---:|
| 137 | 2 | 17 |
| 60 | 1 | 0 |
| 59 | 0 | 59 |
| 0 | 0 | 0 |

## Codice

```python
secondi_totali = int(input())
minuti = secondi_totali // 60
secondi = secondi_totali % 60
print(minuti, secondi)
```

## Trace con 137

```text
secondi_totali        → 137
137 // 60             → 2
minuti                 → 2
137 % 60              → 17
secondi                → 17
print(minuti, secondi) → 2 17
```

Il codice è corto perché il problema è stato modellato bene prima.

---

# 6. `%` come domanda sul resto

Un numero intero è divisibile per 2 quando il resto della divisione per 2 è zero:

```python
numero % 2
```

Esempi:

```text
8 % 2 → 0
9 % 2 → 1
```

Per ora osserviamo soltanto il valore del resto.

Nel prossimo blocco, con `if`, useremo una condizione come:

```python
numero % 2 == 0
```

per decidere fra comportamenti diversi.

Non anticipiamo ancora tutta la selezione: qui impariamo la trasformazione numerica.

---

# 7. Potenze: `**`, non `^`

In Python:

```python
2 ** 5
```

produce:

```text
32
```

Un errore comune è scrivere:

```python
2 ^ 5
```

pensando che `^` significhi potenza.

In Python `^` ha un altro significato (XOR bit-a-bit), che non ci serve ora.

Regola beginner:

```text
potenza → **
```

---

# 8. Precedenza: Python deve sapere cosa calcolare prima

Considera:

```python
2 + 3 * 4
```

Python applica regole di precedenza e produce:

```text
14
```

perché il prodotto viene eseguito prima della somma.

Con:

```python
(2 + 3) * 4
```

il risultato diventa:

```text
20
```

## Regola pratica del corso

Non trasformiamo la precedenza in una gara di memoria.

Usa le parentesi quando:

- cambiano realmente l'ordine del calcolo;
- rendono più evidente l'intenzione;
- evitano a chi legge di dover ricostruire mentalmente un'espressione complessa.

Per il nostro livello basta ricordare la struttura generale:

```text
parentesi
→ potenze
→ *, /, //, %
→ +, -
```

Per casi più sottili, meglio rendere il codice esplicito invece di affidarsi alla memoria.

---

# 9. Espressione corretta ma difficile da leggere

Confronta:

```python
risultato = a + b * c - d / e
```

con:

```python
costo_componenti = b * c
quota = d / e
risultato = a + costo_componenti - quota
```

Le due forme non sono sempre equivalenti dal punto di vista del dominio, ma mostrano un criterio importante:

> un risultato intermedio con un buon nome può spiegare **che cosa significa** una parte del calcolo.

Non estrarre variabili inutili per ogni singolo simbolo; usale quando comunicano un concetto.

---

# 10. Microscope: tipo e valore

Prima di eseguire, completa la tabella.

| Espressione | Valore previsto | Tipo previsto |
|---|---|---|
| `7 + 3` | ? | ? |
| `7 / 2` | ? | ? |
| `7 // 2` | ? | ? |
| `7 % 2` | ? | ? |
| `2 ** 3` | ? | ? |
| `4 * 3.5` | ? | ? |

Poi verifica nel REPL con `type()` soltanto dopo aver scritto le previsioni.

Obiettivo:

```text
prevedere
→ osservare
→ spiegare una differenza
```

non copiare l'output del REPL.

---

# 11. Built-in: usare uno strumento quando esprime bene l'intenzione

Python fornisce funzioni built-in utili.

Esempi semplici:

```python
abs(-8)
round(3.14159, 2)
min(8, 3, 12)
max(8, 3, 12)
len("Python")
```

Non dobbiamo imparare una lunga lista di built-in.

La domanda è:

> questa funzione esprime meglio l'operazione che voglio fare rispetto a riscriverla manualmente?

`len()` era già comparsa come lente sulle stringhe; `min()` e `max()` qui sono semplici strumenti. Più avanti impareremo anche a calcolare min/max progressivamente per capire l'algoritmo sottostante.

---

# 12. Output leggibile con f-string

Per un programma destinato a una persona possiamo voler scrivere:

```python
nome = "Ada"
punti = 27
print(f"{nome} ha {punti} punti")
```

Output:

```text
Ada ha 27 punti
```

Dentro `{...}` possiamo inserire espressioni semplici:

```python
print(f"Il doppio è {numero * 2}")
```

## Contratto prima dell'estetica

Nelle Activity con output esatto dobbiamo comunque rispettare la specifica.

Se il contratto dice:

```text
OUTPUT: 54
```

stampare:

```text
Il doppio è 54
```

è un output diverso.

Le f-string sono uno strumento di presentazione, non un motivo per ignorare l'interfaccia richiesta.

---

# 13. Calcolare e stampare sono responsabilità diverse

Considera:

```python
base = 5
altezza = 3
area = base * altezza
print(area)
```

Qui possiamo distinguere:

```text
calcolo       → base * altezza
risultato     → area
presentazione → print(area)
```

Questa separazione diventerà sempre più utile quando i programmi cresceranno.

---

# 14. Prima funzione: dare un nome a una trasformazione

Possiamo dare un nome al calcolo dell'area:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Poi usarlo:

```python
area = area_rettangolo(5, 3)
print(area)
```

Per ora ci basta questo modello:

```text
input della trasformazione
        ↓
parametri
        ↓
calcolo
        ↓
return
        ↓
valore prodotto
```

Non stiamo ancora facendo il modulo completo sulle funzioni: scope, progettazione top-down, contratti e decomposizione sistematica arriveranno in PY2-05.

---

# 15. `return` non è `print`

Queste due funzioni non hanno lo stesso comportamento:

```python
def doppio(numero):
    return numero * 2
```

```python
def mostra_doppio(numero):
    print(numero * 2)
```

La prima **produce un valore** che può essere usato altrove:

```python
risultato = doppio(4)
print(risultato + 1)
```

La seconda produce output sul terminale, ma non sta restituendo quel numero al chiamante.

Per ora ricordiamo soltanto:

```text
return → valore verso chi ha chiamato la funzione
print  → output verso l'esterno
```

Approfondiremo questa distinzione con molti esempi in PY2-05.

---

# 16. Testare una piccola funzione

Per:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

possiamo pensare ai casi prima del codice:

| base | altezza | atteso |
|---:|---:|---:|
| 5 | 3 | 15 |
| 1 | 7 | 7 |
| 0 | 4 | 0 |

E poi verificare nel REPL:

```python
area_rettangolo(5, 3)
area_rettangolo(1, 7)
area_rettangolo(0, 4)
```

Non serve ancora un framework di testing per imparare l'idea fondamentale:

> una trasformazione dovrebbe poter essere verificata con esempi scelti consapevolmente.

---

# 17. Error Clinic

## Caso 1 — operatore sbagliato

```python
quadrato = numero ^ 2
```

Se volevi una potenza, l'operatore non esprime l'operazione richiesta.

## Caso 2 — divisione sbagliata per il dominio

```python
scatole = pezzi / capacita
```

Se il problema chiede **scatole complete**, probabilmente `/` non è il modello giusto.

## Caso 3 — resto dimenticato

```python
minuti = secondi_totali // 60
```

Se la specifica chiede anche i secondi rimanenti manca una parte dell'output.

## Caso 4 — precedenza non esplicita

```python
media = a + b + c / 3
```

La formula non calcola la media aritmetica dei tre valori.

Una forma corretta e chiara è:

```python
media = (a + b + c) / 3
```

## Caso 5 — funzione definita ma non chiamata

```python
def doppio(numero):
    return numero * 2

risultato = doppio
```

`doppio` e `doppio(5)` non sono la stessa cosa.

Per invocare la trasformazione servono le parentesi e gli argomenti richiesti.

## Caso 6 — stampare invece di restituire

Se una funzione deve produrre un valore riutilizzabile, sostituire `return` con `print` cambia il suo contratto.

---

# 18. Confrontare soluzioni

Problema:

> Converti una quantità di secondi in minuti completi e secondi restanti.

### Soluzione A

```python
minuti = secondi_totali // 60
resto = secondi_totali % 60
```

### Soluzione B

```python
minuti = int(secondi_totali / 60)
resto = secondi_totali - minuti * 60
```

Per input non negativi entrambe possono produrre lo stesso risultato nei casi semplici.

Ma la A comunica direttamente le due operazioni del problema:

```text
gruppi completi
resto
```

Il confronto non riguarda soltanto il numero di caratteri.

Criteri:

```text
correttezza
→ significato espresso
→ leggibilità
→ assenza di lavoro inutile
```

---

# 19. Esercizi brevi

## A — Predict

Prevedi valore e tipo:

```python
15 / 4
15 // 4
15 % 4
3 + 2 * 5
(3 + 2) * 5
2 ** 4
```

## B — Quoziente/resto

Dato un numero di caramelle e una dimensione fissa della confezione, calcola:

- confezioni complete;
- caramelle rimaste.

Prima scrivi input/output e almeno tre casi.

## C — Ore, minuti, secondi

Dato un numero non negativo di secondi, produci:

```text
ore_complete minuti_restanti secondi_restanti
```

Scomponi il problema prima di scrivere il codice.

## D — Debug

Correggi:

```python
a = int(input())
b = int(input())
media = a + b / 2
print(media)
```

Spiega il bug, non limitarti a modificare una riga.

## E — Prima funzione

Scrivi:

```python
def perimetro_rettangolo(base, altezza):
    ...
```

La funzione deve **restituire** il valore. Proponi tre casi di test prima dell'implementazione.

---

# 20. Activity planning — non ancora materializzato

Per M05 sono candidati:

- **A Observe/Trace:** precedenza, valore e tipo;
- **B Controlled Change:** correggere una formula mantenendo invariato il contratto I/O;
- **C Implement:** conversione secondi → unità + resti;
- **D Debug:** precedenza, `/` vs `//`, `%`, `^` vs `**`;
- **E Mini-program:** piccolo calcolatore a una sola trasformazione, senza selezione.

Non materializziamo ora una seconda Activity P1 nel repository: `py2-activity-b-input-somma-001` resta il canarino tecnico finché `python-docente#7` non è certificato.

---

# 21. Checkpoint M05

Senza eseguire Python, spiega:

1. Qual è la differenza tra `/`, `//` e `%`?
2. Perché `17 // 3` e `17 % 3` descrivono due parti dello stesso problema?
3. Perché `(a + b + c) / 3` è diverso da `a + b + c / 3`?
4. Qual è l'operatore di potenza in Python?
5. Perché una f-string può rendere sbagliato un output autogradato anche se il calcolo è corretto?
6. Che differenza c'è tra `return` e `print` nel nostro modello iniziale?
7. Perché mostriamo una funzione già ora senza approfondire ancora scope e decomposizione?

---

# 22. Sintesi

Porta con te questi modelli:

```text
espressione → valore
```

```text
/  → divisione
// → gruppi completi / floor division
%  → resto
```

```text
parentesi = intenzione esplicita
```

```text
buon nome → significato del risultato intermedio
```

```text
funzione piccola = trasformazione con un nome
```

```text
return ≠ print
```

Nel prossimo blocco useremo espressioni che producono `True`/`False` per prendere decisioni con `if`, `elif` ed `else`.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione e verifica tecnica:

- documentazione Python 3.12 — tutorial sui numeri/espressioni e reference delle espressioni;
- Allen Downey, *Think Python / Pensare in Python* — progressione beginner, funzioni e debugging;
- Mark Lutz, *Learning Python / Imparare Python* — copertura sistematica di espressioni/operatori/funzioni;
- Pluralsight Python Essentials — gap-check del percorso e dei laboratori.

Le fonti licensed sono teacher-reference e non testo da riprodurre.

## Collegamenti di progettazione

- `tracks/secondo/PY2_02_SPEC.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

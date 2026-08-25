# M05 — Runbook docente

## Modulo

**Espressioni, operatori e prime funzioni**  
UDA PY2-02 — Primi programmi Python

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Portare la classe dal semplice uso di variabili/input/output a un primo controllo consapevole del calcolo:

```text
problema
→ operazione richiesta
→ espressione
→ previsione
→ valore/tipo
→ casi di test
→ spiegazione della scelta
```

Il modulo introduce anche una funzione pura minuscola per mostrare presto che un programma non deve diventare un unico blocco monolitico. **Non** anticipare ancora il corso formale su scope, API, top-down design o pytest.

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL standard disponibile;
- workspace `.py` disponibile;
- VS Code soltanto se il workflow managed è certificato.

M05 non richiede una nuova capability piattaforma rispetto a M04.

## Materiali

- lesson `content/python/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`;
- slide `slides/python/modules/05_ESPRESSIONI_OPERATORI_PRIME_FUNZIONI.md`;
- quaderno/tabella prediction;
- M04 come richiamo;
- nessuna nuova Activity P1 obbligatoria finché `python-docente#7` non è certificato.

---

# Ritmo consigliato — seconda settimana di PY2-02

## Ora teoria attiva 1 — espressioni, divisioni, precedenza

### 0–10 min — retrieval M04

Domande rapide:

- che tipo restituisce `input()`?
- differenza tra `42` e `"42"`?
- che cosa significa prevedere prima di eseguire?

### 10–25 min — problema secondi → minuti/resto

Partire da `137` senza Python:

```text
137 = 2 × 60 + 17
```

Far emergere due risultati diversi prima di mostrare `//` e `%`.

### 25–40 min — `/`, `//`, `%`

Usare REPL con prediction:

```python
17 / 3
17 // 3
17 % 3
```

Ricostruire:

```text
17 = (17 // 3) * 3 + (17 % 3)
```

### 40–50 min — `**` e errore `^`

Mostrare un bug intenzionale. Non spiegare XOR in profondità; basta chiarire che `^` non è potenza.

### 50–60 min — precedenza

Confronto:

```python
2 + 3 * 4
(2 + 3) * 4
```

Regola didattica: parentesi quando rendono l'intenzione più evidente.

---

# Ora teoria attiva 2 — leggibilità, f-string, prima funzione

## 0–15 min — Microscope valore/tipo

Prediction table:

```python
7 + 3
7 / 2
7 // 2
7 % 2
2 ** 3
4 * 3.5
```

Il docente chiede prima **tipo e valore**, poi fa usare `type()` per verifica.

## 15–25 min — risultati intermedi con nomi

Confrontare una formula compatta con una decomposizione che usa nomi significativi.

Non imporre “una variabile per ogni operazione”: l'obiettivo è semantica, non verbosità.

## 25–35 min — built-in e f-string

Mostrare solo strumenti con ruolo chiaro:

```python
abs
round
min
max
len
```

Poi f-string come presentazione, ricordando che il contratto di output viene prima dell'estetica.

## 35–50 min — prima funzione pura

Costruire dal calcolo già noto:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Poi chiamarla con tre casi.

Non introdurre ancora:

- scope avanzato;
- default arguments;
- `*args`/`**kwargs`;
- type hints;
- docstring come standard formale;
- moduli/package.

## 50–60 min — `return` vs `print`

Confrontare due funzioni semplici. Far verbalizzare:

```text
return → valore al chiamante
print  → output
```

Non serve ancora spiegare formalmente `None` oltre ciò che emerge naturalmente se provato.

---

# Ora laboratorio

Poiché il canarino P1 M04 non è ancora certificato, il laboratorio M05 deve essere pratico ma **non introduce una nuova Activity autogradata obbligatoria**.

## Fase 1 — predict, 10 min

Tabella valore/tipo su 6 espressioni.

## Fase 2 — quoziente/resto, 15 min

Implementare manualmente:

```text
secondi → minuti completi + secondi restanti
```

Casi minimi:

```text
137 → 2 17
60  → 1 0
59  → 0 59
0   → 0 0
```

## Fase 3 — debug clinic, 15 min

Bug a rotazione:

```python
media = a + b + c / 3
quadrato = n ^ 2
minuti = secondi / 60
risultato = doppio
```

Per ogni bug:

```text
previsione
→ esecuzione
→ diagnosi
→ modifica minima
→ nuovo caso
```

## Fase 4 — funzione, 15 min

Implementare una funzione come:

```python
def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)
```

Lo studente propone prima tre casi.

## Fase 5 — exit explanation, 5 min

Domanda orale/scritta:

> Perché abbiamo usato `return` nella funzione e `print` soltanto fuori?

---

# Misconception watchlist

## M1 — `//` significa sempre “rimuovi i decimali”

Correzione: chiamarlo **floor division**. Per il modello gruppi completi usare inizialmente interi non negativi. Evitare di insegnare una falsa regola che crolla con i negativi.

## M2 — `%` serve soltanto a pari/dispari

Correzione: partire da quoziente/resto, packaging, tempo, ciclicità. Pari/dispari è un'applicazione.

## M3 — `^` è potenza

Correzione: contrasto diretto `2 ** 3` vs `2 ^ 3`. Non serve una lezione bitwise ora.

## M4 — parentesi solo se “Python non sa” la precedenza

Correzione: Python la sa; le parentesi servono anche al lettore e all'intenzione.

## M5 — f-string sempre migliore

Correzione: prima viene il contratto di output. Un test può richiedere solo il valore.

## M6 — funzione = codice più complicato

Correzione: scegliere trasformazioni minuscole e già comprese. La funzione dà un nome a qualcosa che sappiamo già calcolare.

## M7 — `return` stampa

Correzione: assegnare il risultato della funzione a un nome e usarlo in una seconda espressione.

## M8 — “più corto” = “migliore”

Correzione: confronto guidato su correttezza, significato e leggibilità.

---

# Differenziazione

## Recupero

- usare soltanto interi positivi per il primo modello `//`/`%`;
- disegnare gruppi da 60 o scatole da N prima del codice;
- una espressione per riga;
- parentesi esplicite;
- prima funzione già fornita con `def` e parametri, lasciando da completare il `return`.

## Enrichment

- verificare la relazione `a = (a // b) * b + (a % b)` su più valori con `b != 0`;
- osservare, senza trasformarlo in core, cosa accade con `//` su numeri negativi;
- costruire conversione secondi → ore/minuti/secondi;
- confrontare formula inline vs risultati intermedi;
- scrivere un quarto caso di test che distingua due implementazioni errate.

---

# Evidence docente

Raccogliere almeno:

- prediction valore/tipo;
- programma secondi → minuti/resto;
- una diagnosi di precedenza o operatore errato;
- una funzione pura piccola + tre casi;
- spiegazione `return` vs `print`.

Evidence formative; nessun voto principale obbligatorio in M05.

---

# Cosa NON anticipare

- `if` completo (solo preview tramite resto/condizione);
- cicli;
- exception handling;
- scope/globals in profondità;
- lambda;
- comprehensions;
- pytest;
- type hints;
- package/module design;
- decoratori;
- floating-point internals o `Decimal` come nuovo argomento.

---

# Handoff a PY2-03

M05 deve lasciare una domanda naturale:

> Possiamo ottenere un valore `True`/`False` da un'espressione e usarlo per decidere quale istruzione eseguire?

Da qui entrano:

```text
confronti
→ bool
→ if / else
→ elif
→ logica composta
```

---

# Stato tecnico

- lesson M05: **draft presente**;
- slides M05: **draft presente**;
- nuova Activity P1: **intenzionalmente non materializzata**;
- M04/P1 canary: `python-docente#7` ancora open;
- private Actions pre-job blocker: `python-docente#8`;
- curriculum: **FROZEN** in `doc/CURRICULUM_FREEZE_2026_2027.md`.

M05 può essere revisionato editorialmente mentre la certificazione M04 è bloccata dall'infrastruttura Actions, ma non viene promosso come contenuto classroom-ready in anticipo.
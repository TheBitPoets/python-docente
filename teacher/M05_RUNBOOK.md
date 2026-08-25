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

Il modulo introduce anche una funzione di calcolo minuscola per mostrare presto che un programma non deve diventare un unico blocco monolitico. **Non** anticipare ancora scope, API, top-down design o pytest.

---

# Priorità didattica

M05 è ricco: non tutto ciò che compare nella lesson deve diventare requisito della settimana.

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. spiegare che un'espressione produce un valore;
2. scegliere l'operatore in base al problema;
3. distinguere `/`, `//` e `%` nei casi beginner;
4. usare parentesi per rendere esplicito il calcolo;
5. usare risultati intermedi con nomi significativi;
6. definire/chiamare una prima funzione di calcolo molto semplice;
7. distinguere operativamente `return` e `print`;
8. proporre almeno tre casi per una trasformazione numerica semplice.

`**` resta un operatore core da riconoscere e usare in problemi elementari, ma non richiede un blocco didattico lungo.

## GUIDED EXPOSURE

- f-string;
- tipo prodotto da `/`;
- relazione quoziente/resto;
- funzione starter fornita dal docente da completare/modificare.

## ENRICHMENT / BACKUP

- comportamento di `//` con valori negativi;
- conversione ore/minuti/secondi più articolata;
- panoramica di `abs`, `round`, `min`, `max`, `len`;
- confronti estesi fra più formulazioni equivalenti.

Le built-in non sono un exit outcome autonomo di M05. In particolare `min/max` non devono sostituire il successivo apprendimento del min/max progressivo in M11.

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
- M04 come retrieval;
- nessuna nuova Activity P1 obbligatoria finché `python-docente#7` non è certificato.

---

# Ritmo consigliato — seconda settimana di PY2-02

## Ora teoria attiva 1 — espressioni, divisioni, precedenza

### 0–10 min — retrieval M04

Domande rapide:

- che tipo restituisce `input()`?;
- differenza tra `42` e `"42"`?;
- che cosa significa prevedere prima di eseguire?.

### 10–25 min — problema secondi → minuti/resto

Partire da `137` senza Python:

```text
137 = 2 × 60 + 17
```

Far emergere due risultati diversi prima di mostrare `//` e `%`.

### 25–42 min — `/`, `//`, `%`

Prediction REPL:

```python
17 / 3
17 // 3
17 % 3
```

Ricostruire:

```text
17 = (17 // 3) * 3 + (17 % 3)
```

Usare inizialmente interi non negativi per il modello “gruppi completi + resto”.

### 42–50 min — `**` e bug `^`

Un solo contrasto:

```python
2 ** 3
2 ^ 3
```

Non spiegare XOR: basta chiarire che `^` non è potenza.

### 50–60 min — precedenza e parentesi

Confrontare:

```python
2 + 3 * 4
(2 + 3) * 4
```

Regola didattica:

> Python conosce la precedenza; le parentesi aiutano anche il lettore a capire l'intenzione.

---

# Ora teoria attiva 2 — leggibilità, presentazione, prima funzione

## 0–10 min — Microscope valore/tipo

Prediction breve:

```python
7 + 3
7 / 2
7 // 2
7 % 2
4 * 3.5
```

Prima valore e tipo previsti, poi verifica con `type()`.

## 10–22 min — risultati intermedi con nomi

Confrontare formula compatta e decomposizione con nomi significativi.

Non imporre “una variabile per ogni operazione”: il nome deve comunicare un concetto.

## 22–30 min — f-string

Un solo esempio di presentazione:

```python
nome = "Ada"
punti = 27
print(f"{nome} ha {punti} punti")
```

Subito dopo ricordare:

> nelle Activity con output esatto viene prima il contratto, non l'estetica.

## 30–50 min — prima funzione di calcolo

Costruire dal calcolo già noto:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Poi chiamarla con tre casi.

Il termine “funzione pura” può restare nel lessico docente, ma non è un vocabolo da valutare in M05. Per gli studenti basta il modello:

```text
dati in ingresso
→ calcolo
→ valore restituito
```

## 50–60 min — `return` vs `print`

Confrontare:

```python
def doppio(numero):
    return numero * 2
```

con una funzione che stampa.

Exit verbalizzato:

```text
return → valore a chi ha chiamato
print  → output
```

### Se avanza tempo

Mostrare **una o due** built-in come esempio di “funzioni già fornite da Python”. Non trasformare `abs/round/min/max/len` in una lista da memorizzare.

---

# Ora laboratorio

Poiché il canarino P1 M04 non è ancora certificato, il laboratorio M05 è pratico ma non introduce una nuova Activity autogradata obbligatoria.

## Fase 1 — predict, 8–10 min

Tabella valore/tipo su poche espressioni mirate.

## Fase 2 — quoziente/resto, 15 min

Implementare:

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

Domanda:

> Perché abbiamo usato `return` nella funzione e `print` soltanto fuori?

---

# Minimum mastery gate — prima di PY2-03

Considerare M05 sufficientemente consolidato quando lo studente riesce, con una consegna breve, a:

- scegliere fra `/`, `//`, `%` spiegandone il motivo;
- correggere una precedenza sbagliata usando parentesi;
- prevedere valore/tipo di una piccola espressione;
- completare una funzione con un `return` corretto;
- distinguere `return` da `print`;
- proporre almeno tre casi per il proprio calcolo.

Se questi punti non sono stabili, usare il laboratorio/recupero per consolidarli invece di spendere tempo sulle built-in di enrichment.

---

# Misconception watchlist

## M1 — `//` significa sempre “rimuovi i decimali”

Correzione: chiamarlo **divisione intera per difetto (floor division)**. Per il modello gruppi completi usare inizialmente interi non negativi.

## M2 — `%` serve soltanto a pari/dispari

Correzione: partire da quoziente/resto, packaging, tempo, ciclicità. Pari/dispari è una sola applicazione.

## M3 — `^` è potenza

Correzione: contrasto diretto con `**`; niente bitwise ora.

## M4 — parentesi solo se “Python non sa” la precedenza

Correzione: Python la sa; le parentesi comunicano intenzione.

## M5 — f-string sempre migliore

Correzione: prima viene il contratto di output.

## M6 — funzione = codice più complicato

Correzione: partire da una trasformazione già compresa e darle un nome.

## M7 — `return` stampa

Correzione: assegnare il risultato della funzione a un nome e usarlo in una seconda espressione.

## M8 — “più corto” = “migliore”

Correzione: confronto su correttezza, significato e leggibilità.

---

# Differenziazione

## Recupero

- interi positivi per il primo modello `//`/`%`;
- disegnare gruppi da 60 o scatole da N prima del codice;
- una espressione per riga;
- parentesi esplicite;
- prima funzione già fornita, lasciando da completare il `return`.

## Enrichment

- verificare `a = (a // b) * b + (a % b)` con `b != 0`;
- osservare `//` con numeri negativi senza renderlo core;
- costruire secondi → ore/minuti/secondi;
- esplorare una o due built-in;
- scrivere un quarto caso che distingue due implementazioni errate.

---

# Evidence docente

Raccogliere almeno:

- prediction valore/tipo;
- programma secondi → minuti/resto;
- una diagnosi di precedenza o operatore errato;
- una funzione di calcolo piccola + tre casi;
- spiegazione `return` vs `print`.

Evidence formative; nessun voto principale obbligatorio in M05.

---

# Cosa NON anticipare

- `if` completo;
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

M05 può essere revisionato editorialmente mentre la certificazione M04 è bloccata dall'infrastruttura Actions, ma non viene promosso come classroom-ready in anticipo.
# M07 — Runbook docente

## Modulo

**`elif`, casi esclusivi e condizioni composte**  
UDA PY2-03 — Selezione e logica

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Il nodo concettuale è distinguere:

```text
una classificazione tra alternative
```

da:

```text
più effetti che possono coesistere
```

Lo studente non deve scegliere `elif` perché “ci sono tante condizioni”, ma perché i casi sono mutuamente esclusivi e vogliamo il primo ramo applicabile.

---

# Priorità didattica

M07 contiene molti concetti in una sola settimana. Il core deve restare centrato sulla struttura dei casi e sulla logica booleana essenziale.

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. spiegare il principio del **primo ramo vero** in `if/elif/else`;
2. distinguere casi mutuamente esclusivi da effetti indipendenti;
3. usare `and` e `or` con casi concreti;
4. usare `not` in condizioni semplici senza creare negazioni inutilmente difficili;
5. esprimere un intervallo prima in forma esplicita e poi concatenata;
6. progettare test sui confini di una classificazione;
7. diagnosticare soglie nell'ordine sbagliato e rami irraggiungibili.

## GUIDED EXPOSURE

- tabelle di verità minime;
- contesto logico creato dai rami precedenti;
- confronto fra due ordinamenti corretti delle soglie.

## ENRICHMENT / BACKUP

- short-circuit;
- esempio del divisore sicuro;
- varianti Romeo multi-regola.

**Short-circuit non è un exit outcome di M07.** Se il core non è stabile, usare quei minuti per confini, branch trace e scelta `elif` vs `if` indipendenti.

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL + script;
- Flowchart Lab se certificato, fallback carta/lavagna;
- Romeo solo enrichment/applicazione selettiva e soltanto con `romeo-sim` certificato.

## Materiali

- lesson `content/python/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`;
- slide `slides/python/modules/07_ELIF_LOGICA_CONDIZIONI_COMPOSTE.md`;
- carte/spec brevi da classificare come “un solo risultato” o “più effetti”;
- linea dei numeri per le fasce;
- truth table minima `and`/`or`.

---

# Ora teoria attiva 1 — `elif` e scelta della struttura

## 0–10 min — retrieval M06

- `=` vs `==`;
- soglia sotto/sulla/sopra;
- che cosa accade quando un `if` è falso?.

## 10–25 min — classificazione voto

Costruire prima i casi:

```text
< 6
6..7
>= 8
```

Poi mostrare la catena `if/elif/else`.

## 25–35 min — primo ramo vero

Trace su `5`, `7`, `9`.

Far verbalizzare:

> perché il secondo `elif voto < 8` non deve ripetere `voto >= 6`?

## 35–50 min — `if` indipendenti vs `elif`

Contrasto pioggia/freddo.

Usare almeno quattro specifiche e far scegliere la struttura **prima** di scrivere codice.

## 50–60 min — Error Clinic soglie

Esempio ramo irraggiungibile con ordine `>= 6` poi `>= 8`.

Far progettare l'input che espone il bug prima di eseguire.

---

# Ora teoria attiva 2 — logica composta

## 0–15 min — `and`

Partire da frase naturale:

```text
età >= 18 E biglietto valido
```

Costruire i quattro casi.

## 15–28 min — `or`

Esempio età < 6 OPPURE >= 65.

Far trovare:

- un caso con entrambe false;
- un caso con solo la prima vera;
- un caso con solo la seconda vera.

## 28–36 min — `not`

Mostrare negazione semplice, poi confronto di leggibilità:

```python
not eta < 18
```

vs

```python
eta >= 18
```

## 36–48 min — intervalli

Prima:

```python
x >= 0 and x <= 10
```

poi:

```python
0 <= x <= 10
```

La forma concatenata arriva **dopo** il modello logico.

## 48–60 min — mixed retrieval / confini

Non introdurre automaticamente un nuovo tema negli ultimi minuti.

Usare 3–4 micro-specifiche che mescolano:

```text
elif vs if indipendenti
and vs or
intervallo
confine
```

Lo studente deve motivare la struttura e proporre almeno un test che la distingue da una soluzione errata.

### Solo se la classe è chiaramente stabile

Mostrare short-circuit come **enrichment** con un unico esempio sicuro. Non valutarlo nel checkpoint ordinario.

---

# Ora laboratorio

## Fase 1 — struttura prima del codice, 10 min

Classificare 6 specifiche in:

```text
A — un solo risultato
B — più effetti possibili
```

## Fase 2 — classificatore, 15 min

Implementare tre fasce con test su tutti i confini.

## Fase 3 — logica composta, 15 min

Problema con due requisiti e tabella dei quattro casi.

## Fase 4 — debug clinic, 15 min

Bug:

- soglie in ordine errato;
- due `if` invece di `elif`;
- `elif` invece di condizioni indipendenti;
- `and` invece di `or`;
- intervallo con confine errato.

## Fase 5 — spiegazione, 5 min

Ogni studente completa:

> Ho scelto `...` perché nella stessa esecuzione ...

---

# Minimum mastery gate — prima di M08

Considerare il modulo consolidato quando lo studente riesce a:

- indicare quale ramo di una catena viene eseguito per un input concreto;
- scegliere `elif` o `if` indipendenti e motivarlo;
- completare i quattro casi di `and`/`or` con valori concreti;
- scrivere un intervallo chiuso semplice;
- proporre test per ogni confine di una classificazione;
- trovare un input che espone un ramo irraggiungibile o una soglia errata.

Short-circuit non fa parte di questo gate.

---

# Misconception watchlist

## M1 — `elif` è solo un `if` più corto

Correzione: primo ramo vero + esclusione dei successivi.

## M2 — tante condizioni → sempre `elif`

Correzione: relazione tra i casi, non quantità.

## M3 — `and` vuol dire “una delle due”

Correzione: truth table concreta.

## M4 — `or` vuol dire “esattamente una”

Correzione: mostrare caso True/True → True.

## M5 — `not` rende il codice più elegante

Correzione: usare la forma che comunica meglio il dominio.

## M6 — confronto concatenato come formula da imparare

Correzione: derivarlo dalla forma con `and`.

## M7 — il ramo centrale deve ripetere tutti i vincoli

Correzione: leggere il contesto creato dai rami precedenti, privilegiando comunque chiarezza.

## M8 — short-circuit è necessario per saper usare `and`

Correzione: no. È un comportamento utile da incontrare solo dopo la logica di base.

---

# Differenziazione

## Recupero

- massimo tre fasce;
- linea dei numeri;
- truth table compilata a metà;
- specifiche con parole `e` / `oppure` esplicite;
- far scrivere prima una frase “può succedere anche l'altro effetto?”.

## Enrichment

- due implementazioni corrette con soglie crescenti vs decrescenti;
- progettare casi che rendono evidente un ramo irraggiungibile;
- short-circuit con input sicuro;
- variante Romeo deterministica senza nuove API concettuali.

---

# Evidence docente

Raccogliere:

- trace di una catena;
- scelta motivata `if` indipendenti vs `elif`;
- truth table `and`/`or`;
- classificatore con test dei confini;
- un debug di ramo irraggiungibile;
- una condizione di intervallo spiegata.

---

# Cosa NON anticipare

- annidamenti complessi: M08;
- guard clauses come pattern sistematico;
- De Morgan formale;
- truthiness di collezioni;
- walrus operator;
- match/case;
- cicli di validazione;
- funzioni predicate come nuovo tema.

---

# Handoff a M08

Domanda finale:

> E se la seconda decisione ha senso soltanto dopo aver superato la prima? E quando un annidamento può essere semplificato senza cambiare il comportamento?

Da qui:

```text
selezione annidata
→ path trace
→ validazione
→ confronto annidato vs condizione composta
→ refactoring
```

---

# Stato tecnico

- lesson M07: **draft presente**;
- slide M07: **draft presente**;
- nuova Activity P1: **non materializzata**;
- M04 canary: `python-docente#7`;
- private Actions blocker: `python-docente#8`;
- Romeo: applicazione opzionale fino a certificazione runtime;
- curriculum: **FROZEN**.
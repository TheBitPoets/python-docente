# M06 — Runbook docente

## Modulo

**Booleani, confronti e prima selezione con `if`**  
UDA PY2-03 — Selezione e logica

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Far costruire il modello:

```text
specifica
→ domanda vero/falso
→ condizione Python
→ True / False
→ ramo
→ test del confine
```

Il successo non è “sa scrivere `if`”: lo studente deve saper spiegare **quale caso** identifica la condizione e quale input percorre ogni ramo.

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL + script `.py`;
- Flowchart Lab se certificato, altrimenti flow chart su carta/lavagna;
- Romeo `romeo-sim` solo come applicazione opzionale se il runtime è certificato.

## Materiali

- lesson `content/python/06_BOOLEANI_CONFRONTI_IF.md`;
- slide `slides/python/modules/06_BOOLEANI_CONFRONTI_IF.md`;
- tabella sotto/sulla/sopra soglia;
- uno o due flow chart sì/no;
- riferimento opzionale Romeo pinned `romeo-y1-u14-condizioni`.

Nessuna nuova Activity P1 obbligatoria finché M04 / `python-docente#7` non è certificato.

---

# Ora teoria attiva 1 — confronti e confini

## 0–10 min — richiamo M05

Usare `%` come ponte:

```python
8 % 2
9 % 2
```

Domanda:

> Come trasformiamo il resto in una domanda vero/falso?

Preview:

```python
numero % 2 == 0
```

## 10–25 min — `bool` da un confronto

Prediction REPL:

```python
7 > 3
7 < 3
7 == 7
7 != 7
```

Far dire esplicitamente:

```text
valore → confronto → bool
```

## 25–40 min — operatori e linguaggio naturale

Associare:

```text
almeno / al massimo / più di / meno di / esattamente
```

agli operatori corretti.

Usare una linea dei numeri per gli studenti che faticano sui confini.

## 40–50 min — `=` vs `==`

Contrasto diretto.

## 50–60 min — sotto / sulla / sopra

Per soglia `18`:

```text
17 / 18 / 19
```

Far progettare i tre casi prima di qualsiasi `if`.

---

# Ora teoria attiva 2 — `if`, `else`, indentazione

## 0–15 min — primo `if`

```python
if temperatura < 0:
    print("gelo")
```

Far eseguire due trace:

```text
-3
5
```

Punto chiave:

> ramo saltato ≠ errore.

## 15–30 min — indentazione

Mostrare:

```python
if temperatura < 0:
    print("gelo")
print("fine")
```

Chiedere quale `print` appartiene al ramo.

Non presentare l'indentazione come “stile Python”: è sintassi/struttura del blocco.

## 30–45 min — `if/else`

Caso maggiorenne/minorenne.

Far emergere che `else` rappresenta il complemento della condizione precedente: non serve riscrivere `eta < 18`.

## 45–55 min — flow chart → Python

Usare un flow chart già noto e tradurlo senza cambiare il modello della decisione.

## 55–60 min — exit ticket

Un confine semplice e una previsione del ramo.

---

# Ora laboratorio

## Fase 1 — prediction, 10 min

Tabella `True/False` + ramo per 6–8 casi.

## Fase 2 — soglia, 15 min

Implementare:

```text
spedizione gratuita da 50 compresi
```

Casi obbligatori:

```text
49 / 50 / 51
```

## Fase 3 — debug clinic, 15 min

Ruotare bug:

```text
> invece di >=
condizione invertita
= invece di ==
indentazione
messaggi scambiati tra i rami
```

Lo studente deve prima indicare **quale caso fallisce**.

## Fase 4 — flow chart → script, 15 min

Un problema sì/no non ancora visto.

Richieste:

1. input/output;
2. tre casi;
3. condizione;
4. codice;
5. trace di un caso.

## Fase 5 — Romeo opzionale, tempo residuo/enrichment

Se `romeo-sim` è certificato:

```text
romeo-y1-u14-condizioni — Decidi con if
```

Usarlo soltanto dopo che la selezione generale è già compresa.

---

# Minimum mastery gate — prima di M07

Considerare M06 consolidato quando lo studente riesce a:

- prevedere `True/False` per un confronto semplice;
- distinguere `=` e `==`;
- tradurre “almeno/al massimo/più di/meno di” nell'operatore corretto;
- scrivere un `if` e un `if/else` con indentazione corretta;
- fare il trace di un caso vero e uno falso;
- progettare test sotto/sulla/sopra una soglia;
- trovare un input che espone `>` vs `>=`.

Non richiedere truthiness, `is`, `match/case` o logica composta per superare questo gate: appartengono ad altri livelli/moduli.

---

# Misconception watchlist

## M1 — `=` e `==` sono quasi la stessa cosa

Correzione:

```text
=   assegna
==  produce bool confrontando valori
```

## M2 — `>` include il confine

Correzione: linea dei numeri + casi `17/18/19`.

## M3 — se il ramo non stampa nulla “il programma non ha funzionato”

Correzione: trace esplicito di condizione `False` e continuazione dopo il blocco.

## M4 — indentazione solo per bellezza

Correzione: mostrare due programmi con appartenenza diversa al blocco.

## M5 — bisogna sempre scrivere `else`

Correzione: distinguere “azione solo se…” da “due risultati complementari”.

## M6 — `is` va bene al posto di `==`

Correzione: nel core beginner uguaglianza di valore = `==`; `is` verrà dopo con identità degli oggetti.

## M7 — testare 25 basta per una soglia 18

Correzione: il confine è il caso che distingue `>` da `>=`.

---

# Differenziazione

## Recupero

- una sola condizione per esercizio;
- linea dei numeri;
- tabella `input → True/False → ramo → output`;
- flow chart con due soli rami;
- starter con `if/else` già strutturato lasciando la condizione da completare.

## Enrichment

- progettare un caso che distingue due condizioni quasi equivalenti;
- confrontare `if` senza `else` vs `if/else` per specifiche diverse;
- osservare `type(7 >= 7)`;
- missione Romeo simulata;
- scrivere una specifica naturale a partire da un `if` dato.

---

# Evidence docente

Raccogliere almeno:

- tabella di confronti `True/False`;
- tre test intorno a una soglia;
- un trace `if` vero e falso;
- un debug del confine;
- una traduzione flow chart → `if/else`;
- breve spiegazione `=` vs `==`.

---

# Cosa NON anticipare

- catene `elif` complete: M07;
- `and`, `or`, `not` come nuovo blocco: M07;
- truthiness di stringhe/liste;
- espressione ternaria;
- `match/case`;
- `is` come tema;
- guard clause/refactoring avanzato;
- cicli di validazione: arriveranno con `while`.

---

# Handoff a M07

M06 lascia volutamente aperta una domanda:

> E se i casi non sono soltanto due? E se due condizioni possono essere vere nello stesso momento?

Da qui:

```text
elif
→ primo ramo vero
→ casi mutuamente esclusivi
→ if indipendenti
→ and / or / not
```

---

# Stato tecnico

- lesson M06: **draft presente**;
- slides M06: **draft presente**;
- Romeo mapping: già congelato/selettivo;
- nuova Activity P1: **non materializzata**;
- canarino P1: `python-docente#7`;
- private Actions blocker: `python-docente#8`;
- Flowchart Lab: `2cornot2c#753/#754`;
- curriculum: **FROZEN**.
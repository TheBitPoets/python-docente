# M10 — Runbook docente

## Modulo

**`for`, `range` e scelta `for` vs `while`**  
UDA PY2-04 — Iterazione e pattern algoritmici

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Far passare la classe da:

```text
so scrivere due sintassi di ciclo
```

a:

```text
capisco che cosa controlla la ripetizione
→ scelgo il costrutto che comunica meglio l'algoritmo
```

Il cuore è la scelta `for` vs `while`, non la memorizzazione di tutte le forme possibili di `range` né l'uso precoce di `break/continue`.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. prevedere i valori prodotti da `range(stop)`, `range(start, stop)` e semplici `range(start, stop, step)`;
2. spiegare start incluso e stop escluso;
3. riconoscere direzione dello step e range vuoto;
4. diagnosticare off-by-one;
5. scegliere `for` quando il percorso/numero di iterazioni è noto;
6. scegliere `while` quando la durata dipende dallo stato;
7. riscrivere un semplice `while`-contatore come `for` mantenendo lo stesso comportamento;
8. riconoscere un contatore manuale che duplica inutilmente la variabile del `for`.

## GUIDED EXPOSURE

- leggere e spiegare un `break` semplice;
- leggere e spiegare un `continue` semplice;
- confrontare queste forme con una versione basata su condizioni normali.

## ENRICHMENT / BACKUP

- range decrescenti o con step meno immediati;
- calcolo a mano del numero di iterazioni in range non banali;
- Romeo a numero noto di ripetizioni.

`break` e `continue` devono essere riconosciuti, ma **non costituiscono un gate autonomo di M10**.

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL + script;
- Romeo `romeo-sim` soltanto come optional applicativo.

## Materiali

- lesson `content/python/10_FOR_RANGE_SCELTA_CICLO.md`;
- slide `slides/python/modules/10_FOR_RANGE_SCELTA_CICLO.md`;
- schede “prevedi il range”;
- coppie di soluzioni `while`/`for` equivalenti;
- problemi da classificare per costrutto.

Nessuna nuova Activity P1 finché M04/#7 non è certificato.

---

# Ora teoria attiva 1 — `for` e `range`

## 0–10 min — retrieval M09

- stato/condizione/aggiornamento;
- zero iterazioni;
- terminazione.

Domanda:

> Se sappiamo già quali valori attraversare, dobbiamo gestire tutto manualmente?

## 10–25 min — `range(stop)`

Prediction su:

```python
range(5)
range(1)
range(0)
```

Stop escluso fin dall'inizio.

## 25–40 min — start/stop/step

Far prevedere prima del REPL:

```python
range(2, 6)
range(2, 10, 2)
range(5, 0, -1)
```

Per ogni range chiedere:

```text
primo valore?
ultimo valore effettivo?
verso?
```

## 40–50 min — range vuoto

Contrasto:

```python
range(5, 0)
range(5, 0, -1)
```

## 50–60 min — off-by-one

Problemi “includi 5” / “escludi 5” con spiegazione del confine.

---

# Ora teoria attiva 2 — scelta del ciclo e refactoring

## 0–22 min — `for` vs `while`

Classificare problemi prima di scrivere codice.

Criterio:

```text
for → percorso/numero di iterazioni noto
while → durata dipendente da condizione/stato
```

## 22–38 min — refactoring contatore

Confrontare:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

con:

```python
for i in range(5):
    print(i)
```

Far nominare lo stato manuale eliminato.

## 38–48 min — stato ridondante

Mostrare un contatore che duplica `i`. Distinguere da un contatore futuro che misura una quantità diversa: questo prepara M11.

## 48–60 min — mixed retrieval

Usare problemi brevi che mescolano:

- scelta `for`/`while`;
- stop escluso;
- step;
- off-by-one;
- range vuoto.

### Solo se il core è stabile

Mostrare un esempio di `break` e uno di `continue` come **guided exposure**. Chiedere che cosa cambia nel flusso e se una versione senza questi costrutti sarebbe più chiara.

---

# Ora laboratorio

## Fase 1 — range microscope, 10 min

Prevedere cinque range:

- crescente;
- con start;
- step 2;
- decrescente;
- vuoto.

## Fase 2 — implement, 15 min

Countdown e ripetizione N volte.

## Fase 3 — scelta costrutto, 10 min

Sei specifiche brevi, una frase di motivazione ciascuna.

## Fase 4 — refactoring, 15 min

Riscrivere un `while` contatore con `for`; verificare stessi output/casi.

## Fase 5 — consolidamento o Romeo, 10 min

Prima scelta: consolidamento su off-by-one/range se necessario.

Solo se il core è stabile e `romeo-sim` è certificato, usare `romeo-y1-u15-ciclo-for` o scenario equivalente.

---

# Minimum mastery gate — prima di M11

Considerare M10 consolidato quando lo studente riesce a:

- scrivere la sequenza prodotta da range semplici;
- spiegare perché lo stop è escluso;
- riconoscere un range vuoto o lo step nel verso sbagliato;
- correggere un off-by-one;
- scegliere `for`/`while` e motivarlo;
- trasformare un semplice `while` contatore in `for`;
- individuare stato manuale ridondante.

Non richiedere uso autonomo di `break`/`continue` per superare il gate.

---

# Misconception watchlist

## M1 — lo stop di `range` è incluso

Correzione: scrivere sempre la sequenza prima del codice.

## M2 — `range(5,0)` dovrebbe scendere automaticamente

Correzione: step predefinito = +1.

## M3 — `for` è sempre migliore di `while`

Correzione: validazione/sentinella sono naturalmente dinamiche.

## M4 — `while` è sempre più potente quindi più professionale

Correzione: preferire la struttura che comunica meglio l'intenzione e riduce stato manuale inutile.

## M5 — dentro `for` devo incrementare `i`

Correzione: `for` assegna i valori successivi prodotti dal range; modificare `i` nel corpo non controlla la sequenza futura del range.

## M6 — ogni `for` richiede un contatore separato

Correzione: distinguere indice del percorso da quantità che vogliamo misurare.

## M7 — `break`/`continue` rendono il codice automaticamente più elegante

Correzione: sono guided exposure; confrontare leggibilità e flusso.

---

# Differenziazione

## Recupero

- range piccoli e visualizzati su linea dei numeri;
- sempre primo/ultimo/quanti valori;
- solo step +1 prima dei countdown;
- coppie equivalenti `while`/`for` già quasi complete.

## Enrichment

- range con step negativo e confini diversi;
- calcolare a mano quante iterazioni senza materializzare liste grandi;
- refactoring di più forme equivalenti;
- `break`/`continue` su esempi controllati;
- Romeo quadrato/schemi ripetuti.

---

# Evidence docente

Raccogliere:

- previsione di range;
- debug off-by-one;
- scelta motivata `for` vs `while`;
- refactoring `while`→`for`;
- spiegazione di stato ridondante.

`break/continue` possono comparire come evidence soltanto se realmente svolti.

---

# Cosa NON anticipare

- iterazione formale su liste: arriverà con le collezioni;
- `enumerate`, `zip` come nuovi temi;
- `for/else`;
- comprehensions;
- iterator protocol/generatori;
- cicli annidati: M12;
- pattern accumulatori/ricerca formalizzati: M11.

---

# Handoff a M11

Domanda finale:

> Durante un ciclo, come ricordiamo quante volte è successa una cosa, la somma dei valori già visti o se abbiamo trovato ciò che cercavamo?

Da qui:

```text
stato progressivo
→ contatore
→ accumulatore
→ min/max
→ flag/ricerca
```

---

# Stato tecnico

- lesson M10: **draft presente**;
- slide M10: **draft presente**;
- nuova Activity P1: **non materializzata**;
- canarino P1: `python-docente#7`;
- private Actions blocker: `python-docente#8`;
- Romeo: opzionale fino a certificazione runtime;
- curriculum: **FROZEN**.
# M09 — Runbook docente

## Modulo

**`while`, stato, sentinelle e validazione ripetuta**  
UDA PY2-04 — Iterazione e pattern algoritmici

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Far costruire questo modello, non una ricetta sintattica:

```text
stato iniziale
→ condizione di continuazione
→ corpo
→ aggiornamento
→ nuovo controllo
```

Per ogni `while` lo studente deve saper rispondere:

> **che cosa cambia e perché il ciclo può terminare?**

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL + script `.py`;
- flow chart su Flowchart Lab se certificato, altrimenti carta/lavagna;
- `romeo-sim` solo come applicazione opzionale.

## Materiali

- lesson `content/python/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`;
- slide `slides/python/modules/09_WHILE_STATO_SENTINELLE_VALIDAZIONE.md`;
- tabelle di trace;
- esempi di validazione M08 da trasformare in ripetizione;
- un esempio sentinella.

Nessuna nuova Activity P1 obbligatoria finché M04 / `python-docente#7` non è certificato.

---

# Ora teoria attiva 1 — stato, condizione, terminazione

## 0–10 min — ponte da M08

Riprendere:

```python
if voto < 0 or voto > 10:
    print("dato non valido")
```

Nuova specifica:

> chiedi di nuovo finché il voto è valido.

Far emergere che una decisione singola non basta.

## 10–25 min — primo `while`

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

Identificare insieme:

```text
inizializzazione
condizione
corpo
aggiornamento
```

## 25–40 min — trace

Tabella iterazione/stato/condizione/output. Far includere anche il controllo finale `False`.

## 40–50 min — terminazione

Domanda sistematica:

> quale istruzione rende possibile che la condizione diventi falsa?

## 50–60 min — ciclo infinito

Togliere l'aggiornamento e far prevedere il comportamento prima dell'esecuzione.

---

# Ora teoria attiva 2 — validazione e sentinella

## 0–20 min — validazione ripetuta

Costruire:

```python
voto = int(input())
while voto < 0 or voto > 10:
    voto = int(input())
```

Usare input `12, -1, 7`.

## 20–30 min — zero/una/molte iterazioni

Progettare tre sequenze di input che producano i tre casi.

## 30–45 min — sentinella

Pattern:

```text
leggi
finché valore != sentinella
    elabora
    leggi di nuovo
```

Far discutere perché la sentinella deve essere distinguibile dai dati normali.

## 45–55 min — debug aggiornamento in un solo ramo

Esempio in cui `0` blocca il progresso. Far seguire il path esatto.

## 55–60 min — `while True` preview

Mostrarlo soltanto come alternativa, non come modello base. Chiedere sempre: dove si trova il percorso di uscita?

---

# Ora laboratorio

## Fase 1 — trace, 10 min

Due cicli piccoli: uno con zero iterazioni, uno con più iterazioni.

## Fase 2 — validazione, 15 min

Richiedere un intero in un intervallo. Prima progettare sequenze di input per 0/1/3 ripetizioni.

## Fase 3 — sentinella, 10 min

Leggere dati fino al valore di fine senza elaborare la sentinella.

## Fase 4 — Debug Clinic, 15 min

A rotazione:

- aggiornamento mancante;
- aggiornamento solo in un ramo;
- condizione invertita;
- inizializzazione errata;
- off-by-one.

## Fase 5 — spiegazione, 10 min

Per un ciclo scelto dallo studente:

```text
stato iniziale = ...
continua quando = ...
progredisce perché = ...
termina quando = ...
```

---

# Misconception watchlist

## M1 — `while` = `if` scritto tante volte

Correzione: il controllo viene rieseguito dopo ogni aggiornamento dello stato.

## M2 — se il programma continua a stampare, Python è bloccato

Correzione: cercare la storia di terminazione e lo stato che dovrebbe cambiare.

## M3 — l'aggiornamento può stare in qualunque ramo

Correzione: verificare ogni path che mantiene il ciclo attivo.

## M4 — `while True` è più semplice quindi sempre migliore

Correzione: richiede comunque una condizione/azione di uscita spiegabile.

## M5 — la sentinella è un dato come gli altri

Correzione: serve a controllare la fine e normalmente non viene elaborata.

## M6 — validazione ripetuta significa anche gestire testo non convertibile

Correzione: in M09 il contratto fornisce il tipo previsto; `try/except` arriverà più avanti.

## M7 — `while` deve eseguire almeno una volta

Correzione: mostrare un caso con condizione iniziale falsa.

---

# Differenziazione

## Recupero

- contatori su 2–3 iterazioni;
- evidenziare con colori stato/condizione/aggiornamento;
- tabelle di trace già impostate;
- validazione con un solo intervallo;
- starter che lascia da completare solo condizione o aggiornamento.

## Enrichment

- confrontare condizione in testata vs `while True` + `break`;
- costruire un test che trova un aggiornamento mancante in un ramo;
- scegliere una sentinella corretta per un dominio dichiarato;
- missione Romeo `y1-u16-ciclo-while` con simulatore certificato.

---

# Evidence docente

Raccogliere:

- trace completo con controllo finale;
- spiegazione della terminazione;
- validazione ripetuta;
- pattern sentinella;
- un debug di ciclo infinito;
- casi zero/una/più iterazioni.

---

# Cosa NON anticipare

- `for`/`range`: M10;
- accumulatori/ricerca come pattern formalizzati: M11;
- cicli annidati: M12;
- gestione eccezioni `try/except`;
- iterator protocol;
- `for/else`;
- generatori.

---

# Handoff a M10

Domanda finale:

> Se sappiamo già che vogliamo attraversare esattamente i valori `0,1,2,3,4`, dobbiamo gestire manualmente stato e incremento?

Da qui:

```text
for
→ range
→ stop escluso
→ for vs while
```

---

# Stato tecnico

- lesson M09: **draft presente**;
- slide M09: **draft presente**;
- nuova Activity P1: **non materializzata**;
- canarino P1: `python-docente#7`;
- private Actions blocker: `python-docente#8`;
- Romeo loop: opzionale fino a certificazione runtime;
- curriculum: **FROZEN**.

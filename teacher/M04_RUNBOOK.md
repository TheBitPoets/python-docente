# M04 — Runbook docente

## Modulo

**Interprete, REPL, script, valori e input/output**  
UDA PY2-02 — Primi programmi Python

Stato: vertical slice draft.

## Obiettivo docente

Portare una classe che conosce algoritmi/flow chart ma non Python a una prima esperienza controllata in cui lo studente:

```text
prevede
→ prova nel REPL
→ comprende tipo/valore
→ salva uno script
→ legge input
→ converte
→ produce output
→ incontra un errore
→ testa più casi
```

Il successo della lezione non è "hanno copiato quattro righe". È che sanno spiegare il flusso dei dati e distinguere almeno errore sintattico/runtime/logico a livello iniziale.

---

# Preparazione

## Ambiente

Target:

- Classroom Environment TheBitLab;
- Python 3.12;
- REPL standard Python;
- workspace del corso scrivibile;
- VS Code solo se il workflow managed è già certificato; altrimenti editor/terminal del profilo supportato.

Non dare istruzioni di installazione Python/VS Code per conto del corso.

Se l'ambiente non è certificato, il contenuto può essere spiegato/demonstrato ma non dichiarare il vertical slice operativo completato.

## Materiali

- lesson `content/python/04_INTERPRETE_REPL_VALORI_IO.md`;
- slide `slides/python/modules/04_INTERPRETE_REPL_VALORI_IO.md`;
- Activity `py2-activity-b-input-somma-001`;
- carta/quaderno per prediction/trace.

## Verifiche rapide prima della classe

Il docente dovrebbe poter:

1. aprire il REPL;
2. eseguire un file `main.py` dal workspace;
3. creare/scaffoldare l'Activity quando il flusso TheBitLab è disponibile;
4. verificare manualmente che la soluzione di riferimento produca 5, 0, 6 sui tre casi;
5. sapere che `python-docente#7` è il gate tecnico del vertical slice e non dichiarare CI verde finché non lo è.

---

# Ritmo consigliato — 2 ore teoria attiva + 1 laboratorio

Il modulo può occupare principalmente la prima settimana di PY2-02; M05 completa la seconda.

## Ora teoria attiva 1 — REPL, valori e nomi

### 0–10 min — richiamo

Riprendere un algoritmo noto:

```text
leggi A
leggi B
somma
mostra
```

Domanda:

> Che cosa manca per farlo eseguire a un computer?

### 10–25 min — interprete e REPL

Breve modello, poi immediatamente prediction:

```python
2 + 3
10 / 2
"2" + "3"
```

Non mostrare il risultato prima delle previsioni.

### 25–40 min — valori e tipi

Microscope con:

```python
42
3.5
"42"
True
```

Usare `type()` come lente, non come nozione da memorizzare.

### 40–55 min — nomi/assegnamento

```python
eta = 15
eta + 1
eta = 16
```

Domande diagnostiche:

- `eta` e `15` sono la stessa cosa?
- cosa cambia dopo il secondo assegnamento?
- perché `=` non significa la stessa cosa dell'uguaglianza matematica?

### Exit micro-check

Ogni studente scrive una previsione su tipo/valore di 3 espressioni.

---

# Ora teoria attiva 2 — input/output, conversioni, script, errori

## 0–15 min — `print` vs REPL display

Mostrare:

```python
2 + 3
```

nel REPL e poi in uno script.

Far emergere la necessità di `print()` per output esplicito.

## 15–30 min — `input()` restituisce `str`

Far digitare un numero e verificare:

```python
dato = input()
type(dato)
```

Poi contrastare:

```python
"2" + "3"
2 + 3
```

## 30–40 min — conversioni

Costruire insieme:

```python
numero = int(input())
print(numero + 1)
```

Non presentare `int()` come rituale: chiedere quale tipo serve al calcolo.

## 40–50 min — primo `main.py`

Trasferire un esperimento dal REPL a un file.

Far eseguire più volte lo stesso file con input diversi.

## 50–60 min — Error Clinic

Mostrare rapidamente:

- syntax error;
- name error;
- conversion ValueError;
- errore logico senza traceback.

Il docente modella la lettura del traceback, non risolve immediatamente il bug.

---

# Ora laboratorio — Activity B

## Fase 1 — prediction, 5 min

Prima di aprire lo starter:

```text
2 + 3 → ?
0 + 0 → ?
-4 + 10 → ?
```

## Fase 2 — osserva lo starter, 5 min

Chiedere di identificare:

- righe di input;
- conversioni;
- riga di calcolo;
- riga di output.

## Fase 3 — modifica controllata, 10 min

Lo studente cambia soltanto:

```python
risultato = 0
```

nel calcolo corretto.

Se modifica tutto il file, chiedere perché: l'obiettivo include imparare a fare una modifica minima e spiegabile.

## Fase 4 — test/report, 10–15 min

Quando il runner è disponibile:

- eseguire i test;
- leggere quale caso passa/fallisce;
- collegare il report al contratto input/output.

Se il P1 vertical slice non è certificato, eseguire manualmente i tre casi nel Classroom Environment e registrare evidence formativa; non simulare un PASS TheBitLab inesistente.

## Fase 5 — debug variants, 10 min

Proporre a rotazione:

```python
risultato = primo - secondo
```

oppure rimuovere `int()`.

Gli studenti devono prevedere il tipo di errore/comportamento prima dell'esecuzione.

## Fase 6 — spiegazione, 5–10 min

Domande a campione:

- perché `input()` viene convertito?
- che cosa contiene `risultato`?
- perché proviamo un numero negativo?
- perché il programma non stampa un prompt?

---

# Misconception watchlist

## M1 — `input()` produce un numero se digito cifre

Correzione: esperimento `type()` + confronto `"2" + "3"`.

## M2 — REPL e script mostrano sempre le stesse cose

Correzione: espressione senza `print` in file.

## M3 — variabile = scatola immutabile

Non serve ancora smontare completamente il modello, ma evitare frasi come "la variabile contiene per sempre". Usare nome → valore/riferimento e mostrare riassegnamento.

## M4 — se non c'è traceback è corretto

Correzione: programma che sottrae invece di sommare.

## M5 — test = prova matematica di correttezza

Dire:

> i test aumentano la nostra evidenza e trovano errori; tre casi non dimostrano automaticamente ogni comportamento possibile.

## M6 — cambiare molte righe è più bravo

Activity B enfatizza modifica minima e comprensione.

---

# Differenziazione

## Recupero

- tenere input e calcolo su righe separate;
- usare valori hardcoded prima di `input`;
- un tipo alla volta;
- fare trace su carta;
- starter quasi completo.

## Enrichment

- `type()` su più espressioni;
- differenza `10 / 2` vs tipo risultante come osservazione, senza anticipare M05 in profondità;
- conversione `float`;
- trovare un input che fa fallire `int()`;
- progettare un quarto caso di test e motivarlo.

---

# Evidence docente

Raccogliere almeno:

- prediction REPL;
- trace breve;
- Activity B/manual equivalent;
- spiegazione di `input()` → `str`;
- un Error Clinic corretto.

Queste evidence sono formative; M04 non richiede un voto principale.

---

# Cosa NON anticipare

- `if`;
- `while`/`for`;
- exception handling con `try`;
- venv/pip;
- pytest;
- type hints;
- classi;
- molte built-in;
- internals completi CPython.

Gli errori vengono osservati e letti; la gestione programmata delle eccezioni arriverà più avanti.

---

# Handoff a M05

M04 lascia aperte domande naturali:

- quali operatori abbiamo oltre `+`?
- che cosa succede con `/`, `//`, `%`?
- come controlliamo la precedenza?
- come formattiamo output più leggibile?
- possiamo dare un nome a un calcolo che vogliamo riutilizzare?

Queste domande aprono M05 — espressioni, operatori e prime funzioni.

---

# Stato tecnico del vertical slice

- lesson M04: **draft presente**;
- slides M04: **draft presente**;
- Activity B: **presente**;
- P1 runner TheBitLab: esiste genericamente;
- certificazione consumer `python-docente`: **OPEN `python-docente#7`**;
- Actions osservate: failure pre-execution senza step, non evidence di failure del test body;
- Classroom Environment: blocker `python-docente#2` / `2cornot2c#753/#754`.

Non dichiarare "M04 pronto per classe" finché i gate di delivery applicabili non sono stati collaudati.

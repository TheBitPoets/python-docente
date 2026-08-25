# Review didattica/semantica — PY2-05 + Checkpoint A

> Data: 2026-08-25  
> Scope: M13–M16 + Checkpoint A, lesson/deck/runbook/SPEC + Git G1 consumer boundary.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Verificare che il passaggio da controllo del flusso a funzioni/decomposizione/testing:

- non ripeta inutilmente la preview di funzioni già avvenuta in M05;
- non anticipi formalismi professionali;
- mantenga `return`, scope, composizione, top-down e regression come strumenti beginner;
- integri Git G1 senza sottrarre al checkpoint il suo ruolo di consolidamento Python.

Regola di pacing:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# Architettura UDA

La progressione è corretta:

```text
M13  formalizza funzione / parametri / return
 ↓
M14  rende esplicito il flusso dei dati e lo scope locale
 ↓
M15  progetta responsabilità prima dei dettagli
 ↓
M16  rende eseguibili le aspettative e protegge il refactoring
 ↓
Checkpoint A  consolida + registra un primo checkpoint Git significativo
```

Non serve cambiare l'ordine né il monte ore frozen.

---

# M13 — Funzioni produttive

## Giudizio

**Buono**, ma deve essere percepito come formalizzazione della preview M05, non come “nuova sintassi da zero”.

Retrieval esplicito:

```text
M05: ho già visto una piccola funzione
M13: ora capisco con precisione chiamata, parametri, return e test
```

### MUST MASTER

1. definizione vs chiamata;
2. parametro vs argomento;
3. uno/più parametri semplici;
4. `return` e uso del valore restituito;
5. `return` vs `print`;
6. funzione di calcolo separata dall'output;
7. call trace semplice;
8. verifica con più casi.

### GUIDED EXPOSURE

- `None` quando manca `return` esplicito;
- predicate booleano come funzione con nome significativo.

### ENRICHMENT / BACKUP

- return multiplo/tuple preview;
- più `return` in rami diversi quando non complica il modello;
- chiamate più concatenate.

### Finding Git

Il vecchio runbook M13 anticipava `git status/diff`. Questo contraddice il consumer contract corrente:

```text
M14–M16 → G1.OBSERVE.STATUS / G1.OBSERVE.DIFF
```

Decisione: **nessun outcome Git in M13**. Git inizia in M14, quando esiste un refactoring/dipendenza globale significativo da osservare.

---

# M14 — Scope locale, passaggio dati, composizione

## Giudizio

**Ben calibrato** se si evita LEGB e si mantiene il principio:

> una funzione riceve esplicitamente ciò che le serve e restituisce ciò che produce.

### MUST MASTER

1. riconoscere nomi locali alla chiamata;
2. capire che un locale non è disponibile fuori dalla funzione;
3. passare dati esplicitamente;
4. evitare stato globale di lavoro come scorciatoia;
5. usare il return di A come input di B;
6. seguire un flusso di dati con variabili intermedie;
7. leggere un call graph semplice.

### GUIDED EXPOSURE

- costante di dominio a livello modulo vs dato di lavoro globale;
- `git status`/`git diff` come outcome G1 guidati per osservare un refactoring.

### ENRICHMENT

- call graph a tre livelli;
- confronto fra composizione compatta e variabili intermedie;
- casi di dipendenze esterne più articolati.

Git resta evidence di processo, non un outcome Python da pesare pesantemente.

---

# M15 — Top-down e responsabilità

## Giudizio

**Molto buono**, con un rischio: trasformare il design in burocrazia.

### MUST MASTER

1. individuare 2–4 responsabilità in un problema adeguato;
2. proporre nomi/firme prima dei corpi;
3. distinguere input, logica e output;
4. stabilire parametri e risultato atteso;
5. costruire un piccolo call graph;
6. implementare/testare una funzione alla volta;
7. riconoscere una funzione che aggrega responsabilità non correlate.

### GUIDED EXPOSURE

- contratto intuitivo;
- termini pre-condizione/post-condizione in linguaggio naturale;
- `git diff` come lente sul refactoring/estrazione.

### ENRICHMENT

- confronto fra due decomposizioni entrambe plausibili;
- smell più sottili;
- contratti più ricchi.

### Regola anti-burocrazia

Per un esercizio piccolo non richiedere documenti lunghi. Bastano, quando utili:

```text
funzione
parametri
return
1 riga di responsabilità
2–4 casi
```

Il design deve ridurre il carico mentale, non aggiungere un modulo cartaceo parallelo.

---

# M16 — `assert`, regression, refactoring

## Giudizio

**Ben calibrato** se `assert` resta il ponte fra casi pensati e aspettative eseguibili.

### MUST MASTER

1. trasformare casi semplici in `assert`;
2. scegliere caso normale + confini rilevanti;
3. leggere un `AssertionError` elementare;
4. capire che test verde non dimostra correttezza universale;
5. distinguere bug nel codice e test incoerente con la specifica;
6. costruire un regression test che riproduce un bug;
7. correggere con modifica minima e rieseguire tutti i test;
8. refactorare mantenendo gli stessi test verdi.

### GUIDED EXPOSURE

- confronto fra due implementazioni con lo stesso contratto;
- P2 come **boundary di delivery docente/piattaforma**, non come concetto da studente.

### ENRICHMENT

- suite più ampia;
- ragionamento su casi non coperti;
- più refactoring consecutivi.

### Finding slide

Il deck studente contiene una slide tecnica `P2 TheBitLab`. Questa informazione appartiene al runbook/delivery, non al mastery dello studente. Va rimossa o convertita in teacher-only/backup.

---

# Checkpoint A — Python + Git senza collisione

## Finding principale

Il Checkpoint A è una settimana di 3 ore flessibili che può contenere:

- consolidamento;
- recupero;
- prova pratica;
- mini-project;
- primo checkpoint Git guidato.

Non può realisticamente contenere anche il completamento del **corso standalone G1**.

Il consumer contract Git già consente un sottoinsieme di outcome. La delivery Python deve quindi dichiarare:

```text
mode = embedded outcome subset
full G1 track completion = false
full G1 lesson completion = false
```

Le lesson G1-M02…M06 sono **fonti canoniche/remediation surfaces**, non cinque lezioni da completare integralmente nella settimana 17.

## Modalità consigliata

Git viene incorporato nel lavoro Python:

```text
prima/durante il lavoro
  status / diff

quando il programma è verificato
  test
  add selettivo
  diff --staged
  commit
  status
  log/show
```

Non aggiungere una seconda verifica Git ad alto rischio nella stessa ora della prova Python.

## Se la classe non ha ancora acquisito status/diff in M14–M16

Non insegnare in emergenza tutto G1 durante la prova valutativa.

Usare:

- remediation canonica G1;
- esercitazione guidata separata nel tempo flessibile del checkpoint;
- valutazione Python indipendente dalla difficoltà iniziale sul workflow Git.

## Peso valutativo

Git resta prevalentemente:

```text
process evidence / formative
```

Nel voto Python non deve dominare correttezza, algoritmo, funzioni e test.

---

# Modello temporale suggerito del Checkpoint A

Non è un orario rigido; dipende dall'uso scelto della settimana.

## Variante assessment-focused

```text
Python practical / recovery      dominante
Git preflight status/diff        micro-check
Git final checkpoint             10–20 min guidati se il lavoro è pronto
```

## Variante lab/consolidation-focused

```text
mini-project Python
→ status/diff durante il lavoro
→ test
→ staging/commit/history guidati
```

Il corso Git standalone può essere svolto altrove/come cross-course track, ma non viene implicitamente “addebitato” alle 3 ore Python del Checkpoint A.

---

# Esito

```text
PY2-05 architecture/order       PASS
M13 pacing                      PASS after retrieval + Git boundary fix
M14 pacing                      PASS
M15 pacing                      PASS with anti-bureaucracy rule
M16 pacing                      PASS; P2 kept teacher/delivery-side
Checkpoint A                    PASS after embedded-G1 clarification
```

Nessun curriculum change richiesto.

## Next review

```text
PY2-06 — M17–M19
PY2-07 — M20–M22 + Checkpoint B
```

Focus:

- evitare che string methods diventino catalogo da memorizzare;
- distinguere algoritmo su sequenza da built-in disponibile;
- alias/copia/mutabilità senza introdurre prematuramente il modello di memoria formale;
- matrici dopo M12 senza ripetizione sterile;
- selezione degli esercizi `friedpython` solo dopo audit individuale.

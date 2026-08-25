# Review didattica/semantica — PY2-04

> Data: 2026-08-25  
> Scope: M09–M12, lesson + deck + runbook + SPEC.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Verificare che le quattro settimane dedicate a iterazione e pattern algoritmici costruiscano un modello mentale progressivo senza trasformare i costrutti in ricette da memorizzare.

Vincolo invariato:

```text
4 settimane × 3 ore
= 12 ore nominali
```

La review non cambia il curriculum frozen. Applica la stessa gerarchia già adottata per PY2-02/PY2-03:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# Giudizio di architettura UDA

La progressione è corretta:

```text
M09
while = stato + condizione + aggiornamento + terminazione
        ↓
M10
for/range = percorso noto + scelta for vs while
        ↓
M11
il ciclo attraversa, lo stato ricorda
        ↓
M12
più dimensioni + quantità di lavoro
```

Non sono emersi prerequisiti invertiti o necessità di spezzare l'UDA.

Il rischio principale non è l'ordine, ma la **densità percepita** di M09/M10/M11.

---

# M09 — `while`, stato, sentinelle e validazione ripetuta

## Giudizio

**Struttura didattica molto forte.** Il modulo parte correttamente da M08: una validazione singola diventa una richiesta ripetuta.

Il vero outcome è la “storia di terminazione”:

```text
stato iniziale
→ condizione di continuazione
→ corpo
→ aggiornamento
→ nuovo controllo
```

La sentinella è core perché introduce una forma diversa di terminazione non basata su un numero noto di iterazioni.

### MUST MASTER

1. riconoscere inizializzazione, condizione, corpo, aggiornamento;
2. fare trace includendo il controllo finale `False`;
3. spiegare quale stato cambia e perché il ciclo può terminare;
4. individuare aggiornamento mancante o eseguito solo su alcuni path;
5. gestire zero/una/più iterazioni;
6. implementare una validazione ripetuta;
7. usare una sentinella dichiarata fuori dal dominio normale;
8. diagnosticare condizione invertita e off-by-one elementare.

### GUIDED EXPOSURE

- distinzione verbale “condizione di continuazione” vs “condizione di uscita”;
- confronto tra forma con condizione in testata e forma con uscita interna.

### ENRICHMENT / BACKUP

- `while True` + `break` come forma alternativa;
- confronto sistematico fra due forme equivalenti;
- Romeo `while` simulato.

`while True` **non entra nel minimum mastery gate**: non deve diventare una scorciatoia per evitare il ragionamento sulla terminazione.

---

# M10 — `for`, `range` e scelta `for` vs `while`

## Giudizio

**Ben progettato**, ma `break`/`continue` non devono sottrarre tempo a `range`, off-by-one e scelta del costrutto.

### MUST MASTER

1. prevedere i valori di `range(stop)`, `range(start, stop)`, `range(start, stop, step)` in casi semplici;
2. spiegare start incluso / stop escluso;
3. riconoscere direzione dello step e range vuoto;
4. individuare off-by-one;
5. scegliere `for` quando il percorso è noto;
6. scegliere `while` quando la durata dipende dallo stato;
7. rifattorizzare un semplice `while`-contatore in `for`;
8. riconoscere un contatore manuale che duplica inutilmente la variabile del `for`.

### GUIDED EXPOSURE

- `break` come interruzione esplicita;
- `continue` come salto del resto dell'iterazione;
- confronto di leggibilità con una versione senza questi costrutti.

### ENRICHMENT / BACKUP

- range decrescenti più articolati;
- calcolo del numero di iterazioni su range non banali;
- Romeo a numero noto di ripetizioni.

`break` e `continue` devono essere **riconosciuti e letti**, ma non costituiscono un gate autonomo di M10.

---

# M11 — Contatori, accumulatori, min/max, ricerca e flag

## Giudizio

**È il modulo con il maggior rischio di “catalogo di ricette”.**

La lesson contiene però già la soluzione pedagogica corretta:

> il ciclo attraversa; lo stato ricorda.

Il modulo deve essere insegnato come una sola famiglia:

```text
problema
→ quale informazione deve sopravvivere alla prossima iterazione?
→ quale variabile rappresenta quella informazione?
→ come viene inizializzata?
→ quando viene aggiornata?
→ quale frase deve restare vera dopo ogni iterazione?
```

### MUST MASTER

1. distinguere contatore e accumulatore dal significato dello stato;
2. inizializzare lo stato al livello corretto;
3. usare `if` per decidere se aggiornare lo stato;
4. esprimere un invariante intuitivo in una frase;
5. costruire min/max progressivo a partire da un dato reale quando esiste almeno un elemento;
6. evitare sentinelle numeriche arbitrarie non garantite dal dominio;
7. distinguere “esiste?”, “primo match?”, “quanti match?”;
8. usare un flag semplice per rappresentare “almeno un match visto finora”;
9. riconoscere quando il flag non aggiunge significato;
10. proteggere una media/rapporto dal caso conteggio zero.

### GUIDED EXPOSURE

- `break` come alternativa per una ricerca del primo match quando il contratto permette di fermarsi;
- confronto flag vs stop anticipato;
- media condizionale come applicazione di contatore + accumulatore.

### ENRICHMENT / BACKUP

- posizione del primo match;
- confronto best/worst case in linguaggio naturale;
- più implementazioni equivalenti della ricerca;
- Romeo come dominio di conteggio/ricerca.

### Regola fondamentale

Non presentare agli studenti cinque template da copiare. Ogni esercizio deve iniziare con:

> Che cosa deve significare questa variabile dopo aver elaborato i primi `k` dati?

---

# M12 — Cicli annidati, griglie e quantità di lavoro

## Giudizio

**Ben calibrato** se resta una lezione su due dimensioni e quantità di lavoro osservabile, non una lezione anticipata di complessità algoritmica.

### MUST MASTER

1. distinguere ciclo esterno e interno;
2. fare trace di coppie `(riga, colonna)` su range piccoli;
3. prevedere `R × C` esecuzioni del corpo interno;
4. capire che il ciclo interno riparte per ogni iterazione esterna;
5. inizializzare/reset tare lo stato al livello corretto;
6. usare una condizione che dipende dalla coppia corrente;
7. riconoscere quando l'annidamento è naturale al problema;
8. riconoscere un calcolo chiaramente ripetuto pur non dipendendo dall'iterazione;
9. confrontare intuitivamente una scansione singola con una doppia scansione.

### GUIDED EXPOSURE

- `print(..., end="")` come puro strumento di output per costruire una riga;
- tabella `N` vs `N×N` per intuizione di crescita;
- spostamento fuori dal ciclo di un calcolo invariabile.

### ENRICHMENT / BACKUP

- pattern diagonali/inversi più elaborati;
- conteggi su griglie;
- confronto `N×M` vs `N×N` in più scenari;
- Romeo su percorsi a griglia.

Nessuna notazione Big-O fa parte del gate di seconda.

---

# Coerenza verticale PY2-04

La UDA costruisce una progressione coerente di controllo e stato:

```text
M09: perché continuo / perché termino?
M10: conosco già il percorso oppure dipende dallo stato?
M11: che cosa devo ricordare mentre attraverso i dati?
M12: che cosa succede quando attraverso due dimensioni?
```

Queste quattro domande devono essere più visibili delle keyword Python.

---

# Exit gate UDA raggruppato

Prima di PY2-05 lo studente deve dimostrare cinque competenze integrate:

## A — Controllare la ripetizione

- scegliere `for`/`while`;
- spiegare terminazione e confini.

## B — Tracciare

- eseguire trace di loop singoli e doppi piccoli;
- prevedere zero/una/più iterazioni.

## C — Mantenere stato

- contatore/accumulatore;
- min/max;
- flag/ricerca;
- inizializzazione e update corretti.

## D — Comporre

- `if` dentro loop;
- semplice doppio ciclo quando il dominio lo richiede.

## E — Ragionare sul lavoro

- `R × C`;
- riconoscere lavoro chiaramente inutile;
- privilegiare correttezza e leggibilità prima dell'ottimizzazione.

Non richiedere nel gate:

- `while True`;
- uso autonomo di `break/continue`;
- Big-O;
- `for/else`;
- iterator protocol;
- comprehensions.

---

# Esito

```text
PY2-04 architecture/order     PASS
M09 pacing                    PASS with while-True demotion
M10 pacing                    PASS with break/continue guided-only
M11 pacing                    PASS if taught as one state/invariant family
M12 pacing                    PASS; complexity remains intuitive only
```

Nessun curriculum change richiesto.

## Next review

```text
PY2-05 — M13–M16 + Checkpoint A
```

Focus:

- evitare doppione fra preview funzione M05 e formalizzazione M13;
- `return`/scope/composizione;
- top-down senza burocrazia;
- `assert`/regression senza trasformare il corso in testing framework;
- integrazione Git G1 già strutturale: verificarne il carico didattico nel Checkpoint A.

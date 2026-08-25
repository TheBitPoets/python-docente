# M11 — Runbook docente

## Modulo

**Contatori, accumulatori, minimo/massimo, ricerca e flag**  
UDA PY2-04 — Iterazione e pattern algoritmici

Stato: draft editoriale controllato.

## Obiettivo docente

Portare gli studenti dal semplice “so usare un ciclo” a:

```text
so quale informazione deve sopravvivere
→ scelgo una variabile che la rappresenta
→ la inizializzo correttamente
→ la aggiorno quando serve
→ so quale proprietà deve restare vera
→ scelgo casi che possono romperla
```

Il lessico chiave del modulo è **invariante intuitivo**. Non serve formalismo matematico: basta una frase corretta sulla variabile dopo ogni iterazione.

Esempi:

- `conteggio` = numero di positivi già elaborati;
- `totale` = somma dei valori già elaborati;
- `minimo` = più piccolo valore visto finora;
- `trovato` = almeno un match è comparso finora.

**Non insegnare questi casi come quattro/cinque ricette indipendenti.** Sono varianti dello stesso problema: che cosa deve ricordare il ciclo?

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. distinguere contatore e accumulatore dal significato dello stato;
2. inizializzare lo stato prima/al livello corretto del ciclo;
3. usare `if` per decidere se aggiornare lo stato;
4. scrivere una frase-invariante semplice;
5. mantenere min/max progressivo partendo da un dato reale quando il contratto garantisce almeno un elemento;
6. evitare sentinelle numeriche arbitrarie non garantite dal dominio;
7. distinguere `esiste?`, `primo match?`, `quanti match?`;
8. usare un flag semplice per rappresentare “almeno un match visto finora”;
9. riconoscere un flag che aggiunge solo meccanica;
10. evitare una divisione per zero quando una media dipende dal conteggio dei valori validi.

## GUIDED EXPOSURE

- `break` come alternativa per il primo match quando il contratto permette di fermarsi;
- confronto flag vs stop anticipato;
- media condizionale come applicazione di contatore + accumulatore.

## ENRICHMENT / BACKUP

- posizione del primo match;
- confronto caso migliore/peggiore in linguaggio naturale;
- due implementazioni equivalenti della ricerca;
- Romeo come dominio di conteggio/ricerca.

---

# Ritmo consigliato — settimana 11

## Ora teoria attiva 1 — stato progressivo: contatore e accumulatore

### 0–10 min — richiamo

Riprendere `for` e chiedere:

> Se il ciclo passa su dieci valori, che cosa devo ricordare tra un valore e il successivo?

Scrivere sempre prima la frase che descrive lo stato.

### 10–25 min — contatore

Costruire “quanti positivi?” con trace su 3–4 valori.

Prima della soluzione finale, ottenere dalla classe:

> `conteggio` = quanti positivi ho visto finora.

### 25–40 min — accumulatore

Costruire “somma dei valori” e poi “somma dei soli validi”.

Bug obbligatorio: reset del totale dentro il ciclo.

Domanda:

> quale frase non è più vera dopo il reset?

### 40–55 min — contatore + accumulatore

Somma dei validi + numero dei validi. La media è una **applicazione**, non un nuovo pattern.

Far emergere il caso `conteggio == 0` prima di eseguire.

### Exit micro-check

Dato un piccolo codice, lo studente scrive in una frase che cosa rappresentano le variabili di stato.

---

# Ora teoria attiva 2 — stessa idea, stato diverso: min/max e ricerca

## 0–18 min — minimo progressivo

Presentare deliberatamente:

```python
minimo = 999999
```

Chiedere:

> quale assunzione nascosta contiene?

Poi usare il primo dato quando il contratto garantisce almeno un valore.

Invariante:

> `minimo` = più piccolo valore visto finora.

Il massimo è lo stesso modello con confronto opposto: non serve ripartire da zero come se fosse un nuovo algoritmo.

## 18–35 min — ricerca: prima la domanda

Separare:

```text
esiste almeno un match?
qual è il primo match?
quanti match?
```

Per ogni richiesta chiedere quale stato serve davvero.

## 35–48 min — flag

Costruire:

```python
trovato = False
```

poi l'invariante:

> `trovato` dice se almeno un match è comparso finora.

Mostrare anche un esempio di flag ridondante.

## 48–60 min — retrieval integrato

Tre specifiche brevi. Per ciascuna lo studente deve indicare:

```text
stato necessario
valore iniziale
quando cambia
frase-invariante
caso che può rompere la soluzione
```

### Solo se il core è stabile

Mostrare `break` come alternativa per una ricerca del primo match. Non trasformarlo nel “modo giusto” di fare ricerca.

---

# Ora laboratorio

## Fase A — trace mirato, 10 min

Non usare una tabella con tutte le variabili insieme. Ogni esercizio contiene soltanto lo stato rilevante:

- `conteggio`;
- oppure `totale`;
- oppure `minimo`;
- oppure `trovato`.

## Fase B — controlled change, 10–15 min

Da “conta positivi” a “conta valori nell'intervallo 10..20”.

Prima modificare casi e frase-invariante, poi il codice.

## Fase C — implementazione integrata, 15–20 min

Serie di `N` valori con:

- conteggio dei validi;
- somma dei validi;
- media soltanto se il conteggio è diverso da zero.

## Fase D — Debug Clinic, 10 min

Assegnare varianti diverse:

- reset dentro il loop;
- aggiornamento nel ramo sbagliato;
- divisione per zero;
- minimo con sentinella fragile;
- flag mai aggiornato.

## Fase E — spiegazione, 5 min

Chiedere:

> Quale frase deve essere vera su questa variabile dopo ogni iterazione?

---

# Minimum mastery gate — prima di M12

Considerare M11 consolidato quando lo studente riesce a:

- scegliere fra contatore/accumulatore/min-max/flag a partire dalla specifica;
- inizializzare lo stato al livello corretto;
- dire quando deve essere aggiornato;
- formulare almeno una frase-invariante corretta;
- usare il primo dato per un min/max quando appropriato;
- distinguere esistenza/primo match/conteggio dei match;
- usare un flag semplice per “esiste almeno un match”;
- proteggere una media dal conteggio zero;
- diagnosticare reset/update errati tramite il significato dello stato.

Non richiedere uso autonomo di `break` o analisi formale del costo per superare il gate.

---

# Misconception watchlist

## M1 — contatore e accumulatore sono la stessa cosa

Correzione:

```text
contatore → quanti eventi/casi?
accumulatore → quale totale progressivo?
```

## M2 — inizializzare dentro il ciclo

Far eseguire un trace con due valori e chiedere quale invariante viene distrutto.

## M3 — sentinella numerica “molto grande” sempre valida

Chiedere quale sia il dominio reale. Se il limite non è garantito, l'inizializzazione è fragile.

## M4 — media sempre possibile

Forzare il caso senza valori validi.

## M5 — un flag è obbligatorio in ogni ricerca

Confrontare “esiste?”, “primo match” e “conta tutti”. La forma dipende dall'obiettivo.

## M6 — `break` è sempre migliore perché fa meno lavoro

Prima correttezza e contratto. Se servono tutti i dati/match, fermarsi non è equivalente.

## M7 — ogni pattern ha un template fisso da copiare

Correzione: tornare alla domanda sul significato della variabile dopo ogni iterazione.

---

# Differenziazione

## Recupero

- sequenze di 3–4 valori;
- una sola variabile di stato alla volta;
- trace completo;
- invariante fornito da completare;
- niente ricerca + media nello stesso esercizio iniziale.

## Enrichment

- due implementazioni equivalenti di ricerca;
- flag vs stop anticipato;
- posizione del primo match;
- motivare quando servono tutti i dati;
- discutere intuitivamente il lavoro nel caso migliore/peggiore senza Big-O.

---

# Evidence docente

Raccogliere almeno:

- un trace contatore/accumulatore;
- una frase-invariante corretta;
- un debug di reset/update;
- una gestione corretta del conteggio zero;
- una scelta motivata tra ricerca, conteggio e flag;
- un esempio di min/max inizializzato senza sentinella arbitraria.

---

# Romeo

Uso opzionale dopo gli esempi generali:

- contare eventi/azioni;
- accumulare tempo/distanza concettuale;
- flag “checkpoint raggiunto”;
- ricerca del primo obiettivo.

Nessuna Activity Romeo diventa obbligatoria finché `romeo-sim` non è certificato nel Classroom Environment.

---

# Cosa NON anticipare

- liste come contenitore dei dati se non necessarie al problema;
- `min()`/`max()` come sostituti del pattern;
- generator expressions/comprehensions;
- `any()`/`all()` come scorciatoie;
- Big-O formale;
- pytest;
- eccezioni avanzate.

Le built-in verranno confrontate più avanti, dopo aver compreso il meccanismo.

---

# Handoff a M12

M11 lavora su **uno stato progressivo durante una scansione**.

M12 aggiunge:

```text
ciclo esterno
→ per ogni valore, ciclo interno
→ coppie/griglie
→ quantità di lavoro
```

Domanda ponte:

> Se per ogni riga visito tutte le colonne, quante volte eseguo il corpo interno?

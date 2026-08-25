# M11 — Runbook docente

## Modulo

**Contatori, accumulatori, minimo/massimo, ricerca e flag**  
UDA PY2-04 — Iterazione e pattern algoritmici

Stato: draft editoriale controllato.

## Obiettivo docente

Portare gli studenti dal semplice “so usare un ciclo” a:

```text
so quale stato devo mantenere
→ so perché viene aggiornato
→ so quale proprietà deve restare vera
→ so scegliere casi che possono romperla
```

Il lessico chiave del modulo è **invariante intuitivo**. Non serve formalismo matematico: basta una frase corretta sulla variabile dopo ogni iterazione.

Esempi:

- `conteggio` = numero di positivi già elaborati;
- `totale` = somma dei valori già elaborati;
- `minimo` = più piccolo valore visto finora;
- `trovato` = almeno un match è comparso finora.

---

# Ritmo consigliato — settimana 11

## Ora teoria attiva 1 — contatore e accumulatore

### 0–10 min — richiamo

Riprendere `for` e chiedere:

> Se il ciclo passa su dieci valori, che cosa devo ricordare tra un valore e il successivo?

### 10–25 min — contatore

Costruire “quanti positivi?” con trace su 3–4 valori.

Far verbalizzare l'invariante prima di mostrare la soluzione finale.

### 25–40 min — accumulatore

Costruire “somma dei valori” e poi “somma dei soli validi”.

Bug obbligatorio: reset del totale dentro il ciclo.

### 40–55 min — combinazione

Somma + conteggio → media condizionale.

Far emergere il caso `conteggio == 0` prima di eseguire.

### Exit micro-check

Dato un piccolo codice, lo studente scrive in una frase che cosa rappresentano le variabili di stato.

---

# Ora teoria attiva 2 — min/max, ricerca e flag

## 0–15 min — minimo progressivo

Presentare deliberatamente:

```python
minimo = 999999
```

Chiedere:

> quale assunzione nascosta contiene?

Poi passare all'inizializzazione con il primo dato quando il contratto garantisce almeno un valore.

## 15–30 min — massimo e invarianti

Confrontare minimo/massimo come stesso schema con relazione opposta.

## 30–45 min — ricerca

Separare esplicitamente:

- esiste?;
- primo match?;
- quanti match?;
- tutti i match?.

Far scegliere se serve flag, conteggio o possibile stop anticipato.

## 45–55 min — flag utile vs ridondante

Mostrare un caso in cui il flag serve dopo il ciclo e uno in cui aggiunge solo meccanica.

### Exit micro-check

Tre specifiche brevi: scegliere `conteggio`, `totale`, `minimo/massimo`, `flag` o ricerca e motivare in una riga.

---

# Ora laboratorio

## Fase A — trace, 10 min

Tabelle con:

```text
valore
condizione
conteggio
totale
minimo
trovato
```

Non usare tutte le colonne in ogni esercizio: selezionare soltanto lo stato rilevante.

## Fase B — controlled change, 10–15 min

Da “conta positivi” a “conta valori nell'intervallo 10..20”.

Prima modificare i casi di test, poi il codice.

## Fase C — implementazione, 15–20 min

Serie di `N` valori con:

- conteggio dei validi;
- somma dei validi;
- media soltanto se possibile.

## Fase D — Debug Clinic, 10 min

Assegnare varianti diverse:

- reset dentro il loop;
- aggiornamento nel ramo sbagliato;
- divisione per zero;
- sentinella numerica fragile;
- flag mai aggiornato.

## Fase E — spiegazione, 5 min

Chiedere:

> Quale frase deve essere vera su questa variabile dopo ogni iterazione?

---

# Misconception watchlist

## M1 — contatore e accumulatore sono la stessa cosa

Correzione:

```text
contatore cambia di una quantità legata al numero di eventi
accumulatore incorpora un valore del problema
```

## M2 — inizializzare dentro il ciclo

Far eseguire un trace con due valori: l'errore diventa evidente.

## M3 — sentinella numerica “molto grande” sempre valida

Chiedere quale sia il dominio reale. Se non esiste un limite garantito, la sentinella è un'assunzione fragile.

## M4 — media sempre possibile

Forzare il caso senza valori validi.

## M5 — un flag è obbligatorio in ogni ricerca

Confrontare “esiste?”, “primo match” e “conta tutti”. La forma dipende dall'obiettivo.

## M6 — `break` è sempre più efficiente quindi migliore

Prima correttezza e contratto. Se l'input deve comunque essere consumato o servono tutti i match, fermarsi non è equivalente.

---

# Differenziazione

## Recupero

- sequenze di 3–4 valori;
- una sola variabile di stato alla volta;
- trace completo;
- invariante fornito da completare;
- niente ricerca + media nello stesso esercizio iniziale.

## Enrichment

- progettare due implementazioni equivalenti di ricerca;
- confrontare flag vs stop anticipato;
- aggiungere posizione del primo match;
- motivare quali casi obbligano a leggere tutta la sequenza;
- discutere intuitivamente il lavoro nel caso migliore/peggiore senza Big-O formale.

---

# Evidence docente

Raccogliere almeno:

- un trace contatore/accumulatore;
- una frase-invariante corretta;
- un debug di reset/update;
- una gestione corretta del conteggio zero;
- una scelta motivata tra ricerca, conteggio e flag.

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
- `min()`/`max()` come sostituti del pattern che stiamo imparando;
- generator expressions/comprehensions;
- `any()`/`all()` come scorciatoie della ricerca;
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

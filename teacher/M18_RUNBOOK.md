# M18 — Runbook docente

## Modulo

**Ricerca, membership, metodi e normalizzazione delle stringhe**  
UDA PY2-06 — Stringhe come sequenze e testo

Stato: draft editoriale controllato.

## Obiettivo docente

Far scegliere l'operazione in base alla domanda, non in base al metodo appena imparato:

```text
esistenza?        → in
posizione?        → find
normalizzazione?  → trasformazione str
algoritmo didattico? → loop esplicito
```

Il modulo non è un catalogo di metodi.

---

# Priorità didattica

## MUST MASTER

1. usare `in` quando serve esistenza;
2. usare `find()` quando serve la posizione e interpretare `-1`;
3. riconoscere il bug `if testo.find(...)`;
4. capire che i metodi `str` producono nuove stringhe e non mutano l'originale;
5. usare `strip()`/`lower()` in una normalizzazione semplice e motivata;
6. scegliere metodo standard vs loop esplicito in base all'outcome.

## GUIDED EXPOSURE

- `count()`;
- `startswith()` / `endswith()`;
- `replace()`;
- `upper()`.

## ENRICHMENT / BACKUP

- `strip(chars)` e la sua semantica non-substring;
- `casefold()`;
- catene di normalizzazione più ricche.

Non valutare la memoria della lista dei metodi. Valutare la **scelta dell'operazione dalla specifica**.

---

# Ora teoria attiva 1 — esistenza, posizione, conteggio

1. Partire da domande naturali, non dai nomi dei metodi.
2. Membership `in/not in`.
3. `find()` e valore `-1`.
4. Error Clinic su `if testo.find(...)`.
5. `count()` come guided exposure: usarlo quando coincide con il requisito, non come nuovo pattern obbligatorio.

Per ogni esempio chiedere:

```text
mi serve sapere se esiste?
mi serve la posizione?
mi serve il numero di occorrenze?
```

---

# Ora teoria attiva 2 — immutabilità e normalizzazione

1. Riprendere immutabilità M17.
2. `lower()` e `strip()` come trasformazioni core.
3. Far vedere che il risultato deve essere usato/assegnato.
4. Normalizzazione come decisione del contratto: che informazione posso ignorare?
5. Mostrare 1–2 metodi guided (`startswith`, `endswith`, `replace`) solo se rispondono a una domanda reale.
6. Confronto loop manuale vs metodo built-in.

Non spendere un blocco separato su ogni API.

---

# Laboratorio

- choose-the-operation;
- confronto case-sensitive vs normalizzato;
- validator semplice;
- debug `find`, risultato metodo ignorato;
- funzione `conta_vocali` come esercizio algoritmico.

Il laboratorio deve alternare:

```text
specifica → scelta operazione → casi → codice
```

non:

```text
usa obbligatoriamente il metodo appena spiegato
```

---

# Minimum mastery gate — prima di M19

Considerare M18 consolidato quando lo studente riesce a:

- scegliere `in` o `find` e motivarlo;
- spiegare `-1` di `find`;
- diagnosticare `if testo.find(...)`;
- conservare il risultato di `lower/strip` quando serve;
- spiegare perché la stringa originale non cambia;
- proporre una normalizzazione coerente con il contratto;
- scegliere fra metodo e loop in un esempio semplice.

`count`, `replace`, `startswith`, `endswith`, `upper`, `casefold` non sono tutti prerequisiti del gate.

---

# Misconception watchlist

- `find()` interpretato come booleano;
- metodi pensati come mutanti;
- `strip(chars)` interpretato come rimozione di una sottostringa;
- normalizzare tutto automaticamente;
- credere che built-in o loop manuale siano sempre superiori;
- scegliere un metodo perché compare nelle slide invece che perché risponde al requisito.

---

# Differenziazione

## Recupero

- una sola domanda per esercizio;
- confronto diretto `in` vs `find`;
- stringhe brevi;
- variabile separata per il risultato del metodo;
- `lower/strip` soltanto dopo aver spiegato cosa vogliamo ignorare.

## Enrichment

- `casefold()`;
- più normalizzazioni confrontate;
- `strip(chars)`;
- spiegare quale informazione una normalizzazione perde;
- confronto loop/metodo con stesso contratto.

---

# Evidence docente

Raccogliere:

- scelta `in/find` motivata;
- un debug `find()`;
- una trasformazione con nuovo valore;
- una normalizzazione motivata;
- una scelta metodo vs loop spiegata.

---

# `friedpython`

Il materiale legacy resta fonte di gap-check. Non importare esercizi fino all'audit individuale e alla riscrittura Python 3.12.

---

# P2 — teacher/delivery only

Le funzioni testuali pure sono candidate naturali al profilo `2cornot2c#756`; fino alla certificazione usare `assert`/manual evidence. Non è un outcome studente.

---

# Cosa NON anticipare

- regex;
- liste come struttura già padroneggiata;
- comprehension;
- bytes/encoding;
- ottimizzazioni stringa avanzate.

---

# Handoff a M19

M18 conosce alcune operazioni standard e soprattutto **come sceglierle**.

M19 le combina con cicli/funzioni per costruire algoritmi di testo, validatori e parsing semplice.

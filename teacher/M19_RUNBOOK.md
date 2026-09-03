# M19 — Runbook docente

## Modulo

**Algoritmi su testo e parsing semplice**  
UDA PY2-06 — Stringhe come sequenze e testo

Stato: draft editoriale controllato.

## Obiettivo docente

Chiudere l'UDA stringhe facendo riusare davvero:

```text
funzioni + loop + if + contatori + slicing + metodi + test
```

Il passaggio chiave è da “conosco alcune operazioni stringa” a:

> progetto un algoritmo testuale con contratto e casi limite.

---

# Priorità didattica

## MUST MASTER

1. combinare funzione + loop + `if` su una stringa;
2. riusare contatore/accumulatore su caratteri;
3. costruire una nuova stringa in un piccolo esercizio;
4. progettare casi limite coerenti col contratto;
5. validare un formato posizionale semplice con `len`/indici/slice;
6. separare analisi e presentazione;
7. motivare metodo standard vs algoritmo manuale.

## GUIDED EXPOSURE

- `isalpha()` / `isdigit()` / `isalnum()` come predicate standard disponibili;
- palindromo come confronto fra algoritmo esplicito e forma compatta;
- `split()` come ponte: riconoscere che restituisce una `list`.

## ENRICHMENT / BACKUP

- `join()`;
- palindrome tramite `[::-1]` dopo il modello manuale;
- `enumerate()` sul testo;
- validator con più regole.

`split()`/`join()` non devono comprimere la chiusura dell'UDA: M20 insegnerà davvero le liste.

---

# Ora teoria attiva 1 — algoritmi su testo

1. Conteggio caratteri con invariante del contatore.
2. Costruzione progressiva di una nuova stringa.
3. Palindromo spiegato con posizioni opposte o percorso equivalente.
4. Solo dopo, confronto con una forma compatta come `[::-1]` se il tempo lo permette.

La forma compatta è un confronto, non il punto di partenza.

---

# Ora teoria attiva 2 — parsing e bridge alle liste

1. Parsing posizionale `AAA-123`.
2. Validazione lunghezza prima degli accessi posizionali.
3. Predicate standard (`isalpha`/`isdigit`) come strumenti guided, non catalogo.
4. Casi limite stringa vuota/1 carattere/spazi quando rilevanti.
5. `split()` come ponte esplicito a `list`.

`join()` è enrichment: non è necessario per chiudere PY2-06.

---

# Laboratorio

- text trace con indice/carattere/accumulatore;
- validator di codice testuale;
- algoritmo su stringa con contratto esplicito;
- mini-normalizzatore/analizzatore con più funzioni;
- debug su off-by-one, immutabilità, metodo non assegnato e stringa vuota.

Non richiedere nello stesso esercizio tutti i predicate/metodi disponibili.

---

# Minimum mastery gate — exit PY2-06

Prima di entrare nelle liste verificare che lo studente sappia:

1. trattare `str` come sequenza immutabile;
2. usare indici e slicing semplici;
3. scegliere iterazione diretta/per indice;
4. scegliere membership/metodo/loop in base alla domanda;
5. normalizzare consapevolmente;
6. scrivere una funzione testuale con loop;
7. progettare casi limite;
8. separare analisi e output;
9. motivare metodo vs loop;
10. riconoscere che `split()` produce una lista.

`join`, regex, enumerate sul testo e palindrome compatto non fanno parte del gate ordinario.

---

# Misconception watchlist

- usare `[::-1]` senza saper spiegare l'idea del confronto;
- normalizzazione non dichiarata;
- parsing che assume una lunghezza senza verificarla;
- credere che `split()` restituisca una stringa;
- usare regex per evitare di capire il formato;
- confondere output di analisi e presentazione;
- trattare `isalpha/isdigit/isalnum` come tre nuovi algoritmi da memorizzare.

---

# Differenziazione

## Recupero

- stringhe molto brevi;
- contratto fornito;
- un solo loop;
- niente `split()` finché indici/slicing non sono stabili;
- casi limite suggeriti.

## Enrichment

- palindrome manuale vs slicing;
- `join` come ponte inverso di `split`;
- validator con più regole;
- `enumerate` se serve indice+valore.

---

# Evidence docente

Raccogliere:

- un algoritmo manuale su stringa;
- casi limite dichiarati;
- una funzione testuale pura;
- scelta metodo vs loop motivata;
- spiegazione di `split()` come ponte verso liste.

---

# `friedpython`

I candidati legacy stringhe restano sorgenti, non contenuto importato. Prima del riuso:

```text
audit individuale
→ outcome preciso M17/M18/M19
→ Python 3.12
→ starter/solution separati
→ casi limite
→ provenance
```

---

# P2 — teacher/delivery only

Le funzioni testuali sono candidate naturali per `2cornot2c#756`. Fino alla certificazione usare `assert` e evidence formative. Non è un outcome studente.

---

# Cosa NON anticipare

- regex;
- bytes/encoding;
- comprehension;
- liste complesse;
- performance avanzata;
- Unicode approfondito.

---

# Handoff a PY2-07

La domanda cambia da:

> come elaboro una sequenza immutabile di caratteri?

verso:

> come gestisco una sequenza mutabile di valori e che cosa succede quando due nomi indicano la stessa lista?

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

Il passaggio chiave è da “conosco metodi stringa” a “progetto un algoritmo testuale con contratto e casi limite”.

## Ora teoria attiva 1 — algoritmi su testo

1. Conteggio caratteri con invariante del contatore.
2. Costruzione progressiva di una nuova stringa.
3. Palindromo spiegato con posizioni opposte.
4. Solo dopo, confronto con `[::-1]`.

## Ora teoria attiva 2 — parsing e bridge alle liste

1. Parsing posizionale `AAA-123`.
2. Validazione lunghezza + tipi di carattere.
3. Casi limite stringa vuota/1 carattere/spazi.
4. `split()` come ponte esplicito a `list`.
5. `join()` come preview controllata.

## Laboratorio

- text trace con indice/carattere/accumulatore;
- validator di codice testuale;
- palindrome con contratto esplicito;
- mini-normalizzatore/analizzatore con più funzioni;
- debug su off-by-one, immutabilità, metodo non assegnato e stringa vuota.

## Misconception watchlist

- usare `[::-1]` senza saper spiegare l'algoritmo;
- normalizzazione non dichiarata;
- parsing che assume una lunghezza senza verificarla;
- credere che `split()` restituisca una stringa;
- usare regex per evitare di capire il formato;
- confondere output di analisi e presentazione.

## Differenziazione

### Recupero

- stringhe molto brevi;
- contratto fornito;
- un solo loop;
- niente `split()` finché indici/slicing non sono stabili;
- casi limite già suggeriti.

### Enrichment

- confrontare palindrome manuale vs slicing;
- discutere `join` come alternativa a concatenazioni ripetute;
- validator con più regole;
- `enumerate` come preview controllata se serve indice+valore.

## Evidence docente

Raccogliere:

- un algoritmo manuale su stringa;
- casi limite dichiarati;
- una funzione testuale pura;
- scelta metodo vs loop motivata;
- spiegazione di `split()` come ponte verso liste.

## `friedpython`

I sette esercizi legacy stringhe restano candidati, non contenuto importato. Prima del riuso:

```text
audit individuale
→ Python 3.12
→ obiettivo M17/M18/M19
→ starter/solution separati
→ casi limite
→ Activity A-F
```

## P2

Le funzioni testuali sono candidate naturali per `2cornot2c#756`. Fino alla certificazione usare `assert` e evidence formative.

## Cosa NON anticipare

- regex;
- bytes/encoding;
- comprehension;
- liste complesse;
- performance avanzata;
- Unicode approfondito.

## Exit checkpoint PY2-06

Prima di entrare nelle liste verificare:

1. sequenza/immutabilità;
2. indici e slicing;
3. iterazione diretta/per indice;
4. membership/metodi;
5. normalizzazione;
6. algoritmo testuale con loop;
7. casi limite;
8. funzioni testabili;
9. metodo vs loop;
10. `split()` produce una lista.

## Handoff a PY2-07

La domanda cambia da:

> come elaboro una sequenza immutabile di caratteri?

verso:

> come gestisco una sequenza mutabile di valori e che cosa succede quando due nomi indicano la stessa lista?

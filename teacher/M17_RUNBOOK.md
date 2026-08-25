# M17 — Runbook docente

## Modulo

**Stringhe: indici, slicing e immutabilità**  
UDA PY2-06 — Stringhe come sequenze e testo

Stato: draft editoriale controllato.

## Obiettivo docente

Far cambiare modello mentale da:

```text
testo = qualcosa da stampare
```

a:

```text
str = sequenza ordinata immutabile
```

Il focus è posizione, slicing e scelta tra iterazione diretta/per indice.

---

# Ritmo consigliato — settimana 18

## Ora teoria attiva 1 — sequenza e indici

1. Disegnare la stringa con indici positivi/negativi.
2. Usare `len()` e ultimo indice valido.
3. Fare prediction su accessi singoli.
4. Mostrare `IndexError` e chiedere quale limite è stato superato.

## Ora teoria attiva 2 — slicing e immutabilità

1. Leggere `start:stop` con stop escluso.
2. Confrontare indice singolo fuori range e slice fuori range.
3. Introdurre step semplice.
4. Provare una mutazione e discutere perché fallisce.
5. Costruire una nuova stringa con concatenazione + slice.

## Laboratorio

- index/slice microscope;
- controlled change di slice;
- estrazione prefisso/suffisso;
- debug su indici/immutabilità;
- confronto `for carattere in testo` vs `for i in range(len(testo))`.

---

# Misconception watchlist

## M1 — primo indice = 1

Disegnare sempre il modello 0-based nelle prime attività.

## M2 — stop dello slice incluso

Collegare esplicitamente a `range`.

## M3 — slice fuori range genera sempre errore

Contrasto pratico con indice singolo.

## M4 — posso modificare un carattere

Mostrare che `str` è immutabile e si crea un nuovo valore.

## M5 — usare indice è più “professionale”

No. Se serve solo il carattere, iterazione diretta comunica meglio l'intenzione.

## M6 — ogni simbolo umano visibile è sempre un singolo indice

Non introdurre dettagli Unicode complessi, ma evitare affermazioni assolute scorrette.

---

# Differenziazione

## Recupero

- stringhe di 3–5 caratteri;
- indice scritto sotto ogni carattere;
- slice senza step;
- una sola operazione alla volta;
- trace su carta.

## Enrichment

- indici negativi;
- step;
- inversione con slicing dopo aver spiegato il modello;
- breve nota Unicode controllata;
- confronto di due soluzioni di estrazione.

---

# Evidence docente

Raccogliere almeno:

- prediction su indici;
- due slice spiegati;
- un debug `IndexError`;
- spiegazione dell'immutabilità;
- scelta motivata tra iterazione diretta/per indice.

---

# `friedpython`

Il legacy pack contiene materiale stringhe utile come fonte di controllo, ma non viene copiato. Prima di importare qualsiasi esercizio serve audit individuale Python 3.12 e riscrittura nel contratto Activity.

---

# Cosa NON anticipare

- `bytes`/encoding;
- regex;
- liste come struttura già padroneggiata;
- comprehension;
- performance avanzata delle stringhe;
- Unicode approfondito.

---

# Handoff a M18

M17 risponde:

> dove si trova il testo e come ne estraggo una parte?

M18 risponde:

> come cerco, normalizzo e trasformo il testo usando metodi standard o loop espliciti?

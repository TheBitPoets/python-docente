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

Il focus è posizione, slicing, immutabilità e scelta tra iterazione diretta/per indice.

---

# Priorità didattica

## MUST MASTER

1. descrivere `str` come sequenza ordinata immutabile;
2. usare `len()` e indici da zero;
3. riconoscere l'ultimo indice positivo valido;
4. distinguere accesso singolo e slicing;
5. usare `start:stop` con stop escluso;
6. spiegare perché una stringa non si modifica per indice;
7. costruire un nuovo valore quando serve una trasformazione;
8. scegliere iterazione diretta o per indice in base al problema.

## GUIDED EXPOSURE

- indici negativi oltre il semplice `-1`;
- step nello slicing;
- differenza fra indice singolo fuori range e slice oltre il limite.

## ENRICHMENT / BACKUP

- inversione `[::-1]`;
- escape meno comuni;
- nota Unicode teacher-side;
- raw/triple strings.

Non trasformare `[::-1]` in una formula da memorizzare prima che il modello `start:stop:step` sia chiaro.

---

# Ritmo consigliato — settimana 18

## Ora teoria attiva 1 — sequenza e indici

1. Disegnare la stringa con indici positivi e `-1` per l'ultimo carattere.
2. Usare `len()` e ultimo indice valido.
3. Fare prediction su accessi singoli.
4. Mostrare `IndexError` e chiedere quale limite è stato superato.
5. Estendere agli indici negativi soltanto quanto serve alla lettura naturale di ultimo/penultimo.

## Ora teoria attiva 2 — slicing e immutabilità

1. Leggere `start:stop` con stop escluso e collegarlo a `range`.
2. Confrontare indice singolo fuori range e slice oltre il limite.
3. Provare una mutazione e discutere perché fallisce.
4. Costruire una nuova stringa con concatenazione + slice.
5. Mostrare uno step semplice solo dopo che `start:stop` è stabile.

L'inversione `[::-1]` resta enrichment: verrà eventualmente confrontata con un algoritmo esplicito in M19.

## Laboratorio

- index/slice microscope;
- controlled change di slice;
- estrazione prefisso/suffisso;
- debug su indici/immutabilità;
- confronto `for carattere in testo` vs `for i in range(len(testo))`.

---

# Minimum mastery gate — prima di M18

Considerare M17 consolidato quando lo studente riesce a:

- trovare un carattere con un indice valido;
- spiegare il rapporto `len` / ultimo indice;
- leggere e scrivere uno slice `start:stop` semplice;
- distinguere indice singolo fuori range e slice;
- spiegare che la stringa è immutabile;
- creare una nuova stringa modificata senza assegnamento a `testo[i]`;
- scegliere `for` diretto o indice e motivarlo.

Step complessi, `[::-1]`, raw/triple strings e dettagli Unicode non sono prerequisiti del gate.

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

Evitare affermazioni assolute scorrette, senza aprire Unicode avanzato.

## M7 — `[::-1]` è “il modo Python” e basta

È una forma compatta da capire dopo il modello di slicing, non un sostituto del ragionamento.

---

# Differenziazione

## Recupero

- stringhe di 3–5 caratteri;
- indice scritto sotto ogni carattere;
- slice senza step;
- una sola operazione alla volta;
- trace su carta.

## Enrichment

- più indici negativi;
- step;
- inversione con slicing;
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

> come scelgo l'operazione giusta per cercare, normalizzare o trasformare il testo?

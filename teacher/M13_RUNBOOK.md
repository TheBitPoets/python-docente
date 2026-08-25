# M13 — Runbook docente

## Modulo

**Funzioni produttive: parametri, argomenti e `return`**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo docente

M05 ha già mostrato una piccola funzione come preview. M13 **non riparte da zero**: formalizza il modello.

```text
M05
→ ho visto che posso dare un nome a un calcolo

M13
→ capisco definizione/chiamata
→ parametro/argomento
→ return
→ valore usato dal chiamante
→ casi di test
```

Il punto centrale è la differenza `return`/`print` e il fatto che la funzione sia un'unità di ragionamento e verifica.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. distinguere definizione e chiamata;
2. distinguere parametro e argomento;
3. usare uno o più parametri semplici;
4. restituire un valore con `return`;
5. usare quel valore in un assegnamento o altra espressione;
6. distinguere funzione di calcolo e funzione che produce output;
7. fare un call trace semplice;
8. verificare la stessa funzione con più casi.

## GUIDED EXPOSURE

- `None` quando una funzione termina senza `return` esplicito;
- predicate semplice che restituisce `bool`.

## ENRICHMENT / BACKUP

- return multiplo / tuple-unpacking come preview;
- più `return` in rami diversi se la classe è pronta;
- chiamate più articolate.

Niente Git in M13: il consumer G1 inizia in **M14**, quando c'è un refactoring significativo da osservare con `status/diff`.

---

# Ritmo consigliato — settimana 13

## Ora teoria attiva 1 — retrieval, definizione, chiamata, parametri

### 0–10 min — retrieval M05

Riprendere una funzione già vista:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Non rispiegarla subito. Chiedere:

- dov'è la definizione?;
- quando viene realmente eseguito il corpo?;
- che dati entrano?;
- dove va il risultato?.

La settimana parte da ciò che gli studenti ricordano, non da una nuova esposizione frontale.

### 10–25 min — definizione vs chiamata

Usare `doppio` e fare call trace.

### 25–40 min — parametro vs argomento

Usare chiamate con valori diversi e una tabella:

```text
chiamata | parametro locale | return
```

### 40–55 min — più parametri

Problema con costo/prezzo o area. Fare variare gli argomenti mantenendo la stessa funzione.

### Exit micro-check

Tre frammenti: identificare definizione, chiamata, parametro e argomento.

---

# Ora teoria attiva 2 — `return` e uso del risultato

## 0–22 min — confronto obbligatorio

```python
def somma(a, b):
    print(a + b)
```

vs

```python
def somma(a, b):
    return a + b
```

Chiedere quale versione può alimentare:

```python
x = somma(2, 3)
print(x * 10)
```

## 22–38 min — separazione calcolo/output

Far trasformare una funzione che stampa in una funzione che restituisce e aggiornare il chiamante.

## 38–50 min — call trace con due chiamate

Usare variabili intermedie, non una lunga espressione annidata.

## 50–60 min — guided exposure

Se il core è stabile:

- mostrare una funzione senza `return` e il valore `None`;
- oppure mostrare un predicate semplice.

Non è necessario fare entrambi se il tempo serve al consolidamento di `return`/`print`.

---

# Ora laboratorio

## Fase A — call trace, 10 min

2–3 funzioni semplici, una chiamata alla volta.

## Fase B — controlled change, 10–15 min

Trasformare una funzione che stampa in una funzione che restituisce.

## Fase C — implementazione, 15 min

Funzione numerica con tre casi dichiarati prima del codice.

Il predicate può essere variante successiva, non requisito per tutti nel primo esercizio.

## Fase D — Debug Clinic, 10 min

- `return` mancante;
- risultato ignorato;
- parametro con nome errato;
- codice irraggiungibile.

## Fase E — spiegazione, 5 min

> Dove va esattamente il valore prodotto da `return`?

---

# Minimum mastery gate — prima di M14

Considerare M13 consolidato quando lo studente riesce a:

- riconoscere definizione e chiamata;
- distinguere parametro/argomento;
- completare una funzione con `return` corretto;
- usare il valore restituito fuori dalla funzione;
- trasformare `print`→`return` quando la responsabilità è calcolare;
- seguire un call trace semplice;
- proporre almeno tre casi per una funzione.

`None`, predicate e tuple-unpacking non sono prerequisiti per passare a M14.

---

# Misconception watchlist

## M1 — funzione = blocco che stampa

Correzione: assegnamento del valore restituito e uso in un'altra espressione.

## M2 — parametro e argomento sono sinonimi

Usare definizione/chiamata affiancate.

## M3 — basta calcolare il valore dentro la funzione

Se non viene restituito, il chiamante non riceve quel risultato.

## M4 — `return` stampa il valore

Mostrare chiamata senza `print`: nello script il valore può essere prodotto senza essere visualizzato.

## M5 — ogni funzione deve avere molti parametri

No. I parametri rappresentano i dati necessari alla responsabilità.

## M6 — `None` è un errore

No. È un valore; in M13 è guided exposure, utile soprattutto per capire un `return` dimenticato.

## M7 — M13 è la stessa lezione di M05

M05 era preview dentro i primi calcoli; M13 rende esplicito il contratto della chiamata e prepara composizione/testing.

---

# Differenziazione

## Recupero

- una funzione con un parametro;
- call trace completo;
- niente chiamate annidate iniziali;
- `return` singolo e diretto;
- confronto visuale `print`/`return`.

## Enrichment

- predicate;
- due funzioni concatenate tramite variabile intermedia;
- più rami `return` solo se leggibili;
- tuple/unpacking preview soltanto se non distrae.

---

# Evidence docente

Raccogliere almeno:

- call trace;
- trasformazione `print`→`return`;
- funzione con 3 casi;
- spiegazione parametro/argomento;
- spiegazione di dove va il valore restituito.

`None` non deve essere una domanda discriminante della verifica ordinaria se è stato solo mostrato come exposure.

---

# P2 TheBitLab

M13 crea il primo bisogno pedagogico reale del profilo `python-function-v1` tracciato in `2cornot2c#756`.

Questa è una **delivery concern docente/piattaforma**, non un concetto da insegnare agli studenti.

Fino alla certificazione:

- usare chiamate/assert/manual evidence nel workspace;
- non fingere P2 tramite parsing del sorgente;
- non trasformare ogni funzione in programma stdin/stdout soltanto per autogradare.

---

# Git G1 — non ancora

Nessun comando Git viene introdotto come outcome in M13.

Il consumer G1 comincia in M14:

```text
refactoring / rimozione dipendenza nascosta
→ git status
→ git diff
```

Questo mantiene allineato `config/git-g1-consumer.json` e impedisce di sovraccaricare la prima settimana di formalizzazione delle funzioni.

---

# Cosa NON anticipare

- LEGB;
- global/nonlocal;
- recursion;
- lambda;
- decorators;
- `*args`/`**kwargs`;
- type hints formali;
- pytest;
- funzioni come oggetti.

---

# Handoff a M14

M13 risponde:

> come entra un dato in una funzione e come torna fuori il risultato?

M14 risponde:

> dove vivono i nomi locali e come faccio collaborare più funzioni senza dipendenze nascoste?

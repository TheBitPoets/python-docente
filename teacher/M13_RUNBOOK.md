# M13 — Runbook docente

## Modulo

**Funzioni produttive: parametri, argomenti e `return`**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo docente

Portare gli studenti dal modello:

```text
programma = sequenza crescente di righe
```

al modello:

```text
problema
→ responsabilità nominata
→ parametri
→ calcolo
→ return
→ valore usato dal chiamante
```

Il punto centrale è la differenza `return`/`print` e il fatto che la funzione è un'unità di ragionamento/test.

---

# Ritmo consigliato — settimana 13

## Ora teoria attiva 1 — definizione, chiamata, parametri

### 0–10 min — richiamo M05

Riprendere una piccola funzione già vista come preview.

Domanda:

> Che differenza c'è tra descrivere una trasformazione e usarla con un valore concreto?

### 10–25 min — definizione vs chiamata

Usare `doppio` e fare call trace.

### 25–40 min — parametro vs argomento

Usare chiamate con valori diversi e far compilare una tabella:

```text
chiamata | parametro locale | return
```

### 40–55 min — più parametri

Usare un problema con costo/prezzo o area.

### Exit micro-check

Tre frammenti: identificare definizione, chiamata, parametro e argomento.

---

# Ora teoria attiva 2 — `return`, `print`, predicate

## 0–20 min — confronto obbligatorio

```python
def somma(a, b):
    print(a + b)
```

vs

```python
def somma(a, b):
    return a + b
```

Chiedere quale versione può essere usata in:

```python
x = somma(2, 3) * 10
```

## 20–35 min — separazione logica/output

Far spostare `print` fuori dalla funzione di calcolo.

## 35–45 min — predicate

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

Collegare direttamente M07/M08 alla funzione nominata.

## 45–55 min — `None` e codice dopo `return`

Solo livello beginner: funzione senza return esplicito → `None`; `return` termina la chiamata.

---

# Ora laboratorio

## Fase A — call trace, 10 min

2–3 funzioni molto semplici con chiamate concatenate tramite variabili intermedie.

## Fase B — controlled change, 10–15 min

Trasformare una funzione che stampa in una funzione che restituisce.

## Fase C — implementazione, 15 min

Funzione numerica o predicate con tre casi dichiarati prima del codice.

## Fase D — Debug Clinic, 10 min

- `return` mancante;
- risultato ignorato;
- parametro con nome errato;
- codice irraggiungibile.

## Fase E — spiegazione, 5 min

Chiedere:

> dove va esattamente il valore prodotto da `return`?

---

# Misconception watchlist

## M1 — funzione = blocco che stampa

Correzione: assegnamento del valore restituito e uso in un'altra espressione.

## M2 — parametro e argomento sono sinonimi

Usare definizione/chiamata affiancate.

## M3 — basta calcolare il valore dentro la funzione

Se non viene restituito, il chiamante non riceve quel risultato.

## M4 — `return` stampa il valore

Mostrare chiamata senza `print`: il valore viene prodotto ma uno script non lo mostra automaticamente.

## M5 — ogni funzione deve avere molti parametri

No. I parametri rappresentano i dati necessari alla responsabilità.

## M6 — `None` è un errore

No. È un valore; qui segnala spesso che la funzione non ha restituito esplicitamente un risultato utile al calcolo.

---

# Differenziazione

## Recupero

- una funzione pura con un parametro;
- call trace completo;
- niente chiamate annidate iniziali;
- `return` singolo e diretto;
- confronto visuale `print`/`return`.

## Enrichment

- predicate;
- due funzioni semplici concatenate tramite variabile intermedia;
- discutere una funzione con più rami `return` solo se leggibile;
- preview tuple/unpacking soltanto se non distrae.

---

# Evidence docente

Raccogliere almeno:

- call trace;
- trasformazione `print`→`return`;
- funzione con 3 casi;
- spiegazione parametro/argomento;
- spiegazione di `None` in un caso semplice.

---

# P2 TheBitLab

M13 crea il primo bisogno pedagogico reale del profilo `python-function-v1` tracciato in `2cornot2c#756`.

Fino alla certificazione:

- usare chiamate/assert/manual evidence nel workspace;
- non fingere P2 tramite parsing del sorgente;
- non trasformare ogni funzione in programma stdin/stdout soltanto per autogradare.

---

# Git G1

In questa settimana può iniziare soltanto il gesto leggero:

```text
git status
git diff
```

come osservazione delle modifiche al codice, se il workflow managed TheBitLab è disponibile.

Non trasformare M13 in una lezione Git: il curriculum Git resta separato.

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

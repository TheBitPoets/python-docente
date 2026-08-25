# M14 — Scope locale, passaggio dei dati e composizione

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-05 — Funzioni, decomposizione e testing  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- capire che parametri e variabili definite dentro una funzione sono locali a quella chiamata;
- distinguere un nome locale da un nome definito fuori dalla funzione;
- passare esplicitamente alla funzione i dati di cui ha bisogno;
- evitare variabili globali come scorciatoia per i dati di lavoro;
- usare il risultato di una funzione come input di un'altra;
- far collaborare più funzioni tramite valori espliciti;
- leggere un piccolo call graph;
- seguire il flusso dei dati tra chiamate;
- riconoscere una dipendenza nascosta da stato globale;
- usare variabili intermedie quando rendono più chiaro il flusso.

---

# 1. Una chiamata crea il proprio contesto locale

```python
def doppio(numero):
    risultato = numero * 2
    return risultato
```

Dentro la funzione esistono i nomi:

```text
numero
risultato
```

Questi nomi servono alla chiamata della funzione.

Modello beginner:

```text
chiamata
→ parametri locali
→ variabili locali
→ return
→ fine della chiamata
```

Non serve ancora studiare formalmente la regola LEGB.

---

# 2. Variabile locale fuori dalla funzione

```python
def doppio(numero):
    risultato = numero * 2
    return risultato

print(risultato)
```

La variabile `risultato` è stata definita dentro la funzione.

Il codice esterno non può usarla come se fosse un proprio nome locale/globale già disponibile.

La funzione comunica verso l'esterno attraverso `return`.

---

# 3. Passare esplicitamente ciò che serve

Se una funzione deve usare un prezzo e una quantità:

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

Il contratto è visibile nella firma.

Chi legge sa quali dati servono.

---

# 4. Dipendenza globale nascosta

Confronta:

```python
prezzo = 10

def costo(quantita):
    return prezzo * quantita
```

con:

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

La prima funzione dipende da un dato esterno che non compare nella firma.

La seconda rende la dipendenza esplicita.

Questo la rende più semplice da:

- capire;
- provare con valori diversi;
- testare;
- riusare.

---

# 5. Non è un dogma contro ogni nome globale

Una costante di configurazione/dominio può avere senso:

```python
IVA_PERCENTUALE = 22
```

ma i dati di lavoro che cambiano da chiamata a chiamata sono spesso meglio passati esplicitamente.

La domanda è:

> questa dipendenza è parte chiara del contratto o è nascosta?

---

# 6. Comporre funzioni

```python
def area_rettangolo(base, altezza):
    return base * altezza


def costo_pittura(area, costo_mq):
    return area * costo_mq
```

Uso:

```python
area = area_rettangolo(3, 4)
costo = costo_pittura(area, 8)
print(costo)
```

Il risultato della prima funzione diventa dato della seconda.

---

# 7. Variabili intermedie rendono visibile il flusso

Possiamo scrivere:

```python
costo = costo_pittura(area_rettangolo(3, 4), 8)
```

ma per un beginner spesso è più leggibile:

```python
area = area_rettangolo(3, 4)
costo = costo_pittura(area, 8)
```

La forma più corta non è automaticamente la migliore.

---

# 8. Call graph introduttivo

Per:

```text
main
├─ area_rettangolo
└─ costo_pittura
```

oppure:

```text
main
→ area_rettangolo
→ costo_pittura
```

possiamo rappresentare quali funzioni chiamano quali altre.

Non serve ancora un tool speciale: basta uno schema leggibile.

---

# 9. Flusso dei dati

Esempio:

```text
base, altezza
      ↓
area_rettangolo
      ↓
area
      ↓
costo_pittura + costo_mq
      ↓
costo
```

Questa vista prepara il design top-down di M15.

---

# 10. Due chiamate, due contesti locali

```python
def doppio(numero):
    risultato = numero * 2
    return risultato

x = doppio(3)
y = doppio(10)
```

Le due chiamate usano valori diversi per `numero` e `risultato`.

Non esiste un unico `numero` locale condiviso tra tutte le chiamate.

---

# 11. Worked example: prezzo finale

```python
def applica_sconto(prezzo, percentuale):
    sconto = prezzo * percentuale / 100
    return prezzo - sconto


def aggiungi_spedizione(prezzo, spedizione):
    return prezzo + spedizione
```

Uso:

```python
scontato = applica_sconto(100, 20)
finale = aggiungi_spedizione(scontato, 5)
print(finale)
```

Ogni funzione ha una responsabilità e riceve i dati necessari.

---

# 12. Error Clinic

## A — locale usata fuori

```python
def f(x):
    y = x + 1
    return y

print(y)
```

## B — dato globale nascosto

La funzione usa una variabile esterna modificabile invece di riceverla.

## C — risultato ignorato

```python
applica_sconto(100, 20)
print(100)
```

Il valore restituito non viene usato.

## D — parametro mancante

La funzione richiede due dati ma il chiamante ne passa uno.

## E — composizione troppo compressa

Una lunga espressione annidata rende difficile seguire il flusso. Introdurre variabili intermedie può migliorare la leggibilità.

---

# 13. Activity candidate

## A — Scope trace

Segna per ogni nome dove nasce e dove può essere usato.

## B — Remove global

Trasforma una funzione dipendente da stato globale in una funzione con parametri/return espliciti.

## C — Compose

Costruisci 2–3 funzioni che collaborano su un piccolo calcolo.

## D — Debug

Correggi locale usata fuori, globale nascosta, parametro mancante o return ignorato.

Nessuna Activity P2 viene materializzata finché il profilo `2cornot2c#756` non è certificato.

---

# 14. Git G1: osservare il cambiamento

Da questa fase del corso Git può iniziare a entrare come workflow trasversale:

```text
git status
→ quali file sono cambiati?

git diff
→ quali righe ho cambiato e perché?
```

Il focus non è ancora il corso Git completo.

Usiamo Git per osservare un refactoring o una rimozione di dipendenza globale.

---

# 15. Checkpoint

Sai spiegare:

1. che cosa significa variabile locale;
2. perché una funzione dovrebbe ricevere esplicitamente i dati che usa;
3. perché una globale può nascondere una dipendenza;
4. come il `return` di una funzione alimenta un'altra;
5. perché una variabile intermedia può migliorare la leggibilità;
6. che cosa rappresenta un piccolo call graph.

---

# 16. Sintesi

```text
funzione
→ riceve dati espliciti
→ usa nomi locali
→ produce un risultato
```

```text
return di A
→ input di B
```

```text
dipendenze esplicite
→ codice più comprensibile e testabile
```

Nel prossimo modulo useremo queste idee per progettare un programma dall'alto verso il basso, prima di implementarne tutti i dettagli.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — funzioni e naming/scope di base;
- *Think Python / Pensare in Python* — funzioni e composizione;
- *Learning Python / Imparare Python* — scope e funzioni come reference;
- TheBitLab `2cornot2c#756` — futuro grading function-behavior.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

# M15 — Progettazione top-down e responsabilità

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-05 — Funzioni, decomposizione e testing  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- partire da una specifica e individuare sotto-problemi;
- dare un nome alle responsabilità prima di scrivere i corpi delle funzioni;
- distinguere acquisizione dati, logica e presentazione;
- proporre firme di funzioni con parametri e `return` coerenti;
- descrivere input/output attesi di una funzione;
- formulare pre-condizioni e post-condizioni semplici in linguaggio naturale;
- riconoscere una funzione che fa troppe cose non correlate;
- estrarre una responsabilità comune quando c'è duplicazione significativa;
- costruire un piccolo call graph;
- implementare e verificare una funzione alla volta.

---

# 1. Prima il progetto, poi i dettagli

Quando il programma cresce, iniziare subito a scrivere righe può produrre un unico blocco difficile da controllare.

Processo top-down:

```text
problema complessivo
→ responsabilità
→ funzioni candidate
→ input/output di ciascuna
→ relazioni tra funzioni
→ test
→ implementazione progressiva
```

Non significa progettare tutto perfettamente prima di provare.

Significa avere una mappa prima di perdere il controllo dei dettagli.

---

# 2. Esempio: calcolatore di spedizione

Specifica semplificata:

> Leggi prezzo, quantità e distanza. Calcola il subtotale, applica uno sconto se previsto, calcola la spedizione e stampa il totale finale.

Possibili responsabilità:

```text
calcola_subtotale
calcola_sconto
calcola_spedizione
calcola_totale
```

Lettura e stampa possono restare nel flusso principale.

---

# 3. Scrivere prima le firme

Prima dei corpi:

```python
def calcola_subtotale(prezzo, quantita):
    ...


def calcola_sconto(subtotale):
    ...


def calcola_spedizione(distanza):
    ...
```

Questo costringe a chiedersi:

- quali dati servono?;
- quale risultato produce la funzione?;
- quale funzione dipende da quale altra?.

---

# 4. Responsabilità singola, senza slogan rigidi

Una buona funzione dovrebbe avere una responsabilità che possiamo nominare chiaramente.

Domanda utile:

> Per descriverla devo dire “fa questo **e poi anche** quest'altra cosa non collegata”?

Se sì, forse contiene più responsabilità.

Non useremo regole meccaniche come:

```text
massimo 10 righe
```

La dimensione non sostituisce il ragionamento sul significato.

---

# 5. Separare input, logica e output

Pattern target beginner:

```python
def calcola_sconto(prezzo, percentuale):
    return prezzo * percentuale / 100


def main():
    prezzo = float(input())
    percentuale = float(input())
    sconto = calcola_sconto(prezzo, percentuale)
    print(sconto)

main()
```

La funzione di logica può essere verificata senza dover simulare tutta l'interfaccia.

`main()` qui è soltanto un modo per organizzare il flusso. Il guard `if __name__ == "__main__"` non è ancora obbligatorio.

---

# 6. Contratto intuitivo

Per una funzione possiamo scrivere:

```text
nome: calcola_sconto
input: prezzo >= 0, percentuale tra 0 e 100
output: importo sconto >= 0
side effect: nessuno
non stampa
```

Non stiamo ancora introducendo design by contract formale.

Stiamo rendendo esplicite le aspettative.

---

# 7. Pre-condizione

Una pre-condizione descrive ciò che deve essere vero prima di usare correttamente la funzione.

Esempio:

```text
percentuale deve essere tra 0 e 100
```

La funzione può:

- assumere che il chiamante rispetti il contratto in un esercizio controllato;
- oppure validare se la specifica richiede quella responsabilità.

La scelta deve essere esplicita.

---

# 8. Post-condizione

Descrive ciò che deve essere vero sul risultato se la funzione termina correttamente.

Esempio:

```text
calcola_sconto restituisce un valore tra 0 e prezzo
```

Queste frasi aiutano a progettare i test.

---

# 9. Call graph

Per il programma di esempio:

```text
main
├─ calcola_subtotale
├─ calcola_sconto
├─ calcola_spedizione
└─ calcola_totale
```

Un call graph non mostra tutti i dettagli.

Mostra la struttura delle collaborazioni.

---

# 10. Implementare una funzione alla volta

Strategia:

```text
1. scegli funzione piccola
2. scrivi casi di test
3. implementa
4. verifica
5. passa alla successiva
6. integra
```

Questo riduce il numero di cose sconosciute contemporaneamente.

---

# 11. Duplicazione significativa

Se lo stesso calcolo coerente compare in più punti:

```python
sconto = prezzo * percentuale / 100
```

può avere senso estrarlo:

```python
def calcola_sconto(prezzo, percentuale):
    return prezzo * percentuale / 100
```

Non estraiamo una funzione per ogni singola riga solo per aumentare il numero di funzioni.

Il nome deve rappresentare un concetto utile.

---

# 12. Smell: funzione che fa tutto

```python
def gestisci_ordine():
    # legge input
    # valida
    # calcola
    # stampa
    # ripete
    # decide sconti
    ...
```

Non è automaticamente sbagliata perché lunga.

Ma è difficile:

- testare una sola responsabilità;
- riusare un calcolo;
- capire dove correggere un bug.

Questo è il momento di cercare sotto-problemi.

---

# 13. Worked example top-down

Problema:

> Calcola il costo finale di una prenotazione con prezzo base, numero persone e sconto percentuale.

Piano:

```text
calcola_subtotale(prezzo, persone) → subtotale
calcola_sconto(subtotale, percentuale) → sconto
calcola_finale(subtotale, sconto) → finale
```

Prima dei corpi, casi di test:

```text
100, 2, 10% → subtotale 200, sconto 20, finale 180
50, 1, 0%   → finale 50
```

---

# 14. Error Clinic

## A — funzione fa input e calcolo

Una funzione che dovrebbe calcolare il totale legge direttamente `input()`.

Domanda: possiamo testarla con dati scelti senza simulare input?

## B — funzione stampa e restituisce lo stesso risultato senza motivo

Qual è davvero il suo contratto?

## C — dipendenza globale

La funzione usa un valore esterno invece di riceverlo.

## D — duplicazione

Lo stesso calcolo appare in tre rami con piccole varianti.

## E — funzione troppo generica

Nome come:

```text
fai_tutto
processa
gestisci
```

senza responsabilità comprensibile.

---

# 15. Activity candidate

## A — Decomposition cards

Dato un problema, raggruppa azioni in responsabilità candidate.

## B — Extract function

Estrai un calcolo coerente da un programma monolitico.

## C — Top-down design

Consegna prima:

- funzioni;
- parametri;
- return;
- call graph;
- casi di test.

Solo dopo implementa.

## D — Smell/debug

Riconosci dipendenze globali, duplicazioni e funzioni con responsabilità troppo ampia.

---

# 16. Git G1: `diff` come strumento di refactoring

Dopo un refactoring:

```text
git diff
```

può aiutarci a rispondere:

- quali righe ho spostato?;
- quali responsabilità ho estratto?;
- ho cambiato anche il comportamento senza volerlo?.

Git resta curriculum separato, ma qui diventa parte naturale del workflow.

---

# 17. Checkpoint

Sai:

1. individuare 2–4 responsabilità in un problema;
2. proporre firme prima dei corpi;
3. separare I/O e logica;
4. scrivere un contratto intuitivo;
5. distinguere pre/post-condizione;
6. disegnare un piccolo call graph;
7. spiegare perché una funzione ha una responsabilità coerente.

---

# 18. Sintesi

```text
specifica
→ responsabilità
→ firme
→ contratti
→ test
→ implementazione
→ integrazione
```

Nel prossimo modulo useremo `assert` per rendere eseguibili molti dei casi di test e useremo i test per proteggere debugging e refactoring.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — funzioni e controllo del flusso;
- *Think Python / Pensare in Python* — decomposizione, funzioni e debugging;
- *Learning Python / Imparare Python* — reference sulle funzioni;
- principi professionali di separazione delle responsabilità adattati al livello beginner.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

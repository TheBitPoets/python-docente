---
marp: true
paginate: true
size: 16:9
title: M15 — Progettazione top-down e responsabilità
---

# M15 — Progettazione top-down e responsabilità
## Prima la mappa, poi i dettagli

PY2-05 — Funzioni, decomposizione e testing

---

# Dal problema alle responsabilità

```text
problema complessivo
→ sotto-problemi
→ funzioni candidate
→ input/output
→ test
→ implementazione
```

---

# Esempio

Ordine con:

- subtotale;
- sconto;
- spedizione;
- totale finale.

Possibili funzioni:

```text
calcola_subtotale
calcola_sconto
calcola_spedizione
calcola_totale
```

---

# Prima le firme

```python
def calcola_subtotale(prezzo, quantita):
    ...
```

Prima di scrivere il corpo chiediti:

- che dati servono?;
- che risultato produce?.

---

# Responsabilità nominabile

Domanda utile:

> per descrivere questa funzione devo dire “fa questo e poi anche...” molte volte?

Se sì, forse contiene più responsabilità.

---

# Niente regole meccaniche

Non useremo:

```text
funzione buona = massimo 10 righe
```

La lunghezza non sostituisce il significato.

---

# Separare I/O e logica

```python
def calcola_sconto(prezzo, percentuale):
    return prezzo * percentuale / 100


def main():
    prezzo = float(input())
    percentuale = float(input())
    print(calcola_sconto(prezzo, percentuale))
```

---

# Contratto intuitivo

```text
funzione: calcola_sconto
input: prezzo >= 0
       percentuale 0..100
output: importo sconto >= 0
non stampa
```

---

# Pre-condizione

Che cosa deve essere vero prima della chiamata?

```text
percentuale tra 0 e 100
```

---

# Post-condizione

Che cosa deve essere vero sul risultato?

```text
0 <= sconto <= prezzo
```

---

# Call graph

```text
main
├─ calcola_subtotale
├─ calcola_sconto
├─ calcola_spedizione
└─ calcola_totale
```

Mostra la struttura, non tutti i dettagli.

---

# Implementare una funzione alla volta

```text
scegli funzione
→ casi di test
→ implementa
→ verifica
→ integra
```

Riduci il numero di cose sconosciute contemporaneamente.

---

# Duplicazione significativa

Se un calcolo coerente compare in più punti, può diventare una funzione nominata.

Non estrarre funzioni solo per aumentare il numero di funzioni.

---

# Smell: funzione che fa tutto

```text
legge
valida
calcola
stampa
ripete
sceglie
```

Domanda:

> quali responsabilità indipendenti posso separare?

---

# Git G1 nel refactoring

```text
git diff
```

serve a vedere:

- che cosa ho estratto;
- che cosa ho rinominato;
- se ho cambiato più del previsto.

---

# Checkpoint

Sai:

- individuare responsabilità;
- proporre firme;
- separare I/O/logica;
- scrivere contratti intuitivi;
- distinguere pre/post-condizioni;
- disegnare un call graph.

---

# Recap

```text
specifica
→ responsabilità
→ firme
→ contratti
→ test
→ implementazione
```

Prossimo modulo: `assert`, regression test e refactoring protetto.

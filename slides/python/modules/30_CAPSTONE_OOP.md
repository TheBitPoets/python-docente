---
marp: true
paginate: true
size: 16:9
title: M30 — Capstone OOP
---

# M30 — Capstone OOP
## Analisi, oggetti, composizione e test

PY2-10 — Classi, oggetti e capstone

---

# Non conta il numero di righe

Un buon capstone dimostra:

```text
analisi
→ modello
→ oggetti
→ collaborazione
→ test
→ revisione
```

---

# Contratto minimo

- almeno 2 responsabilità OOP significative;
- composizione;
- invariante;
- struttura dati motivata;
- 5+ casi/test;
- edge case;
- spiegazione progettuale.

---

# Prima del codice

Per ogni classe candidata:

```text
responsabilità
stato
metodi
invariante
```

Poi disegna le relazioni.

---

# Variante generica

Esempio:

```text
Veicolo
+ MissioneConsegna
```

oppure Prodotto/Ordine, Prenotazione/Servizio, ecc.

---

# Variante Romeo

Se `romeo-sim` è certificato:

```text
Missione
└─ usa Robot
```

Stesse competenze e stessa rubrica.

Hardware non obbligatorio.

---

# Invariante obbligatoria

Esempi:

```text
stock >= 0
0 <= carico <= capacita
checkpoint completati ⊆ previsti
```

Testa almeno un confine.

---

# Composizione

```python
missione = Missione(veicolo, checkpoint)
```

Responsabilità diverse, collaborazione esplicita.

---

# OOP + collezioni

```python
self.checkpoint = list(checkpoint)
self.completati = set()
```

OOP non sostituisce le strutture dati.

---

# Separare I/O

```text
input/file
→ oggetti/metodi dominio
→ output/file
```

Mantieni il dominio testabile.

---

# Piano incrementale

```text
test/casi
→ prima classe
→ invariante
→ seconda classe
→ composizione
→ integrazione
→ edge
→ refactor
```

---

# Test minimi

- costruzione;
- osservatore;
- transizione valida;
- transizione rifiutata;
- collaborazione;
- indipendenza istanze se rilevante.

---

# Regression + refactor

```text
bug
→ test rosso
→ fix
→ verdi
→ refactor
→ ancora verdi
```

Documentane almeno uno.

---

# Git G1

Checkpoint consigliati:

```text
skeleton
core + test
fix/refactor finale
```

Prima del commit:

```text
status → diff → test → add → commit
```

---

# Spiegazione progettuale

Breve:

- classi/responsabilità;
- composizione;
- invariante;
- struttura dati scelta;
- bug/test importante;
- possibile refactor futuro.

---

# Non obbligatorio

- inheritance;
- property;
- dataclass;
- DB/GUI/web;
- async/rete;
- hardware;
- pytest professionale.

---

# Exit outcome

```text
problema
→ algoritmo
→ dati
→ funzioni
→ strutture
→ oggetti
→ invarianti
→ composizione
→ test/debug/refactor
```

Questo è il traguardo del secondo anno.

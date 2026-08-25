---
marp: true
paginate: true
size: 16:9
title: M27 — Classi, istanze, attributi e self
---

# M27 — Classi, istanze, attributi e `self`
## Quando dati + comportamento formano una responsabilità

PY2-10 — Classi, oggetti e capstone

---

# Che cosa deve restare davvero?

```text
classe vs istanza
__init__
stato per istanza
self
metodo che usa lo stato
istanze indipendenti
classe solo se aggiunge valore al modello
```

Attributi di classe condivisi e `__str__` sono guided/enrichment.

---

# Da record a oggetto

M25:

```python
{"nome": "R1", "energia": 100}
```

Nuova domanda:

> se quei dati hanno anche comportamenti e regole proprie, una classe comunica meglio il modello?

---

# Classe vs istanza

```python
class Contatore:
    ...
```

è una definizione.

```python
c1 = Contatore(...)
c2 = Contatore(...)
```

sono istanze distinte.

---

# `__init__`

```python
class Contatore:
    def __init__(self, valore_iniziale):
        self.valore = valore_iniziale
```

Serve a costruire l'istanza con il suo stato iniziale.

---

# `self`

Modello beginner:

```text
self = istanza corrente di quella chiamata
```

```python
c1.incrementa()
```

il metodo opera sullo stato di `c1`.

---

# Metodo e stato

```python
class Contatore:
    def __init__(self, valore=0):
        self.valore = valore

    def incrementa(self):
        self.valore += 1
```

Il metodo appartiene alla responsabilità dell'oggetto.

---

# Due istanze indipendenti

```python
c1 = Contatore(0)
c2 = Contatore(10)

c1.incrementa()
```

Atteso:

```text
c1.valore = 1
c2.valore = 10
```

L'indipendenza è core.

---

# `self.` dimenticato

Bug:

```python
def incrementa(self):
    valore += 1
```

`valore` locale non è automaticamente l'attributo dell'istanza.

---

# Classe o funzione?

Funzione candidata:

```text
calcola_area(base, altezza)
```

Classe candidata:

```text
Batteria con livello
+ carica/scarica
+ regole sul livello
```

> OOP non significa trasformare tutto in classi.

---

# GUIDED EXPOSURE — stato condiviso accidentale

```python
class Gruppo:
    membri = []
```

Una lista mutabile definita a livello di classe può essere condivisa tra istanze.

Usalo come Error Clinic per rafforzare:

```text
stato per istanza → inizializzato su self
```

Non è una lezione sugli attributi di classe.

---

# ENRICHMENT / BACKUP — `__str__`

Una rappresentazione leggibile può aiutare osservabilità/debug:

```python
def __str__(self):
    return f"Contatore({self.valore})"
```

Non è requisito per il mastery di M27.

---

# Error Clinic

- classe confusa con istanza;
- `self` dimenticato;
- locale confusa con attributo;
- stato condiviso accidentale;
- classe introdotta senza comportamento significativo.

---

# Minimum mastery checkpoint

Sai:

1. distinguere classe e istanza?;
2. costruire stato con `__init__`?;
3. spiegare `self`?;
4. scrivere un metodo che usa/modifica lo stato?;
5. dimostrare due istanze indipendenti?;
6. spiegare perché una classe aggiunge valore oppure perché basta una funzione?.

---

# Recap

```text
classe → definisce responsabilità
istanza → stato proprio
self → istanza corrente
metodo → comportamento sullo stato
```

Prossimo: invarianti e transizioni controllate.

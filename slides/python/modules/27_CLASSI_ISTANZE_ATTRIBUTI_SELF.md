---
marp: true
paginate: true
size: 16:9
title: M27 — Classi, istanze, attributi e self
---

# M27 — Classi, istanze, attributi e `self`

PY2-10 — Classi, oggetti e capstone

---

# Da record a oggetto

```python
studente = {"nome": "Anna", "voto": 8}
```

Quando dati e comportamenti appartengono alla stessa responsabilità, una classe può diventare un modello naturale.

---

# Classe vs istanza

```python
class Studente:
    pass
```

```python
anna = Studente()
luca = Studente()
```

Una definizione, due oggetti distinti.

---

# `__init__`

```python
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto
```

Inizializza lo stato essenziale.

---

# Attributi di istanza

```python
anna.nome
anna.voto
```

Lo stato appartiene a quella istanza.

---

# `self`

```python
def descrizione(self):
    return f"{self.nome}: {self.voto}"
```

`self` indica l'istanza concreta su cui il metodo opera.

---

# Metodi

```python
def promosso(self):
    return self.voto >= 6
```

Comportamento legato allo stato dell'oggetto.

---

# Istanze indipendenti

```python
anna = Studente("Anna", 8)
luca = Studente("Luca", 5)
```

Stessa classe, stato distinto.

---

# Non serve una classe per tutto

```python
def area(base, altezza):
    return base * altezza
```

Una funzione può essere il modello migliore.

---

# Dict vs object

```text
dict   → campi/valori
object → stato + comportamenti/responsabilità
```

La scelta dipende dal dominio.

---

# Error Clinic

- dimenticare `self.`;
- locale scambiata per attributo;
- attributo essenziale non inizializzato;
- stato mutabile condiviso accidentalmente.

---

# Romeo

```text
romeo.easy → API procedurale
Robot      → istanza con metodi/stato/backend
```

Stesso dominio, due modi di organizzare responsabilità.

---

# Checkpoint

Sai spiegare:

- classe vs istanza;
- `__init__`;
- attributi;
- `self`;
- metodi;
- istanze indipendenti;
- quando una classe serve davvero.

---

# Recap

```text
classe → tipo
istanza → oggetto
attributi → stato
metodi → comportamento
```

Prossimo: invarianti e transizioni di stato.

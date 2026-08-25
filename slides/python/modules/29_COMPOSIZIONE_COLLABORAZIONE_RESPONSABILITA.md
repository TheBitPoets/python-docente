---
marp: true
paginate: true
size: 16:9
title: M29 — Composizione, collaborazione e responsabilità
---

# M29 — Composizione, collaborazione e responsabilità

PY2-10 — Classi, oggetti e capstone

---

# Un oggetto non deve fare tutto

```text
input + file + dominio + robot + output
```

in una sola classe non è automaticamente “più OOP”.

---

# Composizione

```text
Veicolo ha un Motore
Missione ha un Robot
```

Un oggetto usa/possiede un altro oggetto.

---

# “Ha un” vs “è un”

```text
composizione → ha un
inheritance  → è un tipo di
```

Core di seconda: composizione.

---

# Chi possiede la regola?

```text
Robot → movimento/stato
Missione → checkpoint/obiettivo
```

Le regole vanno dove appartiene la responsabilità.

---

# Dipendenza esplicita

```python
class Missione:
    def __init__(self, robot, target):
        self.robot = robot
        self.target = target
```

Meglio di una variabile globale nascosta.

---

# Dominio vs I/O

```text
input/file
→ crea oggetti
→ metodi dominio
→ output/file
```

Non mettere `input()` dentro ogni metodo.

---

# Dict → object

Se un record acquista:

```text
stato + regole + comportamenti
```

può diventare una classe candidata.

---

# Refactoring incrementale

```text
record
→ classe + init
→ un metodo
→ stessi test
→ sostituzione graduale
```

Niente big-bang rewrite.

---

# God class smell

- troppi motivi per cambiare;
- I/O e dominio mescolati;
- test di una regola richiede tutto il sistema;
- metodi generici `gestisci/processa`.

---

# Collezioni di oggetti

```python
prodotti = [Prodotto(...), Prodotto(...)]
```

oppure:

```python
catalogo = {"P001": Prodotto(...)}
```

OOP si combina con le strutture dati già apprese.

---

# Romeo capstone

```text
Missione
└─ usa Robot
```

Robot non deve conoscere ogni missione possibile.

---

# Perché non inheritance core?

Prima consolidiamo:

```text
classe
→ stato/invarianti
→ composizione
```

Inheritance semplice resta enrichment.

---

# Error Clinic

- god class;
- dipendenza globale;
- regola nell'oggetto sbagliato;
- class wrapper senza comportamento;
- inheritance usata solo per riuso superficiale.

---

# Checkpoint

Sai:

- composizione;
- responsabilità;
- dipendenze esplicite;
- dominio vs I/O;
- refactor dict→object;
- collezioni di oggetti.

---

# Recap

```text
responsabilità chiare
+ collaborazione esplicita
→ sistema testabile
```

Prossimo: capstone OOP.

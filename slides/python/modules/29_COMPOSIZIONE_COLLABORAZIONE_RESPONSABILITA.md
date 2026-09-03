---
marp: true
paginate: true
size: 16:9
title: M29 — Composizione, collaborazione e responsabilità
---

# M29 — Composizione e collaborazione
## Più oggetti, responsabilità più chiare

PY2-10 — Classi, oggetti e capstone

---

# Che cosa deve restare davvero?

```text
composizione = ha/usa un
responsabilità nell'oggetto giusto
dipendenza esplicita
dominio separato da I/O
god class smell
collaborazione testabile
più classi ≠ design migliore
```

La composizione è core. L'ereditarietà non lo è.

---

# Da un oggetto a una collaborazione

M28:

```text
un oggetto
→ stato valido
→ transizioni controllate
```

M29:

```text
più responsabilità
→ più oggetti
→ collaborazione esplicita
```

---

# Composizione

Esempio:

```text
Missione
└─ usa Robot
```

La `Missione` non deve diventare un secondo robot.

Ogni oggetto conserva la propria responsabilità.

---

# Dipendenza esplicita

```python
class Missione:
    def __init__(self, robot):
        self.robot = robot
```

Il collaboratore entra nel contratto dell'oggetto.

Meglio di una dipendenza globale nascosta.

---

# Chi possiede la regola?

Domanda fondamentale:

> quale oggetto possiede i dati e la responsabilità necessari per decidere questa regola?

Non mettere tutto nel “coordinatore” per comodità.

---

# God class smell

```text
legge input
scrive file
muove robot
calcola regole
stampa report
gestisce ogni stato
```

Una classe che fa tutto diventa difficile da:

- testare;
- capire;
- modificare;
- riusare.

---

# Dominio vs I/O

```text
input / file / UI
       ↓
funzioni/adattatori
       ↓
oggetti dominio
```

Il dominio non deve dipendere inutilmente da `input()`/`print()`/file.

---

# Refactoring incrementale

Da:

```python
robot = {"energia": 100, "posizione": 0}
```

verso una classe solo quando esistono comportamento/regole proprie.

Non trasformare ogni dict in classe automaticamente.

---

# Test della collaborazione

Se `Missione` usa `Robot`, il test deve osservare la collaborazione reale:

```text
azione missione
→ metodo sul collaboratore
→ stato/risultato atteso
```

Non basta testare le classi isolate se l'outcome è la composizione.

---

# GUIDED EXPOSURE — list/dict di oggetti

Collezioni di oggetti possono avere senso:

```text
missione → lista di checkpoint
registro → dict id→oggetto
```

Usale solo quando il dominio lo richiede.

---

# GUIDED EXPOSURE — fake minimale

Per testare una collaborazione possiamo usare un collaboratore semplice controllato.

Il concetto utile è:

> rendere la dipendenza esplicita e osservabile.

Non studiamo mocking framework.

---

# ENRICHMENT / BACKUP — inheritance

Domanda:

```text
ha/usa un? → composizione
è davvero un tipo di? → forse inheritance
```

L'ereditarietà è confronto/enrichment, non prerequisito del secondo anno.

---

# Error Clinic

- più classi senza responsabilità;
- composizione solo nominale;
- dipendenza globale;
- regola nell'oggetto sbagliato;
- I/O dentro ogni metodo dominio;
- god class;
- inheritance scelta solo per riuso superficiale.

---

# Minimum mastery checkpoint

Sai:

1. spiegare una relazione “ha/usa un”?;
2. costruire due responsabilità che collaborano?;
3. passare il collaboratore in modo esplicito?;
4. assegnare la regola all'oggetto giusto?;
5. separare dominio e I/O?;
6. riconoscere una god class?;
7. testare una collaborazione?;
8. motivare perché la composizione porta valore?.

---

# Handoff al capstone

Da M29 deve uscire lo skeleton:

```text
responsabilità
→ classi candidate
→ composizione
→ invarianti
→ struttura dati
→ casi
```

M30/week 32 completa implementazione e review.

---

# Recap

```text
oggetti piccoli + responsabilità chiare
→ collaborazione esplicita
→ sistema testabile
```

Prossimo: capstone OOP.

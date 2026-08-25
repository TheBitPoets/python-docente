# M27 — Classi, istanze, attributi e `self`

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-10 — Classi, oggetti e capstone  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- spiegare la differenza tra classe e istanza;
- partire da un record `dict` e riconoscere quando dati + comportamenti suggeriscono un oggetto;
- definire una classe semplice;
- creare istanze;
- usare `__init__` per inizializzare lo stato;
- usare attributi di istanza;
- capire `self` come riferimento all'istanza su cui opera il metodo;
- definire un metodo semplice;
- creare due istanze indipendenti;
- distinguere stato condiviso per errore e stato dell'istanza;
- evitare di usare una classe quando una funzione o un semplice dato basta.

---

# 1. Da record a oggetto

Finora possiamo rappresentare uno studente così:

```python
studente = {
    "nome": "Anna",
    "voto": 8,
}
```

È un buon record di dati.

Se iniziano a comparire comportamenti legati a quei dati:

```text
aggiorna voto
verifica promozione
mostra stato
```

possiamo chiederci se dati e comportamenti appartengono a una stessa responsabilità.

---

# 2. Una classe descrive un tipo di oggetto

```python
class Studente:
    pass
```

La classe è una definizione.

Un'istanza è un oggetto concreto creato da quella classe.

```python
anna = Studente()
luca = Studente()
```

Sono due oggetti distinti.

---

# 3. `__init__`

```python
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto
```

Uso:

```python
anna = Studente("Anna", 8)
```

Modello:

```text
costruzione istanza
→ __init__
→ attributi iniziali
→ oggetto pronto nello stato previsto
```

---

# 4. Attributi di istanza

```python
anna.nome
anna.voto
```

Gli attributi rappresentano stato dell'istanza.

Con:

```python
luca = Studente("Luca", 6)
```

`anna.voto` e `luca.voto` sono stati indipendenti.

---

# 5. Che cos'è `self`?

```python
class Studente:
    def descrizione(self):
        return f"{self.nome}: {self.voto}"
```

Quando chiami:

```python
anna.descrizione()
```

il metodo opera su `anna`.

Modello beginner:

```text
self → l'istanza concreta su cui il metodo sta lavorando
```

---

# 6. Metodo = comportamento legato all'oggetto

```python
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def promosso(self):
        return self.voto >= 6
```

Il metodo usa lo stato dell'istanza per rispondere a una domanda del dominio.

---

# 7. Due istanze indipendenti

```python
anna = Studente("Anna", 8)
luca = Studente("Luca", 5)
```

```python
anna.promosso()  # True
luca.promosso()  # False
```

Stessa classe, stato diverso, comportamento applicato a ciascuna istanza.

---

# 8. Classe non significa “contenitore migliore”

Se serve soltanto calcolare:

```python
def area(base, altezza):
    return base * altezza
```

una classe `AreaCalculator` sarebbe probabilmente rumore.

Domanda:

> esiste un oggetto del dominio con stato e comportamenti che restano insieme nel tempo?

Se no, una funzione/dato può essere migliore.

---

# 9. Dict vs oggetto

## Dict

```python
studente["voto"]
```

## Oggetto

```python
studente.voto
studente.promosso()
```

Non è una gara di sintassi.

Il passaggio ha senso quando il dominio richiede una responsabilità che unisce dati e comportamento.

---

# 10. Stato iniziale coerente

`__init__` dovrebbe lasciare l'oggetto in uno stato utilizzabile.

Esempio:

```python
class Contatore:
    def __init__(self):
        self.valore = 0
```

Non costringere il chiamante a ricordare di creare manualmente attributi essenziali dopo l'istanza.

---

# 11. Error Clinic

## Attributo dimenticato

```python
class Studente:
    def __init__(self, nome, voto):
        nome = nome
        voto = voto
```

Manca:

```python
self.nome
self.voto
```

## `self` dimenticato

Metodo definito senza parametro dell'istanza.

## Variabile locale scambiata per attributo

```python
def aggiorna(self, voto):
    voto = voto
```

non modifica `self.voto`.

## Stato condiviso accidentale

Liste/dict mutabili messi come attributi di classe quando dovevano appartenere a ogni istanza: tema da diagnosticare, senza approfondire ancora tutti gli attributi di classe.

---

# 12. Worked example: `Contatore`

```python
class Contatore:
    def __init__(self):
        self.valore = 0

    def incrementa(self):
        self.valore += 1

    def leggi(self):
        return self.valore
```

Test manuali:

```python
a = Contatore()
b = Contatore()

a.incrementa()
a.incrementa()
b.incrementa()

assert a.leggi() == 2
assert b.leggi() == 1
```

Questo verifica l'indipendenza delle istanze.

---

# 13. Romeo: stessa idea, dominio reale

Prima abbiamo potuto usare un'API procedurale:

```text
romeo.easy.forward(...)
romeo.easy.left(...)
```

Romeo espone anche un oggetto `Robot` con metodi e stato/backend associato.

Questo permette un confronto autentico:

```text
funzioni che operano sul dominio
vs
istanza Robot che possiede responsabilità/comportamenti
```

Il dettaglio dell'API Romeo viene usato solo se `romeo-sim` è certificato nel Classroom Environment.

---

# 14. Activity candidate

- **A — Class/instance microscope:** identifica classe, istanze, attributi e metodi;
- **B — Dict→object:** refactor di un record semplice;
- **C — Implement:** classe con `__init__`, stato e 1–2 metodi;
- **D — Debug:** `self`, attributi mancanti, stato condiviso accidentale, locale vs attributo.

Nessuna Activity P3 viene materializzata finché `2cornot2c#758` non è certificato.

---

# 15. Checkpoint

Sai spiegare:

1. classe vs istanza;
2. `__init__`;
3. attributo di istanza;
4. `self`;
5. metodo;
6. due istanze indipendenti;
7. quando una classe aggiunge valore e quando no.

---

# 16. Sintesi

```text
classe → definizione di un tipo di oggetto
istanza → oggetto concreto
self → istanza corrente
attributi → stato
metodi → comportamento
```

Nel prossimo modulo useremo i metodi per **proteggere invarianti e transizioni di stato**, invece di lasciare che qualunque codice modifichi gli attributi senza regole.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 — classes;
- *Think Python / Pensare in Python* — classes/objects;
- *Learning Python / Imparare Python* — class model reference;
- `TheBitPoets/romeo@45e5f7e1...` — `romeo.easy` / `romeo.robot.Robot` come applied reference;
- TheBitLab `2cornot2c#758` — P3 object behavior.

---
marp: true
paginate: true
size: 16:9
title: M28 — Metodi, stato e invarianti
---

# M28 — Metodi, stato e invarianti
## Proteggere il significato dell'oggetto

PY2-10 — Classi, oggetti e capstone

---

# Che cosa deve restare davvero?

```text
stato
metodo che osserva / modifica
invariante
transizione valida
transizione rifiutata
stato invariato sul rifiuto
test di return/segnale + stato
```

La forma usata per segnalare il fallimento dipende dal contratto.

---

# Oggetto con stato

```python
class Batteria:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0
```

Lo stato rilevante include:

```text
capacita
livello
```

---

# Invariante

```text
0 <= livello <= capacita
```

Deve restare vero dopo ogni operazione pubblica corretta.

Un invariante è una proprietà del modello, non un `if` qualsiasi.

---

# Costruzione valida

`__init__` deve lasciare l'oggetto in uno stato che rispetta l'invariante.

```python
b = Batteria(100)
```

Atteso:

```text
livello = 0
capacita = 100
```

---

# Metodo che osserva

```python
def percentuale(self):
    return self.livello / self.capacita * 100
```

Legge lo stato senza modificarlo.

---

# Metodo che modifica

```python
def carica(self, quantita):
    ...
```

Una transizione modifica lo stato.

Prima di applicarla dobbiamo verificare che il nuovo stato sia valido.

---

# Validare prima di mutare

```python
def carica(self, quantita):
    if quantita < 0:
        return False
    if self.livello + quantita > self.capacita:
        return False

    self.livello += quantita
    return True
```

Qui `True/False` è **una policy didattica possibile**.

Il principio core è:

```text
transizione rifiutata
→ stato invariato
→ segnale coerente col contratto
```

---

# Test: non basta il return

```python
b = Batteria(10)

assert b.carica(5) is True
assert b.livello == 5
```

Testiamo anche lo stato risultante.

---

# Transizione rifiutata

```python
prima = b.livello
esito = b.carica(100)

assert esito is False
assert b.livello == prima
```

Il secondo `assert` protegge l'invariante e l'atomicità del cambiamento.

---

# I confini nascono dall'invariante

Se:

```text
0 <= livello <= capacita
```

casi naturali:

```text
0
capacita
capacita - 1
oltre capacita
quantita negativa
```

Gli invarianti aiutano a progettare test.

---

# Due istanze

```python
b1 = Batteria(10)
b2 = Batteria(10)

b1.carica(5)
```

Atteso:

```text
b1.livello = 5
b2.livello = 0
```

L'indipendenza resta un outcome core.

---

# GUIDED EXPOSURE — policy alternative

Il contratto potrebbe usare un altro segnale di fallimento in un livello futuro.

Non memorizzare:

```text
metodo OOP corretto = sempre return False
```

Memorizza invece:

```text
regola del dominio
→ transizione valida/rifiutata
→ stato coerente
```

---

# GUIDED EXPOSURE — `assert` interno

Un `assert` interno può aiutare a verificare un'invariante durante sviluppo/esercitazione.

Non sostituisce la gestione prevista degli input esterni.

---

# Error Clinic

- validazione dopo la mutazione;
- rifiuto con stato già parzialmente cambiato;
- test solo sul return;
- setter che bypassa le regole;
- due istanze che condividono stato per errore;
- `False` trattato come unica API possibile.

---

# Minimum mastery checkpoint

Sai:

1. indicare lo stato dell'oggetto?;
2. scrivere un invariante?;
3. distinguere osservazione e mutazione?;
4. validare prima di cambiare?;
5. preservare lo stato su rifiuto?;
6. testare stato e segnale?;
7. scegliere casi di confine dall'invariante?.

Property e policy avanzate non fanno parte del gate.

---

# Recap

```text
stato valido
→ metodo
→ transizione controllata
→ stato ancora valido
```

Prossimo: composizione e collaborazione tra oggetti.

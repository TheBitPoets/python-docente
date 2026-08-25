---
marp: true
paginate: true
size: 16:9
title: M28 — Metodi, stato e invarianti
---

# M28 — Metodi, stato e invarianti

PY2-10 — Classi, oggetti e capstone

---

# Stato

```python
class Conto:
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale
```

Gli attributi descrivono lo stato corrente.

---

# Osservatore vs mutazione

```python
def saldo_corrente(self):
    return self.saldo
```

```python
def deposita(self, importo):
    self.saldo += importo
```

Due responsabilità diverse.

---

# Invariante

```text
proprietà che deve restare vera negli stati validi
```

Esempio:

```text
0 <= livello <= capacita
```

---

# Costruzione valida

`__init__` deve lasciare l'oggetto in uno stato utilizzabile secondo il contratto.

---

# Transizione controllata

```text
valida → cambia stato
non valida → stato invariato + segnale di fallimento
```

Una policy semplice e testabile.

---

# Metodo del dominio

Meglio:

```python
aggiungi(quantita)
consuma(quantita)
```

che setter generici usati senza regole.

---

# Testare lo stato

```python
assert s.aggiungi(4) is True
assert s.livello == 4

assert s.aggiungi(8) is False
assert s.livello == 4
```

Il return da solo non basta.

---

# Casi limite

- zero;
- esattamente il limite;
- oltre limite;
- valore negativo;
- transizione rifiutata.

Gli invarianti suggeriscono i test.

---

# Istanze indipendenti

Modificare `a` non deve cambiare `b` se lo stato appartiene alle singole istanze.

---

# Error Clinic

- validazione dopo la mutazione;
- stato invalido lasciato dopo fallimento;
- attributo non inizializzato;
- stato mutabile condiviso;
- setter che bypassa regole;
- test senza verifica stato.

---

# Romeo

```text
Robot → stato + metodi
Missione → regole/obiettivi diversi
```

Domanda: quale regola appartiene a quale oggetto?

---

# Checkpoint

Sai spiegare:

- stato;
- osservatore/mutante;
- invariante;
- transizione;
- test dello stato;
- metodo del dominio.

---

# Recap

```text
stato valido
→ metodo
→ transizione controllata
→ nuovo stato valido
```

Prossimo: composizione e collaborazione.

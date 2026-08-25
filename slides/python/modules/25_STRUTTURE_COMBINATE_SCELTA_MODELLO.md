---
marp: true
paginate: true
size: 16:9
title: M25 — Strutture combinate e modello dati
---

# M25 — Strutture combinate e scelta del modello dati

PY2-08 — Set, dizionari e modellazione dei dati

---

# Prima le operazioni

```text
ordine
mutabilità
unicità
membership
lookup per chiave
record
relazioni uno→molti
```

Poi scegli la struttura.

---

# Mappa beginner

```text
str   → testo immutabile
list  → sequenza mutabile
tuple → raggruppamento stabile
set   → unicità/membership
dict  → chiave→valore
```

---

# Liste parallele

```python
nomi = ["Anna", "Luca"]
voti = [8, 7]
```

Il legame vive soltanto nell'indice.

Rischio: perdere sincronizzazione.

---

# Lista di tuple

```python
studenti = [
    ("Anna", 8),
    ("Luca", 7),
]
```

Record piccolo e posizionale.

---

# Lista di dict

```python
studenti = [
    {"nome": "Anna", "voto": 8},
    {"nome": "Luca", "voto": 7},
]
```

Campi nominati.

---

# Dict per identità

Se la domanda dominante è:

> dato il nome, qual è il voto?

```python
voti = {"Anna": 8, "Luca": 7}
```

Lookup diretto per chiave.

---

# Dict di liste

```text
iniziale → lista di parole
```

```python
gruppi[iniziale].append(parola)
```

Relazione uno→molti.

---

# `setdefault()` solo dopo il modello

Prima capisci:

```text
se manca → crea lista
poi append
```

Poi puoi leggere:

```python
gruppi.setdefault(k, []).append(v)
```

---

# Dict di set

```text
corso → studenti unici
```

Ogni livello deve avere una semantica chiara.

---

# Evitare annidamento gratuito

```python
{"a": {"b": [{"c": ...}]}}
```

non è professionale solo perché profondo.

Domanda: sai nominare il significato di ogni livello?

---

# Lookup intuition

```text
lista di record → scansione per trovare una chiave
 dict per chiave → lookup naturale
```

La struttura può rendere naturale l'operazione dominante.

---

# Bridge OOP

```python
{"nome": "Anna", "voto": 8}
```

è un record con campi.

Più avanti:

> dati + comportamenti/invarianti → classe candidata?

---

# Error Clinic

- liste parallele;
- set quando ordine/duplicati servono;
- dict per problema posizionale;
- tuple poco leggibile con troppi campi;
- chiave non unica;
- annidamento senza significato.

---

# Exit checkpoint

Sai scegliere e motivare:

```text
str / list / tuple / set / dict
```

in base alle operazioni del problema.

---

# Recap

```text
operazioni dominanti
→ modello dati
→ codice naturale
```

Prossimo: file testo e persistenza essenziale.

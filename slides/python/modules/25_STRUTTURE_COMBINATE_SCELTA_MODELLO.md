---
marp: true
paginate: true
size: 16:9
title: M25 — Strutture combinate e modello dati
---

# M25 — Strutture combinate e scelta del modello dati
## La struttura segue le operazioni dominanti

PY2-08 — Set, dizionari e modellazione dei dati

---

# Che cosa deve restare davvero?

```text
ordine?
mutabilità?
duplicati?
membership?
lookup per chiave?
record posizionale o campi nominati?
```

Poi scegli:

```text
str / list / tuple / set / dict
```

Non serve usare più strutture solo per sembrare “avanzati”.

---

# Mappa beginner

```text
str   → testo immutabile
list  → sequenza mutabile
tuple → raggruppamento stabile
set   → unicità/membership
dict  → chiave→valore
```

È una mappa iniziale, non una formula automatica.

---

# Liste parallele

```python
nomi = ["Anna", "Luca"]
voti = [8, 7]
```

Il legame vive soltanto nell'indice:

```text
nomi[i] ↔ voti[i]
```

Se perdono sincronizzazione, il record si rompe.

---

# Un modello possibile: lista di tuple

```python
studenti = [
    ("Anna", 8),
    ("Luca", 7),
]
```

Buona candidata quando:

- pochi campi;
- ruoli posizionali chiari;
- record stabile.

---

# Un altro modello: lista di dict

```python
studenti = [
    {"nome": "Anna", "voto": 8},
    {"nome": "Luca", "voto": 7},
]
```

Campi nominati.

Non è automaticamente migliore della tupla: dipende dal dominio.

---

# Dict per identità

Se la domanda dominante è:

> dato il nome, qual è il voto?

```python
voti = {"Anna": 8, "Luca": 7}
```

La chiave coincide con il lookup naturale.

---

# GUIDED EXPOSURE — dict di liste

Problema:

> raggruppa parole per iniziale.

Modello:

```text
iniziale → lista di parole
```

Una struttura combinata ha senso quando ogni livello ha un significato nominabile.

---

# Evitare annidamento gratuito

```python
{"a": {"b": [{"c": ...}]}}
```

non è professionale solo perché è profondo.

Domanda:

> sai spiegare che cosa rappresenta ogni contenitore?

Se no, il modello va semplificato.

---

# Lookup intuition

Con una lista di record:

```text
cerca una chiave → spesso scansione
```

Con un dict progettato sulla chiave:

```text
usa direttamente la chiave
```

Niente Big-O formale: basta riconoscere che una struttura può rendere naturale l'operazione dominante.

---

# Bridge verso OOP

```python
{"nome": "Anna", "voto": 8}
```

è un record con campi.

Più avanti chiederemo:

> quando questi dati hanno anche comportamenti e invarianti propri, una classe comunica meglio il modello?

Non anticipiamo ancora le classi.

---

# ENRICHMENT / BACKUP — `setdefault()`

Dopo aver capito:

```text
se la chiave manca → crea lista
poi aggiungi
```

puoi leggere:

```python
gruppi.setdefault(k, []).append(v)
```

Non è necessario per il mastery di M25.

---

# ENRICHMENT / BACKUP — dict di set

```text
corso → studenti unici
```

Utile quando la relazione è uno→molti **e** l'unicità conta.

È un esempio di scelta semantica, non un requisito di nesting.

---

# ENRICHMENT / BACKUP — matrice sparsa

```python
celle = {
    (0, 2): 5,
    (3, 1): 7,
}
```

Una struttura diversa può essere naturale se vogliamo memorizzare soltanto alcune coordinate.

Non è core obbligatorio.

---

# Error Clinic

- liste parallele fragili;
- set quando ordine/duplicati servono;
- dict per un problema puramente posizionale;
- tuple con troppi campi poco leggibili;
- chiave non davvero unica;
- annidamento senza significato;
- struttura scelta perché “è l'ultima studiata”.

---

# Exit checkpoint PY2-08

Sai:

1. scegliere fra list/tuple/set/dict?;
2. motivare con operazioni del dominio?;
3. usare set per unicità/membership?;
4. usare dict per lookup?;
5. costruire frequenze?;
6. riconoscere liste parallele fragili?;
7. usare una struttura combinata semplice quando serve?;
8. evitare nesting gratuito?.

`setdefault`, dict di set e matrici sparse non sono prerequisiti del gate.

---

# Recap

```text
operazioni dominanti
→ modello dati
→ codice più naturale
```

Prossimo: file testo e persistenza essenziale.

# M25 — Strutture combinate e scelta del modello dati

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-08 — Set, dizionari e modellazione dei dati  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- scegliere tra `str`, `list`, `tuple`, `set` e `dict` in base alle operazioni dominanti;
- costruire semplici strutture combinate quando il dominio lo richiede;
- usare una lista di tuple o una lista di dict come collezione di record semplici;
- usare un dict con valori lista per raggruppare elementi per chiave;
- usare strutture annidate senza creare profondità inutile;
- distinguere ordine, mutabilità, unicità, membership e lookup;
- confrontare due modelli corretti e motivare quale comunica meglio l'intenzione;
- riconoscere liste parallele fragili;
- capire intuitivamente perché un lookup per chiave può essere più naturale di una scansione ripetuta;
- preparare il passaggio record/dict → oggetto delle settimane OOP.

---

# 1. Non esiste “la struttura migliore” in assoluto

La domanda è:

> quali operazioni dominano questo problema?

Criteri:

```text
ordine
mutabilità
duplicati/unicità
membership
lookup per chiave
record/attributi
relazioni uno→molti
```

La struttura deve rendere naturali le operazioni importanti.

---

# 2. Mappa di scelta beginner

```text
sequenza testuale immutabile            → str
sequenza ordinata che cambia             → list
raggruppamento posizionale stabile        → tuple
valori unici / membership                 → set
chiave → valore / lookup                  → dict
```

Questa mappa è un punto di partenza, non una legge meccanica.

---

# 3. Liste parallele: modello fragile

```python
nomi = ["Anna", "Luca", "Marta"]
voti = [8, 7, 9]
```

Il legame è implicito:

```text
nomi[i] ↔ voti[i]
```

Se le due liste perdono sincronizzazione, il record si rompe.

---

# 4. Alternativa: lista di tuple

```python
studenti = [
    ("Anna", 8),
    ("Luca", 7),
    ("Marta", 9),
]
```

Ogni elemento raggruppa i valori del record.

Unpacking:

```python
for nome, voto in studenti:
    ...
```

È adeguato quando pochi campi hanno ruoli posizionali chiari e stabili.

---

# 5. Alternativa: lista di dict

```python
studenti = [
    {"nome": "Anna", "voto": 8},
    {"nome": "Luca", "voto": 7},
]
```

I campi sono nominati.

Vantaggio:

```text
record leggibile per nome del campo
```

Costo concettuale:

- più struttura;
- chiavi ripetute;
- accesso tramite stringhe.

Non significa che sia sempre migliore della tupla.

---

# 6. Dict indicizzato per identità

Se il requisito dominante è:

> dato il nome, trova rapidamente il voto

potremmo modellare:

```python
voti = {
    "Anna": 8,
    "Luca": 7,
    "Marta": 9,
}
```

Il problema non richiede più una scansione della lista per ogni lookup.

La chiave coincide con l'identità usata dal dominio.

---

# 7. Dict di liste: uno→molti

Problema:

> Raggruppa parole per iniziale.

```python
gruppi = {}

for parola in parole:
    iniziale = parola[0]

    if iniziale not in gruppi:
        gruppi[iniziale] = []

    gruppi[iniziale].append(parola)
```

Modello:

```text
iniziale → lista di parole
```

---

# 8. `setdefault()` come enrichment

Dopo aver compreso il pattern precedente:

```python
gruppi.setdefault(iniziale, []).append(parola)
```

può essere mostrato come forma standard compatta.

Non deve nascondere il modello:

```text
se la chiave manca → crea una lista
poi aggiungi il valore
```

---

# 9. Friedpython: inversione frequenze

Un esercizio legacy costruisce:

```text
frequenza → lista di caratteri
```

Esempio concettuale:

```python
{
    3: ["a", "e"],
    1: ["x"],
}
```

È un buon esempio M25 perché combina:

```text
dict + valori list + accumulo per chiave
```

Va riscritto, non copiato.

---

# 10. Set dentro un dict

Problema:

> Per ogni corso, conserva gli studenti iscritti senza duplicati.

```python
iscritti = {
    "python": {"Anna", "Luca"},
    "git": {"Luca", "Marta"},
}
```

Modello:

```text
corso → set di studenti unici
```

Strutture combinate hanno senso quando ogni livello ha una semantica chiara.

---

# 11. Evitare annidamento gratuito

Questo tipo di struttura:

```python
{"a": {"b": [{"c": ...}]}}
```

non è “più professionale” perché è profonda.

Domande:

- ogni livello rappresenta una relazione reale?;
- posso nominare il significato di ciascun contenitore?;
- il codice di accesso resta comprensibile?.

Se no, il modello va semplificato.

---

# 12. Lookup intuition

Con una lista di record, cercare una chiave spesso significa:

```text
scansiona finché trovi
```

Con un dict progettato sulla chiave:

```text
usa direttamente la chiave
```

Non formalizziamo Big-O, ma introduciamo il principio:

> una struttura può rendere naturale ed efficiente un'operazione dominante.

---

# 13. Ordine vs lookup

Un dict moderno preserva l'ordine di inserimento, ma la sua semantica primaria resta il mapping chiave→valore.

Se il problema richiede:

```text
prima posizione
seconda posizione
slicing
```

una sequenza resta probabilmente il modello più naturale.

Non scegliere dict soltanto perché può mantenere ordine.

---

# 14. Worked example: catalogo prodotti

Requisiti:

- lookup per codice prodotto;
- ogni prodotto ha nome/prezzo/categoria;
- i codici sono unici.

Modello candidato:

```python
catalogo = {
    "P001": {"nome": "Penna", "prezzo": 1.5, "categoria": "scrittura"},
    "Q010": {"nome": "Quaderno", "prezzo": 3.0, "categoria": "carta"},
}
```

Per il secondo anno non serve costruire un'app completa.

La domanda è:

> perché la chiave esterna `P001` è naturale per il lookup?

---

# 15. Bridge verso OOP

Una struttura come:

```python
{"nome": "Anna", "voto": 8}
```

rappresenta un record con campi nominati.

Più avanti potremo chiederci:

> quando questi dati hanno anche comportamenti/invarianti propri, ha senso introdurre una classe?

Questo è il ponte M25 → M27–M30.

Non anticipiamo ancora le classi.

---

# 16. Matrix sparse come enrichment

Dopo tuple + dict possiamo rappresentare solo celle non zero:

```python
celle = {
    (0, 2): 5,
    (3, 1): 7,
}
```

Lookup:

```python
celle.get((r, c), 0)
```

È un buon esempio di struttura scelta dalle operazioni/densità dei dati, ma non è core obbligatorio.

---

# 17. Error Clinic

- liste parallele fuori sincronizzazione;
- set usato quando duplicati/ordine erano significativi;
- dict usato quando il problema era puramente posizionale;
- tupla usata per record con molti campi poco leggibili;
- annidamento senza significato;
- chiave non davvero unica;
- default che nasconde dato obbligatorio;
- struttura scelta per “moda” invece che per operazioni.

---

# 18. Activity candidate

- **A — Data model choice:** scegli struttura e motiva;
- **B — Parallel lists refactor:** passa a record raggruppati;
- **C — Group by:** dict di liste/set;
- **D — Debug model:** correggi struttura che rende innaturale il requisito;
- **E — Mini-project:** piccolo dominio con almeno due strutture combinate e spiegazione del modello.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 19. Exit checkpoint PY2-08

Dovresti saper:

- usare set per unicità/membership;
- usare dict per lookup chiave→valore;
- gestire chiavi mancanti secondo contratto;
- costruire frequenze;
- iterare `items()`;
- scegliere str/list/tuple/set/dict;
- usare semplici strutture combinate;
- evitare liste parallele fragili;
- motivare il modello dati;
- collegare la scelta alle operazioni dominanti.

---

# 20. Sintesi

```text
operazioni dominanti
→ struttura candidata
→ codice più naturale
```

```text
sequenza → list/tuple
unicità → set
lookup → dict
```

Nel prossimo blocco useremo queste strutture con la persistenza su file testo, mantenendo il modulo file volutamente piccolo per proteggere il tempo OOP.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 sulle built-in collections;
- *Think Python / Pensare in Python* — lists/tuples/dictionaries;
- *Fluent Python* — data model/collections come controllo teacher-side;
- audit `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

# M29 — Composizione, collaborazione e responsabilità

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-10 — Classi, oggetti e capstone  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- spiegare la composizione “un oggetto usa/possiede un altro oggetto”;
- separare responsabilità tra due o più classi;
- costruire una collaborazione semplice tra oggetti;
- evitare una god class che legge input, calcola, gestisce file e dominio insieme;
- separare I/O e dominio anche in OOP;
- passare dipendenze esplicitamente quando serve;
- refactorare semplici record/dict verso oggetti quando dati+comportamenti lo giustificano;
- decidere quale oggetto dovrebbe contenere una regola;
- testare oggetti collaboranti con casi piccoli;
- preferire composizione a ereditarietà come modello core di seconda.

---

# 1. Un oggetto non deve fare tutto

Immagina una classe:

```text
Sistema
- legge input
- salva file
- controlla regole
- calcola
- stampa
- gestisce robot
- registra risultati
```

Non è “più OOP” perché contiene tutto.

Domanda:

> quali responsabilità del dominio possiamo nominare separatamente?

---

# 2. Composizione

Esempio:

```python
class Motore:
    def __init__(self):
        self.acceso = False

    def avvia(self):
        self.acceso = True


class Veicolo:
    def __init__(self, motore):
        self.motore = motore
```

`Veicolo` **ha un** `Motore`.

Questo è un rapporto di composizione/collaborazione.

---

# 3. “Ha un” vs “è un”

Composizione:

```text
Missione ha un Robot
Ordine ha una lista di RigheOrdine
Veicolo ha un Motore
```

Ereditarietà cerca invece una relazione:

```text
X è un tipo di Y
```

Nel core di seconda lavoriamo sulla composizione. L'ereditarietà semplice resta enrichment dopo che responsabilità e collaborazione sono stabili.

---

# 4. Chi possiede una regola?

Supponiamo:

```text
Robot → muoversi, fermarsi, stato del robot
Missione → checkpoint, obiettivo, regole di completamento
```

La regola:

> “la missione è completa quando tutti i checkpoint sono stati attraversati”

appartiene più naturalmente a `Missione` che a `Robot`.

---

# 5. Collaborazione esplicita

```python
class Missione:
    def __init__(self, robot, target):
        self.robot = robot
        self.target = target
        self.completata = False
```

`Missione` riceve il robot da usare.

Non lo recupera da una variabile globale nascosta.

Questo rende la dipendenza visibile.

---

# 6. Separare dominio e I/O

Dominio:

```python
class Prenotazione:
    def totale(self):
        ...
```

I/O:

```text
leggi dati utente
→ crea Prenotazione
→ chiama totale
→ stampa/salva
```

Non mettere `input()` dentro ogni metodo del dominio solo perché è possibile.

---

# 7. Da dict a oggetto: quando ha senso

Prima:

```python
prodotto = {
    "nome": "Penna",
    "prezzo": 1.5,
    "stock": 10,
}
```

Se servono comportamenti:

```text
vendi quantità
rifornisci
verifica disponibilità
proteggi stock >= 0
```

una classe `Prodotto` può diventare naturale.

---

# 8. Refactoring incrementale

Non riscrivere tutto insieme.

```text
1. scegli un record
2. definisci classe + __init__
3. trasferisci una regola/metodo
4. mantieni gli stessi test
5. sostituisci gradualmente gli accessi dict
6. riesegui
```

Il refactoring deve preservare il comportamento richiesto.

---

# 9. God class

Smell:

```python
class Applicazione:
    def tutto(self):
        ...
```

Segnali:

- troppi motivi diversi per cambiare;
- dipendenze su input/file/rete/dominio insieme;
- test di una regola richiede avviare tutto;
- nomi generici `gestisci`, `processa`, `fai_tutto`.

Non esiste una soglia magica di righe/metodi.

---

# 10. Oggetti collaboranti e test

```python
class Lampada:
    def __init__(self):
        self.accesa = False

    def accendi(self):
        self.accesa = True


class Stanza:
    def __init__(self, lampada):
        self.lampada = lampada

    def prepara(self):
        self.lampada.accendi()
```

Test:

```python
lampada = Lampada()
stanza = Stanza(lampada)
stanza.prepara()
assert lampada.accesa is True
```

La collaborazione produce un effetto osservabile.

---

# 11. Evitare dipendenze globali

Meglio:

```python
missione = Missione(robot, target)
```

che:

```python
robot_globale = ...

class Missione:
    def avvia(self):
        robot_globale...
```

La dipendenza esplicita rende il contratto più leggibile e testabile.

---

# 12. Liste di oggetti

```python
prodotti = [
    Prodotto("Penna", 1.5, 10),
    Prodotto("Quaderno", 3.0, 4),
]
```

Le collezioni non scompaiono con OOP.

Ora contengono oggetti del dominio.

Riutilizziamo:

```text
list + loop + search + functions/methods
```

---

# 13. Dict di oggetti

Se il lookup per codice domina:

```python
catalogo = {
    "P001": Prodotto(...),
    "Q010": Prodotto(...),
}
```

OOP non sostituisce set/dict/list: **si combina con le strutture dati già studiate**.

---

# 14. Romeo: `Missione` compone `Robot`

Target concettuale del capstone:

```text
Robot
→ movimento/stato/safety di base

Missione
→ obiettivo/checkpoint/regole
→ usa un Robot
```

Questo evita di trasformare `Robot` in una god class che conosce ogni missione possibile.

Se `romeo-sim` non è certificato, lo stesso pattern viene usato in un dominio generico equivalente.

---

# 15. Perché non inheritance adesso?

Potremmo creare gerarchie, ma aggiungeremmo subito domande su:

- override;
- `super()`;
- contratti tra base/subclass;
- sostituibilità.

Non servono per raggiungere il core OOP del secondo anno.

Prima consolidiamo:

```text
classe
→ stato/invarianti
→ collaborazione/composizione
```

Inheritance semplice può essere enrichment.

---

# 16. Error Clinic

- una classe fa dominio + I/O + persistenza;
- dipendenza globale nascosta;
- oggetto crea internamente una dipendenza che doveva essere passata;
- regola della missione messa nel Robot;
- lista/dict sostituiti inutilmente da classi wrapper senza comportamento;
- god class;
- inheritance usata solo per “riusare due righe”.

---

# 17. Activity candidate

- **A — Responsibility cards:** assegna regole a oggetti candidati;
- **B — Dict→objects refactor:** migrazione incrementale con stessi test;
- **C — Composition:** oggetto A usa B con dipendenza esplicita;
- **D — God-class debug:** separa I/O, dominio e dipendenze;
- **E — Capstone skeleton:** definisci classi, responsabilità, relazioni e primi test.

Nessuna Activity P3 viene materializzata finché `2cornot2c#758` non è certificato.

---

# 18. Checkpoint

Sai spiegare:

1. composizione;
2. “ha un” vs “è un”;
3. responsabilità;
4. dipendenza esplicita;
5. dominio vs I/O;
6. god class;
7. list/dict di oggetti;
8. perché composizione è core prima dell'ereditarietà.

---

# 19. Sintesi

```text
oggetti piccoli con responsabilità chiare
+ collaborazione esplicita
→ sistema comprensibile/testabile
```

```text
OOP non sostituisce list/dict/funzioni
→ li organizza quando il dominio lo richiede
```

Nel prossimo modulo costruiremo il capstone finale: analisi, modello, classi, composizione, test, refactoring e una breve spiegazione progettuale.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 — classes;
- principi di composizione/responsabilità adattati al beginner;
- *Think Python / Pensare in Python* — classes/objects;
- `TheBitPoets/romeo@45e5f7e1...` — `Robot` come dominio applicativo;
- TheBitLab `2cornot2c#758` — P3 object behavior.

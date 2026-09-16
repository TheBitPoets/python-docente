# M27 — Classi, istanze, attributi e `self`

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Una classe associa dati e comportamento; le istanze mantengono il proprio stato.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Scrivere funzioni e rappresentare record con dict; riconoscere mutabilità e alias.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare la differenza tra classe e istanza;<br>partire da un record <code>dict</code> e riconoscere quando dati + comportamenti suggeriscono un oggetto;<br>definire una classe semplice; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il passaggio dal record all&#x27;oggetto ha senso quando dati e regole devono collaborare. Riprendi <a href="26_FILE_TESTO_PATHLIB_ERRORI.md">M26 — File testo, <code>pathlib</code> ed errori esterni prevedibili</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="28_METODI_STATO_INVARIANTI.md">M28 — Metodi, stato e invarianti</a>. I metodi controllano le transizioni e preservano una regola valida dello stato dell&#x27;oggetto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Crea due Contatore, modifica il primo e verifica che il secondo conservi il proprio valore.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128279;</span> Rimando:</strong>
<a href="../../student/README.md">Indice del percorso studente</a>; <a href="#obiettivi">obiettivi della lezione</a>.
</p>

</details>
</td></tr>
</table>
<!-- COURSE-FRAME:END -->

<blockquote>
<p align="justify"><strong>Stato:</strong> draft editoriale controllato<br>
<strong>UDA:</strong> PY2-10 — Classi, oggetti e capstone<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>spiegare la differenza tra classe e istanza;</li>
  <li>partire da un record <code>dict</code> e riconoscere quando dati + comportamenti suggeriscono un oggetto;</li>
  <li>definire una classe semplice;</li>
  <li>creare istanze;</li>
  <li>usare <code>__init__</code> per inizializzare lo stato;</li>
  <li>usare attributi di istanza;</li>
  <li>capire <code>self</code> come riferimento all'istanza su cui opera il metodo;</li>
  <li>definire un metodo semplice;</li>
  <li>creare due istanze indipendenti;</li>
  <li>distinguere stato condiviso per errore e stato dell'istanza;</li>
  <li>evitare di usare una classe quando una funzione o un semplice dato basta.</li>
</ul>

---

## 1. Da record a oggetto

<p align="justify">Finora possiamo rappresentare uno studente così:</p>

```python
studente = {
    "nome": "Anna",
    "voto": 8,
}
```

<p align="justify">È un buon record di dati.</p>

<p align="justify">Se iniziano a comparire comportamenti legati a quei dati:</p>

```text
aggiorna voto
verifica promozione
mostra stato
```

<p align="justify">possiamo chiederci se dati e comportamenti appartengono a una stessa responsabilità.</p>

---

## 2. Una classe descrive un tipo di oggetto

```python
class Studente:
    pass
```

<p align="justify">La classe è una definizione.</p>

<p align="justify">Un'istanza è un oggetto concreto creato da quella classe.</p>

```python
anna = Studente()
luca = Studente()
```

<p align="justify">Sono due oggetti distinti.</p>

---

## 3. `__init__`

```python
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto
```

<p align="justify">Uso:</p>

```python
anna = Studente("Anna", 8)
```

<p align="justify">Modello:</p>

```text
costruzione istanza
→ __init__
→ attributi iniziali
→ oggetto pronto nello stato previsto
```

---

## 4. Attributi di istanza

```python
anna.nome
anna.voto
```

<p align="justify">Gli attributi rappresentano stato dell'istanza.</p>

<p align="justify">Con:</p>

```python
luca = Studente("Luca", 6)
```

<p align="justify"><code>anna.voto</code> e <code>luca.voto</code> sono stati indipendenti.</p>

---

## 5. Che cos'è `self`?

```python
class Studente:
    def descrizione(self):
        return f"{self.nome}: {self.voto}"
```

<p align="justify">Quando chiami:</p>

```python
anna.descrizione()
```

<p align="justify">il metodo opera su <code>anna</code>.</p>

<p align="justify">Modello beginner:</p>

```text
self → l'istanza concreta su cui il metodo sta lavorando
```

---

## 6. Metodo = comportamento legato all'oggetto

```python
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def promosso(self):
        return self.voto >= 6
```

<p align="justify">Il metodo usa lo stato dell'istanza per rispondere a una domanda del dominio.</p>

---

## 7. Due istanze indipendenti

```python
anna = Studente("Anna", 8)
luca = Studente("Luca", 5)
```

```python
anna.promosso()  # True
luca.promosso()  # False
```

<p align="justify">Stessa classe, stato diverso, comportamento applicato a ciascuna istanza.</p>

---

## 8. Classe non significa “contenitore migliore”

<p align="justify">Se serve soltanto calcolare:</p>

```python
def area(base, altezza):
    return base * altezza
```

<p align="justify">una classe <code>AreaCalculator</code> sarebbe probabilmente rumore.</p>

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">esiste un oggetto del dominio con stato e comportamenti che restano insieme nel tempo?</p>
</blockquote>

<p align="justify">Se no, una funzione/dato può essere migliore.</p>

---

## 9. Dict vs oggetto

## Dict

```python
studente["voto"]
```

## Oggetto

```python
studente.voto
studente.promosso()
```

<p align="justify">Non è una gara di sintassi.</p>

<p align="justify">Il passaggio ha senso quando il dominio richiede una responsabilità che unisce dati e comportamento.</p>

---

## 10. Stato iniziale coerente

<p align="justify"><code>__init__</code> dovrebbe lasciare l'oggetto in uno stato utilizzabile.</p>

<p align="justify">Esempio:</p>

```python
class Contatore:
    def __init__(self):
        self.valore = 0
```

<p align="justify">Non costringere il chiamante a ricordare di creare manualmente attributi essenziali dopo l'istanza.</p>

---

## 11. Error Clinic

## Attributo dimenticato

```python
class Studente:
    def __init__(self, nome, voto):
        nome = nome
        voto = voto
```

<p align="justify">Manca:</p>

```python
self.nome
self.voto
```

## `self` dimenticato

<p align="justify">Metodo definito senza parametro dell'istanza.</p>

## Variabile locale scambiata per attributo

```python
def aggiorna(self, voto):
    voto = voto
```

<p align="justify">non modifica <code>self.voto</code>.</p>

## Stato condiviso accidentale

<p align="justify">Liste/dict mutabili messi come attributi di classe quando dovevano appartenere a ogni istanza: tema da diagnosticare, senza approfondire ancora tutti gli attributi di classe.</p>

---

## 12. Worked example: `Contatore`

```python
class Contatore:
    def __init__(self):
        self.valore = 0

    def incrementa(self):
        self.valore += 1

    def leggi(self):
        return self.valore
```

<p align="justify">Test manuali:</p>

```python
a = Contatore()
b = Contatore()

a.incrementa()
a.incrementa()
b.incrementa()

assert a.leggi() == 2
assert b.leggi() == 1
```

<p align="justify">Questo verifica l'indipendenza delle istanze.</p>

---

## 13. Romeo: stessa idea, dominio reale

<p align="justify">Prima abbiamo potuto usare un'API procedurale:</p>

```text
romeo.easy.forward(...)
romeo.easy.left(...)
```

<p align="justify">Romeo espone anche un oggetto <code>Robot</code> con metodi e stato/backend associato.</p>

<p align="justify">Questo permette un confronto autentico:</p>

```text
funzioni che operano sul dominio
vs
istanza Robot che possiede responsabilità/comportamenti
```

<p align="justify">Il dettaglio dell'API Romeo viene usato solo se <code>romeo-sim</code> è certificato nel Classroom Environment.</p>

---

## 14. Activity candidate

<ul>
  <li><strong>A — Class/instance microscope:</strong> identifica classe, istanze, attributi e metodi;</li>
  <li><strong>B — Dict→object:</strong> refactor di un record semplice;</li>
  <li><strong>C — Implement:</strong> classe con <code>__init__</code>, stato e 1–2 metodi;</li>
  <li><strong>D — Debug:</strong> <code>self</code>, attributi mancanti, stato condiviso accidentale, locale vs attributo.</li>
</ul>

<p align="justify">Nessuna Activity P3 viene materializzata finché <code>2cornot2c#758</code> non è certificato.</p>

---

## 15. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>classe vs istanza;</li>
  <li><code>__init__</code>;</li>
  <li>attributo di istanza;</li>
  <li><code>self</code>;</li>
  <li>metodo;</li>
  <li>due istanze indipendenti;</li>
  <li>quando una classe aggiunge valore e quando no.</li>
</ol>

---

## 16. Sintesi

```text
classe → definizione di un tipo di oggetto
istanza → oggetto concreto
self → istanza corrente
attributi → stato
metodi → comportamento
```

<p align="justify">Nel prossimo modulo useremo i metodi per <strong>proteggere invarianti e transizioni di stato</strong>, invece di lasciare che qualunque codice modifichi gli attributi senza regole.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — classes;</li>
  <li><em>Think Python / Pensare in Python</em> — classes/objects;</li>
  <li><em>Learning Python / Imparare Python</em> — class model reference;</li>
  <li><code>TheBitPoets/romeo@45e5f7e1...</code> — <code>romeo.easy</code> / <code>romeo.robot.Robot</code> come applied reference;</li>
  <li>TheBitLab <code>2cornot2c#758</code> — P3 object behavior.</li>
</ul>

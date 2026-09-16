# M29 — Composizione, collaborazione e responsabilità

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
La composizione distribuisce le responsabilità fra oggetti che collaborano con dipendenze esplicite.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Gestire stato e invarianti e testare metodi da M27–M28.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare la composizione “un oggetto usa/possiede un altro oggetto”;<br>separare responsabilità tra due o più classi;<br>costruire una collaborazione semplice tra oggetti; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Separare I/O e logica resta utile anche quando le responsabilità sono espresse da classi. Riprendi <a href="28_METODI_STATO_INVARIANTI.md">M28 — Metodi, stato e invarianti</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="30_CAPSTONE_OOP.md">M30 — Capstone OOP: analisi, oggetti, composizione e test</a>. Il capstone integra specifica, strutture dati, oggetti collaboranti, invarianti e test nel prodotto finale.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Disegna due oggetti collaboranti, assegna a ciascuno una regola e scrivi un test della collaborazione.
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
  <li>spiegare la composizione “un oggetto usa/possiede un altro oggetto”;</li>
  <li>separare responsabilità tra due o più classi;</li>
  <li>costruire una collaborazione semplice tra oggetti;</li>
  <li>evitare una god class che legge input, calcola, gestisce file e dominio insieme;</li>
  <li>separare I/O e dominio anche in OOP;</li>
  <li>passare dipendenze esplicitamente quando serve;</li>
  <li>refactorare semplici record/dict verso oggetti quando dati+comportamenti lo giustificano;</li>
  <li>decidere quale oggetto dovrebbe contenere una regola;</li>
  <li>testare oggetti collaboranti con casi piccoli;</li>
  <li>preferire composizione a ereditarietà come modello core di seconda.</li>
</ul>

---

## 1. Un oggetto non deve fare tutto

<p align="justify">Immagina una classe:</p>

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

<p align="justify">Non è “più OOP” perché contiene tutto.</p>

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">quali responsabilità del dominio possiamo nominare separatamente?</p>
</blockquote>

---

## 2. Composizione

<p align="justify">Esempio:</p>

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

<p align="justify"><code>Veicolo</code> <strong>ha un</strong> <code>Motore</code>.</p>

<p align="justify">Questo è un rapporto di composizione/collaborazione.</p>

---

## 3. “Ha un” vs “è un”

<p align="justify">Composizione:</p>

```text
Missione ha un Robot
Ordine ha una lista di RigheOrdine
Veicolo ha un Motore
```

<p align="justify">Ereditarietà cerca invece una relazione:</p>

```text
X è un tipo di Y
```

<p align="justify">Nel core di seconda lavoriamo sulla composizione. L'ereditarietà semplice resta enrichment dopo che responsabilità e collaborazione sono stabili.</p>

---

## 4. Chi possiede una regola?

<p align="justify">Supponiamo:</p>

```text
Robot → muoversi, fermarsi, stato del robot
Missione → checkpoint, obiettivo, regole di completamento
```

<p align="justify">La regola:</p>

<blockquote>
<p align="justify">“la missione è completa quando tutti i checkpoint sono stati attraversati”</p>
</blockquote>

<p align="justify">appartiene più naturalmente a <code>Missione</code> che a <code>Robot</code>.</p>

---

## 5. Collaborazione esplicita

```python
class Missione:
    def __init__(self, robot, target):
        self.robot = robot
        self.target = target
        self.completata = False
```

<p align="justify"><code>Missione</code> riceve il robot da usare.</p>

<p align="justify">Non lo recupera da una variabile globale nascosta.</p>

<p align="justify">Questo rende la dipendenza visibile.</p>

---

## 6. Separare dominio e I/O

<p align="justify">Dominio:</p>

```python
class Prenotazione:
    def totale(self):
        ...
```

<p align="justify">I/O:</p>

```text
leggi dati utente
→ crea Prenotazione
→ chiama totale
→ stampa/salva
```

<p align="justify">Non mettere <code>input()</code> dentro ogni metodo del dominio solo perché è possibile.</p>

---

## 7. Da dict a oggetto: quando ha senso

<p align="justify">Prima:</p>

```python
prodotto = {
    "nome": "Penna",
    "prezzo": 1.5,
    "stock": 10,
}
```

<p align="justify">Se servono comportamenti:</p>

```text
vendi quantità
rifornisci
verifica disponibilità
proteggi stock >= 0
```

<p align="justify">una classe <code>Prodotto</code> può diventare naturale.</p>

---

## 8. Refactoring incrementale

<p align="justify">Non riscrivere tutto insieme.</p>

```text
1. scegli un record
2. definisci classe + __init__
3. trasferisci una regola/metodo
4. mantieni gli stessi test
5. sostituisci gradualmente gli accessi dict
6. riesegui
```

<p align="justify">Il refactoring deve preservare il comportamento richiesto.</p>

---

## 9. God class

<p align="justify">Smell:</p>

```python
class Applicazione:
    def tutto(self):
        ...
```

<p align="justify">Segnali:</p>

<ul>
  <li>troppi motivi diversi per cambiare;</li>
  <li>dipendenze su input/file/rete/dominio insieme;</li>
  <li>test di una regola richiede avviare tutto;</li>
  <li>nomi generici <code>gestisci</code>, <code>processa</code>, <code>fai_tutto</code>.</li>
</ul>

<p align="justify">Non esiste una soglia magica di righe/metodi.</p>

---

## 10. Oggetti collaboranti e test

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

<p align="justify">Test:</p>

```python
lampada = Lampada()
stanza = Stanza(lampada)
stanza.prepara()
assert lampada.accesa is True
```

<p align="justify">La collaborazione produce un effetto osservabile.</p>

---

## 11. Evitare dipendenze globali

<p align="justify">Meglio:</p>

```python
missione = Missione(robot, target)
```

<p align="justify">che:</p>

```python
robot_globale = ...

class Missione:
    def avvia(self):
        robot_globale...
```

<p align="justify">La dipendenza esplicita rende il contratto più leggibile e testabile.</p>

---

## 12. Liste di oggetti

```python
prodotti = [
    Prodotto("Penna", 1.5, 10),
    Prodotto("Quaderno", 3.0, 4),
]
```

<p align="justify">Le collezioni non scompaiono con OOP.</p>

<p align="justify">Ora contengono oggetti del dominio.</p>

<p align="justify">Riutilizziamo:</p>

```text
list + loop + search + functions/methods
```

---

## 13. Dict di oggetti

<p align="justify">Se il lookup per codice domina:</p>

```python
catalogo = {
    "P001": Prodotto(...),
    "Q010": Prodotto(...),
}
```

<p align="justify">OOP non sostituisce set/dict/list: <strong>si combina con le strutture dati già studiate</strong>.</p>

---

## 14. Romeo: `Missione` compone `Robot`

<p align="justify">Target concettuale del capstone:</p>

```text
Robot
→ movimento/stato/safety di base

Missione
→ obiettivo/checkpoint/regole
→ usa un Robot
```

<p align="justify">Questo evita di trasformare <code>Robot</code> in una god class che conosce ogni missione possibile.</p>

<p align="justify">Se <code>romeo-sim</code> non è certificato, lo stesso pattern viene usato in un dominio generico equivalente.</p>

---

## 15. Perché non inheritance adesso?

<p align="justify">Potremmo creare gerarchie, ma aggiungeremmo subito domande su:</p>

<ul>
  <li>override;</li>
  <li><code>super()</code>;</li>
  <li>contratti tra base/subclass;</li>
  <li>sostituibilità.</li>
</ul>

<p align="justify">Non servono per raggiungere il core OOP del secondo anno.</p>

<p align="justify">Prima consolidiamo:</p>

```text
classe
→ stato/invarianti
→ collaborazione/composizione
```

<p align="justify">Inheritance semplice può essere enrichment.</p>

---

## 16. Error Clinic

<ul>
  <li>una classe fa dominio + I/O + persistenza;</li>
  <li>dipendenza globale nascosta;</li>
  <li>oggetto crea internamente una dipendenza che doveva essere passata;</li>
  <li>regola della missione messa nel Robot;</li>
  <li>lista/dict sostituiti inutilmente da classi wrapper senza comportamento;</li>
  <li>god class;</li>
  <li>inheritance usata solo per “riusare due righe”.</li>
</ul>

---

## 17. Activity candidate

<ul>
  <li><strong>A — Responsibility cards:</strong> assegna regole a oggetti candidati;</li>
  <li><strong>B — Dict→objects refactor:</strong> migrazione incrementale con stessi test;</li>
  <li><strong>C — Composition:</strong> oggetto A usa B con dipendenza esplicita;</li>
  <li><strong>D — God-class debug:</strong> separa I/O, dominio e dipendenze;</li>
  <li><strong>E — Capstone skeleton:</strong> definisci classi, responsabilità, relazioni e primi test.</li>
</ul>

<p align="justify">Nessuna Activity P3 viene materializzata finché <code>2cornot2c#758</code> non è certificato.</p>

---

## 18. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>composizione;</li>
  <li>“ha un” vs “è un”;</li>
  <li>responsabilità;</li>
  <li>dipendenza esplicita;</li>
  <li>dominio vs I/O;</li>
  <li>god class;</li>
  <li>list/dict di oggetti;</li>
  <li>perché composizione è core prima dell'ereditarietà.</li>
</ol>

---

## 19. Sintesi

```text
oggetti piccoli con responsabilità chiare
+ collaborazione esplicita
→ sistema comprensibile/testabile
```

```text
OOP non sostituisce list/dict/funzioni
→ li organizza quando il dominio lo richiede
```

<p align="justify">Nel prossimo modulo costruiremo il capstone finale: analisi, modello, classi, composizione, test, refactoring e una breve spiegazione progettuale.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — classes;</li>
  <li>principi di composizione/responsabilità adattati al beginner;</li>
  <li><em>Think Python / Pensare in Python</em> — classes/objects;</li>
  <li><code>TheBitPoets/romeo@45e5f7e1...</code> — <code>Robot</code> come dominio applicativo;</li>
  <li>TheBitLab <code>2cornot2c#758</code> — P3 object behavior.</li>
</ul>

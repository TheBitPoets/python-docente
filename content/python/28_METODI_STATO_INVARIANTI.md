# M28 — Metodi, stato e invarianti

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
I metodi controllano le transizioni e preservano una regola valida dello stato dell&#x27;oggetto.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Definire una classe con __init__, attributi e metodi e distinguere due istanze da M27.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
descrivere lo stato corrente di un oggetto tramite i suoi attributi;<br>distinguere metodo osservatore e metodo che cambia lo stato;<br>definire una semplice invariante di dominio; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Un test di oggetto osserva lo stato prima e dopo una chiamata, oltre al suo eventuale risultato. Riprendi <a href="27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md">M27 — Classi, istanze, attributi e <code>self</code></a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md">M29 — Composizione, collaborazione e responsabilità</a>. La composizione distribuisce le responsabilità fra oggetti che collaborano con dipendenze esplicite.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Verifica stato iniziale, transizione valida e tentativo oltre il limite di ContatoreLimitato.
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
  <li>descrivere lo stato corrente di un oggetto tramite i suoi attributi;</li>
  <li>distinguere metodo osservatore e metodo che cambia lo stato;</li>
  <li>definire una semplice invariante di dominio;</li>
  <li>inizializzare un oggetto in uno stato valido;</li>
  <li>modificare lo stato attraverso metodi coerenti col dominio;</li>
  <li>impedire o segnalare transizioni non valide con una policy semplice;</li>
  <li>testare stato iniziale, transizioni valide e casi limite;</li>
  <li>verificare che due istanze restino indipendenti;</li>
  <li>riconoscere una classe che espone stato ma non protegge nessuna regola utile;</li>
  <li>evitare setter generici usati senza motivo.</li>
</ul>

---

## 1. Stato

<p align="justify">Per un conto semplice:</p>

```python
class Conto:
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale
```

<p align="justify">Lo stato osservabile include:</p>

```text
saldo
```

<p align="justify">Un metodo può leggerlo o cambiarlo.</p>

---

## 2. Metodo osservatore

```python
class Conto:
    ...

    def saldo_corrente(self):
        return self.saldo
```

<p align="justify">Non modifica lo stato.</p>

<p align="justify">Risponde a una domanda sull'oggetto.</p>

---

## 3. Metodo che cambia lo stato

```python
class Conto:
    ...

    def deposita(self, importo):
        self.saldo += importo
```

<p align="justify">Ora dobbiamo porre una domanda più importante:</p>

<blockquote>
<p align="justify">qualunque <code>importo</code> è valido?</p>
</blockquote>

---

## 4. Invariante

<p align="justify">Un'invariante è una proprietà che vogliamo mantenere vera per gli stati validi dell'oggetto.</p>

<p align="justify">Esempio semplificato:</p>

```text
saldo >= 0
```

<p align="justify">oppure per un serbatoio:</p>

```text
0 <= livello <= capacita
```

<p align="justify">Non serve formalismo matematico avanzato.</p>

<p align="justify">Serve saper dire:</p>

<blockquote>
<p align="justify">quali stati non devono esistere?</p>
</blockquote>

---

## 5. Costruzione valida

```python
class Serbatoio:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0
```

<p align="justify">Se la capacità deve essere positiva, la specifica deve dichiararlo.</p>

<p align="justify">Una classe dovrebbe evitare di creare oggetti già invalidi.</p>

---

## 6. Transizione valida

```python
class Serbatoio:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0

    def aggiungi(self, quantita):
        if quantita < 0:
            return False

        if self.livello + quantita > self.capacita:
            return False

        self.livello += quantita
        return True
```

<p align="justify">Policy beginner:</p>

```text
operazione valida → cambia stato
operazione non valida → stato invariato + risultato che segnala il fallimento
```

<p align="justify">Non è l'unica API possibile; è una scelta semplice da testare.</p>

---

## 7. Perché non modificare tutto direttamente?

<p align="justify">Se qualunque codice fa:</p>

```python
serbatoio.livello = 999999
```

<p align="justify">può violare l'invariante.</p>

<p align="justify">Nel core di seconda non imponiamo ancora property/private convention come prerequisiti.</p>

<p align="justify">Ma costruiamo il principio:</p>

<blockquote>
<p align="justify">i metodi del dominio dovrebbero essere il percorso normale per le transizioni significative.</p>
</blockquote>

---

## 8. Setter generico vs metodo del dominio

<p align="justify">Confronta:</p>

```python
def set_livello(self, valore):
    self.livello = valore
```

<p align="justify">con:</p>

```python
def aggiungi(self, quantita):
    ...

def consuma(self, quantita):
    ...
```

<p align="justify">I secondi metodi raccontano <strong>che cosa succede nel dominio</strong> e possono proteggere le regole.</p>

<p align="justify">Non creare <code>get_...</code> / <code>set_...</code> meccanicamente per ogni attributo.</p>

---

## 9. Test dello stato iniziale

```python
s = Serbatoio(10)

assert s.capacita == 10
assert s.livello == 0
```

<p align="justify">Il costruttore è parte del comportamento da verificare.</p>

---

## 10. Test delle transizioni

```python
s = Serbatoio(10)

assert s.aggiungi(4) is True
assert s.livello == 4

assert s.aggiungi(8) is False
assert s.livello == 4
```

<p align="justify">Il test non verifica soltanto il return.</p>

<p align="justify">Verifica anche lo stato dopo una transizione rifiutata.</p>

---

## 11. Casi limite

<p align="justify">Per capacità 10:</p>

```text
aggiungi 0
aggiungi 10 da vuoto
aggiungi oltre capacità
quantità negativa
consuma esattamente tutto
consuma oltre disponibile
```

<p align="justify">Gli invarianti rendono naturali i casi di test.</p>

---

## 12. Istanze indipendenti

```python
a = Serbatoio(10)
b = Serbatoio(20)

a.aggiungi(5)
```

<p align="justify">Dobbiamo avere:</p>

```text
a.livello = 5
b.livello = 0
```

<p align="justify">È un regression test importante dopo M27.</p>

---

## 13. `assert` interno: uso prudente

<p align="justify">Possiamo usare <code>assert</code> per controllare una supposizione interna durante sviluppo, ma non come normale gestione dell'input utente o di un comando non valido.</p>

<p align="justify">Nel core preferiamo che il contratto del metodo dica come segnala una transizione non ammessa.</p>

---

## 14. Error Clinic

<ul>
  <li>metodo mutante che aggiorna prima di validare e lascia stato invalido;</li>
  <li>transizione rifiutata ma stato già cambiato;</li>
  <li>attributo dimenticato in <code>__init__</code>;</li>
  <li>lista mutabile condivisa tra istanze;</li>
  <li>setter generico che bypassa tutte le regole;</li>
  <li>test che controlla solo il return ma non lo stato;</li>
  <li>stato derivato memorizzato e lasciato incoerente senza necessità.</li>
</ul>

---

## 15. Worked example: `ContatoreLimitato`

```python
class ContatoreLimitato:
    def __init__(self, massimo):
        self.massimo = massimo
        self.valore = 0

    def incrementa(self):
        if self.valore == self.massimo:
            return False

        self.valore += 1
        return True
```

<p align="justify">Invariante:</p>

```text
0 <= valore <= massimo
```

<p align="justify">Test:</p>

```python
c = ContatoreLimitato(2)
assert c.incrementa() is True
assert c.incrementa() is True
assert c.incrementa() is False
assert c.valore == 2
```

---

## 16. Romeo come applicazione

<p align="justify">Un <code>Robot</code> simulato possiede stato/backend e metodi di movimento.</p>

<p align="justify">Domande OOP utili:</p>

<ul>
  <li>quali valori di velocità/azione sono ammessi?;</li>
  <li>quali transizioni cambiano lo stato simulato?;</li>
  <li>quali controlli devono restare nel <code>Robot</code> e quali nella <code>Missione</code>?.</li>
</ul>

<p align="justify">Non aggiungere hardware o networking come prerequisito.</p>

---

## 17. Activity candidate

<ul>
  <li><strong>A — State trace:</strong> stato prima/dopo ogni metodo;</li>
  <li><strong>B — Add invariant:</strong> inserisci una regola semplice senza rompere i casi validi;</li>
  <li><strong>C — Implement:</strong> classe con stato, osservatore e 2 transizioni;</li>
  <li><strong>D — Debug:</strong> stato invalido, update-before-validation, istanze condivise.</li>
</ul>

<p align="justify">Nessuna Activity P3 viene materializzata finché <code>2cornot2c#758</code> non è certificato.</p>

---

## 18. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>stato;</li>
  <li>metodo osservatore vs mutante;</li>
  <li>invariante;</li>
  <li>transizione valida/non valida;</li>
  <li>perché testare anche lo stato;</li>
  <li>perché metodo del dominio è spesso migliore di setter generico;</li>
  <li>istanze indipendenti.</li>
</ol>

---

## 19. Sintesi

```text
oggetto valido
→ metodo
→ transizione controllata
→ nuovo stato valido
```

```text
invariante
→ guida API + test + debug
```

<p align="justify">Nel prossimo modulo più oggetti collaboreranno tramite <strong>composizione</strong>. Il problema non sarà più soltanto “come proteggo un oggetto?”, ma “chi è responsabile di che cosa?”.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — classes;</li>
  <li><em>Think Python / Pensare in Python</em> — object state;</li>
  <li>pratiche di object design/invariants adattate al beginner;</li>
  <li><code>TheBitPoets/romeo@45e5f7e1...</code> come applied domain;</li>
  <li>TheBitLab <code>2cornot2c#758</code> — P3 object behavior.</li>
</ul>

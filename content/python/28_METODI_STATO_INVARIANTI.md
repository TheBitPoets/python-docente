# M28 — Metodi, stato e invarianti

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-10 — Classi, oggetti e capstone  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- descrivere lo stato corrente di un oggetto tramite i suoi attributi;
- distinguere metodo osservatore e metodo che cambia lo stato;
- definire una semplice invariante di dominio;
- inizializzare un oggetto in uno stato valido;
- modificare lo stato attraverso metodi coerenti col dominio;
- impedire o segnalare transizioni non valide con una policy semplice;
- testare stato iniziale, transizioni valide e casi limite;
- verificare che due istanze restino indipendenti;
- riconoscere una classe che espone stato ma non protegge nessuna regola utile;
- evitare setter generici usati senza motivo.

---

# 1. Stato

Per un conto semplice:

```python
class Conto:
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale
```

Lo stato osservabile include:

```text
saldo
```

Un metodo può leggerlo o cambiarlo.

---

# 2. Metodo osservatore

```python
class Conto:
    ...

    def saldo_corrente(self):
        return self.saldo
```

Non modifica lo stato.

Risponde a una domanda sull'oggetto.

---

# 3. Metodo che cambia lo stato

```python
class Conto:
    ...

    def deposita(self, importo):
        self.saldo += importo
```

Ora dobbiamo porre una domanda più importante:

> qualunque `importo` è valido?

---

# 4. Invariante

Un'invariante è una proprietà che vogliamo mantenere vera per gli stati validi dell'oggetto.

Esempio semplificato:

```text
saldo >= 0
```

oppure per un serbatoio:

```text
0 <= livello <= capacita
```

Non serve formalismo matematico avanzato.

Serve saper dire:

> quali stati non devono esistere?

---

# 5. Costruzione valida

```python
class Serbatoio:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0
```

Se la capacità deve essere positiva, la specifica deve dichiararlo.

Una classe dovrebbe evitare di creare oggetti già invalidi.

---

# 6. Transizione valida

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

Policy beginner:

```text
operazione valida → cambia stato
operazione non valida → stato invariato + risultato che segnala il fallimento
```

Non è l'unica API possibile; è una scelta semplice da testare.

---

# 7. Perché non modificare tutto direttamente?

Se qualunque codice fa:

```python
serbatoio.livello = 999999
```

può violare l'invariante.

Nel core di seconda non imponiamo ancora property/private convention come prerequisiti.

Ma costruiamo il principio:

> i metodi del dominio dovrebbero essere il percorso normale per le transizioni significative.

---

# 8. Setter generico vs metodo del dominio

Confronta:

```python
def set_livello(self, valore):
    self.livello = valore
```

con:

```python
def aggiungi(self, quantita):
    ...

def consuma(self, quantita):
    ...
```

I secondi metodi raccontano **che cosa succede nel dominio** e possono proteggere le regole.

Non creare `get_...` / `set_...` meccanicamente per ogni attributo.

---

# 9. Test dello stato iniziale

```python
s = Serbatoio(10)

assert s.capacita == 10
assert s.livello == 0
```

Il costruttore è parte del comportamento da verificare.

---

# 10. Test delle transizioni

```python
s = Serbatoio(10)

assert s.aggiungi(4) is True
assert s.livello == 4

assert s.aggiungi(8) is False
assert s.livello == 4
```

Il test non verifica soltanto il return.

Verifica anche lo stato dopo una transizione rifiutata.

---

# 11. Casi limite

Per capacità 10:

```text
aggiungi 0
aggiungi 10 da vuoto
aggiungi oltre capacità
quantità negativa
consuma esattamente tutto
consuma oltre disponibile
```

Gli invarianti rendono naturali i casi di test.

---

# 12. Istanze indipendenti

```python
a = Serbatoio(10)
b = Serbatoio(20)

a.aggiungi(5)
```

Dobbiamo avere:

```text
a.livello = 5
b.livello = 0
```

È un regression test importante dopo M27.

---

# 13. `assert` interno: uso prudente

Possiamo usare `assert` per controllare una supposizione interna durante sviluppo, ma non come normale gestione dell'input utente o di un comando non valido.

Nel core preferiamo che il contratto del metodo dica come segnala una transizione non ammessa.

---

# 14. Error Clinic

- metodo mutante che aggiorna prima di validare e lascia stato invalido;
- transizione rifiutata ma stato già cambiato;
- attributo dimenticato in `__init__`;
- lista mutabile condivisa tra istanze;
- setter generico che bypassa tutte le regole;
- test che controlla solo il return ma non lo stato;
- stato derivato memorizzato e lasciato incoerente senza necessità.

---

# 15. Worked example: `ContatoreLimitato`

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

Invariante:

```text
0 <= valore <= massimo
```

Test:

```python
c = ContatoreLimitato(2)
assert c.incrementa() is True
assert c.incrementa() is True
assert c.incrementa() is False
assert c.valore == 2
```

---

# 16. Romeo come applicazione

Un `Robot` simulato possiede stato/backend e metodi di movimento.

Domande OOP utili:

- quali valori di velocità/azione sono ammessi?;
- quali transizioni cambiano lo stato simulato?;
- quali controlli devono restare nel `Robot` e quali nella `Missione`?.

Non aggiungere hardware o networking come prerequisito.

---

# 17. Activity candidate

- **A — State trace:** stato prima/dopo ogni metodo;
- **B — Add invariant:** inserisci una regola semplice senza rompere i casi validi;
- **C — Implement:** classe con stato, osservatore e 2 transizioni;
- **D — Debug:** stato invalido, update-before-validation, istanze condivise.

Nessuna Activity P3 viene materializzata finché `2cornot2c#758` non è certificato.

---

# 18. Checkpoint

Sai spiegare:

1. stato;
2. metodo osservatore vs mutante;
3. invariante;
4. transizione valida/non valida;
5. perché testare anche lo stato;
6. perché metodo del dominio è spesso migliore di setter generico;
7. istanze indipendenti.

---

# 19. Sintesi

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

Nel prossimo modulo più oggetti collaboreranno tramite **composizione**. Il problema non sarà più soltanto “come proteggo un oggetto?”, ma “chi è responsabile di che cosa?”.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 — classes;
- *Think Python / Pensare in Python* — object state;
- pratiche di object design/invariants adattate al beginner;
- `TheBitPoets/romeo@45e5f7e1...` come applied domain;
- TheBitLab `2cornot2c#758` — P3 object behavior.

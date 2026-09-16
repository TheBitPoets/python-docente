# M30 — Capstone OOP: analisi, oggetti, composizione e test

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il capstone integra specifica, strutture dati, oggetti collaboranti, invarianti e test nel prodotto finale.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Integrare funzioni, collezioni, I/O e OOP da M13–M29, rispettando i confini del percorso.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
analizzare una specifica;<br>scegliere dati/strutture coerenti;<br>individuare almeno due responsabilità OOP; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
La composizione fra oggetti e almeno una invariante sono parti del contratto del progetto. Riprendi <a href="29_COMPOSIZIONE_COLLABORAZIONE_RESPONSABILITA.md">M29 — Composizione, collaborazione e responsabilità</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il <a href="../../student/CHECKPOINT_C.md">Checkpoint C</a> raccoglie le evidenze finali e guida il consolidamento delle competenze.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Prepara modello, casi di test e una prima funzionalità completa; usa le evidenze per il Checkpoint C e la spiegazione progettuale.
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
<strong>Finestra:</strong> settimane 31–32, con Checkpoint C alla settimana 33<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Il capstone dimostra che sai integrare il percorso del secondo anno.</p>

<p align="justify">Devi saper:</p>

<ul>
  <li>analizzare una specifica;</li>
  <li>scegliere dati/strutture coerenti;</li>
  <li>individuare almeno due responsabilità OOP;</li>
  <li>definire classi/istanze con <code>__init__</code> e metodi;</li>
  <li>mantenere almeno una invariante semplice;</li>
  <li>usare composizione/collaborazione;</li>
  <li>riusare liste/dict/set/tuple quando servono;</li>
  <li>separare I/O e logica di dominio;</li>
  <li>progettare test prima/durante l'implementazione;</li>
  <li>includere almeno un caso limite o transizione rifiutata;</li>
  <li>diagnosticare/refactorare un problema;</li>
  <li>spiegare una scelta di design;</li>
  <li>usare Git G1 per checkpoint significativi se il profilo è disponibile.</li>
</ul>

---

## 1. Non è “un programma grande”

<p align="justify">Un capstone non viene valutato per numero di righe.</p>

<p align="justify">È un problema abbastanza ricco da richiedere:</p>

```text
analisi
→ decomposizione
→ modello dati
→ oggetti
→ collaborazione
→ test
→ revisione
```

<p align="justify">Una soluzione più piccola ma coerente vale più di una soluzione enorme e fragile.</p>

---

## 2. Contratto minimo del prodotto

<p align="justify">Il prodotto deve contenere almeno:</p>

```text
1 analisi input/output/vincoli
2 classi significative oppure 1 classe + 1 collaboratore oggetto reale
1 relazione di composizione
1 invariante semplice
1 struttura dati non banale
5+ casi/test complessivi
1 edge case
1 breve spiegazione progettuale
```

<p align="justify">Persistenza file è <strong>desiderabile ma non obbligatoria</strong> se il calendario o P4 non sono pronti.</p>

---

## 3. Prima del codice: il modello

<p align="justify">Scrivi:</p>

### Oggetti candidati

```text
nome classe
responsabilità
stato essenziale
metodi candidati
invariante
```

### Relazioni

```text
chi usa/possiede chi?
```

### Dati

```text
list / tuple / set / dict
```

<p align="justify">con una motivazione breve.</p>

---

## 4. Esempio generico: sistema di consegne

<p align="justify">Possibili responsabilità:</p>

```text
Veicolo
- stato/posizione/capacità
- muovi/carica/scarica

MissioneConsegna
- target/checkpoint
- completamento
- usa un Veicolo
```

<p align="justify">Strutture:</p>

```text
lista checkpoint
dict consegne per codice
set checkpoint completati
```

<p align="justify">Non è obbligatorio usare tutte queste strutture: scegli solo quelle motivate.</p>

---

## 5. Variante Romeo simulata

<p align="justify">Se <code>romeo-sim</code> è certificato:</p>

```text
Robot
→ oggetto/runtime reale Romeo

Missione
→ obiettivi/checkpoint/regole
→ compone/usa Robot
```

<p align="justify">Il capstone deve misurare Python/OOP, non conoscenze hardware.</p>

<p align="justify">Nessun CRICKIT/Raspberry Pi/sensore fisico è requisito core.</p>

---

## 6. Variante generica equivalente

<p align="justify">Se Romeo non è disponibile, usare un dominio equivalente, ad esempio:</p>

<ul>
  <li><code>Veicolo</code> + <code>Missione</code>;</li>
  <li><code>Prodotto</code> + <code>Ordine</code>;</li>
  <li><code>Prenotazione</code> + <code>Servizio</code>;</li>
  <li><code>Biblioteca</code> + <code>Prestito</code>;</li>
  <li><code>Giocatore</code> + <code>Partita</code> semplice.</li>
</ul>

<p align="justify">La rubrica resta la stessa.</p>

---

## 7. Invarianti

<p align="justify">Ogni capstone deve dichiararne almeno una.</p>

<p align="justify">Esempi:</p>

```text
stock >= 0
0 <= carico <= capacita
saldo >= 0
checkpoint completati ⊆ checkpoint previsti
```

<p align="justify">Poi servono test che provino almeno un confine dell'invariante.</p>

---

## 8. Composizione

<p align="justify">Esempio:</p>

```python
missione = Missione(veicolo, checkpoint)
```

<p align="justify">La missione non è una subclass del veicolo.</p>

<p align="justify">Ha/usa un veicolo perché le responsabilità sono diverse.</p>

---

## 9. Strutture dati dentro OOP

<p align="justify">OOP non elimina le collezioni.</p>

<p align="justify">Esempio:</p>

```python
class Missione:
    def __init__(self, checkpoint):
        self.checkpoint = list(checkpoint)
        self.completati = set()
```

<p align="justify">Le strutture studiate continuano a modellare lo stato interno.</p>

---

## 10. Separare I/O

<p align="justify">Dominio:</p>

```python
missione.completa_checkpoint("A")
```

<p align="justify">Interfaccia:</p>

```text
leggi comando
→ chiama metodo
→ mostra risultato
```

<p align="justify">Se usi file, il caricamento/salvataggio deve restare al bordo del programma quando possibile.</p>

---

## 11. Piano di implementazione

<p align="justify">Ordine consigliato:</p>

```text
1. test/casi principali
2. classe più piccola
3. stato iniziale
4. metodi fondamentali
5. invariante
6. seconda classe/composizione
7. integrazione
8. edge case
9. refactor
10. presentazione finale
```

<p align="justify">Non implementare tutto e testare soltanto alla fine.</p>

---

## 12. Test del capstone

<p align="justify">Minimo consigliato:</p>

<ul>
  <li>costruzione oggetto;</li>
  <li>metodo osservatore;</li>
  <li>transizione valida;</li>
  <li>transizione rifiutata/edge;</li>
  <li>collaborazione tra oggetti;</li>
  <li>istanze indipendenti quando rilevante.</li>
</ul>

<p align="justify">Con P3 non certificato, usare <code>assert</code> + evidence manuale.</p>

---

## 13. Regression e refactor

<p align="justify">Durante il lavoro deve comparire almeno una situazione:</p>

```text
bug / comportamento scomodo
→ caso che lo espone
→ fix
→ test verdi
→ refactor
→ test ancora verdi
```

<p align="justify">Documentala brevemente.</p>

---

## 14. Git G1

<p align="justify">Checkpoint suggeriti:</p>

```text
1. skeleton oggetti
2. comportamento core + test
3. bug-fix/refactor finale
```

<p align="justify">Prima di ogni commit:</p>

```text
status → diff → test → add → commit
```

<p align="justify">Non serve branch/PR/rebase per il core.</p>

---

## 15. Spiegazione progettuale

<p align="justify">Consegna breve, non relazione lunga.</p>

<p align="justify">Rispondi a domande come:</p>

<ol>
  <li>Quali classi hai scelto e perché?</li>
  <li>Quale relazione di composizione esiste?</li>
  <li>Quale invariante proteggi?</li>
  <li>Perché hai scelto <code>list/set/dict/tuple</code> in un punto importante?</li>
  <li>Quale bug/test ha guidato una correzione?</li>
  <li>Che cosa refactoreresti con più tempo?</li>
</ol>

---

## 16. Rubrica concettuale

<p align="justify">Dimensioni:</p>

```text
correttezza
comprensione/analisi
modello dati
responsabilità OOP
invarianti/stato
composizione
funzioni/metodi
casi/test/debug
leggibilità
spiegazione
```

<p align="justify">L'autograding può coprire comportamenti deterministici, non la qualità semantica dell'intero design.</p>

---

## 17. P3 TheBitLab

<p align="justify">Target futuro:</p>

```text
classe dichiarata
→ istanziazione sandbox
→ sequenza di metodi
→ return/stato osservabile
→ confronto trusted-side
```

<p align="justify">P3 è <code>2cornot2c#758</code>.</p>

<p align="justify">Non trasformare il capstone in un test meccanico della struttura del codice. Responsabilità/composizione/spiegazione restano rubriche docente.</p>

---

## 18. Error Clinic capstone

<ul>
  <li>god class;</li>
  <li>attributi modificati senza regole;</li>
  <li>inheritance introdotta senza necessità;</li>
  <li>dipendenze globali;</li>
  <li>input/file mescolati nel dominio;</li>
  <li>test soltanto happy-path;</li>
  <li>stato condiviso tra istanze;</li>
  <li>struttura dati scelta senza motivazione;</li>
  <li>capstone Romeo che richiede hardware o networking non curricolare.</li>
</ul>

---

## 19. Cosa NON è obbligatorio

<ul>
  <li>inheritance;</li>
  <li>property;</li>
  <li>dataclass;</li>
  <li>multi-file package;</li>
  <li>database;</li>
  <li>GUI/web;</li>
  <li>async;</li>
  <li>rete;</li>
  <li>hardware fisico;</li>
  <li>JSON/CSV persistence;</li>
  <li>pytest professionale.</li>
</ul>

<p align="justify">Questi possono essere enrichment/futuro.</p>

---

## 20. Exit outcome del secondo anno

<p align="justify">Se completi il capstone dovresti riuscire a raccontare l'intera catena:</p>

```text
problema
→ algoritmo
→ dati
→ controllo del flusso
→ funzioni
→ strutture dati
→ oggetti
→ stato/invarianti
→ composizione
→ test/debug/refactor
```

<p align="justify">Questo è il vero risultato del corso: non una lista di parole chiave Python, ma la capacità di progettare e verificare piccoli programmi in modo consapevole.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — classes/collections;</li>
  <li><em>Think Python / Pensare in Python</em> — percorso beginner→objects;</li>
  <li><em>Learning Python / Imparare Python</em> — reference;</li>
  <li><code>TheBitPoets/romeo@45e5f7e1...</code> — applied simulator/object domain;</li>
  <li><code>tracks/secondo/ROMEO_MAPPING.md</code>;</li>
  <li>TheBitLab <code>2cornot2c#758</code> — P3 object behavior.</li>
</ul>

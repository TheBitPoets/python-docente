# M30 — Capstone OOP: analisi, oggetti, composizione e test

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-10 — Classi, oggetti e capstone  
> **Finestra:** settimane 31–32, con Checkpoint C alla settimana 33  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Il capstone dimostra che sai integrare il percorso del secondo anno.

Devi saper:

- analizzare una specifica;
- scegliere dati/strutture coerenti;
- individuare almeno due responsabilità OOP;
- definire classi/istanze con `__init__` e metodi;
- mantenere almeno una invariante semplice;
- usare composizione/collaborazione;
- riusare liste/dict/set/tuple quando servono;
- separare I/O e logica di dominio;
- progettare test prima/durante l'implementazione;
- includere almeno un caso limite o transizione rifiutata;
- diagnosticare/refactorare un problema;
- spiegare una scelta di design;
- usare Git G1 per checkpoint significativi se il profilo è disponibile.

---

# 1. Non è “un programma grande”

Un capstone non viene valutato per numero di righe.

È un problema abbastanza ricco da richiedere:

```text
analisi
→ decomposizione
→ modello dati
→ oggetti
→ collaborazione
→ test
→ revisione
```

Una soluzione più piccola ma coerente vale più di una soluzione enorme e fragile.

---

# 2. Contratto minimo del prodotto

Il prodotto deve contenere almeno:

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

Persistenza file è **desiderabile ma non obbligatoria** se il calendario o P4 non sono pronti.

---

# 3. Prima del codice: il modello

Scrivi:

## Oggetti candidati

```text
nome classe
responsabilità
stato essenziale
metodi candidati
invariante
```

## Relazioni

```text
chi usa/possiede chi?
```

## Dati

```text
list / tuple / set / dict
```

con una motivazione breve.

---

# 4. Esempio generico: sistema di consegne

Possibili responsabilità:

```text
Veicolo
- stato/posizione/capacità
- muovi/carica/scarica

MissioneConsegna
- target/checkpoint
- completamento
- usa un Veicolo
```

Strutture:

```text
lista checkpoint
dict consegne per codice
set checkpoint completati
```

Non è obbligatorio usare tutte queste strutture: scegli solo quelle motivate.

---

# 5. Variante Romeo simulata

Se `romeo-sim` è certificato:

```text
Robot
→ oggetto/runtime reale Romeo

Missione
→ obiettivi/checkpoint/regole
→ compone/usa Robot
```

Il capstone deve misurare Python/OOP, non conoscenze hardware.

Nessun CRICKIT/Raspberry Pi/sensore fisico è requisito core.

---

# 6. Variante generica equivalente

Se Romeo non è disponibile, usare un dominio equivalente, ad esempio:

- `Veicolo` + `Missione`;
- `Prodotto` + `Ordine`;
- `Prenotazione` + `Servizio`;
- `Biblioteca` + `Prestito`;
- `Giocatore` + `Partita` semplice.

La rubrica resta la stessa.

---

# 7. Invarianti

Ogni capstone deve dichiararne almeno una.

Esempi:

```text
stock >= 0
0 <= carico <= capacita
saldo >= 0
checkpoint completati ⊆ checkpoint previsti
```

Poi servono test che provino almeno un confine dell'invariante.

---

# 8. Composizione

Esempio:

```python
missione = Missione(veicolo, checkpoint)
```

La missione non è una subclass del veicolo.

Ha/usa un veicolo perché le responsabilità sono diverse.

---

# 9. Strutture dati dentro OOP

OOP non elimina le collezioni.

Esempio:

```python
class Missione:
    def __init__(self, checkpoint):
        self.checkpoint = list(checkpoint)
        self.completati = set()
```

Le strutture studiate continuano a modellare lo stato interno.

---

# 10. Separare I/O

Dominio:

```python
missione.completa_checkpoint("A")
```

Interfaccia:

```text
leggi comando
→ chiama metodo
→ mostra risultato
```

Se usi file, il caricamento/salvataggio deve restare al bordo del programma quando possibile.

---

# 11. Piano di implementazione

Ordine consigliato:

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

Non implementare tutto e testare soltanto alla fine.

---

# 12. Test del capstone

Minimo consigliato:

- costruzione oggetto;
- metodo osservatore;
- transizione valida;
- transizione rifiutata/edge;
- collaborazione tra oggetti;
- istanze indipendenti quando rilevante.

Con P3 non certificato, usare `assert` + evidence manuale.

---

# 13. Regression e refactor

Durante il lavoro deve comparire almeno una situazione:

```text
bug / comportamento scomodo
→ caso che lo espone
→ fix
→ test verdi
→ refactor
→ test ancora verdi
```

Documentala brevemente.

---

# 14. Git G1

Checkpoint suggeriti:

```text
1. skeleton oggetti
2. comportamento core + test
3. bug-fix/refactor finale
```

Prima di ogni commit:

```text
status → diff → test → add → commit
```

Non serve branch/PR/rebase per il core.

---

# 15. Spiegazione progettuale

Consegna breve, non relazione lunga.

Rispondi a domande come:

1. Quali classi hai scelto e perché?
2. Quale relazione di composizione esiste?
3. Quale invariante proteggi?
4. Perché hai scelto `list/set/dict/tuple` in un punto importante?
5. Quale bug/test ha guidato una correzione?
6. Che cosa refactoreresti con più tempo?

---

# 16. Rubrica concettuale

Dimensioni:

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

L'autograding può coprire comportamenti deterministici, non la qualità semantica dell'intero design.

---

# 17. P3 TheBitLab

Target futuro:

```text
classe dichiarata
→ istanziazione sandbox
→ sequenza di metodi
→ return/stato osservabile
→ confronto trusted-side
```

P3 è `2cornot2c#758`.

Non trasformare il capstone in un test meccanico della struttura del codice. Responsabilità/composizione/spiegazione restano rubriche docente.

---

# 18. Error Clinic capstone

- god class;
- attributi modificati senza regole;
- inheritance introdotta senza necessità;
- dipendenze globali;
- input/file mescolati nel dominio;
- test soltanto happy-path;
- stato condiviso tra istanze;
- struttura dati scelta senza motivazione;
- capstone Romeo che richiede hardware o networking non curricolare.

---

# 19. Cosa NON è obbligatorio

- inheritance;
- property;
- dataclass;
- multi-file package;
- database;
- GUI/web;
- async;
- rete;
- hardware fisico;
- JSON/CSV persistence;
- pytest professionale.

Questi possono essere enrichment/futuro.

---

# 20. Exit outcome del secondo anno

Se completi il capstone dovresti riuscire a raccontare l'intera catena:

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

Questo è il vero risultato del corso: non una lista di parole chiave Python, ma la capacità di progettare e verificare piccoli programmi in modo consapevole.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 — classes/collections;
- *Think Python / Pensare in Python* — percorso beginner→objects;
- *Learning Python / Imparare Python* — reference;
- `TheBitPoets/romeo@45e5f7e1...` — applied simulator/object domain;
- `tracks/secondo/ROMEO_MAPPING.md`;
- TheBitLab `2cornot2c#758` — P3 object behavior.

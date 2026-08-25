# M30 — Runbook docente

## Modulo

**Capstone OOP: analisi, oggetti, composizione e test**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Usare il capstone come prova integrata del percorso, non come gara di complessità o lunghezza.

Competenze osservate:

```text
analisi
+ data model
+ classi/stato
+ invarianti
+ composizione
+ funzioni/metodi
+ test/debug/refactor
+ spiegazione
```

## Finestra

Settimane 31–32. La settimana 33 resta Checkpoint C per finalizzazione, recupero o enrichment.

## Contratto minimo

Richiedere:

- almeno 2 responsabilità OOP significative;
- relazione di composizione;
- almeno 1 invariante;
- almeno 1 struttura dati motivata;
- 5+ casi/test;
- 1 edge case/transizione rifiutata;
- una breve evidence di bug-fix/regression/refactor;
- spiegazione progettuale breve.

Persistenza file è desiderabile ma non obbligatoria.

## Variante Romeo

Usabile soltanto se `romeo-sim` è certificato nel Classroom Environment.

Pattern consigliato:

```text
Robot
→ stato/movimento/safety di base

Missione
→ checkpoint/obiettivo/regole
→ usa Robot
```

Non importare networking, camera, FastAPI, WebSocket o hardware fisico dal track Romeo avanzato.

## Variante generica

Deve essere sempre disponibile e valutata con la stessa rubrica.

Domini candidati:

- Veicolo + Missione;
- Prodotto + Ordine;
- Prenotazione + Servizio;
- Biblioteca + Prestito;
- Giocatore + Partita semplice.

## Ritmo consigliato

### Fase 1 — design

- specifica;
- classi/responsabilità;
- relazione di composizione;
- stato/invarianti;
- struttura dati;
- casi di test.

### Fase 2 — skeleton

- `__init__`;
- metodi minimi;
- primi assert;
- primo checkpoint Git.

### Fase 3 — comportamento

- transizioni valide/invalide;
- collaborazione;
- edge cases;
- secondo checkpoint Git.

### Fase 4 — review

- bug/regression;
- refactor;
- tutti i test;
- spiegazione;
- commit finale.

## Rubrica

Dimensioni candidate:

- correttezza;
- comprensione/analisi;
- modello dati;
- responsabilità OOP;
- stato/invarianti;
- composizione;
- decomposizione/metodi;
- test/debug/regression;
- leggibilità;
- spiegazione.

I pesi finali vanno allineati alla V4 del calendario senza trasformare design e spiegazione in falsi test automatici.

## Misconception watchlist

- più classi = progetto migliore;
- inheritance obbligatoria per essere OOP;
- god class;
- input/file dentro ogni metodo;
- test soltanto happy-path;
- capstone Romeo che misura hardware;
- GUI/web aggiunti per impressionare ma fuori curriculum;
- refactor effettuato senza rieseguire i test.

## Recovery

Se lo studente è in difficoltà, ridurre il dominio, non eliminare gli outcome core.

Minimo recuperabile:

```text
2 classi piccole
1 composizione
1 invariante
1 list/dict/set motivato
5 test
1 spiegazione
```

## Enrichment

Solo dopo il core:

- `__str__`;
- property semplice;
- inheritance minimale e motivata;
- file persistence se P4/workflow è disponibile;
- variante Romeo più articolata nel simulatore;
- dataclass come confronto dopo la classe esplicita.

## P3

`2cornot2c#758` può coprire comportamento deterministico di classi/istanze/metodi/stato.

Restano rubriche manuali:

- qualità delle responsabilità;
- adeguatezza della composizione;
- chiarezza del modello;
- spiegazione.

## Git G1

Richiedere checkpoint significativi, non un numero artificiale di commit.

Workflow:

```text
status → diff → test → add → commit → log
```

La sintassi definitiva deve puntare al materiale Git G1 canonico dopo audit dispense.

## Checkpoint C

Settimana 33:

- finalizzazione;
- recupero mirato;
- presentazione breve;
- enrichment;
- nessun nuovo prerequisito obbligatorio.

## Gate per promozione del capstone

Prima di renderlo definitivo:

- scegliere 1–2 specifiche concrete equivalenti;
- prototipare la rubrica;
- verificare carico reale in 6h + buffer;
- certificare Romeo se usato come variante;
- certificare P3 prima di promettere object autograding;
- mantenere sempre fallback generico.

# M25 — Runbook docente

## Modulo

**Strutture combinate e scelta del modello dati**  
UDA PY2-08 — Set, dizionari e modellazione dei dati

Stato: draft editoriale controllato.

## Obiettivo docente

Portare la classe da:

```text
conosco list/tuple/set/dict
```

verso:

```text
riconosco le operazioni dominanti
→ scelgo il modello
→ motivo la scelta
```

È un modulo di design, non un catalogo di nesting.

---

# Priorità didattica

## MUST MASTER

1. scegliere `str/list/tuple/set/dict` dalle operazioni dominanti;
2. motivare la scelta con ordine, mutabilità, duplicati, membership, lookup e ruolo dei campi;
3. riconoscere liste parallele come modello fragile in molti casi;
4. confrontare almeno due modelli plausibili;
5. usare una semplice struttura combinata quando il dominio la richiede;
6. evitare profondità di nesting priva di significato;
7. spiegare il ponte record/dict → oggetto senza anticipare classi.

## GUIDED EXPOSURE

- lista di tuple vs lista di dict;
- dict indicizzato per identità;
- dict di liste per relazione uno→molti;
- lookup diretto vs scansione ripetuta in linguaggio qualitativo.

## ENRICHMENT / BACKUP

- dict di set;
- `setdefault()`;
- matrice sparsa con tuple-key;
- lista di dict vs dict di dict;
- inversione frequenza→lista.

La complessità strutturale non è un obiettivo: una sola struttura ben scelta può essere migliore di tre contenitori annidati.

---

# Ora teoria attiva 1 — scegliere il modello

1. Mappa `str/list/tuple/set/dict`.
2. Liste parallele come smell.
3. Lista di tuple vs lista di dict su un record piccolo.
4. Dict indicizzato per identità quando il lookup domina.
5. Ordine/duplicati/membership/lookup come criteri.

Per ogni scenario chiedere prima:

```text
quale operazione faccio più spesso?
quale informazione deve essere naturale da leggere/aggiornare?
```

---

# Ora teoria attiva 2 — combinare solo quando serve

1. Dict di liste come primo modello uno→molti.
2. Refactoring di liste parallele.
3. Annidamento con significato vs profondità gratuita.
4. Ponte record/dict → classe futura.
5. Confronto qualitativo scansione vs lookup diretto.

`dict di set`, `setdefault` e matrice sparsa restano enrichment se il core non è già stabile.

---

# Laboratorio

- data-model choice cards;
- refactoring liste parallele;
- una struttura combinata semplice scelta dal dominio;
- confronto fra due modelli plausibili;
- mini-project con **modello sufficiente e motivato**, non con un numero minimo artificiale di contenitori;
- spiegazione scritta delle operazioni dominanti.

Il mini-project non richiede per principio “almeno due strutture combinate”. Se un dict semplice rappresenta bene il dominio, questa può essere la scelta migliore.

---

# Minimum mastery gate — exit PY2-08

Considerare PY2-08 consolidata quando lo studente riesce a:

- scegliere fra list/tuple/set/dict in scenari semplici;
- motivare la scelta con almeno 2 criteri del dominio;
- usare set per unicità/membership;
- usare dict per lookup chiave→valore;
- gestire chiavi mancanti secondo contratto;
- costruire una frequenza semplice;
- usare `items()` quando servono chiave+valore;
- riconoscere liste parallele fragili;
- usare una struttura combinata semplice senza annidamento gratuito;
- spiegare il ponte record/dict → oggetto.

Non richiedere `setdefault`, dict di set, matrice sparsa o nesting profondo per superare il gate.

---

# Misconception watchlist

- dict scelto sempre perché “più potente”;
- set usato perdendo ordine/duplicati richiesti;
- tuple usata per record con molti campi poco leggibili;
- nesting profondo considerato sofisticazione;
- ordine di inserimento del dict confuso con semantica posizionale;
- default usato per nascondere dato obbligatorio;
- scegliere una struttura perché “è l'ultima studiata”.

---

# Differenziazione

## Recupero

- scegliere tra due sole strutture candidate;
- record con 2 campi;
- dict di liste già schematizzato;
- tabella criteri ordine/unicità/lookup;
- nessun nesting oltre due livelli inizialmente.

## Enrichment

- matrice sparsa con tuple-key;
- setdefault dopo pattern esplicito;
- dict di set;
- lista di dict vs dict di dict;
- costo qualitativo scansione vs lookup.

---

# Evidence docente

Raccogliere:

- almeno 3 scelte struttura motivate;
- refactoring liste parallele;
- una struttura combinata realmente giustificata;
- piccolo data-model diagram;
- spiegazione del ponte record→oggetto.

---

# Friedpython

Audit: `sources/FRIEDPYTHON_DICTS_AUDIT.md`.

Esercizi 5–6 sono spunti per frequenze e dict di liste, ma vanno riscritti. Le vecchie note su ordine/keys non vanno propagate.

---

# Cosa NON anticipare

- dataclass/classi;
- defaultdict/Counter come core;
- database/ORM;
- JSON persistence;
- generics/type hints avanzati.

---

# Handoff a PY2-09

Il modello dati ora è abbastanza ricco. M26 aggiunge soltanto il confine minimo di persistenza:

```text
workspace path
→ file testo UTF-8
→ with/open
→ errore esterno mirato
```

senza sottrarre tempo all'OOP.

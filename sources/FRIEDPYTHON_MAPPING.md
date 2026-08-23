# friedpython → python-docente mapping (DRAFT)

Source repository: `TheBitPoets/friedpython`  
Audited source SHA: `cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f`

`friedpython` è un **source pack legacy**, non una dipendenza del nuovo corso. Gli asset vengono importati selettivamente con provenance esplicita e possono essere riscritti, spezzati, testati o riclassificati.

## Inventario iniziale osservato

| Area friedpython | Contenuto osservato | Destinazione candidata | Azione |
|---|---|---|---|
| root `README.md` | tipizzazione dinamica, nomi/oggetti/reference condivise | A1/B1 | semplificare per beginner; preservare modello corretto; parte avanzata in B1 |
| `stringhe/` | esempi su stringhe | A6 | audit e trasformazione in microscopes |
| `esercizi_stringhe/` | almeno 7 esercizi + verifica | A6 | classificare A/B/C/D e revisionare consegne/test |
| `liste/` | base, slicing, metodi, iterazione/mapping, matrici | A7/B2 | separare core beginner da comprehension/mapping avanzati |
| `esercizi_liste/` | almeno 6 esercizi + verifica | A7 | trasformare in problems/Activity; aggiungere edge cases/test |
| `tuple/` | immutabilità, metodi/conversioni, esempi d'uso | A7 | integrare nel confronto list vs tuple |
| `dizionari/` | CRUD, iterazione, missing key, ordering, creazione, matrici sparse | A8/B7 | core dict in A8; matrici sparse come enrichment/advanced |
| `esercizi_dizionari/` | almeno 6 esercizi + PDF | A8 | classificare, modernizzare, aggiungere rubric/test |
| `esercizi_strutture_dati/` | raccolte cumulative stringhe/liste/dict + PDF | A6–A8 assessment | usare come banca per verifiche cumulative, non come unica sequenza |
| `file/` | open, esempi, file binari, context manager | A9/B8/C7 | text + `with` in A9; binary/advanced I/O dopo |

## Regole di importazione

Ogni asset importato deve dichiarare:

```text
source_repo: TheBitPoets/friedpython
source_sha: cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f
source_path: ...
transformation: reused | adapted | rewritten | split | combined
reason: ...
```

## Checklist prima dell'import

- sintassi compatibile con la Python target;
- naming e stile coerenti con il nuovo corso;
- nessuna spiegazione fuorviante sul modello Python;
- difficoltà adeguata ai prerequisiti della UDA;
- consegna separata dalla solution;
- edge cases espliciti;
- test deterministici quando appropriato;
- classificazione Activity A–F;
- eventuale materiale docente separato dallo scaffold studente;
- provenance mantenuta.

## Cosa manca in friedpython e va progettato ex novo

L'audit iniziale non mostra un curriculum completo per:

- problem solving e decomposizione;
- pseudocodice e flow chart;
- primi programmi/input/output;
- selezione completa e annidata;
- iterazione completa e annidata;
- pattern algoritmici;
- funzioni e progettazione top-down;
- OOP come percorso didattico;
- test come competenza progressiva;
- ambienti/package/tooling;
- database/ORM;
- professional engineering.

Queste aree devono nascere nel nuovo repository e non essere forzate dentro la struttura legacy.

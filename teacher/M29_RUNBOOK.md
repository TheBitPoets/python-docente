# M29 — Runbook docente

## Modulo

**Composizione, collaborazione e responsabilità**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Far passare la classe da singoli oggetti corretti a un piccolo sistema di oggetti con responsabilità separate.

Modello:

```text
oggetto A
→ usa/riceve oggetto B
→ ciascuno mantiene il proprio contratto
```

## Ora teoria attiva 1

1. God class come smell.
2. Composizione “ha un”.
3. Chi possiede una regola del dominio.
4. Dipendenze esplicite nel costruttore.
5. Dominio separato da input/output.

## Ora teoria attiva 2

1. Refactoring incrementale dict→object.
2. Liste/dict di oggetti.
3. Test di collaborazione.
4. Romeo: `Missione` usa `Robot` come applied design.
5. Perché inheritance non è core.

## Laboratorio

- responsibility cards;
- refactor record→classe;
- oggetto A che riceve B;
- Debug Clinic god class/dipendenza globale;
- skeleton del capstone con classi, relazioni e test candidati.

## Misconception watchlist

- più classi = design migliore;
- classe wrapper attorno a una lista/dict senza responsabilità;
- inheritance come modo predefinito di riuso;
- regole della missione dentro `Robot`;
- oggetto che costruisce internamente ogni dipendenza rendendo impossibile il test;
- input/file dentro il dominio per comodità.

## Differenziazione

### Recupero

- due classi soltanto;
- una relazione “ha un”;
- dipendenza già suggerita;
- niente persistence nel capstone skeleton.

### Enrichment

- confronto composizione vs inheritance semplice;
- dict di oggetti;
- sostituzione di una dipendenza con fake molto semplice per test concettuale;
- `__str__` per diagnostica.

## Evidence docente

Raccogliere:

- responsabilità di 2–3 classi;
- diagramma di composizione;
- dipendenza esplicita;
- test di collaborazione;
- refactoring piccolo protetto da test.

## Romeo

Se `romeo-sim` è certificato, usare `Robot` come dipendenza reale di `Missione`. Non importare networking/web/camera dal curriculum Romeo avanzato.

Se il runtime non è certificato, usare il dominio generico equivalente: `Veicolo/Missione`, `Catalogo/Prodotto`, `Prenotazione/Servizio` o simile.

## P3

P3 deve verificare classi/istanze/metodi/stato nel sandbox. Le rubriche di responsabilità/composizione restano comunque in parte manuali: non fingere autograding semantico del design.

## Cosa NON anticipare

- design patterns;
- DI framework;
- inheritance polymorphism come requisito;
- abstract base classes;
- multi-package architecture.

## Handoff a M30

M29 produce lo skeleton progettuale. M30 lo trasforma in un prodotto integrato:

```text
analisi
→ modello dati/oggetti
→ classi
→ composizione
→ test
→ debug/refactor
→ breve spiegazione
```

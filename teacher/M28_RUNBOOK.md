# M28 — Runbook docente

## Modulo

**Metodi, stato e invarianti**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Far capire che l'OOP non è soltanto “mettere funzioni dentro una classe”. Un oggetto utile mantiene uno stato e offre operazioni coerenti con le regole del dominio.

## Ora teoria attiva 1

1. Stato dell'istanza.
2. Metodo osservatore vs mutante.
3. Invariante semplice.
4. Costruzione valida con `__init__`.
5. Metodo del dominio vs setter generico.

## Ora teoria attiva 2

1. Transizioni valide/non valide.
2. Validare prima di mutare.
3. Test del return + stato.
4. Casi limite suggeriti dall'invariante.
5. Istanze indipendenti.

## Laboratorio

- state trace;
- `ContatoreLimitato` / `Serbatoio`;
- aggiunta di un'invariante;
- test di transizione rifiutata;
- Debug Clinic su update-before-validation e stato condiviso.

## Misconception watchlist

- attributi pubblici = qualunque modifica è sempre corretta;
- setter per ogni attributo come regola OOP;
- invariante = assert scritto a caso;
- testare soltanto ciò che restituisce il metodo;
- se un metodo fallisce può lasciare lo stato mezzo modificato;
- dati derivati duplicati senza necessità.

## Differenziazione

### Recupero

- un solo attributo di stato + limite;
- un osservatore + un mutante;
- tre casi: valido, limite, invalido.

### Enrichment

- `__str__` per osservabilità;
- policy alternativa di errore discussa senza implementare eccezioni custom;
- più invarianti correlate;
- ispezione guidata dello stato Romeo simulato.

## Evidence docente

Raccogliere:

- invariante scritto in linguaggio naturale;
- stato iniziale;
- due transizioni;
- test di transizione rifiutata con stato invariato;
- spiegazione della responsabilità del metodo.

## P3

Il futuro P3 (`2cornot2c#758`) deve poter istanziare la classe, chiamare metodi e osservare stato/return autorizzati dentro il sandbox. Expected e rubric restano trusted-side.

## Cosa NON anticipare

- property come prerequisito;
- inheritance;
- custom exceptions;
- dataclass;
- pattern OOP formali.

## Handoff a M29

M28 protegge un singolo oggetto. M29 introduce collaborazione:

```text
oggetto A possiede/riceve oggetto B
→ responsabilità separate
→ composizione
```

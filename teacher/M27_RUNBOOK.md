# M27 — Runbook docente

## Modulo

**Classi, istanze, attributi e `self`**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Introdurre OOP come risposta a un problema di modellazione:

```text
dati + comportamenti + responsabilità
→ oggetto candidato
```

Non presentare le classi come contenitori obbligatori o come “livello professionale” superiore alle funzioni.

## Ora teoria attiva 1 — record → classe

1. Riprendere record `dict` di M25.
2. Aggiungere comportamenti legati al record.
3. Classe vs istanza.
4. `__init__` e attributi.
5. Due istanze con stato diverso.

## Ora teoria attiva 2 — self e metodi

1. Metodo che legge lo stato.
2. `self` come istanza corrente.
3. Metodo che modifica lo stato in modo semplice.
4. Quando una funzione resta migliore di una classe.
5. Romeo `easy` vs `Robot` come demo opzionale, solo con runtime certificato.

## Laboratorio

- class/instance microscope;
- `Contatore` con due istanze;
- refactor dict→object;
- Debug Clinic su `self`, attributi e stato condiviso;
- test/manual evidence di indipendenza istanze.

## Misconception watchlist

- classe = oggetto concreto;
- `self` come parola magica globale;
- ogni funzione deve diventare metodo;
- `__init__` restituisce esplicitamente l'oggetto;
- attributi locali senza `self` come stato;
- lista mutabile di classe usata accidentalmente per tutte le istanze.

## Differenziazione

### Recupero

- classe con 2 attributi;
- un metodo osservatore;
- due istanze;
- niente composizione ancora.

### Enrichment

- `__str__` come preview controllata;
- confronto dict/object;
- piccola classe con metodo mutante;
- inspect Romeo `Robot` senza hardware.

## Evidence docente

Raccogliere:

- identificazione classe/istanza;
- `__init__` corretto;
- due istanze indipendenti;
- metodo che usa `self`;
- spiegazione perché la classe rappresenta una responsabilità del dominio.

## P3 TheBitLab

`2cornot2c#758` è il profilo corretto per grading oggetti. Il futuro worker deve poter:

```text
import modulo
→ istanzia classe
→ chiama metodi
→ osserva return/stato ammesso
→ trusted host confronta expected
```

Niente P1/P2 artificiale per fingere object grading.

## Cosa NON anticipare

- inheritance come core;
- metaclass;
- descriptor;
- property come prerequisito;
- dataclass prima della classe esplicita;
- design pattern.

## Handoff a M28

M27 crea oggetti con stato.
M28 chiede:

> quali stati sono validi e attraverso quali metodi permettiamo di cambiarli?

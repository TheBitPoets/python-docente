# M28 — Runbook docente

## Modulo

**Metodi, stato e invarianti**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Portare la classe da “oggetto = contenitore di attributi” a:

```text
stato valido
→ metodo del dominio
→ transizione controllata
→ nuovo stato valido
```

L'invariante deve diventare una frase concreta e testabile, non un termine da memorizzare.

---

# Priorità didattica

## MUST MASTER

1. identificare lo stato di un'istanza;
2. distinguere un metodo che osserva da uno che modifica lo stato;
3. scrivere un invariante semplice in linguaggio naturale;
4. costruire l'oggetto in uno stato valido;
5. validare una transizione prima di applicarla;
6. lasciare lo stato invariato dopo una transizione rifiutata;
7. testare sia il segnale/return sia lo stato risultante;
8. progettare casi di confine suggeriti dall'invariante;
9. mantenere istanze indipendenti.

## GUIDED EXPOSURE

- termini observer/mutator;
- policy alternative di segnalazione del fallimento;
- `assert` interno come controllo didattico;
- `__str__` per osservabilità.

## ENRICHMENT / BACKUP

- property;
- eccezioni custom;
- invarianti multiple più ricche.

`return False` è **una policy possibile**, non l'unica API OOP corretta.

---

# Ora teoria attiva 1 — stato e invariante

1. Riprendere una classe M27.
2. Identificare gli attributi che descrivono lo stato.
3. Separare metodo osservatore e metodo che cambia stato.
4. Scrivere un invariante come frase.
5. Verificare che `__init__` produca uno stato valido.

Esempio:

```text
0 <= livello <= capacita
```

L'invariante deve suggerire immediatamente casi di test.

---

# Ora teoria attiva 2 — transizioni controllate

1. Metodo `aggiungi`/`consuma` con validazione prima della mutazione.
2. Transizione valida.
3. Transizione rifiutata con stato invariato.
4. Test sia del segnale sia dello stato.
5. Confronto fra due policy di fallimento semplici:
   - `False`;
   - altra forma dichiarata dal contratto.

Il punto è il **contratto coerente**, non imporre `False` come stile universale.

---

# Laboratorio

- completa un metodo osservatore;
- implementa una transizione valida;
- aggiungi caso limite esatto;
- aggiungi transizione rifiutata;
- verifica stato invariato dopo fallimento;
- due istanze indipendenti;
- Debug Clinic su validazione dopo mutazione/stato condiviso/setter che bypassa regole.

---

# Minimum mastery gate — prima di M29

Considerare M28 consolidato quando lo studente riesce a:

- indicare lo stato di un oggetto;
- scrivere un invariante semplice;
- costruire l'oggetto in stato valido;
- distinguere osservazione e mutazione;
- validare prima di modificare;
- preservare lo stato su transizione rifiutata;
- testare stato e segnale;
- derivare casi limite dall'invariante;
- dimostrare indipendenza fra due istanze.

Property, custom exceptions e una particolare policy di fallimento non sono prerequisiti del gate.

---

# Misconception watchlist

- invariante = qualsiasi `if`;
- validare dopo aver già corrotto lo stato;
- testare solo il return;
- rifiutare una transizione ma lasciare stato parzialmente modificato;
- setter generico usato per bypassare le regole del dominio;
- `False` considerato l'unico modo corretto per segnalare un rifiuto;
- stato di classe condiviso confuso con stato per istanza.

---

# Differenziazione

## Recupero

- un solo attributo di stato + capacità;
- due transizioni;
- invariante già suggerito;
- assert su stato espliciti.

## Enrichment

- `__str__`;
- `assert` interno didattico;
- più invarianti;
- confronto policy di fallimento;
- property dopo mastery del metodo di dominio.

---

# Evidence docente

Raccogliere:

- invariante scritto;
- transizione valida;
- transizione rifiutata;
- test dello stato prima/dopo;
- caso limite;
- test di indipendenza istanze.

---

# P3 — teacher/delivery boundary

Il profilo P3 (`2cornot2c#758`) riguarda autograding del comportamento degli oggetti. Non è contenuto studente.

Fino alla certificazione usare assert/manual evidence e rubriche senza promettere object autograding.

---

# Cosa NON anticipare

- property come requisito;
- custom exceptions;
- inheritance;
- dataclass;
- pattern State/Command;
- framework di validazione.

---

# Handoff a M29

M28 rende affidabile un singolo oggetto.

M29 chiede:

> come collaborano più oggetti senza concentrare tutte le regole in una sola classe?

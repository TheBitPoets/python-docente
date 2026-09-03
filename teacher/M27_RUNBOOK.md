# M27 — Runbook docente

## Modulo

**Classi, istanze, attributi e `self`**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Far emergere l'OOP come scelta di modellazione:

```text
dati + comportamenti della stessa responsabilità
→ classe candidata
```

Non insegnare una classe come “scatola più avanzata” o come sostituto automatico di funzioni/dict.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. distinguere classe e istanza;
2. usare `__init__` per inizializzare lo stato essenziale;
3. usare attributi di istanza tramite `self`;
4. definire/chiamare un metodo che usa lo stato;
5. creare due istanze indipendenti;
6. spiegare che `self` indica l'istanza corrente della chiamata;
7. scegliere una classe quando dati e comportamenti formano una responsabilità significativa;
8. riconoscere quando una funzione/dict resta il modello più semplice.

## GUIDED EXPOSURE

- bug di stato mutabile condiviso tramite attributo di classe;
- `__str__` come osservabilità;
- confronto con API Romeo procedurale/object-style se runtime certificato.

## ENRICHMENT / BACKUP

- metodi di rappresentazione più ricchi;
- introspezione semplice;
- dettagli sugli attributi di classe oltre il bug didattico.

M27 non è una lezione sugli attributi di classe: il core è **stato per istanza**.

---

# Ora teoria attiva 1 — da record a classe

1. Riprendere un record/dict da M25.
2. Chiedere quali comportamenti appartengono a quei dati.
3. Definire una classe semplice.
4. Creare due istanze.
5. `__init__` e attributi di istanza.

Domanda guida:

> perché questa responsabilità merita una classe invece di un dict + funzione?

---

# Ora teoria attiva 2 — `self`, metodi, indipendenza

1. Metodo osservabile semplice.
2. Trace di `oggetto.metodo()` come chiamata sull'istanza.
3. Due istanze con stati diversi.
4. Modificare una istanza e verificare che l'altra resti indipendente.
5. Confronto finale funzione vs classe.

Solo se il core è stabile mostrare il bug dell'attributo di classe condiviso come Error Clinic.

---

# Laboratorio

- classe/istanza microscope;
- `__init__` con 1–2 attributi;
- metodo di dominio semplice;
- due istanze indipendenti;
- refactoring dict→classe in un caso piccolo;
- Debug Clinic su `self.` dimenticato/locale vs attributo/stato condiviso.

---

# Minimum mastery gate — prima di M28

Considerare M27 consolidato quando lo studente riesce a:

- distinguere classe/istanza;
- costruire un oggetto con `__init__`;
- leggere/modificare correttamente stato di istanza tramite metodi/attributi secondo il contratto;
- spiegare `self` senza formule magiche;
- usare un metodo che dipende dallo stato;
- creare due istanze indipendenti;
- motivare perché una classe aggiunge valore in un esempio e perché in un altro basta una funzione.

Attributi di classe condivisi e `__str__` non devono dominare il gate.

---

# Misconception watchlist

- classe = oggetto;
- `self` = keyword magica separata dall'istanza;
- tutti i dati devono diventare classi;
- funzione inferiore a classe per definizione;
- locale dentro metodo scambiata per attributo;
- `self.` dimenticato;
- attributo mutabile di classe interpretato come stato indipendente per istanza.

---

# Differenziazione

## Recupero

- una classe con due attributi;
- un solo metodo;
- due istanze;
- niente class attributes;
- nessun Romeo iniziale.

## Enrichment

- `__str__`;
- confronto API procedurale/object-style;
- bug di stato condiviso;
- un terzo metodo coerente col dominio.

---

# Evidence docente

Raccogliere:

- definizione classe;
- due istanze;
- trace `self`/stato;
- metodo di dominio;
- test di indipendenza;
- motivazione classe vs funzione/dict.

---

# P3 — teacher/delivery boundary

Il futuro P3 (`2cornot2c#758`) potrà istanziare classi e osservare comportamento nel sandbox. Questa è una concern docente/piattaforma, non un outcome studente.

Fino alla certificazione usare assert/manual evidence senza fingere object autograding.

---

# Cosa NON anticipare

- property come prerequisito;
- inheritance;
- custom exceptions;
- dataclass;
- metaclass;
- internals del descriptor model.

---

# Handoff a M28

M27 crea oggetti indipendenti.

M28 chiede:

> quali stati sono validi e come impediamo che un metodo lasci l'oggetto in uno stato incoerente?

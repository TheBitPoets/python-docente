# M29 — Runbook docente

## Modulo

**Composizione, collaborazione e responsabilità**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Obiettivo docente

Far passare la classe da:

```text
oggetto singolo con stato valido
```

a:

```text
più responsabilità
→ più oggetti
→ collaborazione esplicita
→ sistema ancora testabile
```

Il centro del modulo è la **composizione**, non il numero di classi.

---

# Priorità didattica

## MUST MASTER

1. spiegare composizione come relazione “ha/usa un”;
2. assegnare una regola all'oggetto che possiede la responsabilità;
3. passare una dipendenza in modo esplicito quando serve;
4. separare dominio da input/file/output;
5. riconoscere una god class;
6. rifattorizzare incrementalmente record/dict verso oggetti quando porta valore;
7. testare una collaborazione tra oggetti;
8. spiegare perché più classi non significa automaticamente design migliore.

## GUIDED EXPOSURE

- list/dict di oggetti;
- fake molto semplice per testare una collaborazione;
- confronto composizione vs inheritance.

## ENRICHMENT / BACKUP

- inheritance minimale come confronto;
- `__str__` diagnostico;
- collaborazioni più articolate.

La composizione è un outcome core del curriculum frozen e deve essere dimostrata prima della fine del track.

---

# Ora teoria attiva 1 — responsabilità e composizione

1. Presentare una classe che fa troppo.
2. Separare due responsabilità nominabili.
3. Costruire relazione “ha/usa un”.
4. Passare l'oggetto collaboratore nel costruttore.
5. Chiedere chi possiede ogni regola.

Esempio:

```text
Missione → obiettivo/checkpoint
Robot    → movimento/stato
```

---

# Ora teoria attiva 2 — dominio, dipendenze e refactor

1. Separare `input/file` dal dominio.
2. Refactoring incrementale dict→object quando il record ha comportamento proprio.
3. God class smell.
4. Testare la collaborazione con un collaboratore reale semplice o un fake minimo.
5. Confrontare brevemente “ha un” vs “è un tipo di” per motivare perché inheritance non è core.

Non aprire gerarchie di classi.

---

# Laboratorio

- responsibilities mapping;
- costruzione di due oggetti collaboranti;
- dipendenza esplicita nel costruttore;
- test della delega/collaborazione;
- refactoring incrementale da record a oggetto;
- Debug Clinic su god class/dipendenza globale/regola nell'oggetto sbagliato.

## Handoff capstone

La parte finale del laboratorio può produrre **lo skeleton del capstone**:

```text
responsabilità
→ classi candidate
→ relazione di composizione
→ invarianti
→ casi
```

Questo è l'avvio del capstone nella settimana 31; M30/week 32 è la fase dedicata di implementazione/integration/review.

---

# Minimum mastery gate — prima di M30

Considerare M29 consolidato quando lo studente riesce a:

- identificare almeno due responsabilità distinte;
- rappresentare una collaborazione “ha/usa un”;
- costruire un oggetto che riceve/usa un collaboratore;
- collocare una regola nell'oggetto responsabile;
- tenere I/O fuori dal nucleo dominio in un esempio semplice;
- riconoscere una god class;
- testare che un oggetto deleghi/collabori correttamente;
- spiegare perché la composizione scelta porta valore.

Collezioni di oggetti, fake e inheritance non devono dominare il gate.

---

# Misconception watchlist

- più classi = più OOP;
- ogni dict deve diventare una classe;
- composizione = mettere un oggetto in un attributo senza responsabilità reale;
- dipendenza globale scambiata per collaborazione;
- I/O sparso nei metodi dominio;
- god class considerata “coordinatore centrale” inevitabile;
- inheritance scelta solo per riuso superficiale.

---

# Differenziazione

## Recupero

- due classi semplici;
- una sola relazione di composizione;
- metodi dominio già parzialmente definiti;
- niente collezioni di oggetti iniziali.

## Enrichment

- list/dict di oggetti;
- fake minimale;
- confronto composizione/inheritance;
- secondo collaboratore solo se il dominio lo richiede.

---

# Evidence docente

Raccogliere:

- responsibilities map;
- relazione di composizione;
- dipendenza esplicita;
- test collaborazione;
- refactor incrementale;
- motivazione del design.

---

# P3 — teacher/delivery boundary

Il futuro P3 potrà testare graph/state di oggetti nel sandbox. Fino alla certificazione usare assert/manual evidence.

Non trasformare il bisogno di autograding in un vincolo sul design studente.

---

# Cosa NON anticipare

- inheritance come core;
- ABC/protocol;
- dependency injection framework;
- mocking framework;
- design pattern formali;
- DI container.

---

# Handoff a M30

M29 produce lo skeleton progettuale.

M30/week 32 completa:

```text
implementazione
→ invarianti
→ composizione
→ test
→ edge case
→ regression/refactor
→ spiegazione
```

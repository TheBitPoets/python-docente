# Review didattica/semantica — PY2-10 + Checkpoint C

> Data: 2026-08-25  
> Scope: M27–M30 + Checkpoint C.  
> Stato: **review editoriale**, non certificazione runtime e non teacher sign-off finale.

## Obiettivo

Verificare che l'OOP di seconda:

- resti modellazione di dati + comportamento, non sintassi decorativa;
- renda `self`, stato e invarianti comprensibili senza internals prematuri;
- privilegi composizione e responsabilità;
- chiuda con un capstone piccolo ma realmente integrato;
- non introduca nuovi prerequisiti nella settimana 33;
- mantenga P3/Romeo come boundary di delivery, non come ostacolo al core.

Regola invariata:

```text
MUST MASTER
→ GUIDED EXPOSURE
→ ENRICHMENT / BACKUP
```

---

# Architettura complessiva

La progressione è didatticamente corretta:

```text
M27  classe / istanza / self / stato indipendente
 ↓
M28  invarianti + transizioni controllate
 ↓
M29  composizione + responsabilità + collaborazione
 ↓
M30  capstone integrato
 ↓
Checkpoint C  finalizzazione / recupero / evidence
```

Composizione prima dell'ereditarietà è la scelta giusta per il secondo anno.

---

# M27 — Classi, istanze, attributi e `self`

## MUST MASTER

1. distinguere classe e istanza;
2. usare `__init__` per inizializzare lo stato essenziale;
3. usare attributi di istanza tramite `self`;
4. definire/chiamare un metodo che usa lo stato;
5. creare due istanze indipendenti;
6. spiegare che `self` è l'istanza corrente della chiamata;
7. scegliere una classe soltanto quando dati e comportamenti formano una responsabilità significativa;
8. distinguere quando una funzione resta il modello più semplice.

## GUIDED EXPOSURE

- bug di stato mutabile condiviso tramite attributo di classe;
- `__str__` come osservabilità;
- confronto con API Romeo procedurale/object-style se runtime certificato.

## ENRICHMENT / BACKUP

- introspezione/printing più ricco;
- metodi aggiuntivi non necessari al modello.

### Finding

Il bug dell'attributo di classe condiviso è utile come Error Clinic, ma non deve far pensare che M27 sia una lezione su class attributes. Il core è stato **per istanza**.

P3 è teacher/delivery-only.

---

# M28 — Stato e invarianti

## MUST MASTER

1. identificare lo stato di un'istanza;
2. distinguere un metodo che osserva da uno che modifica lo stato;
3. scrivere un invariante semplice in linguaggio naturale;
4. costruire l'oggetto in stato valido;
5. validare una transizione prima di applicarla;
6. lasciare lo stato invariato dopo una transizione rifiutata;
7. testare sia return/segnale sia stato risultante;
8. progettare casi di confine suggeriti dall'invariante;
9. mantenere istanze indipendenti.

## GUIDED EXPOSURE

- termini observer/mutator;
- policy alternative di segnalazione del fallimento;
- assert interni come controllo didattico;
- `__str__` per osservabilità.

## ENRICHMENT / BACKUP

- property;
- eccezioni custom;
- invarianti multiple più ricche.

### Finding

`return False` è **una policy didattica possibile**, non la forma OOP obbligatoria. Il mastery riguarda:

```text
transizione valida
→ stato valido
transizione rifiutata
→ stato invariato + segnale coerente col contratto
```

---

# M29 — Composizione e responsabilità

## MUST MASTER

1. spiegare composizione come relazione “ha/usa un”;
2. assegnare regole all'oggetto che possiede la responsabilità;
3. passare una dipendenza in modo esplicito quando serve;
4. separare dominio da input/file/output;
5. riconoscere una god class;
6. rifattorizzare incrementalmente record/dict verso oggetti quando porta valore;
7. testare una collaborazione tra oggetti;
8. spiegare perché più classi non significa automaticamente design migliore.

## GUIDED EXPOSURE

- list/dict di oggetti;
- fake/dipendenza sostitutiva molto semplice per test;
- confronto composizione vs inheritance.

## ENRICHMENT / BACKUP

- inheritance minimale;
- `__str__` diagnostico;
- collaborazioni più articolate.

### Finding

La composizione è **core** e deve essere dimostrata prima della fine del track. Non può diventare opzionale nel Checkpoint C completo.

---

# M30 — Capstone OOP

## Giudizio

Il capstone è correttamente orientato a qualità/responsabilità, non quantità di codice. Va però chiarita la sua finestra e il contratto minimo.

## Finestra reale

```text
M29 / settimana 31
→ skeleton progettuale del capstone

M30 / settimana 32
→ implementazione/integration/review dedicata

Checkpoint C / settimana 33
→ finalizzazione/recupero/evidence, se necessario
```

Quindi “settimane 31–32” significa **handoff M29 + lavoro M30**, non due ulteriori settimane M30 che romperebbero la mappa frozen.

## MUST MASTER / contratto capstone completo

Il capstone deve mostrare in forma proporzionata:

1. almeno due responsabilità OOP significative;
2. collaborazione/composizione reale tra oggetti;
3. almeno un invariante;
4. almeno una scelta di struttura dati motivata;
5. metodi con responsabilità riconoscibili;
6. 5+ casi/test complessivi;
7. almeno un edge case o transizione rifiutata;
8. una evidence di bug-fix/regression/refactor;
9. spiegazione breve delle scelte.

Persistenza file resta **opzionale**: non deve compromettere il capstone se M26 non è sufficientemente consolidato.

## Non forzare

- numero alto di classi;
- inheritance;
- GUI/web/database;
- hardware;
- pytest professionale;
- strutture annidate complesse;
- persistence soltanto per “usare tutto il corso”.

## Recovery

Se uno studente non può completare il capstone pieno, ridurre il **dominio**, non cancellare gli outcome.

Le evidence mancanti possono essere recuperate con micro-task mirati. In particolare la composizione, essendo outcome frozen, deve essere dimostrata almeno in un esercizio/parte separata se il prodotto finale viene ridotto.

---

# Git G1 nel capstone

Il workflow deve restare quello completo già acquisito:

```text
status
→ diff
→ test
→ add
→ diff --staged
→ commit
→ status
→ log/show
```

Non richiedere un numero artificiale di commit. Richiedere checkpoint significativi quando c'è un cambiamento coerente e verificato.

Non introdurre G2.

---

# Checkpoint C — nessun nuovo prerequisito

## Correzione necessaria

La precedente checklist studente consentiva:

> composizione oppure motivazione del perché non serve

Questo è incoerente con il curriculum frozen, che include composizione fra gli outcome obbligatori.

Nuova regola:

- **capstone completo** → composizione/collaborazione obbligatoria;
- **percorso di recupero ridotto** → se il prodotto non la contiene, composizione va dimostrata con evidence separata;
- settimana 33 non introduce però una nuova nozione: recupera/dimostra qualcosa già insegnato in M29.

## Priorità Checkpoint C

1. outcome core mancanti;
2. finalizzazione capstone;
3. bug/regression;
4. evidence;
5. chiarezza di responsabilità/composizione;
6. enrichment solo dopo il core.

---

# P3 / Romeo boundary

P3 è teacher/delivery-only. Il corso può insegnare e valutare manualmente OOP anche senza P3 certificato; ciò che non può fare è promettere object autograding non certificato.

Romeo è una variante applicativa soltanto se `romeo-sim` è certificato. Deve esistere sempre fallback generico equivalente.

---

# Exit outcome annuale

Il traguardo resta:

```text
problema
→ algoritmo
→ funzioni
→ strutture dati
→ classe/istanza
→ stato + invarianti
→ composizione
→ test/debug/refactor
→ spiegazione
```

Non:

```text
più classi + più framework + più righe
```

---

# Esito

```text
PY2-10 architecture/order       PASS
M27 pacing                      PASS with shared-class-state guided
M28 pacing                      PASS with failure-policy generalized
M29 pacing                      PASS; composition remains core
M30 capstone                    PASS after window/contract clarification
Checkpoint C                    REQUIRES composition wording fix
```

Nessun curriculum change richiesto: la correzione del Checkpoint C **ripristina** il curriculum frozen invece di modificarlo.

## Dopo questa review

Il core M04–M30 è semanticamente revisionato UDA per UDA.

Restano i prossimi layer:

1. riallineamento dei documenti di stato/checklist;
2. build/QA reale delle slide artifact;
3. teacher review finale;
4. provenance/coverage finale;
5. Activity planning/materialization per profilo certificato;
6. PY2-01 / Flowchart Lab boundary;
7. CI privata e rehearsal TheBitLab;
8. soltanto dopo: Content Pack `1.0.0 / approved` e GO classroom.

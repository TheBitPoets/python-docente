# M08 — Selezioni annidate, validazione e refactoring

> **Stato:** draft / controlled authoring continuation  
> **UDA:** PY2-03 — Selezione e logica  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine di questo modulo dovresti saper:

- leggere e scrivere una selezione annidata semplice;
- seguire il percorso dei rami con un trace;
- riconoscere quando una seconda decisione dipende davvero dalla prima;
- distinguere annidamento necessario da annidamento accidentale;
- rilevare un input non valido e separare caso valido/non valido;
- progettare casi di test che percorrono i principali path;
- confrontare annidamento e condizione composta quando entrambi sono corretti;
- usare una variabile booleana con un nome quando aggiunge significato;
- semplificare codice senza cambiare il comportamento osservabile;
- spiegare perché una versione è più leggibile o più aderente alla specifica.

## Prerequisiti

Da M06–M07 dovresti già saper:

- costruire `if`, `if/else`, `if/elif/else`;
- distinguere condizioni indipendenti e casi esclusivi;
- usare confronti, `and`, `or`, `not`;
- testare soglie e intervalli;
- individuare rami irraggiungibili o sovrapposti;
- fare il trace del primo ramo vero.

---

# 1. Problema iniziale: una domanda che ha senso solo dopo un'altra

Specifica:

> Prima controlla se le credenziali sono valide. Soltanto se lo sono, controlla se l'account è attivo.

La seconda domanda dipende dalla prima:

```text
credenziali valide?
    no  → accesso negato
    sì  → account attivo?
              no  → account disabilitato
              sì  → accesso consentito
```

Una traduzione diretta è:

```python
if credenziali_valide:
    if account_attivo:
        print("accesso consentito")
    else:
        print("account disabilitato")
else:
    print("accesso negato")
```

Qui l'annidamento rappresenta una **dipendenza reale fra decisioni**.

---

# 2. Che cosa significa “annidare”

Un `if` è annidato quando compare dentro il blocco di un'altra selezione.

```python
if condizione_1:
    if condizione_2:
        ...
```

Il secondo `if` viene raggiunto soltanto quando:

```text
condizione_1 → True
```

Quindi il percorso del programma dipende da più decisioni successive.

---

# 3. Path trace: segui il percorso, non tutto il codice

Programma:

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
    else:
        print("disabilitato")
else:
    print("negato")
```

## Caso A

```text
credenziali_valide = False
account_attivo = True
```

Trace:

```text
credenziali_valide? → False
ramo esterno else   → negato
secondo if           → non raggiunto
```

## Caso B

```text
credenziali_valide = True
account_attivo = False
```

Trace:

```text
credenziali_valide? → True
account_attivo?     → False
ramo interno else   → disabilitato
```

Il trace segue **un path** per volta.

---

# 4. Costruire una tabella dei path

Per due booleani:

| credenziali valide | account attivo | output atteso |
|---|---|---|
| False | False | negato |
| False | True | negato |
| True | False | disabilitato |
| True | True | accesso |

Notare che quando le credenziali non sono valide, il valore di `account_attivo` non cambia il risultato.

Questa tabella ci aiuta a capire la struttura prima del codice.

---

# 5. Annidamento oppure condizione composta?

Specifica più semplice:

> Stampa `accesso` soltanto se credenziali valide **e** account attivo.

Versione annidata:

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

Versione composta:

```python
if credenziali_valide and account_attivo:
    print("accesso")
```

In questa specifica ridotta possono essere equivalenti per l'output richiesto.

La seconda comunica direttamente:

```text
entrambe le condizioni devono essere vere
```

Ma se dobbiamo distinguere anche `credenziali non valide` da `account disabilitato`, l'annidamento o una struttura multi-ramo può rappresentare meglio il dominio.

---

# 6. Meno annidamento non significa automaticamente codice migliore

Evita regole meccaniche come:

```text
meno righe = meglio
meno livelli = sempre meglio
```

Confronta invece:

1. quali casi deve distinguere la specifica;
2. quali condizioni hanno senso solo dopo altre;
3. quali output/comportamenti devono restare differenti;
4. quale struttura rende evidente il percorso.

Il refactoring deve preservare il comportamento richiesto, non soltanto ridurre l'indentazione.

---

# 7. Validazione: separare dati validi e non validi

Problema:

> Leggi un voto tra 0 e 10. Se è fuori intervallo stampa `dato non valido`; altrimenti classificalo.

Per ora sappiamo **rilevare** l'errore:

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
```

Importante:

> non sappiamo ancora ripetere automaticamente la richiesta finché il dato diventa valido.

Quello richiederà `while` in PY2-04.

---

# 8. Validare non significa “mettere un try ovunque”

Nel punto attuale del corso distinguiamo due problemi diversi.

### Valore numerico fuori dal dominio

```text
voto = 12
```

Il dato è un intero, ma non è valido per la nostra specifica `0..10`.

Possiamo rilevarlo con una condizione.

### Testo non convertibile in intero

```text
"ciao"
```

`int("ciao")` produce un errore di conversione.

Non introduciamo ancora `try/except` come nuovo argomento: la gestione programmata delle eccezioni verrà affrontata più avanti.

Per ora i test delle selezioni usano input del tipo già previsto dal contratto.

---

# 9. Worked example: voto valido + classificazione

## Specifica

```text
INPUT: intero
se fuori 0..10 → dato non valido
altrimenti:
  < 6  → insufficiente
  >= 6 → sufficiente
```

## Casi di test

| input | atteso |
|---:|---|
| -1 | dato non valido |
| 0 | insufficiente |
| 5 | insufficiente |
| 6 | sufficiente |
| 10 | sufficiente |
| 11 | dato non valido |

## Codice

```python
voto = int(input())

if voto < 0 or voto > 10:
    print("dato non valido")
else:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
```

I casi `-1`, `0`, `10`, `11` controllano i confini della validità; `5` e `6` controllano la soglia della classificazione.

---

# 10. Variante: condizione di validità nominata

Quando un nome aggiunge significato:

```python
voto_valido = 0 <= voto <= 10
```

Poi:

```python
if voto_valido:
    if voto < 6:
        print("insufficiente")
    else:
        print("sufficiente")
else:
    print("dato non valido")
```

Il nome `voto_valido` rende esplicita una regola del dominio.

Non trasformiamo però ogni confronto in una variabile booleana: il nome deve spiegare qualcosa.

---

# 11. Refactoring controllato: stessi test prima e dopo

Supponiamo che questo comportamento sia sufficiente:

```python
if credenziali_valide:
    if account_attivo:
        print("accesso")
```

Possibile refactoring:

```python
if credenziali_valide and account_attivo:
    print("accesso")
```

Prima di dire che il refactoring è corretto:

1. conserva i casi di test;
2. esegui mentalmente o realmente gli stessi input;
3. verifica che output/comportamento restino uguali;
4. spiega quale versione comunica meglio l'intenzione.

Il test non serve solo a trovare bug nuovi: protegge anche durante le modifiche.

---

# 12. Error Clinic: annidamento che cambia il significato

Specifica:

> se piove stampa `ombrello`; se fa freddo stampa `giacca`. I due effetti possono coesistere.

Bug:

```python
if piove:
    if fa_freddo:
        print("giacca")
    print("ombrello")
```

Se `fa_freddo` è True ma `piove` è False, `giacca` non viene mai stampato.

L'annidamento ha introdotto una dipendenza che la specifica non aveva.

Corretto per effetti indipendenti:

```python
if piove:
    print("ombrello")

if fa_freddo:
    print("giacca")
```

---

# 13. Error Clinic: ramo valido nel posto sbagliato

Bug:

```python
if voto < 6:
    print("insufficiente")
else:
    if voto < 0 or voto > 10:
        print("dato non valido")
    else:
        print("sufficiente")
```

Con `voto = -1`:

```text
voto < 6 → True
```

quindi viene stampato `insufficiente` prima ancora di controllare che il dato sia fuori dominio.

La validazione deve avvenire **prima** della classificazione se la classificazione ha senso solo per valori validi.

---

# 14. Error Clinic: condizione composta che perde informazioni

Versione:

```python
if credenziali_valide and account_attivo:
    print("accesso")
else:
    print("negato")
```

È corretta se la specifica distingue soltanto:

```text
accesso / non accesso
```

Non è sufficiente se dobbiamo distinguere:

```text
credenziali errate
account disabilitato
```

Una semplificazione sintattica può perdere informazioni richieste dal dominio.

---

# 15. Path coverage: quali percorsi abbiamo davvero provato?

Per una selezione annidata non basta dire “ho fatto tre test”.

Chiediti:

```text
quali path del diagramma/codice percorrono?
```

Esempio credenziali/account:

```text
P1 → credenziali false
P2 → credenziali true, account false
P3 → credenziali true, account true
```

Questi tre path coprono i tre risultati distinti.

La combinazione `credenziali false, account true` può essere utile per confermare che il secondo dato è irrilevante quando la prima decisione fallisce.

---

# 16. De Morgan: solo una lente, non un capitolo

A volte incontreremo negazioni come:

```python
not (eta >= 18 and biglietto_valido)
```

Esistono regole logiche per trasformare condizioni negate, ma in questa fase non facciamo algebra booleana formale.

Regola pratica:

> se una condizione è difficile da leggere, prima riscrivila in linguaggio naturale e verifica i casi; non cercare una forma “furba”.

Eventuali equivalenze di De Morgan vengono usate soltanto come piccoli esempi guidati.

---

# 17. Microscope: dipendenza reale o accidentale?

Per ogni coppia di regole decidi se la seconda dipende dalla prima.

### A

```text
se utente autenticato, allora controlla se ha permesso admin
```

### B

```text
se piove, ombrello; se freddo, giacca
```

### C

```text
se voto valido, allora classificalo
```

### D

```text
se ha completato quiz, badge; se ha completato progetto, bonus
```

Prima descrivi la relazione; poi scegli annidamento, condizione composta o `if` indipendenti.

---

# 18. Activity planning — M08

Candidati, non ancora materializzati come nuove Activity P1 obbligatorie:

### A — Path trace

Dato codice annidato, segnare il percorso seguito per più input.

### B — Controlled refactor

Trasformare un annidamento ridondante in una condizione composta, mantenendo gli stessi test.

### C — Implement

Problema con:

- validazione iniziale;
- almeno tre casi validi;
- output deterministico;
- tabella dei casi prima del codice.

### D — Debug Clinic

Correggere validazione tardiva, dipendenza accidentale o ramo mancante.

### E — Mini-project

Configuratore/regole semplici:

1. input/output/vincoli;
2. flow chart o pseudocodice;
3. tabella casi/path;
4. implementazione;
5. test;
6. spiegazione della struttura scelta.

M04 resta il canarino P1 fino alla certificazione `python-docente#7`.

---

# 19. Romeo come problema di path/refactoring

Romeo resta opzionale.

Un uso sensato in M08 è confrontare due modi di esprimere regole di una missione simulata:

```text
prima valida un parametro
→ poi scegli un comportamento
```

oppure fare il path trace di una missione già nota.

Vincoli:

- niente hardware necessario;
- niente nuove API avanzate;
- niente networking;
- nessuna Activity Romeo duplicata nel repo Python;
- `romeo-sim` solo quando certificato.

---

# 20. Mini-project: classificatore validato

Specifica candidata:

> Leggi un punteggio intero tra 0 e 100. Se non è valido stampa `errore`. Se è valido, classificalo in tre fasce definite dalla consegna.

Deliverable:

```text
input/output/vincoli
flow chart o pseudocodice
tabella casi
codice
trace di un path
spiegazione di una scelta strutturale
```

Non serve un progetto grande: il valore è integrare analisi, selezione, test e refactoring.

---

# 21. Checkpoint M08 / uscita PY2-03

Senza eseguire Python, spiega:

1. Quando un `if` annidato rappresenta una dipendenza reale?
2. Perché l'annidamento pioggia → freddo sarebbe sbagliato se i due effetti sono indipendenti?
3. Perché validiamo un voto prima di classificarlo?
4. In questa fase, che cosa facciamo con un voto fuori `0..10`?
5. Perché non ripetiamo ancora automaticamente l'input?
6. Quando `if A: if B:` può essere sostituito da `if A and B:` senza perdere comportamento richiesto?
7. Che cosa significa preservare i test durante un refactoring?
8. Perché una variabile come `voto_valido` può migliorare la leggibilità?
9. Che cosa significa coprire i principali path?

---

# 22. Sintesi

Porta con te questi modelli:

```text
annidamento → una decisione dipende da un'altra
```

```text
validazione → prima stabilisci se il dato appartiene al dominio
```

```text
refactoring → cambia struttura, preserva comportamento
```

```text
test/path → proteggono anche durante le modifiche
```

```text
leggibilità → il codice deve comunicare la regola del problema
```

La prossima UDA introduce la ripetizione: useremo `while` per ripetere una richiesta finché una condizione cambia e `for` quando il numero/insieme delle iterazioni è noto.

---

# Fonti e riferimenti docente

Questa lesson è materiale originale del corso. Per progettazione/verifica:

- documentazione Python 3.12 — control flow, Boolean operations e comparisons;
- Allen Downey, *Think Python / Pensare in Python* — conditional execution, nested conditionals, debugging;
- Mark Lutz, *Learning Python / Imparare Python* — statement nesting, Boolean logic e control flow;
- Romeo pinned `45e5f7e131802fccc89358a23a25dbed1884bbfa` — riferimento applicativo selettivo.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.

## Collegamenti di progettazione

- `tracks/secondo/PY2_03_SPEC.md`;
- `tracks/secondo/ASSESSMENT_CALENDAR.md`;
- `tracks/secondo/ROMEO_MAPPING.md`;
- `doc/CURRICULUM_FREEZE_2026_2027.md`;
- `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

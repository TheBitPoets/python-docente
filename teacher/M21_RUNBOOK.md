# M21 — Runbook docente

## Modulo

**Alias, copie, filtri e ordinamento delle liste**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Rendere aliasing e mutabilità un modello mentale osservabile:

```text
nome → oggetto
altro nome → stesso oggetto oppure nuova lista?
mutazione → chi la vede?
```

Non serve formalizzare memoria, heap o reference graph. Serve prevedere correttamente gli effetti delle mutazioni.

---

# Priorità didattica

## MUST MASTER

1. `b = a` crea un altro nome per lo stesso oggetto list;
2. prevedere una mutazione osservata tramite alias;
3. creare una nuova lista esterna con `.copy()` o slicing;
4. distinguere alias vs copia per liste piatte;
5. evitare rimozione ingenua mentre si itera sulla stessa lista;
6. costruire una nuova lista filtrata/trasformata con loop esplicito;
7. distinguere `sort()` in-place da `sorted()` nuova lista;
8. verificare il contratto mutazione/non-mutazione con test.

## GUIDED EXPOSURE

- shallow copy su una struttura annidata;
- iterare su una copia quando la mutazione dell'originale è davvero richiesta;
- intuizioni qualitative sul costo di ricerca/inserimento.

## ENRICHMENT / BACKUP

- comprehension dopo il loop equivalente;
- più API di inversione;
- confronto fra contratti in-place e new-result;
- nested alias più articolato.

`deepcopy` non è core.

---

# Ora teoria attiva 1 — alias e copia

1. `b = a` con diagramma due nomi → un oggetto.
2. Mutare tramite `b` e prevedere che cosa vede `a`.
3. `b = a.copy()` / `b = a[:]` e nuova previsione.
4. Testare la promessa “non mutare l'input”.

Soltanto se il modello piatto è stabile, mostrare una shallow copy annidata come **guided exposure**.

Domanda da ripetere:

> quali contenitori sono nuovi e quali oggetti sono ancora condivisi?

Non serve introdurre terminologia più profonda.

---

# Ora teoria attiva 2 — trasformare senza mutazioni accidentali

1. Rimuovere durante `for` sulla stessa lista: trace del bug.
2. Costruire una nuova lista filtrata.
3. Trasformare costruendo una nuova lista.
4. `sort()` vs `sorted()`.
5. Testare sia risultato sia input quando il contratto parla di mutazione.

Performance intuitiva resta sullo sfondo: prima correttezza e contratto.

---

# Laboratorio

- alias microscope;
- filtro sicuro che preserva input;
- assert sull'originale;
- debug `.sort()` assegnato;
- una trasformazione con nuova lista;
- massimo progressivo modernizzato senza usare `max` come nome variabile.

Il confronto di più API per l'inversione può essere enrichment, non deve comprimere alias/copia/sort.

---

# Minimum mastery gate — prima di M22

Considerare M21 consolidato quando lo studente riesce a:

- disegnare due nomi che puntano alla stessa lista;
- prevedere l'effetto di una mutazione tramite alias;
- creare e riconoscere una copia esterna indipendente per lista piatta;
- spiegare perché rimuovere mentre si itera può saltare elementi;
- filtrare costruendo una nuova lista;
- distinguere `sort()` e `sorted()`;
- scrivere un test che verifica che l'input non venga mutato quando il contratto lo promette.

La semantica completa della shallow copy annidata non deve essere un requisito discriminante del gate.

---

# Misconception watchlist

- assegnamento = copia;
- `.copy()` = duplicazione ricorsiva infinita;
- rimozione durante `for` sempre sicura;
- `sort` produce nuova lista;
- comprehension obbligatoria perché “più Pythonica”;
- testare solo il valore restituito senza verificare effetti collaterali;
- confondere il modello beginner “stesso oggetto” con dettagli implementativi non ancora studiati.

---

# Differenziazione

## Recupero

- liste piatte;
- diagrammi nome→oggetto;
- una mutazione per trace;
- `.copy()` senza nested structures;
- filtro in nuova lista.

## Enrichment

- shallow nested;
- `copy()` vs slice;
- comprehension dopo loop equivalente;
- quando mutare input è un contratto legittimo;
- più modi per invertire una lista.

---

# Evidence docente

Raccogliere:

- diagramma alias;
- previsione di una mutazione;
- test di non-mutazione;
- filtro sicuro;
- spiegazione `sort`/`sorted`.

---

# Friedpython

- massimo: riusabile solo riscritto (`massimo`, non `max`);
- conteggio pari: buon candidato;
- inversione: utile come confronto new-object vs in-place;
- frequenze ASCII: rinviate a dict M24.

Ogni riuso resta subordinato ad audit individuale.

---

# Cosa NON anticipare

- `copy.deepcopy` come requisito;
- hashing/set/dict;
- generatori;
- NumPy;
- complexity formale;
- modello CPython della memoria.

---

# Handoff a M22

M21 chiarisce:

```text
stesso oggetto?
nuovo contenitore?
chi vede la mutazione?
```

M22 riusa queste idee per:

```text
tuple stabili
+ unpacking
+ liste annidate
+ matrici
+ righe condivise
```

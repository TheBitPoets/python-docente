# M20 — Runbook docente

## Modulo

**Liste: mutabilità, metodi essenziali e iterazione**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Usare il contrasto con `str` per introdurre la mutabilità senza presentare le liste come un catalogo di metodi.

Modello target:

```text
nome → oggetto list mutabile
operazione mutante → cambia quell'oggetto
```

---

# Priorità didattica

## MUST MASTER

1. `str` immutabile vs `list` mutabile;
2. creare/accedere/modificare una lista per indice;
3. usare `append()` per costruire progressivamente una lista;
4. capire che un metodo mutante cambia l'oggetto e spesso restituisce `None`;
5. diagnosticare `lista = lista.append(x)`;
6. iterare direttamente sugli elementi;
7. usare l'indice soltanto quando la posizione serve;
8. costruire una lista da N valori;
9. usare membership `in`.

## GUIDED EXPOSURE

- `extend()`;
- `remove()` vs `pop()`;
- `enumerate()`;
- slicing di lista come nuova lista superficiale.

## ENRICHMENT / BACKUP

- `insert()`;
- slice assignment;
- confronto concatenazione/extend.

Non serve memorizzare cinque metodi di modifica per capire la mutabilità.

---

# Ora teoria attiva 1 — da `str` a `list`

1. Contrasto `str` vs `list`.
2. Creazione, indice, slicing già noti dalle stringhe.
3. Mutazione per indice.
4. `append()` come operazione core.
5. Prediction sul bug `lista = lista.append(x)`.

Domanda ricorrente:

> questa operazione crea un nuovo valore o modifica l'oggetto esistente?

---

# Ora teoria attiva 2 — scegliere poche operazioni

1. Iterazione diretta sugli elementi.
2. Indice soltanto quando la posizione è parte del problema.
3. Membership `in` come riuso M18.
4. `extend()` e `remove/pop` come guided exposure su specifiche concrete.
5. `enumerate()` soltanto se servono davvero indice e valore.

`insert()` non merita tempo core se la classe deve ancora consolidare mutabilità/append/iterazione.

---

# Laboratorio

- prediction di sequenze di mutazioni;
- debug `lista = lista.append(...)`;
- costruzione lista da N input;
- confronto `for` diretto vs indice;
- uno scenario guidato `append/extend` o `remove/pop`;
- calcolo di proprietà già note su una lista raccolta.

Il laboratorio deve far riusare M11, non introdurre una collezione di nuove API.

---

# Minimum mastery gate — prima di M21

Considerare M20 consolidato quando lo studente riesce a:

- spiegare la differenza `str`/`list` sul piano della mutabilità;
- prevedere una modifica per indice;
- costruire una lista con `append`;
- spiegare perché `append` non va assegnato alla stessa variabile;
- attraversare una lista con `for` diretto;
- scegliere quando serve un indice;
- usare `in` su una lista;
- raccogliere N input e riutilizzarli successivamente.

`insert`, `extend`, `remove`, `pop`, `enumerate` non devono essere tutti ricordati a memoria per passare a M21.

---

# Misconception watchlist

- lista come “stringa con parentesi”;
- metodi mutanti pensati come funzioni che restituiscono la lista;
- `append` e `extend` considerati sinonimi;
- `remove` usato con un indice;
- indice usato sempre perché sembra più tecnico;
- slice interpretato come vista live invece di nuova lista superficiale;
- memorizzare API senza collegarle a una specifica.

---

# Differenziazione

## Recupero

- liste di 3–5 valori;
- `append` come unico metodo iniziale;
- prediction prima dell'esecuzione;
- `for` diretto prima di indice/enumerate.

## Enrichment

- `extend` vs concatenazione;
- `insert` giustificato dal requisito;
- `remove/pop` su casi controllati;
- `enumerate` come coppia indice/valore;
- slice assignment.

---

# Evidence docente

Raccogliere:

- prediction di una mutazione;
- debug `lista = lista.append(...)`;
- iterazione scelta e motivata;
- costruzione progressiva di lista;
- almeno una scelta di operazione spiegata dalla specifica.

---

# Friedpython

Usare soltanto come source pack auditato. Gli esercizi 1–2 sono buoni per il confronto tra indice e iterazione diretta; non importare automaticamente codice/commenti legacy.

---

# Cosa NON anticipare

- aliasing annidato prima di M21;
- comprehensions come forma primaria;
- set/dict;
- type hints generici;
- NumPy.

---

# Handoff a M21

M20 mostra che la lista può cambiare.

M21 risponde:

> se due nomi indicano la stessa lista, chi vede la mutazione? E quando ho davvero creato una copia?

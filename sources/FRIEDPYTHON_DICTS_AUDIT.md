# `friedpython` — audit dizionari per PY2-08

Snapshot:

```text
TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f
```

Scopo: classificare spunti M24–M25 senza copiare materiale legacy.

## File concettuali

### `dizionari/operazioni_di_base.py`

Spunti validi:

- mapping chiave→valore;
- accesso/assegnamento/cancellazione;
- chiavi hashable;
- `keys`, `values`, `items`;
- membership sulle chiavi;
- `get`/`pop`/`update` come panoramica.

Da correggere/riscrivere:

- descrizioni Python 2 vs 3 ormai storiche;
- `dict.keys()` in Python 3 restituisce una **view**, non una lista e non va descritta genericamente come iteratore monouso;
- l'ordine di inserimento dei `dict` è garantito dai Python moderni (language guarantee da 3.7); non propagare note che descrivono ordine arbitrario/ignoto;
- separare metodi core da metodi che possono sovraccaricare un beginner.

### `dizionari/gestire_errore_chiave_mancante.py`

Spunti validi:

- accesso con `[]` e `KeyError`;
- membership prima dell'accesso;
- `get()` e default;
- `setdefault()` come tecnica possibile.

Uso didattico:

- M24 deve distinguere chiaramente **chiave obbligatoria** vs **chiave opzionale/default**;
- `get()` non deve essere un rituale automatico che nasconde errori di modello;
- `setdefault()` può essere enrichment dopo il pattern frequenze base.

### `dizionari/iterare_un_dizionario.py`

Spunti validi:

- `for k in d` itera sulle chiavi;
- `d.items()` è la forma naturale per chiave+valore.

Da riscrivere:

- output/esempi basati su ordine non deterministico sono obsoleti per il baseline corrente;
- evitare di presentare conversioni `list(keys())` come necessarie per una normale iterazione.

### `dizionari/dizionari_matrici_sparse.py`

Buon enrichment M25/futuro:

- tuple `(riga, colonna)` come chiavi;
- dict come rappresentazione sparsa;
- `get((r,c), 0)` per celle assenti.

Non core M24: prima lookup chiave→valore, frequenze e record; poi matrice sparsa come confronto di data modeling.

---

# Esercizi dizionari

## Esercizio 1 — inglese→italiano

**Classificazione:** M24 Activity A/B candidate.

Buono per creare/inserire/leggere mapping semplice. Nella riscrittura non fissare l'apprendimento sulla stampa letterale del repr del dict.

## Esercizio 2 — iterazione chiave/valore

**Classificazione:** M24 Activity A.

Modernizzare preferendo anche `for chiave, valore in d.items()` quando servono entrambi.

## Esercizio 3 — keys/values

**Classificazione:** M24 microscope.

Usare per spiegare views e differenza tra iterare direttamente e materializzare una `list` solo se serve davvero.

## Esercizio 4 — completa mapping da due liste parallele

**Classificazione:** M25 data-model comparison.

Valore didattico: mostra fragilità/complessità delle liste parallele e prepara il passaggio a strutture più esplicite. L'uso di `enumerate` è coerente col percorso; `zip` può essere enrichment futuro.

## Esercizio 5 — frequenze caratteri

**Classificazione:** ottimo M24 core candidate, da riscrivere.

Pattern:

```python
d[carattere] = d.get(carattere, 0) + 1
```

È il confronto naturale con il vecchio esercizio liste ASCII-256, che viene superato da un modello Unicode-friendly chiave→conteggio.

## Esercizio 6 — frequenza → lista di caratteri

**Classificazione:** M25 combined-structures candidate.

Dizionario con valori-lista: ottimo per mostrare strutture composte e accumulo per chiave. Richiede però che M20–M24 siano già stabili.

---

# Set

`friedpython` non offre un blocco equivalente significativo per `set`; M23 sarà quindi materiale originale.

Il set va introdotto da operazioni dominanti reali:

- unicità;
- membership;
- deduplicazione quando l'ordine non è requisito;
- unione/intersezione/differenza come operazioni su insiemi.

Non presentare `set` come “lista senza duplicati”: cambia semantica, non solo contenuto.

---

# Regole per PY2-08

1. M23: `set` da unicità/membership, senza promesse di ordine utile.
2. M24: `dict` da mapping/lookup/frequenze; distinzione chiave obbligatoria vs optional/default.
3. M25: combinazioni (`dict` di liste, lista di dict, dict di dict soltanto se serve) e scelta struttura.
4. L'ordine di inserimento dei dict può essere osservato, ma non va usato come surrogato di una struttura scelta per ordinamento/posizione.
5. Frequenze: confrontare concettualmente lista ASCII legacy vs dict Unicode-friendly.
6. Matrice sparsa: enrichment dopo tuple+dict, non core iniziale.
7. Ogni esercizio legacy va riscritto con contratto, casi, nomi moderni, starter/solution ed evidence.

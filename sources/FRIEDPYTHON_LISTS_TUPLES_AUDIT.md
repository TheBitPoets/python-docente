# `friedpython` — audit liste/tuple per PY2-07

Snapshot analizzato:

```text
TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f
```

Scopo: classificare materiale legacy utile per **M20–M22** senza import/copia automatica.

## File concettuali liste

### `liste/operazioni_di_base.py`

**Spunti utili:** creazione, `len`, concatenazione, ripetizione.

**Da riscrivere:** esempi/errori vanno contestualizzati; evitare di presentare concatenazione come modo primario di aggiungere elementi quando `append/extend` esprimono meglio l'intenzione.

### `liste/chiamate_ai_metodi_lista.py`

**Spunti utili:** `append`, `extend`, `insert`, `pop`, `del`, `reverse`, `sort`, `sorted`, `index`; distinzione metodi mutanti vs funzioni che producono nuovi risultati.

**Punto molto utile per M20/M21:** `append()` e `sort()` modificano la lista e restituiscono `None`; quindi pattern tipo `L = L.append(x)` è un bug fondamentale da diagnosticare.

**Da modernizzare:** lunga nota comparativa Python 2.6/3.0 non appartiene al corso 2026/27; spelling/commenti legacy; esempi di comprehension non devono guidare l'ordine didattico.

### `liste/assegnamento_tramite_indirizzamento_e_sezionamento.py`

**Spunti utili:** mutazione per indice e slice assignment; differenza fra sostituzione/estensione/cancellazione.

**Uso:** M20 come enrichment dopo mutazione elementare; non sovraccaricare il primo contatto con slice assignment avanzato.

### `liste/indirizzamento_sezionamento_e_matrici.py`

**Spunti utili:** indice, slice che crea nuova lista superficiale, liste annidate come rappresentazione tabellare/matrice.

**Uso:** ponte M20 → M22.

### `liste/iterarioni_ed_espressioni_di_mappature.py`

**NON riusare direttamente.** Contiene:

- comprehension prima del nostro ordine curricolare;
- descrizione di `map()` come funzione che restituisce una lista, non corretta per Python 3 (restituisce un iteratore);
- typo/errori nel codice (`asb`, `-2-3`);
- terminologia/spelling legacy.

Eventuali comprehension saranno enrichment solo dopo padronanza dei loop espliciti.

---

# Esercizi liste

## Esercizio 1 — `while` + indice

**Classificazione:** candidato M20 / Activity A-B.

Valore didattico: confrontare iterazione manuale per indice con iterazione diretta. Non presentarlo come stile preferito se la posizione non serve.

## Esercizio 2 — `for` diretto sugli elementi

**Classificazione:** candidato M20 / Activity A-B.

Ottimo da affiancare all'esercizio 1: stessa osservazione della lista, due modelli; scegliere quello che comunica meglio l'intenzione.

## Esercizio 3 — massimo senza `max()`

**Classificazione:** candidato M21 / Activity C-D, con riscrittura.

Problema: usa `max` come nome variabile, oscurando la built-in `max()`. Nella riscrittura usare `massimo` e collegare l'invariante già appreso in M11.

## Esercizio 4 — conteggio dei pari

**Classificazione:** candidato M21 / Activity B-C.

Buono per riusare contatore + `if` su dati conservati in lista. L'output della futura Activity deve seguire un contratto esplicito, non una frase hardcoded se non è parte del requisito.

## Esercizio 5 — lista inversa

**Classificazione:** candidato M21 / comparison exercise.

Ottimo per confrontare:

- costruzione manuale;
- `reversed()` + `list()`;
- slicing `[::-1]`;
- `reverse()` in-place.

Il focus deve essere **nuova lista vs mutazione della lista originale**, non la forma più corta.

## Esercizio 6 — tabella ASCII 256 per frequenze

**Classificazione:** NON core PY2-07; conservare come caso storico/anti-pattern e possibile enrichment dopo M24.

Motivi:

- assume un universo ASCII 0..255 mentre Python `str` è Unicode;
- usa una lista indicizzata dal codice del carattere come mappa artificiale;
- anticipa un problema di frequenze che verrà modellato più naturalmente con `dict` in PY2-08/M24;
- può diventare un buon confronto futuro “lista indicizzata vs dizionario”, non un primo esercizio liste.

---

# Tuple legacy

## `tuple/conversioni_metodi_immutabilita.py`

**Spunti utili:** immutabilità, `list()`/`tuple()`, `sorted()` restituisce lista, `index`, `count`, oggetti mutabili annidati.

**Uso:** M22; il caso tupla contenente lista è enrichment dopo aver capito l'immutabilità del contenitore al primo livello.

**Da evitare nel core iniziale:** comprehension e catene di conversione presentate prima del motivo per scegliere una tupla.

## `tuple/esempi_uso.py`

**Spunti utili:** concatenazione, ripetizione, indexing/slicing, tupla a un elemento `(x,)`.

**Da riscrivere completamente:** usa sintassi `print T` Python 2 e contiene note storiche/formulazioni da non propagare senza verifica.

---

# Regole per PY2-07

1. Lesson canoniche originali, nessun copy/paste legacy.
2. Liste introdotte come **sequenze mutabili**, in contrasto esplicito con `str`.
3. M20: creazione/accesso/mutazione/metodi essenziali/iterazione.
4. M21: alias vs copia, metodi mutanti/`None`, search/filter/aggregate/sort e confronto in-place vs nuova lista.
5. M22: tuple, packing/unpacking, liste di liste e matrici; alias delle righe come misconception obbligatoria.
6. Comprehension solo enrichment dopo loop equivalente.
7. Esercizio ASCII frequenze rinviato a M24 come confronto di data modeling.
8. Ogni candidato legacy deve essere riscritto con contratto, casi limite, starter/solution ed evidence moderni prima di diventare Activity.

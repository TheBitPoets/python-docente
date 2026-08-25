# M21 — Runbook docente

## Modulo

**Alias, copie, filtri e ordinamento delle liste**  
UDA PY2-07 — Liste, tuple e dati tabellari

Stato: draft editoriale controllato.

## Obiettivo docente

Rendere aliasing e mutabilità un modello mentale osservabile:

```text
nome → oggetto
altro nome → stesso oggetto oppure copia?
mutazione → chi la vede?
```

## Ora teoria attiva 1 — alias e copia

1. `b = a` con diagramma due nomi → un oggetto.
2. `b = a.copy()` e slicing.
3. Test di mutazione su alias vs copia.
4. Shallow copy annidata come sorpresa controllata.

## Ora teoria attiva 2 — filtri e ordinamento

1. Mutazione durante iterazione: perché può saltare elementi.
2. Costruzione di nuova lista filtrata.
3. `sort()` vs `sorted()`.
4. Contratto di mutazione/non-mutazione.
5. Performance intuitiva di ricerca/inserimento senza Big-O.

## Laboratorio

- alias microscope;
- safe filtering;
- funzione che non muta input + assert sull'originale;
- debug `.sort()` assegnato;
- confronto reverse/manual/reversed/slicing;
- massimo progressivo modernizzato senza usare `max` come variabile.

## Misconception watchlist

- assegnamento = copia;
- `.copy()` = copia profonda ricorsiva;
- rimozione durante `for` sempre sicura;
- `sort` produce nuova lista;
- comprehension obbligatoria perché “più Pythonica”;
- testare solo il valore restituito senza verificare effetti collaterali.

## Differenziazione

### Recupero

- liste piatte;
- diagrammi riferimento/oggetto;
- una mutazione per trace;
- niente shallow nested finché alias semplice non è stabile.

### Enrichment

- shallow nested;
- confronto `copy()`/slice;
- comprehension dopo loop equivalente;
- discutere quando mutare input è un contratto legittimo.

## Evidence docente

Raccogliere:

- diagramma alias;
- previsione di una mutazione;
- test di non-mutazione;
- filtro sicuro;
- spiegazione sort/sorted.

## Friedpython

- esercizio 3 massimo: riusabile solo riscritto (`massimo`, non `max`);
- esercizio 4 conteggio pari: buon candidato;
- esercizio 5 inversione: ottimo confronto nuovo oggetto vs in-place;
- esercizio 6 ASCII frequenze: rinviato a M24/dict, non core liste.

## Cosa NON anticipare

- `copy.deepcopy` come requisito;
- hashing/set/dict;
- generatori;
- NumPy;
- complexity formale.

## Handoff a M22

M21 chiarisce riferimenti e copie. M22 usa queste idee per:

```text
tuple stabili
+ packing/unpacking
+ liste annidate
+ matrici
+ aliasing delle righe
```

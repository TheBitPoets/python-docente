# Checkpoint B — Stringhe, liste, tuple e dati tabellari

> Stato: **draft controllato**. Settimana 24; non introduce nuovi prerequisiti.

## Scopo

Consolidare il secondo blocco del corso:

```text
stringhe
→ liste
→ mutabilità
→ alias/copie
→ tuple/unpacking
→ dati tabellari/matrici
```

Il checkpoint può ospitare recupero, mini-project e parte della preparazione alla prova teorico/scritta V3.

## Competenze da verificare

Devi saper:

- usare `str` come sequenza immutabile;
- usare indici/slicing e casi limite;
- scegliere membership/metodi/loop;
- normalizzare testo consapevolmente;
- usare liste e metodi essenziali;
- distinguere mutazione e nuovo valore;
- spiegare alias vs copia superficiale;
- evitare mutazioni strutturali ingenue durante iterazione;
- usare `sort()` vs `sorted()`;
- usare tuple e unpacking;
- scegliere list vs tuple;
- costruire/attraversare una lista di liste;
- diagnosticare righe alias in una matrice;
- usare funzioni e test su queste strutture.

## Mini-project candidato

Un piccolo **registro/tabella dati** con:

- input già controllato o fixture fornita;
- almeno una stringa da normalizzare;
- una lista principale;
- tuple o righe tabellari quando appropriate;
- almeno 3 funzioni;
- ricerca/aggregazione;
- almeno 5 casi di test/assert;
- spiegazione della struttura dati scelta.

Il dominio può essere voti, temperature, posti, prodotti o altro problema equivalente.

## Error Clinic obbligatoria

Riconosci almeno uno dei seguenti bug:

- metodo mutante assegnato (`lista = lista.append(...)` / `sort()`);
- alias involontario;
- rimozione mentre iteri;
- indice/slice errato;
- matrice costruita con righe condivise;
- tupla/lista scelta senza coerenza col requisito.

## Preparazione V3

La prova teorico/scritta successiva potrà chiedere:

- trace su stringhe/liste;
- mutabilità e alias;
- output/errore previsto;
- scelta list vs tuple;
- confronto di due soluzioni;
- correzione di bug;
- motivazione della struttura.

## Git

Git resta workflow di processo:

```text
status → diff → test → commit significativo
```

Non introduce nuovi comandi G2 in questo checkpoint.

## Dopo il checkpoint

Entrano strutture con semantiche diverse dalla semplice sequenza:

```text
set  → unicità / membership
 dict → chiave → valore / lookup
```

La domanda diventa:

> quale struttura rende naturali le operazioni dominanti del problema?

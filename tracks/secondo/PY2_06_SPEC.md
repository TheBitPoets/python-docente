# PY2-06 — Stringhe come sequenze e testo

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 18–20;
- monte ore nominale: 9 ore;
- prerequisiti: funzioni, cicli, selezione e testing di base;
- baseline: Python 3.12;
- output: lo studente tratta `str` come sequenza immutabile, sa indicizzare/affettare/iterare, scegliere tra loop e metodi built-in, normalizzare/validare/elaborare testo e costruire funzioni testabili su stringhe.

## Perché questa UDA esiste

Una stringa non è soltanto "testo da stampare". È una struttura ordinata su cui si possono eseguire algoritmi.

La domanda guida è:

```text
che operazione devo fare sul testo?
→ accesso posizionale?
→ ricerca/membership?
→ scansione completa?
→ normalizzazione?
→ trasformazione?
→ parsing?
→ quale metodo o algoritmo comunica meglio l'intenzione?
```

---

# M17 — `str`: indici, slicing e immutabilità

## Obiettivi osservabili

Lo studente sa:

1. descrivere una stringa come sequenza ordinata immutabile di testo Unicode a livello beginner;
2. usare `len()`;
3. usare indici da `0`;
4. usare indici negativi;
5. leggere e scrivere slicing `start:stop`;
6. capire che lo `stop` è escluso;
7. usare uno step semplice quando porta valore;
8. spiegare perché `testo[0] = ...` non è ammesso;
9. creare una nuova stringa invece di modificare quella esistente;
10. iterare carattere per carattere con `for`;
11. scegliere tra iterazione diretta e iterazione per indice;
12. diagnosticare `IndexError` e slicing fuori range senza confonderli.

## Modello mentale

Per:

```python
parola = "python"
```

visualizzare:

```text
indice       0  1  2  3  4  5
             p  y  t  h  o  n
indice neg. -6 -5 -4 -3 -2 -1
```

Lo slicing crea una **nuova** stringa.

## Accesso per valore vs indice

Preferire:

```python
for carattere in testo:
    ...
```

quando serve soltanto il carattere.

Usare indice quando la posizione è parte del problema:

```python
for i in range(len(testo)):
    ...
```

La scelta deve avere una ragione, non essere un'abitudine.

## Unicode: modello corretto ma leggero

Core studente:

> `str` rappresenta testo Unicode.

Teacher note/enrichment:

> un elemento indicizzato Python corrisponde a un code point; un simbolo visibile umano può in casi complessi essere composto da più code point. Non usare questa complessità per confondere il beginner, ma non affermare che ogni glifo visibile è sempre un singolo indice.

`bytes`/`bytearray` vengono citati soltanto come tipi distinti per dati binari e rinviati al percorso avanzato/file/networking.

## Letterali

Consolidare senza trasformare la UDA in catalogo sintattico:

- apici singoli/doppi;
- escape `\n`, `\t`, `\\`, virgolette;
- triple quote per testo multilinea quando serve;
- raw string come preview mirata, non prerequisito.

## Activity candidate

### A — Index/slice microscope

Prevedere risultato o errore per piccoli accessi/slice.

### B — Controlled Change

Cambiare intervallo di slicing e spiegare inclusione/esclusione.

### C — Implement

Funzione che estrae/ricompone parti di un codice testuale.

### D — Debug

- indice fuori range;
- stop sbagliato;
- tentativo di mutazione;
- uso dell'indice quando serviva il carattere;
- variabile indice riutilizzata male.

---

# M18 — Ricerca, membership, conteggio e metodi di trasformazione

## Obiettivi osservabili

Lo studente sa:

- usare `in` / `not in`;
- usare `find()` consapevole del valore `-1`;
- usare `count()` quando il problema è davvero contare occorrenze non sovrapposte secondo la semantica del metodo;
- usare `lower()`, `upper()`, `casefold()` solo con spiegazione appropriata; `lower()` core, `casefold()` enrichment/teacher correctness;
- usare `strip()`/`lstrip()`/`rstrip()`;
- usare `replace()`;
- usare `startswith()` / `endswith()`;
- usare semplici metodi `is...` quando il requisito corrisponde alla loro semantica;
- capire che i metodi di `str` restituiscono nuove stringhe;
- scegliere tra metodo built-in e loop esplicito;
- non riscrivere manualmente un'operazione standard senza una ragione didattica/algoritmica.

## Metodo vs algoritmo manuale

Il corso mostra entrambe le prospettive.

### Per imparare l'algoritmo

```python
def conta_vocali(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.lower() in "aeiou":
            conteggio += 1
    return conteggio
```

### Per esprimere una operazione standard

Se Python offre un metodo che coincide con il requisito, usarlo può essere più leggibile e affidabile.

Criterio:

```text
capisco l'algoritmo
+
conosco gli strumenti standard
+
scelgo quello che esprime meglio l'intenzione
```

## `find` vs `in`

Se serve soltanto sapere se esiste:

```python
if "@" in email:
    ...
```

è più diretto che controllare un indice di `find`.

Se serve la posizione, `find()` può essere appropriato.

## Normalizzazione

Pattern:

```python
normalizzato = testo.strip().lower()
```

Lo studente deve sapere **perché** normalizza e quali informazioni perde/modifica.

Non normalizzare automaticamente tutto.

## Activity candidate

### A — Choose the operation

Problemi brevi: membership, posizione, normalizzazione, prefisso, sostituzione; scegliere metodo/loop.

### B — Controlled Change

Da confronto case-sensitive a confronto normalizzato.

### C — Implement

Validator/normalizzatore testuale semplice.

### D — Debug

- dimenticare che metodo restituisce nuova stringa;
- `find()` usato come booleano senza capire `0`/`-1`;
- `strip(chars)` interpretato erroneamente come rimozione di una sottostringa esatta;
- case conversion applicata al dato sbagliato.

---

# M19 — Algoritmi su testo e parsing semplice

## Obiettivi osservabili

Lo studente sa:

1. combinare funzioni, loop, selezione e metodi su testo;
2. contare caratteri che soddisfano una proprietà;
3. costruire progressivamente una nuova stringa quando il problema lo richiede;
4. riconoscere e verificare un palindromo semplice dopo normalizzazione definita;
5. validare pattern testuali elementari senza regex;
6. estrarre parti con indici/slicing;
7. progettare casi limite: stringa vuota, un carattere, spazi, maiuscole/minuscole, caratteri inattesi;
8. distinguere analisi del testo e formattazione output;
9. confrontare soluzione manuale con soluzione basata su metodi;
10. incontrare `split()` come ponte esplicito verso la prossima UDA sulle liste.

## Costruzione di una nuova stringa

Per piccoli esercizi beginner è ammesso:

```python
risultato = ""
for carattere in testo:
    if ...:
        risultato += carattere
```

Teacher note:

- utile pedagogicamente per accumulatore testuale;
- per grandi quantità di frammenti, `join` può essere più appropriato;
- performance avanzata non va usata per complicare ora il modello.

## Palindromo

Non ridurre tutto a:

```python
return testo == testo[::-1]
```

prima che lo studente sappia spiegare l'algoritmo.

Progressione possibile:

1. trace con due lati/indici oppure reverse costruito;
2. versione con slicing;
3. confronto di leggibilità e costo concettuale.

## Parsing senza regex

Problemi candidati:

- codice `AAA-123` con vincoli semplici;
- username elementare;
- conteggio parole semplificato;
- estrazione prefisso/suffisso;
- normalizzazione di spazi ai bordi;
- analisi di una riga con delimitatore noto.

Regex appartiene al percorso avanzato/optional, non serve per imparare le stringhe di base.

## `split()` come ponte verso le liste

Alla fine della UDA si può mostrare:

```python
parti = testo.split(",")
```

ma dichiarando esplicitamente:

> il risultato è una `list`; nella prossima UDA impareremo cosa significa, come si modifica e come si sceglie rispetto ad altre strutture.

Regole:

- niente algoritmi complessi su liste prima di PY2-07;
- `join()` può essere mostrato in coppia come preview, ma la sua padronanza viene consolidata dopo l'introduzione delle liste;
- non usare comprehension nella UDA stringhe core.

## Activity candidate

### A — Text trace

Seguire indice/carattere/accumulatore.

### B — Controlled Change

Modificare regola di validazione o normalizzazione mantenendo test.

### C — Implement

Funzione testuale con contratto chiaro e casi limite.

### D — Debug Clinic

- off-by-one;
- immutabilità;
- metodo non assegnato;
- `find`/membership;
- normalizzazione incompleta;
- stringa vuota non gestita.

### E — Mini-project

**Analizzatore/normalizzatore di testo** con almeno:

- più funzioni;
- iterazione;
- selezione;
- metodi stringa;
- almeno 5 casi di test;
- spiegazione di una scelta metodo vs loop.

---

# `friedpython` — policy specifica PY2-06

Snapshot:

`TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f`

Materiale individuato:

- `stringhe/stringhe.py`;
- `esercizi_stringhe/esercizio1.py` … `esercizio7.py`;
- verifica PDF storica.

## Riutilizzabile come spunto

Da `stringhe.py`:

- sequenza ordinata;
- immutabilità;
- letterali;
- escape;
- raw/triple string come esempi.

## Da correggere/non propagare

- riferimenti Python 2 (`str` vs `unicode`) non pertinenti al corso 2026/27;
- spiegazioni/path storici da verificare con Python/documentazione corrente;
- typo/commenti legacy;
- nessun copia-incolla diretto nella lesson canonica.

In particolare la nota storica che suggerisce `|` come separatore di path non è un modello da riusare. Per i path useremo `pathlib` nella UDA file.

## Esercizi

I sette script sono **candidate source material**. Prima dell'import:

```text
leggi consegna/soluzione
→ assegna obiettivo M17/M18/M19
→ verifica correttezza Python 3.12
→ separa starter/solution
→ aggiungi casi limite/test
→ classifica A–F
→ riscrivi la consegna se necessario
```

---

# Piano delle tre settimane

## Settimana 18 — M17

- teoria attiva: sequenza, indici, slicing, immutabilità;
- microscope REPL;
- trace;
- lab: Activity A–D su indici/slice.

## Settimana 19 — M18

- membership/search/metodi;
- normalizzazione;
- metodo vs loop;
- lab: validator/normalizzatore + Debug Clinic.

## Settimana 20 — M19

- algoritmi su testo;
- casi limite;
- parsing semplice;
- preview `split` → list;
- lab: mini-project E / consolidamento.

---

# Exit checkpoint UDA

Lo studente dovrebbe saper:

- spiegare ordine e immutabilità di `str`;
- usare indici positivi/negativi e slicing;
- iterare direttamente e per indice quando serve;
- usare membership e metodi appropriati;
- sapere che le trasformazioni restituiscono nuove stringhe;
- normalizzare consapevolmente;
- implementare almeno un algoritmo testuale con loop;
- progettare casi limite su testo;
- scegliere metodo vs loop e motivarlo;
- scrivere funzioni testabili su stringhe;
- riconoscere `split()` come produttore di una lista senza anticiparne tutta la semantica.

---

# Remediation

- stringhe di 3–5 caratteri con indice scritto sotto;
- slice disegnati graficamente;
- un solo metodo per esercizio;
- trace carattere per carattere;
- distinguere valore originale e nuovo valore dopo metodo;
- evitare parsing multi-step finché immutabilità/indici non sono stabili.

# Enrichment

- slicing con step;
- `casefold` e Unicode con esempi controllati;
- confronto palindrome manuale vs slicing;
- `enumerate` come preview quando serve indice+valore (formalizzato con sequenze nella UDA successiva);
- prime considerazioni sul costo di concatenazioni ripetute vs `join`, senza benchmark formali.

---

# Fonti

- *Think Python / Pensare in Python*: strings, traversal, searching, debugging;
- *Learning Python / Imparare Python*: string object coverage;
- *Fluent Python*: Unicode/sequence correctness come controllo docente;
- *Python in a Nutshell*: reference/coverage;
- documentazione Python 3.12 `str`;
- `friedpython` pinned come legacy source pack;
- Pluralsight Data Structures / Python Essentials come gap-check.

---

# Dipendenze piattaforma

- Python 3.12;
- P1 per programmi stdin/stdout;
- P2 function behavior desiderabile per funzioni testuali, bloccato su `TheBitPoets/2cornot2c#756`;
- nessun runtime speciale richiesto.

---

# Criteri per produzione

- audit dei 7 esercizi friedpython completato prima di importarli;
- nessun contenuto Python 2 residuo;
- lesson M17–M19 originali;
- almeno un algoritmo manuale + confronto con metodo built-in;
- casi limite stringa vuota/1-char presenti;
- `split/join` trattati come bridge, non liste insegnate implicitamente;
- Activity P2 solo dopo contratto piattaforma o fallback didattico esplicito.

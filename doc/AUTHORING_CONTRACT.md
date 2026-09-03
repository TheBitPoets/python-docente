# python-docente — authoring contract (DRAFT)

`python-docente` adotta senza forkare:

- `thebitlab.content-pack.v1`;
- Course Design v1;
- Activity schema 1.0;
- tassonomia Activity A–F.

Questo documento definisce soltanto le convenzioni specifiche del corso Python.

## 1. Contratto di ogni lesson

Ogni modulo M00–M30 deve produrre una lesson canonica originale con struttura adattabile al tema.

Sezioni attese, quando pertinenti:

```text
1. Perché ci serve
2. Obiettivi osservabili
3. Prerequisiti
4. Problema iniziale
5. Modello mentale
6. Algoritmo / pseudocodice / flow chart
7. Concetto Python
8. Microscope / esempio minimo
9. Worked example realistico
10. Trace / previsione dell'esecuzione
11. Varianti e scelta del costrutto
12. Errori frequenti / misconception
13. Debug clinic
14. Esercizi graduati
15. Activity correlate
16. Checkpoint
17. Sintesi
18. Fonti / riferimenti
```

Non tutte le sezioni devono essere forzate in ogni modulo. Un modulo su flow chart, per esempio, non deve fingere di avere già “concetto Python”.

## 2. Densità per studenti di seconda

Rispetto a TPSI5:

- paragrafi più brevi;
- un concetto principale per sezione;
- più tabelle di trace;
- più esempi prima/DOPO;
- più visualizzazioni di stato;
- meno salti impliciti;
- più domande predittive;
- frequenti “fermati e prova”.

La lesson resta rigorosa: semplificare la presentazione non significa introdurre modelli falsi.

## 3. Problema → algoritmo → codice

Per i moduli significativi la lesson deve mostrare almeno una volta il percorso:

```text
specifica
→ input/output/vincoli
→ casi di test
→ algoritmo
→ flow chart/pseudocodice
→ trace
→ Python
→ test
→ debug/refactor
```

Con l'avanzare del corso non è necessario produrre sempre tutti gli artefatti, ma il processo deve restare riconoscibile.

## 4. Modello mentale prima della sintassi

Ogni costrutto nuovo deve rispondere a due domande:

1. **che problema risolve?**
2. **quando lo scelgo invece delle alternative?**

Esempi:

- `if/elif/else` vs `if` indipendenti;
- `for` vs `while`;
- funzione vs blocco duplicato;
- list vs tuple vs set vs dict;
- dict/record vs classe;
- metodo vs funzione esterna.

## 5. Trace obbligatorio

Ogni UDA di controllo del flusso/dati deve includere Activity di trace.

Formati ammessi:

- tabella variabili;
- previsione output;
- evidenziazione riga corrente;
- step Flowchart Lab;
- simulator/event trace Romeo;
- debugger più avanti.

## 6. Debugging come contenuto canonico

Ogni UDA deve avere almeno un `Debug Clinic` con bug realistici:

- sintassi;
- tipo/conversione;
- condizione sbagliata;
- off-by-one;
- loop infinito;
- alias/mutazione;
- chiave mancante;
- path/file;
- stato oggetto incoerente.

Non concentrare il debugging in un unico modulo.

## 7. Testing progressivo

La lesson non deve esporre pytest prima che serva.

Progressione:

```text
casi su carta
→ input/output attesi
→ trace
→ assert
→ test di funzioni
→ test di oggetti
→ pytest nei livelli professionali
```

TheBitLab può usare test nascosti come infrastruttura anche quando lo studente non conosce ancora pytest.

## 8. Source mapping

Ogni content item deve dichiarare provenienza/reference coerente con Content Pack v1.

Ruoli pratici del corso:

- TP: pedagogia;
- DOC: semantica autoritativa;
- LP/PN: coverage;
- FP: controllo idiomatico/modelli mentali;
- PS: gap-check/lab;
- FR: legacy source pack;
- RO: runtime/progetto applicativo.

Nessun testo licensed viene copiato nel contenuto canonico.

## 9. Slide

Ogni modulo ha un deck separato.

Default:

- 12–25 slide, non 40–60;
- poco testo per slide;
- almeno un problema/trace visuale;
- uno o più momenti “prova adesso”;
- handoff esplicito all'Activity;
- build HTML/PDF/PPTX riproducibile.

## 10. Teacher notes

Per ogni modulo il materiale docente dovrebbe includere:

- misconception previste;
- domande diagnostiche;
- spiegazione alternativa;
- demo consigliata;
- punti dove fermarsi e far provare;
- remediation;
- enrichment;
- solution/reference;
- criteri manuali non autogradabili.

## 11. Student path

Lo studente deve poter navigare:

```text
student/README
→ settimana/UDA
→ lesson
→ slide/recap
→ Activity
→ workspace TheBitLab
→ evidence/consegna
```

Non deve conoscere la struttura interna del repository per trovare il lavoro assegnato.

## 12. Ambiente

Le lesson non possono contenere istruzioni di setup ad hoc che aggirino il Classroom Environment.

I prerequisiti tecnici vengono espressi come capability del profilo TheBitLab.

Esempio:

```text
requires:
  python: 3.12
  workspace: true
  flowchart-lab: optional|required
  romeo-sim: optional|required
  git-basic: optional|required
```

La sintassi finale di questo contratto è bloccata su `2cornot2c#753`.

## 13. Curriculum vs delivery

Dopo il freeze:

- cambio obiettivo/prerequisito/ordine necessario/outcome → curriculum change;
- typo, chiarimento, slide, setup, lab-fix a contratto invariato → delivery change.

Stesso principio TPSI5.

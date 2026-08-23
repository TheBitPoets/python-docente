# Python secondo anno — delivery profile (DRAFT)

## Vincolo orario reale

Il corso dispone di **3 ore settimanali**:

- 2 ore in aula teorica;
- 1 ora in laboratorio.

Sono disponibili portatili anche fuori dal laboratorio, quindi la progettazione non separa rigidamente “teoria” e “pratica”.

## Principio

Ogni settimana dovrebbe contenere, quando possibile, almeno tre tipi di attività:

1. **modello mentale / teoria**;
2. **esecuzione guidata / trace / micro-coding**;
3. **problema da risolvere / Activity / progetto**.

Una lezione teorica può quindi includere:

- lavagna e flow chart;
- REPL;
- previsione dell'output;
- modifica di poche righe;
- debugging collettivo;
- confronto di due soluzioni;
- micro-missione Romeo simulata;
- mini-checkpoint TheBitLab.

## Pattern settimanale consigliato

### Ora teoria A

```text
problema / scenario
→ concetto
→ flow chart / trace
→ domande predittive
→ micro-esempio
```

### Ora teoria B

```text
REPL / guided coding
→ esercizi brevi
→ errori comuni
→ confronto di alternative
→ preparazione dell'Activity
```

### Ora laboratorio

```text
Activity C/D/E/F
→ implementazione
→ test
→ debugging
→ evidence/consegna
→ recap
```

Le tre ore non devono necessariamente avvenire nello stesso giorno.

## Primo contatto con Python

Progressione raccomandata:

```text
Flowchart Lab
→ REPL Python standard
→ script .py molto piccoli
→ editor gestito / VS Code
→ debugger
→ progetto multi-file più avanti
```

### Perché il REPL

Il REPL permette di isolare senza rumore:

- espressioni;
- tipi;
- variabili;
- operatori;
- conversioni;
- chiamate di funzione;
- errori immediati.

Non deve durare troppo: lo studente passa presto a file `.py` per imparare programma, ordine, salvataggio, riesecuzione e debugging.

IPython può essere enrichment se entra nel profilo TheBitLab; non è requisito curricolare.

## Ambiente

Unico percorso supportato: Classroom Environment TheBitLab / 2cornot2c.

### Docker-light

Target macchine con poca RAM. Oggi è una shell Ubuntu isolata; quindi le capability grafiche devono essere esposte dal host/browser o da servizi gestiti, non presunte dentro il container.

### VM grafica

Target completo con desktop Linux XFCE e workspace condivisi.

### Regola di equivalenza

Un'Activity core deve poter essere completata sui due profili oppure dichiarare esplicitamente una capability/fallback gestita da TheBitLab.

Nessun esercizio core deve richiedere installazioni manuali diverse tra scuola e casa.

## Flow chart

Il corso richiede una capability cross-platform gestita da TheBitLab.

Flowgorithm può essere usato come riferimento didattico/funzionale su Windows, ma non è il percorso canonico.

Il futuro Flowchart Lab dovrebbe permettere di salvare il diagramma nello stesso workspace dell'Activity e produrre evidence revisionabile.

## Romeo

Romeo entra come applicazione ricorrente dopo che il concetto Python è stato introdotto anche in forma generale.

Esempio:

```text
for generale
→ esercizio su numeri/stringhe
→ missione Romeo: ripeti un movimento N volte
```

oppure:

```text
funzioni
→ decomponi un problema generale
→ missione Romeo composta da funzioni di movimento
```

Nel blocco OOP si passa dall'API facile a funzioni all'API a oggetti quando questo aiuta a vedere concretamente stato e comportamento.

## Valutazione nel flusso

Oltre alle quattro verifiche minime annuali (teoria + pratica per quadrimestre), raccogliere evidence leggere:

- trace;
- diagramma;
- codice;
- test;
- bug diagnosis;
- spiegazione scelta `for` vs `while`;
- scelta struttura dati;
- commit Git selezionati;
- missione Romeo;
- mini-progetto.

Non tutte generano voto; servono anche a diagnosi e recupero.

## AI

Default nelle Activity fondamentali: no generazione della soluzione.

Quando l'AI viene introdotta come strumento professionale, l'Activity deve distinguere almeno:

```text
prompt / suggerimento AI
→ verifica umana
→ test
→ correzione
→ spiegazione
```

Lo studente è responsabile del codice consegnato.

## Conseguenza progettuale

Le lesson e le slide devono essere progettate per essere interrotte da azioni dello studente. Evitare deck da 50 minuti di sola esposizione.

Ogni modulo dovrebbe identificare esplicitamente:

- cosa spiega il docente;
- cosa prevede/traccia lo studente;
- cosa prova al REPL/editor;
- cosa svolge come Activity;
- quale evidence dimostra l'apprendimento.

# Checkpoint C — Chiusura del percorso di seconda

> Stato: **draft editoriale controllato**  
> Finestra: settimana 33  
> Vincolo: **nessun nuovo prerequisito obbligatorio**.

## Scopo

Il Checkpoint C non introduce un nuovo argomento. Serve a chiudere l'anno usando ciò che hai già imparato per:

- completare o rifinire il capstone OOP;
- recuperare competenze ancora fragili;
- correggere bug rimasti aperti;
- migliorare leggibilità e struttura senza cambiare il comportamento corretto;
- organizzare le evidence del percorso;
- spiegare le scelte fatte.

## Percorso base

1. Rileggi la specifica del tuo capstone.
2. Elenca le funzionalità obbligatorie già completate e quelle mancanti.
3. Esegui i test/casi previsti dal progetto.
4. Scegli **un solo problema alla volta** da correggere.
5. Dopo ogni correzione riesegui i casi che prima funzionavano.
6. Verifica che le responsabilità delle classi siano chiare.
7. Controlla che la composizione tra oggetti sia comprensibile.
8. Prepara una breve spiegazione finale del modello scelto.

## Checklist minima capstone

Il progetto finale dovrebbe mostrare, in forma proporzionata al problema:

- analisi del problema;
- almeno una classe significativa;
- più istanze quando il dominio lo richiede;
- attributi e metodi coerenti;
- stato valido/invarianti semplici;
- almeno una collaborazione/composizione tra oggetti oppure una motivazione del perché non serve;
- una struttura dati non banale quando appropriata;
- funzioni/metodi con responsabilità riconoscibili;
- casi di test o checklist di verifica;
- almeno un edge case;
- una breve spiegazione delle scelte di progetto.

La persistenza su file è utile ma non diventa obbligatoria se il calendario annuale non ha consentito di consolidarla adeguatamente.

## Recupero competenze

Se non devi completare il capstone, usa la settimana per recuperare una competenza precisa, ad esempio:

- `for` vs `while`;
- funzioni e `return`;
- alias vs copia;
- scelta tra list/tuple/set/dict;
- dizionari e lookup;
- file di testo;
- classi/istanze/metodi;
- composizione e responsabilità.

Il recupero deve produrre una evidence verificabile: trace, esercizio corretto, debug spiegato, piccolo programma o revisione di una parte del progetto.

## Enrichment

Solo dopo il core, puoi esplorare una estensione non necessaria per la sufficienza, ad esempio:

- `__str__` / `__repr__`;
- property introduttiva;
- ereditarietà semplice come confronto;
- dataclass dopo aver compreso la classe esplicita;
- persistenza più ricca;
- piccola estensione Romeo simulata se il runtime è certificato.

## Presentazione finale

Devi saper rispondere almeno a queste domande:

1. Quale problema risolve il progetto?
2. Quali sono le classi principali e perché esistono?
3. Quale stato mantiene ciascun oggetto?
4. Dove avviene la collaborazione tra oggetti?
5. Quale struttura dati hai scelto e perché?
6. Quale bug o edge case hai dovuto gestire?
7. Quale parte rifattorizzeresti con più tempo?

## AI

Se la policy del docente consente AI in questa fase, può essere usata solo come supporto a review/debug. Ogni suggerimento va verificato, testato e spiegato. Non sostituisce la tua capacità di motivare il progetto.

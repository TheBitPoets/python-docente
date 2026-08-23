# Python — modello di valutazione del secondo anno (DRAFT)

> Obiettivo: valutare la capacità di progettare, implementare, verificare e spiegare una soluzione, non soltanto la memoria della sintassi.

## Tipi di evidenza

Durante l'anno il corso raccoglie evidenze diverse:

1. **Problem analysis** — dati, output, vincoli, casi limite.
2. **Algorithm design** — pseudocodice/flow chart.
3. **Trace** — previsione e simulazione dell'esecuzione.
4. **Implementation** — codice funzionante.
5. **Debugging** — diagnosi e correzione.
6. **Design choice** — motivazione di costrutti e strutture dati.
7. **Testing** — casi e risultati attesi.
8. **Refactoring** — miglioramento senza cambiare comportamento.
9. **Explanation** — spiegazione orale/scritta.
10. **Integrated product** — mini-progetto/capstone.

Non ogni prova deve contenere tutti i tipi di evidenza.

## Rubrica trasversale

Dimensioni candidate:

| Dimensione | Domanda |
|---|---|
| Comprensione | Ha capito realmente il problema? |
| Algoritmo | La strategia porta al risultato ed è spiegabile? |
| Correttezza | Il programma produce risultati corretti nei casi richiesti? |
| Casi limite | Gestisce input/casi significativi oltre all'happy path? |
| Costrutti | Usa selezione/iterazione/funzioni in modo appropriato? |
| Dati | Sceglie e modella correttamente le strutture dati? |
| Decomposizione | Divide il problema in responsabilità gestibili? |
| Leggibilità | Naming, struttura e formattazione rendono il codice comprensibile? |
| Test/debug | Sa dimostrare e diagnosticare il comportamento? |
| Spiegazione | Sa motivare le proprie scelte e confrontare alternative? |

## Progressione della valutazione

### Primo nucleo

Peso maggiore a:

- algoritmo;
- trace;
- correttezza;
- controllo del flusso;
- debugging.

Il codice può essere piccolo e guidato.

### Funzioni e strutture dati

Aumenta il peso di:

- decomposizione;
- scelta del modello dati;
- test;
- confronto tra alternative;
- leggibilità.

### OOP/capstone

Aumenta il peso di:

- responsabilità;
- modellazione;
- composizione;
- coerenza tra stato e comportamento;
- integrazione delle competenze precedenti.

## Prove pratiche

Una verifica non deve essere necessariamente una lista di esercizi tutti uguali.

Formato candidato:

```text
Parte A — trace / comprensione
Parte B — implementazione breve
Parte C — debug / correzione
Parte D — problema da progettare
Parte E — spiegazione di una scelta
```

Il mix cambia in base alla UDA.

## Autograding e valutazione docente

### Buoni candidati per test automatici

- output deterministico;
- funzioni pure;
- trasformazioni di stringhe/collezioni;
- casi limite codificabili;
- eccezioni/return contract quando stabile.

### Evidence manuale/rubric

- flow chart;
- qualità dell'algoritmo;
- motivazione della scelta;
- leggibilità oltre a regole meccaniche;
- refactoring;
- responsabilità OOP;
- spiegazione orale.

TheBitLab non deve trasformare una dimensione qualitativa in un falso numero soltanto perché è più semplice da automatizzare.

## Uso delle soluzioni

Le reference solution servono al docente e alla regressione del corso.

Per problemi aperti può esistere più di una soluzione valida. La rubrica deve permettere strategie alternative corrette e motivate.

## Recupero

Il recupero deve essere competence-based:

- identificare la skill mancante;
- assegnare Activity A/B/D mirate;
- riprovare una evidence dello stesso tipo con problema diverso;
- non richiedere necessariamente di ripetere un intero modulo.

## Capstone di seconda

Il prodotto finale deve mostrare almeno:

- analisi;
- funzioni;
- una struttura dati non banale;
- classi/oggetti;
- test/checklist;
- gestione di almeno un caso limite;
- breve spiegazione delle decisioni.

Persistenza su file è desiderabile ma non obbligatoria se il calendario reale ha consumato la settimana PY2-09.

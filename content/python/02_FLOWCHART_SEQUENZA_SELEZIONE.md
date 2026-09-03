# M02 — Flow chart: sequenza, input/output e selezione

> **Stato:** draft  
> **UDA:** PY2-01 — Problem solving, algoritmi e flow chart  
> **Delivery:** Flowchart Lab candidate quando disponibile; fallback manuale sempre valido finché la capability non è classroom-certified

## Obiettivi

Alla fine di questo modulo dovresti saper:

- leggere i simboli fondamentali di un diagramma di flusso;
- costruire una sequenza con input, elaborazione e output;
- rappresentare una decisione booleana;
- costruire selezione semplice e doppia;
- seguire un diagramma passo-passo con dati concreti;
- compilare una trace table elementare;
- diagnosticare rami mancanti, condizioni invertite e output collocati nel punto sbagliato;
- salvare, quando il Flowchart Lab è disponibile, l'artifact gestito `algorithm.flow.json` senza confondere la validità strutturale con la qualità dell'algoritmo.

---

# 1. Perché un diagramma?

Lo pseudocodice descrive i passi con testo.

Un flow chart rende visibile il **flusso di controllo**:

```text
inizio
  ↓
input
  ↓
calcolo
  ↓
decisione
 ↙      ↘
...     ...
```

Non serve a “decorare” l'algoritmo. Serve a mostrare:

- che cosa succede prima e dopo;
- dove il flusso si divide;
- dove i rami si ricongiungono;
- se ogni percorso può arrivare a una conclusione.

---

# 2. Simboli core del corso

Usiamo un insieme piccolo e stabile.

| Idea | Forma convenzionale | Significato |
|---|---|---|
| start/end | terminatore | inizio/fine |
| input/output | parallelogramma | dato acquisito o mostrato |
| processing | rettangolo | calcolo/assegnamento |
| decision | rombo | condizione con rami |
| freccia | collegamento | prossimo passo |

La forma grafica aiuta, ma la correttezza dipende soprattutto dal significato dei nodi e dei collegamenti.

---

# 3. Prima sequenza

Problema:

> Leggi due numeri e mostra la loro somma.

Modello:

```text
START
  ↓
INPUT A
  ↓
INPUT B
  ↓
SOMMA ← A + B
  ↓
OUTPUT SOMMA
  ↓
END
```

Ogni passo ha un solo successore.

Questa è una **sequenza**.

---

# 4. Trace della sequenza

Con input `2` e `3`:

| nodo | A | B | somma | output |
|---|---:|---:|---:|---:|
| start | — | — | — | — |
| input A | 2 | — | — | — |
| input B | 2 | 3 | — | — |
| calcolo | 2 | 3 | 5 | — |
| output | 2 | 3 | 5 | 5 |

Il diagramma non sostituisce il trace: ci dice **dove andare**, il trace mostra **che cosa succede ai dati**.

---

# 5. La decisione

Problema:

> Leggi una temperatura e indica se supera 30.

La condizione è:

```text
temperatura > 30 ?
```

Dal rombo partono due possibilità:

```text
           temperatura > 30?
              /      \
           true      false
            /          \
     "sopra soglia"  "entro soglia"
```

Una condizione deve poter essere valutata come vera o falsa nel punto in cui viene usata.

---

# 6. Selezione doppia

Nel nostro Flowchart Lab i rami di una decisione sono espliciti:

```text
true
false
```

Per la soglia:

```text
START
 ↓
INPUT temperatura
 ↓
[temperatura > 30?]
  true ↙       ↘ false
OUTPUT alta   OUTPUT normale
       ↘       ↙
          END
```

Domanda importante:

> Tutti i possibili input seguono uno dei due rami?

Per una condizione booleana sì: o è vera o è falsa.

---

# 7. Selezione semplice

A volte un ramo non richiede un'azione specifica.

Esempio:

> Se il saldo è negativo, mostra un avviso; poi continua.

```text
[saldo < 0?]
 true ↙     ↘ false
AVVISO       |
     \       /
      prossimo passo
```

Anche quando un ramo “non fa nulla”, il flusso deve restare chiaro.

---

# 8. Condizione invertita

Specificazione:

> Mostra “ammesso” se età >= 14.

Diagramma sbagliato:

```text
età >= 14?
true  → "non ammesso"
false → "ammesso"
```

Il diagramma può essere strutturalmente valido ma semanticamente sbagliato.

Questo è un punto fondamentale:

```text
file/schema valido ≠ algoritmo corretto
```

Per questo la qualità dell'algoritmo resta evidence/rubric docente.

---

# 9. Output troppo presto

Problema:

> Applica uno sconto se il prezzo supera 100, poi mostra il prezzo finale.

Errore:

```text
INPUT prezzo
↓
OUTPUT prezzo
↓
decisione sconto
```

Il risultato viene mostrato **prima** della decisione che dovrebbe modificarlo.

Il trace individua immediatamente il primo punto di divergenza.

---

# 10. Più casi

Problema:

> Classifica un valore come negativo, zero o positivo.

Possiamo usare due decisioni:

```text
n < 0?
 true → negativo
 false → n == 0?
          true → zero
          false → positivo
```

Non abbiamo bisogno di un nuovo simbolo per ogni possibile problema.

Componiamo poche primitive chiare.

---

# 11. Flowchart Lab: che cosa deve fare per noi

Quando il runtime managed è disponibile, il percorso è:

```text
TheBitLab
→ Flowchart Lab locale
→ browser UI
→ diagramma
→ Run / Step / Reset
→ variable watch
→ algorithm.flow.json nel workspace
```

Il browser non esegue Python dello studente.

Il motore usa un linguaggio di espressioni ristretto e deterministico.

## Importante

Finché `flowchart.lab.v1` non è certificata nei profili classroom, il corso mantiene il fallback:

```text
carta / lavagna / template
+ trace table
+ casi di test
+ rubric docente
```

Gli outcome didattici non dipendono dalla disponibilità del tool.

---

# 12. Save non significa “consegna perfetta”

Il Flowchart Lab può verificare cose deterministiche:

- schema valido;
- nodi e archi coerenti;
- esecuzione terminata entro il limite;
- output/trace per input dichiarati.

Non può assegnare automaticamente un voto affidabile a:

- chiarezza della decomposizione;
- scelta più appropriata dei costrutti;
- semplicità del diagramma;
- qualità della spiegazione.

Questi aspetti restano manuali.

---

# 13. Laboratorio guidato — soglia

Costruisci il diagramma:

> Leggi `temperatura`. Se è maggiore di 30 mostra “sopra soglia”, altrimenti mostra “entro soglia”.

Prima di eseguirlo, prepara i test:

```text
31 → sopra soglia
30 → entro soglia
29 → entro soglia
```

Perché 30 è il caso più importante da non dimenticare?

---

# 14. Controlled Change

Parti dal diagramma funzionante e cambia soltanto:

```text
soglia 30 → soglia 25
```

Poi aggiorna i casi di test.

Obiettivo:

> modificare il requisito senza ridisegnare parti non coinvolte.

---

# 15. Error Clinic

Diagnostica uno alla volta:

1. ramo `false` mancante;
2. condizione invertita;
3. output prima dell'assegnamento;
4. nodo non raggiungibile;
5. ramo che non arriva a `end`;
6. trace atteso diverso dall'esecuzione.

Per ogni errore scrivi:

```text
sintomo
primo nodo problematico
modifica minima
caso che lo rivela
```

---

# Minimum mastery checkpoint

Dovresti saper:

1. riconoscere start/end, input/output, processing e decision;
2. costruire una sequenza;
3. costruire una selezione doppia;
4. seguire true/false con un input concreto;
5. compilare una trace table;
6. progettare almeno un test sul confine;
7. distinguere validità strutturale e correttezza semantica;
8. usare il fallback manuale senza perdere gli outcome se il tool non è disponibile.

## Recap

```text
sequenza → un percorso
selezione → il flusso sceglie un ramo
trace → rende visibile stato e percorso
test → prova casi diversi, soprattutto i confini
```

Prossimo modulo: introduciamo ripetizione, terminazione e annidamento nei diagrammi.

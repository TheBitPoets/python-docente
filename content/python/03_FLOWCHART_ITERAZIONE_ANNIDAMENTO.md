# M03 — Flow chart: iterazione, terminazione e annidamento

> **Stato:** draft  
> **UDA:** PY2-01 — Problem solving, algoritmi e flow chart  
> **Delivery:** Flowchart Lab candidate quando disponibile; fallback manuale sempre valido finché la capability non è classroom-certified

## Obiettivi

Alla fine di questo modulo dovresti saper:

- riconoscere quando una parte dell'algoritmo deve essere ripetuta;
- rappresentare un ciclo controllato da una condizione;
- rappresentare un ciclo controllato da un contatore a livello algoritmico;
- individuare inizializzazione, condizione, corpo e aggiornamento;
- spiegare perché un ciclo termina;
- usare una selezione dentro un ciclo e un ciclo dentro una selezione;
- leggere un primo ciclo annidato senza trasformarlo in una ricetta da memorizzare;
- progettare casi che rivelano off-by-one, aggiornamento mancante e mancata terminazione.

---

# 1. Quando una freccia torna indietro

Problema:

> Chiedi un valore finché non è compreso tra 1 e 10.

Una sequenza non basta, perché non sappiamo in anticipo quante volte l'utente fornirà un dato non valido.

Serve una ripetizione:

```text
leggi valore
↓
valido?
  sì → continua
  no → torna a leggere
```

La freccia che ritorna non significa “ripeti per sempre”.

Deve esistere una condizione che permette di uscire.

---

# 2. Le quattro domande del ciclo

Per ogni ciclo chiedi:

```text
1. che stato esiste prima del ciclo?
2. quando il corpo deve essere eseguito?
3. che cosa cambia nel corpo?
4. perché prima o poi la condizione cambia abbastanza da uscire?
```

Queste domande sono più importanti del nome che il futuro linguaggio userà per il ciclo.

---

# 3. Ciclo controllato da condizione

Pseudocodice:

```text
LEGGI valore
MENTRE valore < 1 O valore > 10
    LEGGI valore
FINE MENTRE
MOSTRA "valido"
```

Trace con input:

```text
0
12
7
```

| controllo | valore | invalido? | azione |
|---:|---:|---|---|
| 1 | 0 | sì | leggi ancora |
| 2 | 12 | sì | leggi ancora |
| 3 | 7 | no | esci |

Il numero di ripetizioni dipende dai dati.

---

# 4. Aggiornamento mancante

Algoritmo:

```text
ASSEGNA i ← 0
MENTRE i < 3
    MOSTRA i
FINE MENTRE
```

Che cosa cambia `i`?

Nulla.

La condizione `i < 3` resta vera e il ciclo non termina.

Correzione:

```text
ASSEGNA i ← i + 1
```

nel punto appropriato del corpo.

---

# 5. Contatore: stato che racconta quante volte

```text
ASSEGNA i ← 0
MENTRE i < 3
    MOSTRA i
    ASSEGNA i ← i + 1
FINE MENTRE
```

Trace:

| passo ciclo | i prima | output | i dopo |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 2 | 3 |

Al controllo successivo `3 < 3` è falso.

Quindi il ciclo termina.

---

# 6. Off-by-one

Vogliamo mostrare:

```text
1 2 3
```

Confronta:

```text
i ← 1
MENTRE i < 3
```

con:

```text
i ← 1
MENTRE i <= 3
```

Una sola differenza nel confine cambia il numero di iterazioni.

Per i cicli i casi vicino al limite sono test fondamentali.

---

# 7. Accumulatore concettuale

Problema:

> Somma tre valori.

Possiamo mantenere uno stato `totale`:

```text
totale ← 0
contatore ← 0

MENTRE contatore < 3
    LEGGI valore
    totale ← totale + valore
    contatore ← contatore + 1
FINE MENTRE

MOSTRA totale
```

Domanda guida:

> Che cosa significa `totale` dopo ogni iterazione?

Risposta utile:

> contiene la somma dei valori letti **finora**.

Questa spiegazione vale più della memorizzazione di un pattern.

---

# 8. Selezione dentro un ciclo

Problema:

> Leggi 5 numeri e conta quanti sono positivi.

Struttura:

```text
ripeti per 5 valori
    leggi valore
    se valore > 0
        incrementa conteggio
```

Il ciclo decide **quante volte osservare**.

La selezione decide **se aggiornare lo stato** per quel dato.

Sono due responsabilità diverse.

---

# 9. Ciclo dentro una selezione

Problema:

> Se l'utente sceglie “esegui”, ripeti un'operazione 3 volte; altrimenti termina.

Qui la decisione avviene prima:

```text
scelta = esegui?
 true → ciclo
 false → end
```

Non esiste una regola “il ciclo va sempre fuori” o “la decisione va sempre dentro”.

La struttura dipende dal problema.

---

# 10. Primo ciclo annidato

Una piccola griglia 2 × 3 può essere descritta così:

```text
per ogni riga
    per ogni colonna
        visita cella
```

A livello di flow chart possiamo rappresentare due stati:

```text
riga
colonna
```

Il ciclo interno completa le colonne di una riga; poi il ciclo esterno passa alla riga successiva.

Non serve ancora formalizzare complessità Big-O.

Domanda intuitiva:

> Se raddoppio righe e colonne, quante più celle devo visitare?

---

# 11. Trace di cicli annidati

Per 2 righe × 2 colonne:

| riga | colonna | cella visitata |
|---:|---:|---|
| 0 | 0 | (0,0) |
| 0 | 1 | (0,1) |
| 1 | 0 | (1,0) |
| 1 | 1 | (1,1) |

Se perdi il filo, non indovinare: costruisci una tabella.

---

# 12. Flowchart Lab e step limit

Il Flowchart Lab candidate può eseguire diagrammi e produrre un trace deterministico.

Per sicurezza esiste un limite massimo di step.

Un risultato `limit-exceeded` non dimostra automaticamente quale sia il bug, ma è evidence che il diagramma non ha raggiunto `end` entro il limite previsto.

Il lavoro dello studente resta:

1. trovare il ciclo coinvolto;
2. osservare stato e condizione;
3. individuare ciò che non cambia come previsto;
4. correggere il modello.

---

# 13. Error Clinic — ciclo infinito

Cerca uno di questi segnali:

- aggiornamento assente;
- aggiornamento nella direzione sbagliata;
- condizione che non può diventare falsa;
- ritorno grafico collegato al nodo sbagliato.

Non correggere “a tentativi”.

Usa il trace degli ultimi step disponibili.

---

# 14. Error Clinic — inizializzazione nel posto sbagliato

Vogliamo contare eventi:

```text
conteggio ← 0
MENTRE ...
    ...
    conteggio ← conteggio + 1
FINE MENTRE
```

Errore:

```text
MENTRE ...
    conteggio ← 0
    conteggio ← conteggio + 1
FINE MENTRE
```

Il contatore viene azzerato a ogni iterazione.

Domanda:

> Quale significato avrebbe dovuto mantenere da un giro al successivo?

---

# 15. Controlled Change

Diagramma iniziale:

> mostra i valori da 0 a 2.

Modifica richiesta:

> mostra i valori da 0 a 4.

Cambia soltanto il confine necessario e aggiorna i test attesi.

Poi prova una seconda modifica:

> mostra da 1 a 5.

Questa volta potrebbe servire cambiare sia inizializzazione sia condizione.

---

# 16. Mini-project — missione su griglia

Progetta una piccola missione algoritmica senza API Python e senza hardware obbligatorio.

Esempio:

> Un robot concettuale percorre una riga di 5 celle. Per ogni cella legge se è libera; conta gli ostacoli e termina dopo l'ultima cella.

Consegna:

```text
specifica sintetica
input/output
flow chart
trace su almeno 2 casi
1 caso limite
spiegazione della terminazione
```

Romeo può essere solo scenario motivante: questa UDA non dipende da `romeo-sim`.

---

# 17. Exit checkpoint PY2-01

Prima di passare al primo programma Python dovresti riuscire a:

1. identificare input/output/vincoli;
2. scrivere pseudocodice leggibile;
3. costruire una sequenza;
4. costruire una selezione;
5. costruire un ciclo con inizializzazione/condizione/aggiornamento;
6. seguire il diagramma con un trace;
7. trovare almeno un caso limite;
8. spiegare perché il diagramma termina;
9. diagnosticare un errore evidente in un algoritmo altrui.

Non è richiesta perfezione grafica.

## Recap

```text
problema
→ algoritmo
→ flow chart
→ trace
→ test
→ debug
```

Nel prossimo modulo useremo Python per tradurre procedure che sappiamo già leggere, simulare e verificare.

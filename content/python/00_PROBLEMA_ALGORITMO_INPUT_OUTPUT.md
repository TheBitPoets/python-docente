# M00 — Problema, algoritmo, programma, input e output

> **Stato:** draft / orientamento iniziale  
> **Collocazione:** prima settimana, integrato nella finestra PY2-01  
> **Dipendenze:** nessuna; Python e Flowchart Lab non sono prerequisiti

## Obiettivi

Alla fine di questo modulo dovresti saper:

- distinguere un **problema** da un **algoritmo** e da un **programma**;
- individuare input, output e vincoli in una consegna semplice;
- riconoscere informazioni necessarie, inutili o mancanti;
- descrivere una soluzione come una sequenza finita di passi;
- usare esempi e controesempi per controllare se hai capito il problema;
- distinguere almeno intuitivamente un errore di comprensione, un errore nell'algoritmo e un errore di esecuzione.

Non devi ancora scrivere codice.

---

# 1. Prima del linguaggio viene il problema

Considera la richiesta:

> Una bottiglia costa 2 euro. Un cliente paga con 5 euro. Quanto resto deve ricevere?

La domanda non chiede ancora Python, un flow chart o una formula da memorizzare.

Prima dobbiamo capire:

```text
INPUT  → prezzo, denaro ricevuto
OUTPUT → resto
VINCOLO → il pagamento deve essere sufficiente
```

Una possibile procedura è:

```text
1. leggi il prezzo
2. leggi quanto è stato pagato
3. calcola pagato - prezzo
4. comunica il resto
```

Questa procedura è un piccolo **algoritmo**.

---

# 2. Problema, algoritmo, programma

## Problema

È ciò che vogliamo risolvere.

Può essere espresso in linguaggio naturale e può contenere informazioni incomplete o ambigue.

## Algoritmo

È una procedura abbastanza precisa da poter essere seguita passo-passo.

Per i nostri primi problemi deve essere:

- finita;
- non ambigua al livello necessario;
- eseguibile con i dati disponibili;
- verificabile con esempi concreti.

## Programma

È una descrizione dell'algoritmo in un linguaggio che il computer può eseguire.

Il percorso del corso sarà spesso:

```text
problema
→ analisi
→ algoritmo
→ rappresentazione / trace
→ programma
→ test
→ debug
```

Il programma non sostituisce il ragionamento che viene prima.

---

# 3. Input, output e vincoli

Prendiamo una seconda consegna:

> Dati la temperatura attuale e una soglia, indica se la temperatura supera la soglia.

Possiamo estrarre:

```text
INPUT
- temperatura attuale
- soglia

OUTPUT
- sì/no: supera la soglia?
```

Un vincolo potrebbe essere, per esempio, l'unità di misura comune.

## Informazioni inutili

Se la consegna aggiunge:

> Il sensore è di colore blu.

il colore probabilmente non serve a decidere se la temperatura supera la soglia.

Un buon programmatore non usa automaticamente ogni dato disponibile: chiede **quale dato serve davvero alla decisione**.

---

# 4. Informazioni mancanti

Consegna:

> Calcola l'area.

Possiamo farlo?

Non ancora: manca almeno la forma e mancano le misure necessarie.

Una specifica insufficiente non si corregge inventando dati.

Prima si chiarisce il problema.

---

# 5. I passi devono essere operativi

Confronta:

```text
1. fai il calcolo giusto
2. mostra il risultato
```

con:

```text
1. acquisisci base
2. acquisisci altezza
3. calcola base × altezza
4. mostra il prodotto
```

La seconda versione è più utile perché rende espliciti dati e trasformazione.

Non significa che ogni algoritmo debba avere molti passi: significa che i passi essenziali non devono essere nascosti dietro parole vaghe.

---

# 6. Un esempio non dimostra tutto

Supponiamo di avere un algoritmo che dovrebbe restituire il maggiore tra due numeri.

Con il caso:

```text
A = 8
B = 3
```

ottiene 8.

È sufficiente per dire che l'algoritmo funziona sempre?

No.

Proviamo almeno:

```text
A = 3, B = 8
A = 5, B = 5
A = -2, B = -7
```

Un caso riuscito è **evidence**, non una dimostrazione generale.

Nel secondo anno costruire casi di test diventerà una normale abitudine di lavoro.

---

# 7. Caso normale, caso limite, controesempio

## Caso normale

Rappresenta una situazione comune.

Esempio: età 15 in una verifica `età >= 14`.

## Caso limite

È vicino a un confine importante.

Esempi:

```text
13
14
```

per la soglia 14.

## Controesempio

È un dato che mostra che la nostra soluzione non funziona come pensavamo.

Cercare controesempi non significa voler “rompere” il lavoro di qualcuno: significa verificarlo seriamente.

---

# 8. Error Clinic: tre errori diversi

## Ho capito male il problema

La specifica chiede la media, ma io progetto la somma.

Il programma potrebbe essere eseguito perfettamente e restare comunque sbagliato.

## L'algoritmo è sbagliato

Ho capito la richiesta, ma ho ordinato male i passi o dimenticato un caso.

## L'esecuzione fallisce

L'algoritmo può essere corretto, ma un futuro programma può contenere un errore di sintassi, un dato non valido o un altro problema di esecuzione.

Questa distinzione ci aiuterà a fare debug senza cambiare cose a caso.

---

# 9. Micro-lab senza computer

Per ciascuna consegna annota:

```text
INPUT
OUTPUT
VINCOLI
PASSI
UN CASO NORMALE
UN CASO LIMITE
```

Proposte:

1. calcolare il resto;
2. decidere se una temperatura supera una soglia;
3. trovare il maggiore tra due valori;
4. descrivere un percorso di tre mosse su una griglia.

Poi scambia il foglio con un compagno: deve poter seguire i passi senza chiederti che cosa intendevi.

---

# 10. Diagnostic iniziale

Il diagnostic non è una verifica con voto.

Serve a capire da dove parte la classe.

Domande possibili:

- quali dati servono?;
- quale risultato è richiesto?;
- quale passo manca?;
- questo procedimento termina?;
- quale esempio proveresti per primo?.

Non serve conoscere parole tecniche perfette: conta il ragionamento.

---

# Minimum mastery checkpoint

Prima di proseguire dovresti riuscire a:

1. spiegare con parole tue problema/algoritmo/programma;
2. estrarre input e output da una consegna breve;
3. segnalare un'informazione mancante;
4. ordinare una sequenza semplice di passi;
5. proporre almeno due casi diversi;
6. dire perché un solo esempio non garantisce che la soluzione sia corretta.

## Recap

```text
capire il problema
→ separare dati e risultato
→ costruire passi eseguibili
→ provare esempi diversi
→ correggere il modello prima del codice
```

Prossimo modulo: trasformiamo il problema in pseudocodice e impariamo a fare un trace manuale sistematico.

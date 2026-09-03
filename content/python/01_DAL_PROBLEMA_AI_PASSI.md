# M01 — Dal problema ai passi: specifica, pseudocodice e trace

> **Stato:** draft  
> **UDA:** PY2-01 — Problem solving, algoritmi e flow chart  
> **Prerequisiti:** M00; nessun linguaggio di programmazione richiesto

## Obiettivi

Alla fine di questo modulo dovresti saper:

- leggere una specifica breve e separare dati, risultato e vincoli;
- decomporre un problema in passi piccoli e controllabili;
- riconoscere un algoritmo ambiguo, incompleto o non terminante;
- scrivere pseudocodice semplice senza mascherarlo da Python;
- eseguire un dry-run manuale;
- annotare come cambia lo stato durante l'esecuzione;
- scegliere casi normali, casi limite e controesempi.

---

# 1. Una specifica è un contratto da capire

Problema:

> Leggi due prezzi e indica quale dei due è maggiore. Se sono uguali, dichiaralo.

Prima di pensare alla soluzione estraiamo:

```text
INPUT  → prezzo A, prezzo B
OUTPUT → A maggiore / B maggiore / uguali
```

La parola **uguali** è importante: senza quel caso una soluzione apparentemente corretta potrebbe essere incompleta.

Domanda guida:

> Che cosa deve essere vero dell'output per ogni input ammesso?

---

# 2. Decomporre non significa complicare

Una soluzione utile può essere divisa così:

```text
1. acquisisci A
2. acquisisci B
3. confronta A e B
4. scegli uno dei tre risultati
5. comunica il risultato
```

Non serve spezzare ogni gesto in decine di micro-passaggi.

La decomposizione serve a rendere visibili:

- decisioni;
- trasformazioni dei dati;
- punti in cui potrebbe mancare un caso;
- parti che potremo verificare separatamente.

---

# 3. Ambiguo per chi?

Considera:

```text
1. prendi due numeri
2. scegli quello giusto
3. stampa
```

Per l'autore può sembrare chiaro, ma **“quello giusto”** non definisce una regola eseguibile.

Un algoritmo deve comunicare la decisione, non solo l'intenzione.

Versione migliore:

```text
se A > B
    risultato ← A
altrimenti se B > A
    risultato ← B
altrimenti
    risultato ← "uguali"
```

Qui la freccia `←` significa “assegna/aggiorna il valore concettuale”, non è sintassi Python.

---

# 4. Pseudocodice: scrivere per persone

Lo pseudocodice non ha un unico standard universale per il nostro corso.

Usiamo convenzioni semplici e coerenti:

```text
LEGGI dato
ASSEGNA nome ← espressione
SE condizione
    ...
ALTRIMENTI
    ...
FINE SE
MOSTRA valore
```

Più avanti useremo anche:

```text
MENTRE condizione
    ...
FINE MENTRE
```

Lo scopo è esprimere l'algoritmo senza essere bloccati dalla sintassi di un linguaggio.

---

# 5. Non scrivere “Python travestito” troppo presto

Se ancora non conosci Python, questo:

```text
if x >= 10:
    print(x)
```

non è davvero pseudocodice neutro: introduce già regole di un linguaggio specifico.

Per ora preferiamo:

```text
SE x >= 10
    MOSTRA x
FINE SE
```

Quando arriverà Python, collegheremo idee già comprese a una sintassi concreta.

---

# 6. Dry-run: eseguire con carta e penna

Algoritmo:

```text
LEGGI prezzo
ASSEGNA sconto ← 0
SE prezzo > 100
    ASSEGNA sconto ← 10
FINE SE
ASSEGNA finale ← prezzo - sconto
MOSTRA finale
```

Proviamo `prezzo = 120`.

| passo | prezzo | sconto | finale | output |
|---:|---:|---:|---:|---:|
| iniziale | 120 | — | — | — |
| sconto iniziale | 120 | 0 | — | — |
| decisione | 120 | 10 | — | — |
| calcolo | 120 | 10 | 110 | — |
| output | 120 | 10 | 110 | 110 |

Il trace rende visibile lo **stato** dell'algoritmo.

---

# 7. Lo stato cambia nel tempo

Una variabile concettuale non è soltanto un'etichetta su un foglio.

Durante il trace può cambiare:

```text
saldo: 100 → 80 → 65
```

Per capire un algoritmo chiediti spesso:

> Che cosa rappresenta questo valore **dopo** il passo appena eseguito?

Questa domanda tornerà nei cicli, nei contatori e negli accumulatori.

---

# 8. Ordine dei passi

Algoritmo sbagliato:

```text
1. MOSTRA totale
2. LEGGI prezzo
3. ASSEGNA totale ← prezzo + 5
```

Il risultato viene chiesto prima di essere determinato.

Correzione minima:

```text
1. LEGGI prezzo
2. ASSEGNA totale ← prezzo + 5
3. MOSTRA totale
```

Il debug non richiede sempre di riscrivere tutto: cerca la **modifica minima che ripristina il contratto**.

---

# 9. Finitezza e terminazione

Procedura:

```text
ripeti "prova ancora"
```

Quando finisce?

Non è dichiarato.

Una procedura automatica deve avere una regola di terminazione o un numero finito di passi.

In M03 studieremo i cicli e impareremo a cercare esplicitamente:

```text
inizializzazione
condizione
aggiornamento
uscita
```

---

# 10. Test prima del programma

Per il problema “maggiore tra due prezzi” scegliamo:

```text
10, 5   → primo maggiore
5, 10   → secondo maggiore
7, 7    → uguali
```

Poi aggiungiamo, se ammessi:

```text
0, 0
-2, -5
```

Non dobbiamo aspettare di avere un programma per progettare test utili.

---

# 11. Error Clinic

## Passaggio mancante

Calcolo una media senza aver contato quanti valori ci sono.

## Stato senza significato

Uso `totale`, ma non so spiegare che cosa rappresenta in un certo punto.

## Caso non coperto

Gestisco A > B e B > A, ma non A = B.

## Procedura non terminante

Ripeto un passo senza una condizione di uscita.

Per ogni errore prova a rispondere:

1. qual è il contratto violato?;
2. qual è il primo passo in cui il trace diverge?;
3. qual è la modifica minima?.

---

# 12. Laboratorio: dal testo all'algoritmo

Scegli uno dei problemi:

- tariffa base + supplemento sopra una soglia;
- maggiore tra due valori;
- temperatura dentro/fuori intervallo;
- tre mosse di un robot su griglia.

Consegna:

```text
INPUT
OUTPUT
VINCOLI
PSEUDOCODICE
2 casi normali/alternativi
1 caso limite
TRACE di almeno un caso
```

Il compagno che riceve il tuo lavoro deve poter simulare l'algoritmo senza chiederti spiegazioni aggiuntive.

---

# Minimum mastery checkpoint

Dovresti saper:

1. estrarre input/output/vincoli;
2. trasformare una consegna in passi ordinati;
3. usare pseudocodice leggibile e non dipendente da Python;
4. fare un trace con almeno una variabile che cambia;
5. riconoscere un caso non coperto;
6. spiegare perché un algoritmo finisce;
7. proporre test prima della codifica.

## Recap

```text
specifica
→ decomposizione
→ pseudocodice
→ trace
→ casi di test
```

Prossimo modulo: rappresentiamo sequenze e decisioni con diagrammi di flusso.

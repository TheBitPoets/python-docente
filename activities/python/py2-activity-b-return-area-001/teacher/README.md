# M13 P2 canary — note docente

Activity: `py2-activity-b-return-area-001`

## Perché esiste

È il primo consumer reale candidato del profilo TheBitLab `python-function-v1` (P2 — function behavior).

La Controlled Change è intenzionalmente minima:

```text
calcolo già corretto
+ print(area)
→ return area
```

L'obiettivo non è verificare la moltiplicazione, ma distinguere semanticamente **mostrare** un valore da **restituirlo al chiamante**.

## Oracle

La soluzione deve superare tre chiamate deterministiche di `area_rettangolo(base, altezza)`.

Lo starter stampa valori numericamente corretti ma ritorna `None`; deve quindi fallire i test P2. Se lo starter passasse, il profilo starebbe accidentalmente valutando stdout invece del valore di ritorno.

## Boundary

- `function_tests` è teacher-only e non deve entrare nello scaffold studente;
- expected return resta sul trusted host;
- il worker riceve soltanto nome funzione + argomenti;
- il grading autorevole usa il Docker assignment-runner P2 candidate;
- questa Activity non certifica da sola P2 e non autorizza materializzazione massiva.

## Stato

DRAFT / canary. Promuovere solo dopo consumer CI contro uno SHA TheBitLab P2 esatto e dopo integrazione del profilo nel percorso managed normale.

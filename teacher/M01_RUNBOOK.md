# M01 — Runbook docente

## Modulo

**Dal problema ai passi: specifica, pseudocodice e trace**  
UDA PY2-01 — Problem solving, algoritmi e flow chart.

Stato: draft.

## Obiettivo docente

Portare la classe dalla comprensione intuitiva di M00 a una prima rappresentazione controllabile dell'algoritmo:

```text
specifica
→ decomposizione
→ pseudocodice
→ trace
→ casi di test
```

Il traguardo non è insegnare una sintassi di pseudocodice rigida. È far sì che un'altra persona possa eseguire i passi senza interpretare intenzioni nascoste.

---

# Preparazione

## Ambiente

Nessuna dipendenza digitale obbligatoria.

Materiale consigliato:

- lesson `content/python/01_DAL_PROBLEMA_AI_PASSI.md`;
- slide `slides/python/modules/01_DAL_PROBLEMA_AI_PASSI.md`;
- fogli per trace table;
- 2 algoritmi volutamente difettosi;
- una specifica finale nuova.

Non mostrare ancora la traduzione Python completa.

---

# Collocazione nella settimana 1

Dopo M00, usare circa:

```text
60–75 min teoria attiva M01
+ laboratorio restante della settimana
```

M00 + M01 insieme costituiscono la prima settimana da 3 ore.

---

# Teoria attiva

## 0–15 min — specifica e casi

Problema:

> indica il maggiore tra due prezzi; se uguali dichiaralo.

Far elencare i tre casi prima di costruire la soluzione:

```text
A > B
B > A
A = B
```

## 15–30 min — decomposizione

Costruire insieme 4–6 passi.

Poi mostrare una versione troppo vaga:

```text
scegli quello giusto
```

Chiedere perché non è operativa.

## 30–45 min — pseudocodice

Introdurre solo le convenzioni che servono:

```text
LEGGI
ASSEGNA ←
SE / ALTRIMENTI / FINE SE
MOSTRA
```

Non valutare punteggiatura o maiuscole se il significato è chiaro e coerente.

## 45–60 min — trace

Usare un algoritmo con una variabile che cambia.

Far compilare almeno:

```text
passo
stato prima/dopo
condizione
output
```

## 60–75 min — finitezza e test

Mostrare una procedura senza regola di uscita e chiedere:

> Quale informazione ci manca per sapere che termina?

Poi progettare test prima di qualsiasi codice.

---

# Laboratorio della settimana 1

## Fase A — riordino

Consegnare 6–8 passi mescolati.

Lo studente:

- ordina;
- identifica input/output;
- segnala un passo mancante.

## Fase B — controlled change

Pseudocodice volutamente ambiguo/incompleto.

Obiettivo: correggere solo i punti necessari.

## Fase C — design

Da una specifica nuova produrre:

```text
input
output
vincoli
pseudocodice
2 casi diversi
1 caso limite
trace di un caso
```

## Fase D — debug

Usare almeno due difetti tra:

- ordine sbagliato;
- variabile concettuale non definita;
- caso non coperto;
- procedura non terminante.

---

# Feedback docente

Preferire domande che rendono visibile il modello mentale:

- Che cosa rappresenta questa variabile adesso?;
- Qual è il primo passo in cui il risultato diverge?;
- Quale input fa emergere il problema?;
- Questa correzione cambia più parti del necessario?;
- Come sai che la procedura termina?.

Evitare “riscrivi da capo” come default.

---

# Minimum mastery gate

Prima di M02 lo studente dovrebbe, su problemi semplici, saper:

- produrre pseudocodice leggibile;
- eseguire un trace;
- riconoscere un caso non coperto;
- spiegare una regola di terminazione;
- progettare test senza aspettare il programma.

Se la classe non è stabile, M02 può iniziare con diagrammi lineari senza anticipare selezioni complesse.

---

# Handoff a M02

Chiudere mostrando lo stesso pseudocodice in forma di flusso:

```text
passi testuali
→ nodi
→ frecce
→ decisione true/false
```

La nuova rappresentazione non cambia l'algoritmo: cambia il modo in cui osserviamo il controllo.

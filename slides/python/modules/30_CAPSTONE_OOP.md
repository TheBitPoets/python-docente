---
marp: true
paginate: true
size: 16:9
title: M30 — Capstone OOP
---

# M30 — Capstone OOP
## Integrare ciò che sappiamo, senza gonfiare il progetto

PY2-10 — Classi, oggetti e capstone

---

# Finestra reale

```text
M29 / settimana 31
→ skeleton progettuale

M30 / settimana 32
→ implementazione + integration + review

Checkpoint C / settimana 33
→ eventuale finalizzazione / recupero / evidence
```

Nessuna settimana extra e nessun nuovo prerequisito.

---

# Che cosa deve dimostrare il capstone completo?

- responsabilità OOP significative;
- composizione/collaborazione reale;
- almeno un invariante;
- una scelta di struttura dati motivata;
- metodi con responsabilità riconoscibili;
- almeno 5 casi/test complessivi;
- almeno un edge case/transizione rifiutata;
- una evidence bug-fix/regression/refactor;
- breve spiegazione del design.

Non serve un numero alto di classi.

---

# Prima il modello, poi il codice

```text
problema
→ responsabilità
→ classi candidate
→ stato
→ metodi
→ invarianti
→ composizione
→ strutture dati
→ casi
```

Il progetto deve essere spiegabile prima di diventare grande.

---

# Due responsabilità, non “due classi perché sì”

Esempio:

```text
Veicolo
→ posizione / carico / regole

Missione
→ checkpoint / completamento
→ usa il Veicolo
```

La composizione deve avere un significato reale nel dominio.

---

# Variante generica sempre disponibile

Il capstone core non dipende da:

- Romeo;
- hardware;
- rete;
- GUI;
- database;
- web.

Un piccolo dominio simulato è sufficiente.

---

# Variante Romeo

Solo se `romeo-sim` è certificato.

```text
Missione
└─ usa Robot
```

Gli outcome restano gli stessi della variante generica.

Hardware fisico non è requisito core.

---

# Sviluppo incrementale

```text
1. skeleton + casi
2. prima responsabilità
3. invariante + test
4. collaboratore
5. composizione
6. integrazione
7. edge case
8. bug/regression
9. refactor
10. spiegazione
```

Piccoli checkpoint, non un mega-codice alla fine.

---

# Struttura dati

Riusa almeno una scelta significativa:

```text
list / tuple / set / dict
```

Domanda:

> quale struttura rende naturali le operazioni dominanti?

Non usare più collezioni del necessario.

---

# Invariante

Scrivi almeno una proprietà che deve restare vera.

Esempi:

```text
0 <= energia <= capacita
checkpoint_completati <= checkpoint_totali
carico <= capacita
```

L'invariante suggerisce i casi limite.

---

# Test minimi

Progetta casi su:

- costruzione;
- stato osservabile;
- transizione valida;
- transizione rifiutata/confine;
- collaborazione;
- indipendenza fra istanze quando pertinente.

La suite concreta dipende dal dominio.

---

# Regression + refactor

```text
bug/caso mancante
→ test rosso
→ fix
→ tutti verdi
→ refactor
→ ancora verdi
```

Basta una evidence reale e spiegabile.

---

# Git G1 embedded

Non è un nuovo corso Git.

Prima di un checkpoint significativo:

```text
git status
→ git diff
→ test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log / git show
```

Non creare commit artificiali soltanto per aumentare il numero.

---

# Se devi recuperare

Riduci il dominio:

```text
meno funzionalità
una relazione di composizione
una struttura dati semplice
niente file/Romeo/enrichment
```

Ma gli outcome core non diventano opzionali.

Se una evidence manca nel prodotto ridotto, può essere dimostrata con un micro-task separato.

---

# Persistenza è opzionale

M26 esiste, ma il capstone non deve usare file soltanto “per usare tutto il corso”.

Se la persistenza complica il progetto e non serve al dominio, lasciala fuori.

Proteggiamo l'OOP core.

---

# Enrichment soltanto dopo il core

- `__str__/__repr__`;
- property;
- inheritance semplice;
- dataclass come confronto;
- file;
- Romeo più ricco.

Nessuno è prerequisito del prodotto base.

---

# Spiegazione finale

Devi poter rispondere:

1. Quali sono le responsabilità?
2. Dove avviene la composizione?
3. Quale invariante proteggi?
4. Perché quella struttura dati?
5. Quale edge case è importante?
6. Quale bug hai corretto?
7. Che cosa miglioreresti dopo?.

---

# Traguardo del secondo anno

```text
problema
→ algoritmo
→ funzioni
→ strutture dati
→ oggetti
→ invarianti
→ composizione
→ test/debug/refactor
→ spiegazione
```

Non:

```text
più classi + più framework + più righe
```

Checkpoint C finalizza/recupera: non introduce nuovi concetti.

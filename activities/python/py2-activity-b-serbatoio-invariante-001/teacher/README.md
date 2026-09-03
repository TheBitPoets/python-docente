# M28 P3 canary — Serbatoio e invariante

Questa Activity è il **primo consumer reale P3** del corso Python seconda.

Non è autorizzazione alla produzione massiva di Activity OOP e non implica stabilità del toolchain.

## Outcome osservato

La Controlled Change misura comportamento dell'oggetto, non output testuale:

```text
stato iniziale
→ transizione valida
→ transizione non valida rifiutata
→ stato invariato dopo il rifiuto
→ istanze indipendenti
```

Contratto didattico coerente con M28:

```text
0 <= livello <= capacita
```

Il metodo `aggiungi` usa la policy beginner della lesson:

```text
operazione valida   -> cambia stato + True
operazione invalida -> stato invariato + False
```

Le eccezioni sono già coperte dalla certificazione piattaforma P3 e non vengono forzate in questa Activity.

## Oracle intenzionale

```text
solution: 5/5
starter:  3/5
```

Lo starter passa:

- costruzione/stato iniziale;
- aggiunta valida;
- indipendenza fra istanze.

Fallisce invece i due outcome che motivano la Controlled Change:

- overflow oltre capacità;
- quantità negativa.

Quindi il canarino non premia una classe che semplicemente modifica un attributo: deve proteggere davvero l'invariante.

## P3 candidate

Consumer pin:

```text
TheBitPoets/2cornot2c
PR #767
source = 1c2889530d0bdd485fa68b233311cd5f91cd67c2
profile = python-object-v1
```

La branch P3 eredita ancora il manifest `2026.08.2` dal candidato P2+P4 #766. Questo consumer certifica **l'esatto source SHA**, non promuove `2026.08.2` a nuova release P2+P3+P4 e non autorizza pubblicazione con identità riutilizzata.

Prima di una stabilità reale serve una distinta decisione di release, pubblicazione GHCR e digest immutabile verificato.

## Redaction

`object_tests` e gli expected teacher-side non devono comparire nello scaffold o nel report Student Lab pubblico. Il consumer CI verifica entrambe le superfici.

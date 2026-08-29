# Python Activities

Activity root del curriculum Python.

Stato attuale: **quattro canarini deliberati + authoring draft**, non produzione massiva.

Le Activity definitive usano lo schema TheBitLab Activity 1.0 e la tassonomia A–F.

## Canary materializzati

```text
M04  py2-activity-b-input-somma-001             P1 stdin/stdout
M13  py2-activity-b-return-area-001             P2 python-function-v1
M26  py2-activity-b-file-risultato-001          P4 python-filesystem-v1
M28  py2-activity-b-serbatoio-invariante-001    P3 python-object-v1
```

### M04 / P1

Prima Activity Python beginner reale: `main.py` single-file, test deterministici stdin/stdout e scaffold studente separato dagli asset teacher/solution.

### M13 / P2

Canary di comportamento funzione. La controlled change distingue `print(area)` da `return area`: stdout numericamente corretto non soddisfa il contratto se la funzione non restituisce il valore.

### M26 / P4

Canary di comportamento filesystem. La controlled change distingue il calcolo/stampa del totale dalla produzione reale di `risultato.txt`; fixture e oracle docente restano redatti dal report studente.

### M28 / P3

Primo consumer OOP non-Romeo. Il `Serbatoio` misura comportamento dell'oggetto e invariante:

```text
0 <= livello <= capacita
```

Oracle certificato sul candidato P3 exact-source:

```text
solution = 5/5
starter  = 3/5
```

Lo starter passa stato iniziale, transizione valida e indipendenza delle istanze, ma fallisce overflow e quantità negativa perché modifica lo stato quando dovrebbe rifiutare la transizione. Il normale Docker ExecutionService/Student Lab usa `python-object-v1` e redige gli `object_tests` teacher-only.

P3 è ancora un **source candidate**, non una release immutabile: il source certificato è `TheBitPoets/2cornot2c@1c2889530d0bdd485fa68b233311cd5f91cd67c2`. La branch eredita il manifest `2026.08.2` dal candidato P2+P4 e non deve essere pubblicata sotto quella stessa identità come se fosse la medesima release.

## Regola di materializzazione

```text
outcome
→ profilo evidence corretto
→ implementazione piattaforma
→ certificazione reale
→ un canary consumer
→ promozione stable
→ materializzazione più ampia
```

I quattro canarini sono prove tecniche/didattiche deliberate. Non autorizzano ancora la produzione in massa delle Activity successive, né `Content Pack 1.0 / approved`, né il GO classroom.

Per il profilo beginner seguire `doc/PYTHON_ACTIVITY_RUNTIME_CONTRACT.md`.

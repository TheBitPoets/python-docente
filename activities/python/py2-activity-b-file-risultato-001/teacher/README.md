# M26 P4 canary — note docente

Activity: `py2-activity-b-file-risultato-001`  
UDA: PY2-09  
Profilo candidate: `python-filesystem-v1`

## Intento didattico

La modifica controllata deve isolare il passaggio:

```text
print(totale)
→
Path("risultato.txt").write_text(..., encoding="utf-8")
```

La lettura, il parsing e la somma sono gia corretti nello starter.

## Oracle di certificazione

Fixture autorevole di grading:

```text
fixtures/misure.txt
12
15
9
```

Artifact atteso:

```text
risultato.txt = "36\n"
```

La fixture pubblica nello scaffold e volutamente diversa. Il grading deve quindi osservare il comportamento sul filesystem e non un valore hardcoded.

## Boundary

Questa Activity e un solo canarino P4. Non autorizza la materializzazione in massa finche #757 non ha:

- consumer CI reale;
- normale Student Lab dispatch;
- student-report redaction;
- release/stable promotion coerente con il toolchain lifecycle.

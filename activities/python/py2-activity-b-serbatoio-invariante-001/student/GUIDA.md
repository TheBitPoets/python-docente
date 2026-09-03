# Proteggi l'invariante del `Serbatoio`

Lo starter costruisce già un oggetto con due attributi:

```text
capacita
livello
```

e il metodo `aggiungi(...)` modifica già lo stato.

Il problema è che al momento **accetta qualunque quantità**.

## Obiettivo

Completa soltanto il metodo `aggiungi` affinché rispetti questa regola:

```text
0 <= livello <= capacita
```

Contratto richiesto:

- se l'aggiunta è valida, il livello cambia e il metodo restituisce `True`;
- se la quantità è negativa, il metodo restituisce `False` e lo stato non cambia;
- se l'aggiunta supererebbe la capacità, il metodo restituisce `False` e lo stato non cambia.

Non cambiare il nome della classe, degli attributi o del metodo.

## Come ragionare

Per ogni chiamata chiediti sempre:

1. qual è lo **stato prima**;
2. la transizione è ammessa dall'invariante?;
3. quale valore deve restituire il metodo?;
4. qual è lo **stato dopo**.

Ricorda che due oggetti `Serbatoio` diversi devono mantenere stati indipendenti.

## Prima di consegnare

Prova mentalmente almeno:

- un'aggiunta valida;
- una quantità negativa;
- un'aggiunta che supererebbe la capacità;
- due istanze diverse, modificandone soltanto una.

Non aggiungere `input()`, `print()` o codice di prova obbligatorio nel file consegnato.

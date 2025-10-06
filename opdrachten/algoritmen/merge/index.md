# Merge lists

Schrijf een functie `merge_lists`. Deze neemt twee gesorteerde lijsten van integers aan (`lst1` en `lst2`), en voegt ze samen in een nieuwe lijst. De nieuwe lijst moet ook gesorteerd zijn.

Het liefst willen we dit efficiënt doen. Efficiënt betekent hier dat je algoritme zo weinig mogelijk stappen neemt voor het samenvoegen.

## Voorbeeld

    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]

De strategie is: bekijk per **stap** of je een getal van `lst1` of van `lst2` kunt toevoegen. Dat moet de kleinste van de twee zijn!

Als je een getal van een lijst hebt toegevoegd moet je die "wegstrepen" zodat je deze niet nog een keer gaat bekijken. Dat doe je door bij te houden hoeveel getallen van elke lijst je al hebt toegevoegd.

## Stappenplan

0. Doctests

    - Schrijf een `def` met meer doctests.

1. Variabelen

    - Maak een lege lijst `result`.
    - Maak twee tellers `i` en `j` die bijhouden hoeveel getallen van `lst1` en `lst2` we al hebben toegevoegd (begint dus op 0).

2. Loop 1

    - Maak een `while`-loop die eindigt als je helemaal door `lst1` of `lst2` bent.
    - Vergelijk `lst1[i]` en `lst2[j]` om te kijken welke het kleinste element is.
        - Voeg die toe aan `result`.
        - Hoog teller `i` of `j` op, afhankelijk van welke lijst je hebt gekozen.

3. Loop 2

    - Als de lijsten niet even lang zijn, dan bevat één van de twee nog getallen die groter zijn dan alle andere, en nog toegevoegd moeten worden aan het resultaat.
    - Bepaal eerst welke van de twee lijsten nog getallen bevat (als dat zo is).
    - Maak een `for`-loop die vanaf de juiste positie uit de juiste lijst de rest van de getallen overneemt in `result`.

4. Return

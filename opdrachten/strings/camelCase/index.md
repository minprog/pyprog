# camelCase of snake_case?

Over het algemeen wordt er bij programmeren in Python gebruik gemaakt van snake_case, waarbij er een `_` tussen de woorden staat. Er zijn echter ook mensen die camelCase prefereren.
Bij de camelCase begint de naam van de variabele of functie met een kleine letter, maar hierbij begint elk nieuw woord met een hoofdletter zodat de verschillende woorden binnen de naam nog steeds goed te onderscheiden zijn.
Zo krijg je namen als `check`, `convertInput` of `readFromFile`.
In Python is het dus gebruikelijk om `snake_case` te gebruiken. Daarom schrijven we een programma dat onze namen kan omzetten naar dat formaat.

## Opdracht

Schrijf, in een bestand genaamd `camelcase.py`, een programma dat de naam van een variabele in camelCase omschrijft snake_case. Maak daarbij een functie `convert` voor het algoritme van het omzetten van de string.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python camelcase.py
    camelCase: check
    snake_case: check

    $ python camelcase.py
    camelCase: convertInput
    snake_case: convert_input

    $ python camelcase.py
    camelCase: readFromFile
    snake_case: read_from_file

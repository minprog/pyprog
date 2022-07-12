# camelCase

## camelCase of snake_case?

Over het algemeen hebben jullie bij het programmeren gebruik gemaakt van snake_case. Waarbij er een `_` tussen de woorden staat. Er zijn echter ook mensen die de camelCase prefereren.
Bij de camelCase begint de naam van de variabele of functie met een kleine letter maar hierbij begint elk nieuw woord met een hoofdletter zodat de verschillende woorden binnen de naam nog steeds goed te onderscheiden zijn.
Zo kan je bijvoorbeeld de functie `check` hebben, maar wil je iets specifieks checken bijvoorbeeld de input krijg je bijvoorbeeld de naam `checkInput` of `checkInputFromUser`.

## Opdracht

Schrijf, in een bestand genaamd `camel.py`, een programma dat een naam in camelCase omschrijft naar een naam in snake_case.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def convert(name: str) -> str:
        """
        Converteer een naam van camelCase naar snake_case
        """

    if __name__ == '__main__':
        Vraag de gebruiker om input, roep je functie aan, en print het resultaat.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python camel.py
    camelCase: check
    snake_case: check

    $ python camel.py
    camelCase: checkInput
    snake_case: check_input

    $ python camel.py
    camelCase: checkInputFromUser
    snake_case: check_input_from_user

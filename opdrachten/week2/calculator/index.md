# Calculator

Het is inmiddels duidelijk dat Python wiskundige formules begrijpt en deze voor ons kan uitrekenen. Laten we deze kracht gebruiken om onze eigen gebruikers snel de uitkomst van sommen te geven die ze zelf verzinnen.
Daarom gaan we een programma schrijven dat de gebruiker vraagt een formule te geven, waarna het programma de uitkomst berekent.

## Opdracht

Schrijf, in een bestand genaamd `calculator.py`, een programma dat de gebruiker vraagt een formule in te tikken en het antwoord van de formule geeft als output.

* De formule die wordt gegeven door de gebruiker is van de vorm `x y z` met een spatie tussen de `x` en `y`, en `y` en `z`.
* Hier zijn de `x` en `z` integers en is de `y` één van de operaties `+, -, *, / `.
* Je mag aannemen dat de gebruiker `z` niet nul maakt als voor `y` de operatie `/` is gekozen (dat zou een probleem zijn!).
* De output van het programma moet een float zijn.
* Je programma moet ook kunnen omgaan met negatieve getallen.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def perform_operation(x: int, y: str, z: int) -> float:
        """
        Bereken het resultaat van de operatie y toegepast op x en z.
        De output is een float.
        """

    def evaluate(formula: str) -> float:
        """
        Bereken het resultaat van een formule die in een string staat.
        Deze functie bereidt de berekening voor door de onderdelen van de
        formule uit de string te halen. De output is een float.
        """

    if __name__ == '__main__':
        <Invoer, functies, uitvoer>

## Tips

* Je kunt de `split`-methode gebruiken net als in de opdracht Etenstijd. Experimenteer even met `split` in Python zodat je je idee voor een oplossing kunt ontwikkelen.

* Moet `main` alleen `evaluate` aanroepen, die daarna `perform_operation` aanroept? Of moet `main` beide functies aanroepen? Bestudeer de types van (de argumenten van) de functies om te achterhalen welke optie past.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python calculator.py
    1 + 1
    2.0

    $ python calculator.py
    100 - 9
    91.0

    $ python calculator.py
    4 * 6
    24.0

    $ python calculator.py
    3 / 8
    0.375

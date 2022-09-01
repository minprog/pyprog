# Calculator

Het is inmiddels duidelijk dat Python wiskundige formules begrijpt en deze voor ons kan uitrekenen. Laten we deze kracht gebruiken om onze eigen gebruikers snel de uitkomst van sommen te geven die ze zelf verzinnen.
Daarom gaan we een programma schrijven dat de gebruiker vraagt een formule te geven, waarna het programma de uitkomst berekent.

## Opdracht

Schrijf, in een bestand genaamd `calc.py`, een programma dat de gebruiker vraagt een formule in te tikken en het antwoord van de formule geeft als output.

* De formule die wordt gegeven door de gebruiker is van de vorm `x y z` met een spatie tussen de `x` en `y`, en `y` en `z`.
* Hier zijn de `x` en `z` integers en is de `z` één van de operaties `+, -, *, / `.
* Je mag aannemen dat de gebruiker `z` niet nul maakt als voor `y` de operatie `/` is gekozen (dat zou een probleem zijn!).
* De output van het programma moet een float zijn.
* Je programma moet ook kunnen omgaan met negatieve getallen.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def get_values(expression: str):
        """
        Krijg de waardes voor x, y, z van de expressie. Zorg dat in je output de x
        en z waardes integers zijn en de y waarde een string die bestaat uit 1
        karakter.
        """

    def get_result(x: int, y: str, z: int) -> float:
        """
        Bereken het resultaat van de expressie gebasseerd op de x, y, en z waardes.
        Je output is een float.  
        """

    if __name__ == '__main__':
        <Invoer, functies, uitvoer>

## Tips

* De getallen in de expressie kunnen uit meerdere cijfers bestaan (bijvoorbeeld 135). Denk dus even na hoe je de expressie op zo'n manier splitst zodat je zowel honderdtallen als losse cijfers kan verwerken.
* Je kan meerdere waardes uit een string uitpakken door met de split() functie de string op te splitsen bij een specifiek scheidingsteken; `a, b = "hello world!".split(" ")`. Let op dat de string nu bij elke 'spatie' wordt opgesplitst en dat het aantal variabelen waar je naar uitpakt gelijk moet zijn aan het resultaat van de opsplitsing.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python wiskunde_verwerker.py
    1 + 1
    2.0

    $ python wiskunde_verwerker.py
    100 - 9
    81.0

    $ python wiskunde_verwerker.py
    4 * 6
    24.0

    $ python wiskunde_verwerker.py
    3 / 8
    0.325

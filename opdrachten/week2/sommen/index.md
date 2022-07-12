# Sommen

## Verwerken

Het is inmiddels duidelijk dat Python wiskunde formules begrijpt en deze voor ons kan uitrekenen. Stel je weet niet hoe Python werkt, zou het alsnog leuk zijn om deze kracht van Python te kunnen gebruiken.
Daarom gaan we een programma schrijven dat de gebruiker vraagt een formule te geven die wordt uitgerekend door Python.
In andere woorden: een programma dat wiskunde verwerkt en omzet tot een antwoord.

## Opdracht

Schrijf, in een bestand genaamd `wiskunde_verwerker.py`, een programma dat de gebruiker vraagt een formule te geven en het antwoord van de formule geeft als output.

* De formule die wordt gegeven door de gebruiker is van de vorm `x y z` met een spatie tussen de `x` en `y`, en `y` en `z`. Hier zijn de `x` en `z` integers en is de `z` een van de volgende operaties `+, -, *, / `.
* Je mag aannemen dat de gebruiker `z` niet nul maakt als voor `y` de operatie `/` is gekozen.
* De output van het programma moet een float zijn.
* Je programma moet ook kunnen omgaan met min getallen.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.


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
        Prompt de gebruiker voor input, roep je functies aan, en print het resultaat.

## Tips

* De getallen in de expressie kunnen uit meerdere cijfers bestaan (bijv 135), hoe zorg je ervoor dat je de expressie op een manier split zodat je zowel honderdtallen als losse cijfers kan verwerken.

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

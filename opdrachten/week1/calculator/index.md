# Calculator

Het is inmiddels duidelijk dat Python wiskundige formules begrijpt en deze voor ons kan uitrekenen. Laten we deze kracht gebruiken om onze eigen gebruikers snel de uitkomst van sommen te geven die ze zelf verzinnen.
Daarom gaan we een programma schrijven dat de gebruiker vraagt een formule te geven, waarna het programma de uitkomst berekent.

## Opdracht

Schrijf, in een bestand genaamd `calculator.py`, een programma dat de gebruiker vraagt een formule in te tikken en het antwoord van de formule geeft als output.

* De formule die wordt gegeven door de gebruiker is van de vorm `x y z` met een spatie tussen de `x` en `y`, en `y` en `z`.
* Hier zijn de `x` en `z` getallen en is de `y` één van de operaties `+, -, *, / `.
* Het antwoord moet als float geprint worden.
* Je programma moet ook kunnen omgaan met negatieve getallen.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python calculator.py
    1 + 1
    2.0

    $ python calculator.py
    100 - 9
    91.0

    $ python calculator.py
    4 * -6
    -24.0

    $ python calculator.py
    3 / 8
    0.375

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def evaluate(x: int, y: str, z: int) -> float:
        """
        Bereken het resultaat van de operatie y toegepast op x en z.
        """

    if __name__ == '__main__':
        <Invoer, verwerken, functie, uitvoer>

## Tips

* De functie `evaluate` krijgt twee `int`s en een `str` mee. Die moet je dus klaarmaken in de `main`. De functie geeft een float terug, en mag niks printen (anders zou dat in de docstring staan).

* Je kunt de `split`-methode gebruiken net als in de opdracht Etenstijd. Experimenteer even met `split` in Python zodat je je idee voor een oplossing kunt ontwikkelen.

* Je mag aannemen dat de gebruiker geen 0 invult voor `z` als de operatie `/` is gekozen (dat zou een probleem zijn, want delen door nul mag niet). Je hoeft hier dus geen controle voor in te bouwen.

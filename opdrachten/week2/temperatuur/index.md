# Temperatuurtabellen

Graden Celsius en graden Fahrenheit staan met elkaar in verband via `F = (18C + 320) / 10` en andersom `C = (10F - 320) / 18`. Een conversietabel kan er als volgt uitzien. Deze is op basis van de temperatuur in Celcius, en loopt van 0° tot en met 20°, in stappen van 5 graden.

|      C |   F|
|-------:|---:|
|      0 |  32|
|      5 |  41|
|     10 |  50|
|     15 |  59|
|     20 |  68|


## Opdracht

Schrijf, in een bestand genaamd `temperatuur.py`, een programma dat de gebruiker vraagt om de eenheid van temperatuur: `C` van Celsius of `F` van Fahrenheit. Vervolgens vraagt het programma om de begintemperatuur, de eindtemperatuur en de stapgrootte. Daarna wordt een nette tabel uitgeprint, met op iedere rij een temperatuur in de gekozen eenheid en daarbij de omgerekende temperatuur.

* Je programma moet niet gevoelig zijn voor hoofdletters: zowel `c` als `C` moeten worden gezien als Celsius.
* De eindtemperatuur moet groter zijn dan de begintemperatuur (als dit niet zo is wordt een "lege tabel" uitgeprint, zie voorbeelden hieronder).
* De stapgrootte moet een positief geheel getal zijn, anders moet opnieuw worden gevraagd.
* Je moet de getallen (en letters) rechts uitlijnen zoals in de voorbeelden.
* Alle temperaturen worden op gehele graden naar *beneden* afgerond.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def convert_temperature(old_type: str, old_temp: int) -> int:
        """
        Zet de temperatuur (old_temp) van het type old_type om naar
        de temperatuur van het nieuwe type.
        """

    def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
        """
        Print de conversie-tabel.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

*   Tel zeer zorgvuldig de spaties in onderstaande voorbeelden. Je programma wordt alleen goedgekeurd als de uitvoer *exact* is zoals hieronder.

*   Voor het uitlijnen van de getallen zijn er verschillende technieken. Moderne Python-programma's maken gebruik van f-strings. Hiermee kun je expressies in een string opnemen:

        f"Hierbij de som van 1 en 1: {1+1}"

    Elke expressie tussen accolades `{}` wordt geëvalueerd bij het maken van de string. Bovenstaande string is dus in dit geval gelijk aan:

        "Hierbij de som van 1 en 1: 2"

    Je kunt elke expressie opnemen, dus ook een expressie met variabelen erin:

        >>> credits = 10.5
        >>> print(f"Your credits are {credits}")
        Your credits are 10.5

    En tot slot kun je de waarde *formatten* (vandaar de naam f-string):

        >>> letter = 'a'
        >>> f"{letter:10}"
        'a         '
        >>> f"{letter:>10}"
        '         a'

    Bestudeer goed dit laatste voorbeeld want het gaat je helpen de tabel mooi uit te printen, exact volgens de voorbeelden hieronder!

*   We gaan ervan uit dat we geen temperaturen tegenkomen in de duizendtallen. Dit houdt in dat je ervan uit mag gaan dat er voor drie karakters ruimte moet zijn in de tabel, precies zoals in de voorbeelden hieronder.

## Voorbeelden

Je programma moet uiteindelijk exact werken zoals in de voorbeelden hieronder.

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? C
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 20
    Wat is de stapgrootte? 5
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 2
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 10
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 100
    Wat is de eindtemperatuur? 0
    Wat is de stapgrootte? 3
      F |   C

    $ python temperatuur.py
    Welke eenheid van temperatuur (C of F)? v
    Welke eenheid van temperatuur (C of F)? F
    Wat is de begintemperatuur? 0
    Wat is de eindtemperatuur? 9
    Wat is de stapgrootte? -3
    Wat is de stapgrootte? 0
    Wat is de stapgrootte? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

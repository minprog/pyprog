# String module

In de vorige module heb je een aantal basisoperaties voor strings gezien, zoals het opvragen van de lengte van een string met `len(...)` en het herhalen van een string met `"string" * aantal`.

Bij Python wordt een module `string` geleverd waarin een paar handige variabelen staan om te gebruiken in je eigen programma's:

- `string.ascii_lowercase` bevat alle kleine letters uit het Amerikaanse basis-alfabet (26 letters)
- `string.ascii_uppercase` bevat alle hoofdletters uit het Amerikaanse basis-alfabet (26 letters)
- `string.ascii_letters` bevat zowel kleine als hoofdletters
- `string.digits` bevat alle cijfers van 0 tot en met 9
- `string.whitespace` bevat een aantal soorten witruimte zoals de spatie en de tab

Maak een bestand genaamd `string_module.py`. Zet bovenin de regel `import string`, zodat je toegang hebt tot deze string-variabelen.

## Oefeningen

- Schrijf een functie `isalpha(...)` die een enkele letter aanneemt en bepaalt of de letter tot het Amerikaanse basis-alfabet behoort.

- Schrijf een functie `islower(...)` die een enkele letter aanneemt en bepaalt of de letter tot de kleine letters uit het Amerikaanse basis-alfabet behoort.

- Schrijf een functie `isupper(...)` die een enkele letter aanneemt en bepaalt of de letter tot de kleine letters uit het Amerikaanse basis-alfabet behoort.

- Schrijf een functie `isdigit(...)` die een enkel teken aanneemt en bepaalt of dit teken een cijfer is.

- Schrijf een functie `isblank(...)` die een enkel teken aanneemt en bepaalt of dit teken één van de soorten witruimte is.

## Hints

- Bedenk zelf welke type hints je moet toevoegen bij de functies in deze opdracht.

- In het boek op pagina 86 staat hoe je kunt testen of een string onderdeel is van een andere string. Dit concept kun je goed gebruiken voor bovenstaande oefeningen.

- Waarom het Amerikaanse basis-alfabet? Omdat veel systemen traditioneel maar een beperkt alfabet aankunnen, zijn sommige systeemfuncties beperkt tot alleen dat alfabet (en wat speciale tekens). In vrijwel alle grote programma's zoals Word, Pages of jouw webbrowser kan er gewerkt worden met een uitgebreid alfabet dat niet zo beperkt is.

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

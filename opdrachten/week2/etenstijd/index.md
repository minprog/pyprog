# Etenstijd

Een welbekend stereotype van Nederlanders is dat ze stipt om 18:00 uur aan tafel zitten. Laten we aannemen dat dit stereotype ook doorwerkt op de andere maaltijden en dat de vaste etenstijden voor ontbijt tussen 7:00 en 8:00 zijn, voor lunch tussen 12:00 en 13:00 en voor avondeten tussen 18:00 en 19:00.
Zou het niet handig zijn als er een programma is dat ons vertelt, op basis van het tijdstip, welke maaltijd we moeten eten?

## Opdracht

Schrijf, in een bestand genaamd `etenstijd.py`, een programma dat de gebruiker vraagt hoe laat het is en vervolgens vertelt welke maaltijd er gegeten kan worden.

* In de output van het programma staat of het tijd is voor ontbijt, lunch of avondeten. Als er geen maaltijd genuttigd hoeft te worden, geef dan geen output.
* Je mag ervan uitgaan dat alle input die de gebruiker geeft van de vorm `X:XX` of `XX:XX` is en dat tijdstippen in een 24-uurs tijdsformaat worden ingevuld.
* De tijden zijn *inclusief*, dus elk tijdstip vanaf 7:00 *tot en met* 8:00 is ontbijt.

## Code

In deze opdracht moet je weer zelf een functie schrijven. Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def meal(time: str) -> str:
        """
        Converteert een tijd-string naar een maaltijd.
        De maaltijd kan zijn "ontbijt", "lunch", "avondeten" of "".
        """

    if __name__ == '__main__':
        <Prompt hier de gebruiker om invoer, roep je functie aan en print het antwoord>

## Tips

*   Je kunt meerdere waardes uit een string "uitpakken" met de methode `split()`. Heb je bijvoorbeeld een string met daarin `help@mprog.nl` dan kun je deze als volgt uitpakken naar twee variabelen:

        email = "help@mprog.nl"
        user, domain = email.split("@")

    Daarna heb je twee losse variabelen `user` en `domain` met daarin informatie uit de originele string `email`. Probeer zelf nog even uit hoe dit werkt in Python en of je de informatie uit de `user`-variabele kunt printen!

*   In de `main` moet je zorgen dat er echt helemaal niets wordt geprint als het nog geen etenstijd is. Zie de voorbeelden hieronder.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python etenstijd.py
    Hoe laat is het? 7:15
    Het is tijd voor ontbijt

    $ python etenstijd.py
    Hoe laat is het? 13:00
    Het is tijd voor lunch

    $ python etenstijd.py
    Hoe laat is het? 18:53
    Het is tijd voor avondeten

    $ python etenstijd.py
    Hoe laat is het? 22:12

De laatste geeft dus geen enkele uitvoer.

## Extra uitdaging

Wil je voor een extra uitdaging gaan? Zorg dan dat de gebruiker ook tijden kan invullen van de vorm `X:XX AM`, `XX:XX AM`, `X:XX PM`, en `XX:XX PM`. Let op: dit is niet verplicht, hier zijn dan ook geen checks voor in `checkpy`. Zorg wel dat alle bestaande checks blijven werken!

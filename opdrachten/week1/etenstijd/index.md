# Etenstijd

> **Studeertip.** Het oplossen van de opdrachten telt niet mee voor het eindcijfer. De reden om de opdrachten te maken is dus puur om steeds meer Python te leren en uiteindelijk goed te kunnen programmeren. Bij het tentamen zullen we dit toetsen: je gaat dan zonder internet, zonder oude uitwerkingen en zonder hulp programma's schrijven. Gebruik de opdrachten dus goed!

Een welbekend stereotype van Nederlanders is dat ze stipt om 18:00 uur aan tafel zitten. Laten we aannemen dat dit stereotype ook doorwerkt op de andere maaltijden en dat de vaste etenstijden voor ontbijt tussen 7:00 en 8:00 zijn, voor lunch tussen 12:00 en 13:00 en voor avondeten tussen 18:00 en 19:00.
Zou het niet handig zijn als er een programma is dat ons vertelt, op basis van het tijdstip, welke maaltijd we moeten eten?

## Opdracht

Schrijf, in een bestand genaamd `etenstijd.py`, een programma dat de gebruiker vraagt hoe laat het is en vervolgens vertelt welke maaltijd er gegeten kan worden.

* In de output van het programma staat of het tijd is voor ontbijt, lunch of avondeten. Als er geen maaltijd genuttigd hoeft te worden, geef dan geen output.
* Je mag ervan uitgaan dat alle input die de gebruiker geeft van de vorm `X:XX` of `XX:XX` is en dat tijdstippen in een 24-uurs tijdsformaat worden ingevuld.
* De tijden zijn *inclusief*, dus elk tijdstip vanaf 7:00 *tot en met* 8:00 is ontbijt.

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

## Code

In deze opdracht moet je weer zelf een functie schrijven. Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def meal(time: str) -> str | None:
        """
        Converteert een tijd-string naar een maaltijd.
        De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
        """

    if __name__ == '__main__':
        <Vraag hier de gebruiker om invoer, roep je functie aan en print het antwoord>

## Tips

*   De functie `meal()` moet een string returnen. De mogelijkheden hiervoor staan uitgespeld in de docstring. Zorg dat de functie niets anders returnt dan één van die mogelijkheden, tenzij...

*   ...in de functie `meal()` wordt bepaald wordt dat het géén tijd is voor eten. In dat geval moet de waarde `None` worden teruggegeven met `return None`.

*   Je kunt meerdere waardes uit een string "uitpakken" met de methode `split()`. Heb je bijvoorbeeld een string met daarin `python@proglab.nl` dan kun je deze als volgt uitpakken naar twee variabelen:

        email = "python@proglab.nl"
        user, domain = email.split("@")

    Daarna heb je twee losse variabelen `user` en `domain` met daarin informatie uit de originele string `email`. Probeer zelf nog even uit hoe dit werkt in Python en of je de informatie uit de `user`-variabele kunt printen!

    Bedenk zelf hoe je hiermee de uren en minuten uit kunt pakken en deze verder gebruiken.

*   In de `main` moet je zorgen dat er echt helemaal niets wordt geprint als het nog geen etenstijd is (zie het laatste voorbeeld hierboven). Je kunt met een `if` checken of `None` wordt teruggegeven of niet.

*   Heb je een Python-versie ouder dan 3.11, dan moet je de header van de functie wijzigen naar:

        def meal(time: str) -> Optional[str]:

    en bovenaan je programma deze `import` toevoegen:

        from typing import Optional

## Extra uitdaging

Wil je voor een extra uitdaging gaan? Zorg dan dat de gebruiker ook tijden kan invullen van de vorm `X:XX AM`, `XX:XX AM`, `X:XX PM`, en `XX:XX PM`. Let op: dit is niet verplicht, dus het wordt niet gecontroleerd bij inzenden. Zorg wel dat alle bestaande checks blijven werken!

# Etenstijd

## Maaltijden

Een welbekend stereotype van Nederlanders is dat ze om stipt 1800 uur aan tafel zitten. Laten we aannemen dat dit steroetype ook doorwerkt op de andere maaltijden en daarmee de vaste etenstijden voor ontbijt tussen 7:00 en 8:00 zijn, voor lunch tussen 12:00 en 13:00 en voor avondeten tussen 18:00 en 19:00.
Zou het niet handig zijn als er een programma is dat ons verteld op basis van het tijdstip welke maaltijd we moeten eten?

## Opdracht

Schrijf, in een bestand genaamd `etenstijd.py`, een programma dat de gebruiker vraagt hoe laat het is en vervolgens vertelt welke maaltijd er gegeten kan worden.

* De output van het programma is of het tijd is voor ontbijt, lunch of avondeten. Als er geen maaltijd genuttigd hoeft te worden, geef dan geen output.
* Je mag ervan uitgaan dat alle input die de gebruiker geeft van de vorm `X:XX` of `XX:XX` is en dat tijdstippen in een 24-uurs tijdsformat worden ingevuld.
* De tijden zijn inclusief dus elk tijdstip vanaf 7:00 tot en met 8:00 zijn tijdstippen voor ontbijt.

## Code

In deze opdracht moet je weer een zelf een functie schrijven.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def convert(time):
        """
        Converteert de string van de de tijd naar een float.
        """

    if __name__ == '__main__':
        Prompot hier de gebruiker voor input, roep je functie aan en print voor welke maaltijd het tijd is.

## Tips

* De gebruiker kan de tijdstippen invullen in de vorm `X:XX` en `XX:XX` wat is dan een goede manier om de uren van de minuten te splitten?

## Extra uitdaging

Wil je voor extra uitdaging gaan? Zorg dan dat de gebruiker ook tijden kan invullen van de vorm `X:XX a.m.`, `XX:XX a.m.`, `X:XX p.m.`, en `XX:XX p.m.`. Let op dit is niet verplicht, hier zijn dan ook geen checks voor in checkpy.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python etenstijd.py
    Hoe laat is het? 7:15
    Het is tijd voor onbijt

    $ python etenstijd.py
    Hoe laat is het? 13:00
    Het is tijd voor lunch

    $ python etenstijd.py
    Hoe laat is het? 18:53
    Het is tijd voor avondeten

    $ python maaltijd.py
    Hoe laat is het? 22:12

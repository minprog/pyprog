# Gelijke rechthoeken

![](rechthoeken.png){: width="215"}

We gaan een programma schrijven om te bepalen of twee rechthoeken dezelfde afmetingen hebben.
Als je naar het voorbeeld hierboven kijkt zie je dat de rechthoeken ongeveer even groot lijken.
We kunnen dit precies bepalen als we de coördinaten van de rechthoeken hebben.
In dit geval hebben we een aantal gegevens, zoals de x-waarden van de *linkerzijde* van A (Ax1) en *rechterzijde* van A (Ax2).
Trek je deze van elkaar af, dan heb je één van de beide afmetingen van A.

## Opdracht

    $ python rechthoeken.py
    Geef de x-coordinaten van A: 0,7
    Geef de y-coordinaten van A: 0,4
    Geef de x-coordinaten van B: 6,13
    Geef de y-coordinaten van B: 2,6
    De rechthoeken zijn gelijk!

Schrijf, in een bestand genaamd `afmetingen.py`, een programma dat op basis van de gegeven coördinaten bepaalt of twee rechthoeken dezelfde afmetingen hebben.
Het is daarnaast mogelijk dat de rechthoeken ook vierkanten zijn van dezelfde afmetingen, en in dat geval moet dat ook gemeld worden.
Mocht er helemaal niks interessants te melden zijn over de rechthoeken dan meld je dat.
Je mag ervan uitgaan dat de gebruiker gehele getallen invoert per paar. Met bovenstaande invoer geeft de gebruiker aan dat Ax1 = 0 en Ax2 = 7.

## Code

Je schrijft een hoofdprogramma dat de invoer vraagt en netjes maakt. Daarnaast zijn er drie hulpfuncties die je vanuit je hoofdprogramma gebruikt.

Zoals je kan zien staan er twee TODO's in; hier moet je zelf bedenken wat het type van de functie moet zijn.

    def gelijk(Ax: int, Ay: int, Bx: int, By: int) -> TODO:
        """
        Controleert of de zijdes gelijk zijn
        """

    def vierkant(Ax: int, Ay: int, Bx: int, By: int) -> TODO:
        """
        Controleert of beide rechthoeken hetzelfde vierkant zijn
        """

    def lengte(c1: int, c2: int) -> int:
        """
        Berekent de lengte van een zijde op basis van twee coördinaten
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python rechthoeken.py
    Geef de x-coordinaten van A: 0,7
    Geef de y-coordinaten van A: 0,4
    Geef de x-coordinaten van B: 6,13
    Geef de y-coordinaten van B: 2,6
    De rechthoeken zijn gelijk!

    $ python rechthoeken.py
    Geef de x-coordinaten van A: 0,7       
    Geef de y-coordinaten van A: 0,7
    Geef de x-coordinaten van B: 6,13
    Geef de y-coordinaten van B: 2,9
    De rechthoeken zijn gelijk!
    En ze zijn ook nog vierkant!

    $ python rechthoeken.py
    Geef de x-coordinaten van A: 0,7
    Geef de y-coordinaten van A: 0,7
    Geef de x-coordinaten van B: 6,15
    Geef de y-coordinaten van B: 2,9
    Er is niks aan :(

# Overlap berekenen

![](rechthoeken.png){: width="215"}

De coördinaten van een rechthoek kunnen als volgt worden weergegeven: `rechthoek A1 = ((x1,y1), (x2,y2), (x3,y3), (x4,y4))`, waar elk coördinaat een hoek voorstelt.
Aangezien we het hebben over een rechthoek zijn een aantal van deze waarden gelijk en hebben we genoeg informatie als we dit schrijven als `rechthoek A2 = ((x5,y5), (x6,y6))`.
Nu mag je zelf uitzoeken welke waarden van rechthoek A1 corresponderen met de waarden in rechthoek A2.

Wanneer je twee rechthoeken hebt in een vlak, dan kunnen deze overlappen.
Aangezien het veel werk is om telkens twee rechthoeken te tekenen om te kijken of ze overlappen, is het een handigere optie om dit te bepalen aan de hand van de coördinaten.

## Opdracht

Schrijf, in een bestand genaamd `overlap.py`, een programma dat op basis van de coordinaten van twee rechthoeken bepaalt of er een overlap tussen de twee is. Elke rechthoek bestaat uit twee paar x,y coördinaten doe door de gebruiker worden ingevoerd in het format `x,y`. Je mag ervan uitgaan dat de gebruiker altijd eerst een valide x,y paar voor linksonder invoert gevolgd door een valide x,y paar voor rechtsboven.

## Code

Voor deze opdracht zul je drie functies moeten schrijven en om invoer van de gebruiker vragen voor 2 vierhoeken die elk uit 2 paren x,y coördinaten bestaan.

Ontwerp je code zoals hieronder beschreven. Zoals je kan zien staan er twee TODO's in, hier moet je zelf bedenken wat voor output de functie moet hebben.

    def check_xaxis(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> TODO:
        """
        Controleert of er een overlap is op de x-as.
        """

    def check_yaxis(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> TODO:
        """
        Controleert of er een overlap is op de y-as.
        """

    def check_overlap(x_overlap: bool, y_overlap: bool) -> bool:
        """
        Controleert of de twee rechthoeken overlappen op basis van de overlap op de x en y assen.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

* Om een `x,y` coordinaat lost uit de invoer van de gebruiker te halen kun je de invoer splitten op de komma; `a, b = "3,5".split(",")`.
* De check_overlap functie heeft twee booleans als input, wat zegt dat over de output van de andere twee functies?

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python overlap.py    
    Wat is het linkeronder coordinaat van vierhoek 1? 1,2
    Wat is het rechterboven coordinaat van vierhook 1? 4,4
    Wat is het linkeronder coordinaat van vierhoek 2? 2,3
    Wat is het rechterboven coordinaat van vierhook 2? 5,8
    Er is een overlap tussen de twee rechthoeken

    $ python overlap.py
    Wat is het linkeronder coordinaat van vierhoek 1? 1,2
    Wat is het rechterboven coordinaat van vierhook 1? 4,4
    Wat is het linkeronder coordinaat van vierhoek 2? 5,3
    Wat is het rechterboven coordinaat van vierhook 2? 6,5
    Er is geen overlap tussen de twee rechthoeken

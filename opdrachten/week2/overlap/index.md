# Overlap berekenen

![](rechthoeken.png){: width="215"}

Wanneer je twee rechthoeken hebt in een vlak, dan kunnen deze overlappen.
Aangezien het veel werk is om telkens twee rechthoeken te tekenen om te kijken of ze overlappen, is het een handigere optie om dit te bepalen aan de hand van de coördinaten.
De coördinaten van een rechthoek kunnen als volgt worden weergegeven: `rechthoek A1 = ((x1,y1), (x2,y2), (x3,y3), (x4,y4))`, waar elk coördinaat een hoek voorstelt.
Aangezien we het hebben over een rechthoek zijn een aantal van deze waarden gelijk en hebben we genoeg informatie als we dit schrijven als `rechthoek A2 = ((x5,y5), (x6,y6))`.
Nu mag je zelf uitzoeken welke waarden van rechthoek A1 corresponderen met de waarden in rechthoek A2.

## Opdracht

Schrijf, in een bestand genaamd `overlap.py`, een programma dat op basis van de coordinaten van twee rechthoeken bepaalt of er een overlap tussen de twee is.
De coördinaten van de rechthoeken hoeven niet gegeven te worden door de gebruiker en kunnen gewoon in je code zelf worden gezet.

## Code

Voor deze opdracht ga je drie functies moeten schrijven.
We gebruiken geen gebruik van input van de gebruiker. Je moet de coördinaten van de verschillende rechthoeken waarvan je de overlap wil weten dus telkens veranderen in je code.

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
        Roep hier je drie functies aan. Vul hier dus ook de rechthoeken in die je wil testen.

## Tips

* Voorheen was de input van een functie vaak input van de gebruiker. Maar je kan als input ook de output van een andere functie gebruiken. Dat is het geval voor check_overlap. Daar gebruik je de output van check_xaxis en check_yaxis als input.
* De check_overlap functie heeft twee booleans als input, wat zegt dat over de output van de andere twee functies?

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python overlap.py
    *Bij het invullen van de volgende input: (1,2, 4,4, 2,3 5,8) krijg je de volgende output*
    Er is een overlap tussen de twee rechthoeken

    $ python overlap.py
    *Bij het invullen van de volgende input: (1,2, 4,4, 5,3 6,5) krijg je de volgende output*
    Er is geen overlap tussen de twee rechthoeken

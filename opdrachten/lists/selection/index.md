# Selection sort

Schrijf een functie die een lijst aanneemt en deze sorteert volgens het "selection sort"-algoritme.

## Details

![embed](https://www.youtube.com/embed/NEbb4XqKDNU)

## Code

Gebruik de pseudocode uit bovenstaande video om het sorteren te implementeren. Dit is echt even goed nadenken hoe je loops gaat inzetten. Onhou dat sorteren inhoudt dat je herhaaldelijk een aantal vaste stappen neemt. Elke herhaling raakt de lijst "meer gesorteerd".

Ontwerp je code zoals hieronder beschreven. Schrijf veel doctests, zodat de correcte werking van het sorteren goed wordt aangetoond, en het hoofdprogramma.

Let op dat de functie de lijst l moet aanpassen, maar deze alsnog moet returnen. Dat is nodig om handig doctests te kunnen doen.

    def selection_sort(l: list[int]) -> list[int]:
        """
        Sorteert de lijst `l` door deze aan te passen.
        Er wordt geen nieuwe lijst gemaakt.
        Moet wel `l` returnen.
        """

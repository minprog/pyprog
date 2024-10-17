# List Functions

Maak een Python-bestand aan genaamd `list_functions.py`. Neem onderstaande functies over, vul de doctests aan, en voeg een implementatie toe:

## Indexing

Gebruik hier van lists alleen indexing, zoals beschreven in hoofdstuk 7.1 van het boek. En we vertellen je meteen een trucje: als je een negatieve index gebruikt dan telt Python vanaf het einede. Dus een list heeft normaal deze indices: `[0, 1, 2, 3, ...]` maar vanaf de andere kant is het `[..., -3, -2, 1]`.

    def same_first_last(in_list: list[object]) -> bool:
        """Precondition: len(L) >= 2
        Return True if and only if first item of the list is the same as the
        last.
        
        >>> same_first_last([3, 4, 2, 8, 3])
        True
        >>> same_first_last(['apple', 'banana', 'pear'])
        
        >>> same_first_last([4.0, 4.5])
        
        """

## Lengte

Net als met strings kun je de lengte van een list opvragen. Dat heb je nodig voor deze functie.

    def is_longer(in_list1: list[object], in_list2: list[object]) -> bool:
        """
        Return True if and only if the length of L1 is longer
        than the length of L2.
        
        >>> is_longer([1, 2, 3], [4, 5])
        True
        >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
        
        >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
        
        """

## Palindroom-ish

In hoofdstuk 6.6 van het boek staat een voorbeeldfunctie om een string om te keren. Je kunt zoiets ook gebruiken om een list om te keren. Gebruik dit voorbeeld om een palindroom-functie te maken die op lijsten werkt.

    from typing import Any
    
    def is_palindromish(items: list[Any]):
        # TODO

We gebruiken het type `list[Any]` om aan te geven dat de lijst objecten van alle types mag bevatten.

## Efficientere palindroom-ish

Het geheel omkeren van een lijst (of string) om de palindroom-eigenschap te controleren is wat omslachtig. Je kunt namelijk ook het eerste item en het laatste vergelijken, dan het 2e item en het één-na-laatste item, enzovoort. Maak deze functie.

    from typing import Any
    
    def is_palindromish_eff(items: list[Any]):
        # TODO


## Hint

Gebruik alleen wat je uit het boek geleerd hebt!

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

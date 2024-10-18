# List Functions

Maak een Python-bestand aan genaamd `list_functions.py`. Neem onderstaande functies over, vul de doctests aan, en voeg een implementatie toe:

## Indexing

Implementeer de volgende functie. Vul zelf de ontbrekende uitkomsten van de doctests aan.

Gebruik hier van lists alleen indexing, zoals beschreven in hoofdstuk 7.1 van het boek. En we vertellen je meteen een trucje: als je een negatieve index gebruikt dan telt Python vanaf het einede. Dus een list heeft normaal deze indices: `[0, 1, 2, 3, ...]` maar vanaf de andere kant is het `[..., -3, -2, -1]`.

    from typing import Any
    
    def same_first_last(in_list: list[Any]) -> bool:
        """
        Geeft True als het eerste element van
        de lijst gelijk is aan het tweede,
        anders False.
        
        >>> same_first_last([3, 4, 2, 8, 3])
        True
        >>> same_first_last(['apple', 'banana', 'pear'])
        
        >>> same_first_last([4.0, 4.5])
        
        """
        return in_list[0] == in_list[-1]

> We gebruiken het type `list[Any]` om aan te geven dat de lijst objecten van alle types mag bevatten. In feite wordt de inhoud van de lijst dan niet meer gecontroleerd op juiste types. Hieronder gaan we dit ook voor diverse functies doen. Dat is omdat deze functies *generiek* zijn en niet een speciaal soort element verwachten.

## Lengte

Implementeer de volgende functie.

Tip: net als met strings kun je de lengte van een list opvragen. Dat heb je nodig voor deze functie.

    def is_longer(in_list1: list[Any], in_list2: list[Any]) -> bool:
        """
        Geeft True als de lengte van in_list1
        groter is dan de lengte van in_list2,
        anders False.
        
        >>> is_longer([1, 2, 3], [4, 5])
        True
        >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
        False
        >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
        False
        """
        return len(in_list1) > len(in_list2)

## Palindroom-ish

Implementeer de volgende functie. Voeg zelf doctests toe.

In hoofdstuk 6.6 van het boek staat een voorbeeldfunctie om een string om te keren. Je kunt zoiets ook gebruiken om een list om te keren. Gebruik dit voorbeeld om een palindroom-functie te maken die op lijsten werkt (gebruik dus de `+`-operator).

    from typing import Any
    
    def is_palindromish(items: list[Any]) -> bool:
        """
        Geeft True als de lijst een palindroom
        is, anders False.
        """
        result = []
        for element in items:
            result = [element] + result
        return result == items

## Efficientere palindroom-ish

Implementeer de volgende functie, rekening houdend met de eisen in de volgende alinea. Voeg zelf doctests toe.

Het geheel omkeren van een lijst (of string) om de palindroom-eigenschap te controleren is wat omslachtig. Je kunt namelijk ook het eerste item en het laatste vergelijken, dan het 2e item en het één-na-laatste item, enzovoort. Maak deze functie. De uitkomst moet correct zijn voor lijsten met 0 elementen, met één element, en ook voor een even en oneven aantal elementen. Geef ook doctests die dat aantonen.

    from typing import Any
    
    def is_palindromish_eff(items: list[Any])  -> bool:
        """
        Geeft True als de lijst een palindroom
        is, anders False.
        """

## Even getallen

Implementeer de volgende functie.

    def filter_even(in_list: list[int]) -> list[int]:
        """
        Geeft alle even getallen uit de lijst,
        in een nieuwe lijst.
        
        >>> filter_even([2, 4, 6])
        [2, 4, 6]
        >>> filter_even([2, 3, 4])
        [2, 4]
        >>> filter_even([])
        []
        """

## Alles is even

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

Maak een functie die een lijst aanneemt en controleert of elk getal in de lijst even is. Het resultaat is een boolean.

    def all_even(in_list: list[int]) -> bool:
        """
        Geeft True als alle getallen uit de
        lijst even zijn, anders False.
        
        >>> all_even([2, 4, 6])
        True
        >>> all_even([2, 3, 4])
        
        >>> all_even([])
        
        """

## Maximum-element

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

    def max_element(in_list: list[int]) -> int:
        """
        Geeft het hoogste getal uit de lijst.
        
        >>> max_element([1, 3, 2, 5, 4])
        5
        >>> max_element([-1, -3, -2])
        
        >>> max_element([5, 5, 5])
        
        """

## Zoek element

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

    from typing import Any
    
    def element_exists(in_list: list[Any], element: Any) -> bool:
        """
        Geeft True als het element in de lijst
        staat, anders False.
        
        >>> element_exists([1, 2, 3], 2)
        True
        >>> element_exists([1, 2, 3], 4)
        
        >>> element_exists([], 4)
        
        """

## Tel aantal elementen

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

    from typing import Any
    
    def count_occurrences(in_list: list[Any], element: Any) -> int:
        """
        Geeft het aantal keer dat het element
        voorkomt in de lijst.
        
        >>> count_occurrences([1, 2, 3, 2, 4], 2)
        2
        >>> count_occurrences(['a', 'b', 'a'], 'a')
        
        >>> count_occurrences([1, 2, 3], 4)
        
        """

## Verwijder dubbele items

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

    def remove_duplicates(in_list: list[Any]) -> list[Any]:
        """
        Neemt een lijst aan en geeft een nieuwe lijst
        zonder de dubbele items uit het origineel.
        
        >>> remove_duplicates([1, 2, 2, 3, 4, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        
        >>> remove_duplicates([1, 1, 1])
        
        """

## Lijsten op volgorde samenvoegen (moeilijker!)

Implementeer de volgende functie. Vul de doctests aan met verwachte antwoorden.

Je kunt onderstaande voor elkaar krijgen door uit de twee lijsten (min of meer) om beurten getallen te nemen.

    def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
        """
        Neemt twee gesorteerde lijsten aan en geeft een nieuwe
        lijst terug waarin de elementen van beide voorkomen,
        wederom gesorteerd.
        
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted_lists([1, 2], [3, 4])
        
        >>> merge_sorted_lists([], [1, 2])
        
        """

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

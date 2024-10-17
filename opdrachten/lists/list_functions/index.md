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

We gebruiken het type `list[Any]` om aan te geven dat de lijst objecten van alle types mag bevatten. In feite wordt de inhoud van de lijst dan niet meer gecontroleerd op juiste types. Hieronder gaan we dit ook voor diverse functies doen. Dat is omdat deze functies *generiek* zijn en niet een speciaal soort element verwachten.

## Efficientere palindroom-ish

Het geheel omkeren van een lijst (of string) om de palindroom-eigenschap te controleren is wat omslachtig. Je kunt namelijk ook het eerste item en het laatste vergelijken, dan het 2e item en het één-na-laatste item, enzovoort. Maak deze functie. De uitkomst moet correct zijn voor lijsten met 0 elementen, met één element, en ook voor een even en oneven aantal elementen. Geef ook doctests die dat aantonen.

    from typing import Any
    
    def is_palindromish_eff(items: list[Any]):
        # TODO

## Even getallen

Maak een functie die een lijst aanneemt en alleen de even getallen uit die lijst teruggeeft, in een nieuwe lijst.

    def filter_even(in_list: list[int]) -> list[int]:
        """
        Return all even numbers from the list.
    
        >>> filter_even([2, 4, 6])
        [2, 4, 6]
        >>> filter_even([2, 3, 4])
        [2, 4]
        >>> filter_even([])
        []
        """
        # TODO

## Alles is even

Maak een functie die een lijst aanneemt en controleert of elk getal in de lijst even is. Het resultaat is een boolean.

    def all_even(in_list: list[int]) -> bool:
        """
        Return True if all integers in the list are even.
    
        >>> all_even([2, 4, 6])
        True
        >>> all_even([2, 3, 4])
    
        >>> all_even([])
    
        """
        # TODO

## Maximum-element

Maak een functie die de integer met de hoogste waarde vindt in een lijst. Gebruik loops en operators.

    def max_element(in_list: list[int]) -> int:
        """
        Return the maximum number in the list.
    
        >>> max_element([1, 3, 2, 5, 4])
        5
        >>> max_element([-1, -3, -2])
    
        >>> max_element([5, 5, 5])
    
        """

## Zoek element

Maak een functie die controleert of een bepaalde waarde in een lijst te vinden is. 

    from typing import Any
    
    def element_exists(in_list: list[Any], element: Any) -> bool:
        """
        Return True if and only if element is in the list.
    
        >>> element_exists([1, 2, 3], 2)
        True
        >>> element_exists([1, 2, 3], 4)
    
        >>> element_exists([], 4)
    
        """

## Tel aantal elementen

Maak een functie die het aantal voorkomens van een bepaald object telt.

    from typing import Any
    
    def count_occurrences(in_list: list[Any], element: Any) -> int:
        """
        Return the number of times element appears in the list.
    
        >>> count_occurrences([1, 2, 3, 2, 4], 2)
        2
        >>> count_occurrences(['a', 'b', 'a'], 'a')
    
        >>> count_occurrences([1, 2, 3], 4)
    
        """
        # TODO

## Verwijder dubbele items

Maak een functie die dubbele items weglaat als ze direct na elkaar staan in een lijst. Maak een nieuwe lijst met de ontdubbelde inhoud, dus verander niks aan de oorspronkelijke list.

    def remove_duplicates(in_list: list[Any]) -> list[Any]:
        """
        Return a new list with duplicates removed, keeping only the first
        occurrence of each element.
    
        >>> remove_duplicates([1, 2, 2, 3, 4, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
    
        >>> remove_duplicates([1, 1, 1])
    
        """

## Lijsten op volgorde samenvoegen (moeilijker!)

Maak een functie die een nieuwe lijst maakt met daarin de elementen van twee bronlijsten. De elementen van de bronlijsten moeten al gesorteerd aangeleverd worden en de resulterende lijst moet ook gesorteerd zijn. Je kunt dit voor elkaar krijgen door om beurten in de lijst steeds verder te gaan.

    def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
        """
        Merge two sorted lists into one sorted list.
    
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted_lists([1, 2], [3, 4])
    
        >>> merge_sorted_lists([], [1, 2])
    
        """
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

# List Functions

Maak een Python-bestand aan genaamd `list_functions.py`.

Voeg de volgende functies toe, vul de uitkomsten van de voorbeelden (examples) aan, en voeg een implementatie (body) toe:

    def same_first_last(L: list[object]) -> bool:
        """Precondition: len(L) >= 2
        Return True if and only if first item of the list is the same as the
        last.
        
        >>> same_first_last([3, 4, 2, 8, 3])
        True
        >>> same_first_last(['apple', 'banana', 'pear'])
        
        >>> same_first_last([4.0, 4.5])
        
        """

    def is_longer(L1: list[object], L2: list[object]) -> bool:
        """
        Return True if and only if the length of L1 is longer
        than the length of L2.
        
        >>> is_longer([1, 2, 3], [4, 5])
        True
        >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
        
        >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
        
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

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

## Testen

Je kunt testen of je functie correct is door je bestand in te leveren op deze pagina. Maar je kunt ook je functie handmatig testen:

- Start `python -i string_functions.py`. Jouw programma wordt dan ingeladen en je krijgt een prompt `>>>` om commando's in te voeren.

- Tik bijvoorbeeld in `repeat('yes', 4)` om te kijken of je functie het juiste antwoord geeft.

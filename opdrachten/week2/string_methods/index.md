# String Methods

In de vorige opdracht heb je string-functies geschreven zoals `isupper(...)`. In hoofdstuk 6 heb je nu gelezen dat er ook al **methods** bestaan die deze functionaliteit hebben. Die functies hoeven we dus niet meer te gebruiken, en in plaats daarvan werk je in deze opdracht met de bestaande methods die gedefinieerd zijn voor strings.

## Oefeningen

Maak een bestand genaamd `string_methods.py`.

- Schrijf een functie `number_of_Os(...)` die een string aanneemt en bepaalt hoeveel letters "o" voorkomen in de string. Gebruik de `count(...)`-methode.

- Schrijf een functie `first_O(...)` die string aanneemt en de positie bepaalt van de *eerste* letter "o" in de string. Gebruik de `find(...)`-methode. Je mag ervan uitgaan dat de letter voorkomt in de string.

- Schrijf een functie `number_of_letters(...)` die een string aanneemt + een losse letter, en bepaalt hoe vaak de opgegeven letter voorkomt in de string.

- Schrijf een functie `where_letter(...)` die string aanneemt + een losse letter, en bepaalt op welke positie de opgegeven letter voor het *eerst* voorkomt in de string. Je mag ervan uitgaan dat de letter voorkomt in de string.

- Schrijf een functie `total_occurences(...)` gebaseerd op de volgende template:

        def total_occurrences(s1: str, s2: str, ch: str) -> int:
            """
            Return the total number of times that ch occurs in s1 and s2.
        
            >>> total_occurrences('color', 'yellow', 'l')
            3
            >>> total_occurrences('red', 'blue', 'l')
        
            >>> total_occurrences('green', 'purple', 'b')
        
            """

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

# Acid test

> **Studeertip.** Zorg dat je het boek t/m hoofdstuk 4.3 hebt doorgenomen voordat je aan de programmeeropdrachten over conditionals begint.

Vanaf nu zul je `if`-statements gaan gebruiken in de programma's. Deze opdracht is een oefening om in te komen. De logica is grotendeels gegeven, maar de structurering moet jij doen.

## Opdracht

Gegeven is het volgende Python-programma:

    ph = float(input("Geef een pH-waarde: "))
    if ph < 7.0:
        print("Het is een zuur")
    else:
        print("Het is een base")

Maak een Python-bestand aan genaamd `acid.py`. Splits bovenstaande programma op zodat het voldoet aan onze standaard-manier van programma's schrijven. Hierin is er een **functie die een berekening doet** en een **hoofdprogramma dat de input en output afhandelt**. Het moet er ongeveer zo uitzien:

    def is_acidic(...) -> bool:
        <functie met docstring, voorbeelden en implementatie>
    
    if __name__ == '__main__':
        <hoofdprogramma doet alleen input en print, en roept is_acidic aan>

## Hint

- De functie `is_acidic` moet een `bool` returnen, volgens de type hint. Doe dit via `return True` of `return False`, al naar gelang de conclusie die de functie trekt.

- De logica is al gegeven. Het enige dat je moet doen is het in de template passen. Maar dat is niet helemaal triviaal, zie de volgende hint.

- Het is noodzakelijk om zowel in `is_acidic` als in de `__main__` een `if`-`else` toe te voegen.

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

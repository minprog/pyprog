# Schrikkeljaar

Wat is een schrikkeljaar? In het werkcollege heb je al een formule samengesteld hiervoor.

## Opdracht

Schrijf een functie die bepaalt of een bepaald jaartal een schrikkeljaar is. Schrijf daarbij een `main` die om een jaartal vraagt en dan print of het inderdaad een schrikkeljaar is (iets als `2025 is geen schrikkeljaar`).

## Hint

Baseer het ontwerp van je programma op *Acid test*.

Submit je programma om te achterhalen of het precies voldoet aan wat wij dachten. De output (dus het printen) is net een beetje anders dan bij *Acid test*. Kies een output en check dan de resultaten van de submit om te zien hoe wij het graag willen.

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

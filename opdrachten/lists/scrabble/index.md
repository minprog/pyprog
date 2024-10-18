# Scrabble

Bij het spel Scrabble leggen de spelers woorden neer waar ze punten voor krijgen. De punten per letter zijn te zien in onderstaande tabel. De som van alle letterpunten is de score voor het gelegde woord.

| **A** | **B** | **C** | **D** | **E** | **F** | **G** | **H** | **I** | **J** | **K** | **L** | **M** | **N** | **O** | **P** | **Q** | **R** | **S** | **T** | **U** | **V** | **W** | **X** | **Y** | **Z** |
|:-----:|:-----:|:-----:|:-----:|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|   1   |   3   |   3   |   2   | 1     | 4     | 2     | 4     | 1     | 8     | 5     | 1     | 3     | 1     | 1     | 3     | 10    | 1     | 1     | 1     | 1     | 4     | 4     | 8     | 4     | 10    |

Als we bijvoorbeeld naar het woord `code` kijken, dan zien we dat de Scrabble-score `3 + 1 + 2 + 1 = 7` zou zijn.

## Opdracht

Schrijf, in een bestand genaamd `scrabble.py`, een programma dat twee gebruikers vraagt een woord in te vullen. Vervolgens moet het programma laten weten welke speler heeft gewonnen: die gaf het woord met de meeste punten. Hoofd- en kleine letters mogen door elkaar worden gebruikt en hebben geen verdere invloed op de score. Let op dat ook tekens gebruikt zouden kunnen worden die geen letter zijn. Zorg dat je deze tekens negeert in de berekening.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en verdere uitleg van de aanpak die je gekozen hebt.

    POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
              1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    def compute_score(word: str) -> int:
        """
        Bereken en return de score voor het woord.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Details

* Om de score van een *woord* te berekenen moet je de score van alle *letters* in dat woord optellen.

* In de code zie je boven de functies een variabele in hoofdletters staan (`POINTS`). Dit is een globale variabele die een vast gegeven definieert. Voeg verder geen globale variabelen toe.

* De score van een *letter* kun je uitvogelen door te kijken welke plek in het alfabet de letter heeft (a = 0, b = 1) en dan op te zoeken wat de bijbehorende puntenwaarde is.

    * Gebruik een loop om te kijken op welke plek in de string `"abcdefghijklmnopqrstuvwxyz"` jouw letter zit. Gebruik dat getal om de score op te zoeken in de list `POINTS`.
    
    * Nogmaals: gebruik een loop zoals beschreven. Gebruik geen andere constructies. Het doel is niet om de opdracht werkend te krijgen, maar om deze specieke manier te oefenen.

    * Verberg het berekenen van de score van één letter in een aparte functie.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python scrabble.py
    Speler 1: Hallo
    Speler 2: Doei
    Speler 1 wint!

    $ python scrabble.py
    Speler 1: Apenkoppen
    Speler 2: Bananenbroodje
    Speler 2 wint!

    $ python scrabble.py
    Speler 1: cat
    Speler 2: dog
    Gelijkspel!

    $ python scrabble.py
    Speler 1: Hardly?
    Speler 2: Hardly!
    Gelijkspel!

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

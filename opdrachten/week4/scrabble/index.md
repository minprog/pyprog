# Scrabble

Bij het spel Scrabble, leggen de spelers woorden neer waar ze punten voor krijgen. Voor elke letter krijgen ze een bijbehorend aantal punten, te zien in onderstaande tabel, de som van alle letters is de score voor hun woord.

| **A** | **B** | **C** | **D** | **E** | **F** | **G** | **H** | **I** | **J** | **K** | **L** | **M** | **N** | **O** | **P** | **Q** | **R** | **S** | **T** | **U** | **V** | **W** | **X** | **Y** | **Z** |
|:-----:|:-----:|:-----:|:-----:|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|   1   |   3   |   3   |   2   | 1     | 4     | 2     | 4     | 1     | 8     | 5     | 1     | 3     | 1     | 1     | 3     | 10    | 1     | 1     | 1     | 1     | 4     | 4     | 8     | 4     | 10    |

Als we bijvoorbeeld naar het woord `Code` kijken, dan zien we uit de tabel dat in Scrabble het woord `3 + 1 + 2 + 1 = 7` zou krijgen.

## Opdracht

Schrijf, in een bestand genaamd `scrabble.py`, een programma dat twee gebruikers vraagt een woord in te vullen. Vervolgens moet het programma laten weten wie volgens de scrabble regels heeft gewonnen: wie het woord met de meeste punten heeft ingevuld.

* Zorg dat zowel hoofd als kleine letters worden geaccepteerd.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    def compute_score(word: str) -> int:
        """
        Bereken en return de score voor het woord.
        """

    if __name__ == '__main__':
        Prompt beide spelers voor een woord, bereken de score van beide woorden. Print welke speler er heeft gewonnen.

In de code zie je boven de functies een variabele in hoofdletters staan (`POINTS`). Dit is een globale variabele. Dit is om te voorkomen dat je deze overal opnieuw hoeft te definiëren. Globale variabelen worden ook gebruikt om het gebruik van zogenoemde 'magic numbers' tegen te gaan.

## Tips

* Om makkelijk een string van het alfabet te genereren, kan je de module string gebruiken.

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

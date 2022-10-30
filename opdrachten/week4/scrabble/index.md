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

Het wordt bij deze opdracht aangemoedigd om extra functies te introduceren die een klein deel van het probleem oplossen. Die moeten dan ook types hebben en doctests.

    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    def compute_score(word: str) -> int:
        """
        Bereken en return de score voor het woord.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

* In de code zie je boven de functies een variabele in hoofdletters staan (`POINTS`). Dit is een globale variabele. Dit is om te voorkomen dat je deze overal opnieuw hoeft te definiëren.

* Om makkelijk een string van het alfabet te genereren, kan je de module `string` gebruiken. Zie de [handleiding](https://docs.python.org/3/library/string.html).

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

## Insturen

Hoeveel tijd heb je gewerkt aan deze opdracht?

<input name="form[qTime]" type="text" required>

Waren er nog dingen waar je op vastliep of heb je specifieke feedback voor deze opdracht?

<textarea name="form[qVastlopers]">

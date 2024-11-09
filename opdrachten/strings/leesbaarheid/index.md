# Leesbaarheid

> **Studeertip.** Je gaat deze opdracht aanzienlijk sneller en makkelijker maken als je de opdracht eerst helemaal leest voordat je aan de slag gaat.

De Coleman-Liau index is een maat voor de leesbaarheid van een tekst.
Dit gaat op basis van het Amerikaanse systeem waarin ze 'grades' gebruiken.
Deze index wordt onder andere berekend op basis van het aantal letters per woord.

De formule is als volgt:

    CLI = 0.0588 * L - 0.296 * S - 15.8

waarbij L het gemiddelde aantal letters per 100 woorden is en S het gemiddelde aantal zinnen per 100 woorden.

Meer informatie over de Coleman-Liau index kan je vinden op de betreffende [Wikipedia-pagina](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index).

## Opdracht

Schrijf, in een bestand genaamd `leesbaarheid.py`, een programma dat de leesbaarheid van een tekst berekent op basis van de Coleman-Liau index.

* De output van het programma is van de vorm `Grade X`, waar X de berekende grade is. Dit is een geheel getal, dus rond de output van de `coleman_liau` functie af.

* Als de grade groter of gelijk is aan 16, geef dan `Grade 16+` als output. Print `Below Grade 1` als de grade kleiner is dan 1.

* Je mag geen split gebruiken, maar je moet statistieken berekenen door te loopen over de string.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def calculate_grade(text: str) -> int:
        """
        Bepaalt aantal letters, woorden en zinnen van de tekst,
        en roept coleman_liau aan om grade te berekenen.
        
        >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
        
        >>> calculate_grade("Congratulations! Today is your day. You're "
        ...     "off to Great Places! You're off and away!")
        
        >>> calculate_grade("There are more things in Heaven and Earth, "
        ...     "Horatio, than are dreamt of in your philosophy.")
        
        """

    def coleman_liau(words: int, sentences: int, letters: int) -> int:
        """
        Berekent de index volgens de Coleman Liau-formule.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

*  De maat `L` uit de index is: $$100 "aantal\_letters" / "aantal\_woorden"$$.

*  De maat `S` uit de index is: $$100 "aantal\_zinnen" / "aantal\_woorden"$$.

*  Beredeneer uit de voorbeelden hieronder hoe je definieert wat een "zin", een "woord" en een "letter" is. `You're` is 1 woord met 5 letters! Bedenk daarna hoe je in Python de tekst kunt analyseren om deze statistieken te bepalen.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python leesbaarheid.py
    Text: One fish. Two fish. Red fish. Blue fish.
    Below Grade 1

    $ python leesbaarheid.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3

    $ python leesbaarheid.py
    Text: There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.
    Grade 9

    $ python leesbaarheid.py
    Text: A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.
    Grade 16+

    $ python leesbaarheid.py
    Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
    Grade 7

    $ python leesbaarheid.py
    Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
    Grade 10

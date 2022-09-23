# Leesbaarheid

De Coleman-Liau index is een leesbaarheidstest die de mate van leesbaarheid van een tekst meet. Dit is op basis van het Amerikaanse systeem waarin ze 'grades' gebruiken.
Deze index wordt onder andere berekend op basis van het aantal karakters per woord.

De formule is als volgt:

    CLI = 0.0588 * L - 0.296 * S - 15.8

waarbij L het gemiddelde aantal letters per 100 woorden is en S het gemiddelde aantal zinnen per 100 woorden.

Meer informatie over de Coleman-Liau index kan je vinden op de betreffende [Wikipedia-pagina](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index). Hier vind je ook uitleg over de manier waarop je het gemiddelde aantal letters en zinnen per 100 woorden kunt berekenen.

## Opdracht

Schrijf, in een bestand genaamd `leesbaarheid.py`, een programma dat de leesbaarheid van een tekst berekent op basis van de Coleman-Liau index.

* De output van het programma is van de vorm `Grade X`, waar X de berekende grade is. Dit is een geheel getal, dus rond de output van de coleman_liau functie af.
* Als de grade groter of gelijk is aan 16, geef dan `Grade 16+` als output. Print `Below Grade 1` als de grade kleiner is dan 1.


## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def calculate_grade(words: int, sentences: int, letters: int) -> int:
        """
        Berekent eerst de waarden L en S gebasseerd op het aantal 
        woorden en zinnen. Returnt de grade op basis van deze gegevens.
        """

    def coleman_liau(L: float, S: float) -> float:
        """
        Berekent de grade volgens de Coleman Liau-formule.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Tips

* Je kan een alfabet string krijgen via de string module. Kijk bijvoorbeeld even naar de functie `string.ascii_lowercase`.

* `You're` is 1 woord met 5 letters!

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

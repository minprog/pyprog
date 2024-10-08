# Byte

Binair 010101 robot

## Opdracht

Schrijf, in een bestand genaamd `byte.py`, een programma dat om een decimaal getal vraagt en dit uitprint als een binair getal (precies één byte van 8 bits).

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python byte.py
    Getal: 4
    0100

    $ python binair.py
    Getal: 15
    1111

    $ python binair.py
    Getal: 5
    0101

## Code

In deze opdracht bestaat je code uit drie zelfgeschreven functies.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen (doctests!) en de gewenste uitkomsten.
Schrijf ook code om invoer te vragen en de functie aan te roepen.

    def convert(number: int) -> int:
        """
        Zet het getal dat gerepresenteerd wordt door bit1 t/m bit 4
        om in decimale representatie.
        """
    
    if __name__ == '__main__':
        <Schrijf hier code die input van de gebruiker opvraagt,
        convert aanroept, en de uitkomst print>

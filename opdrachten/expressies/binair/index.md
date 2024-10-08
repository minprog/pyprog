# Binair tellen

Binair 010101 robot

## Opdracht

Schrijf, in een bestand genaamd `binair.py`, een programma dat om vier bits vraagt (0 of 1) en dit omzet naar een decimaal getal en uitprint.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python binair.py
    bit 1: 0
    bit 2: 1
    bit 3: 0
    bit 4: 0
    4

    $ python binair.py
    bit 1: 1
    bit 2: 1
    bit 3: 1
    bit 4: 1
    15

    $ python binair.py
    bit 1: 0
    bit 2: 1
    bit 3: 0
    bit 4: 1
    5

## Code

In deze opdracht bestaat je code uit drie zelfgeschreven functies.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen (doctests!) en de gewenste uitkomsten (stap 3 van het FDR), en eventueel verdere uitleg.
Schrijf ook code om invoer te vragen en de functie aan te roepen.

    def convert(bit1: int, bit2: int, bit3: int, bit4: int) -> int:
        """
        Zet het getal dat gerepresenteerd wordt door bit1 t/m bit 4
        om in decimale representatie.
        """
    
    if __name__ == '__main__':
        <Schrijf hier code die input van de gebruiker opvraagt,
        convert aanroept, en de uitkomst print>

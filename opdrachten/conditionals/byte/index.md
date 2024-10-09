# Byte

Schrijf een programma dat om een decimaal getal vraagt en vervolgens de bits van hetzelfde getal print in binaire representatie.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python byte.py
    getal: 3
    0
    0
    0
    0
    0
    0
    1
    1

    $ python byte.py
    getal: 50
    0
    0
    1
    1
    0
    0
    1
    0

## Code

    def print_bits(...) -> None:
        <functie print bits, returnt niks>

    if __name__ == '__main__':
        <hoofdprogramma doet alleen input en aanroep van print_bits>

## Hints

- Je hebt heel veel if-statements nodig om de functie werkend te krijgen. Je mag nog geen loop gebruiken in deze opdracht, want loops zijn nog niet aan bod geweest!

- De strategie is als volgt:

    -   Check of het getal groter is dan 128. Zo ja, dan is bit 1 **actief** en print je een `1`. Je trekt 128 van het getal af en je gaat door. Als het niet zo is, dan is bit 1 **inactief** en print je een `0`. Enzovoort.
    
            >>> 15 > 128
            False
            >>> 15 > 64
            False
            >>> 15 > 32
            False
            >>> 15 > 16
            False
            >>> 15 > 8
            True
            >>> 7 > 4
            True
            >>> 3 > 2
            True
            >>> 1 > 1
            True

- Je kunt doctests schrijven zoals gebruikelijk voor een functie. Het feit dat de functie print en niet `return`t maakt niet uit voor het doctest-systeem.

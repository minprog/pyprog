# Byte

> **Studeertip.** Deze opdracht is echt een beetje een puzzel. Wat moet je doen? En hoe? We weten dat een heel groot deel van de studenten deze opdracht kan oplossen door goed te bestuderen wat hieronder gezegd wordt en dan een algemeen stappenplan (algoritme) te formuleren en omzetten in code. Een deel van de studenten heeft even wat aanspraak nodig omdat ze ergens overheen lezen of iets verkeerd begrijpen. Dan helpt het om met een medestudent door te spreken "wat de bedoeling is". Doe dat, en betrek je docent en assistent erbij als het nodig is.

## Opdracht

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

- Je hebt heel veel if-statements nodig om de functie werkend te krijgen. Je mag nog geen loop gebruiken in deze opdracht, want loops zijn nog niet aan bod geweest.

- De strategie is als volgt:

    -   Check of het getal groter is dan 128, of precies gelijk aan 128. Zo ja, dan is bit 1 **actief** en print je een `1`. Je trekt 128 van het getal af en je gaat door. Als het niet zo is, dan is bit 1 **inactief** en print je een `0`. Enzovoort.

    - Als voorbeeld nemen we het getal 14.

        - We beginnen met 128, maar 14 is kleiner, dus we printen een `0`.
        - Dan hebben we 64, 32 en 16, dus printen we nog drie keer een `0`.
        - Nu komen we bij de 8, en 14 is groter. We printen dus een `1` en dan trek je 8 van 14 af, geeft 6.
        - Nu komen we bij de 4, en 6 is groter. We printen dus een `1` en dan trek je 4 van 6 af, geeft 2.
        - Nu komen we bij de 2, en 2 is gelijk. We printen dus een `1` en dan trek je 2 van 2 af, geeft 0.
        - Nu komen we bij de 1, maar 0 is kleiner, dus we printen een `0`.

- Je kunt doctests schrijven zoals gebruikelijk voor een functie. Het feit dat de functie print en niet `return`t maakt niet uit voor het doctest-systeem.

## Zelf testen

Werkt je programma goed? Je kunt het insturen om te controleren. Maar je kunt een deel van de tests ook zelf runnen. Dat maakt het verbeteren van fouten misschien iets sneller.

-   Gebruik dit commando om de doctests te controleren die je zelf geschreven hebt:

        python3 -m doctest -v programma.py

    Gebruik hierin het `python` of `python3`-commando afhankelijk van wat op jouw computer de juiste versie is.

-   Je kunt ook de type hints checken. Installeer dan `mypy` via het commando `pip3 install mypy` en controleer zo je programma:

        mypy --strict --ignore-missing-imports programma.py

Mocht het installeren niet lukken, dan kun je altijd hulp vragen. Maar hoe dan ook kun je insturen op deze website, en dan gebeurt het controleren automatisch.

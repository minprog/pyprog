# Spongebob

Maak een Python-module genaamd `spongebob.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Om de letter uppercase 1

    >>> spongebob1('hello world!')
    'hElLo wOrLd!'

Schrijf een functie `spongebob1` die elk tweede teken in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Voor deze functie moet je een positie-loop maken zodat je weer weet "waar je bent" in de string (`for i in range(len(s))`). Alle oneven posities worden uppercase.

## Om de letter uppercase 2

    >>> spongebob2('hello world!')
    'hElLo WoRlD!'

Schrijf een functie `spongebob2` die elke tweede letter in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Hier is een extra beperking, namelijk dat het echt alleen om *letters* gaat. Je moet met de methode `.isalpha()` checken of een teken alfabetisch is en alleen dan telt deze als letter.

In dit geval geeft een positie-loop geen nuttige informatie, want niet elke positie bevat een letter. Je maakt nu dus weer een normale transformatie-loop (`for char in s:`).

Algoritme:

- Loop door alle tekens in de invoerstring met een transformatie-loop.
    - Houd een teller bij voor hoeveel letters je tot nu toe hebt gezien.
        - Als char een letter is (`char.isalpha()`), dan verhoog je de teller.
        - Als de teller een even getal is (2, 4, 6, …), dan maak je deze letter uppercase.
        - Anders laat je de letter zoals hij is.
    - Voeg het teken daarna toe aan de resultaatstring.

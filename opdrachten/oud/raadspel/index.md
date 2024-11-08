# Raadspel

"Getal onder de tien" is een spel waar je minstens twee mensen voor nodig hebt: degene die het
getal weet en degene die het raadt. Stel nou je hebt zin om dit in je eentje te spelen, dan is een
computer natuurlijk de perfecte medespeler ;-) En bovendien: waarom ophouden bij 10, dit kan je
natuurlijk ook doen tot 100 of 5843!

## Opdracht

Schrijf, in een bestand genaamd `raadspel.py`, een programma dat de gebruiker vraagt om een getal tussen 1 en een zelfgekozen "level". Blijf getallen vragen totdat de gebruiker het goede getal heeft geraden.

* Vraag als eerst de gebruiker om een level. Dit moet een positief getal zijn: als 0 of hoger wordt ingevoerd vraag dan opnieuw.
* Genereer een getal tussen 1 en het level dat de gebruiker moet raden. Hierbij mogen 1 en het level ook gekozen worden.
    * Zet bovenaan het programma `import random`
    * Gebruik de functie `random.randint(a, b)` om een willekeurig getal tussen `a` en `b` te kiezen
* Geef de gebruiker een tip na het raden, tips die je mag geven zijn:
    * `Je gok is te groot!`
    * `Je gok is te klein!`
    * `Je hebt het getal goed geraden, gefeliciteerd!`

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    import random

    def check_guess(guess: int, number: int) -> bool:
        """
        Check of de gok goed is. Als de gok niet goed is, return dan
        False en print of de gok te groot of te klein is.
        """

    def decide_number(level: int) -> int:
        """
        Kies een willekeurig getal tussen 1 en level.

        >>> decide_number(1)
        1
        >>> decide_number(100) <= 100
        True
        >>> 1 <= decide_number(2) <= 2
        True
        """

    if __name__ == '__main__':
        <Vraag de gebruiker om een (valide) level, kies een getal, laat de gebruiker gokken totdat de gok correct is.>

## Tip

-   Je moet de gebruiker zo lang laten gokken als nodig is, maar elke gok van de gebruiker moet wel valide zijn (dus bijvoorbeeld niet 13 als het level 10 is). Dit kan resulteren in het gebruik van een loop in een loop!

-   Doctests voor `decide_number()` zijn al  gegeven. Doctesten van random-functies zijn ingewikkelder om  te maken, daarom zijn hier de benodigde doctests bijgeleverd.

    - De eerste doctest geeft als `level` het getal 1. Dat betekent dat de enige output van de functie ook het getal 1 kan zijn.

    - De andere twee doctests laten op twee verschillende manieren zien dat de uitkomt van de functie altijd tussen 1 en `level` moet zitten.

    - De doctests tonen eigenlijk niet helemaal aan dat de functie goed werkt. Alleen  als je de doctests 100000 keer zou runnen en deze zou steeds akkoord geven dan is de kans wel heel groot dat de functie correct is!

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python raadspel.py
    Level: 10
    Gok: 3
    Je gok is te klein!
    Gok: 7
    Je gok is te groot!
    Gok: 6
    Je hebt het getal goed geraden, gefeliciteerd!

    $ python raadspel.py
    Level: 1
    Gok: 1
    Je hebt het getal goed geraden, gefeliciteerd!

    $ python raadspel.py
    Level: -5
    Level: 27
    Gok: 30
    Gok: 13
    Je gok is te groot!
    Gok: 8
    Je hebt het getal goed geraden, gefeliciteerd!

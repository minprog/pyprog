# Raadspel

"Getal onder de tien" is misschien wel een van de meest gespeelde spellen om keuzes te maken voor kinderen. Het is echter wel een spel waar je minstens twee mensen voor nodig hebt: degene die het getal weet en degene die het raadt.
Stel nou je hebt zin om dit in je eentje te spelen, dan is een computer natuurlijk de perfecte medespeler! Maar waarom ophouden bij 10, dit kan je natuurlijk ook doen tot 100 of 5843!

## Opdracht

Schrijf, in een bestand genaamd `raadspel.py`, een programma dat de gebruiker vraagt om een getal tussen 1 en een zelfgekozen level. Blijf getallen vragen totdat de gebruiker het goede getal heeft geraden.

* Vraag als eerst de gebruiker om een level, als een negatief level wordt ingevoerd (of 0) prompt dan voor een nieuw level.
* Genereer een getal tussen 1 en het level dat de gebruiker moet raden. Hierbij mogen 1 en het level ook gekozen worden.
* Geef de gebruiker een tip na het raden, tips die je mag geven zijn:
    * `Je gok is te groot!`
    * `Je gok is te klein!`
    * `Je hebt het getal goed geraden, gefeliciteerd!`
* Bij deze opdracht mag je niet aannemen dat de invoer geldig is. Check dit dan ook en zorg dat een nieuw level of een nieuwe gok moet worden gegeven na incorrecte invoer.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def check_guess(guess: int, number: int) -> bool:
        """
        Check of de gok goed is. Als de gok niet goed is, return dan
        False en print of de gok te groot of te klein is.
        """

    def decide_number(level: int) -> int:
        """
        Kies een willekeurig getal tussen 1 en level.
        """

    if __name__ == '__main__':
        Prompt de gebruiker voor een (valide) level, kies een getal, laat de gebruiker gokken totdat de gok correct is.

## Tips

* Je moet de gebruiker zo lang laten gokken als nodig is, maar elke gok van de gebruiker moet wel valide zijn. Dit kan resulteren in het gebruik van een loop in een loop.

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
    Level: Kat
    Level: 27
    Gok: 30
    Gok: Hond
    Gok: 13
    Je gok is te groot!
    Gok: 8
    Je hebt het getal goed geraden, gefeliciteerd!

# String-transformatie

Maak een Python-module genaamd `transformatie.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Verwijder letter 'n'

Schrijf een functie `verwijder_n` die alle letters `n` verwijdert uit een string en deze teruggeeft.

    def verwijder_n(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Net als bij het werkcollege blijkt dat het niet mogelijk is letterlijk delen van een string te _verwijderen_. Je zult daarom een nieuwe string moeten opbouwen op basis van de gegeven string `s` en die nieuwe string returnen.

## Verwijder letter 'n' aan eind van elk woord

Schrijf een functie `verwijder_n_eind` die alle letters `n` verwijdert uit een string en deze teruggeeft.

    def verwijder_n_eind(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Hiervoor moet je _vooruit kijken_. Je moet een loop maken op basis van posities, zodat je het teken op elke positie kan bekijken (`pos`) maar ook de letter op de volgende positie (`pos + 1`). Let wel op, dat als je bij het einde van de string bent (`pos = len(s)-1`) je niet naar de volgende positie mag kijken.

    for pos in len(s):
        ...

## Verwijder letter 'n' aan begin van elk woord

Schrijf een functie `verwijder_n_begin` die alle letters `n` verwijdert uit een string en deze teruggeeft.

    def verwijder_n(s: str) -> str:
        ...

Bedenk zelf een paar voorbeelden.

Hiervoor moet je _achteruit kijken_. Je moet een loop maken op basis van posities, zodat je het teken op elke positie kan bekijken (`pos`) maar ook de letter op de vorige positie (`pos - 1`). Let wel op dat je niet positie `-1` bekijkt als je op `pos = 0` bent.

    for pos in len(s):
        ...

## Om de letter uppercase 1

Schrijf een functie `spongebob1` die elke tweede letter in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Ook voor deze functie moet je een positie-loop maken zodat je weer "waar je bent" in de string. Als de oneven posities worden uppercase.

## Om de letter uppercase 2

Schrijf een functie `spongebob2` die elke tweede letter in een string naar uppercase omzet. Je mag de methode `.upper()` gebruiken om één letter naar uppercase te converteren.

Hier is een extra beperking, namelijk dat het echt alleen om letters gaat. Je moet met de methode `.isalpha()` checken of een teken alfabetisch is en alleen dan telt deze als letter.

Algoritme:

1. Maak een lege string waarin je het resultaat gaat opbouwen, plus een teller die op 0 staat.
2. Loop door alle tekens in de invoerstring met een `for char in s`-loop.
3. Houd een teller bij voor hoeveel letters je tot nu toe hebt gezien.
    - Als char een letter is (`char.isalpha()`), dan verhoog je de teller.
    - Als de teller een even getal is (2, 4, 6, …), dan maak je deze letter uppercase.
    - Anders laat je de letter zoals hij is.
4. Voeg het bewerkte teken toe aan de resultaatstring.
5. Geef de resultaatstring terug.

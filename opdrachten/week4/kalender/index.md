# Kalender

De kalender zoals we hem kennen kan op vele manieren worden weergegeven. Een van deze manieren is per maand:

    $ python kalender.py
    Jaar: 2022
    Maand: 9
              Sep 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
                      1   2   3
      4   5   6   7   8   9  10
     11  12  13  14  15  16  17
     18  19  20  21  22  23  24
     25  26  27  28  29  30

## Opdracht

Schrijf, in een bestand genaamd `kalender.py`, een programma dat op basis van een jaartal en maand een kalender weergeeft zoals hierboven afgebeeld.

Dit is algoritmisch een aardige uitdaging, want de datums moeten op de juiste weekdag geprint worden. Om dit correct te kunnen doen moet je weten op welke dag de eerste van de maand valt. En dat kun je berekenen als je van een willekeurige historische datum week op welke weekdag deze viel. Zo weten we bijvoorbeeld dat 1 januari 1800 een woensdag was.

De weekdagen gaan we nummeren. In de kalender hierboven zien we zondag als de eerste dag en zaterdag als de laatste; daarmee heeft zondag index 0 en zaterdag index 6. Woensdag is dus index 3 en daarmee kunnen we declareren dat 1 januari 1800 eveneens de index 3 heeft. We definiëren daarvoor een constante genaamd `START_DAY`.

Om te weten welke op welke weekdag 1 september 2022 is, moeten we dus weten:

* hoeveel dagen er tussen 1 januari 1800 en 1 september 2022 zitten (`days_from_1800`), en
* wat de dag van de week op 1 januari 1800 is (`START_DAY`).
* Samen geeft dit de formule `(days_from_1800 + START_DAY) % 7` voor de index van de eerste dag van de maand.

Tot slot, vergeet niet dat er schrikkeljaren kunnen zijn! Een jaar is een schrikkeljaar als het deelbaar is door 4. Maar wegens kalenderhervorming zijn jaren die deelbaar zijn door 100 geen schrikkeljaren, behalve als het ook nog eens deelbaar is door 400, dan is het juist wel weer een schrikkeljaar.

Je mag er bij deze opdracht vanuit gaan dat de gebruiker jaartallen `>= 1800` invult en valide maandnummers.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en verdere uitleg van de aanpak die je gekozen hebt. Zoals je ziet hebben we voor deze opdracht het hoofdprogramma al voor je geschreven; je hoeft dus alleen de andere functies aan te vullen.

Het wordt ook bij deze opdracht aangemoedigd om extra functies te introduceren die een klein deel van het probleem oplossen. Die moeten dan ook types hebben en doctests.

    # 1 januari 1800 is een woensdag
    START_DAY = 3

    def is_leap_year(year: int) -> bool:
        """
        Return True als `year` een schrikkeljaar is.
        """

    def days_from_1800(month: int, year: int) -> int:
        """
        Telt de dagen vanaf 1800 tot aan `month` of `year`.
        De eerste dag van `month` zit hier dus niet bij.
        Gebruikt `days_from_1800_until_year`, `is_leap_year` en `days_until_month`.
        """

    def days_from_1800_until_year(year: int) -> int:
        """
        Telt de dagen vanaf 1800 tot aan `year`.
        1 januari van het nieuwe jaar is niet meegerekend.
        """

    def days_until_month(month: int, year: int, is_leap_year: bool) -> int:
        """
        Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
        De dagen van `month` zitten hier dus niet bij.
        """

    def days_in_month(month: int, year: int) -> int:
        """
        Bepaalt het aantal dagen in `month` van `year`.
        Gebruikt `is_leap_year`.
        """

    def display_calendar(month: int, year: int) -> None:
        """
        Print de kalender.
        Gebruikt `display_header` en `display_grid`.
        """

    def display_header(month: int, year: int) -> None:
        """
        Print de koptekst van de kalender.
        """

    def display_grid(month: int, year: int) -> None:
        """
        Print het grid van de kalender.
        Gebruikt `first_weekday_month` en `days_in_month`.
        """

    def first_weekday_month(month: int, year: int) -> int:
        """
        Bepaalt de eerste weekdag van de maand.
        Gebruikt `days_from_1800`.
        """

    if __name__ == '__main__':
        year = int(input("Jaar: "))
        month = int(input("Maand: "))
        display_calendar(month, year)

## Tips

* Net als in Tiles kun je `print` aanpassen om <u>geen</u> newline te printen.

* De header heeft altijd dezelfde breedte, en je mag deze gerust hardcoden.

## Voorbeelden

Je programma moet uiteindelijk werken als in de voorbeelden hieronder.

    $ python kalender.py
    Jaar: 2022
    Maand: 6
              Jun 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
                  1   2   3   4
      5   6   7   8   9  10  11
     12  13  14  15  16  17  18
     19  20  21  22  23  24  25
     26  27  28  29  30

    $ python kalender.py
    Jaar: 2022
    Maand: 2
              Feb 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
              1   2   3   4   5
      6   7   8   9  10  11  12
     13  14  15  16  17  18  19
     20  21  22  23  24  25  26
     27  28

## Testen

* Begin altijd bij het begin: kijk of de kalender van januari 1800 correct weergegeven wordt (je weet dat 1 januari op woensdag valt).

* Kijk dan naar een makkelijk geval: gaat februari 1800 ook goed? Deze kalender moet aansluiten op die van februari.

* Kijk ook eens naar een recente kalender om te kijken of dat goed gaat. Hier zitten wel veel schrikkeljaren tussen, dus trek niet meteen de verkeerde conclusie, of je nu de juiste kalender ziet of niet.

* Zoek op welke schrikkeljaren er zijn of beredeneer op basis van de regels hierboven. Dan kun je zien of die jaren ook kloppen.

* Vergeet niet dat februari ook echt het correcte aantal dagen moet aangeven in een schrikkeljaar, en dat maart hier correct op moet aansluiten.

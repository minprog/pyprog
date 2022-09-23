# Kalender

De kalender zoals we hem kennen kan op vele manieren worden weergegeven. Een van deze manieren is per maand:

              Jun 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
                  1   2   3   4
      5   6   7   8   9  10  11
     12  13  14  15  16  17  18
     19  20  21  22  23  24  25
     26  27  28  29  30

## Opdracht

Schrijf, in een bestand genaamd `kalender.py`, een programma dat op basis van een jaartal en maand een kalender weergeeft op de manier zoals hierboven beschreven.

Dit is algoritmisch nogal een uitdaging want de datums moeten op de juiste weekdag geprint worden. Om dit correct te kunnen tonen, moet je weten op welke dag de eerste van de maand valt. Dit kan je berekenen door de eerste dag van een willekeurige maand te weten, bijvoorbeeld dat 1 januari 1800 een woensdag was.

In de kalender zien we zondag als de eerste dag en zaterdag als de laatste, zondag heeft dus index 0 en zaterdag 6. Dit resulteert erin dat 1 januari 1800 de index 3 heeft. Om te weten welke dag 1 juni 2022 is, moeten we dus weten:

* hoeveel dagen er tussen 1 januari 1800 en 1 juni 2022 zitten (`days_from_1800`),
* wat de index van 1 januari 1800 is (`START_1800`).

Samen geeft dit de formule `(days_from_1800 + START_1800) % 7` voor de index van de eerste dag van de maand.

Je mag er bij deze opdracht vanuit gaan dat de gebruiker jaartallen `>= 1800` invult en valide maandnummers.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    # 1 januari 1800 is een woensdag
    START_1800 = 3

    def check_leap_year(year: int) -> bool:
        """
        Return True als `year` een schrikkeljaar is.
        """

    def days_from_1800(month: int, year: int) -> int:
        """
        Telt de dagen vanaf 1800 tot aan `month`.
        De eerste dag van `month` zit hier dus niet bij.
        Gebruikt `days_from_1800_until_year`, `check_leap_year` en `days_until_month`
        """

    def days_from_1800_until_year(year: int) -> int:
        """
        Telt de dagen vanaf 1800 tot aan `year`.
        1 januari van het nieuwe jaar is niet meegerekend.
        """

    def days_until_month(month: int, LEAP: bool) -> int:
        """
        Telt het aantal dagen van 1 januari tot aan `month`.
        De dagen van `month` zitten hier dus niet bij.
        """

    def days_in_month(month: int, year: int) -> int:
        """
        Bepaalt het aantal dagen in `month`.
        Gebruikt `check_leap_year`.
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
        Print de grid van de kalender die alle dagen bevat.
        Gebruikt `first_weekday_month` en `days_in_month`.
        """

    def first_weekday_month(month: int, year: int) -> int:
        """
        Bepaalt de eerste weekdag van de maand (zo/ma/di..).
        Gebruikt `days_from_1800`.
        """

    if __name__ == '__main__':
        year = int(input("Geef het jaar: "))
        month = int(input("Geef de maand: "))
        display_calendar(month, year)

## Tips

* Net als in Tiles kun je `print` aanpassen om geen newline te printen.

* De display van de header is altijd dezelfde breedte, en dit mag je hardcoden.

* Vergeet niet dat er schrikkeljaren kunnen zijn! Een jaar is een schrikkeljaar als het deelbaar is door 4. Maar wegens kalenderhervorming zijn jaren die deelbaar zijn door 100 geen schrikkeljaren, behalve als het ook nog eens deelbaar is door 400, dan is het juist wel weer een schrikkeljaar.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python kalender.py
    Geef het jaar: 2022
    Geef de maand: 6
              Jun 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
                  1   2   3   4
      5   6   7   8   9  10  11
     12  13  14  15  16  17  18
     19  20  21  22  23  24  25
     26  27  28  29  30

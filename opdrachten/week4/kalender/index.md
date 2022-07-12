# Kalender

## Kalender

De kalender zoals we hem kennen kan op vele manieren worden weergegeven. Een van deze manieren is per maand:

              Jun 2022
    --------------------------
    Zo  Ma  Di  Wo  Do  Vr  Za
                 1   2   3   4

     5   6   7   8   9  10  11

    12  13  14  15  16  17  18

    19  20  21  22  23  24  25

    26  27  28  29  30

## Opdracht

Schrijf, in een bestand genaamd `kalender.py`, een programma dat op basis van een jaartal en maand een kalender weergeeft op de manier zoals hierboven beschreven.

Dit is algoritmisch nogal een uitdaging want er worden ook weekdagen (zo/ma/di) weergegeven, en deze moeten passen bij de dagnummers van de maand. Om dit correct te kunnen tonen, moet je weten op welke dag de eerste van de maand valt. Dit kan je berekenen door de eerste dag van een willekeurige maand te weten, bijvoorbeeld dat 1 januari 1800 een woensdag was.

In de kalender zien we zondag als de eerste dag en zaterdag als de laatste, zondag heeft dus index 0 en zaterdag 6. Dit resulteert erin dat 1 januari 1800 de index 3 heeft. Om te weten welke dag 1 juni 2022 is, moeten we dus weten:
* hoeveel dagen er tussen 1 januari 1800 en 1 juni 2022 zitten (`days_from_1800`),
* wat de index van 1 januari 1800 is (`START_1800`).
Samen geeft dit de formule `(days_from_1800 + START_1800) % 7` voor de index van de eerste dag van de maand.

Je mag er bij deze opdracht vanuit gaan dat de gebruiker jaartallen `>= 1800` invult en valide maandnummers.

## Decompositie

Omdat er veel verschillende aspecten geïmplementeerd moeten worden, helpen we je deze opdracht nog wat extra in de decompositie van het probleem.
De functies die je nodig hebt, worden zoals bij elke opdracht onder het kopje `Code` beschreven. Maar eerst krijg je hier een overzicht van de verschillende functies en hoe ze met elkaar zijn verweven.

    display_calendar
        display_header
        display_grid
            first_day_month
                days_from_1800
                    days_from_1800_till_year
                    check_leap_year
                    days_till_month
            days_in_month
                check_leap_year

Dit houdt in dat in `display_calendar` de functies `display_header` en `display_grid` worden aangeroepen. In de functie `display_header` worden geen zelfgeschreven functies aangeroepen, in `display_grid` echter wel. Namelijk `first_day_month` en `days_in_month`. Op analoge wijze kan je zien in welke functies er andere zelfgeschreven functies worden aangroepen.


## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    START_1800 = 3

    def check_leap_year(year: int) -> bool:
        """
        Return True als year een schrikkeljaar is.
        """

    def days_from_1800(month: int, year: int) -> int:
        """
        Tel de dagen vanaf 1800 tot aan month. De eerste dag van month zit hier dus niet bij.
        """

    def days_from_1800_till_year(year: int) -> int:
        """
        Tel de dagen vanaf 1800 tot aan year. 1 januari van het nieuwe jaar is niet meegerekend.
        """

    def days_till_month(month: int, LEAP: bool) -> int:
        """
        Tel het aantal dagen van 1 januari tot aan month. De dagen van month zitten hier dus niet bij.
        """

    def days_in_month(month: int, year: int) -> int:
        """
        Bepaal het aantal dagen in month
        """

    def display_calendar(month: int, year: int):
        """
        Print de kalender.
        """

    def display_header(month: int, year: int):
        """
        Print de koptekst van de kalender.
        """

    def display_grid(month: int, year: int):
        """
        Print de grid van de kalender die alle dagen bevat.
        """

    def first_day_month(month: int, year: int) -> int:
        """
        Bepaal de eerste dag van de maand (zo/ma/di..) op basis van de eerste dag in het jaar 1800.
        """

    if __name__ == '__main__':

        year = int(input("Geef het jaar in XXXX "))
        month = int(input("Geef de maand in XX "))

        display_calendar(month, year)

## Tips

* Voor het printen van de grid, moet je meerdere dingen printen per regel. Dit kan met behulp van het gebruiken van `end` in je printstatement. Voor meer informatie, zie hoofdstuk 4 van Practical Programming.
* De display van de header is altijd dezelfde breedte, dit mag je dan ook hardcoden. Denk hierbij ook weer aan alle opties binnen de strings (hoofdstuk 4).
* Vergeet niet dat er schrikkeljaren kunnen zijn! Een jaar is een schrikkeljaar als het deelbaar is door 4. Wegens kalenderhervorming zijn jaren die deelbaar zijn door 100 geen schrikkeljaren, behalve als het ook nog eens deelbaar is door 400, dan is het juist wel weer een schrikkeljaar.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python kalender.py
    Geef het jaar in XXXX 2022
    Geef de maand in XX 6
            Jun 2022
    --------------------------
    Zo  Ma  Di  Wo  Do  Vr  Za
                 1   2   3   4

     5   6   7   8   9  10  11

    12  13  14  15  16  17  18

    19  20  21  22  23  24  25

    26  27  28  29  30

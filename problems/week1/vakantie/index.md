# Vakantiekosten

## Vakantie
Je wil in je eentje op vakantie naar Frankrijk, maar dat kost nogal wat.
De kosten van de reis naar het verblijf zijn afhankelijk van hoe veel kilometer je moet reizen en hoe lang je blijft. Je gaat met de auto en dat kost 0.13 cent per km. Daarnaast kost het verblijf 60 euro per nacht.

## Opdracht
Schrijf, in een bestand genaamd `vakantie.py`, een programma dat berekent hoeveel je vakantie kost op basis van hoe ver weg je gaat en het aantal dagen dat je op vakantie gaat. Je mag hierbij ervan uit gaan dat alle invoer invoer geldig is.

## Code

In deze opdracht bestaat je code uit twee zelfgeschreven functies.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def travel_costs(km: int) -> int:
        """
        Bepaal de vervoerskosten op basis van de te rijden afstand naar de accomodatie.
        """

    def overnight_costs(nights: int) -> int:
        """
        Bepaal de overnachtingskosten op basis van het aantal nachten dat je op vakantie gaat.
        """

    Schrijf hier code die input van de gebruiker krijgt en print hoeveel de vakantie gaat kosten.

## Tips

* Het totaal aan vakantie kosten is de som van de vervoers- en overnachtingskosten.
* Houdt bij `travel_costs(km)` in de gaten dat je niet alleen heen maar ook terug moet rijden!
* Zorg dat in je functies je getallen worden afgerond, zodat je output een integer is.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 1250
    Hoe veel nachten is je verblijf? 5
    Jouw vakantie kost: 634


    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 800
    Hoe veel nachten is je verblijf? 10
    Jouw vakantie kost: 826

    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 2159
    Hoe veel nachten is je verblijf? 12
    Jouw vakantie kost: 1302

# Cafeïne inname

## Cafeïne

Om gezond te blijven is het belangrijk om te letten op je cafeïne inname en te zorgen dat deze niet te hoog is.
Hierbij een lijst met de hoeveelheid cafeïne voor één portie van verschillende dranken.

* Coffee - 90 mg
* Thee - 45 mg
* Energiedrankjes - 80 mg
* Cola - 40 mg

## Opdracht

Schrijf, in een bestand genaamd `cafeine.py`, een programma dat de gebruiker vraagt hoeveel cafeïne houdende dranken die drinkt en vervolgens de totale cafeïne inname berekent.
Hierbij mag je ervan uit gaan dat de gebruiker getallen groter dan nul invult.

## Code

In deze opdracht bestaat je code uit een zelfgeschreven functie en het aanroepen van een aantal functies.
Je moet hier niet alleen je zelfgeschreven functie aanroepen maar ook een aantal functies die al implementeerd zijn in Python.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
        """
        Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
          drankjes van het type koffie, thee, energie, en cola.
        """

    Roep hier de benodigde functies aan.

## Tips

* Voor deze opdracht moet je een functie schrijven, houd de functional design recipe bij de hand hiervoor.
* We hebben input van de gebruiker nodig om de hoeveelheid caffeïne te berekenen, welke ingebouwde functie van Python kunnen we hiervoor gebruiken?


## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python cafeine.py
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 1
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Je krijgt 225 mg cafeïne binnen.

    $ python cafeine.py
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 2
    Hoeveel glazen cola? 0
    Je krijgt 340 mg cafeïne binnen.

    $ python cafeine.py
    Hoeveel koppen koffie? 0
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 1
    Je krijgt 40 mg cafeïne binnen.

    $ python cafeine.py
    Hoeveel koppen koffie? 5
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Je krijgt 450 mg cafeïne binnen.

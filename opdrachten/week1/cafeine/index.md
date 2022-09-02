# Cafeïne

Om gezond te blijven is het belangrijk om te letten op je cafeïne-inname en te zorgen dat deze niet te hoog is.
Hierbij een lijst met de hoeveelheid cafeïne voor één portie van verschillende dranken.

* Coffee - 90 mg
* Thee - 45 mg
* Energiedrankjes - 80 mg
* Cola - 40 mg

## Opdracht

Schrijf, in een bestand genaamd `cafeine.py`, een programma dat de gebruiker vraagt hoeveel cafeïne houdende dranken die drinkt en vervolgens de totale cafeïne-inname berekent.
Hierbij mag je ervan uitgaan dat de gebruiker getallen groter dan nul invult, en dus geen fouten maakt bij de invoer.

## Code

In deze opdracht bestaat je code uit een zelfgeschreven functie en het aanroepen van een aantal functies.
Je moet hier niet alleen je zelfgeschreven functie aanroepen maar ook een aantal functies die al implementeerd zijn in Python.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen en de gewenste uitkomsten (stap 3 van het function design recipe), en eventueel verdere uitleg.
Schrijf ook code om de functie aan te roepen.

    def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
        """
        Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
          drankjes van het type koffie, thee, energie, en cola.
        """

    <Schrijf op deze plek code voor de invoer en roep de functie aan>

## Tips

* Voor deze opdracht moet je een functie schrijven, dus houd het functional design recipe (FDR) bij de hand.
* We hebben invoer van de gebruiker nodig om de hoeveelheid cafeïne te berekenen, welke ingebouwde functie van Python kunnen we hiervoor gebruiken?
* Je ziet dat de naam van de functie en van de parameters in het Engels is, maar het commentaar is in het Nederlands. Dit is bewust zo gedaan, dus zorg dat je dit patroon ook blijft volgen.


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

# Cafeïne

Om gezond te blijven is het belangrijk om te letten op je cafeïne-inname en te zorgen dat deze niet te hoog is.
Hierbij een lijst met de hoeveelheid cafeïne voor één portie van verschillende dranken.

* Coffee - 90 mg
* Thee - 45 mg
* Energiedrankjes - 80 mg
* Cola - 40 mg

## Opdracht

Schrijf, in een bestand genaamd `cafeine.py`, een programma dat de gebruiker vraagt hoeveel cafeïnehoudende dranken die drinkt en vervolgens de totale cafeïne-inname berekent.
Hierbij mag je ervan uitgaan dat de gebruiker getallen groter dan of gelijk aan nul invult, en dus geen fouten maakt bij de invoer.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.
Maar dat is niet de enige eis aan je uitwerking!
Let ook op de voorwaarden die vermeld staan in de rest van de opdracht.

    $ python3 cafeine.py
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 1
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Je krijgt 225 mg cafeïne binnen.

    $ python3 cafeine.py
    Hoeveel koppen koffie? 2
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 2
    Hoeveel glazen cola? 0
    Je krijgt 340 mg cafeïne binnen.

    $ python3 cafeine.py
    Hoeveel koppen koffie? 0
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 1
    Je krijgt 40 mg cafeïne binnen.

    $ python3 cafeine.py
    Hoeveel koppen koffie? 5
    Hoeveel koppen thee? 0
    Hoeveel energiedrankjes? 0
    Hoeveel glazen cola? 0
    Je krijgt 450 mg cafeïne binnen.

## Code

In deze opdracht bestaat je code uit een zelfgeschreven functie en een hoofdprogramma.
Je moet hier niet alleen je zelfgeschreven functie aanroepen maar ook een aantal functies die al geïmplementeerd zijn in Python.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen en de gewenste uitkomsten (stap 3 van het function design recipe), en eventueel verdere uitleg.

Schrijf ook code om invoer te vragen en de functie aan te roepen. Het is gebruikelijk (en in deze cursus verplicht) om de invoer en het uitprinten af te handelen in het `main`-deel, zoals hieronder aangegeven. De *berekening* vindt dan juist in een aparte functie plaats.

    def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
        """
        Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
          drankjes van het type koffie, thee, energie, en cola.
        """

    if __name__ == '__main__':
        <Schrijf op deze plek code voor de invoer en roep de functie aan>

## Tips

*   Je ziet dat de naam van de functie en van de parameters in het Engels is, maar het commentaar is in het Nederlands. Dit is bewust zo gedaan, dus zorg dat je dit patroon ook blijft volgen.

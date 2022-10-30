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

* Voor deze opdracht moet je een functie schrijven, dus houd het functional design recipe (FDR) bij de hand.
* We hebben invoer van de gebruiker nodig om de hoeveelheid cafeïne te berekenen; welke ingebouwde functie van Python kunnen we hiervoor gebruiken?
* Je ziet dat de naam van de functie en van de parameters in het Engels is, maar het commentaar is in het Nederlands. Dit is bewust zo gedaan, dus zorg dat je dit patroon ook blijft volgen.

## Doctests

In het boek heb je kennis gemaakt met "voorbeeld-aanroepen". Deze noemen we ook wel **doctests**, voor tests die in de docstring staan. Zie hieronder weer het voorbeeld van de functie `days_difference` waarvoor drie voorbeelden ingevoegd zijn.

    >>> def days_difference(day1: int, day2: int) -> int:
    ... """Return the number of days between day1 and day2, which are
    ... both in the range 1-365 (thus indicating the day of the
    ... year).
    ...
    ... >>> days_difference(200, 224)
    ... 24
    ... >>> days_difference(50, 50)
    ... 0
    ... >>> days_difference(100, 99)
    ... -1
    ... """
    ... return day2 - day1

Als je exact op die manier voorbeelden (doctests) bij jouw functie schrijft, dan worden deze automatisch getest als je je oplossing instuurt op deze website. Daarmee weten we of jouw oplossing consistent is met je zelfbedachte tests. Dat zijn overigens niet de enige tests die we doen! Want er worden ook nog tests gedaan om te controleren of jouw uitwerking ook klopt met de *opdracht*.

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

## Insturen

Je kunt je uitwerking onderaan deze pagina insturen. Na enige minuten vind je op de [voortgangspagina](/submissions) een knop om de resultaten van de automatische controle te bekijken. Als er nog fouten zijn, verbeter ze dan en stuur opnieuw in.

Hoeveel tijd heb je gewerkt aan deze opdracht?

<input name="form[qTime]" type="text" required>

Waren er nog dingen waar je op vastliep bij deze opdracht?

<textarea name="form[qVastlopers]">

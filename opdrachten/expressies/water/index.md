# Water

Implementeer een programma dat aan een gebruiker diens waterverbruik rapporteert, door het aantal minuten douchen om te rekenen naar flesjes drinkwater. Eén minuut douchen komt overeen met 12 flesjes water (van 0.5L).

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    Hoeveel minuten douche je? 1
    12

    Hoeveel minuten douche je? 10
    120

## Code

Ontwerp je code zoals hieronder beschreven. Vul de doctests aan en voeg dan de implementatie toe. Welke Python-onderdelen uit de eerste hoofdstukken van het boek kun je hiervoor gebruiken?

    def hoeveelheid_water(minuten: int) -> int:
        """
        Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
        gegeven het aantal minuten douchen.
        """

    if __name__ == '__main__':
        <vraag input, roep functie aan, en print resultaat

## Specificatie

* De functie moet minimaal 3 gevarieerde en realistische doctests krijgen.

* Om het simpel te houden, mag je aannemen dat de gebruiker altijd braaf een positief getal invoert. Je hoeft dus geen foutafhandeling te implementeren voor het geval de gebruiker dat niet doet.

* Het resultaat moet er precies uitzien als de voorbeelden hierboven.

## Hints

* Maak eerst de functie `hoeveelheid_water`. Achterhaal uit bovenstaande opdracht en uit de voorbeelden de formule die we nodig hebben om de berekening te doen. Dan is het belangrijkste deel van het werk gedaan.

* Maak gebruik van de `input`-functie en gebruik `int()` om de invoer van de gebruiker om te zetten van een string naar een integer, zodat je de berekening kunt uitvoeren.

## Testen

Loop eerst je eigen programma na, werkt deze voor alle normale invoer? Vul bijvoorbeeld eens als aantal douche-minuten de waarden 0, 10 en 137 in.

Lijkt alles te werken, stuur je opdracht dan in. De website zal de opdracht nakijken. Zie je unhappy smileys in de check-resultaten, en kom je er niet uit wat er fout gaat? Vraag om hulp!

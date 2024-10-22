# Vakantiekosten

> **Studeertip.** Heb je het idee dat je Python niet begrijpt? Bestudeer dan de uitleg in het boek en probeer alle voorbeelden goed te begrijpen. Ook hier geldt: stel vragen en schakel hulp in. Bedenk wel dat we nog niet alle details uitleggen nu, een deel komt later! Daarnaast is het belangrijk dat je leert experimenteren met Python. Maak mini-programma's om te begrijpen hoe een functie van Python werkt. Vraag hoe!

Je wil in je eentje op vakantie naar Frankrijk, maar dat kost nogal
wat. De kosten van de reis naar het verblijf zijn afhankelijk van
hoeveel kilometer je moet reizen en hoe lang je blijft. 

## Opdracht

Schrijf, in een bestand genaamd `vakantie.py`, een programma dat
berekent hoeveel je vakantie kost. De vervoerskosten zijn 13 cent per
kilometer voor zowel de heen- als de terugreis. De verblijfskosten zijn
60 euro per nacht. De totale kosten moeten worden afgerond naar
de dichtbijzijnde hele euro.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 1250
    Hoe veel nachten is je verblijf? 5
    Jouw vakantie kost: 625

    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 800
    Hoe veel nachten is je verblijf? 10
    Jouw vakantie kost: 808

    $ python vakantie.py
    Hoe ver ga je weg in kilometers? 2159
    Hoe veel nachten is je verblijf? 12
    Jouw vakantie kost: 1281

## Code

In deze opdracht bestaat je code uit drie zelfgeschreven functies.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen (doctests!) en de gewenste uitkomsten (stap 3 van het FDR), en eventueel verdere uitleg.
Schrijf ook code om invoer te vragen en de functie aan te roepen.

    def travel_costs(km: int) -> float:
        """
        Bepaalt de vervoerskosten op basis van de te rijden afstand
        naar de accomodatie (tel `km` twee keer voor heen en terug).
        """
    
    def overnight_costs(nights: int) -> float:
        """
        Bepaalt de overnachtingskosten op basis van het aantal nachten
        dat je op vakantie gaat.
        """
    
    def total_costs(km: int, nights: int) -> int:
        """
        Bepaalt de totale kosten op basis van de afstand en het aantal
        nachten en rondt af naar hele euro's.
        Deze functie delegeert zoveel mogelijk werk naar de andere
        twee functies (roep die dus hier aan).
        """
    
    if __name__ == '__main__':
        <Schrijf hier code die input van de gebruiker opvraagt,
        total_costs aanroept, en print hoeveel de vakantie gaat kosten>

## Tips

* Je moet nu meerdere functies implementeren. Deze functies werken samen om de kosten te berekenen. In de docstring staat welke functie de andere twee functies moet aanroepen.

* Zorg dat de uiteindelijke kosten worden afgerond, zodat je output een integer is. In de docstring staat wanneer je moet afronden. Ga dan ook geen tussenstappen afronden, want dan krijg je een verkeerd antwoord.

    * De ingebouwde Python-functie `round()` werkt niet goed voor deze opdracht. Die functie gebruikt een statistisch verantwoorde manier van afronden: `round(2.5)` geeft `2`. Maar in deze opdracht gaat het over afronden van geld, wat normaliter wordt gedaan op de manier die je op school leert: `2.4` wordt `2` en `2.5` wordt `3`. Je kunt deze manier van afronden bereiken met de volgende expressie: `int(x + 0.5)` waarbij `x` is het af te ronden getal. Het is geen slecht idee om een aparte zelfgeschreven functie te definiëren voor het afronden, maar dat is optioneel. Je moet hoe dan ook wel de juiste manier van afronden gebruiken.

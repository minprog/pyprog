# Vakantiekosten

Je wil in je eentje op vakantie naar Frankrijk, maar dat kost nogal
wat. De kosten van de reis naar het verblijf zijn afhankelijk van
hoeveel kilometer je moet reizen en hoe lang je blijft. 

## Opdracht

Schrijf, in een bestand genaamd `vakantie.py`, een programma dat
berekent hoeveel je vakantie kost. De vervoerskosten zijn 13 cent per
kilometer voor zowel de heen- als de terugreis. De verblijfskosten zijn
60 euro per nacht. De totale kosten moeten worden afgerond naar
de dichtbijzijnde hele euro.

## Code

In deze opdracht bestaat je code uit drie zelfgeschreven functies.

Ontwerp je code zoals hieronder beschreven.
Vul de docstrings aan met voorbeeld-aanroepen (doctests!) en de gewenste uitkomsten (stap 3 van het FDR), en eventueel verdere uitleg.
Schrijf ook code om invoer te vragen en de functie aan te roepen.

    
    def travel_costs(km: int) -> float:
        """
        Bepaalt de vervoerskosten op basis van de te rijden afstand naar de accomodatie.
        """

    def overnight_costs(nights: int) -> float:
        """
        Bepaalt de overnachtingskosten op basis van het aantal nachten dat je op vakantie gaat.
        """
        
    def total_costs(km: int, nights: int) -> int:
        """
        Bepaalt de totale kosten op basis van de afstand en het aantal nachten en rond af naar hele euros.
        """
    
    if __name__ == '__main__':
        <Schrijf hier code die input van de gebruiker krijgt en print hoeveel de vakantie gaat kosten>

## Tips

* Houd bij `travel_costs(km)` in de gaten dat je niet alleen heen maar ook terug moet rijden, terwijl de functie de afstand voor alleen de heenreis ontvangt!

* Zorg dat de uiteindelijke kosten worden afgerond, zodat je output een integer is.

    * De ingebouwde Python-functie `round()` werkt niet goed voor deze opdracht. Die functie gebruikt een statistisch verantwoorde manier van afronden: `round(2.5)` geeft `2`. Maar in deze opdracht gaat het over afronden van geld, wat normaliter wordt gedaan op de manier die je op school leert: `2.4` wordt `2` en `2.5` wordt `3`. Je kunt deze manier van afronden bereiken met de volgende expressie: `int(x + 0.5)` waarbij `x` is het af te ronden getal. Het is geen slecht idee om een aparte zelfgeschreven functie te definiëren voor het afronden, maar dat is optioneel. Je moet hoe dan ook wel de juiste manier van afronden gebruiken.

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

## Insturen

Je kunt je uitwerking onderaan deze pagina insturen. Na enige minuten vind je op de [voortgangspagina](/submissions) een knop om de resultaten van de automatische controle te bekijken. Als er nog fouten zijn, verbeter ze dan en stuur opnieuw in.

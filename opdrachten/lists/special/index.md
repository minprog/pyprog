# Special sort

Schrijf een functie die een lijst aanneemt en deze sorteert volgens ons speciale sorteeralgoritme.

## Details

Dit algoritme is geen bestaand sorteeralgoritme met een mooie naam. Maar het werkt wel! Als je selection sort al succesvol hebt geïmplementeerd zal het makkelijker zijn dit algoritme te maken (dat betekent niet dat het er per se op lijkt, maar dat je meer ervaring hebt met de kleine stapjes). Gebruik de volgende stappen:

- Het algoritme moet van links naar rechts elke positie in de lijst langsgaan.

    - Elke stap zullen meer getallen gesorteerd raken (tenzij ze om te beginnen al gesorteerd waren natuurlijk).
    
    - Dat we van links naar rechts sorteren betekent dat we het laatste element niet meer mee hoeven nemen. Dit is namelijk al gesorteerd geraakt toen we de andere getallen behandelden.
    
- Voor elk van de posities die we langsgaan, beschouw alle posities rechts daarvan.

    - Voor elke combinatie van posities, als de eerste groter is, swap ze.
    
    - Als je bijvoorbeeld bij positie 0 bent, beschouw je de combinatie met posities 1, 2, 3, enz.... en swap je elke keer als nodig is. Het kan dus zijn dat je 0 en 1 swapt, en daarna ook 0 en 2 swapt.

## Hint

1. Kijk of je de procedure op papier handmatig kunt doen. Dan krijg je een beter gevoel voor de regelmaat die in het algoritme verscholen zit.

2. Schrijf het algoritme uit in een concreter stappenplan waar je al de "taal" van lists gebruikt en variabelenamen (we hebben hierboven in de beschrijving heel zorgvuldig géén variabelen gebruikt, maar dat kan dus wel). Dit is je pseudocode.

## Code

Gebruik de pseudocode om het sorteren te implementeren. Ontwerp je code zoals hieronder beschreven. Schrijf veel doctests, zodat de correcte werking van het sorteren goed wordt aangetoond, en het hoofdprogramma.

Let op dat de functie de lijst l moet aanpassen, maar deze alsnog moet returnen. Dat is nodig om handig doctests te kunnen doen.

    from typing import Any
    
    def special_sort(l: list[int]) -> list[int]:
        """
        Sorteert de lijst `l` door deze aan te passen.
        Er wordt geen nieuwe lijst gemaakt.
        Moet wel `l` returnen.
        """

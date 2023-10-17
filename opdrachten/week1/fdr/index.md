# Function Design Recipe

Maak een Python-bestand aan genaamd `fdr.py`. Voeg eerst de volgende functie toe aan het bestand. Dit is een voorbeeld uit het boek. Het is een functie die één parameter heeft, een getal `n`, en het percentage taart teruggeeft (returnt) dat elk van de `n` personen kan eten.

    def pie_percent(n: int) -> int:
        """Precondition: n > 0

        Assuming there are n people who want to eat a pie, return the percentage
        of the pie that each person gets to eat.

        >>> pie_percent(5)
        20
        >>> pie_percent(2)
        50
        >>> pie_percent(1)
        100
        """
        return int(100 / n)

Vervolgens ga je een aantal functies zelf ontwikkelen en toevoegen aan het bestand.

1. Ontwikkel met hulp van het function design recipe een functie die één parameter heeft, een getal, en dat getal verdrievoudigd teruggeeft.
1. Ontwikkel met hulp van het function design recipe een functie die twee parameters heeft, allebei getallen, en de absolute waarde van het verschil tussen die twee teruggeeft. Hint: roep de ingebouwde functie `abs` aan als onderdeel van je functie.
1. Ontwikkel met hulp van het function design recipe een functie die één parameter heeft, een afstand in kilometers, en een vergelijkbare afstand in mijlen teruggeeft. Neem aan dat er 1,6 kilometers in een mijl zitten.
1. Ontwikkel met hulp van het function design recipe een functie die drie parameters heeft, alledrie cijfers tussen 0 en 100 inclusief, en het gemiddelde van deze cijfers teruggeeft.
1. Ontwikkel met hulp van het function design recipe een functie die vier parameters heeft, allemaal cijfers tussen 0 en 100 inclusief, en het gemiddelde van de beste drie cijfers teruggeeft. Verplicht: roep als onderdeel de functie aan die je in de vorige opdracht hebt gemaakt.

## Hint

In het boek staat welke onderdelen een functie moet hebben als je het function design recipe moet volgen.

## Inleveren

Inleveren kan op de Submit-tab van deze pagina. Je uitwerking wordt automatisch gecontroleerd op juiste werking. Is er iets mis? Vraag om hulp! Je kunt wel alvast door naar de volgende module, zolang je deze opdracht nog maar verbetert.

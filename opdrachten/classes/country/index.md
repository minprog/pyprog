# Country

Maak een Python-bestand aan genaamd `country.py`. Voeg de volgende `main`-code toe.

    if __name__ == '__main__':

        # stap 1
        # per land: naam, aantal mensen, opp. in vierkante kilometers
        canada = Country('Canada', 34482779, 9984670)
        print(canada.name)
        print(canada.population)
        print(canada.area)

        # stap 2
        usa = Country('United States of America', 313914040, 9826675)
        print(canada.is_larger(usa)) # geeft True

        # stap 3
        # bevolkingsdichtheid <- mensen per vierkante kilometer
        print(canada.population_density())

        # stap 4
        # definieer de __str__ method
        usa = Country('United States of America', 313914040, 9826675)
        print(usa)

## Stap 1: een simpele data-class

Schrijf de class zodat stap 1 werkt. Zorg dat de class een "name", een "population" en een "area" kan opslaan. De testcode moet netjes de drie waarden printen (pas de testcode niet aan).

## Stap 2: vergelijken

Maak een nieuwe methode `is_larger`. Deze neemt als extra parameter nog een *ander* `Country`-object aan en vergelijkt hun groottes (kilometers). Schrijf de `def` zo:

    def is_larger(self, other: 'Country'):
        ...

In deze methode heb je nu en `self` en een `other`. Allebei zijn het `Country`-objecten en van allebei kun je de `area` opvragen. Dus kun je deze oppervlaktes ook vergelijken en het verschil returnen.

## Stap 3: berekening

Schrijf de methode `population_density()` om de bevolkingsdichtheid te berekenen.

## Stap 4: netjes printen

Als je een object `print` dan krijg je normaal een lelijke omschrijving van het object en het geheugenadres in de computer. Heb je niks aan. Je kunt zelf de `__str__`-methode implementeren. Als je dan `print` aanroept ziet het er netjes uit.

Specifiek voor deze opdracht moet die laatste `print` de volgende output geven:

    United States of America has a population of 313914040 and is 9826675 square km.

Maak een `def __str__(self)` die zo'n string teruggeeft.

## Testen

1. Run de code met de `main` en zorg dat het precies de juiste ouptut geeft.

2. Kopieer nu de code uit `main` naar je functies als doctests! Voeg wel de gewenste output van de prints nog toe. Die staat er nu niet tussen.

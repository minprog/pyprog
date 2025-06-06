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

Die laatste `print` moet de volgende output geven:

    United States of America has a population of 313914040 and is 9826675 square km.

Implementeer stap voor stap de `Country` class om te zorgen dat de bovenstaande testcode goed werkt. Voeg ook doctests toe volgens de voorbeelden in het boek!

## Hint

- Gebruik alleen wat je uit het boek geleerd hebt.

- Als header voor `is_larger` gebruik je `def is_larger(self, other: Self) -> bool:`. De vermelding `Self` betekent dat die parameter graag een object van de class `Country` wil hebben. Om dit te gebruiken moet je bovendien `from typing import Self` doen.

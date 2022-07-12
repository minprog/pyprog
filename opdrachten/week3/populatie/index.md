# Populatie verloop

## Populatie

Stel we hebben een populatie van `n` lama's. Elk jaar worden er `n / 3` nieuwe lama's geboren en sterven er `n / 4` lama's.
Bijvoorbeeld, als we starten met `n = 1200` lama's, dan worden er in het eerste jaar, `1200 / 3 = 400` nieuwe lama's geboren. Maar er zijn ook `1200 / 4 = 300` lama's die overlijden.
Aan het einde van het jaar zijn er dan dus `1200 + 400 - 300 = 1300` lama's, een groei van 100 lama's!

Een ander voorbeeld is als we starten met `n = 1000` lama's. Dan zouden we aan het einde van het jaar `1000 / 3 = 333.33` nieuwe lama's hebben. Omdat we alleen maar hele lama's kunnen hebben, ronden we dit naar beneden af naar `333` lama's.
In het zelfde jaar sterven er `1000 / 4 = 250` lama's, dus we eindig met `1000 + 333 - 250 = 1083` lama's aan het einde van het jaar. Hier is de populatie dit jaar dus met 83 lama's gegroeid.

Met deze twee formules kunnen we berekenen hoeveel jaar het duurt om van een start populatie van `n` lama’s een populatie van `m` lama’s te bereiken.

## Opdracht

Schrijf, in een bestand genaamd `populatie.py`, een programma dat berekent hoeveel jaar het duurt om van een start populatie tot een specifieke eind populatie te komen.
Zowel de start als de eind populaties moeten als input worden gegeven door de gebruiker.

* Voor dit programma moet je de gebruiker vragen naar de startgrootte en eindgrootte:
    * De startgrotte moet groter of gelijk zijn dan 9 (aangezien de groei anders erg snel stabiliseerd). Als de gebruiker een waarde geeft dat geen geheel getal is of kleiner dan 9, moet je de gebruiker prompten voor een nieuw getal.
    * De eindgrootte moet groter zijn dan de startgrootte. Opnieuw geldt dat je de gebruiker moet prompten voor een geldige input als een ongeldige input wordt gegeven.
* Wanneer het aantal jaar dat het duurt om de eindpopulatie te bereiken niet een geheel getal is, moet je dat naar boven afronden.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

    def calculate_years(start_size: int, end_size: int) -> int:
        """
        Return het aantal jaar dat het duurt voor de populatie om van start_size end_size te bereiken.
        """

    if __name__ == '__main__':
        Prompt de gebruiker voor een valide startgrootte en eindgrootte. Bereken en print vervolgens het benodigd aantal jaren.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

      $ python populatie.py
      Startgrootte: 1200
      Eindgrootte: 1300
      Jaren: 1

      $ python populatie.py
      Startgrootte: -5
      Startgrootte: 3
      Startgrootte: 9
      Eindgrootte: 5
      Eindgrootte: 18
      Jaren: 8

      $ python populatie.py
      Startgrootte: 20
      Eindgrootte: 1
      Eindgrootte: 10
      Eindgrootte: 100
      Jaren: 20

      $ python populatie.py
      Startgrootte: 100
      Eindgrootte: 1000000
      Jaren: 115

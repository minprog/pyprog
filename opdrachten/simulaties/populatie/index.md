# Populatie-verloop

Stel we hebben een populatie van `n` lama's. Elk jaar worden er `n / 3` nieuwe lama's geboren en sterven er `n / 4` lama's.
Bijvoorbeeld, als we starten met `n = 1200` lama's, dan worden er tijdens het eerste jaar, `1200 / 3 = 400` nieuwe lama's geboren. Maar er zijn ook `1200 / 4 = 300` lama's die overlijden.
Precies een jaar later zijn er dan `1200 + 400 - 300 = 1300` lama's, een groei van 100 lama's!

Een ander voorbeeld is als we starten met `n = 1000` lama's. Dan zouden we aan na het jaar `1000 / 3 = 333.33` nieuwe lama's hebben. Omdat we alleen maar hele lama's kunnen hebben, ronden we dit naar beneden af naar `333` lama's.
In datzelfde jaar sterven er `1000 / 4 = 250` lama's, dus we eindigen met `1000 + 333 - 250 = 1083` lama's aan het einde van het jaar. Hier is de populatie dit jaar dus met 83 lama's gegroeid.

Door deze formules herhaaldelijk in te zetten kunnen we berekenen hoeveel jaar het duurt om van een startpopulatie van `n` lama's een eindpopulatie van `m` lama's te bereiken.

## Opdracht

Schrijf, in een bestand genaamd `populatie.py`, een programma dat berekent hoeveel jaar het duurt om van een startpopulatie tot **minstens** een specifieke eindpopulatie te komen.
Zowel de start- als de eindpopulaties moeten als input worden gegeven door de gebruiker.

* Voor dit programma moet je de gebruiker vragen naar de startpopulatie en eindpopulatie:

    * De startpopulatie moet groter of gelijk zijn dan 9 (aangezien de groei anders erg snel stabiliseert). Als de gebruiker een waarde geeft die geen geheel getal is of kleiner dan 9, moet je de gebruiker vragen om een nieuw getal.

    * De eindpopulatie moet groter zijn dan de startgrootte. Opnieuw geldt dat je de gebruiker moet vragen om een geldige input als een ongeldige input wordt gegeven.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def calculate_years(start_size: int, end_size: int) -> int:
        """
        Berekent het aantal jaar dat het duurt voor de populatie om
        end_size te bereiken.
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Hint

Dit programma is een "discrete simulatie". Discreet betekent dat we steeds een stap nemen in de simulatie; in dit geval precies 1 jaar. Je gaat de populatie elk jaar laten groeien (of krimpen) volgens de formules. Zodra de populatie **minstens** zo groot is als de opgegeven eindgrootte ben je klaar en weet je hoeveel jaar het heeft geduurd.

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

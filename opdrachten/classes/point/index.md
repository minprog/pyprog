# Point

Maak een bestand `point.py` met de class `Point` die een punt in het vlak voorstelt.

    if __name__ == '__main__':
        p1 = Point(2, 3)
        p2 = Point(5, -1)
        p3 = p1 + p2
        print(p3)  # Point(7, 2)
    
        print(p1.distance_to(p2))  # afstand tussen p1 en p2

De coördinaten moeten worden opgeslagen als de attributen `x` en `y` (zonder underscore).

Schrijf zelf een doctest voor elke method.

## Mooi printen

In de wiskunde noteren we een punt als `(2, 3)`. Maak een `__str__`-methode die zo'n soort string geeft als we de waarde printen. Die kunnen we dan mooi gebruiken in doctests.

## Optellen van twee objecten

De methode `__add__` is een *special method* die bepaalt wat `+` betekent voor objecten. Definieer deze zo:

    def __add__(self, other: 'Point') -> 'Point':

Binnen deze methode kun je bij de waarden van het andere punt via `other.x` en `other.y`.

## Afstand

`distance_to` berekent de afstand tussen twee punten met hulp van de stelling van Pythagoras (weet je nog, in de eerste week van het vak?). Geef de methode vorm zoals de methode `__add__`.

## Doctests

Vergeet niet om doctests te schrijven voor alle methodes.

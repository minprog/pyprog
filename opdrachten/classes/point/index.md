# Point

Maak een bestand `point.py` met de class `Point` die een punt in het vlak voorstelt.

    if __name__ == '__main__':
        p1 = Point(2, 3)
        p2 = Point(5, -1)
        p3 = p1 + p2
        print(p3)  # Point(7, 2)
    
        print(p1.distance_to(p2))  # afstand tussen p1 en p2

Schrijf zelf een doctest voor elke method.

## Mooi printen



## Optellen van twee objecten

De methode `__add__` is een *special method* die bepaalt wat `+` betekent voor objecten. Definieer deze zo:

    def __add__(self, other: 'Point') -> 'Point':

Binnen deze methode kun je bij de waarden van het andere punt via `other.x` en `other.y`.

`distance_to` berekent de afstand tussen twee punten met de standaardformule. Voeg doctests toe.

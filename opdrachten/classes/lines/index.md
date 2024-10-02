# Lines

Maak een Python-bestand aan genaamd `lines.py`. Voeg de volgende `main`-code toe.

    if __name__ == '__main__':

        segment = LineSegment(Point(1, 1), Point(3, 2))
        print(segment.slope())  # <- 0.5
        print(segment.length()) # <- 2.23606797749979

Implementeer stap voor stap de `LineSegment` en `Point` classes om te zorgen dat de bovenstaande testcode goed werkt.

1.  Schrijf een `Point` class waarvan de `__init__` twee getallen als parameter heeft.

2.  Schrijf een `LineSegment` class waarvan de constructor twee `Point`-instanties als parameter heeft. De eerstgegeven `Point` zal dienen als de start van een lijnsegment.

3.  Schrijf een methode `slope` voor `LineSegment` die de helling van de lijn berekent. De helling is de verandering in `y`-waarde gedeeld door de verandering in `x`-waarde.

4.  Schrijf een methode `length` voor `LineSegment` die de lengte van de lijn berekent. Gebruik de stelling van Pythagoras en gebruik de Python-operator `**` voor machtsverheffen. Doe `** (1/2)` om de wortel te nemen.

Voeg ook doctests toe!

## Hint

- Als je `**` gebruikt om een wortel te nemen dan is het resultaat standaard van type Any (ofwel, Python weet niet wat het type gaat worden). In ons geval komt er altijd een float uit maar dat weet Python niet. Zorg dat je het resultaat van je formule voor `length` altijd converteert naar float voordat je returnt. Dan krijg je geen melding over het verkeerde type.

# Doctests voor classes

In het boek vind je voorbeelden die *bijna* geschikt zijn als doctest. Hieronder iets aangepast als voorbeeld.

Het idee is dat je voor elke doctest een nieuw object maakt, eventueel eigenschappen instelt, en dan een methode aanroept en de uitkomst controleert.

**Test de uitkomst van een methode die iets berekent**

Hier maken we een object aan met een aantal eigenschappen. De methode `area()` is de methode die we uiteindelijk testen.

    >>> rectangle1 = Rectangle()
    >>> rectangle1.width = 85
    >>> rectangle1.height = 87
    >>> rectangle1.x = 245
    >>> rectangle1.y = 199
    >>> rectangle1.area()
    7395

**Test de uitkomst van een Queue class**

Hier maken we een Queue aan, we stoppen er twee getallen in. Dan halen we er één uit en checken of het het juiste getal is. En tot slot checken we of dat getal ook echt is *verwijderd* uit de queue.

    >>> q = Queue()
    >>> q.enqueue(3)
    >>> q.enqueue(1)
    >>> q.dequeue()
    3
    >>> q.size()
    1

Dit zijn dus twee tests in één.

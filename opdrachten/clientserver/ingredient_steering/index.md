# Steering

Misschien is het leuker om een unit een richting te geven waarin het
beweegt zodat je kan sturen in plaats van alleen naar
links/recht/boven/onder te bewegen. Kijk dan naar de
[steering.py](steering.py) voorbeeldcode.

![steering.gif](steering.gif)

# Polar to Cartesian

In deze code wordt de
[pygame.Vector2.from_polar](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.from_polar)
method gebruikt voor het omzetten van een polar coordinaat naar een
cartesian coordinaat zoals uitgelegd in [Math is Fun, Polar and
Cartesian
Coordinates](https://www.mathsisfun.com/polar-cartesian-coordinates.html) wat je waarschijnlijk eerder met wiskunde op de middelbare school gehad
hebt. Maar, omdat deze wiskunde is ingebouwd (encapsulated) in de
`pygame.Vector2` class kunnen we het gebruiken zonder over de details
na te hoeven denken (abstraction) wat het programmeren een stuk
makkelijker en de code een stuk leesbaarder maakt.

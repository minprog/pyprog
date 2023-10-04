# Steering

Misschien is het leuker om een unit een richting te geven waarin het
begeegt zodat je kan sturen in plaats van alleen naar
links/recht/boven/onder bewegen. Kijk dan naar de [main.py](main.py)
voorbeeldcode.

![steering.gif](steering.gif)


# Polar to Cartesian

In deze code wordt de
[pygame.Vector2.from_polar](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.from_polar)
method gebruikt voor het omzetten van een polar coordinaat naar
een cartesian coordinate zoals uitgelegd in [Math is Fun, Polar and Cartesian
Coordinates](https://www.mathsisfun.com/polar-cartesian-coordinates.html). Maar,
omdat deze wiskunde is ingebouwd (encapsulation) in de
`pygame.Vector2` class kunnen we het gebruiken zonder over de details
na te hoeven denken (abstraction) wat het programmeren een stuk
makkelijker en de code een stuk leesbaarder maakt.

# Different Aliens

Het spel heeft meer soorten Aliens nodig. In bestand
[Alien_Seeker.py](Alien_Seeker.py) is een Alien_Seeker class
gedefinieerd welke inherit van `Alien`. De radius van dit Alien type
is 12, en de kleur is (255,255,0):

```python
import pygame

from Alien import Alien

class Alien_Seeker(Alien):

    def __init__(self, size, player):
        """ Initializes an Alien_Seeker at a random position within 'size' and
        random speed between (-3,-3) and (+3,+3). This alien seeks the 'player' unit
        """
        super().__init__(size)
        self.radius = 12
        self.color = (255, 255, 0)  # red+green color
        self.player = player

    def step(self, size):
        """ Changes 'speed' to move to 'player' and changes the 'position'
        based on its 'speed'.
        """
        super().step(size)  # call 'step()' method of parent
        difference = self.player.position - self.position  # difference between 'player' and 'self'
        difference.normalize_ip()  # scale difference to length 1
        self.speed += difference * 0.05  # change speed a bit in direction of 'player'

    def draw(self, surface):
        super().draw(surface)  # call 'draw()' method of parent
        size = pygame.Vector2(self.radius * 1.2, self.radius * 1.2)
        rect = pygame.Rect(self.position - size / 2, size)
        black = (0, 0, 0)
        pygame.draw.rect(surface, black, rect, 3)  # draw a rectangle on top
```

Objecten van class `Alien_Seeker` krijgen in `__init__()` een
'instance variable' `player` waar dit type alien tot aangetrokken
wordt. Dit aantrekken wordt gedaan door in `step()` methode de `speed`
steeds een beetje aan te passen zodat het naar de `player` toe
beweegt. In de `draw()` methode wordt tot slot nog een rechthoekje
getekend om een groter visueel verschil te maken.

Bestand [main.py](main.py) is aangepast zodat nu ook objecten van type
Alien_Seeker gespawned worden met een kans van 0.003.

## Opdracht: Alien_Bouncer

Voeg zelf nog een `Alien_Bouncer` class toe. Een `Alien_Bouncer` wordt
niet aangetrokken tot de speler maar tot de grond (hint: `self.speed.y
+= 0.05`). Het heeft een `(0,255,255)` kleur, een `radius` van 14 en
plus-teken in plaats van een rechthoekje. Pas ook bestand
[main.py](main.py) aan zodat objecten van type Alien_Bouncer gespawned
worden met een kans van 0.003.

![Alien_Bouncer.png](Alien_Bouncer.png)

![bouncer.gif](bouncer.gif)

import pygame
import random

import Unit

class Alien(Unit.Unit):

    def __init__(self,surface):
        super().__init__(surface)
        width, height = surface.get_size()
        px = random.random()*width
        py = random.random()*height
        self.position = pygame.Vector2(px,py)
        speed = 4
        sx = random.random()*2*speed - speed
        sy = random.random()*2*speed - speed
        self.speed = pygame.Vector2(sx,sy)
        self.radius = 10
        self.color = (0,255,0)

    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

import pygame
import random

from Unit import Unit

class Alien(Unit):
    spawn_chance=0.01
    remaining=10
    
    def __init__(self,surface):
        super().__init__()
        self.set_random_position(surface)
        self.set_random_speed(4)
        self.radius = 10
        self.color = (0,255,0)
        Alien.remaining-=1

    def __del__(self):
        Alien.remaining+=1
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

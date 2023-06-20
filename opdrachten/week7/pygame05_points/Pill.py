import pygame
import random

from Unit import Unit

class Pill(Unit):
    spawn_chance=0.05
    remaining=1
    
    def __init__(self,surface):
        super().__init__(surface)
        self.set_random_position(surface)
        self.set_random_speed(2)
        self.radius = 15
        self.color = (0,0,255)
        Pill.remaining-=1

    def __del__(self):
        Pill.remaining+=1
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

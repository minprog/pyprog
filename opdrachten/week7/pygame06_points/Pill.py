import pygame
import random

from Static_Unit import Static_Unit

class Pill(Static_Unit):
    spawn_chance=0.05
    remaining=1
    
    def __init__(self,surface):
        super().__init__()
        self.set_random_position(surface)
        self.radius = 15
        self.color = (0,0,255)
        Pill.remaining-=1

    def __del__(self):
        Pill.remaining+=1
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

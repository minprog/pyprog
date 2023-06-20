import pygame
import random

from Unit import Unit

class Points(Unit):
    spawn_chance=0.02
    remaining=5
    
    def __init__(self,surface):
        super().__init__()
        self.set_random_position(surface)
        self.set_random_speed(3)
        self.radius = 5
        self.color = (255,0,0)
        Points.remaining-=1

    def __del__(self):
        Points.remaining+=1
        super().__del__()
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

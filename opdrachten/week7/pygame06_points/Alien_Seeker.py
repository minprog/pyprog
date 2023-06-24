import pygame
import random

from Alien import Alien

class Alien_Seeker(Alien):
    spawn_chance=0.005
    remaining=2
    
    def __init__(self,surface,unit):
        super().__init__(surface)
        self.set_random_position(surface)
        self.set_random_speed(4)
        self.radius = 10
        self.color = (0,255,0)
        self.seek_unit=unit
        Alien_Seeker.remaining-=1

    def __del__(self):
        Alien_Seeker.remaining+=1
        super().__del__()
        
    def step(self,surface):
        diff = self.seek_unit.position - self.position
        diff.normalize_ip()
        self.speed += diff*0.05
        super().step(surface)
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

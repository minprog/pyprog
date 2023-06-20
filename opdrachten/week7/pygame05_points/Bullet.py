import pygame
import random

from Unit import Unit

class Bullet(Unit):
    
    def __init__(self,position,speed):
        super().__init__()
        self.position = position
        self.speed = speed
        self.radius = 3
        self.color = (255,255,255)

    def stay_on_screen(self,surface):
        if super().stay_on_screen(surface):
            self.set_alive(False)
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

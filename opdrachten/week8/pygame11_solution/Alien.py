import pygame
import random

from Unit import Unit

class Alien(Unit):

    def __init__(self, size):
        """ Initializes an Alien at a random position within 'size' and
            random speed between (-3,-3) and (+3,+3).
        """
        width, height = size
        position = pygame.Vector2(random.random()*width,
                                  random.random()*height)
        speed = 3
        speed = pygame.Vector2(random.random()*speed*2-speed,
                               random.random()*speed*2-speed)
        super().__init__(position, speed, radius=10, line_width=0, color=(0, 255 ,0))

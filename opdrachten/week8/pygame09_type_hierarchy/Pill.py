import pygame
import random

from Unit import Unit

class Pill(Unit):
    count = 0
    
    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(random.random() * width,
                                  random.random() * height)
        speed = pygame.Vector2(0, 0)
        super().__init__(position, speed, radius=20, line_width=0, color=(255, 0, 0))
        Pill.count += 1

    def __del__(self):
        Pill.count -= 1

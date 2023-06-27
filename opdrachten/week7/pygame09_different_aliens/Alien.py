import pygame
import random

from Unit import Unit

class Alien(Unit):
    remaining = 10      # number of Aliens that remain to be added to game
    spawn_chance = 0.01 # chance that we add an Alien in each time step
    radius = 10
    line_width = 0
    color = (0,255,0)

    def __init__(self, size, r=1):
        """ Initializes an Alien at a random position within 'size' and
            random speed between (-3,-3) and (+3,+3).
        """
        width, height = size
        speed = 3
        super().__init__( pygame.Vector2(random.random()*width, random.random()*height),
                          pygame.Vector2(random.random()*speed*2-speed, random.random()*speed*2-speed))
        Alien.remaining -= r
        
    def __del__(self, r=1):
        Alien.remaining += r

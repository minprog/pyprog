import pygame
import random

from Unit import Unit

class Pill(Unit):
    remaining = 1
    spawn_chance = 0.002 # chance that we add an Alien_Bouncer in each time step
    radius = 20
    line_width = 0
    color = (255,0,0)
    
    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        super().__init__( pygame.Vector2(random.random()*width, random.random()*height),
                          pygame.Vector2(0,0) )
        Pill.remaining -= 1

    def __del__(self):
        """ Increases 'remaining' when an objects gets deleted. """
        Pill.remaining += 1


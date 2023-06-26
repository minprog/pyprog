import pygame
import random

from Alien import Alien

class Alien_Seeker(Alien):
    remaining = 2
    spawn_chance = 0.005 # chance that we add an Alien in each time step
    radius = 12
    line_width = 0
    color = (255,255,0) # red+green color
    
    def __init__(self, size, seek_unit):
        """ Initializes an Alien at a random position within 'size' and
        random speed between (-3,-3) and (+3,+3).
        """
        super().__init__(size)
        Alien_Seeker.remaining -= 1
        self.seek_unit = seek_unit

    def __del__(self):
        """ Increases 'remaining' when an objects gets deleted. """
        Alien_Seeker.remaining += 1

    def step(self, size):
        """ Changes 'speed' to move to 'seek_unit' and changes the 'position' 
        based on its 'speed'.
        """
        super().step(size) # call 'step()' method of parent
        difference = self.seek_unit.position - self.position # difference between 'seek_unit' and 'self'
        difference.normalize_ip() # scale difference to length 1
        self.speed += difference*0.05 # change speed a bit in direction of 'unit'


    def draw(self, surface):
        super().draw(surface) # call 'draw()' method of parent
        size = pygame.Vector2(Alien_Seeker.radius*1.2, Alien_Seeker.radius*1.2)
        rect = pygame.Rect(self.position-size/2, size)
        black = (0,0,0)
        pygame.draw.rect(surface, black, rect, 3) # draw a rectangle on top

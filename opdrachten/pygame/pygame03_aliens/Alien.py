import pygame

class Alien:

    def __init__(self, size):
        """ Initializes an Alien at a random position within 'size' and
            random speed between (-3,-3) and (+3,+3).
        """

    def step(self, size):
        """ Changes the position of the Alien based on its speed. """
        
    def stay_on_window(self, size):
        """ Makes sure the Alien stays on the window with 'size'. """

    def draw(self, surface):
        """ Draws the Alien on the 'surface'. """

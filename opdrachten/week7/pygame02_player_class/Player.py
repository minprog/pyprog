import pygame

class Player:

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
    
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard keys pressed. 
        Limits the speed by multipling by '0.95'.
        """
        
    def step(self, size):
        """ Change the position of player basedo on its speed. """
        
    def stay_in_window(self, size):
        """ Make sure the players stays on in the window with 'size'. """

    def draw(self, surface):
        """ Draws the player """

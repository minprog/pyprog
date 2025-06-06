import pygame

class Player:

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
    
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard 'keys' pressed. 
        Limits the speed by multipling it by '0.95'.
        """
        
    def step(self, size):
        """ Changes the position of player based on its speed. """
        
    def stay_on_window(self, size):
        """ Makes sure the players stays on the window with 'size'. """

    def draw(self, surface):
        """ Draws the player on the 'surface'. """

import pygame

from Alien import Alien

class Alien_Seeker(Alien):
    
    def __init__(self, size, player):
        """ Initializes an Alien_Seeker at a random position within 'size' and
        random speed between (-3,-3) and (+3,+3). This alien seeks the 'player' unit
        """
        super().__init__(size)
        self.radius = 12
        self.color = (255,255,0) # red+green color
        self.player = player
        
    def step(self, size):
        """ Changes 'speed' to move to 'player' and changes the 'position' 
        based on its 'speed'.
        """
        super().step(size) # call 'step()' method of parent
        difference = self.player.position - self.position # difference between 'player' and 'self'
        difference.normalize_ip() # scale difference to length 1
        self.speed += difference * 0.05 # change speed a bit in direction of 'player'

    def draw(self, surface):
        super().draw(surface) # call 'draw()' method of parent
        size = pygame.Vector2(self.radius * 1.2, self.radius * 1.2)
        rect = pygame.Rect(self.position-size / 2, size)
        black = (0,0,0)
        pygame.draw.rect(surface, black, rect, 3) # draw a rectangle on top

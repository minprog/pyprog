import pygame

from Alien import Alien

class Alien_Bouncer(Alien):
    
    def __init__(self, size):
        """ Initializes an Alien_Seeker at a random position within 'size' and
        random speed between (-3,-3) and (+3,+3). This alien seeks the 'player' unit
        """
        super().__init__(size)
        self.radius = 14
        self.color = (0,255,255) # green+blue color
        
    def step(self, size):
        """ Changes 'speed' to move to 'player' and changes the 'position' 
        based on its 'speed'.
        """
        super().step(size) # call 'step()' method of parent
        self.speed.y += 0.05

    def draw(self, surface):
        super().draw(surface) # call 'draw()' method of parent
        black = (0,0,0)
        down = pygame.Vector2(self.radius*0.7, 0)
        right = pygame.Vector2(0, self.radius*0.7)
        pygame.draw.line(surface, black, self.position + down, self.position - down, 3) # draw a line on top
        pygame.draw.line(surface, black, self.position + right, self.position - right, 3) # draw a line on top

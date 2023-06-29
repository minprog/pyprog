import pygame

from Alien import Alien

class Alien_Bouncer(Alien):
    remaining = 3
    spawn_chance = 0.008 # chance that we add an Alien_Bouncer in each time step
    radius = 14
    line_width = 0
    color = (0,255,255) # green+blue color
    
    def __init__(self, size):
        """ Initializes an Alien at a random position within 'size' and
        random speed between (-3,-3) and (+3,+3).
        """
        super().__init__(size)
        Alien_Bouncer.remaining -= 1
        
    def __del__(self):
        """ Increases 'remaining' when an objects gets deleted. """
        Alien_Bouncer.remaining += 1
        super().__del__()
        
    def step(self, size):
        """ Changes 'speed' to move to 'seek_unit' and changes the 'position' 
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

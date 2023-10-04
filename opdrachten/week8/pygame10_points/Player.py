import pygame
import time

from Unit import Unit

class Player(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(width//2,height//2)
        speed = pygame.Vector2(0,0)
        super().__init__(position, speed, radius=20, line_width=4, color=(255, 255 ,255))
        self.total_points = 0
        
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard 'keys' pressed. 
        Limits the speed by multipling it by '0.95'.
        """
        acceleration = 0.5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed.x -= acceleration
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed.x += acceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed.y -= acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed.y += acceleration
        self.speed *= 0.95

    def add_points(self,points):
        """ Adds 'points' to the 'total_points'. """
        self.total_points += points
        self.total_points = max(self.total_points, 0) # total_points remains non-negative

    def get_total_points(self):
        """ Returns the 'total_points'. """
        return self.total_points
    
    def draw(self, surface):
        """ Draws the player on the 'surface' and a bar with the 'total_points'. """
        super().draw(surface)
        # draw total_point in red using a bar
        border = 2
        offset = 8
        bar_width = 12
        rect = pygame.Rect(offset, offset, border+self.get_total_points()*8, bar_width)
        red = (255,0,0)
        pygame.draw.rect(surface, red, rect)
        rect = pygame.Rect(offset, offset, border*2+400, bar_width)
        white = (255,255,255)
        pygame.draw.rect(surface, white, rect, border)

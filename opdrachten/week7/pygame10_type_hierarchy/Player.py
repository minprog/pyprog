import pygame
import time

from Unit import Unit

class Player(Unit):
    radius = 20
    line_width = 4
    color = (255,255,255)

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        super().__init__( pygame.Vector2(width//2,height//2),
                          pygame.Vector2(0,0) )
        self.pill_time = 0
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

    def eat_pill(self):
        self.pill_time = time.time() # record time we eat the pill

    def has_pill(self):
        time_since_eat_pill = time.time() - self.pill_time
        return time_since_eat_pill < 7

    def add_points(self,points):
        self.total_points += points
        self.total_points = max(self.total_points, 0)

    def get_total_points(self):
        return self.total_points
    
    def draw(self, surface):
        """ Draws the player on the 'surface'. """
        c = self.color
        r = self.radius
        lw = self.line_width
        if self.has_pill():
            c = (255,0,0)
            r = 24
            lw = 8
        pygame.draw.circle(surface, c, self.position, r, lw)
        border = 2
        offset = 8
        rect = pygame.Rect(offset, offset, border+self.get_total_points()*4, 10)
        red = (255,0,0)
        pygame.draw.rect(surface, red, rect)
        rect = pygame.Rect(offset, offset, border*2+400, 10)
        white = (255,255,255)
        pygame.draw.rect(surface, white, rect, border)

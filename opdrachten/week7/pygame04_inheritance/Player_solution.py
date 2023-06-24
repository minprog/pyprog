import pygame

from Unit import Unit

class Player(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(width//2,height//2)
        speed = pygame.Vector2(0,0)
        super().__init__(position, speed)
    
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

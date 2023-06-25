import pygame

class Player:

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        self.position = pygame.Vector2(width//2,height//2)
        self.speed = pygame.Vector2(0,0)
        self.radius = 20
        self.line_width = 4
        self.color = (255,255,255)
    
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

    def step(self, size):
        """ Changes the position of player based on its speed. """
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Draws the player on the 'surface'. """
        width, height = size
        if self.position.x<self.radius:
            self.position.x = self.radius
            self.speed.x =- self.speed.x
        if self.position.y<self.radius:
            self.position.y=self.radius
            self.speed.y =- self.speed.y
        if self.position.x>width-self.radius:
            self.position.x = width-self.radius
            self.speed.x =- self.speed.x
        if self.position.y>height-self.radius:
            self.position.y=height-self.radius
            self.speed.y =- self.speed.y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)
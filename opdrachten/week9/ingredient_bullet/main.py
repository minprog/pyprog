import pygame
import time

class Unit:

    def __init__(self, position, speed, radius=20, line_width=4, color=(255,255,255)):
        """ Initializes a Unit. """
        self.position = position
        self.speed = speed
        self.radius = radius
        self.line_width = line_width
        self.color = color

    def step(self, size):
        """ Changes the position of Unit based on its speed. """
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Makes sure the Unit stays on the window with 'size'. """
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
        """ Draws the Unit on the 'surface'. """
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

class Bullet(Unit):

    def __init__(self, position):
        """ Initializes a player in the middle of 'size'. """
        speed = pygame.Vector2(8,0)
        super().__init__(position, speed, radius=6, line_width=3, color=(255,0,0))
        
class Player(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(width//2,height//2)
        speed = pygame.Vector2(0,0)
        super().__init__(position, speed)
        self.last_shoot_time = 0
    
    def move(self, keys, units):
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
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]: # shoot with SPACE or RETURN key
            self.shoot(units)
        self.speed *= 0.95

    def shoot(self, units):
        now = time.time()
        if now - self.last_shoot_time > 0.05: # wait some time between bullets
            units.append( Bullet(self.position + pygame.Vector2(self.radius,0)) ) # append new bullet unit
            self.last_shoot_time = now # record last time bullet was shot
        
def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('bullets')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())

    units = []
    units.append(player)

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys, units)

        for unit in units:
            unit.step(surface.get_size())
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

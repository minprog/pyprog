import pygame
import random

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

    def draw(self, surface, center_world, center_window):
        """ Draws the Unit on the 'surface'. """
        pos = self.position - center_world + center_window
        pygame.draw.circle(surface, self.color, pos, self.radius, self.line_width)

class Ball(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(random.random()*width, random.random()*height)
        speed = pygame.Vector2(0,0)
        gray = (100,100,100)
        super().__init__(position, speed, radius=10, line_width=2, color=gray)
        
class Player(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(width//2,height//2)
        speed = pygame.Vector2(0,0)
        super().__init__(position, speed)
    
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
        self.speed *= 0.95

    def get_position(self):
        return self.position
        
def draw_border(surface, world_size, center_world, center_window):
    pos = -center_world + center_window
    width, height = world_size
    rect = pygame.Rect(pos.x, pos.y, width, height)
    white = (255, 255, 255)
    pygame.draw.rect(surface, white, rect, 4)
    
def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('bullets')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    world_size = pygame.Vector2( surface.get_size() ) * 1.5
    player = Player(world_size)
    
    units = []
    units.append(player)

    for i in range(40):
        units.append(Ball(world_size))

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys, units)
        center_world = player.get_position() 
        center_window = pygame.Vector2(surface.get_size()) / 2
        
        for unit in units:
            unit.step(world_size)
            unit.draw(surface, center_world, center_window)
        draw_border(surface, world_size, center_world, center_window)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

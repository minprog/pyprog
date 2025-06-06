import pygame
import math

class Player:

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        self.position = pygame.Vector2(width//2,height//2)
        self.speed = pygame.Vector2(0,0)
        self.radius = 20
        self.line_width = 4
        self.color = (255,255,255)
        self.angle = 0
    
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard 'keys' pressed. 
        Limits the speed by multipling it by '0.95'.
        """
        acceleration = 0.5
        rotation = 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= rotation  # turn left
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += rotation  # turn right
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed += pygame.Vector2.from_polar((acceleration, self.angle)) # forwards in 'angle' direction
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed -= pygame.Vector2.from_polar((acceleration, self.angle)) # backwards in 'angle' direction 
        self.speed *= 0.97

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
        p1 = self.position
        p2 = p1 + pygame.Vector2.from_polar((self.radius*3/2, self.angle))
        pygame.draw.line(surface, self.color, p1, p2, self.line_width)
        
def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('steering')
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
        player.move(keys)

        for unit in units:
            unit.step(surface.get_size())
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

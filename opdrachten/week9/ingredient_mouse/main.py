import pygame
import math

class Ball:

    def __init__(self, position):
        """ Initializes a ball in the middle of 'size'. """
        self.position = position
        self.speed = pygame.Vector2(0,3)
        self.radius = 20
        self.line_width = 4
        self.color = (255,255,255)

    def step(self, size):
        """ Changes the position of ball based on its speed. """
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Draws the ball on the 'surface'. """
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

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('balls')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()

    units = []
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # for more info on mouse events see: https://www.pygame.org/docs/ref/mouse.html
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("MOUSEBUTTONDOWN: ",pos)
                units.append( Ball(pygame.Vector2(pos)) )
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                # print("MOUSEMOTION: ",pos)
                
        for unit in units:
            unit.step(surface.get_size())
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

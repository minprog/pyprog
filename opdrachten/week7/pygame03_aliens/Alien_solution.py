import pygame
import random

class Alien:

    def __init__(self, size):
        """ Initializes an Alien at a random position within 'size' and
            random speed between (-3,-3) and (+3,+3).
        """
        width, height = size
        self.position = pygame.Vector2(random.random()*width,
                                       random.random()*height)
        speed = 3
        self.speed = pygame.Vector2(random.random()*speed*2-speed,
                                    random.random()*speed*2-speed)
        self.radius = 10
        self.line_width = 0
        self.color = (0, 255 ,0)

    def step(self, size):
        """ Changes the position of the Alien based on its speed. """
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Makes sure the Alien stays on the window with 'size'. """
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
        """ Draws the Alien on the 'surface'. """
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

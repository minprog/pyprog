import pygame
import random

class Alien:

    def __init__(self,surface):
        width, height = surface.get_size()
        self.position = pygame.Vector2(width//2,height//2)
        speed=4
        sx = random.random()*2*speed - speed
        sy = random.random()*2*speed - speed
        self.speed = pygame.Vector2(sx,sy)
        self.radius = 10
        self.color = (0,255,0)

    def step(self):
        self.position += self.speed

    def stay_on_screen(self,surface):
        width, height = surface.get_size()
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

    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

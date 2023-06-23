import pygame
import random

from Static_Unit import Static_Unit

class Unit(Static_Unit):

    def __init__(self):
        super().__init__()
        self.speed = pygame.Vector2(0,0)

    def set_random_speed(self,speed):
        sx = random.random()*2*speed - speed
        sy = random.random()*2*speed - speed
        self.speed = pygame.Vector2(sx,sy)

    def step(self,surface):
        self.position += self.speed
        self.stay_on_screen(surface)

    def stay_on_screen(self,surface):
        hit_wall = False
        width, height = surface.get_size()
        if self.position.x<self.radius:
            self.position.x = self.radius
            self.speed.x =- self.speed.x
            hit_wall=True
        if self.position.y<self.radius:
            self.position.y=self.radius
            self.speed.y =- self.speed.y
            hit_wall=True
        if self.position.x>width-self.radius:
            self.position.x = width-self.radius
            self.speed.x =- self.speed.x
            hit_wall=True
        if self.position.y>height-self.radius:
            self.position.y=height-self.radius
            self.speed.y =- self.speed.y
            hit_wall=True
        return hit_wall

import pygame
import random

class Unit:

    def __init__(self):
        self.position = pygame.Vector2(0,0)
        self.speed = pygame.Vector2(0,0)
        self.radius = 20
        self.color = (255,255,255)
        self.line_width = 4
        self.set_alive(True)

    def __dell__(self):
        pass
        
    def set_random_position(self,surface):
        width, height = surface.get_size()
        px = random.random()*width
        py = random.random()*height
        self.position = pygame.Vector2(px,py)

    def set_random_speed(self,speed):
        sx = random.random()*2*speed - speed
        sy = random.random()*2*speed - speed
        self.speed = pygame.Vector2(sx,sy)
        
    def set_alive(self,alive: bool):
        self.alive=alive
        
    def is_alive(self):
        return self.alive
        
    def step(self):
        self.position += self.speed

    def stay_on_screen(self,surface):
        hit_wall=False
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
            
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

    def has_collision(self,other):
        position_difference = self.position - other.position
        return position_difference.length() < self.radius + other.radius

        
        

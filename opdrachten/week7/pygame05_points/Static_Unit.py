import pygame
import random

class Static_Unit:

    def __init__(self):
        self.position = pygame.Vector2(0,0)
        self.radius = 20
        self.color = (255,255,255)
        self.line_width = 4
        self.set_alive(True)

    def __dell__(self):
        pass

    def step(self,surface):
        pass
    
    def set_random_position(self,surface):
        width, height = surface.get_size()
        px = random.random()*width
        py = random.random()*height
        self.position = pygame.Vector2(px,py)

    def set_alive(self,alive: bool):
        self.alive=alive
        
    def is_alive(self):
        return self.alive
            
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

    def has_collision(self,other):
        position_difference = self.position - other.position
        return position_difference.length() < self.radius + other.radius

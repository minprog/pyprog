import pygame

class Unit:

    def __init__(self,surface):
        width, height = surface.get_size()
        self.position = pygame.Vector2(width//2,height//2)
        self.speed = pygame.Vector2(0,0)
        self.radius = 20
        self.color = (255,255,255)
        self.line_width = 4
        self.alive=True

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
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

    def has_collision(self,other):
        position_difference = self.position - other.position
        return position_difference.length() < self.radius + other.radius

        
        

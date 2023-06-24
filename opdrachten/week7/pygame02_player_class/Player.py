import pygame

class Player:

    def __init__(self,surface):
        width, height = surface.get_size()
        self.position = pygame.Vector2(width//2,height//2)
        self.speed = pygame.Vector2(0,0)
        self.radius =20
        self.line_width = 4
        self.color = (255,255,255)
    
    def keyboard(self):
        accel=0.8
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed.x -= accel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed.x += accel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed.y -= accel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed.y += accel
        self.speed.y += 0.5
        self.speed *= 0.99

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

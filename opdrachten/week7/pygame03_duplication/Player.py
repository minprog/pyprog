import pygame

import Unit

class Player(Unit.Unit):
    
    def __init__(self,surface):
        super().__init__(surface)
    
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

    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

import pygame
import time

import Unit

class Player(Unit.Unit):
    
    def __init__(self,surface):
        super().__init__(surface)
        self.pill_time=0
        
    def keyboard(self):
        accel=0.5
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed.x -= accel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed.x += accel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed.y -= accel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed.y += accel
        self.speed *= 0.99

    def set_pill(self):
        self.pill_time=time.time()

    def is_pill_active(self):
        return time.time() - self.pill_time < 8

    def is_pill_ending(self):
        return time.time() - self.pill_time > 5
        
    def draw(self,surface):
        color=self.color
        if self.is_pill_active():
            color=(255,0,0)
            if self.is_pill_ending():
                color=(155,0,0)
        pygame.draw.circle(surface, color, self.position, self.radius, self.line_width)

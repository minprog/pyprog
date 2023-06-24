import pygame
import time

from Unit import Unit
from Bullet import Bullet

class Player(Unit):
    
    def __init__(self,surface):
        super().__init__()
        width, height = surface.get_size()
        self.position = pygame.Vector2(width//2,height//2)
        self.pill_time=0
        self.bullet_time=0
        self.total_points = 0
        
    def keyboard(self,units):
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
        if keys[pygame.K_SPACE ] and time.time()-self.bullet_time > 0.2:
            self.bullet_time = time.time()
            bullet_speed=self.speed*2
            if bullet_speed.length()>10:
                bullet_speed=bullet_speed.normalize()*10
            units.append( Bullet(self.position.copy(),
                                 bullet_speed) )
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
        border = 2
        offset = 8
        rect = pygame.Rect(offset, offset, border+self.total_points*4, 10)
        red = (255,0,0)
        pygame.draw.rect(surface, red, rect)
        rect = pygame.Rect(offset, offset, border*2+400, 10)
        white = (255,255,255)
        pygame.draw.rect(surface, white, rect, border)

    def add_points(self,points):
        self.total_points += points
        print("total_points:",self.total_points)

    def get_total_points(self):
        return self.total_points

import pygame

class Player:
    radius = 20
    line_width = 4
    color = (255,255,255)
        
    def __init__(self,world_size):
        self.position = pygame.Vector2(world_size.x//2, world_size.y//2)
        self.speed = pygame.Vector2(0,0)
        self.line_width = 4
        self.color = (255,255,255)

    def __repr__(self):
        return f"position: {self.position} speed: {self.speed}"

    def get_position(self):
        return self.position
    
    def accelerate(self,acceleration):
        self.speed += acceleration
        self.speed *= 0.99
        
    def step(self):
        self.position += self.speed

    def stay_on_screen(self,world_size):
        if self.position.x<Player.radius:
            self.position.x = Player.radius
            self.speed.x =- self.speed.x
        if self.position.y<Player.radius:
            self.position.y=Player.radius
            self.speed.y =- self.speed.y
        if self.position.x > world_size.x - Player.radius:
            self.position.x = world_size.x -Player.radius
            self.speed.x =- self.speed.x
        if self.position.y > world_size.y - Player.radius:
            self.position.y = world_size.y -Player.radius
            self.speed.y =- self.speed.y

    def draw(self, surface, name_texture):
        pygame.draw.circle(surface, Player.color, self.position, Player.radius, Player.line_width)
        text_offset = pygame.Vector2( name_texture.get_size() )
        text_offset.x /= 2
        text_offset.y += Player.radius
        surface.blit(name_texture, self.position - text_offset )

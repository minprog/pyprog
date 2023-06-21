import pygame

from Player import Player

class Game_State:

    def __init__(self, world_size):
        self.world_size = world_size
        self.units = {}
        
    def __repr__(self):
        return f"world_size: {self.world_size}\nunits: {self.units}"

    def update(self, action):
        name = action.get_name()
        if not name in self.units:
            self.units[name]=Player(self.world_size)
        player = self.units[name]
        player.accelerate(action.get_acceleration())
        player.step()
        player.stay_on_screen(self.world_size)

    def draw(self, name, surface, name_textures):   
        rect = pygame.Rect(pygame.Vector2(0,0), self.world_size)
        white = (255,255,255)
        pygame.draw.rect(surface, white, rect, 2)
        for name, unit in self.units.items():
            name_texture = name_textures.get_texture(name)
            unit.draw(surface,name_texture)

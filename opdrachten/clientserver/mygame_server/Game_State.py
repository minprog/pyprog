import pygame

from Player import Player

class Game_State:

    def __init__(self, world_size):
        self.world_size = world_size
        self.players = {}
        self.units = []

    def __repr__(self):
        return f"world_size: {self.world_size}\nunits: {self.units}"

    def update(self, action):
        name = action.get_name()
        if not name in self.players: # if the name is not seen before
            player = Player(self.world_size, name) # create a new player
            self.units.append(player)              # add to units
            self.players[name] = player            # add to players too for fast lookup by name 
        player = self.players[name]
        player.accelerate(action.get_acceleration())
        player.step()
        player.stay_on_screen(self.world_size)

    def spawn_units(self):
        pass
        
    def draw(self, name, surface, name_textures):
        rect = pygame.Rect(pygame.Vector2(0, 0), self.world_size)
        white = (255, 255, 255)
        pygame.draw.rect(surface, white, rect, 2)
        for unit in self.units:
            unit.draw(surface, name_textures)

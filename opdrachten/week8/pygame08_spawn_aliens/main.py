import pygame
import random

from Player import Player
from Alien import Alien

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('interaction')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())  

    units = []
    units.append(player)
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        spawn_aliens(units, surface.get_size()) # spawn aliens in the units list
        
        for unit in units:
            unit.step(surface.get_size())
            for other in units:
                if unit.has_collision(other):
                    handle_collision(unit, other)
            unit.draw(surface)
            
        pygame.display.flip()
        clock.tick(60)

def handle_collision(unit, other):
    """ Handles the collision of 'unit' and 'other' by swapping their speed. """ 
    unit.swap_speed(other)

def spawn_aliens(units, size):
    """ Spawns Alies in 'units' list based on its 'spawn_chance' and 'remaining' count. """
    if Alien.remaining > 0 and random.random() < Alien.spawn_chance: # Alien spawn condition
        units.append( Alien(size) ) # spawn Alien
    
if __name__ == "__main__":
    main()

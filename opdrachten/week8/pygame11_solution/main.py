import pygame
import random

from Player import Player
from Alien import Alien
from Alien_Seeker import Alien_Seeker
from Alien_Bouncer import Alien_Bouncer

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

    #units.append(Alien(surface.get_size()))
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        spawn_aliens(units, surface.get_size(), player)
        
        for unit in units:
            unit.step(surface.get_size())
            for other in units:
                if unit.has_collision(other):
                    handle_collision(unit, other)
            unit.draw(surface)

        units = [unit for unit in units if unit.is_alive()]  # only keep alive units for the next time step
        
        for unit in units:
            if isinstance(unit, Alien) and unit.get_age() > 10:
                unit.set_alive(False)        
        
        pygame.display.flip()
        clock.tick(60)

def handle_collision(unit, other):
    """ Handles the collision of 'unit' stepping into 'other'. 
    """
    unit.swap_speed(other)
    unit.step_back()
    
    # When Player hits an Alien_Bouncer it gets 1 point and the Alien_Bouncer dies
    if (type(unit) is Player and type(other) is Alien_Bouncer):
        unit.add_points(1)
        other.set_alive(False)
    elif (type(unit) is Alien_Bouncer and type(other) is Player): # reverse
        other.add_points(1)
        unit.set_alive(False)

    # When Player hits any other alien type it looses 2 points and the alien dies
    elif (type(unit) is Player and isinstance(other, Alien)):
        unit.add_points(-2)
        other.set_alive(False)
    elif (isinstance(unit, Alien) and type(other) is Player): # reverse
        other.add_points(-2)
        unit.set_alive(False)
        
    # When Alien_Seeker hits an Alien the Alien dies
    elif (type(unit) is Alien and type(other) is Alien_Seeker):
        unit.set_alive(False)
    elif (type(unit) is Alien_Seeker and type(other) is Alien): # reverse
        other.set_alive(False)
    
    
def spawn_aliens(units, size, player):
    """ Spawns Alies in 'units' list based on its 'spawn_chance'. """
    max_nr_units = 15
    alien_spawn_chance = 0.01
    alien_seeker_spawn_chance = 0.006
    alien_bouncer_spawn_chance = 0.006
    if len(units) < max_nr_units:
        if random.random() < alien_spawn_chance:
            units.append( Alien(size) )
        if random.random() < alien_seeker_spawn_chance:
            units.append( Alien_Seeker(size, player) )
        if random.random() < alien_bouncer_spawn_chance:
            units.append( Alien_Bouncer(size) )
            
if __name__ == "__main__":
    main()

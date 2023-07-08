import pygame
import random

from Unit import Unit
from Player import Player
from Alien import Alien
from Alien_Seeker import Alien_Seeker
from Alien_Bouncer import Alien_Bouncer
from Pill import Pill

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('points')
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

        spawn_aliens(units, surface.get_size(), player)
        
        for unit in units:
            unit.step(surface.get_size())
            for other in units:
                if unit.has_collision(other):
                    handle_collision(unit, other)
            unit.draw(surface)

        units = [unit for unit in units if unit.is_alive()]  # only keep alive units for the next time step
            
        pygame.display.flip()
        clock.tick(60)

def handle_collision(unit, other):
    """ Handles the collision of 'unit' stepping into 'other' by swapping their speed 
        and stepping 'unit' back. 
    """
    if isinstance(other, Pill):         # if there is a collision with an instance of Pill 
        if isinstance(unit, Player):    #    if a Player instance collides with Pill, eat the pill
            unit.eat_pill()
            unit.add_points(1)
            other.set_alive(False)       
        else:                           #    else (another instance collides with Pill), reverse the speed
            unit.speed = -unit.speed    # **************************************** move to method
            unit.step_back()
    elif isinstance(unit, Pill):
        pass
    else:                               # else (deal with all other collisions), swap the speed
        unit.swap_speed(other)
        unit.step_back()

def spawn_aliens(units, size, player):
    """ Spawns Alies in 'units' list based on its 'spawn_chance'. """
    max_nr_units = 15
    alien_spawn_chance = 0.01
    alien_seeker_spawn_chance = 0.003
    alien_bouncer_spawn_chance = 0.003
    pill_spawn_chance = 0.01
    if Pill.count<1 and random.random() < pill_spawn_chance:
        units.append( Pill(size) )
    if len(units) < max_nr_units:
        if random.random() < alien_spawn_chance:
            units.append( Alien(size) )
        if random.random() < alien_seeker_spawn_chance:
            units.append( Alien_Seeker(size, player) )
        if random.random() < alien_bouncer_spawn_chance:
            units.append( Alien_Bouncer(size) )
            
if __name__ == "__main__":
    main()

import pygame
import random
from multimethod import multimethod

from Unit import Unit
from Player import Player
from Alien import Alien
from Alien_Seeker import Alien_Seeker
from Alien_Bouncer import Alien_Bouncer
from Pill import Pill

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('type hierarchy')
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

        spawn_aliens(units, surface.get_size(), player) # now also add player for Alien_Seekers to lock on to
        
        for unit in units:
            unit.step(surface.get_size())
            for other in units:
                if unit.has_collision(other):
                    handle_collision(unit, other)
            unit.draw(surface)

        units = [unit for unit in units if unit.is_alive()] # only keep alive units for next time step

        pygame.display.flip()
        clock.tick(60)

@multimethod
def handle_collision(unit1: Unit, unit2: Unit):
    """ Handles the collision of 'unit' and 'other' by swapping their speed. """ 
    unit1.swap_speed(unit2)
    
@multimethod    
def handle_collision(unit1: Player, unit2: Pill):
    unit2.set_alive(False)
    unit1.eat_pill()
    unit1.add_points(1)
@multimethod    
def handle_collision(unit2: Pill, unit1: Player):
    handle_collision(unit1, unit2)
    
def spawn_aliens(units, size, player):
    """ Spawns Alies in 'units' list based on its 'spawn_chance' and 'remaining' count. """
    if Alien.remaining > 0 and random.random() < Alien.spawn_chance:
        units.append( Alien(size) )
    if Alien_Seeker.remaining > 0 and random.random() < Alien_Seeker.spawn_chance:
        units.append( Alien_Seeker(size, player) )
    if Alien_Bouncer.remaining > 0 and random.random() < Alien_Bouncer.spawn_chance:
        units.append( Alien_Bouncer(size) )
    if Pill.remaining > 0 and random.random() < Pill.spawn_chance:
        units.append( Pill(size) )
        
if __name__ == "__main__":
    main()
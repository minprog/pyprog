import pygame
import random
from multimethod import multimethod

from Static_Unit import Static_Unit
from Unit import Unit
from Player import Player
from Alien import Alien
from Alien_Seeker import Alien_Seeker
from Points import Points
from Pill import Pill
from Bullet import Bullet

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    player = Player(surface)
    units = []
    units.append(player) # add player as unit
    max_nr_units = 20
    
    running = True
    while running:
        display.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.keyboard(units) # keyboard 

        spawn_units(units, surface, player)
            
        for unit in units:
            unit.step(surface)
            for unit2 in units:
                if unit is not unit2 and unit.has_collision(unit2):
                    handle_collision(unit,unit2)
            unit.draw(surface)
        
        units = [u for u in units if u.is_alive()]
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

def spawn_units(units, surface, player):
    if Alien.remaining>0 and random.random()<Alien.spawn_chance:
        units.append( Alien(surface) )
    if Alien_Seeker.remaining>0 and random.random()<Alien_Seeker.spawn_chance:
        units.append( Alien_Seeker(surface, player) )
    if Points.remaining>0 and random.random()<Points.spawn_chance:
        units.append( Points(surface) )
    if Pill.remaining>0 and random.random()<Pill.spawn_chance:
        units.append( Pill(surface) )

def bounce(unit1: Unit,unit2: Unit):
    unit1.speed, unit2.speed = unit2.speed, unit1.speed
    unit1.step_to_previous()
    unit2.step_to_previous()
        
@multimethod
def handle_collision(unit1: Unit,unit2: Static_Unit):
    unit1.step_to_previous()
    unit1.speed=-unit1.speed
@multimethod
def handle_collision(unit2: Static_Unit,unit1: Unit):
    handle_collision(unit1,unit2)
        
@multimethod
def handle_collision(unit1: Unit,unit2: Unit):
    bounce(unit1,unit2)
    
@multimethod
def handle_collision(unit1: Player,unit2: Alien):
    bounce(unit1,unit2)
    if unit1.is_pill_active():
        unit2.set_alive(False)
        unit1.add_points(unit2.get_points())
@multimethod
def handle_collision(unit2: Alien,unit1: Player):
    handle_collision(unit1,unit2)
    
@multimethod
def handle_collision(unit1: Player,unit2: Points):
    unit2.set_alive(False)
    unit1.add_points(unit2.get_points())
@multimethod
def handle_collision(unit2: Points,unit1: Player):
    handle_collision(unit1,unit2)

@multimethod
def handle_collision(unit1: Player,unit2: Pill):
    unit2.set_alive(False)
    unit1.set_pill()
    unit1.add_points(unit2.get_points())
@multimethod
def handle_collision(unit2: Pill,unit1: Player):
    handle_collision(unit1,unit2)

@multimethod
def handle_collision(unit1: Player,unit2: Bullet):
    pass # do nothing
@multimethod
def handle_collision(unit2: Bullet,unit1: Player):
    handle_collision(unit1,unit2)

@multimethod
def handle_collision(unit1: Alien,unit2: Bullet):
    unit1.set_alive(False)
    unit2.set_alive(False)
@multimethod
def handle_collision(unit2: Bullet,unit1: Alien):
    handle_collision(unit1,unit2)

    
if __name__ == "__main__":
    main()

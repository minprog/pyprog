import pygame
import random
from multimethod import multimethod

from Unit import Unit
from Player import Player
from Alien import Alien
from Alien_Seeker import Alien_Seeker
from Points import Points
from Pill import Pill

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    player = Player(surface)
    units = []
    units.append(player) # add player as unit
    max_nr_units = 20
    
    running = True
    frame_count=0
    while running:
        screen.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.keyboard() # keyboard 

        spawn_units(units, surface, player)
            
        for unit in units:
            unit.step()
            unit.stay_on_screen(surface)
            unit.draw(surface)

        for i1 in range(len(units)):
            for i2 in range(i1+1,len(units)):
                if units[i1].has_collision(units[i2]):
                    handle_collision(units[i1],units[i2])

        units = [u for u in units if u.is_alive()]
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second
        frame_count+=1
        if frame_count%100==0:
            print("Alien.remaining:",Alien.remaining)

def spawn_units(units, surface, player):
    if Alien.remaining>0 and random.random()<Alien.spawn_chance:
        units.append( Alien(surface) )
    if Alien_Seeker.remaining>0 and random.random()<Alien_Seeker.spawn_chance:
        units.append( Alien_Seeker(surface, player) )
    if Points.remaining>0 and random.random()<Points.spawn_chance:
        units.append( Points(surface) )
    if Pill.remaining>0 and random.random()<Pill.spawn_chance:
        units.append( Pill(surface) )

@multimethod
def handle_collision(unit1: Unit,unit2: Unit):
    unit1.speed, unit2.speed = unit2.speed, unit1.speed
        
@multimethod
def handle_collision(unit1: Player,unit2: Alien):
    unit1.speed, unit2.speed = unit2.speed, unit1.speed
    if unit1.is_pill_active():
        unit2.set_alive(False)
@multimethod
def handle_collision(unit2: Alien,unit1: Player):
    handle_collision(unit1,unit2)
    
@multimethod
def handle_collision(unit1: Player,unit2: Points):
    unit2.set_alive(False)
@multimethod
def handle_collision(unit2: Points,unit1: Player):
    handle_collision(unit1,unit2)

@multimethod
def handle_collision(unit1: Player,unit2: Pill):
    unit2.set_alive(False)
    unit1.set_pill()
    
@multimethod
def handle_collision(unit2: Pill,unit1: Player):
    handle_collision(unit1,unit2)
    


if __name__ == "__main__":
    main()

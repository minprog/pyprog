import pygame
import Player
import Alien
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    player = Player.Player(surface)
    units = []
    units.append(player) # add player as unit
    new_alien_chance = 0.01
    max_nr_units = 20
    
    running = True
    while running:
        screen.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.keyboard() # keyboard 

        if len(units)<max_nr_units and random.random()<new_alien_chance:
            units.append( Alien.Alien(surface) )
            
        for unit in units:
            unit.step()
            unit.stay_on_screen(surface)
            unit.draw(surface)

        for i1 in range(len(units)):
            for i2 in range(i1+1,len(units)):
                if units[i1].has_collision(units[i2]):
                    handle_collision(units[i1],units[i2])
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

def handle_collision(unit1,unit2):
    unit1.speed, unit2.speed = unit2.speed, unit1.speed
    
        
if __name__ == "__main__":
    main()

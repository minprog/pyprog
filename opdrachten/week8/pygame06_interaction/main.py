import pygame

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

    units = [] # create units list
    units.append(player) # add player to units
    nr_aliens = 5
    for i in range(nr_aliens):
        alien = Alien(surface.get_size()) # create an Alien object
        units.append(alien)               # add alien to units list
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        for unit in units:                        # for each unit
            unit.step(surface.get_size())         # move the unit based on its speed, stay in the window
            for other in units:
                if unit.has_collision(other):     # check for collision with other units
                    handle_collision(unit, other) # handle the collision
            unit.draw(surface)                    # draw the unit
            
        pygame.display.flip()
        clock.tick(60)

def handle_collision(unit, other):
    """ Handles the collision of 'unit' stepping into 'other' by swapping their speed. """ 
    unit.swap_speed(other)
    
if __name__ == "__main__":
    main()

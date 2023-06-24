import pygame

from Player import Player
from Alien import Alien

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())  

    aliens = []
    nr_aliens = 5
    for i in range(nr_aliens):
        alien = Alien(surface.get_size()) # create an Alien object
        aliens.append(alien)              # add alien to aliens list
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.step(surface.get_size())
        player.draw(surface)

        for alien in aliens:                # for each alient
            alien.step(surface.get_size())  # move the alien based on its speed, stay in the window
            alien.draw(surface)             # draw the alien
            
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

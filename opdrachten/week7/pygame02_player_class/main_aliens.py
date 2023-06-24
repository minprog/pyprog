import pygame
import Player
import Alien
import random

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    player = Player.Player(surface)
    aliens = []
    new_alien_chance = 0.01
    max_nr_aliens = 20
    
    running = True
    while running:
        display.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.keyboard()
        player.step()
        player.stay_on_screen(surface)
        player.draw(surface)

        if len(aliens)<max_nr_aliens and random.random()<new_alien_chance:
            aliens.append( Alien.Alien(surface) )
        for alien in aliens:
            alien.step()
            alien.stay_on_screen(surface)
            alien.draw(surface)
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

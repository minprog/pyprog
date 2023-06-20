import pygame
import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    player = Player.Player(surface)
    
    running = True
    while running:
        screen.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.keyboard()
        player.step()
        player.stay_on_screen(surface)
        player.draw(surface)
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

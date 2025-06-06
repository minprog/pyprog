import pygame

from Player import Player

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())  # create a player object

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)                # use the keyboard to change the speed of player
        player.step(surface.get_size())  # move the player based on its speed, stay in the window
        player.draw(surface)             # draw the player
        
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

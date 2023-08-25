import pygame

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    position = pygame.Vector2(width // 2, height // 2) # position of the player
    radius = 20                                        # radius of player
    line_width = 4                                     # line width of player
    color = (255, 255, 255)                            # color if player

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        speed = 4
        keys = pygame.key.get_pressed()  # read which keyboard keys are pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # change position based on keys
            position.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            position.x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            position.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            position.y += speed

        pygame.draw.circle(surface, color, position, radius, line_width) # draw player

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

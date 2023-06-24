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
    speed = pygame.Vector2(0, 0)                       # speed of the player
    radius = 20                                        # radius of player
    line_width = 4                                     # line width of player
    color = (255, 255, 255)                            # color if player

    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        acceleration = 0.5
        keys = pygame.key.get_pressed()  # read which keyboard keys are pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # change position based on keys
            speed.x -= acceleration
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            speed.x += acceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            speed.y -= acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            speed.y += acceleration

        speed *= 0.95
        position += speed
        
        width, height = surface.get_size()
        if position.x < radius:
            position.x = radius
            speed.x = -speed.x
        if position.y<radius:
            position.y=radius
            speed.y = -speed.y
        if position.x>width-radius:
            position.x=width-radius
            speed.x = -speed.x
        if position.y>height-radius:
            position.y=height-radius
            speed.y = -speed.y
            
        pygame.draw.circle(surface, color, position, radius, line_width) # draw player

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

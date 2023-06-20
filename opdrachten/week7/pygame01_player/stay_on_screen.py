import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('player')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)

    surface=pygame.display.get_surface()
    width, height = surface.get_size()
    position = pygame.Vector2(width//2,height//2) # https://www.pygame.org/docs/ref/math.html
    radius=20
    line_width= 4
    color = (255,255,255)
    
    running = True
    while running:
        screen.fill(background_colour)
        surface=pygame.display.get_surface()
        width, height = surface.get_size()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        speed=4
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            position.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            position.x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            position.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            position.y += speed

        if position.x<radius:
            position.x=radius
        if position.y<radius:
            position.y=radius
        if position.x>width-radius:
            position.x=width-radius
        if position.y>height-radius:
            position.y=height-radius
            
        pygame.draw.circle(surface, color, position, radius, line_width)
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

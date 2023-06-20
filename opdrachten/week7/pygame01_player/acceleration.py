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
    speed = pygame.Vector2(0,0)
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

        accel=0.8
        keys = pygame.key.get_pressed() # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            speed.x -= accel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            speed.x += accel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            speed.y -= accel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            speed.y += accel
        speed.y += 0.5
        speed *= 0.99
        position += speed
            
        if position.x<radius:
            position.x=radius
            speed.x =- speed.x
        if position.y<radius:
            position.y=radius
            speed.y =- speed.y
        if position.x>width-radius:
            position.x=width-radius
            speed.x =- speed.x
        if position.y>height-radius:
            position.y=height-radius
            speed.y =- speed.y
            
        pygame.draw.circle(surface, color, position, radius, line_width)
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

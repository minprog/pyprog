import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('drawing')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)
    
    running = True
    while running:
        screen.fill(background_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface=pygame.display.get_surface()
        width, height = surface.get_size()

        red = (255,0,0)
        rect = pygame.Rect(0, 0, width/3, height/2)
        pygame.draw.rect(surface, red, rect)
        rect = pygame.Rect(0, height/2, width/3, height/2)
        pygame.draw.rect(surface, red, rect, 1)
        
        green = (0,255,0)
        ellipse = (width/3, 0, width/3, height/2)
        pygame.draw.ellipse(surface, green, ellipse)
        ellipse = (width/3, height/2, width/3, height/2)
        pygame.draw.ellipse(surface, green, ellipse, 1)
        
        blue = (0,0,255)
        start_pos = (width*2/3 , 0)
        end_pos = (width, height/2)
        pygame.draw.aaline(surface, blue, start_pos, end_pos)
        points = [ (width*2/3 , height/2), (width, height), (width,height/2), (width*2/3,height) ]
        pygame.draw.aalines(surface, blue, False, points)
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

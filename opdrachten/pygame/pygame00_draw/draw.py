import pygame

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # create a display window
    pygame.display.set_caption('drawing')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)  # set background_color Red,Green,Blue components (black)

    running = True
    while running: # keep looping 
        display.fill(background_colour)  # fill display with background_colour
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # stop loop if display window is closed
                running = False

        surface = pygame.display.get_surface()
        width, height = surface.get_size()  # get size of display

        
        # draw white rectangles
        white = (255, 255, 255)  # color
        rect = pygame.Rect(0, 0, width / 2, height / 2)  # create a rectangle
        pygame.draw.rect(surface, white, rect, 4)  # draw rectangle with line_width 4
        rect = pygame.Rect(width / 2, height / 2, width / 2, height / 2)  # create a rectangle
        pygame.draw.rect(surface, white, rect, 0)  # draw rectangle filled in

        # draw red ellipse
        red = (255,0,0)
        ellipse = (0, height / 2, width / 2, height / 2)
        pygame.draw.ellipse(surface, red, ellipse, 4)

        # draw blue line
        blue = (0,0,255)
        start_pos = (width / 2      , 0)
        end_pos   = (width          , height / 2)
        pygame.draw.line(surface, blue, start_pos, end_pos, 4)
        
        
        pygame.display.flip()  # update display with drawings
        clock.tick(60)  # run loop at 60 frames per second

if __name__ == "__main__":
    main()

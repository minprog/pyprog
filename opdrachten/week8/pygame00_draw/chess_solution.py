import pygame
import math

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('chessboard')
    clock = pygame.time.Clock()
    background_colour = (0,0,0) # Red,Green,Blue (black)
    
    running = True
    while running:
        display.fill(background_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface=pygame.display.get_surface()
        width, height = surface.get_size()

        line_thickness=4
        n=8
        rect_width=width/n
        rect_height=height/n
        white=(255,255,255)
        for xi in range(n):
            for yi in range(n):
                if (xi+yi)%2==0:
                    rect = pygame.Rect(xi*rect_width, yi*rect_height, rect_width, rect_height)
                    pygame.draw.rect(surface, white, rect)

        red = (255,0,0)
        ellipse = (rect_width, rect_height, width-rect_width*2, height-rect_height*2)
        pygame.draw.ellipse(surface, red, ellipse, line_thickness)
                    
        blue = (0,0,255)
        p1 = (rect_width, rect_height)
        p2 = (width-rect_width, height-rect_height)
        pygame.draw.line(surface, blue, p1, p2, line_thickness)
        p1 = (width-rect_width, rect_height)
        p2 = (rect_width, height-rect_height)
        pygame.draw.line(surface, blue, p1, p2, line_thickness)
        
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

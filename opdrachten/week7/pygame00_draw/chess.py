import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('chessboard')
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
        for i in range(1,math.ceil(n/2)):
            ellipse = (i*rect_width, i*rect_height, (n-i*2)*rect_width, (n-i*2)*rect_height)
            pygame.draw.ellipse(surface, red, ellipse, line_thickness)
                    
        blue = (0,0,255)
        for i in range(1,n):
            for j in range(1,n):
                start_pos = (rect_width      , rect_height*i)
                end_pos   = (rect_width*(n-1), rect_height*j)
                pygame.draw.line(surface, blue, start_pos, end_pos, line_thickness)
            
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

if __name__ == "__main__":
    main()

import pygame

class Unit:

    def __init__(self, position, speed):
        """ Initializes a player in the middle of 'size'. """
        self.position = position
        self.previous_position = self.position.copy()
        self.speed = speed        
        
    def step(self, size):
        """ Changes the position of player based on its speed. """
        self.previous_position = self.position.copy()
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Makes sure the players stays on the window with 'size'. """
        width, height = size
        if self.position.x<self.radius:
            self.position.x = self.radius
            self.speed.x =- self.speed.x
        if self.position.y<self.radius:
            self.position.y=self.radius
            self.speed.y =- self.speed.y
        if self.position.x>width-self.radius:
            self.position.x = width-self.radius
            self.speed.x =- self.speed.x
        if self.position.y>height-self.radius:
            self.position.y=height-self.radius
            self.speed.y =- self.speed.y

    def draw(self, surface):
        """ Draws the player on the 'surface'. """
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

    def has_collision(self, other):
        """ Returns True if 'self' is in collision with 'other'. """
        if other is self: # 'self' does not collide with 'self'
            return False
        position_difference = self.position - other.position
        return position_difference.length() < self.radius + other.radius

    def swap_speed(self, other):
        """ Swaps the the speed of 'unit' and 'other'. """
        self.speed, other.speed = other.speed, self.speed
    
    def step_to_previous_position(self):
        """ Step to previous position that so there is no collision. """
        self.position = self.previous_position
    

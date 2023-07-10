import pygame
import random
import math

class Line:

    def __init__(self, p1, p2, collision = False):
        self.p1 = p1
        self.p2 = p2
        self.collision = collision

    def set_collision(self, collision):
        self.collision = collision
        
    def draw(self, surface, color=(255,255,255), line_width=4):
        if self.collision:
            line_width *= 2
            color = (255,0,0)
        pygame.draw.line(surface, color, self.p1, self.p2, line_width)
        
    def does_intersect(self, other: "Line"):
        # math taken from: https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect/565282#565282
        p = self.p1
        r = self.p2 - self.p1
        q = other.p1
        s = other.p2 - other.p1
        rxs = r.cross(s)
        q_p = q - p
        q_pxr = q_p.cross(r)
        close_to_zero = 0.00000001
        if math.fabs(rxs) < close_to_zero: # lines are parallel
            if math.fabs(q_pxr) < close_to_zero:
                rdr = r.dot(r)
                if math.fabs(rdr) < close_to_zero:
                    return False
                t0 = q_p.dot(r) / rdr
                t1 = t0 + s.dot(r) / rdr
                return not ((t0 < 0 and t1 < 0) or (t0 > 1 and t1 > 1))
            else:
                return False
        t = q_p.cross(s)/rxs
        u = q_pxr/rxs
        return t>=0 and t<=1 and u>=0 and u<=1

    def __add__(self, pos: pygame.Vector2):
        return Line(self.p1+pos, self.p2+pos, self.collision)

class Unit:

    def __init__(self, position, speed, radius=20, line_width=4, color=(255,255,255)):
        """ Initializes a Unit. """
        self.position = position
        self.speed = speed
        self.line_width = line_width
        self.color = color
        self.lines = []

    def step(self, size):
        """ Changes the position of Unit based on its speed. """
        self.position += self.speed
        self.stay_on_window(size)
        
    def stay_on_window(self, size):
        """ Makes sure the Unit stays on the window with 'size'. """
        width, height = size
        if self.position.x<0:
            self.position.x = 0
            self.speed.x =- self.speed.x
        if self.position.y<0:
            self.position.y=0
            self.speed.y =- self.speed.y
        if self.position.x>width:
            self.position.x = width
            self.speed.x =- self.speed.x
        if self.position.y>height:
            self.position.y=height
            self.speed.y =- self.speed.y

    def draw(self, surface):
        """ Draws the Unit on the 'surface'. """
        for line in self.lines:
            (line+self.position).draw(surface, self.color, self.line_width)
            line.set_collision(False) # clear collision state

    def has_collision(self, other):
        """ Returns True if 'self' is in collision with 'other'. """
        if other is self: # 'self' does not collide with 'self'
            return False
        for l1 in self.lines:
            for l2 in other.lines:
                if (l1+self.position).does_intersect(l2+other.position):
                    l1.set_collision(True) # set collision state
                    l2.set_collision(True) # set collision state
            
class Player(Unit):

    def __init__(self, size):
        """ Initializes a player in the middle of 'size'. """
        width, height = size
        position = pygame.Vector2(width//2,height//2)
        speed = pygame.Vector2(0,0)
        super().__init__(position, speed)
        self.lines.append( Line( pygame.Vector2(  0, 30), pygame.Vector2(  0,-30)) )
        self.lines.append( Line( pygame.Vector2( 30,  0), pygame.Vector2(-30,  0)) )
        self.lines.append( Line( pygame.Vector2(-30,-30), pygame.Vector2( 30, 30)) )
        self.lines.append( Line( pygame.Vector2( 30,-30), pygame.Vector2(-30, 30)) )
        
    def move(self, keys):
        """ 
        Moves the player by changing its speed based on keyboard 'keys' pressed. 
        Limits the speed by multipling it by '0.95'.
        """
        acceleration = 0.5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed.x -= acceleration
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed.x += acceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed.y -= acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed.y += acceleration
        self.speed *= 0.95

class Triangle(Unit):
    def __init__(self, size):
        width, height = size
        position = pygame.Vector2(random.random()*width,
                                  random.random()*height)
        speed = 3
        speed = pygame.Vector2(random.random()*speed*2-speed,
                               random.random()*speed*2-speed)
        super().__init__(position, speed)
        length = 20
        p1 = pygame.Vector2(-length,+length)
        p2 = pygame.Vector2(+length,+length)
        p3 = pygame.Vector2(      0,-length)
        self.lines.append( Line(p1 , p2) )
        self.lines.append( Line(p2 , p3) )
        self.lines.append( Line(p3 , p1) )
        
def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('steering')
    clock = pygame.time.Clock()
    background_colour = (0, 0, 0)

    surface = pygame.display.get_surface()
    player = Player(surface.get_size())

    units = []
    units.append(player)
    for i in range(20):
        units.append( Triangle(surface.get_size()) )
    
    running = True
    while running:
        display.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        for unit in units:
            unit.step(surface.get_size())
            for other in units:
                if unit.has_collision(other):     
                    pass
            unit.draw(surface)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

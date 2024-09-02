# MyGame Server

We kunnen ook zmq sockets gebruiken om een multi-player computerspel te
schrijven.

## Alle Bestanden

- [mygame_client.py](mygame_client.py)
- [mygame_server.py](mygame_server.py)
- [Action.py](Action.py)
- [Game_State.py](Game_State.py)
- [Player.py](Player.py)

## Protocol

In ons multi-player computerspel stuurt een client in de elke tijstap
de naam en de actie die een speler in het spel maakt naar de server in
een `Action` object. De server ontvangt de acties van elke speler,
berekent de staat van het spel in de volgende tijdstap, en stuurt deze
staat terug naar elke client in een `Game_State` object. Elke client
ontvangt een `Game_State` object en tekent vervolgens deze staat
waarin dus de acties van elke speler verwerkt zitten zodat alle
spelers gezamelijk hetzelfde spel spelen.

![mygame_server.png](mygame_server.png)

## mygame_client.py

Bestand [mygame_client.py](mygame_client.py) is een aanpasssing van
'status_client.py' en laat zien hoe elke tijdstap een `Action` object
naar de server wordt gestuurd met de actie van de gebruiker. Als
antwoord ontvangt het een `Game_State` object van de server met de
huidige staat van het spel wat wordt getekend.

~~~python
import sys
import zmq
import pygame

from Action import Action
from Game_State import Game_State

def main(name, port, host):
    # connect to server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    print(f"Connecting to port '{port}' of host '{host}'.")

    # start pygame
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('mygame')
    surface = pygame.display.get_surface()
    clock = pygame.time.Clock()
    background_color = (0,0,0)
    name_textures = Name_Textures()
    game_state = None
    
    running = True
    while running:
        display.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        socket.send_pyobj(get_action(name, pygame.key.get_pressed())) # send action
        if game_state:
            game_state.draw(name,surface,name_textures) # draw while waiting for answer
        game_state = socket.recv_pyobj() # receive game_state
        #print("game_state:",game_state)
        
        pygame.display.flip()
        clock.tick(60) # run at 60 frames per second

def get_action(name,keys):
    acceleration=pygame.Vector2(0,0)
    accel=0.5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        acceleration.x -= accel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        acceleration.x += accel
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        acceleration.y -= accel
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        acceleration.y += accel
    return Action(name, acceleration)

class Name_Textures: # class to generate and store textures of user names

    def __init__(self):
        self.name_textures={}

    def get_texture(self, name):
        if not name in self.name_textures:
            font = pygame.font.SysFont('Comic Sans MS', 20)
            name_texture = font.render(name, False, (255,255,255))
            self.name_textures[name] = name_texture
        return self.name_textures[name]
        
if __name__ == "__main__":
    name = "_"
    port = 2345
    host = "127.0.0.1"
    if len(sys.argv)>1:
        name = sys.argv[1]
    if len(sys.argv)>2:
        port = int(sys.argv[2])
    if len(sys.argv)>3:
        host = sys.argv[3]
    main(name, port, host)
~~~

## mygame_server.py

Bestand [mygame_server.py](mygame_server.py) is een aanpasssing van
'status_server.py' en laat zien hoe elke tijdstap de `Action` objecten
van de clients worden ontvangen, de `Game_State` wordt bijgewerkt en
teruggestuurd naar elke client. Dit bestand hoeft
niet te worden aangepast, dus het is niet nodig om alle details te
begrijpen.


~~~python
import sys
import zmq
import time
import pygame

from Action import Action
from Game_State import Game_State

def main(port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{host}:{port}")
    print(f"Waiting for clients on port '{port}' on host '{host}'.")
    prev_time = time.time()
    game_fps = 60
    actions = {}
    game_state = Game_State(pygame.Vector2(800,600))
    while True:
        try:
            action = socket.recv_pyobj(flags=zmq.NOBLOCK)
            #print("action:",action)
            actions[action.get_name()] = action
            socket.send_pyobj(game_state)
        except zmq.ZMQError as e:
            time.sleep(0.0005) # wait a bit
        current_time = time.time()
        elapsed_time = current_time - prev_time
        if elapsed_time > 1/game_fps: # when enough time has passed
            prev_time = current_time
            update_game_state(game_state, actions)

def update_game_state(game_state, actions):
    for name, action in actions.items():
        if name != '_':
            game_state.update(action)
            
if __name__ == "__main__":
    port = 2345
    host = "127.0.0.1"
    if len(sys.argv)>1:
        port = int(sys.argv[1])
    if len(sys.argv)>2:
        host = sys.argv[2]
    main(port, host)
~~~


## Server en Clients Starten

We starten eerst de mygame_server met:

~~~console
$ python mygame_server.py 
pygame 2.4.0 (SDL 2.26.4, Python 3.10.6)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '2345' on host '127.0.0.1'.
~~~

En daarna twee clients met een gebruikersnaam als
command-line-argument. Vervolgens kan iedere gebruiker in hetzelfde
spel acties uitvoeren:

<table style="width:100%">
<tr>
<th>myclient_client</th>
<th>myclient_client</th>
</tr>
<tr>
<td valign="top">
  
$ python mygame_client.py Jackson <br>
pygame 2.4.0 (SDL 2.26.4, Python 3.10.6) <br>
Hello from the pygame community. <br>
Connecting to port '2345' of host '127.0.0.1'.

</td>
<td valign="top">

$ python mygame_client.py Madonna <br>
pygame 2.4.0 (SDL 2.26.4, Python 3.10.6) <br>
Hello from the pygame community. <br>
Connecting to port '2345' of host '127.0.0.1'.

</td>
</tr>
</table>

![mygame.gif](mygame.gif)

## Spelelement

Het spel heeft nu nog geen spelelement. Om dat toe te voegen kan de
`Action` class in [Action.py](Action.py) worden aangepast zodat een
gebruiker naast haar acceleratie ook nog evenuteel andere acties kan
sturen naar de server:

~~~python
class Action:

    def __init__(self, name, acceleration):
        self.name = name
        self.acceleration = acceleration

    def __repr__(self):
        return f"name: {self.name} acceleration:{self.acceleration}"

    def get_name(self):
        return self.name

    def get_acceleration(self):
        return self.acceleration
~~~

De server kan in de `Game_State` class in
[Game_State.py](Game_state.py) ook andere units aan de `units` list
toevoegen. In deze `units` list worden alle units van het spel
opgeslagen. Nu heeft het nog alleen `Player` objecten. Deze `Player`
objecten worden ook in dictionary `players` opgeslagen, dat is omdat
we een `Player` snel op naam willen kunnen zoeken.

~~~python
import pygame

from Player import Player

class Game_State:

    def __init__(self, world_size):
        self.world_size = world_size
        self.players = {}
        self.units = []

    def __repr__(self):
        return f"world_size: {self.world_size}\nunits: {self.units}"

    def update(self, action):
        name = action.get_name()
        if not name in self.players: # if the name is not seen before
            player = Player(self.world_size, name) # create a new player
            self.units.append(player)              # add to units
            self.players[name] = player            # add to players too for fast lookup by name 
        player = self.players[name]
        player.accelerate(action.get_acceleration())
        player.step()
        player.stay_on_screen(self.world_size)

    def spawn_units(self):
        pass
        
    def draw(self, name, surface, name_textures):
        rect = pygame.Rect(pygame.Vector2(0, 0), self.world_size)
        white = (255, 255, 255)
        pygame.draw.rect(surface, white, rect, 2)
        for unit in self.units:
            unit.draw(surface, name_textures)
~~~

Het enige unit type van dit spel is nu nog de `Player` class in
[Player.py](Player.py) die we al eerder gezien hebben, maar nu wordt
ook de naam van de gebruiker boven een `Player` getekend in de
`draw()` methode:

~~~python
import pygame

class Player:
    radius = 20
    line_width = 4
    color = (255,255,255)
        
    def __init__(self, world_size, name):
        self.name = name
        self.position = pygame.Vector2(world_size.x//2, world_size.y//2)
        self.speed = pygame.Vector2(0,0)
        self.line_width = 4
        self.color = (255,255,255)

    def __repr__(self):
        return f"position: {self.position} speed: {self.speed}"

    def get_position(self):
        return self.position
    
    def accelerate(self,acceleration):
        self.speed += acceleration
        self.speed *= 0.95
        
    def step(self):
        self.position += self.speed

    def stay_on_screen(self,world_size):
        if self.position.x<Player.radius:
            self.position.x = Player.radius
            self.speed.x =- self.speed.x
        if self.position.y<Player.radius:
            self.position.y=Player.radius
            self.speed.y =- self.speed.y
        if self.position.x > world_size.x - Player.radius:
            self.position.x = world_size.x -Player.radius
            self.speed.x =- self.speed.x
        if self.position.y > world_size.y - Player.radius:
            self.position.y = world_size.y -Player.radius
            self.speed.y =- self.speed.y

    def draw(self, surface, name_textures):
        pygame.draw.circle(surface, Player.color, self.position, Player.radius, Player.line_width)
        name_texture = name_textures.get_texture(self.name)
        text_offset = pygame.Vector2( name_texture.get_size() )
        text_offset.x /= 2
        text_offset.y += Player.radius
        surface.blit(name_texture, self.position - text_offset )
~~~

## Opdracht: Spelen

Lees de code en speel even met clients en server.

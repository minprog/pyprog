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
            update_game_state(game_state,actions)

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

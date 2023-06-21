import sys
import traceback
import zmq
import time

def main(name, port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    print(f"Connecting as '{name}' to server '{host}' on port '{port}'.")
    count=0
    while True:
        if name!="_":
            line = input(f"{name}: ") # blocks
            socket.send_string(f"{name}: {line}") # send state
        else:
            socket.send_string("_:") # request state
        states = socket.recv_string()
        print("-----------------",count)
        print(states)
        if name=="_":
            time.sleep(2)
        count+=1
    
if __name__ == "__main__":
    name = "_"
    port = 2345
    host = "0.0.0.0"
    if len(sys.argv)>1:
        name = sys.argv[1]
    if len(sys.argv)>2:
        port = int(sys.argv[2])
    if len(sys.argv)>3:
        host = sys.argv[3]
    main(name, port, host)

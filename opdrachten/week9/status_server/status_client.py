import sys
import zmq
import time

def main(name, port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    print(f"Connecting to port '{port}' of host '{host}'.")
    count = 0
    while True:
        if name != "_":
            line = input(f"{name}: ")  # blocks
            socket.send_string(f"{name}: {line}")  # send state
        else:
            time.sleep(2)  # every 2 seconds
            socket.send_string("_:")  # request state
        states = socket.recv_string() # receive answer
        print("-----------------", count)
        print(states)
        count += 1


if __name__ == "__main__":
    name = "_"
    port = 2345
    host = "127.0.0.1"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    if len(sys.argv) > 3:
        host = sys.argv[3]
    main(name, port, host)

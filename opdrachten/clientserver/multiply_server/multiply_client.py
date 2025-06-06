import sys
import zmq

def main(port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    print(f"Connecting to port '{port}' of host '{host}'.")
    count=0
    while True:
        line = input("give a number to multiply: ")
        socket.send_string(line)      # send number
        line = socket.recv_string()   # receive number
        print(line)
    
if __name__ == "__main__":
    port = 2345
    host = "127.0.0.1"
    if len(sys.argv)>1:
        port = int(sys.argv[1])
    if len(sys.argv)>2:
        host = sys.argv[2]
    main(port, host)

import sys
import zmq
        
def main(multiplier, port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{host}:{port}")
    print(f"Waiting for clients on port '{port}' on host '{host}'.")
    while True:
        line = socket.recv_string()
        try:
            input_number = float(line)
            output_number = input_number * multiplier
        except ValueError:
            output_number = "not a 'float'"
        print(f"received: {line} sending: {output_number}")
        socket.send_string(str(output_number))
            
if __name__ == "__main__":
    multiplier = 2
    port = 2345
    host = "127.0.0.1"
    if len(sys.argv)>1:
        multiplier = int(sys.argv[1])
    if len(sys.argv)>2:
        port = int(sys.argv[2])
    if len(sys.argv)>3:
        host = sys.argv[3]
    main(multiplier, port, host)

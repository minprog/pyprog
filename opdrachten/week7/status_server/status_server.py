import sys
import zmq

def split(line):
    index=line.find(':')
    return line[:index],line[index:]

def states_to_string(states):
    s=""
    for name,state in states.items():
        s+="- "+name+state+'\n'
    return s
        
def main(port, host):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{host}:{port}")
    print(f"Waiting for clients on port '{port}' on host '{host}'.")
    states={}
    while True:
        line = socket.recv_string()
        name,status = split(line)
        if name!='_':
            print("received name: '{name}' status: '{status}'")
            states[name]=status
        socket.send_string(states_to_string(states))
            
if __name__ == "__main__":
    port = 2345
    host = "0.0.0.0"
    if len(sys.argv)>1:
        port = int(sys.argv[1])
    if len(sys.argv)>2:
        host = sys.argv[2]
    main(port, host)

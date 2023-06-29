# Client Server

Om verschillende Python programma's met elkaar te laten communiceren
kunnen we zmq sockets gebruiken. Installeer zmq met:

```console
$ pip install zmq
```

Programma [multiply_server.py](multiply_server.py) is een 'server' die
een vermenigvuldig-service aanbiedt. Het 'bind' een zmq socket op een
port, wacht tot het een verzoek krijgt van een 'client', en
stuurt de vermenigvuldiging terug als antwoord:

```python
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
```

Programma [multiply_client.py](multiply_client.py) is een 'client' die
gebruik maakt van de vermenigvuldig-service. Het 'connect' een zmq
socket op de port, vraagt de gebruiker steeds om een getal, stuurt dat
naar de server, en wacht op antwoord:

```python
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
```

## Client en Server Starten

Als we de twee programma's allebei starten en de client wat getallen
geven zien we bijvoorbeeld:

<table>
<tr>
<th>multiply_server</th>
<th>multiply_client</th>
</tr>
<tr>
<td>
  
```console
$ python multiply_server.py 
Waiting for clients on port '2345' on host '127.0.0.1'.
received: 100 sending: 200.0
received: 1000 sending: 2000.0
```

</td>
<td>

```console
$ python multiply_client.py 
Connecting to port '2345' of host '127.0.0.1'.
give a number to multiply: 100
200.0
give a number to multiply: 1000
2000.0
give a number to multiply:
```

</td>
</tr>
</table>

Een server kan verzoeken van meerdere clients afhandelen. Stuur zelf
verzoeken van meerdere clients.


## Meedere Servers

Als we tegelijkertijd meerdere servers willen starten moeten we elke
server een eigen poort geven. Poorten onder de 2000 zijn gereserveerd
dus die zullen we niet gebruiken. Onze server gebruikt bij default
multiplier 2 en poort 2345, maar met command-line-arguments kunnen we
dat aanpassen. Gebruik bijvoorbeeld dit om een server die met 5
vermenigvuldigd te starten op poort 2500, en een client die daarmee
verbindt:

<table>
<tr>
<th>multiply_server</th>
<th>multiply_client</th>
</tr>
<tr>
<td>
  
```console
$ python multiply_server.py 5 2500
Waiting for clients on port '2500' on host '127.0.0.1'.
received: 100 sending: 500.0
received: 1000 sending: 5000.0
```

</td>
<td>

```console
$ python multiply_client.py 2500
Connecting to port '2500' of host '127.0.0.1'.
give a number to multiply: 100
500.0
give a number to multiply: 1000
5000.0
give a number to multiply:
```

</td>
</tr>
</table>

## Opdracht: Spelen

Lees de code en speel even met clients en servers.

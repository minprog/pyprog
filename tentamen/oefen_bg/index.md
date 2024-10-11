# Oefententamen

[Ga naar de tentamen-editor](https://pyprog.proglab.nl/exams)

## List comprehensions

Door het oplossen van onderstaande opgaven laat je zien dat je het gebruik van comprehensions beheerst. Elke opgave wordt opgelost door het schrijven van één functie met daarin een list comprehension. Zorg dat elke functie minimaal drie doctests heeft, inclusief de gegeven doctest, en dat alle type hints op orde zijn.

### Deelbaar (0.5 punt)

Schrijf een functie `deelbaar()` die een lijst van getallen en een getal (de deler) aanneemt. De functie moet een lijst van getallen teruggeven die deelbaar zijn door de deler. Implementeer deze functie door middel van een enkele list comprehension. Voeg nog minimaal twee zinvolle doctests toe.

    >>> deelbaar([10, 15, 20, 25, 100], 10)
    [10, 20, 100]

### Oeps (0.5 punt)

Schrijf een functie `oeps()` die elke tweede waarde in een lijst van strings vervangt door de string `"oeps"`. Implementeer deze functie door middel van een enkele list comprehension. Voeg nog minimaal twee zinvolle doctests toe.

    >>> oeps(["dit", "was", "een", "lijst", "van", "woorden"])
    ["dit", "oeps", "een", "oeps", "van", "oeps"]

### Schreeuw (0.5 punt)

Schrijf een functie `schreeuw()` die een string aanneemt en iedere klinker (`aeiou`) vervangt door vijf keer dezelfde klinker. Implementeer deze functie door middel van een enkele list comprehension. Voeg nog minimaal twee zinvolle doctests toe.

    >>> schreeuw("dit is een zin")
    'diiiiit iiiiis eeeeeeeeeen ziiiiin'

### Ketting (0.5 punt)

Implementeer onderstaande functie op één regel door middel van een enkele list comprehension. Je hoeft geen extra doctests toe te voegen. Je moet je hier baseren op de indices van de lijst, met de functie `range()`.

    def ketting(paren: list[list[int]]) -> list[list[int]]:
        """
        Geeft alle paren terug waarvoor het tweede getal in het paar gelijk is aan het
        eerste getal van het volgende paar.

        >>> ketting([[1, 2], [2, 3], [3, 4]])
        [[1, 2], [2, 3]]
        >>> ketting([[1, 7], [2, 3], [3, 4]])
        [[2, 3]]
        >>> ketting([[1, 2]])
        []
        """


## Collection types

Door het oplossen van onderstaande opgaven laat je zien dat je het gebruik van collection types beheerst en de basis-operaties die je erop kunt toepassen. Zorg dat elke functie minimaal drie doctests heeft, inclusief de gegeven doctest, en dat alle type hints op orde zijn.

### Emmeren (1 punt)

Implementeer de functie. Vul zelf het return type in. Voeg nog minimaal twee zinvolle doctests toe.

### Frisdrank (1 punt)

Implementeer de functie. Vul zelf het return type in. Voeg nog minimaal twee zinvolle doctests toe.

### Rits (1 punt)

Implementeer de functie. Vul zelf het return type in. Bij deze opgave hoef je geen extra doctests te schrijven, maar je moet de onderstaande wel overnemen. Je mag <u>geen</u> gebruik maken van functies als `zip()`, `map()` en `filter()`.

## Objects en classes (4 punten)

DiceRace is een bordspel. We definiëren X posities op het bord, genummerd van 0 tot en met X-1. Als er drie spelers zijn, dan worden deze op posities 0, 1 en 2 geplaatst. We maken een versie in Python, waar de spelers om beurten zelf een dobbelsteen gooien en de gegooide waarde invoeren. Degene die als eerst bij X is heeft gewonnen. Als we drie spelers hebben, kan het spel op de volgende manier verlopen:

    How long is the racing track? 10
     A C J - - - - - - -
    Current player:  Ali
    Throw your dice: 6
     - C J - - - A - - -
    Current player:  Carmen
    Throw your dice: 1
     - - CJ - - - A - - -
    Current player:  Jakub
    Throw your dice: 2
     - - C - J - A - - -
    Current player:  Ali
    Throw your dice: 4
    Game won by Ali!

Door het oplossen van deze opgave laat je zien dat je het gebruik van classes beheerst. Neem de volgende testcode heel nauwkeurig over (zonder de comments!) en schrijf de ontbrekende classes `Player` en `DiceRace`. Verander niets aan de gegeven code. Zorg dat elke method minimaal twee doctests heeft, want alleen methodes met zinvolle doctests en type hints worden meegeteld. Uitzondering: een methode die niets returnt of print hoeft geen doctest te krijgen.

<!--
# Oeber

You are tasked with developing a queue-like data structure for a fictional ride-hailing application. The application uses the queue to manage ride requests from customers and dispatch them to drivers in real-time. The core functionality of the queue is the same as a traditional queue, with First In, First Out (FIFO) behavior. However, the application needs additional features to handle more advanced scenarios, and you are required to implement a custom class RideQueue to meet these requirements.

## Requirements:

1. **Basic Queue Operations**:

    Your `RideQueue` class should support the following standard queue operations:

    - `enqueue(item)` – Adds a new ride request to the queue.
    - `dequeue()` – Removes and returns the ride request that has been in the queue the longest.
    - `is_empty()` – Returns `True` if the queue is empty, `False` otherwise.
    - `peek()` – Returns the ride request that is next in line without removing it from the queue.

2.  **Enhanced Features**:

    To meet the needs of the ride-hailing application, your queue must provide the following custom behaviors:

    - **VIP Ride Requests**:
        Sometimes, the system receives VIP ride requests that must be prioritized. When a VIP ride request is added to the queue using `enqueue_vip(item)`, it should be placed at the front of the queue, before any regular ride requests.

    - **Cancel a Ride Request**:
        Ride requests can be canceled before they are dispatched. Implement a method `cancel_request(item)` that removes a specific ride request from the queue (either regular or VIP). The method should return `True` if the request was found and canceled, and `False` otherwise.

    - **Waiting Time Calculation**:
        Implement a method `waiting_time(position)` that returns the number of ride requests a customer has to wait through before their request is dispatched. This will depend on their position in the queue (the first ride in the queue has a waiting time of 0).

    - **Limit Queue Size**:
        The queue has a maximum capacity, and once full, new requests cannot be added unless space becomes available (via a dequeue or cancellation). Implement a constructor parameter `max_size` that allows the user to set the maximum size of the queue. If the queue is full, `enqueue` should raise an exception or return an error message.

3.  **Bonus Challenge**:

    For extra credit, add a feature that tracks the **average wait time** of ride requests in the queue. Implement a method `average_wait_time()` that returns the average number of rides a request must wait through before it is dispatched.

## Class Definition:

You are required to implement the class `RideQueue` with the following methods:

- `__init__(self, max_size)`
- `enqueue(self, item)`
- `enqueue_vip(self, item)`
- `dequeue(self)`
- `cancel_request(self, item)`
- `is_empty(self)`
- `peek(self)`
- `waiting_time(self, position)`
- *(Optional)* `average_wait_time(self)`

## Example Usage:

    queue = RideQueue(max_size=5)
    queue.enqueue("Ride1")
    queue.enqueue("Ride2")
    queue.enqueue_vip("VIP_Ride1")
    queue.enqueue("Ride3")

    # Queue: ["VIP_Ride1", "Ride1", "Ride2", "Ride3"]
    print(queue.peek())  # Output: "VIP_Ride1"
    queue.dequeue()      # Dispatches "VIP_Ride1"
    print(queue.waiting_time(1))  # Output: 1 (Ride2 is next after Ride1)
    queue.cancel_request("Ride2") # Cancels "Ride2"
    print(queue.is_empty())       # Output: False

## Constraints:

- The ride requests are simple strings representing customer IDs (e.g., "Ride1", "VIP_Ride1").
- You must handle edge cases, such as trying to dequeue from an empty queue or adding a ride request when the queue is full. -->

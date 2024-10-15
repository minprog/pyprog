# Oefententamen

[Ga naar de tentamen-editor](https://pyprog.proglab.nl/exams) om deze goed te leren kennen vóór het tentamen plaatsvindt --- hier staat ook een deel van de code die je nodig hebt voor onderstaande vragen!

1. Voor het nakijken is het nodig dat je de gevraagde technieken gebruikt (zoals bv. comprehensions). Daarnaast moeten alle uitwerkingen doctests hebben die aantonen dat het werkt voor een aantal goedgekozen gevallen, en ook types die logisch zijn. Voor een deel geven we al doctests om je op weg te helpen.

2. Tijdens het echte tentamen zul je ook op je eigen laptop in de tentamen-editor werken. Je mag dan geen enkel ander programma of andere website open hebben, altijd de editor in beeld. Hier wordt ook op gesurveilleerd.

3. De puntentelling hieronder is indicatief voor het tentamen (de gewichten van elke som), maar er kunnen nog wijzigingen doorgevoerd worden, afhankelijk van de inhoud van het tentamen. Het tentamen moet voldoende gemaakt worden, dat wil zeggen: minimaal de helft van de punten.

4. Tentamenstrategie-tip: doe eerst een paar kleintjes om in te komen en concentreer je daarna op de grotere OOP-opgaven. Kijk daarna strategisch waar je nog het best tijd aan kunt besteden.

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

Implementeer de functie. Vul zelf het return type in. Bij deze opgave hoef je geen extra doctests te schrijven, maar je moet de gegeven doctests wel overnemen. Je mag <u>geen</u> gebruik maken van functies als `zip()`, `map()` en `filter()`.

## Objects en classes

### DiceRace (3 punten)

DiceRace is een bordspel. We definiëren X posities op het bord, genummerd van 0 tot en met X-1. Als er drie spelers zijn, dan worden deze op posities 0, 1 en 2 geplaatst. We maken een versie in Python, waarin we het spel simuleren. Spelers gooien om beurten een dobbelsteen. Degene die als eerst bij de laatste positie is heeft gewonnen. Als we drie spelers hebben, kan het spel op de volgende manier verlopen:

     A C J - - - - - - -
    Current player Ali throws die value: 1
    - AC J - - - - - - -
    Current player Carmen throws die value: 3
    - A J - C - - - - -
    Current player Jakub throws die value: 1
    - A - J C - - - - -
    Current player Ali throws die value: 6
    - - - J C - - A - -
    Current player Carmen throws die value: 6
    Game won by Carmen!

Door het oplossen van deze opgave laat je zien dat je het gebruik van classes beheerst. Schrijf de ontbrekende classes `Player` en `DiceRace`. Verander niets aan de gegeven code. Zorg dat elke method minimaal twee doctests heeft, want alleen methodes met zinvolle doctests en type hints worden meegeteld. Uitzondering: een methode die niets returnt of print hoeft geen doctest te krijgen.


Aangepaste template:

    if __name__ == '__main__':
        # create 3 new player objects
        players = [Player('Ali'), Player('Carmen'), Player('Jakub')]
        number_of_places = 10
    
        # create new game
        # the game should keep track of what player's turn it is
        # and also place them in the correct initial position
        game = DiceRace(players, number_of_places)

        while not game.is_done():
            # print current board state
            state_string = ""
            for pos in range(number_of_places):
                state_string += " "
                # get initials for all players that are at position i
                players_at_pos = [player.initial() for player in players
                                  if player.position == pos]
                # either print those initials or "-" if no players are at position i
                if len(players_at_pos) > 0:
                    state_string += "".join(players_at_pos)
                else:
                    state_string += "-"
            print(state_string)

            # current player throws a die
            die = random.randint(1, 6)
            print(f"Current player {game.current_player_name()} throws die value:", die)
            # move the current player, it should automatically advance to next player
            game.play(die)
            if game.is_done():
                print(f"Game won by {game.winner_name()}!")


### Oeber (3 punten)

You are tasked with developing a queue-like data structure for a fictional ride-hailing application. The application uses the queue to manage ride requests from customers and dispatch them to drivers in real-time. The core functionality of the queue is the same as a traditional queue, with First In, First Out (FIFO) behavior. However, the application needs additional features to handle more advanced scenarios, and you are required to implement a custom class RideQueue to meet these requirements.

#### Requirements:

Your `RideQueue` class should start with the following standard queue operations:

- `enqueue(item)` – Adds a new ride request to the queue.
- `dequeue()` – Removes and returns the ride request that has been in the queue the longest.
- `is_empty()` – Returns `True` if the queue is empty, `False` otherwise.
- `peek()` – Returns the ride request that is next in line without removing it from the queue.

Then paste the example code from below into your program. Start testing and then also implement the following features for the class:

To meet the needs of the ride-hailing application, your queue must provide the following custom behaviors:

- **VIP Ride Requests**:
    Sometimes, the system receives VIP ride requests that must be prioritized. When a VIP ride request is added to the queue using `enqueue_vip(item)`, it should be placed at the front of the queue, before any regular ride requests.

- **Cancel a Ride Request**:
    Ride requests can be canceled before they are dispatched. Implement a method `cancel_request(item)` that removes a specific ride request from the queue (either regular or VIP). The method should return `True` if the request was found and canceled, and `False` otherwise.

- **Waiting Time Calculation**:
    Implement a method `waiting_time(position)` that returns the number of ride requests a customer has to wait through before their request is dispatched. This will depend on their position in the queue (the first ride in the queue has a waiting time of 0).

- **Limit Queue Size**:
    The queue has a maximum capacity, and once full, new requests cannot be added unless space becomes available (via a dequeue or cancellation). Implement a parameter for the initializer called `max_size` that allows the user to set the maximum size of the queue. If the queue is full, `enqueue` should return False, else True.

#### Class Definition:

Ride requests are represented as simple strings like "Ride1", "VIP_Ride1".

Class `RideQueue` should have the following methods:

- `__init__(self, max_size)`
- `enqueue(self, item)`
- `enqueue_vip(self, item)`
- `dequeue(self)`
- `cancel_request(self, item)`
- `is_empty(self)`
- `peek(self)`
- `waiting_time(self, position)`

#### Example Usage:

    queue = RideQueue(5)
    queue.enqueue("Ride1")
    queue.enqueue("Ride2")
    queue.enqueue_vip("VIP_Ride1")
    queue.enqueue("Ride3")

    # Queue is now ["VIP_Ride1", "Ride1", "Ride2", "Ride3"]
    print(queue.peek())  # Output: "VIP_Ride1"
    queue.dequeue()      # Dispatches "VIP_Ride1"
    print(queue.waiting_time("Ride2"))  # Output: 1 (because Ride2 is next after Ride1)
    queue.cancel_request("Ride2") # Cancels "Ride2"
    print(queue.is_empty())       # Output: False

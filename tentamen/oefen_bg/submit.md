[Ga naar de tentamen-editor](https://pyprog.proglab.nl/exams)

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

```python
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
```

## Constraints:

- The ride requests are simple strings representing customer IDs (e.g., "Ride1", "VIP_Ride1").
- You must handle edge cases, such as trying to dequeue from an empty queue or adding a ride request when the queue is full.

# Holiday Costs

You're looking to go on a holiday on your own, but that's no cheap endeavour
The costs of the trip and the stay depend on the amount of kilometers you have to travel and how long you will be staying at your destination. You're traveling by car and that costs 13 cents per kilometer. Besides those costs, a night at your chosen destination is going to cost 60 euros per night.

## Assignment

Implement, in a file named `vakantie.py`, a program that calculates how much your vacation will cost based on the distance you're traveling and the number of days you will need to book. The total costs for your vacation is the sum of traveling costs and the booking costs of your stay. We'll be expressing our results in whole euro's, so be sure to round your calculations to the nearest integer. 
You may assume that all input in the program are valid values.

## Code

For this assignment your code will consist of two self-written functions.

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def travel_costs(km: int) -> int:
        """
        Determine the costs of travel based on the distance to the destination.
        """

    def overnight_costs(nights: int) -> int:
        """
        Determine the costs of staying overnight based on the number of nights you stay at your destination.
        """

    <Write code here that prompts the user for input and prints the total cost of they vacation>

## Tips

* Remember to correctly calculate `travel_costs(km)` for a round-trip even though the function only receives km for a one way trip!
* Make sure your functions round the result of their calculations to the nearest integer before returning.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python vakantie.py
    How far are you traveling in kilometers? 1250
    How many nights will you book? 5
    Your vacation will cost: 625

    $ python vakantie.py
    How far are you traveling in kilometers? 800
    How many nights will you book? 10
    Your vacation will cost: 808

    $ python vakantie.py
    How far are you traveling in kilometers? 2159
    How many nights will you book? 12
    Your vacation will cost: 1281

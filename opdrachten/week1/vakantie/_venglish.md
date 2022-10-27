# Holiday Costs

You're looking to go on a holiday on your own, but that's no cheap
endeavour The costs of the trip and the stay depend on the amount of
kilometers you have to travel and how long you will be staying at your
destination.

## Assignment

Implement, in a file named `vakantie.py`, a program that calculates
how much your vacation will cost. The transport costs are 13 cents per
kilometers for both the outward and return journey. The accommodation
costs are 60 euros per night. The total cost should be rounded to the
nearest whole euro.

## Code

For this assignment your code will consist of three self-written functions.

Design your program as described below.
Complete the docstrings with example calls and return values (step three from the function design recipe), and any other explanations as needed.
Finally, write some code that asks for input and calls the function.

    def travel_costs(km: int) -> float:
        """
        Determines the costs of travel based on the distance to the destination.
        """

    def overnight_costs(nights: int) -> float:
        """
        Determines the costs of staying overnight based on the number of nights you stay at your destination.
        """
        
    def total_costs(km: int, nights: int) -> int:
        """
        Determines the total costs of travel based on distance and number of nights and round to whole euros.
        """
        
    <Write code here that prompts the user for input and prints the total cost of they vacation>

## Tips

* Remember to correctly calculate `travel_costs(km)` for a round-trip even though the function only receives km for a one way trip!
* Make sure the final cost calculation is rounded so that your output is an integer.

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

## Submit

You can submit your solution at the bottom of this page. After a few minutes you'll find on the [progress page](/submissions) a button to view the results of the automatic checks. If there are still errors, please fix them and submit again.

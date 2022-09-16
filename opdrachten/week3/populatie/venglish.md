# Population Growth

> Please note: the checks for this assignment will be available on Wednesday at the latest. Do not submit your solution before that time.

Imagine a population of `n` llamas. Each year `n / 3` new llamas are born, but also each year `n / 4` llamas die off. 
That means if we start with `n = 1200` llamas, in the first year `1200 / 3 = 400` new llamas are born and `1200 / 4 = 300` llamas die by the end of that year.
Ultimately at the end of the year `1200 + 400 - 300 = 1300` llamas exist in the ecosystem, a growth of 100 llamas!

Another example is if we start out with `n = 1000` llamas. Then by the end of the year we'd `1000 / 3 = 333.33` new llamas. But because we can only have whole llamas, we round this down to `333` new llamas.
That same year `100 / 4 = 250` llamas would die, so we end with `1000 + 333 - 250 = 1083` llamas at the end of the year. So this year the population grew by only `83` llamas.

Using the same two formulas we can calculate the amount of years it takes to grow our starting population of `n` llamas to a target population of `m` llamas.

## Assignment

Implement, in a file called `populatie.py`, a program that calculates the number of years it takes to grow from a starting population into a target population, or over that exact amount.
Both starting population and target population should be provided as input by the user.

* The program is supposed to prompt the user for start and target population sizes:
    * The starting population has to be larger or equal to 9 (or else the growth would stabilize too quickly). If the user provides a value that is not an integer or is a value lesser than 9, the user should be prompted for a new number.
    * The target population should be greater than the starting population. Again the user has to be prompted for a valid input if they provide an invalid value.
* when the number of years that it takes to reach the target population is not a whole number, round that number to the nearest higher whole number.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def calculate_years(start_size: int, end_size: int) -> int:
        """
        Returns the number of year it takes for the population to
        reach end_size.
        """

    if __name__ == '__main__':
        <Main program>

## Hint

This program is called a "discrete simulation". Discrete means that the simulation makes calculations ins `steps`; in our case they are steps of 1 year. You will grow (or shrink) the population each year according to the formulas. Once the population is greater than or equal to the size of the targeted population, you are finished simulating and you know the number of years it takes.

## Examples

Your program should work like the examples below.

      $ python populatie.py
      Starting population: 1200
      Target population: 1300
      Years: 1

      $ python populatie.py
      Starting population: -5
      Starting population: 3
      Starting population: 9
      Target population: 5
      Target population: 18
      Years: 8

      $ python populatie.py
      Starting population: 20
      Target population: 1
      Target population: 10
      Target population: 100
      Years: 20

      $ python populatie.py
      Starting population: 100
      Target population: 1000000
      Years: 115

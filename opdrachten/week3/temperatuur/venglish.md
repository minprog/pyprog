# Temperature Tables

Degrees Celsius and degrees Fahrenheit can be expressed as a function of each other like so `F = (18C + 320) / 10` or the other way around `C = (10F - 320) / 18`. A conversion table can be seen below. This one is based on the temperature in Celsius and goes from 0° through 20°, in intervals of 5 degrees.

|      C |   F|
|-------:|---:|
|      0 |  32|
|      5 |  41|
|     10 |  50|
|     15 |  59|
|     20 |  68|


## Assignment

Implement, in a file called `temperatuur.py`, a program that prompts the user for the measure of temperature: `C` for Celsius, or `F` for Fahrenheit. Then the program should prompt for a starting temperature, the final temperature, and the interval size. After which a pretty table is printed, with the chosen measure of temperature, followed by the temperature in the other measure on each row. Print a row for each temperatures on the interval [starting temperature, final temperature] with steps of `interval size`.

* Your program should not be case sensitive: both `c` and `C` should be interpreted as Celsius.
* The final temperature has to be higher than the starting temperature.
* The interval size has to be a positive whole number.
* Align the numbers (and letters) to the right in each cell of the table.
* All temperatures have to be rounded up to the nearest whole number.

## Code

Your program should work like the examples below.

    def convert_temperature(old_type: str, old_temp: str) -> int:
        """
        Converts the temparture (old_temp) of old_type to a temperature
        in the new type.
        """

    def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int):
        """
        Pretty prints the conversion table.
        """

    if __name__ == '__main__':
        <Main program>

## Tips

* To align numbers there are different techniques at your disposal. Think of `str.format()` to convert numbers to strings, or use `str.rjust()`. You can also [use f-strings](https://peps.python.org/pep-0498/) to accomplish this.

* We assume that there are no temperatures that exceed 999 degrees. That means you only need to reserve room for 3 digits in the cells of your table, just like the examples below.

## Examples

Your program should work like the examples below.

    $ python temperatuur.py
    Which measure of temperature (C or F)? C
    What is the starting temperature? 0
    What is the final temperature? 20
    What is the interval size? 5
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68

    $ python temperatuur.py
    Which measure of temperature (C or F)? F
    What is the starting temperature? 0
    What is the final temperature? 10
    What is the interval size? 2
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12

    $ python temperatuur.py
    Which measure of temperature (C or F)? F
    What is the starting temperature? 0
    What is the final temperature? 10
    What is the interval size? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

    $ python temperatuur.py
    Which measure of temperature (C or F)? F
    What is the starting temperature? 100
    What is the final temperature? 0
    What is the interval size? 3
      F |   C

    $ python temperatuur.py
    Which measure of temperature (C or F)? v
    Which measure of temperature (C or F)? F
    What is the starting temperature? 0
    What is the final temperature? 9
    What is the interval size? -3
    What is the interval size? 0
    What is the interval size? 3
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12

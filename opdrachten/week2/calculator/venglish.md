# Calculator

By now we have seen that Python understands mathematical formulas and can calculate their results for us. Let's use that computer power to quickly provide users with results from sums they think of themselves.
To that end we'll write a program that prompts the user to input a formula, for which Python will compute the result.

## Opdracht

Implement, in a file named `calc.py`, a program that prompts the user to input a formula and then outputs the correct result for that formula.

* The formula that is input by the user should be of the form `x y z` with a space between each of the `x`, `y`, and `z`.
* `x` and `z` should be integers and `y` is one of the following operators: `+`, `-`, `*`, `/`.
* You may assume that the user will not input a 0 (zero) for `z` if the operator is chosen as `/`.
* The output of the program should be the `float` type.
* Your program should also work for negative numbers.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def get_values(expression: str):
        """
        Get values for x, y, and z from `expression`. 
        `x` and `z` are returned as integers and `y` as a single character string.
        """

    def calculate(x: int, y: str, z: int) -> float:
        """
        Calculate the result of the expression based on the values of x, y and z.
        The result is returned as a float.
        """

    if __name__ == '__main__':
        <input, functions, output>

## Tips

* The numbers in the expression can consist of multiple digits (i.e. 135). Think carefully how to split the expression in such a way that numbers of any order can be processed.
* You can unpack multiple values from a string by using the split() function to split the string on a known delimiter; `a, b = "hello world!".split(" ")`. Note that the string is being split at any 'space' character and the number of variables you unpack has to match the resulting split.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python wiskunde_verwerker.py
    1 + 1
    2.0

    $ python wiskunde_verwerker.py
    100 - 9
    81.0

    $ python wiskunde_verwerker.py
    4 * 6
    24.0

    $ python wiskunde_verwerker.py
    3 / 8
    0.325

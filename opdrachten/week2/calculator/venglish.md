# Calculator

By now we have seen that Python understands mathematical formulas and can calculate their results for us. Let's use that computer power to quickly provide users with results from sums they think of themselves.
To that end we'll write a program that prompts the user to input a formula, for which Python will compute the result.

## Opdracht

Implement, in a file named `calculator.py`, a program that prompts the user to input a formula and then outputs the correct result for that formula.

* The formula that is input by the user should be of the form `x y z` with a space between each of the `x`, `y`, and `z`.
* `x` and `z` should be integers and `y` is one of the following operators: `+`, `-`, `*`, `/`.
* You may assume that the user will not input a 0 (zero) for `z` if the operator is chosen as `/`.
* The output of the program should be the `float` type.
* Your program should also work for negative numbers.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def perform_operation(x: int, y: str, z: int) -> float:
        """
        Calculate the result of operation y performed on x and z.
        The result is returned as a float.
        """

    def evaluate(formula: str) -> float:
        """
        Calculate the result of a formula that is found in a string.
        The result is returned as a float.
        """

    if __name__ == '__main__':
        <Input, functions, output>

## Tips

* You can use the split-method just like in the Meal-time assignment. Experiment a little using `split` in Python to develop your idea for a solution.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python calculator.py
    1 + 1
    2.0

    $ python calculator.py
    100 - 9
    81.0

    $ python calculator.py
    4 * 6
    24.0

    $ python calculator.py
    3 / 8
    0.325

# camelCase or snake_case?

In general, snake_case is used for naming variables or functions in Python, where a `_` separates the individual words. Some people prefer using camelCase, where the very first letter is lower case, and the first letter of each new word is upper case. This ensures the words within the name are distinguishable.

Camelcase would lead to names such as `check`, `convertInput`, or `readFromFile`. However in Python it is convention to use `snake_case`. That is why we are going to write a program to convert any name into that format.


## Assignment

Write, in a file named `camel.py`, a program which converts the string format from camelCase to snake_case.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def convert(name: str) -> str:
        """
        Convert a name from camelCase to snake_case
        """

    if __name__ == '__main__':
        Prompt the user for a name, call your function, and print the result.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python camel.py
    camelCase: check
    snake_case: check

    $ python camel.py
    camelCase: convertInput
    snake_case: convert_input

    $ python camel.py
    camelCase: readFromFile
    snake_case: read_from_file

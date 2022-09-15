# Coke-machine

Image you are the thirstiest you have ever been, and you want to buy a bottle of coke from the vending machine. The machine in front of you sells bottles for 50ct a piece, and only accepts coins of 25, 10, and 5 cents.
You could just put some coins in the machine without giving it much thought, but you are way too thirsty to think straight and you want to be sure you get the right amount of change back.
This is of course the perfect reason to write a program to mimic the vending machine, that tells you which coins you could insert into the machine, and how much change you should be given back.

## Assignment
Write, in a file named `cola.py`, a program which prompts the user to insert a coin (one at the time), and prints the remaining price each time.
The program has to print the amount of change if at least 50ct is paid, so that you pay too much money for a bottle.

* You may assume that the user only enters integers
* The machine only accepts coins of 25, 10 and 5 cents, so ensure other amounts are not accepted.

## Code

For this assignment you are going to write your own function, as before. Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.


    def check_coin(coin: int) -> bool:
        """
        Checks if a coin is accepted.
        """

    def determine_due(coin: int) -> bool:
        """
        Determines the due ammount after a coin is inserted. Inserted coin must be valid.
        """

    def prompt_coin(due: int) -> int:
        """
        Keeps asking the user to insert coins until the due amount is reached. Output is amount of change.
        """

    if __name__ == '__main__':
        Prompt the user for an answer, call your function, and print the result.

## Tips

* The user must repeatedly insert coins, and be prompted to do so. This can be nicely done by using a loop. We have the final condition, so which type of loop fits best?
* Some functions don't have to be called in the `if __name__ == '__main__'`. The function `check_coin` is only used from within the other functions.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python cola.py
    Cash due: 50
    Insert coin: 25
    Cash due: 25
    Insert coin: 25
    Change: 0

    $ python cola.py
    Cash due: 50
    Insert coin: 10
    Cash due: 40
    Insert coin: 25
    Cash due: 15
    Insert coin: 25
    Change: 10

    $ python cola.py
    Cash due: 50
    Insert coin: 10
    Cash due: 40
    Insert coin: 30
    Cash due: 40
    Insert coin: 25
    Cash due: 15
    Insert coin: 5
    Cash due: 10
    Insert coin: 10
    Change: 0

# Coke-machine

> Please note: the checks for this assignment will be available on Wednesday at the latest. Do not submit your solution before that time.

Imagine that you are thirstier than you have ever been, and you would like to buy a bottle of coke from the vending machine. The machine in front of you sells bottles for 50ct a piece, and it only accepts coins of 25, 10 and 5 cents.
You could just put some coins in the machine without giving it much thought, but you are way too thirsty to think straight and you want to be sure you get the right amount of change back.
This is a perfect reason to write a program to mimic the vending machine, that will tell you which coins to insert into the machine, and how much change you should then be given back.

## Assignment

Write, in a file named `cola.py`, a program which prompts the user to insert a coin (one at the time), and prints the remaining price each time.
When enough coins have been inserted, the program should print the amount of change that is returned making the amount paid exactly 50 cents.

* You may assume that the user only enters integers

* Ensure that coins other than 25, 10 and 5 cents are not accepted.

## Code

Design your program as described below. Complete the docstrings with doctests and any additional explanations.

    def check_coin(coin: int) -> bool:
        """
        Checks if a coin is accepted.
        """

    def determine_due(due: int, coin: int) -> bool:
        """
        Determines the due ammount after a coin is inserted. Inserted
        coin must be valid.
        """

    def prompt_coin(due: int) -> int:
        """
        Keeps asking the user to insert coins until the due amount is
        reached. Output is amount of change.
        """

    if __name__ == '__main__':
        <Main program>

## Tips

* The user should insert multiple coins. This can be nicely done by using a loop. We have a final condition to keep track of, so which type of loop fits best?

* Some functions don't have to be called in the `if __name__ == '__main__'`. The function `check_coin` is only called from the other two functions.

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

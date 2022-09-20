# The Guessing Game

"Guess a number under ten" is perhaps one of the most played games by children to come to a choice. It is however a game that requires at least two people: the person who knows the number and the person who has to guess the number.
Imagine you would like to play this game by yourself, then a computer is your perfect match! But why stop at 10? You could play this game for numbers under 100, or even 5843!

## Assignment

Implement, in a file called `raadspel.py`, a program that prompts the user to guess a number between 1 and a number of their choice.
Keep prompting for numbers until the user has chosen the correct number.

* First prompt the user for a `level`, if a negative number is provided (or 0), prompt for a new value for the `level`.
* Generate a number between 1 and the `level` the user has to then guess. The number 1 and the provided `level` are included in available numbers.
* Give the user some feedback after they guess. Feedback you can give:
    * `Your guess is too high!`
    * `Your guess is too low!`
    * `You guessed right, congratulations!`
* You cannot assume the input from the user are valid values. That means you have to check for validity and prompt for a new `level` or guess when a value is not valid.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def check_guess(guess: int, number: int) -> bool:
        """
        Check if the guess is valid, if the guess is invalid return 
        False and print some feedback.
        """

    def decide_number(level: int) -> int:
        """
        Return a random number between 1 and level.
        """

    if __name__ == '__main__':
        <Prompt the user for a (valid) level, choose a number, and let the user guess numbers until correct.>

## Tips

* You have to keep letting the user guess for as long as necessary, but every guess by the user has to be a valid number. This might mean you have to nest a loop inside a loop.

## Examples

Your program should work like the examples below.

    $ python raadspel.py
    Level: 10
    Guess: 3
    Your guess is too low!
    Guess: 7
    Your guess is too high!
    Guess: 6
    You guessed right, congratulations!

    $ python raadspel.py
    Level: 1
    Guess: 1
    You guessed right, congratulations!

    $ python raadspel.py
    Level: -5
    Level: Kat
    Level: 27
    Guess: 30
    Guess: Hond
    Guess: 13
    Your guess is too high!
    Guess: 8
    You guessed right, congratulations!

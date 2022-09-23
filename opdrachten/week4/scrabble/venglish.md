# Scrabble

In the game of Scrabble players create words from letters to generate points. The number of points that each letter is worth is summarized in the following table. The sum of all letter points makes the word score.

| **A** | **B** | **C** | **D** | **E** | **F** | **G** | **H** | **I** | **J** | **K** | **L** | **M** | **N** | **O** | **P** | **Q** | **R** | **S** | **T** | **U** | **V** | **W** | **X** | **Y** | **Z** |
|:-----:|:-----:|:-----:|:-----:|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|   1   |   3   |   3   |   2   | 1     | 4     | 2     | 4     | 1     | 8     | 5     | 1     | 3     | 1     | 1     | 3     | 10    | 1     | 1     | 1     | 1     | 4     | 4     | 8     | 4     | 10    |

Say that we made the word `code`, this would make a Scrabble score of `3 + 1 + 2 + 1 = 7`.

## Assignment

Write in a file called `scrabble.py` a program that asks two players to enter a word. The program is then to decide which of the players has won: this would be the player who created the word yielding the highest number of points. Upper and lower case letters may be used interchangeable and do not influence the score further. Also note that characters could be used that are not letters (in the sense of the table above). Make sure to ignore these characters in your calculations.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanations about the approach that you chose.

For this assignment you are encouraged to create additional functions to solve a small part of the problem. These functions should then also have types and doctests.

    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    def compute_score(word: str) -> int:
        """
        Bereken en return de score voor het woord.
        """

    if __name__ == '__main__':
        <Main program>

## Hints

* In the code you will find a variable called `POINTS`. This is a global variable. We introduce this variable because its contents are a static part of the game logic. You can use it anywhere in the code.

* To easily generate a string of alphabetic characters you can use the module `string`. See the [manual](https://docs.python.org/3/library/string.html) for further information.

## Examples

Your programs must eventually behave exactly like the examples below.

    $ python scrabble.py
    Player 1: Apenkoppen
    Player 2: Bananenbroodje
    Player 2 wins!

    $ python scrabble.py
    Player 1: cat
    Player 2: dog
    Gelijkspel!

    $ python scrabble.py
    Player 1: Hardly?
    Player 2: Hardly!
    Gelijkspel!

    $ python scrabble.py
    Player 1: Hello
    Player 2: Bye
    It's a tie!

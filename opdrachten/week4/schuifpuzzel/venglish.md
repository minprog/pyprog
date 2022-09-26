# Tiles

Tiles is a puzzle played on a square, two-dimensional board with numbered tiles that slide. Most often, the puzzle has 15 tiles.
The goal of this puzzle is to arrange the board's tiles from smallest to largest, left to right, top to bottom, with an empty space in board’s bottom-right corner, as in the below.

![correct_config](tiles1.png){: style="width:20rem;"}

Sliding any tile that borders the board’s empty space in that space constitutes a "move." Although the configuration above depicts a game already won, notice how the tile numbered 12 or the tile numbered 15 could be slid into the empty space. Tiles may not be moved diagonally, though, or forcibly removed from the board.

Although other configurations are possible, we shall assume that this game begins with the board’s tiles in reverse order, from largest to smallest, left to right, top to bottom, with an empty space in the board's bottom-right corner. If, however, and only if the board contains an odd number of tiles (i.e., the height and width of the board are even), the positions of tiles numbered 1 and 2 must be swapped, as in the below. The puzzle is solvable from this configuration.

![start_config](tiles2.png){: style="width:20rem;"}

## Assignment

Write, in a file called `schuifpuzzel.py`, a program that allows a player to solve a tile game.

* The tile game always uses the 4 × 4 format.

* The solvable starting configuration is like described above.

* Keep prompting the player to move another tile. Should the player choose a tile that can't be moved, let them choose another tile. You may assume that your player enters valid tile numbers.

* The puzzle is solved when all tiles are sorted in ascending order like described above.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanations about the approach that you chose. The main program has already been provided and should not be changed.

For this assignment you are again encouraged to create additional functions to solve a small part of the problem. Those functions should then also have types and doctests.

    Board = list[list[int]]

    def is_won(board: Board) -> bool:
        """
        Checks whether the board is in a winning configuration. Returns True
        if so, and False otherwise.
        """

    def move_tile(board: Board, tile: int) -> bool:
        """
        If the tile is in a movable position: move the tile to the empty
        spot and return True. If the tile is not movable, do not change the
        board and just return False.
        """

    def print_board(board: Board) -> None:
        """
        Print all rows of the board. The format is like in the examples at
        the bottom of the assignment.
        """

    def create_board() -> Board:
        """
        Initialises a board of dimensions 4 x 4. Sorts the numbers in descending
        order, while exchanging the tiles 1 and 2.
        """

    if __name__ == '__main__':
        print("Welcome to Tiles!")
        board = create_board()
        while not is_won(board):
            print_board(board)
            tile = input("Tile to move: ")
            valid = move_tile(board, int(tile))
            if not valid:
                print("That tile can't be moved.")
        print("Congratulations, you have solved the puzzle!")

## Hint

* Atop the program we declare a type named `Board`. Note that this is actually a list of lists with integers in them.

    * Note: we use `list` with a lower case L. In the book you have seen that you should declare a "list of something" using `List[something]` but this is now considered "old" syntax. The advantage here is that it saves you an `import` statement.

    * Do you use the old Python 3.7 of 3.8? Then use `Board = List[List[int]]` with capital L's.

* For the board in this program this will be 4 lists of length 4. When you create the board it thus makes sense to create lists for each line of the board and put all of these into a list. The empty tile will be represented by the number 0.

* For `move_tile()` you will need to know which row and column is occupied by the chosen tile, so you kan check if the tile might be moved to the north, south, west or east directions (or not at all). This means that the tile must either be in the same row or the same column as the empty tile. What else do you need to check?

* For `is_won()` you will need to check whether the board is in the expected winning configuration. Because the orde must be ascending, you could use a counter variable and "walk through" the board using two `for`-loops.

* When you would like to print multiple times after each other (on a single line) you need to change the behaviour of `print` to not add ENTER or newline at the end. You can do that like this: `print(number, end="")`. Adding `end=""` as an argument to `print` will eliminate the newline.

## Examples

Your program should eventually behave exactly like in the example below.

    $ python schuifpuzzel.py
    Welcome to Tiles!
     15 14 13 12
     11 10  9  8
      7  6  5  4
      3  1  2  0
    Tile to move: 4
     15 14 13 12
     11 10  9  8
      7  6  5  0
      3  1  2  4
    Tile to move: 5
     15 14 13 12
     11 10  9  8
      7  6  0  5
      3  1  2  4
    Tile to move: 1
    That tile can't be moved.
     15 14 13 12
     11 10  9  8
      7  6  0  5
      3  1  2  4
    Tile to move: 6
     15 14 13 12
     11 10  9  8
      7  0  6  5
      3  1  2  4
    Tile to move:
    ...
    ...
    ...
      1  2  3  4
      5  6  7  8
      9 10 11  0
     13 14 15 12
    Tile to move: 12
    Congratulations, you have solved the puzzle!

## Testing

You can check your solution using a [text file containing the puzzle's solution](solution.txt). You can pass the solution to your program using the following command:

    python schuifpuzzel.py < solution.txt

The files must be in the same directory for this to work!


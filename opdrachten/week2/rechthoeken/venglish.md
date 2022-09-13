# Identical rectangles

![](rechthoeken.png){: width="415"}

We will be writing a program to determine whether two rectangles are of identical dimensions.
Looking at the example above, you can see that the rectangles do indeed seem to be identical.
We can check this better if we have the exact coordinates of the rectangles.

In this case we do have some data, like the position of the *left side* of A (Ax1) and the *right side* of A (Ax2).
When we subtract these two, the result is one of the dimensions of A.

    Ax2 - Ax1 = 7

Using Ay1 and Ay2 we can calculate the other side of that rectangle.
Then we can calculate the sides of rectangle B. Are the sides equal indeed?

## Assignment

    $ python rechthoeken.py
    Provide the x coordinates of A: 0,7
    Provide the y-coordinates of A: 0,4
    Provide the x-coordinates of B: 6,13
    Provide the y-coordinates of B: 2,6
    The rectangles are identical!

Write, in a file names `rechthoeken.py`, a program that calculates on the basis of the provided coordinates whether the rectangles have identical dimensions.
In addition, it is possible that the rectangles are also *square* and of identical dimensions, and in that case it must also be noted in the output.
If there's not much interesting going on with the rectangles, that fact is what is printed as a result.
You may assume that the use inputs pairs of two integers. Given the example above, the user would mean that Ax1 = 0 and Ax2 = 7.

## Code

You will write a main program that asks for input and tidies it for further use. In addition there are three helper functions that you will use from the main program.

As you can see, there are two TODOs in the code. The functions are supposed to return a single value that signifies whether the check passed or not (e.g. it is square, or it isn't). What datatype fits perfectly for returning pass/fail information?

    def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> TODO:
        """
        Checks whether the lengths of the sides are equal
        """

    def is_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> TODO:
        """
        Checks whether the rectangles are (identical) squares
        """

    def calculate_length(c1: int, c2: int) -> int:
        """
        Calculates the length of a side from two coordinates
        """

    if __name__ == '__main__':
        <Main program>

## Hints

- You can't perform calculations on strings, so one step of tidying your data is to convert the inputs into integers.

- For the function `calculate_length` you don't know in advance which coordinate is larger (think of the case: c1 = 5, c2 = 3). Ensure that the function's output is always positive. You can write some code for this yourself or make use of a standard Python-function.

## Examples

Ultimately, your program should work as demonstrated below.

    $ python rechthoeken.py
    Provide the x coordinates of A: 0,7
    Provide the y-coordinates of A: 0,4
    Provide the x-coordinates of B: 6,13
    Provide the y-coordinates of B: 2,6
    The rectangles are identical!

    $ python rechthoeken.py
    Provide the x coordinates of A:0,7       
    Provide the y-coordinates of A:0,7
    Provide the x-coordinates of B:6,13
    Provide the y-coordinates of B:2,9
    The rectangles are identical!
    And they're square, too!

    $ python rechthoeken.py
    Provide the x coordinates of A:0,7
    Provide the y-coordinates of A:0,7
    Provide the x-coordinates of B:6,15
    Provide the y-coordinates of B:2,9
    Nothing to report :(

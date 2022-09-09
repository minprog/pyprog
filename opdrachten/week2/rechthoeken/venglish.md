# Identical rectangles

![](rechthoeken.png){: width="415"}

We will be writing a program to determine whether two rectangles are of identical dimensions.
Looking at the example above, you can see that the rectangles do indeed seem to be identical.
We can check this better if we have the exact coordinates of the rectangles.
In this case we do have some data, like the position of the *left side* of A (Ax1) and the *right side* of A (Ax2).
When we subtract these two, the result is one of the dimensions of A.
Using Ay1 and Ay2 we can calculate the other dimension.
Then we can calculate the sides of rectangle B.

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

As you can see, there are two TODOs in the code; here you must come up with the type of the function yourself.

    def gelijk(Ax: int, Ay: int, Bx: int, By: int) -> TODO:
        """
        Controleert of de zijdes gelijk zijn
        """

    def vierkant(Ax: int, Ay: int, Bx: int, By: int) -> TODO:
        """
        Controleert of beide rechthoeken hetzelfde vierkant zijn
        """

    def lengte(c1: int, c2: int) -> int:
        """
        Berekent de lengte van een zijde op basis van twee coördinaten
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Hints

You can't perform calculations on strings, so one step of tidying your data is to convert the inputs into integers.

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

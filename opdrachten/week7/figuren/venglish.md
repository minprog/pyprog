# Shapes

> Correctly implementing this assignment with decent doctests and type hints, and a good style, will yield 2 points for this module.

A traditional subject of object oriented programming is modelling shapes. You might define classes for rectangles, triangles and circles, and then make individual instances. In this assignment we will design a couple of classes and use these to *sort various shape instances by surface area*.

As you might know, the surface area is calculated in different ways depending on the specific shape. For example, the areas of squares and circles can be calculated using just a single measure: for a square this is the length of the side, and for a circle this is the radius. Having that information, you just need the right formula.

![](oppervlaktes.png){: style="width:30rem;"}

For other types of shapes you might need more than just a single measure.

## Sorting

Sorting in Python is most commonly done using the standard function `sorted()`. You can provide a list to it and it will yield a completely new list containing the same elements, but sorted:

    >>> sorted([4, 2, 3, 1])
    [1, 2, 3, 4]
    >>> sorted(['z', 'a', 'b'])
    ['a', 'b', 'z']

The sort function contains no specific knowledge on how to sort various items. Instead, it just needs to be able to *compare* elements, which is then used to put everything in order. The only thing that is needed to achieve this, is the less-than operator `<`. It is used repeatedly while sorting a list. As you can see here, `<` is defined not only for integers, but also for strings:

    >>> 1 < 3
    True
    >>> 'b' < 'a'
    False

For our own classes we must provide our own definition of less-than, if we would like to be able to sort instances of that class.

## Preparation

Thoroughly study the book's explanation about inheritance starting on page 290. It is not a long section, but it contains a lot of concepts. Re-read multiple times if needed. You should be able to finish this assignment using the explanation in the book, your previous Python knowledge, and the information in this assignment.

## Classes

Develop the classes for `Square`, `Rectangle`, and `Circle` in a file named `figuren.py`.

*   Each class should have an `__init__()` that receives the parameters that are needed to represent a particular shape (e.g. radius for a circle). And each class should define a method `area()` that calculates and returns the correct surface area.

*   In addition you should define  a `Shape` class that is the parent of the different shape-type classes (using inheritance). This particular class will not contain any methods yet, and does not need an `__init__()`. Make all other classes inherit from the `Shape` class. Also add an *empty* method `area()` so it is clear that dependent classes require this method.

At this point you will have four classes and you can test these by creating a few instances and requesting the area (by calling the `area()` method). You can even make doctests for `area()`, as demonstrated in the book on page 292.

## Implementing less-than

To be able to sort objects, their class must implement `__lt__(self, other)`. This is the method that is run when the `<` operator is used. The method needs to decide, based on the information available, whether an object `self` is smaller than the object `other`:

    def __lt__(self, other):
        ...

When you implement this method for `Shape` it will automatically be available in any inherited classes. You should therefore be able to test whether `Square(2) < Square(1)`.

## Testing code

Create a main program where you instantiate several `Shape`-objects. Put each of these objects into a list. Then print the result of calling `sorted()` on that list. Does it make sense when you run it?

## Representation

The output may actually not make much sense at all at this point. You'll get something like this:

    [<__main__.Square object at 0x10451bbe0>, <__main__.Square object at 0x10451bfa0>]

This is the new list that is (hopefully) sorted, but when `print` receives the `Square` class objects, it prints the type and a memory address. Instead, we would rather be able to inspect the relevant properties of the Square!

So, implement a `__repr__()` method for each of your shape classes. Ideally, the output of `__repr__()` is just what you would call to create a new object. So we're looking for the following:

    >>> squares = [Square(3), Square(2)]
    >>> print(sorted(squares))
    [Square(2), Square(3)]

Experiment with defining `__repr__` until you get it just right!

## Other comparison operators

As stated in the [official documentation](https://docs.python.org/3/library/functions.html#sorted) for `sorted()` it is recommended to always define all of the "rich comparison" operators. Those are the following:

    object.__lt__(self, other)  #-> less than
    object.__le__(self, other)  #-> less than or equal to
    object.__eq__(self, other)  #-> equal to
    object.__ne__(self, other)  #-> not equal to
    object.__gt__(self, other)  #-> greater than
    object.__ge__(self, other)  #-> greater than or equal to

Implement all of these operators for the `Shape` class.

Extra challenge: you have defined less-than `__lt__` earlier. Use your knowledge of logic to define the remaining operators in terms of less-than. For example, less-than-or-equal is equivalent to `self.__lt__(other) or not other.__lt__(self)`. Understand why?

## Positions

When you add a position to each shape it becomes possible to calculate the midpoint-to-midpoint distance between pairs of shapes. Add this idea of *positions* to the `Shape` class. A shape should thus receive (x,y)-coordinates that represent the shape's midpoint (because we will not be drawing the shapes on-screen it does not really matter if it's the midpoint or bottom-left or something else).

*   Add an `__init__()` to `Shape` to receive these coordinates and save them as instance variables.

*   Define a method `distance_to(self, other)` for `Shape` that calculates the distance between two shapes using the Pythagorean theorem:

        math.sqrt((x1-x2)**2 + (y1-y2)**2)

    Where x1, x2, y1 and y2 are the respective coordinaten of the two shapes that we're calculating the distance between. Do not forget to import `math`!

*   Change the `__init__()` for each of the shape classes so they can receive the (x,y)-coordinates in addition to the other measures and call `super().__init__()` like in the examples in the book.

## Final steps

To complete your program, add type hints everywhere and check whether you have written appropriate doctests for all functions and methods.

## Beoordeling

Your program will be automatically checked for doctests and type hints. The functionality of your solution will be manually assessed after the deadline. Make sure that your program adheres to the above requirements and that you make use of the ideas that set out in the assignment.

# Knapsack

> Correctly implementing this assignment with decent doctests and type hints, and a good style, will yield 3 points for this module.

In the "Knapsack" problem there are points to earn for each item that can be packed into an imaginary knapsack. However, there are some limitations to the sack itself: there is a maximum in volume and in weight that can be packed. The total amounts cannot exceed this limit, and thus poses a constraint on which item combinations might be packed. In the following picture a knapsack is shown with its constraints, along with some possible items and their weights and volumes.

![](knapsack.png){: style="width:40rem;"}

The data in the figure is available in the file 
[knapsack_small.csv](knapsack_small.csv). Data for larger knapsack problems
is available in the files
[knapsack_medium.csv](knapsack_medium.csv) and
[knapsack_large.csv](knapsack_large.csv).

The computational goal is to pack a sack with as much value as possible, keeping in mind the constraints.

## Object oriented orogramming

Let's *model* this problem using object oriented programming.
We will define new "types of things" from the problem domain, using classes.
And we will assign the classes some useful instance variables and methods to build the functionality.
The classes that we will use in this problem are `Resources`, `Item` and `Knapsack`.

## Resources

We first define the class `Resources` as:

    class Resources:
        """
        Holds the recources for a Knapsack problem.
        """
    
        def __init__(self, weight, volume):
            """ Creates a resources object with weight and volume. """
            self.weight = weight
            self.volume = volume

        def __repr__(self):
            """ Enables printing """
            return f"weight:{self.weight} volume:{self.volume}"

        def __iadd__(self, other):
            """ Implements '+=' operator. """
            self.weight += other.weight
            self.volume += other.volume
            return self
    
        def __isub__(self, other):
            """ Implements '-=' operator. """
            self.weight -= other.weight
            self.volume -= other.volume
            return self

        def __lt__(self, other):
            """ Implements '<' operator. """
            return self.weight < other.weight and self.volume < other.volume

Using this class as a type in some test code, it becomes possible to add and compare resources:

    r1 = Resources(100, 200)
    r2 = Resources(25, 50)
    r1 += r2
    print(r1)
    print(r2 < r1)

**Assignment.** Copy the class definition and provide one doctest for each of the methods, showing that everything work as expected.

## Items

The `Item` class is a container that connects points and resources.

    class Item:
        """ A Knapsack Item with points and resources. """
    
        def __init__(self, points, resources):
            """ Creates an item object with points and resources. """
            pass
        
        def __repr__(self):
            """ Enables printing. """
            return None

        def get_points(self):
            """ Returns the points. """
            return None

        def get_resources(self):
            """ Returns the resources. """
            return None

This class is not implemented yet.

**Assignment.** Implement this class so it becomes possible to create an `Item`, print it, and retrieve points and resources like so:

    item = Item(20, Resources(100,200))
    print(item)
    print(item.get_points())
    print(item.get_resources())

## Knapsack

Now we can implement a `Knapsack` class.

    class Knapsack:
        """ Knapsack to which Items can be added. Keeps track of points and available resources."""

        def __init__(self,resources):
            """ Creates an empty knapsack with resources. """
            pass
        
        def __repr__(self):
            """ Enables printing. """
            return None

        def item_fits(self,item):
            """ Returns True if item can still be add to the knapsack given 
            the remaing resources, False otherwise. """
            return None
    
        def add_item(self,item):
            """ Adds item to the knapsack and updates resources. """
            pass
        
        def remove_random_item(self):
            """ Removes and returns a random item from the knapsack. 
            Returns None if the knapsack has no items. """
            return None

        def __len__(self):
            """ Implements 'len(knapsack)' function where knapsack is of type Knapsack 
            to return the number of items in knapsack. """
            return None

        def get_points(self):
            """ Returns the points of all items in the knapsack. """
            return None

**Assignment.** Implement the class based on the docstring descriptions. The goal is to be able to run test code like the below:

    knapsack = Knapsack(Resources(100, 200))
    print( knapsack )
    item1 = Item(10, Resources(40, 70))
    knapsack.add_item( item1 )
    item2 = Item(20, Resources(45, 90))
    knapsack.add_item( item2 )
    print( knapsack )
    print( len(knapsack) ) 
    print( knapsack.get_points() )
    print( knapsack.item_fits(item2) )
    item = knapsack.remove_random_item()
    print( knapsack.item_fits(item2) )

## Loading a Knapsack problem

**Assignment.** Create a function that can read Knapsack problem data from a CSV file. Use the following code as a starting point:

    def load_knapsack(filename):
        with open(filename,'r') as file:
            header = file.readline()
            for line in file:
                splits = line.split(',')
                if len(splits)>3:
                    element = splits[0].strip()
                    points = int(splits[1])
                    weight = int(splits[2])
                    volume = int(splits[3])
                    print(f"element:{element} points:{points} weight:{weight} volume:{volume}")

(Notice that this function is not part of a class, but like before, exists separately in the program.)

## Packing

**Assignment.** Write a Knapsack solver in a function like this:

    def solve_knapsack(filename):
        """ Return the highest number of points found when packing the knapsack in file 'filename' """
        return None

The goal is to score as many points as possible from whatever items are available.
A basic algorithm to do this:

*   put all items in a knapsack called `all_items`

*   in random order, move each item to a different knapsack called `knapsack`, as long as it still fits

*   do this many times and keep track of the highest score that you found

Feel free to decompose the solution into further functions.

Test your solution on the `knapsack_small.csv` problem first, and when satisfied with the results, tackle the larger `knapsack_medium.csv` problem.

## Extra: packing better

Come up with a better algorithm to determine the maximum score given a knapsack and some items. One example is to remove items from a knapsack and making space for different items.

What is the highest score you are able to find using the `knapsack_large.csv` problem? Compare your results with those from other students.

## Advantages of object oriented programming

We could have solved the Knapsack problem without using any object oriented programming (so without classes). We might even have needed less code. So what would be the *advantages* of classes then?

### Types from the problem domain

The types (classes) that we defined are closely linked to the problem domain, which makes it easier to reason about the code (this does certainly take some practice, so you might not have noticed this, yet!).

### Encapsulation

*Encapsulation* means that a class hides implementation details in a particular part of the code. You've seen the same principle used with functions; we might use a function without seeing the code and how exactly it is implemented. We just need some documentation and the required types.
But different from functions is that a class can also hide *instance variables*, which means that the object can keep track of things between various method calls (whereas with functions, it is very uncommon that a function "remembers" something from the last time it was called).

A programmer does not even need to know what the types of instance variables are when calling methods. This makes it much easier to change parts of a class without changing any other part of the code. This means that object oriented programming helps you compartimentalize code. Some examples are:

*   The class `Resources` currently has instance variables `weight` and
    `volume`; were we to add any variables inside the class, we could just do that
    without changing the rest of the code.
    
*   In the `Knapsack` class you probably used a list to keep track of items. However, removing random items from a list can be very slow when the list gets long. This isn't helpful when we are trying to solve calculation-intensive problems like the above. For larger 
    knapsack problems it would be wise to use a set instead of a list. And it is perfectly possible to make this (implementation) change in `Knapsack` without changing any other code!

## Finishing up

Don't forget your doctests and add as many type hints as possible.

# Caffeine

With your health in mind, it is important to keep a close watch on your caffeine intake and make sure that it is not too high.
Following is a list of caffeine dosages for a variety of caffeinated beverages.

* Coffee - 90 mg
* Tea - 45 mg
* Energy drinks - 80 mg
* Cola - 40 mg

## Assignment

Implement, in a file named `cafeine.py`, a program that prompts the user to indicate how many caffeinated drinks they drink, that then calculates the total caffeine intake of the user based on their input. 
You may assume the user only enters numbers greater than or equal to zero and never inputs any incorrect values.

## Code

For this assignment your code will consist of a self-written function and calls to a number of functions.
Not only do you have to call your own created function, but also a number of functions already implemented and included in the Python distribution.

Design your program as described below.
Complete the docstrings with example calls and return values (step three from the function design recipe), and any other explanations as needed.
Finally, write some code that asks for input and calls the function.

    def calculate_caffeine(coffee: int, tea: int, energy: int, cola: int) -> int:
        """
        Calculates the amount of caffeine based on the number of consumed beverages
          of either coffee, tea, energy, or cola.
        """

    <Write code here to prompt for input and call the function>

## Tips

* For this assignment you have to write a function, so keep the functional design recipe (FDR) at hand.
* Which built-in Python function should you use to prompt the user?

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python cafeine.py
    How many cups of coffee? 2
    How many cups of tea? 1
    How many energy drinks? 0
    How many glasses of cola? 0
    Your intake is 225 mg of caffeine.

    $ python cafeine.py
    How many cups of coffee? 2
    How many cups of tea? 0
    How many energy drinks? 2
    How many glasses of cola? 0
    Your intake is 340 mg of caffeine.

    $ python cafeine.py
    How many cups of coffee? 0
    How many cups of tea? 0
    How many energy drinks? 0
    How many glasses of cola? 1
    Your intake is 40 mg of caffeine.

    $ python cafeine.py
    How many cups of coffee? 5
    How many cups of tea? 0
    How many energy drinks? 0
    How many glasses of cola? 0
    Your intake is 450 mg of caffeine.

## Submit

You can submit your solution at the bottom of this page. After a few minutes you'll find on the [progress page](/submissions) a button to view the results of the automatic checks. If there are still errors, please fix them and submit again.

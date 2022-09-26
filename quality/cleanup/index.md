# Cleanup

While programming you might (and you will!) stumble upon some unforeseen bugs and tricky edge cases.
In such situations, you will have to rethink your design or approach. It is quite likely that your code file still contains some remnants of your previous approach.

## Dead code

One example is commented-out code or "dead code":

    # x = 8
    # if x > 7:
    #     print("hello!")

This should be removed! If you really would like to keep it, save it in a separate file.

## Unreachable code

A bit more tricky is the condition that is never met, resulting in lines of code that will **never** be reached:

    x = 10
    if x < 10:
        print("bye!")

Or perhaps there is a function that you defined, but do not actually use:

    def why_dont_you_call_me_anymore():
        print("hello?")

You should remove all of these.

## Removing imports

Atop your files you may have imported some module that you once needed, but don't anymore:

    import math

The solution is clear: delete the unused imports!

## Doctest

You might have tested your programs by adding this line to your program:

    doctest.testmod()

However, this is just for you, for testing purposes. It is not part of the assignment and makes the program work differently. So before you hand in, always remove it, along with the associated `import doctest`!

## Learn more

Want to know more about keeping your code tidy? Have a look at this chapter (which is a combination of basic and very advanced suggestions, so beware!):

- Robert Martin, *Clean code: a handbook of agile software craftsmanship*. Chapter 17, *Smells and heuristics*. Pearson Education, 2009.

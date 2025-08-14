# Cleanup

While programming you might (and you will!) stumble upon some unforeseen bugs and tricky edge cases.
In such situations, you will have to rethink your design or approach. It is quite likely that your code file still contains some remnants of your previous approach.

## Commented-out code

You might be tempted to "keep" some old code in comments. For example, if you have written a few lines of code, but you can't use them yet, you might put comment marks around those lines (often, your editor has a shortcut for this).

    # x = 8
    # if x > 7:
    #     print("hello!")

This is called commented-out code. When experimenting, this is a great system, because you can easily revert it. However, be sure to clean up your code from such comments. Your job is to design a nice solution to a problem, and when you design something, you have to make choices. So as soon as you feel you're done, you will need to remove any old parts that you don't need anymore.

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

# Comments

There are multiple reasons that comments make code easier to understand.
One is that time may pass before you look at your code again: hours, days, weeks, months, or even years.
If you then decide you want to reuse some parts of it, or get it going again, you will need a little bit of help understanding.
The code itself is great at telling you every tiny bit of detail, because that is exactly what a programming language has you do.
But that makes code quite verbose and harder to make sense of.
Some annotations, written in a natural language, can carry an amazing amount of information in just a few words, while not needing to hang onto details.
Playing up to the strength of both tools at your disposal, we ask you to write comments next to your code, such that these comments aid you and your fellow programmers in understanding the code better and faster than without.

## Annotations

Here's our advice: add comments to your code that make programmers (including you) understand your code more easily.
Use short annotations to **describe** what a part of your code does at a high level.
And use **clarifying** comments when a part of your code is so complicated, that you need to explain the details of how something is done.
But do not use comments to describe what should already be clear from your code: some lines may not need a comment at all!
On the other hand, if you do feel the need to write multiple sentences of comments for one line of code,
consider splitting up that line instead, or try rethinking your algorithm.

Consistency also plays a part in formatting your comments.
First of all, you should choose the language in which to write them.
It doesn't have to be the same language as your variable names,
but the comments in your programs should all be written in the same natural language.

You do not need to write full sentences including capitals and punctuation,
but you should leave one space between the `#` and your comment's first character, just like this:

    # compute one student's average
    average = sum / QUIZZES + 0.5

In other words, don't do this:

    #compute one student's average
    average = sum / QUIZZES + 0.5

Or this:

    # Compute one student's average.
    average = sum / QUIZZES + 0.5

And as a general rule, you should **not** place comments on the same line as actual code:

    average = sum / QUIZZES + 0.5  # compute one student's average

## How many comments are enough?

Well, ideally, your code is expressed in small functions, with good names, each having only a few variables, again with good names, resulting in code that hardly needs any comment, except for maybe some technical explanations in cases where the code uses a smart trick that is a little bit hard to understand.

However, it is not for the faint of heart to write code that is already so easy to understand that it hardly needs any documentation. So in general, we would recommend that you divide your functions into **blocks** of a few lines of code, each block introduced by a small comment that divulges its purpose. For example:

    # collects and sums all house numbers
    house_numbers = []
    sum_of_nos = 0
    for person in persons:
        house_numbers.append(person.address_no)
        sum_of_nos += person.address_no

    # calculates average of all house numbers
    average_house_no = sum_of_nos / len(house_numbers)

Obvious candidates for adding a comment are any separate `for` and `while` loops, as well as `if` blocks that make decisions. Like above with the `for` loop, you might group it with some of the variables that you need to use inside the loop and then add a comment describing the purpose of the whole block.

## Summaries

Atop your `.py` file you should have multi-line comments
that summarize what your program (or that particular file) does
along with, perhaps, your name and that of the file.

    """
    hello.py

    UvA Programmeren in Python
    Martijn Stegeman

    - Zegt hallo tegen iedereen.
    - Laat zien hoe printen werkt.
    """

Atop each of your function should be multi-line comments
that summarize what your function does along with doctests and other information to
quickly assess its purpose.

    def chorus(bottles: int) -> str:
        """
        Sings about a number of bottles.
        
        >>> chorus(1)
        ...
        >>> chorus(2)
        ...
        """

## Learn more

Want to know more about writing good comments? Have a look at these chapters:

- Robert Martin, *Clean code: a handbook of agile software craftsmanship*. Chapter 4, *Comments*. Pearson Education, 2009.
- Steve McConnell, *Code complete: a practical handbook of software construction*. Chapter 32, *Self-documenting code*. Microsoft Press, 2004.

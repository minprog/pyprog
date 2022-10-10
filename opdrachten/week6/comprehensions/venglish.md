# Comprehensions

In Python we have "comprehensions" that we can use to create a new collection using just a short expression. In this course we will stick to `list` comprehensions, but keep in mind that there are more!

## Create lists

A list comprehension is really just a one-line `for` loop, combined with a special syntax to create a list. This looks like this:

    >>> some_list = [i * 2 for i in range(10)]
    >>> print(some_list)
    [0,2,4,6,8,10,12,14,16,18]

The above makes a brand new list. You should read the list comprehension as follows: for each `i` in `range(10)` put the result of the expression `i*2` in the list. This achieves exactly the same as the following code:

    some_list = []
    for i in range(10):
        some_list.append(i * 2)

You do not necessarily have to use the value `i` when generating the result. In the following comprehension there is still a variable `i`, but it is used only as a counter, used to generate a random number 100 times:

    >>> import random
    >>> random_numbers = [random.random() for i in range(100)]
    >>> print(random_numbers)
    [0.298720086438369, 0.7619029711407771, 0.6239567171981671, ...]

#### Excercise

Write a list comprehension that generates a list of four random letters from the options `'A', 'B', 'C', 'D'`. To choose one random letter, use `random.choice()`. An example of an outcome of this expression could be `['A', 'C', 'A', 'A']`.

> Please enter your answer in the Dutch version :-)

## Conditions

You can add a condition to a list comprehension. The following comprehension specifically relies on the numbers that are "divisible by 2", and multiplies each of those numbers by 3 to generate the new list.

    >>> some_list = [i * 3 for i in range(10) if i % 2 == 0]
    >>> print(some_list)
    >>> [0, 6, 12, 18, 24]

Fully equivalent is the written `for` loop:

    some_list = []
    for i in range(10):
        if i % 2 == 0
            some_list.append(i * 3)

In the above, make sure that you completely understand why the resulting list starts with 0 and ends with 24, even though `range(10)` is used as a starting point.

#### Excercise

Write a list comprehension that uses the first 10 odd numbers to generates "value + 5". This means it should yield ten numbers, starting with `[6, 8, 10, ...]`. Be careful not to generate just 5 numbers!

> Enter your answer in the Dutch version

## From list to list

You can also base list comprehensions on existing lists. In that case we do not use something like `range(10)` to control the loop, but a list. For example:

    >>> vowels = ['a', 'e', ​​'i', 'o', 'u', 'y']
    >>> uppercase_vowels = [vowel.upper() for vowel in vowels]
    >>> print(uppercase_vowels)
    ['A', 'E', 'I', 'O', 'U', 'Y']

Note that it is customary to make a combination of a singular variable name ("vowel") with a plural variable name ("vowels"). The singular then points to the single element being processed.

#### Excercise

Write a list comprehension that is not based on a list but on a *string*. We'll give you a string containing the password `'mo4br99!'` to use as input. Give a list comprehension that, with the help of `isnumeric()`, indicates per character of the password whether it is a number. The result should start with `[False, False, True, ...]`.

> Enter your answer in the Dutch version

## Filter

If you base a comprehension on a list, combined with an `if` statement, we call that a filter. For example:

    >>> numbers = [1, 4, 9, 3, 2, 5, 10, 6]
    >>> even_numbers = [number for number in numbers if number % 2 == 0]
    >>> print(even_numbers)
    [4, 2, 10, 6]

This is where list comprehensions can be very useful to get a lot done with very little code. And such expressions are often more readable than a large `for` loop! So if you're writing a `for` loop to filter a list, consider whether you can simplify this with a list comprehension.

Mind you, you can go too far. For example, you can write multidimensional list comprehensions with all kinds of conditions. At a certain point you have to ask yourself whether it is as manageable as a normal `for` loop!

We do not consider this a good example of using list comprehensions:

    >>> dont_do_this_at_home = [[a * b for a in range(10) for b in range(5) if a > b] for i in range(3)]

#### Excercise

Write a list comprehension that returns all digits in the password `'mo4br99!'`.

> Enter your answer in the Dutch version

## Generate Strings

Note that although the base of a comprehension can be a string, a comprehension will always return a *list*. Generating strings directly using a comprehension is not possible in Python. However, with a small additional step you can do it:

    >>> ['a' for i in range(4)]
    ['a', 'a', 'a', 'a']
    >>> ''.join(['a' for i in range(4)])
    'aaaa'

This can come in handy sometimes!

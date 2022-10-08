# Comprehensions

> This version has been automatically translated and will be reviewed for errors on Monday.

In Python there are "comprehensions" with which you can create a new collection using a short expression. In this course we will stick to `list` comprehensions, but keep in mind that there are more!

## Create lists

A list comprehension is really just a one-line `for` loop, combined with a special syntax to create a list. This looks like this:

    >>> some_list = [i * 2 for i in range(10)]
    >>> print(some_list)
    [0,2,4,6,8,10,12,14,16,18]

The above makes a brand new list. You read the list comprehension as follows: for each `i` in `range(10)` put the result of the expression `i*2` in the list. So it is a very compact syntax to achieve the following:

    some_list = []
    for i in range(10):
        some_list.append(i * 2)

You do not necessarily have to use the value `i` when generating the result. In the following comprehension we use `i` purely as a counter, so that we can generate a random number 100 times:

    >>> import random
    >>> random_numbers = [random.random() for i in range(100)]
    >>> print(random_numbers)
    [0.298720086438369, 0.7619029711407771, 0.6239567171981671, ...]

#### Excercise

Write a list comprehension that generates a list of four random letters from the options `'A', 'B', 'C', 'D'`. To do this, use `random.choice()`. So a completely random outcome could be `['A', 'C', 'A', 'A']`.

> Enter your answer in the Dutch version

## Conditions

You can process a condition in a list comprehension. The following comprehension specifically relies on the numbers that are divisible by 2, and multiplies each of those numbers by 3 to generate the new list.

    >>> some_list = [i * 3 for i in range(10) if i % 2 == 0]
    >>> print(some_list)
    >>> [0, 6, 12, 18, 24]

Fully equivalent is the written `for` loop:

    some_list = []
    for i in range(10):
        if i % 2 == 0
            some_list.append(i * 3)

#### Excercise

Write a list comprehension that generates a "value + 5" from 10 odd numbers. So that should yield ten numbers that start with `[6, 8, 10, ...]`. Be careful not to generate just 5 numbers!

> Enter your answer in the Dutch version

## From list to list

You can also base list comprehensions on existing lists. Then we don't use `range(10)` to control the loop, but a list. For example:

    >>> vowels = ['a', 'e', ​​'i', 'o', 'u', 'y']
    >>> uppercase_vowels = [vowel.upper() for vowel in vowels]
    >>> print(uppercase_vowels)
    ['A', 'E', 'I', 'O', 'U', 'Y']

Note that it is customary to make such a combination of singular ("vowel") and plural ("vowels") for the variables. The singular then points to the single element being processed.

#### Excercise

Write a list comprehension that is not based on a list but on a *string*. We'll give you a password string `'mo4br99!'` to use as input. Give a list comprehension that, with the help of `isnumeric()`, indicates per character of the password whether it is a number. The result would start with `[False, False, True, ...]`.

> Enter your answer in the Dutch version

## Filter

If you base a comprehension on a list, combined with an `if` statement, we call that a filter. For example:

    >>> numbers = [1,4,9,3,2,5,10,6]
    >>> even_numbers = [number for number in numbers if number % 2 == 0]
    >>> print(even_numbers)
    [4, 2, 10, 6]

List comprehensions can therefore be very useful for getting a lot done with very little code. They are also often more readable than a large `for` loop! So if you're writing such a `for` loop, consider whether you can simplify this with a list comprehension.

Mind you, you can go very far. For example, you can write multidimensional list comprehensions with all kinds of conditions. At a certain point you have to ask yourself whether it is even more manageable than a normal `for` loop!

    >>> dont_do_this_at_home = [[a * b for a in range(10) for b in range(5) if a > b] for i in range(3)]

#### Excercise

Write a list comprehension that returns all digits in the password `'mo4br99!'`.

> Enter your answer in the Dutch version

## Generate Strings

Note that the base of the comprehensions is sometimes a string, but a comprehension will always return a *list*. Generating strings with a comprehension is not possible in Python. However, with a small extra step you can create a string:

    >>> ['a' for i in range(4)]
    ['a', 'a', 'a', 'a']
    >>> ''.join(['a' for i in range(4)])
    'aaaa'

This can come in handy sometimes!

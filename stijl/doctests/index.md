# Doctests

For every assignment you will write doctests that show, to some extent, that your solution is correct.

## Minimum requirement

Your doctests will be automatically checked upon submission. Every function needs to have an absolute minimum of 2 tests, and every test should work out OK. You can then resubmit until the deadline passes.

Upon submission, the doctests will be automatically run. You can review the results on the Progress page of this website. However, it's much better to run the doctests yourself.

## Running your own doctests

As required by the function design recipe, you can and should try your own doctests.

In the book in chapter 6 you have seen how to do this by including the `doctest` module in your program. However, we also ask you to write full programs that take input and output, which is a bit difficult to combine with doctests.

The simplest way to run doctests is by executing the following command in the terminal:

    python -m doctest -v program.py

Substitute `program.py` by the name of your program, and when needed, `python` by `python3`. Your program should then be fully tested. The output could look like this for the `rechthoeken` program that you wrote earlier:

    Trying:
        calculate_length(0,2)
    Expecting:
        2
    ok
    Trying:
        calculate_length(-2, 2)
    Expecting:
        4
    ok
    Trying:
        calculate_length(8, 0)
    Expecting:
        8
    ok
    Trying:
        is_same_rectangle(7,4,7,4)
    Expecting:
        True
    ok
    Trying:
        is_same_rectangle(3,3,7,4)
    Expecting:
        False
    ok
    Trying:
        is_square(3,3,3,3)
    Expecting:
        True
    ok
    Trying:
        is_square(7,7,2,2)
    Expecting:
        False
    ok
    1 items had no tests:
        rechthoeken
    3 items passed all tests:
       3 tests in rechthoeken.calculate_length
       2 tests in rechthoeken.is_same_rectangle
       2 tests in rechthoeken.is_square
    7 tests in 4 items.
    7 passed and 0 failed.
    Test passed.

Conclusion: each function has at least two tests and all tests pass. Do make note of the following line:

    1 items had no tests:
        rechthoeken

This output is expected. You should only write doctests for your functions. However, you will also write some code under the `if __name__ == '__main__'` section. This part of your program is also counted by `doctest` as a part that could be tested. We will not be writing tests for that part.

## Writing good tests

So when you adhere to the minimum requirements you're all set and have shown that you have masters the **mechanics** of testing. But you do not yet show that you have mastered the **art** of testing. So how do you choose which tests to include?

There are many tests that you could write, but you do not need to test every single case of input for your functions. Some tests are functionally equal. For example, above, we included the test for `calculate_length(0,2)`. One could argue that we should also test for `calculate_length(1,3)`. However, it is not so likely that you would find different bugs with that latter test than you would with the former. Why? Maybe because:

- In both cases both arguments are non-negative
- In both cases the difference is 2

One reason to include the second test for `calculate_length(1,3)` is because it does not include the number 0. This number could be seen are an "edge case", because it is the *lowest* non-negative number. But it is hard to imagine a situation where your code would handle the number 0 any different than the number 1.

Another reason to include `calculate_length(1,3)` is because it could show the linearity of the result. If you have used a wrong formula for calculating the length, a second test can make it more likely that you find the problem. However, in that case it may be wiser to test `calculate_length(1,4)` because it has a different expected answer.

You should not restrict your testing to just the simplest cases, but design tests that could help find different kinds of bugs in your program.

For example, the second test above is `calculate_length(-2, 2)`. Because the function `calculate_length` is handling lengths, we must ensure that negative coordinates are handled correctly. Lengths themselves cannot be negative and it is imaginable that a programmer might make or introduce a mistake that would yield negative lengths for negative inputs.

The third test above is `calculate_length(8, 0)`. Here, the numbers are in reverse orde: the second is smaller than the first. Again, a programming mistake could be made here so we include such a test.

From the above you should conclude that we will not be testing each and every combination of input but we will be testing *categories* of input. Which categories are relevant to the assignment differs, and it will take some time and creativity to come up with good sets of tests.

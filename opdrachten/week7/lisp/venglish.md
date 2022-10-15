# LISP

The programming language LISP is known for the many brackets that are needed to write a program.

    (defun factorial (n)
        (loop for i from 1 to n
            for fac = 1 then (* fac i)
            finally (return fac)))

Those brackets do make it possible to write a full program on a single line, after which the computer will still understand it. Here's the same program on one line:

    (defun factorial (n) (loop for i from 1 to n for fac = 1 then (* fac i) fi...

Your task is to write a check for the validity of a given LISP program. The question here is simply whether the number of brackets matches: for each opening bracket there must be a closing bracket, and the other way around!

## Validator class

We ask you specifically to write a validator into a class. This class named `LispValidator` has an initializer with one parameter: the LISP program's content (a string). Next to the initializer there must be a method called `is_valid()` that returns True or False.

    >>> LispValidator("(defun factorial (())(] (loop))))").is_valid
    False

    >>> LispValidator("(write (factorial 3))").is_valid
    True

    >>> LispValidator("(defun gretting ((write-line \"let it snow\"))").is_valid
    False

## Algorithm

To check the validity of a program you can go through the string and keep track of how many opening brackets you encounter. When you find one, add one to the statistics. And when you find a closing bracket, subtract one. The input program will then be valid when your final count is 0.

## Doctests

Above you can find a few doctests. These test the complete usage of the class, including a call to `is_valid`. You could add them to a docstring for the `class`, or to a docstring for the `is_valid` method. The doctests above are not the only ones that you could use.

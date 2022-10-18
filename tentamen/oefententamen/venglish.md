# Exam

The goal of this exam is to show how broad and deep your knowledge about Python programming reaches. We will look at everything that you have seen in the course, but we will specifically assess:

- Strong functional decomposition together with good names for functions
- Good use of variables and parameters to pass information around within the program
- Use of type hints to record the intention of the program
- Use of doctests to check the correctness of the code as closely as possible
- Use of built-in Python collections like list, dict, set, tuple
- Carefully reading and processing data files and manipulating strings
- Use of list comprehensions to process lists with little code
- Splitting up code into classes, each with a clear task, in close collaboration

You certainly do not have to apply everyting "perfectly" to earn a pass for the exam. It must become clear that you have reached a sufficient level to write working code within reasonable time and that you have grown enough basic knowledge of Python constructs. This will allow you to continue into the next courses where programming plays an important part.

## Getting help in Python

For this exam you will not use external sources like websites, the book or your old code. You are able to use the Python help functionality to look up information.

- Start Python using either of the commands `python` and `python3`
- Need help using a built-in function like `ord`? Enter `help(ord)`
- Need help using a built-in method like `str.startswith`? Enter `help(str.startswith)`
- Want to know what methods are supported by a (built-in) class like `dict`? Enter `help(dict)`

## Checks

- You can run a type check using `mypy --strict --ignore-missing-imports programma.py`.
- You can run doctests using `python -m doctest -v programma.py`.

## Submitting in one file

You must code everything in a single file. Make sure to demarcate different problems using the following comment with a brief name/summary of the problem substituted:

    # -------------------------------------------------------------------------
    # Problem: <name of problem>

## Strings & Files

-   Write a function that decides whether an argument `string1` is a prefix of argument `string2`. Do not use any existing string functions or methods other than indexing.

-   Write a function that calculates the *checksum* for any given file. The checksum is the sum of all characters in a file. Use the built-in Python function `ord(a)` to calculate the value of a single character; e.g., `ord('B')` equals `66`.

-   Write a function that counts all characters, words and lines in a given file and returns these numbers.

-   Each hour a measurement was taken of the C02 levels in a programming classroom at Science Park. We have saved the measurements in a file called `C02.txt`. The file contains two columns of data. The first column is the hour of measurement, and the second column is the ppm (parts per million) of C02 in the air. After ten measurement the file `C02.txt` contains the following:

        0,512
        1,640
        2,593
        3,580
        4,581
        5,613
        6,840
        7,889
        8,863
        9,891

    Write some functions that 1) provide a list of measurement values 2) provide the average of all measurements 3) provide the hour where the increase in CO2 value was largest. A better alternative to functions is to implement a single class that provides all of the above functionality.

## Classes

-   Create a class called `SecretMessage` where the initializer (constructor) gets a secret code and a secret message. Add the methods `open` (to retrieve the secret message if the correct code is provided) and `changeCode` (to change the unlock code, but only if the correct original code is provided).

-   Create a class called `Student` that stores: name, student number and status. Status is the academic year of the student: options 1 to 4 (or higher). Write code to automatically generate 20 students (named "Student1" and so on) with random student number and status. Then write code to print only the first-year students in the list.

## Comprehensions

-   Given a list containing integers, write a function that converts it to a string containing all numbers from the list with commas in between. The list `[1, 2, 3]` becomes the string `"1,2,3"`. Use a list comprehension for this.

## Types & Collections

-   What will be printed when executing this piece of code?

        data = [1,2,3,1,2,1,2,3]
        x = {}
        for datum in data:
            if datum in x:
                x[datum] += 1
            else:
                x[datum] = 1
        print(x)

-   The following piece of code gives an error. How can you make sure that variable `S` contains the string entered by the user, with a "C" as the first letter?

        >>> S = input("What is your name?")
        Jasper
        >>> S[0] = "C"
        TypeError: ’str’ object does not support item assignment

## Case study

Take a loot at the following file `passwd` that stores user data from a UNIX system:

    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1:System Services:/var/root:/usr/bin/false
    joedoe:*:1000:1000:Joe Dough:/Users/joe:/bin/zsh

As you can see the columns (fields) are written by colons. The columns are described as follows:

1. The username
2. The password (this is always `*`)
3. The user id
4. The group id
5. The name or description of the user
6. The home directory
7. The shell used

The following problems are based on this password file.

1. Write a function `load()` that takes the name of the file, and returns a `dict` in which the keys are the username and the values ​​are always a list containing the other data of the user.

2. Write a function `users()` that takes the user dict and returns a list containing just the usernames of all users.

3. Write a function `priviliged_users()` that takes the user dict and returns a list containing the usernames of privileged users (they have a user id between 0 and 100, inclusive).

4. Write a function `chpass()` that takes the user dict, a username, that user's password, and a new password. If username and old password are correct, the password will be changed to the new password.

5. Write a function `chsh()` that takes the user dict, a username and a new shell. The user's shell is changed to the specified value. You must first check whether the new shell appears in a list of allowed shells (you can define this list yourself based on the examples in the file above).

Extension options:

1. Use a dict with the username as the key, and also a dict with all other data of the user as values.

2. Use a class `User` which contains all the properties of one user and the list of users is a dict in which a username is always linked to a User object.

3. Use a `User` class and also create a `UserList` class that stores all `User` instances. All the functions written above should be implemented as methods of those classes, rather than as separate functions.

## Final checks

Don't forget to write doctests that test as good as possible and place all relevant type hints!

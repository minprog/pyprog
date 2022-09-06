# Password Police

These days you need an account for just about anything; email, social networks, web shopping, and each account requires it's own unique password. 
Often times these passwords are constrained by certain rules to make them harder to guess by 'hackers' or other third-parties.

## Assignment

Implement, in a file named `wachtwoord.py`, a program that prompts the user for a password and give the user feedback whether that password fulfills the constraints. At minimum the password should contain at least:

* one upper case letter, and one lower case letter.
* 8 characters.
* 1 numeric character.

## Code

The password should comply with at least the 3 earlier mentioned constraints. Implement an individual function to check for each constraint. Since the password has to comply with all three of the constraints, you will also need to implement a function to tie all of the other functions together.

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def check_length(password: str) -> bool:
        """
        Check whether the password contains a least 8 characters.
        """

    def check_letter(password: str) -> bool:
        """
        Check whether the password contains a least 1 upper case letter and 1 lower case letter.
        """

    def check_number(password: str) -> bool:
        """
                Check whether the password contains a least 1 numeric character.

        """

    def check_password(letter: bool, length: bool, number: bool) -> bool:
        """
        Check whether the password passed all three of the tests.

        """

    if __name__ == '__main__':
        <Your Program>

## Tips

* Ther is no one correct solution for each of the checks! There's more than one way to implement each of the functions, take a look at all of the string-operations in the book for inspiration.
* Beware! When you check whether a password contains both an upper case letter and a lower case letter, you also need to check whether there is any letter at all.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python wachtwoord.py
    Provide a password: PotatoTester123
    The provided password is valid.

    $ python wachtwoord.py
    Provide a password: hello
    The provided password is invalid.

## Extra challenge

To ensure the password is as secure as can be, add any extra contraints you can think of yourself. Instead of demanding the presence of certain characters, you could also prohibit the use of certain elements. You could for example exclude the use of spaces.

In case you have some extra time on your hands, try and give the user feedback on which constraint is violated in case their password is invalid. It is good practice to give detailed information about the result of your programs so that users can adapt accordingly. No one is helped by the knowledge that a program 'failed successfully'.

Note: once again there are no checks for this extra challenge.

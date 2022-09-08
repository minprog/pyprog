# Meal time

An infamous stereotype of the Dutch is that they start dinner at exactly 18:00. Let's assume this stereotype also reflects punctuality for other meals of the day. This means that breakfast time will be between 7:00 and 8:00, lunchtime is between 12:00 and 13:00 and dinnertime is between 18:00 and 19:00.
Let's utilize the knowledge of these time slots and have a program tell us what meal we should be eating based on the time of day.

## Assignment

Implement, in a file named `etenstijd.py`, a program that prompts the user to input the time and subsequently tells which meal corresponds to that hour of the day.

* The output of the program reflects whether is time for 'breakfast', 'lunch', or 'dinner'. If it's not time to eat anything, the program does not produce *any* output.
* You can assume that all input provided by the user is formatted either as 'X:XX' or 'XX:XX' and that these numbers describe the time using the 24-hour time format.
* These times are *inclusive*, meaning that, for example, 8:00 is still breakfast time, but 8:01 no longer is.

## Code

For this assignment you are going to write your own function, as before. Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def meal(time: str) -> str:
        """
        Converts a time string to a meal name.
        Meal can be "breakfast", "lunch", "dinner" or "".
        """

    if __name__ == '__main__':
        <Prompt the user for an answer, call your function, and print the result>

## Tips

*   You can "unpack" multiple values from one string by using the method `split()`. If you have a string containing `help@mprog.nl` you can unpack it into two variables like so:

        email = "help@mprog.nl"
        user, domain = email.split("@")

    After these two lines you will have two separate variables `user` and `domain` containing information from the original string `email`. Try it yourself using Python and see if you can print all information from the `user`-variable!

*   In the `main` part you need to ensure that absolutely nothing is printed if it's not time for a meal yet. See the examples below.

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python etenstijd.py
    What is the time? 7:15
    It's time for breakfast.

    $ python etenstijd.py
    What is the time? 13:00
    It's time for lunch.

    $ python etenstijd.py
    What is the time? 18:53
    It's time for dinner.

    $ python etenstijd.py
    What is the time? 22:12

Note that the last example does not produce any output aside from the prompt.

## Extra challenge

Looking for a little bit of increase in difficulty? Allow the user to also specify the time in 12-hour time format using PM or AM. This would allow for the following formats: `X:XX AM`, `XX:XX AM`, `X:XX PM`, and `XX:XX PM`. Since this is part of an optional extra challenge there will be no checks in `checkpy` to test for this, but you still have to make sure you pass all existing checks.

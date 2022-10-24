# Calendar

Implement a month calendar display, per the below:

    $ python kalender.py
    Year: 2022
    Month: 9
              Sep 2022
    ---------------------------
    Sun Mon Tue Wed Thu Fri Sat
                      1   2   3
      4   5   6   7   8   9  10
     11  12  13  14  15  16  17
     18  19  20  21  22  23  24
     25  26  27  28  29  30

## Assignment

Write, in a file named `kalender.py`, a program that displays a calendar as shown above, based on a given year and month.

Algorithmically, this is a bit of a challenge, because the date must be shown aligned to the correct weekdays. To do this you need to know which weekday is the first of the month. And to determine that day, you will need to know the weekday of an arbitrary historical date. As it happens, we know that 1 January 1800 was a Wednesday.

Let's assign numbers to the weekdays. In the example calendar above we can see that Sunday is the first day and Saturday the last; accordingly, we assign Sunday an index of 0 and Saturday an index of 6. This makes Wednesday equivalent to 3 and we will define a constant named `START_DAY` with a value of 3 to indicate that this is the first known weekday.

To then know on what weekday 1 September 2022 falls, we need to know:

* how many days fall between 1 January 1800 and 1 September 2022 (`days_from_1800`), and
* what day of the week 1 January 1800 is (`START_DAY`); together,
* this yields a formula `(days_from_1800 + START_DAY) % 7` to calculate the index of the first day of the month.

Finally, we need to account for leap years. A year is a leap year if divisible by 4. Because of calendar reforms, years that are also divisible by 100 are actually not leap years, but years that are divisible by 400 are. It's complicated.

You may assume that the user enters a year `>= 1800` and valid month numbers.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanations about the approach that you chose. The main program has already been provided and should not be changed.

For this assignment you are again encouraged to create additional functions to solve a small part of the problem. Those functions should then also have types and doctests.

    # 1 January 1800 is a Wednesday
    START_DAY = 3

    def is_leap_year(year: int) -> bool:
        """
        Return True if `year` is a leap year.
        """

    def days_from_1800(month: int, year: int) -> int:
        """
        Counts the days from 1800 until `month` of `year`.
        The first day of `month` is not included.
        Uses `days_from_1800_until_year` and `days_until_month`.
        """

    def days_from_1800_until_year(year: int) -> int:
        """
        Counts the days from 1800 until `year`.
        1 January of the new year is not included.
        Uses `is_leap_year`.
        """

    def days_until_month(month: int, year: int) -> int:
        """
        Counts the number of days from 1 January of `year` until `month` of `year`.
        The days of `month` are not included.
        Uses `is_leap_year`.
        """

    def days_in_month(month: int, year: int) -> int:
        """
        Determines the number of days in `month` of `year`.
        Uses `is_leap_year`.
        """

    def display_calendar(month: int, year: int) -> None:
        """
        Prints the calendar.
        Uses `display_header` and `display_grid`.
        """

    def display_header(month: int, year: int) -> None:
        """
        Prints the calendar header.
        """

    def display_grid(month: int, year: int) -> None:
        """
        Prints the calendar grid.
        Uses `first_weekday_month` and `days_in_month`.
        """

    def first_weekday_month(month: int, year: int) -> int:
        """
        Determines the first weekday of `month`.
        Uses `days_from_1800`.
        """

    if __name__ == '__main__':
        year = int(input("Year: "))
        month = int(input("Month: "))
        display_calendar(month, year)

## Hints

* Like in Tiles you can change `print` to <u>not</u> print a newline.

* The header always has the same width and format, so you can freely hardcode this.

## Examples

Your program should eventually behave exactly like in the example below.

    $ python kalender.py
    Year: 2022
    Month: 6
              Jun 2022
    ---------------------------
    Sun Mon Tue Wed Thu Fri Sat
                  1   2   3   4
      5   6   7   8   9  10  11
     12  13  14  15  16  17  18
     19  20  21  22  23  24  25
     26  27  28  29  30

    $ python kalender.py
    Year: 2022
    Month: 2
              Feb 2022
    ---------------------------
    Sun Mon Tue Wed Thu Fri Sat
              1   2   3   4   5
      6   7   8   9  10  11  12
     13  14  15  16  17  18  19
     20  21  22  23  24  25  26
     27  28

## Testing

* Always start you testing with the start case: see if the calendar of January 1800 is displayed correctly (you know that 1 January is a Wednesday).

* Then find another easy case: is February 1800 correct? That calendar should fit that of January in terms of weekdays.

* Take a look at a more recent calendar to see if those are correct. There are quite a few leap years in between, so don't jump to the wrong conclusions, whether you see the correct calendar or not!

* Find some leap years or reason which years should be leap years based on the rules stated earlier. Then you can check whether those are displayed correctly. And also the year after such a leap year.

* Don't forget that February should display the correct number of days in a leap year, and that March should also be correct.

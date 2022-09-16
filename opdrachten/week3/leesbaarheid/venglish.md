# Readability


The coleman-Liau index is a readability-test which determines the measure of readability of a text. This is based on the American system where 'grades' are used. This index is calculated with the amount of characters per word, and other such characteristics.

The formula is:

    CLI = 0.0588 * L - 0.296 * S - 15.8

where L is the average number of letters per 100 words, and S is the average number of sentences per 100 words.

More information on the Coleman-Liau index can be found on its [Wikipedia-page](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index). This is where you can find the way to calculate the average number of letters and sentences per 100 words as well.


## Assignment

Write, in a file named `leesbaarheid.py`, a program which calculates the readability of a text based on the Coleman-Liau index.

* The output of the program is in the vorm of `Grade X`. where X is the calculated grade. This is a whole number, so round off the result.
* If the grade is 16 or higher, give a grade of `Grade 16+` as output. Print `Below Grade 1` if the grade is less than 1.

## Code

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def calculate_grade(words: int, sentences: int, letters: int) -> float:
        """
        First, calculate the values of L and S based on the amount
        of words and sentences. Calculate the grade based on that.
        """

    def coleman_liau(L: float, S: float) -> int:
        """
        Calculate the grade according to the Coleman-Liau formula.
        """

    if __name__ == '__main__':
        <Main program>

## Tips

* You can get an alphabetical string by using the string module. Take a look aat the function `string.ascii_lowercase`.

* `You're` is 1 word with 5 letters!

## Examples

Your program should work like the examples below.

    $ python leesbaarheid.py
    Text: One fish. Two fish. Red fish. Blue fish.
    Below Grade 1

    $ python leesbaarheid.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3

    $ python leesbaarheid.py
    Text: There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.
    Grade 8

    $ python leesbaarheid.py
    Text: A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.
    Grade 16+

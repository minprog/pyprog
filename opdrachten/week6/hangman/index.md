# Classic Hangman

## tl;dr

Implement a program that allows someone to play the classic Hangman game against the computer.

    $ python hangman.py
    WELCOME TO HANGMAN ツ
    What length of word would you like to play with?
    8
    How many guesses are allowed?
    10
    I have a word in my mind of 8 letters.
    Guess a letter: a
    Wrong guess :(
    Guess a letter: n
    It's in the word! :)
    _____N__
    Guess a letter: ...


## Background

In case you aren't familiar with the game Hangman, the rules are as follows:

1. One player chooses a secret word, then writes out a number of dashes equal to the word length.

2. The other player begins guessing letters. Whenever she guesses a letter contained in the hidden word, the first player reveals each instance of that letter in the word. Otherwise, the guess is wrong.

3. The game ends either when all the letters in the word have been revealed or when the guesser runs out of guesses.


## Specification

Your assignment is to write a computer program that plays a game of Hangman using the game rules above. You are provided with the main program, but all **game logic** is missing. Your task is to design and implement two classes called `Hangman` and `Lexicon`, that together provide all functionality to make the starter code work *without any changes*.

- Objects of class `Lexicon` are used to retrieve words for the game from a dictionary. The `Lexicon` class will be based on the contents of `dictionary.txt`. This file contains the full contents of the Official Scrabble Player's Dictionary, Second Edition. This word list has over 120,000 words! That should be more than enough for our purposes.

- Objects of class `Hangman` will include all of the logic needed to play a single game. Hangman objects keep track of the current status of the game, and are able to update the status of the game when a letter is guessed. However, a Hangman object will not directly interact with the "user" (the person playing the game via the keyboard). In other words, it may not use anything like `print` or `input` functions.


## Getting started

On Linux, WSL or Mac, download the dictionary zip via:

    curl -LO https://github.com/minprog/hangman/raw/2020/classic/dictionary.zip
    unzip dictionary.zip
    rm -f dictionary.zip

If you are using Windows (not WSL), open the link in your browser, download the zip file, then manually unzip the file.

Then create a file called `hangman.py` and add the following code.

    if __name__ == '__main__':
    
        print("WELCOME TO HANGMAN ツ")
    
        # prompt and re-prompt for word length
        word_length = int(input("What length of word would you like to play with?\n"))
        while word_length > 44:
            word_length = int(input("No words are longer than 44 letters!\n"))
    
        # load words
        lexicon = Lexicon(word_length)
    
        # prompt and re-prompt for number of guesses
        number_guesses = int(input("How many guesses are allowed?\n"))
        while number_guesses <= 0:
            number_guesses = int(input("Negative or zero guesses make no sense.\n"))
    
        # run an infinite number of games
        while True:
        
            # game set-up
            print(f"I have a word in my mind of {word_length} letters.")
            word = lexicon.get_word()
            game = Hangman(word, number_guesses)
        
            # allow guessing and provide guesses to the game
            while game.is_running():
            
                # prompt and re-prompt for single letter
                letter = input(f"Guess a letter ({game.guesses_left()} left): ")
                if len(letter) != 1:
                    continue
            
                # provide feedback
                if game.guess(letter):
                    print("It's in the word! :)")
                else:
                    print("Wrong guess :(")
                    
                print(game.current_pattern())
        
            # after game ends, present the conclusion
            if game.won():
                print("Whoa, you won!!! Let's play again.")
            else:
                print(f"Sad, you lost ¯\_(ツ)_/¯. This was your word: {word}")

(This code does not contain any type hints. Your classes should contain type hints though!)


## Assignment 1

Your first task is to understand what the `Lexicon` class should look like and define an *interface* for it (recall from Queue that an interface is defined by the *operations* that are supported by a class).

1. Deeply study the starter code and make note in particular of how the `Lexicon` class is instantiated. What kind of parameter is needed to make a valid instance of `Lexicon`?

2. Find all occurrences of the `Lexicon` object in the code (only a single instance is ever made). What methods are called on this object? What parameters are needed and what should the method return?

3. Draw your class in UML class diagram format. Because you're just starting out and trying to understand the problem, put as much information in there as possible, including return types and parameters. In other words, the UML diagram should contain *implementation details*.

4. Think about the internal structure of the class: what variables do you need to support all expected operations? Write your ideas below the diagram.

Do not share your diagram with other students until after the assignment is fully completed by everyone.

Add your diagram and the answers the the questions to a file called `analysis.pdf`. You will add more to it in assignment 3.


## Assignment 2

Having created your diagram, you can implement your `Lexicon` class. Place it inside the `hangman.py` source file above the started code.

In the initializer for `Lexicon`, load words from `dictionary.txt`. You can use the following code:

    words = set()
    file = open('dictionary.txt', "r")
    for line in file:
        words.add(line.rstrip())
    file.close()

Make sure that all words of the right length are stored in an instance variable in `Lexicon`. Then complete the remainder of the class (using what you know from studying the `main` code).

Because the `Hangman` class is still missing, you can't really test the `Lexicon` class yet using the started code that we provided, because it will crash. But, you can test your code through doctests. Be sure to write doctests for each method (excluding `__init__`). Perhaps add the following to get you started:

    """
    >>> len(Lexicon(5).get_word())
    5
    """

Depending on what you want to test (and how), you might need a few setup steps for tests. You can do that by simply writing multiple lines prepended with `>>>`. For instance, the test above can also be written as:

    """
    >>> lexicon = Lexicon(5)
    >>> lexicon.get_word()
    5
    """

Do note that doctest will count the above as two tests instead of one. So if you can avoid multiple lines, it is probably better.

Don't forget to actually run your doctests at this point by running:

    $ python3 -m doctest -v hangman.py

## Assignment 3

Now you are going to analyse the `Hangman` class and define an *interface* for it.

1. Peruse the starter code and note how the `Hangman` class is instantiated. What kind of parameters are needed to make a valid instance of `Hangman`?

2. Find all occurrences of the `Hangman` object in the code. What methods are called on this object? What parameters are needed and what should each method return?

3. Draw a UML class diagram from the information you gathered. Because you are starting out and trying to understand the problem, put in all known implementation details.

4. Think about the internal structure of the class: what variables do you need to support all expected operations? Write your ideas below the diagram.

Again, do not share your diagram with other students until after the assignment is fully completed by everyone.

Add your complete diagram and the answers to the questions to a file called `analysis.pdf`.


## Assignment 4

Now implement the `Hangman` class, write doctests for each method you implement. It is hard to test the entire program without each method fully implemented, and even harder to debug the program if you only test once the entire program is implemented. So do write and run your doctests while you are working on your implementation of `Hangman`.

With the implementation of Hangman, and most `class`es in general, you will want to not only test for the output of a method, but also its so called: side-effects. For instance, in case of `Hangman` certain methods will change the **state** of the game. Guessing a letter through `guess()` is such a thing. For instance, we might test that `guess()` accepts a correct letter the first time, but rejects it if is entered again. To do so you can write doctests consisting of multiple lines:

    >>> game = Hangman("hello", 5)
    >>> game.guess("h")
    True
    >>> game.guess("h")
    False


## Manual testing

Hangman should now be a fully functional game that is also somewhat easier to debug. Run it, test it, and double-check if everything is still according to specification. If all is well, congratulations!


## Submitting

To submit this assignment, submit your UML diagrams in a PDF called analysis.pdf, together with your code.

### Assertions and our code checker

Upon submitting your code, our code checker will run its own checks alongside your doctests. To do this our code checker makes use of Python's builtin `assert`-statement. Like an `if`-statement an `assert` checks whether the expression to the right evaluates to `True` or `False`. If it evaluates to `True` all is good, and the code continues on like nothing ever happened. However, if it evaluates to `False` Python will raise an `AssertionError`. Yes, an actual Error! Meaning the code will fail at that point.

For instance, you might see the following message upon submitting:

    :( current_pattern() changes after a correct guess
        This check failed. Run the following code in the terminal to see if you can find out why:
        $ python3
        >>> from hangman import *
        >>> game = Hangman("abc", 5)
        >>> assert game.current_pattern() == "___"
        >>> assert game.guess("a")
        >>> assert game.current_pattern() == "a__"

Meaning, something went wrong in the example above. If you see such a message, run the code example in your own terminal to see just what went wrong. Odds are you will encounter the following:

    $ python3
    Python 3.10.6 (main, Oct  6 2022, 16:46:30) [Clang 14.0.0 (clang-1400.0.29.102)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from hangman import *
    >>> game = Hangman("abc", 5)
    >>> assert game.current_pattern() == "___"
    >>> assert game.guess("a")
    >>> assert game.current_pattern() == "a__"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError
    >>>

Notice the AssertionError above. At this point you know that the assert statement failed. This means `game.current_pattern() == "a__"` evaluated to `False`. But why? Well that is up to you to find out! For instance, here you could print out the outcome of `game.current_pattern()` like so:

    >>> game.current_pattern()
    "___"

Mmmm, that's a bug! 
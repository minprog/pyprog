# Tentamen-oefening

Lever hier je uitwerking in.

Geen probleem als het nog niet helemaal goed werkt na 30 minuten, maar lever het wel in! Zorg dat je, om zoveel mogelijk oefening te krijgen, de oefening dan later afmaakt. Je mag de oplossing zelfs nog een keer insturen op deze pagina.

## Opdracht

Advanced automated text analysis is often done using AI. It is possible to identify writing styles, authors, genres, and many other things using machine learning models. However, much of text analysis is much simpler. It is often needed to pre-process texts and generate basic statistics in preparation for advanced applications.

Write a program that counts how many words are in a text, and also reports how many words start with a capital letter and how many punctuation marks have been used. Note: how many words start with a capital letter is not necessarily the same number as the amount of capital letters in the text.

This test has quite a few aspects and challenges! Try to tackle it one aspect at a time and don't worry if you do not make it within 30 minutes. You can finish your program in the coming week(s) to train for the exam. But always hand in what you have after 30 minutes.

(For this test it's really easy to come up with all kinds of extra requirements that aren't mentioned above or visible in the examples below. Keep to the text of the assignment and do not complicate things anymore than is needed!)

    $ python3 count.py
    Text: There are no good writers.
    5 words
    1 capitalized word
    1 punctuation mark

    $ python3 count.py
    Text: Obi-Wan Kenobi took their job quite seriously.
    7 words
    2 capitalized words
    2 punctuation marks

    $ python3 count.py
    Text: The life on Sunday began without a speck of agitation.
    10 words
    2 capitalized words
    1 punctuation mark

    $ python3 count.py
    Text: It's difficult when you're carrying other people's dreams
    8 words
    1 capitalized word
    3 punctuation marks

Also note this:

    0 words
    1 word
    2 words

Design your program with functions as usual.

The last example sentence is a quote attributed to Sidney Poitier.

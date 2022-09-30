# Tentamen-oefening

Lever hier je uitwerking in.

Geen probleem als het nog niet helemaal goed werkt na 20 minuten, maar lever het wel in! Zorg dat je, om zoveel mogelijk oefening te krijgen, de oefening dan later afmaakt. Je mag de oplossing zelfs nog een keer insturen op deze pagina.

## Opdracht

Write a function called `has_more_vowels()` that counts all (lowercase) vowels in a string using just the Python `count()` method and returns True if there are more vowels than other characters in the string. You can use that method like below:

    d = 'haai'.count('a')
    # d is now 2

However, `count()` can only count one letter at a time so you will need to call it for each vowel aeiouy. You only need to consider lowercase though!

You can use `len()` to get the length of the string. With that information you can decide if the string does indeed have more vowels than any other character.

You must design the function yourself using the FDR and it must include a minimum of 2 doctests and correct types.

Finally, you must add a `if name == main` part to get input from the user and run it through the `has_more_vowels()` function. Print "It has more vowels than other characters" if that is true, otherwise "It has at least as many other letters than vowels".

Your code will be checked upon submission, including whether your doctests are correct.

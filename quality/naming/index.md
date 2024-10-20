# Naming

Choosing good names for your variables is an art more than a science.
Please take your time to choose clear names for your variables that describe the idea behind it and that help programmers (including you) understand your code more easily.
While we can't give a general rule for finding good names, we can help you narrow your choices down by noting some constraints.


## Name length

It is often hard to find a short name that intuitively describes what a variable represents, but it is worth the effort.
Some oft-used short names that have a clear meaning are:

- `sum`
- `average`
- `age`
- `name`
- `total`

You should understand that the meanings of those words are not clear by themselves, but dependent on the **context**.
Each of the names in your code tell one part of the full story.
So when choosing the variable name `sum`, make sure that somewhere close it becomes clear what exactly is being summed (like the total number of tonic waters ordered in a restaurant).

Some names are a bit more specific than the examples above and contain words that differentiate them from other variables.
Here are some examples of variable names having two words:

- `current_user` (from a list of users)
- `starting_position` (within a string)
- `old_name` (as opposed to a changed name)

For variables, there is often a preference to use single-word names. Long names often don't help understanding because they themselves take longer to understand. But there are many options, so it's good to experiment.


## Consistency

Consistency is a part of choosing names, too.
This mostly concerns how one formats names.
There are several ways to write names, and we will follow the specification which asks to write all names in **lowercase**, and to separate different words in names using an **underscore** (`_`).
Above, you have seen several examples of variable names that are formatted consistently with this specification. Like before, this is just a convention, and writing names differently will not result in a compiler error. However, being consistent does allow one to more easily make sense of a given program.


## Constants

It might be tempting to just write the literal value in your code somewhere and not use a constant name. This is commonly called a **magic number**, because without diving deep into the code it would often be very hard to understand what that number means. That's why we expect (almost) every magic number to be defined as a constant. Put such constants a the top of your code, so it is clear that these are unchangeable facts (for your program).


## Learn more

Want to know more about choosing good names? Have a look at these chapters:

- Robert Martin, *Clean code: a handbook of agile software craftsmanship*. Chapter 2, *Meaningful names*. Pearson Education, 2009.
- Steve McConnell, *Code complete: a practical handbook of software construction*. Chapter 11, *The power of variable names*. Microsoft Press, 2004.

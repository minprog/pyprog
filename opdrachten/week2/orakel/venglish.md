# The answer to everything

> "All right," said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.  
> "You’re really not going to like it," observed Deep Thought.  
> "Tell us!"  
> "All right," said Deep Thought. "The Answer to the Great Question…"  
> "Yes...!"  
> "Of Life, the Universe and Everything…" said Deep Thought.  
> "Yes...!"  
> "Is.." said Deep Thought, and paused.  
> "Yes...!"  
> "Is.."  
> "Yes...!!!...?"  
> "Forty-two," said Deep Thought, with infinite majesty and calm.
>
> --- The Hitchhiker’s Guide to the Galaxy, Douglas Adams

## Assignment

Implement, in a file named `orakel.py`, a program that prompts the user for the answer to "The Question of Life, the Universe and Everything". If the user answers with `42`, `forty-two`, `forty two` or `fortytwo`, the program should output `Yes`, for any other answer it should output `No`.

## Code

From now onwards we will wrap our function calls in an `if __name__ == '__main__':` statement, instead of putting those function calls under or in between our function definitions.
Aside from those function calls, your code will consist of a self-written function.

Design your program as described below. Complete the docstrings with doctests and any other explanation you deem necessary.

    def check_answer(answer: str) -> str:
        """
        Check whether the answer is equal to 42, forty-two, fortytwo, or forty two.
        """

    if __name__ == `__main__`:
        <Prompt the user for an answer, call your function, and print the result>

## Tips

* This is the first time you have to work with an `if`-`else`-statement. Don't forget there are also logical operators such as `and` and `or`. 

## Examples

Ultimately, your program has to produce output like the examples below.

    $ python orakel.py
    What is the answer to The Question of Life, the Universe and Everything? 42
    Yes

    $ python orakel.py
    What is the answer to The Question of Life, the Universe and Everything? forty-two
    Yes

    $ python orakel.py
    What is the answer to The Question of Life, the Universe and Everything? eighty-three
    No

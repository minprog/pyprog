# Types

In this course you are required to have types for all your functions: a single return type as well as a type for each of the function arguments. In many cases we have decided the types for you and specified these in the assignment.

Your code can be automatically tested to check for any deviations from the types that are specified in the function headers. For example, when we have the following function:

    def is_zero(number: int) -> bool:
        return 0

The actual return type of the function is `int`, not `bool`. This is a type error.

Upon submission, a **type checker** called `mypy` will be automatically run. You can review the results on the Progress page of this website. However, it's much better to run `mypy` yourself.

## Checking types

You can use the `mypy` command to check your program types. First install it by typing the following command in the Terminal:

    pip install mypy

Then check your program by:

    mypy --strict program.py

while substituting your own program's filename for `program.py`. This should ideally return the following message:

    Success: no issues found in 1 source file

But it could well be that `mypy` does encounter typing problems. Read the error messages well and ask for help when needed.

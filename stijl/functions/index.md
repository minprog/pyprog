# Functions and decomposition

In this course you write a lot of functions. Often, the function requirements are given by the assignments. However, you can further **decompose** your solution into smaller functions. For example, take this function:

    def print_fruityness(name_of_food: str) -> None:
        # determine whether it's fruit
        answer = False
        for fruit in fruits:
            if name_of_food == fruit:
                answer = True
        
        # print the result
        if answer:
            print(f"{name_of_food} is a fruit")
        else:
            print(f"{name_of_food} is not a fruit")

Note that the variable `fruits` is not defined here; we just assume it's available and filled correctly. Studying the code, you can see that it has two very **distinct** parts: 

- One part to **decide** whether something is a fruit
- One part to **print** the result in a formatted string

You could take this observation and split the function in two:

    def is_fruit(name_of_food: str) -> bool:
        answer = False
        for fruit in fruits:
            if name_of_food == fruit:
                answer = True
        return answer
    
    def print_fruityness(name_of_food: str) -> None:
        if is_fruit(name_of_food):
            print(f"{name_of_food} is a fruit")
        else:
            print(f"{name_of_food} is not a fruit")

That makes two clearly defined functions that each perform a **single task**: deciding or printing. The return type of each function makes this even more obvious.

Now let's simplify the first function a bit:

    def is_fruit(name_of_food: str) -> bool:
        return name_of_food in fruits
    
    def print_fruityness(name_of_food: str) -> None:
        if is_fruit(name_of_food):
            print(f"{name_of_food} is a fruit")
        else:
            print(f"{name_of_food} is not a fruit")

Apparently we can describe all of the function `is_fruit` in just a very simple statement. The question now is: should we have defined this function at all or not? 

Because in hindsight, we could also have written the function like this:

    def print_fruityness(name_of_food: str) -> None:
        if name_of_food in fruits:
            print(f"{name_of_food} is a fruit")
        else:
            print(f"{name_of_food} is not a fruit")

and then it would have been just as short.

The answer is that yes, in this case the expression `name_of_food in fruits` is just as clear as `is_fruit(name_of_food)`. We could do without the extra function.

However, not in all cases can you reduce the function's lines of code so easily. So prefer creating functions with clearly defined single tasks until you find that leaving the function out would be just as easy to understand as using it.

It must then be remarked that sometimes you do want such a function after all. Because one challenge for you as a programmer is to build a nice set of clearly defined functions. You are the one who decides on the names and when you find a nice systematic set of function names, your code can become even easier to read (even when you have a few single-line functions). But do not take this challenge until your are ready!

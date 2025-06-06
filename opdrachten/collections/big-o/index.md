# Complexity questions

In the file `questions.txt` write down the answers to the questions below.

All the code fragments below have some structure that holds data. Determine the big O complexity in terms of `n` for these fragments, where `n` is a variable that represents the number of elements in the datastructure. If for example the big O complexity of an algorithm is quadratic, your answer should be "O(n^2)".

## Complexity of built-in operations

On <https://wiki.python.org/moin/TimeComplexity> you can find the Time Complexity for each built-in operation of `list`, `set` and `dict`. 

The different tables on this website list both the avarage complexity and the worst-case complexity. For this assignment we ask you to **use the avarage complexity from the table**. The reasoning here is that `set` and `dict` have incredible avarage case performance, but very rarely hit a worst case performance. For algorithm comparison reasons, the latter is often not worth considering. That said, in critical high performance situations, it is worth considering that "Individual actions may take surprisingly long".

### Question 1

Consider the following pseudo code. Take `n` to be the length of the list.

    while list is not sorted:
        for every element in the list:
            if this element > element to the right:
                swap element with element to the right

### Question 2

For determining the complexity of the code below you don't need to take the first line into account.

    my_set = set([42, 21, 7, 3, 2])

    # determine complexity of part here below:
    if 14 in my_set:
        print("found :)")
    else:
        print("not found :(")

### Question 3

For determining the complexity of the code below you don't need to take the first line into account.

    my_set = set([42, 21, 7, 3, 2])

    # determine complexity of part here below:
    for i in range(len(my_set):
        if i in my_set:
            print(f"{i}: found :)")
        else:
            print(f"{i}: not found :(")

### Question 4

For determining the complexity of the code below you don't need to take the first three lines into account.

    n = 10
    set1 = set(range(0, n))
    set2 = set(range(n//2, n + n//2))

    # determine complexity of part here below:
    intersection = set1 & set2
    print(intersection)

### Question 5

For determining the complexity of the code below you don't need to take the first three lines into account.

    n = 10
    list1 = list(range(0, n))
    list2 = list(range(n//2, n + n//2))

    # determine complexity of part here below:
    intersection = []
    for element in list1:
        if element in list2:
            intersection.append(element)

    print(intersection)

### Question 6

For determining the complexity of the code below you don't need to take the first four lines into account.

    n = 10
    my_dict = {}
    for key in range(n):
        my_dict[key] = list(range(2 * key, 2 * key + n))

    for i in range(n):
        my_list = my_dict[i]
        if i * 5 in my_list:
            print(i * 5)

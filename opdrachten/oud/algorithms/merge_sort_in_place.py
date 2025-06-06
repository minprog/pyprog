import random
from typing import Any
random.seed(0)

def merge_in_place(array: list[Any], index1: int, index2: int, index3: int) -> None:
    """ Merge in place two sorted adjacent lists in 'array' to one sorted list. 
    List1 starts at 'index1' and goes up to 'index2'. 
    List2 starts at 'index2' and goes up to 'index3'. """
    print("index1:",index1,"index2:",index2,"index3:",index3)
    size1 = index2 - index1 # the size of list1
    size2 = index3 - index2 # the size of list2
    while size1 > 0 and size2 > 0:
        # check which list has next smallest element
        if array[index1] <= array[index2]:
            # if list1 has smallest it is easy
            index1 += 1
            size1 -= 1
        else:
            # if list2 has smallest we have to also move list1
            smallest = array[index2]
            index2 += 1
            size2 -= 1
            oldindex1 = index1
            index1 += 1
            array[index1:index1+size1] = array[oldindex1:oldindex1+size1] # moves list1
            array[oldindex1] = smallest # insert smallest

def merge_sort(array: list[Any]) -> None:
    """ Merge sorts 'array' in place. """
    list_length = len(array)
    sub_list_length = 1 # start with sub_list_length of 1
    while sub_list_length < list_length:
        # loop over all pairs of sub_lists as [index1:index2] and [index2:index3] 
        for index1 in range(0, list_length, sub_list_length * 2):
            index2 = index1 + sub_list_length
            index3 = min(len(array), index2 + sub_list_length) # make sure index3 is valid
            # merge the pair of sub_lists
            merge_in_place(array, index1, index2, index3)
            print(array) # debug print
        sub_list_length *= 2 # double the sub_list_length

def merge_sort_test(n: int =1000,rand_size: int =10000) -> bool:
    """ Tests the merge_sort() fuctions 'n' times with a list randomly chosen up to
    'rand_size' elements. Returns 'True' if all tests pass, 'False' otherwise. """
    for i in range(n):
        size = random.randrange(rand_size)
        array = [random.randrange(rand_size) for _ in range(size)]
        correct_sorted = sorted(array)
        merge_sort(array)
        if correct_sorted != array:
            print("error")
            return False
    return True

if __name__ == "__main__":
    n = 10
    array = [5, 1, 2, 8, 6]
    merge_sort(array)
    #merge_sort_test(1000,1000) # runs a lot of tests

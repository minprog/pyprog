""" Taken from chapter 13 of "Practical Programming, Third Edition
An Introduction to Computer Science Using Python 3.6" by Paul Gries, 
Jennifer Campbell, Jason Montojo."""

from typing import Any

def merge(L1: list[Any], L2: list[Any]) -> list[Any]:
    """Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1, i2 = 0, 0
    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

def merge_sort(L: list[Any]) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        newL = merge(workspace[i], workspace[i + 1])
        workspace.append(newL)
        i += 2
        print(workspace)
    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]

merge_sort([4,5,7,2,1,8,9])

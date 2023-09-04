# Algorithms

Get more comfortable with sorting algorithms. Each algorithm below intends to sort an array of integers into ascending order. Generally speaking, smaller elements in the array are moved to the "left" and larger elements are moved to the "right", until they are in order.

> Do the exercises on paper!

## Swapping

In most of the sorting algorithms below, *swapping* is important. By swapping, we mean exchanging the values at two positions in an array.

## Selection sort

![embed](https://www.youtube.com/embed/NEbb4XqKDNU)

The following Python code describes the selection sort algorithm.

~~~ python
for i in range(n):
    min_j = i; j = i
    for j in range(i, n):
        if array[j] < array[min_j]:
            min_j = j
    array[min_j], array[i] = array[i], array[min_j]
    print(array)
~~~

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Bubble sort

![embed](https://www.youtube.com/embed/LZaU8GHNsQI)

Consider the following Python code for bubble sort.

~~~ python
counter = 1
while counter > 0:
    counter = 0
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            counter += 1
    print(array)
~~~

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Insertion sort

![embed](https://www.youtube.com/embed/ntB1D3Bbz5I)

Consider the following Python code for insertion sort.

~~~ python
for i in range(n):
    element = array[i]
    j = i
    while j > 0 and array[j - 1] > element:
        array[j] = array[j - 1]
        j = j - 1
    array[j] = element
    print(array)
~~~

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Merge sort

> This algorithm is based on recursion, which is not part of the course. The merge sort algorithm will not be on any of the tests. However, merge sort is a great subject for practising recursion.

![embed](https://www.youtube.com/embed/yF3hMKmCk1A)

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

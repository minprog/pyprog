# Exercise: Algorithms

Get more comfortable with sorting algorithms. Each algorithm below intends to sort an array of integers into ascending order. Generally speaking, smaller elements in the array are moved to the "left" and larger elements are moved to the "right", until they are in order.

> Do the exercises on paper!

## Swapping

In most of the sorting algorithms below, *swapping* is important. By swapping, we mean exchanging the values at two positions in an array.

## Selection sort

![embed](https://www.youtube.com/embed/NEbb4XqKDNU)

The following pseudocode describes the selection sort algorithm.

    i = 0
    while i < n
        min_j = i; j = i
        while j < n:
            if array[j] < array[min_j]
                min_j = j
            j = j + 1

        tmp = array[min_j]
        array[min_j] = array[i]
        array[i] = tmp

        print(array)
        i = i + 1

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Bubble sort

![embed](https://www.youtube.com/embed/LZaU8GHNsQI)

Consider the following pseudocode for bubble sort.

    do
        counter = 0
        i = 0
        while i < n - 1
            if array[i] > array[i + 1]
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                counter = counter + 1
            i = i + 1

        print(array)
    while counter > 0

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Insertion sort

![embed](https://www.youtube.com/embed/ntB1D3Bbz5I)

Consider the following pseudocode for insertion sort.

    i = 0
    while i < n
        element = array[i]
        j = i
        while(j > 0 and array[j - 1] > element)
            array[j] = array[j - 1]
            j = j - 1
        array[j] = element
        print(array)
        i = i + 1

Perform the procedure on the array `{5, 1, 2, 8, 6}` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the array is sorted on every line by drawing a rectangle around the sorted part of the array.  

![](sort.PNG)

## Submit

To submit, make photos of your solution tables and then create a PDF containing each of the photos (no other formats will be accepted, so if you need help creating a PDF, just ask!). The PDF may not be larger than ~9MB, so best to convert your photos to black/white before converting to PDF.

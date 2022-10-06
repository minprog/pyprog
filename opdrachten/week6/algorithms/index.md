# Exercise: Algorithms

Get more comfortable with sorting algorithms. Each algorithm below intends to sort a list of integers into ascending order. Generally speaking, smaller elements in the list are moved to the "left" and larger elements are moved to the "right", until they are in order.

> Do the exercises on paper!

## Swapping

In most of the sorting algorithms below, *swapping* is important. By swapping, we mean exchanging the values at two positions in an list.

## Selection sort

![embed](https://www.youtube.com/embed/NEbb4XqKDNU)

The following pseudocode describes the selection sort algorithm.

    i = 0
    while i < n
        min_j = i; j = i
        while j < n:
            if numbers[j] < numbers[min_j]
                min_j = j
            j = j + 1

        tmp = numbers[min_j]
        number[min_j] = numbers[i]
        numbers[i] = tmp

        print(numbers)
        i = i + 1

Perform the procedure on the list `[5, 1, 2, 8, 6]` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the list is sorted on every line by drawing a rectangle around the sorted part of the list.  

![](sort.PNG)

## Bubble sort

![embed](https://www.youtube.com/embed/LZaU8GHNsQI)

Consider the following pseudocode for bubble sort.

    do
        counter = 0
        i = 0
        while i < n - 1
            if numbers[i] > numbers[i + 1]
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp
                counter = counter + 1
            i = i + 1

        print(numbers)
    while counter > 0

Perform the procedure on the list `[5, 1, 2, 8, 6]` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the list is sorted on every line by drawing a rectangle around the sorted part of the list.  

![](sort.PNG)

## Insertion sort

![embed](https://www.youtube.com/embed/ntB1D3Bbz5I)

Consider the following pseudocode for insertion sort.

    i = 0
    while i < n
        element = numbers[i]
        j = i
        while(j > 0 and numbers[j - 1] > element)
            numbers[j] = numbers[j - 1]
            j = j - 1
        numbers[j] = element
        print(numbers)
        i = i + 1

Perform the procedure on the list `[5, 1, 2, 8, 6]` of length `n=5`. Show every swap on an individual line and show which elements you're swapping by underlining them. Also show which part of the list is sorted on every line by drawing a rectangle around the sorted part of the list.  

![](sort.PNG)

## Submit

To submit, make photos of your solution tables and then create a PDF containing each of the photos (no other formats will be accepted, so if you need help creating a PDF, just ask!). The PDF may not be larger than ~9MB, so best to convert your photos to black/white before converting to PDF.

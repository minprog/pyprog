array=[4,5,7,2,1,8,9]
n=len(array)

for i in range(n):
    min_j = i; j = i
    for j in range(i, n):
        if array[j] < array[min_j]:
            min_j = j
    array[min_j], array[i] = array[i], array[min_j]
    print(array) # debug print

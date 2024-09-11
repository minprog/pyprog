array=[4,5,7,2,1,8,9]
n=len(array)

counter = 1
while counter > 0:
    counter = 0
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            counter += 1
    print(array) # debug print

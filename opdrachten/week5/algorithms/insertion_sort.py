array=[4,5,7,2,1,8,9]
n=len(array)

for i in range(n):
    element = array[i]
    j = i
    while j > 0 and array[j - 1] > element:
        array[j] = array[j - 1]
        j = j - 1
    array[j] = element
    print(array) # debug print

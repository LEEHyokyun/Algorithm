##selected array
## 1 2 3 4 5 6 7 8 9 10

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
arrayLength = len(array)

for i in range(arrayLength):
    for j in range(0, arrayLength-i-1):
        if array[j] > array[j+1]:
           temp = array[j]
           array[j] = array[j+1]
           array[j+1] = temp


print(array)
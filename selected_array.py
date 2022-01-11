##selected array
## 1 2 3 4 5 6 7 8 9 10

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
arrayLength = len(array)

for i in range(arrayLength):
    minValue = array[i]
    minIndex = i
    for j in range(i, arrayLength):
        if minValue > array[j]:
            minValue = array[j]
            minIndex = j
    temp = array[i]
    array[i] = array[minIndex]
    array[minIndex] = temp

print(array)
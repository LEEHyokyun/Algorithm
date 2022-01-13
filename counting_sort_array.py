array = [1, 3, 2, 4, 3, 2, 5, 3, 1, 2,
         3, 4, 4, 3, 5, 1, 2, 3, 5, 2,
         3, 1, 4, 3, 5, 1, 2, 1, 1, 1]
count = 5 #범위가 정해져 있을떼

countSort = [0, 0, 0, 0, 0]
result = []

for j in range(0, len(array)):
        countSort[array[j]-1] = countSort[array[j]-1] + 1

print(countSort)

for i in range(0, count):
    print(i)
    if countSort[i] != 0:
        for j in range(countSort[i]):
            result.append(i + 1)


print(result)
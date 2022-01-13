import sys
sys.setrecursionlimit(10**7)

array = [3, 10, 5, 1, 7, 6, 4, 2, 8, 9]
arrayLength = len(array)
result = []

#병합
def merge(start, middle, end):
    #부분집합1
    i = start
    #부분집합2
    j = middle + 1
    #병합된 집합(=i)
    k = start

    ##부분집합이 분할된 상태에서 병합하는 과정
    while i <= middle and j <= end:
        if array[i] <= array[j]:
            result[k] = array[i]
            i = i+1
        else:
            result[k] = array[j]
            j = j+1
        k = k+1
        print(result)

        ## i, j가 먼저 도달할경우 다른 부분집합의 원소를 그대로 병합해준다
        if i > middle:
            for t in range(j, end):
                result[k] = array[t]
                k = k+1
        else:
            for t in range(i, middle):
                result[k] = array[t]
                k = k+1


#분할
def mergeSort(start, end):
    if start <= end:
        middle = (start + end)/2
        mergeSort(start, middle)
        mergeSort(middle+1, end)
        merge(start, middle, end)


#함수호출
mergeSort(0, arrayLength-1)
print(result)








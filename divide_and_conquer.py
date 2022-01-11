array = [3, 10, 5, 1, 7, 6, 4, 2, 8, 9]
arrayLength = len(array)


##분할정복을 하면서 부분집합을 나누게 되는데
##부분집합의 처음 숫자, 마지막 숫자
##부분집합의 원소가 1개일 경우
##처음 숫자가 마지막 숫자보다 크거나 같은 경우로 빼면
##그대로 return
##기본적으로 분할정복은 한 함수를 선언하고, 이에 따라 각 부분집합에 대해 분할정복을 수행하는 방식으로 진행한다.
##즉 재귀법으로 진행
# def quickSort(array, dividedStart, dividedFinal)
# if (dvidedStart >= dividedFinal):
# return

## pivot값을 설정
## 큰 값 찾을때(처음에서 끝 순으로) : dividedStart + 1
## 작은 값 찾을때(끝에서 처음 순으로) : dividedFinal
##key = pivot
# key = dividedStart
# i = divdiedStart + 1
# j = dividedFinal

##순회 시 연산종료시점은 엇갈리는 시점(그 전까지 반복)
##엇갈리는 시점에서 pivot값과 큰 값(j index)을 교체
##그 전까지는 탐색하면서 pivot값보다 작은 값, 큰 값을 찾아 나간다.
# while (i <= j)
# while(data[i] <= data[key]) #pivot보다 큰 값을 만날때까지
# i++
# while(data[j] >= data[key] && j > dividedStart) #pivot보다 작은 값을 만날때까지, 단 비교는 부분집합의 첫째 index까지(하한선 설정)
# j--

##엇갈린 상태면 pivot값과 end index value를 바꾼다.
# if( i > j)
# temp = data[j]
# data[j] = data[key]
# data[key] = temp

##엇갈리지 않은 상태면 위에서 구한 두 값을 바꾼다.
# else
# temp = data[j]
# data[j] = data[i]
# data[i] = temp

##위 알고리즘을 통해 분할된 왼쪽, 오른쪽 부분집합에 대해 각각 퀵정렬을 재귀함수처럼 다시 진행한다.
# quickSort(data, dividedStart, j-1)
# quickSort(data, j+1, dividedFianl)

def quickSort(array, dividedstart, dividedfianl):
    if (dividedstart >= dividedfianl):
        return
    key = dividedstart
    i = dividedstart + 1
    j = dividedfianl

    while i <= j:
        while i <= dividedfianl and array[i] <= array[key]:
            i = i + 1
        while j > dividedstart and array[j] >= array[key]:
            j = j - 1

        # 엇갈리면 pivot값과 작은 값을 교체(현재 오름차순 정렬중)
        if i > j:
            temp = array[j]
            array[j] = array[key]
            array[key] = temp
        # 엇갈리지 않았다면 해당 data들만 교체
        else:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    quickSort(array, dividedstart, j - 1)
    quickSort(array, j + 1, dividedfianl)


quickSort(array, 0, arrayLength - 1)
print(array)

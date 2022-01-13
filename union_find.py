array = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# 부모노드 찾기(1차구성)
def getParent(array, value):
    if array[value] == value:
        return array[value]
    return getParent(array, array[value])


# 부모노드 합치기(2차구성)
def unionParent(array, value1, value2):
    value1 = getParent(array, value1)
    value2 = getParent(array, value2)
    if value1 < value2:
        array[value2] = value1
    else:
        array[value1] = value2


# 같은 부모를 가지는지(같은 graph의 node인지) 확인하기
def findParent(array, value1, value2):
    value1 = getParent(array, value1)
    value2 = getParent(array, value2)
    if value1 == value2:
        return True
    else:
        return False

unionParent(array, 1, 2)
unionParent(array, 2, 3)
unionParent(array, 3, 4)
unionParent(array, 5, 6)
unionParent(array, 6, 7)
unionParent(array, 7, 8)
print(array)

print(findParent(array, 1, 2))
print(findParent(array, 4, 5))
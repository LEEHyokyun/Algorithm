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

#간선정보
edges = [
    [12, 1, 7],
    [28, 1, 4],
    [67, 1, 2],
    [24, 2, 4],
    [62, 2, 5],
    [20, 3, 5],
    [37, 3, 6],
    [13, 4, 7],
    [45, 5, 6],
    [73, 5, 7]
]

edges.sort()
result = 0

for edge in edges:
    cost, node1, node2 = edge
    if findParent(array, node1, node2):
        pass
    else:
        unionParent(array, node1, node2)
        result = result + cost

print(result)


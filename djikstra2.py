node = 6
INF = 100000000

#graph 구성하기
graph = {
    1: {2: 2, 3: 5, 4: 1},
    2: {1: 2, 3: 3, 4: 2},
    3: {1: 5, 2: 3, 4: 3, 5: 1, 6: 5},
    4: {1: 1, 2: 2, 3: 3, 5: 1},
    5: {3: 5, 4: 1, 6: 2},
    6: {3: 5, 5: 2}
}

#distance
import heapq
#최소비용인 인접노드를 탐색하는 부분을 heap정렬을 이용해 구하는 경우
#시간복잡도를 기존 알고리즘 대비 개선시킬 수 있는 알고리즘
def dijkstra(start):
    distance = {node: INF for node in graph}
    distance[start] = 0
    queue = []
    #min heap
    heapq.heappush(queue, [distance[start], start])

    while queue:
        currentDistance, currentIndex = heapq.heappop(queue)

        #시작점이 정해진 상태임을 기억
        #현재 선택된 노드에 대해
        if distance[currentIndex] < currentDistance:
            continue
        #인접노드 방문 후 새로운 거리값 계산
        for newIndex, newDistance in graph[currentIndex].items():
            tempDistance = currentDistance + newDistance
            if tempDistance < distance[newIndex]:
                distance[newIndex] = tempDistance
                heapq.heappush(queue, [tempDistance, newIndex])
    return distance

print(dijkstra(1))
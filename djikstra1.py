node = 6
INF = 100000000

#graph 구성하기
graph = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]

#방문여부
visited =  [False] * node

#거리
distance = [0] * node

#출발노드를 기준으로 해당 노드까지 최소비용이 구해진 후(배열생성)
#최소거리(비용)에 대한 노드를 반환(방문하지 않은 노드 중)
def getSmallIndex():
    min = INF
    index = 0
    for i in range(node):
        if distance[i] < min and visited[i] is not True:
            min = distance[i]
            index = i
    return index

#다익스트라를 수행하는 함수
def dijkstra(start):

    visited[start] = True
    for i in range(node):
        #graph에 적혀진 비용정보를 distance에 입력
        #원래 알고있는 최소비용
        distance[i] = graph[start][i]
    #방문하지않는 노드 중 최소 비용이 발생하였을때(거쳐가는 경우)
    #방문하지않는 노드의 우선노드는 distance 상에서 최소비용을 가지는 노드
    for i in range(node-2):
        #자기자신과 이전 기준점까지는 탐색완료(탐색대상이 node-2)
        currentIndex = getSmallIndex()
        visited[currentIndex] = True
        for j in range(node):
            if visited[j] is not True and distance[currentIndex]+graph[currentIndex][j] < distance[j]:
                distance[j] = distance[currentIndex] + graph[currentIndex][j]


dijkstra(5)
print((distance))
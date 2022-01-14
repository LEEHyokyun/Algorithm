node = 4
INF = 1000000

graph = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]

def floydWarshall():
    d = [[0] * node for _ in range(node)]

    for i in range(node):
        for j in range(node):
            d[i][j] = graph[i][j]

    ##k는 거쳐가는 노드
    for k in range(node):
        #i는 출발노드
        for i in range(node):
            #j는 도착노드
            for j in range(node):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    for i in range(node):
        for j in range(node):
            print(d[i][j])

floydWarshall()
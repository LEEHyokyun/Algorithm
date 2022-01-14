node = 7

#진입차수정보
inDegree = [0, 1, 1, 1, 1, 2, 1]

graph = [
    [2,5],
    [3],
    [4],
    [6],
    [6],
    [7],
    [0]
]
def topologySort():
    result = []
    queue = []

    #진입차수가 0인 노드를 큐에 삽입
    for i in range(0, len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)
    #위상정렬의 완전한 수행을 위해 모든 node를 방문

    for i in range(len(inDegree)):
        #n개 방문 이전에 cycle이 Queue가 빈다면 사이클이 발생한 경우
        if len(queue) == 0:
            print("위상정렬이 불가능한 graph입니다.")
            return
        else:
            nextNode = queue.pop(0)
            result.append(nextNode+1)
            if graph[nextNode] == 0:
                result.append(nextNode + 1)
            else:
                for j in graph[nextNode]:
                    inDegree[j-1] = inDegree[j-1] - 1
                    if inDegree[j-1] == 0:
                        queue.append(j-1)


    return result

print(topologySort())
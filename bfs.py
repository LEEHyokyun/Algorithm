from queue import Queue

graph = {
    1: [2,3],
    2: [1,3,4,5],
    3: [1,2,6,7],
    4: [2,5],
    5: [2,4],
    6: [3,7],
    7: [3,6]
}

def bfs(graph, start):
    checked = []
    q = Queue()
    q.put(start)

    while q.qsize() > 0:
        node = q.get()
        if node not in checked:
            checked.append(node)
            for adj in graph[node]:
                q.put(adj)
    return checked


print(bfs(graph, 1))

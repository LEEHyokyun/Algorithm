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
    stack =[]
    stack.append(start)

    while stack :
        node = stack.pop()
        if node not in checked:
            checked.append(node)
            for adj in graph[node]:
                stack.append(adj)
    return checked


print(bfs(graph, 1))

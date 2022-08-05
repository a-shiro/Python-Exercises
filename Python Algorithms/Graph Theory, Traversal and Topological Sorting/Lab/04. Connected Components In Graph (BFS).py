from collections import deque


def bfs(node, graph, visited, component):
    visited[node] = True
    queue = deque([node])
    component.append(node)

    while queue:
        current_node = queue.pop()

        for child in graph[current_node]:
            if not visited[child]:
                queue.appendleft(child)
                visited[child] = True
                component.append(child)


graph = [
    [3, 6],
    [3, 4, 5, 6],
    [8],
    [0, 1, 5],
    [1, 6],
    [1, 3],
    [0, 1, 4],
    [],
    [2]
]

visited = [False] * len(graph)
component = []

for node in range(len(graph)):
    if visited[node]:
        continue

    bfs(node, graph, visited, component)

    print(*component)
    component.clear()

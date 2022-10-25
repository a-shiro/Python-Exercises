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


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * len(graph)

for node in range(len(graph)):
    if visited[node]:
        continue

    component = []
    bfs(node, graph, visited, component)

    print(f"Connected component: {' '.join([(str(x)) for x in component])}")

# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2

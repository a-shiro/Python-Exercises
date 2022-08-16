nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    node_1, node_2 = (int(x) for x in input().split())

    if node_1 not in graph:
        graph[node_1] = []

    if node_2 not in graph:
        graph[node_2] = []

    graph[node_1].append(node_2)

visited = []
for node in range(1, nodes + 1):
    visited.append(node)


def dfs(node, graph, visited):
    visited.remove(node)

    for child in graph[node]:
        if child not in visited:
            continue
        dfs(child, graph, visited)


starting_node = int(input())
dfs(starting_node, graph, visited)

print(*visited)

# 6
# 5
# 1 2
# 2 4
# 3 4
# 6 5
# 6 4
# 1

# 4
# 4
# 1 4
# 2 3
# 3 4
# 4 1
# 3

def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


def create_graph(edges):
    result = {}

    for node_1, node_2 in edges:
        if node_1 not in result:
            result[node_1] = []

        if node_2 not in result:
            result[node_2] = []

        result[node_1].append(node_2)
        result[node_2].append(node_1)

    return result


def read_edges(streets):
    result = []

    for _ in range(streets):
        node_1, node_2 = input().split(' - ')

        result.append((node_1, node_2))

    return result


buildings = int(input())
streets = int(input())

edges = read_edges(streets)
graph = create_graph(edges)

result = []

for node_1, node_2 in edges:
    visited = set()

    graph[node_1].remove(node_2)
    graph[node_2].remove(node_1)

    dfs(node_1, graph, visited)

    if len(visited) != buildings:
        result.append((node_1, node_2))

    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


print('Important streets:')
for result_tuple in result:
    streets = [*result_tuple]
    streets.sort()

    print(*streets)

# 5
# 5
# 1 - 0
# 0 - 2
# 2 - 1
# 3 - 0
# 3 - 4

# 7
# 8
# 0 - 1
# 1 - 2
# 2 - 0
# 1 - 3
# 1 - 4
# 1 - 6
# 3 - 5
# 4 - 5

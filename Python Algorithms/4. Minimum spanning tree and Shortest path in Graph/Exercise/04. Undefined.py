# Bellman-Ford
from collections import deque


def find_path(parent, node):
    result = deque()

    while node is not None:
        result.appendleft(node)
        node = parent[node]

    return result


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

start = int(input())
destination = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue

        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            parent[second] = first

for first, second, weight in graph:
    new_distance = distance[first] + weight
    if new_distance < distance[second]:
        print('Undefined')
        break
else:
    path = find_path(parent, destination)

    print(*path)
    print(distance[destination])

# 5
# 8
# 1 2 -1
# 1 3 4
# 2 3 3
# 2 4 2
# 2 5 2
# 4 2 1
# 4 3 5
# 5 4 -3
# 1
# 4

# 5
# 8
# 1 2 -1
# 1 3 4
# 2 3 3
# 2 4 2
# 2 5 2
# 4 2 -1
# 4 3 5
# 5 4 -3
# 1
# 4

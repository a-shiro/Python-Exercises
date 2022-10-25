from collections import deque

nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split(' ')]

    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes_count + 1)
parent = [None] * (nodes_count + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()

    if node == destination_node:
        break

    for child in graph[node]:
        if visited[child]:
            continue

        visited[child] = True

        queue.append(child)
        parent[child] = node

shortest_path = deque()

node = destination_node
while node is not None:
    shortest_path.appendleft(node)
    node = parent[node]

print(f'Shortest path length is: {len(shortest_path) - 1}')
print(*shortest_path)

# 8
# 10
# 1 2
# 1 4
# 2 3
# 4 5
# 5 8
# 5 6
# 5 7
# 5 8
# 6 7
# 7 8
# 1
# 7

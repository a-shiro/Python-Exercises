from collections import deque


def get_result_sequence(target_destination):
    result = deque()
    node = target_destination

    while node is not None:
        result.appendleft(node)
        node = parent[node]

    return result


# 1. First read the edges and create a graph
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

# 2. Read Start point and Destination point and start the algorithm
start = int(input())
target_destination = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False

    for edge in graph:
        if distance[edge.source] == float('inf'):  # this means we haven't found a result for that node yet
            continue

        new_distance = distance[edge.source] + edge.weight

        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True

    if not updated:
        break

# 3. Do a second iteration over the graph
for edge in graph:  # second iteration catches if there are negative cycles
    new_distance = distance[edge.source] + edge.weight

    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    result = get_result_sequence(target_destination)

    print(*result)
    print(distance[target_destination])

# 6
# 8
# 1 2 8
# 1 3 10
# 2 4 1
# 3 6 2
# 4 3 -4
# 4 6 -1
# 6 5 -2
# 5 3 1
# 1
# 6

# 4
# 4
# 1 2 1
# 2 3 -1
# 3 4 -1
# 4 1 -1
# 1
# 4
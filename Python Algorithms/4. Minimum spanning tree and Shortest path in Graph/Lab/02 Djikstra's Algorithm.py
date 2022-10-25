from queue import PriorityQueue
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


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]  # example input - 0, 6, 10

    if source not in graph:
        graph[source] = []

    if destination not in graph:
        graph[destination] = []

    graph[source].append(Edge(source, destination, weight))

# 2. Read Start point and Destination point, create a distance and parent list to keep the shortest distances and
# parents of nodes
start = int(input())
target_destination = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start] = 0

# 3. Create a priority queue and start the BFS
priority_queue = PriorityQueue()
priority_queue.put((0, start))

while not priority_queue.empty():
    min_distance, node = priority_queue.get()  # get removes the shortest current path(node and distance) from the queue
    # and returns it

    if node == target_destination:
        break  # we have found the shortest path to the destination

    for edge in graph[node]:
        new_distance = min_distance + edge.weight

        if new_distance < distance[edge.destination]:  # swap the distance if new one is better and mark parent node
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            priority_queue.put((new_distance, edge.destination))  # add iteration tuple in queue

if distance[target_destination] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target_destination])  # prints the shortest path number for the targeted node

    result = get_result_sequence(target_destination)  # extract the result sequence by tracing back from the end node

    print(*result)

# 18
# 0, 6, 10
# 0, 8, 12
# 6, 4, 17
# 6, 5, 6
# 8, 5, 3
# 5, 4, 5
# 5, 11, 33
# 8, 2, 14
# 2, 11, 9
# 2, 7, 15
# 4, 1, 20
# 4, 11, 11
# 11, 1, 6
# 11, 7, 20
# 1, 9, 5
# 1, 7, 26
# 7, 9, 3
# 3, 10, 7
# 0
# 9

# 18
# 0, 6, 10
# 0, 8, 12
# 6, 4, 17
# 6, 5, 6
# 8, 5, 3
# 5, 4, 5
# 5, 11, 33
# 8, 2, 14
# 2, 11, 9
# 2, 7, 15
# 4, 1, 20
# 4, 11, 11
# 11, 1, 6
# 11, 7, 20
# 1, 9, 5
# 1, 7, 26
# 7, 9, 3
# 3, 10, 7
# 0
# 10

def find_root(parent, node):
    while node != parent[node]:  # if 1's parent is 1 that means that 1 is root
        node = parent[node]
    return node


# 1. First read the edges and create a graph
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())
graph = []

biggest_node = float('-inf')

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    biggest_node = max(first, second, biggest_node)

# 2. Sort edges and iterate
parent = [n for n in range(biggest_node + 1)]  # we create a helper list that helps keeping parents of nodes
forest = []

for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    # if they are different merge them together and add them to the forest list
    # if they have the same root (ex. 8 and 8) that means they are in the same tree, and we don't add them
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')

# 11
# 0, 3, 9
# 0, 5, 4
# 0, 8, 5
# 1, 4, 8
# 1, 7, 7
# 2, 6, 12
# 3, 5, 2
# 3, 6, 8
# 3, 8, 20
# 4, 7, 10
# 6, 8, 7

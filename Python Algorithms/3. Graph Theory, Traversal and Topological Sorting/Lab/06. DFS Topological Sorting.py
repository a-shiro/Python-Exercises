from collections import deque


def dfs(node, graph, visited, cycles, queue):
    if node in cycles:
        raise Exception('Cycle has been detected. Invalid topological sorting.')

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        if child:
            dfs(child, graph, visited, cycles, queue)

    cycles.remove(node)
    queue.appendleft(node)


graph = {}

for _ in range(int(input())):
    line = input().split('->')
    node = line[0].strip()
    children = line[1].split(', ')

    graph[node] = []

    for child in children:
        if child:
            graph[node].append(child.strip())

visited = set()
cycles = set()
queue = deque()

for node in graph:
    dfs(node, graph, visited, cycles, queue)

print(f'Topological sorting: {", ".join(queue)}')


# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->

# 5
# IDEs -> variables, loops
# variables -> conditionals, loops, bits
# conditionals -> loops
# loops -> bits
# bits ->

# 2
# A -> B
# B -> A
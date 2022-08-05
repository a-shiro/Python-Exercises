def find_node_dependencies(graph):
    result = {}

    for node in graph:
        if node not in result:
            result[node] = 0

        for child in graph[node]:
            if child:
                if child not in result:
                    result[child] = 1
                else:
                    result[child] += 1

    return result


def find_node_without_dependencies(node_dependencies):
    for node, dependencies in node_dependencies.items():
        if dependencies == 0:
            return node
    return None


def remove_dependencies(node_dependencies):
    result = []

    while node_dependencies:
        node_to_remove = find_node_without_dependencies(node_dependencies)

        if node_to_remove is None:
            return False

        for child in graph[node_to_remove]:
            node_dependencies[child] -= 1

        node_dependencies.pop(node_to_remove)
        result.append(node_to_remove)

    return result


def create_graph():
    graph = {}

    for _ in range(int(input())):
        line = input().split('->')
        node = line[0].strip()
        children = line[1].split(', ')

        graph[node] = []

        for child in children:
            if child:
                graph[node].append(child.strip())

    return graph


graph = create_graph()
node_dependencies = find_node_dependencies(graph)
result = remove_dependencies(node_dependencies)

if not result:
    print('Invalid topological sorting')
else:
    print(f'Topological sorting: {", ".join(result)}')

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

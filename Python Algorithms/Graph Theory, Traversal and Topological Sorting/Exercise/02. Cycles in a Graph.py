def is_graph_acyclic(dependencies):
    acyclic = False

    for node in dependencies:
        if dependencies[node] == 0:
            acyclic = True
            break

    return acyclic


def find_node_dependencies(node, graph, node_dependencies):
    if node not in node_dependencies:
        node_dependencies[node] = 0

    for child in graph[node]:
        if child not in node_dependencies:
            node_dependencies[child] = 1
        else:
            node_dependencies[child] += 1


def create_graph():
    result = {}

    while True:
        line = input().split('-')

        if len(line) == 1:
            break

        result[line[0]] = line[1]

    return result


graph = create_graph()

node_dependencies = {}
for node in graph:
    find_node_dependencies(node, graph, node_dependencies)

acyclic = is_graph_acyclic(node_dependencies)

if acyclic:
    print('Acyclic: Yes')
else:
    print('Acyclic: No')

# A-F
# F-D
# D-A
# End

# K-J
# J-N
# N-L
# N-M
# M-I
# End

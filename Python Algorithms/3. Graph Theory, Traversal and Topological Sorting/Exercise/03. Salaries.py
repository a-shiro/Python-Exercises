def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]

    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    return salary


employees = int(input())

graph = []
salaries = [None] * employees

for i in range(employees):
    graph.append([])
    for j, el in enumerate(input()):
        if el == 'Y':
            graph[i].append(j)

result = 0
for node in range(len(graph)):
    salary = dfs(node, graph, salaries)
    result += salary

print(result)



# 4
# NNYN
# NNYN
# NNNN
# NYYN


# 6
# NNNNNN
# YNYNNY
# YNNNNY
# NNNNNN
# YNYNNN
# YNNYNN

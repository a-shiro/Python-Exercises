from queue import PriorityQueue


class Edge:
    def __init__(self, currency_1, currency_2, value):
        self.currency_1 = currency_1
        self.currency_2 = currency_2
        self.value = float(value)


edges = int(input())
graph = {}

for _ in range(edges):
    currency_1, currency_2, value = input().split()

    if currency_1 not in graph:
        graph[currency_1] = []

    if currency_2 not in graph:
        graph[currency_2] = []

    graph[currency_1].append(Edge(currency_1, currency_2, value))

target_destination = input()
break_counter = 0

priority_queue = PriorityQueue()
priority_queue.put((1, target_destination))

total_end_result_value = 1
node_to_put = ''
highest_value = 0

result_elements = []

while not priority_queue.empty():
    value, node = priority_queue.get()

    result_elements.append((total_end_result_value, node))

    if node == target_destination:
        break_counter += 1
        if break_counter == 2:
            break

    if not graph[node]:
        break

    for edge in graph[node]:
        if len(graph[node]) > 1:
            if highest_value < edge.value:
                highest_value = edge.value
                node_to_put = edge.currency_2
        else:
            highest_value = edge.value
            node_to_put = edge.currency_2

    new_price = abs(value) * highest_value

    total_end_result_value = new_price

    priority_queue.put((-total_end_result_value, node_to_put))


if total_end_result_value > 1:
    result = []
    print('True')
    for el in result_elements:
        result.append(el[1])

    print(*result)
else:
    print('False')
    for el in range(len(result_elements) - 1):
        print(f'{result_elements[el][1]}: {result_elements[el][0]:.3f}')

# 5
# GBP USD 1.27
# USD AUD 1.43
# USD NZD 1.51
# NZD AUD 0.95
# AUD GBP 0.55
# GBP

# 5
# GBP USD 1.27
# USD AUD 1.43
# USD NZD 1.51
# NZD AUD 0.95
# AUD GBP 0.50
# GBP

# 1
# GBP USD 1.27
# USD
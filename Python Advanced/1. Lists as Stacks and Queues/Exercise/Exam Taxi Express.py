from collections import deque


def start_matching(customers, taxis):
    total_time = 0

    while True:
        if not customers:
            return True, total_time
        elif not taxis:
            return False, None

        customer_time, taxi_gas = customers[0], taxis[-1]

        if taxi_gas < customer_time:
            taxis.pop()
            continue

        customers.popleft()
        taxis.pop()
        total_time += customer_time


customers = deque([int(c) for c in input().split(', ')])
taxis = [int(t) for t in input().split(', ')]

customers_satisfied, total_time = start_matching(customers, taxis)

if customers_satisfied:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(c) for c in customers])}')

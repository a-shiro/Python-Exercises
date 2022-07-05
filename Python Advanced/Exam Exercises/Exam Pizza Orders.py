from collections import deque


def make_pizzas(orders, employees):
    global total_pizzas

    while True:
        order, employee = orders[0], employees[-1]

        if order > 10:
            orders.popleft()

        elif order <= 0:
            orders.popleft()

        elif order <= employee:
            total_pizzas += order
            orders.popleft()
            employees.pop()

        else:
            total_pizzas += employee
            orders[0] -= employee
            employees.pop()

        if not orders:
            return True

        if not employees:
            return False


orders = deque([int(o) for o in input().split(', ')])
employees = [int(e) for e in input().split(', ')]

total_pizzas = 0

orders_completed = make_pizzas(orders, employees)

if orders_completed:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(map(str, employees))}')

else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, orders))}')


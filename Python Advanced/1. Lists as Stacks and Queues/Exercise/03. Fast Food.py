from collections import deque

food_quantity = int(input())
orders = deque(int(order) for order in input().split())
orders_complete = True
print(max(orders))

while orders:

    if orders[0] > food_quantity:
        orders_complete = False
        break
    else:
        food_quantity -= orders.popleft()

if orders_complete:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders))}")
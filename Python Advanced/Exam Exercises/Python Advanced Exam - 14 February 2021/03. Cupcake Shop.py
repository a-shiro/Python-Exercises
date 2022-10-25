from collections import deque


def stock_availability(inventory, command, *args):
    inventory = deque(inventory)

    if command == 'delivery':
        for item in args:
            inventory.append(item)

    elif command == 'sell':
        if len(args) == 1 and type(args[0]) == int:
            for _ in range(args[0]):
                inventory.popleft()
        elif len(args) >= 1:
            for item in args:
                while item in inventory:
                    inventory.remove(item)
        else:
            inventory.popleft()

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

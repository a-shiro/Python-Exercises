wagons = int(input())
train = [0] * wagons
command = input()

while not command == "End":
    data = command.split()

    if data[0] == "add":
        train[-1] += int(data[1])

    elif data[0] == "insert":
        train_index = int(data[1])
        train[train_index] += int(data[2])

    elif data[0] == "leave":
        train_index = int(data[1])
        train[train_index] -= int(data[2])

    command = input()

print(train)
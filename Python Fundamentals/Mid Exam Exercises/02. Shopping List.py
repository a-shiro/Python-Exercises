groceries = input().split("!")
command = input()

while True:
    if command == "Go Shopping!":
        break
    command = command.split()

    if len(command) == 2:
        command_name = command[0]
        item = command[1]
    elif len(command) == 3:
        command_name = command[0]
        item = command[1]
        item_2 = command[2]

    if command_name == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    elif command_name == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif command_name == "Correct":
        if item in groceries:
            index = groceries.index(item)
            groceries.insert(index, item_2)
            groceries.remove(item)

    elif command_name == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command = input()

print(", ".join(groceries))
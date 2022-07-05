inventory = input().split(", ")
command = input()

while not command == "Craft!":

    current_command, item = command.split(" - ")

    if current_command == "Collect":
        if item not in inventory:
            inventory.append(item)

    elif current_command == "Drop":
        if item in inventory:
            inventory.remove(item)

    elif current_command == "Combine Items":
            first_item = item[:item.index(":")]
            second_item = item[item.index(":") + 1:]
            if first_item in inventory:
                first_item_index = inventory.index(first_item)
                second_item_to_inventory = inventory.insert(first_item_index + 1, second_item)

    elif current_command == "Renew":
        if item in inventory:
            item_index_in_inventory = inventory.index(item)
            last_index_in_inventory = len(inventory) - 1
            item = inventory.pop(item_index_in_inventory)
            inventory.insert(last_index_in_inventory, item)

    command = input()

print(", ".join(inventory))
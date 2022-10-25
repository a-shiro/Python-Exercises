treasure_chest = input().split("|")
command = input().split()

while not command[0] == "Yohoho!":

    if command[0] == "Loot":
        for treasure in range(1, len(command)):
            if not command[treasure] in treasure_chest:
                treasure_chest.insert(0, command[treasure])

    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(treasure_chest):
            loot = treasure_chest.pop(int(command[1]))
            treasure_chest.append(loot)

    elif command[0] == "Steal":
        stolen_items = []
        stolen_counter = 0
        for loot in range(len(treasure_chest) - 1, -1, -1):
            stolen_items.append(treasure_chest[loot])
            treasure_chest.remove(treasure_chest[loot])
            stolen_counter += 1
            if stolen_counter == int(command[1]):
                break
            if treasure_chest == []:
                break
        if not stolen_items == []:
            print(", ".join(reversed(stolen_items)))

    command = input().split()

if treasure_chest == []:
    print("Failed treasure hunt.")

else:
    total_length = 0
    for loot in treasure_chest:
        total_length += len(loot)
    average_gains = total_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gains:.2f} pirate credits.")

# Diamonds
# Yohoho!
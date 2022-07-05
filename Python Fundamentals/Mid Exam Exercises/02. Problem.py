friends = input().split(", ")
command = input().split()

blacklisted_names = 0
lost_names = 0

while not command[0] == "Report":

    if command[0] == "Blacklist":
        if command[1] in friends:
            index = friends.index(command[1])
            blacklisted = friends.pop(index)
            friends.insert(index, "Blacklisted")
            print(f"{blacklisted} was blacklisted.")
            blacklisted_names += 1
        else:
            print(f"{command[1]} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friends):
            if not friends[index] == "Blacklisted":
                if not friends[index] == "Lost":
                    print(f"{friends[index]} was lost due to an error.")
                    friends.pop(index)
                    friends.insert(index, "Lost")
                    lost_names += 1

    elif command[0] == "Change":
        index = int(command[1])
        if 0 <= index < len(friends):
            current_name = friends.pop(index)
            new_name = command[2]
            friends.insert(index, new_name)
            print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(friends))
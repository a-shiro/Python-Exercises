neighborhood = [int(house) for house in input().split("@")]
command = input()

index_after_jump = 0
while not command == "Love!":
    command_name, jump_length = command.split()

    index_after_jump += int(jump_length)
    if index_after_jump > len(neighborhood) - 1:
        index_after_jump = 0

    if neighborhood[index_after_jump] == 0:
        print(f"Place {index_after_jump} already had Valentine's day.")

    else:
        neighborhood[index_after_jump] -= 2
        if neighborhood[index_after_jump] == 0:
            print(f"Place {index_after_jump} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {index_after_jump}.")

failed_count = 0
for house in neighborhood:
    if house > 0:
        failed_count += 1
if failed_count > 0:
    print(f"Cupid has failed {failed_count} places.")
else:
    print("Mission was successful.")


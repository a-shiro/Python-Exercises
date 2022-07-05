locations = input()

command = input().split(":")

while not command[0] == "Travel":

    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]

        if index in range(len(locations)):

            l_half = locations[:index] + string
            r_half = locations[index:]

            locations = l_half + r_half

    elif command[0] == "Remove Stop":
        start_i, end_i = int(command[1]), int(command[2])

        if start_i in range(len(locations)) and end_i in range(len(locations)):

            l_half = locations[:start_i]
            r_half = locations[end_i + 1:]

            locations = l_half + r_half

    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]

        if old_string in locations:
            locations = locations.replace(old_string, new_string)

    print(locations)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {locations}")

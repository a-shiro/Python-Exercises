activation_key = input()

command = input().split(">>>")

while not command[0] == "Generate":

    if command[0] == "Contains":
        substring = command[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":

        start_index, end_index = int(command[2]), int(command[3])

        if command[1] == "Lower":
            l_half = activation_key[:start_index]
            to_convert = activation_key[start_index:end_index].lower()
            r_half = activation_key[end_index:]

            activation_key = l_half + to_convert + r_half
            print(activation_key)
        elif command[1] == "Upper":
            l_half = activation_key[:start_index]
            to_convert = activation_key[start_index:end_index].upper()
            r_half = activation_key[end_index:]

            activation_key = l_half + to_convert + r_half
            print(activation_key)

    elif command[0] == "Slice":

        start_slice, end_slice = int(command[1]), int(command[2])

        l_half = activation_key[:start_slice]
        r_half = activation_key[end_slice:]
        activation_key = l_half + r_half
        print(activation_key)

    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
message = input()

command = input().split("|")

while not command[0] == "Decode":

    if command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]

        message = message.replace(substring, replacement)

    elif command[0] == "Insert":
        index, value = command[1], command[2]

        l_half = message[:int(index)] + value
        r_half = message[int(index):]

        message = l_half + r_half

    elif command[0] == "Move":
        number_l_to_move = command[1]

        l_half = message[:int(number_l_to_move)]
        r_half = message[int(number_l_to_move):]

        message = r_half + l_half

    command = input().split("|")

print(f"The decrypted message is: {message}")
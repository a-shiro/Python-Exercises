message = input()

command = input().split(":|:")

while not command[0] == "Reveal":

    if command[0] == "InsertSpace":
        index = int(command[1])

        l_half = message[:index] + " "
        r_half = message[index:]

        message = l_half + r_half

        print(message)
    elif command[0] == "Reverse":

        substring = command[1]

        if substring in message:
            index = message.find(substring)
            length = index + len(substring)

            l_half = message[:index]
            to_slice = message[index:length]
            r_half = message[length:]

            message = l_half + r_half + to_slice[::-1]

            print(message)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]

        message = message.replace(substring, replacement)

        print(message)

    command = input().split(":|:")

print(f"You have a new text message: {message}")
message = input()

command = input().split()

while not command[0] == "Finish":

    if command[0] == "Replace":
        current_char, new_char = command[1], command[2]
        message = message.replace(current_char, new_char)
        print(message)
    elif command[0] == "Cut":
        start_i, end_i = int(command[1]), int(command[2])

        if start_i in range(len(message)) and end_i in range(len(message)):
            l_half = message[:start_i]
            r_half = message[end_i + 1:]
            message = l_half + r_half
            print(message)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":

        if command[1] == "Upper":
            message = message.upper()
            print(message)
        elif command[1] == "Lower":
            message = message.lower()
            print(message)

    elif command[0] == "Check":
        searched = command[1]

        if searched in message:
            print(f"Message contains {searched}")
        else:
            print(f"Message doesn't contain {searched}")

    elif command[0] == "Sum":
        start_slice, end_slice = int(command[1]), int(command[2])

        if start_slice in range(len(message)) and end_slice in range(len(message)):
            sliced_word = message[start_slice:end_slice + 1]
            total = 0
            for char in sliced_word:
                total += ord(char)
            print(total)
        else:
            print("Invalid indices!")

    command = input().split()


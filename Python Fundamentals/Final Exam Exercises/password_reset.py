password = input()
raw_password = ""

command = input().split()

while not command[0] == "Done":

    if command[0] == "TakeOdd":

        raw_password = ""

        for i in range(len(password)):
            if i % 2 == 1:
                raw_password += password[i]

        password = raw_password
        print(password)

    elif command[0] == "Cut":

        index, length = int(command[1]), int(command[2])

        to_remove = password[index: index + length]
        password = password.replace(to_remove, "", 1)

        print(password)

    elif command[0] == "Substitute":

        substring, substitute = command[1], command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split()

print(f"Your password is: {password}")
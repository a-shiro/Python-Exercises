command_lines = int(input())

registered_dict = {}

for _ in range(command_lines):

    command = input().split()

    if command[0] == "register":
        if command[1] not in registered_dict.keys():
            registered_dict[command[1]] = command[2]
            print(f"{command[1]} registered {registered_dict[command[1]]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_dict[command[1]]}")

    elif command[0] == "unregister":
        if command[1] not in registered_dict.keys():
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            del registered_dict[command[1]]

for key, value in registered_dict.items():
    print(f"{key} => {value}")


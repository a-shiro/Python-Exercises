message_capacity = int(input())

users = {}

command = input().split("=")

while not command[0] == "Statistics":

    if command[0] == "Add":
        username, sent, received = command[1], int(command[2]), int(command[3])

        if username not in users.keys():
            users[username] = {"sent": sent, "received": received}

    elif command[0] == "Message":
        sender, receiver = command[1], command[2]

        if sender in users.keys() and receiver in users.keys():

            users[sender]["sent"] += 1
            users[receiver]["received"] += 1

            if users[sender]["sent"] + users[sender]["received"] == message_capacity:
                users.pop(sender)
                print(f"{sender} reached the capacity!")
            if users[receiver]["sent"] + users[receiver]["received"] == message_capacity:
                users.pop(receiver)
                print(f"{receiver} reached the capacity!")

    elif command[0] == "Empty":
        user = command[1]

        if user == "All":
            users.clear()
        elif user in users.keys():
            users.pop(user)

    command = input().split("=")

users = sorted(users.items(), key=lambda x: (-x[1]["received"], x[0]))

print(f"Users count: {len(users)}")
for tup in users:

    name, sent, received = tup[0], tup[1]['sent'], tup[1]['received']

    print(f"{name} - {sent + received}")


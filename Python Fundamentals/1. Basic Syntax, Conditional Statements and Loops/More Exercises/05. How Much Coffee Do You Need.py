command = input()
coffee_count = 0
activities = ["coding", "dog", "cat", "movie", "CODING", "DOG", "CAT", "MOVIE"]
while not command == "END":

    if command.islower() and command in activities:
        coffee_count += 1
    elif command.isupper() and command in activities:
        coffee_count += 2

    if coffee_count > 5:
        break

    command = input()

if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
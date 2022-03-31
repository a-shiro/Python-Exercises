lenght_of_cake = int(input())
width_of_cake = int(input())

total_cake = lenght_of_cake * width_of_cake

pieces_of_cake = input()
while pieces_of_cake != "STOP":
    pieces_of_cake = int(pieces_of_cake)

    if total_cake < pieces_of_cake:
        break
    total_cake -= pieces_of_cake

    pieces_of_cake = input()


if pieces_of_cake == "STOP":
    piece_number = total_cake
    print(f"{piece_number} pieces are left.")

else:
    print(f"No more cake left! You need {pieces_of_cake - total_cake} pieces more.")


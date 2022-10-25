num_pieces = int(input())

pieces_dict = {}
for i in range(num_pieces):

    piece, composer, key = input().split("|")
    pieces_dict[piece] = [composer, key]

command = input().split("|")

while not command[0] == "Stop":

    if command[0] == "Add":

        piece, composer, key = command[1], command[2], command[3]

        if piece not in pieces_dict.keys():
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":

        piece = command[1]

        if piece in pieces_dict:
            print(f"Successfully removed {piece}!")
            del pieces_dict[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":

        piece, new_key = command[1], command[2]

        if piece in pieces_dict:
            del pieces_dict[piece][1]
            pieces_dict[piece].append(new_key)
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input().split("|")

pieces_dict = sorted(pieces_dict.items(), key=lambda x: x[0])

for tup in pieces_dict:
    piece, composer, key = tup[0], tup[1][0], tup[1][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
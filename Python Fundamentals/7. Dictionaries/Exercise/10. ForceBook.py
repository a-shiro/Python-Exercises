def change_user_side(user, side): # 1.Change Side

    for key in sides_n_users_dict.keys():
        if user in sides_n_users_dict[key]:
            user = sides_n_users_dict[key].pop(sides_n_users_dict[key].index(user))
            if side not in sides_n_users_dict.keys():
                sides_n_users_dict[side] = []
            sides_n_users_dict[side].append(user)
            return True


def add_user_to_existing_side(user, side): # 2.Adds user to Existing Side if he isnt in any side.

    not_in = True
    if side not in sides_n_users_dict.keys():
        return False

    for key in sides_n_users_dict.keys():
        if user in sides_n_users_dict[key]:
            not_in = False

    if not_in:
        sides_n_users_dict[side].append(user)
        return True


def add_new_side_n_user(user, side): # 3.Adds new side and a new user.
    sides_n_users_dict[side] = []
    sides_n_users_dict[side].append(user)
    return True


def is_not_unique(user):
    for key in sides_n_users_dict.keys():
        if user in sides_n_users_dict[key]:
            return True


side_and_user = input()

sides_n_users_dict = {}

while not side_and_user == "Lumpawaroo":

    if "|" in side_and_user:
        side, user = side_and_user.split(" | ")

        if is_not_unique(user):
            side_and_user = input()
            continue

        if side not in sides_n_users_dict.keys():
            sides_n_users_dict[side] = []

        if user not in sides_n_users_dict[side]:
            sides_n_users_dict[side].append(user)

    elif " -> " in side_and_user:
        user, side = side_and_user.split(" -> ")

        if change_user_side(user, side):
            print(f"{user} joins the {side} side!")

        elif add_user_to_existing_side(user, side):
            print(f"{user} joins the {side} side!")

        elif add_new_side_n_user(user, side):
            print(f"{user} joins the {side} side!")

    side_and_user = input()

for side, users in sorted(sides_n_users_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if not len(users) == 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
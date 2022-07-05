cards = input()

my_list = cards.split(" ")

team_a = 11
team_b = 11

current_card = ""
previous_card = ""

flag = False


for i in range(len(my_list) - 1, -1, -1):
    if team_a < 7 or team_b < 7:
        flag = True
        break

    card = my_list[i]
    if "A" in card:
        team_a -= 1

    elif "B" in card:
        team_b -= 1

print(f"Team A - {team_a}; Team B - {team_b}")
if flag:
    print("Game was terminated")
import sys

easter_bread_count = int(input())

highest_score = -sys.maxsize
best_chef = ""

for each_easter_bread in range(easter_bread_count):

    current_score= 0

    bread_maker = input()
    command = input()
    while command != "Stop":
        score = int(command)
        current_score += score

        command = input()
    print(f"{bread_maker} has {current_score} points.")

    if current_score > highest_score:
        best_chef = bread_maker
        highest_score = current_score
        print(f"{bread_maker} is the new number 1!")


print(f"{best_chef} won competition with {highest_score} points!")

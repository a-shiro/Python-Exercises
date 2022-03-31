lines = int(input())

balanced = True
bracket_list = []

for _ in range(lines):

    string = input()

    if string == "(" or string == ")":
        bracket_list.append(string)

for i in range(0, len(bracket_list), 2):
    if len(bracket_list) % 2 == 1:
        balanced = False
        break

    bracket_1 = bracket_list[i]
    bracket_2 = bracket_list[i + 1]

    if bracket_1 == bracket_2:
        balanced = False
        break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


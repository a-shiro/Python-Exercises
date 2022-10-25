n = int(input())

number = 0
current_number = 1
is_current_bigger_than_n = False

for rows in range(1, n + 1):
    for columns in range(1, rows + 1):
        number += 1
        current_number = number
        if current_number > n:
            is_current_bigger_than_n = True
            break
        print(number, end =" ")

    if is_current_bigger_than_n == True:
        break
    print()

